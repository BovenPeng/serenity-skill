#!/usr/bin/env python3
"""Generate a Serenity single-company note with ModelHub Chat Completions.

The script reads an existing evidence note, calls ModelHub once per required
section, and assembles a Markdown note. It never prints or writes API keys.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import sys
import time
import urllib.error
import urllib.request


DEFAULT_BASE_URL = "https://aidp.bytedance.net/api/modelhub/online/v2/crawl"
DEFAULT_MODEL = "gpt-5.5-2026-04-24"
DEFAULT_API_VERSION = "2024-03-01-preview"

SECTIONS = [
    ("1", "产业链位置"),
    ("2", "供需与涨价/产能/扩产"),
    ("3", "主营业务、客户与订单证据"),
    ("4", "上下游财报影响"),
    ("5", "跨市场同类股票与最近 30 日涨跌幅"),
    ("6", "股东人数、流通市值、总市值"),
    ("7", "结论与降级条件"),
]


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        if key.startswith(("MODELHUB_", "ASUKAQT_CODEX_MODELHUB_")):
            os.environ.setdefault(key, value)


def env_value(*names: str, default: str | None = None) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return default


def modelhub_config() -> dict[str, str]:
    load_env_file(Path.home() / ".codex" / ".env")
    load_env_file(Path.cwd() / ".env")

    api_key = env_value("MODELHUB_API_KEY", "ASUKAQT_CODEX_MODELHUB_API_KEY")
    if not api_key:
        raise SystemExit(
            "Missing MODELHUB_API_KEY or ASUKAQT_CODEX_MODELHUB_API_KEY. "
            "Set it outside Git before running."
        )

    return {
        "api_key": api_key,
        "base_url": env_value(
            "MODELHUB_BASE_URL",
            "ASUKAQT_CODEX_MODELHUB_BASE_URL",
            default=DEFAULT_BASE_URL,
        ),
        "model": env_value(
            "MODELHUB_MODEL",
            "ASUKAQT_CODEX_MODELHUB_MODEL",
            default=DEFAULT_MODEL,
        ),
        "api_version": env_value(
            "MODELHUB_API_VERSION",
            "ASUKAQT_CODEX_MODELHUB_API_VERSION",
            default=DEFAULT_API_VERSION,
        ),
    }


def chat_completion(
    *,
    config: dict[str, str],
    messages: list[dict[str, str]],
    max_completion_tokens: int,
    retries: int,
    retry_sleep: float,
) -> tuple[str, dict[str, object]]:
    base_url = config["base_url"].rstrip("/")
    model = config["model"]
    api_version = config["api_version"]
    url = (
        f"{base_url}/openai/deployments/{model}/chat/completions"
        f"?api-version={api_version}"
    )
    payload = {
        "messages": messages,
        "max_completion_tokens": max_completion_tokens,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "api-key": config["api_key"],
        },
        method="POST",
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    last_error = ""
    for attempt in range(1, retries + 1):
        try:
            with opener.open(request, timeout=120) as response:
                raw = response.read().decode("utf-8")
            result = json.loads(raw)
            choice = result.get("choices", [{}])[0]
            content = choice.get("message", {}).get("content", "")
            if not content.strip():
                last_error = f"empty content, response id={result.get('id', '<unknown>')}"
                raise RuntimeError(last_error)
            meta = {
                "id": result.get("id"),
                "model": result.get("model", model),
                "usage": result.get("usage", {}),
                "finish_reason": choice.get("finish_reason"),
            }
            return content.strip(), meta
        except urllib.error.HTTPError as exc:
            body = exc.read(500).decode("utf-8", "replace").replace("\n", " ")
            last_error = f"HTTP {exc.code}: {body}"
        except Exception as exc:  # noqa: BLE001 - CLI should report concise failure.
            last_error = f"{type(exc).__name__}: {exc}"
        if attempt < retries:
            time.sleep(retry_sleep)

    raise RuntimeError(f"ModelHub request failed after {retries} attempts: {last_error}")


def build_messages(
    *,
    title: str,
    section_no: str,
    section_name: str,
    evidence: str,
) -> list[dict[str, str]]:
    system = (
        "你是 Serenity 风格的中文投资研究助手。"
        "只基于用户提供的证据包写研究辅助材料，不给买卖指令，不承诺收益，"
        "不编造客户、供应商、股价、市值、财务数据或来源。"
    )
    section_rules = ""
    if section_no == "3":
        section_rules = """
第 3 节额外要求：
- 必须按主营业务/产品线给出客户与订单证据矩阵，字段至少包含：业务/产品线、收入或占比、客户名称、订单量、订单金额、证据来源、证据状态/缺口。
- 客户名称、订单量、订单金额只能来自证据包里的财报、公告、官方 IR、招投标/中标、客户认证、客户侧文件或已证实新闻。
- 如果证据包没有披露某业务客户、订单量或订单金额，必须写“未披露”；如果只是传闻、推断或下游 proxy，必须写“未证实”或“需求侧 proxy”，不能当作已确认客户。
- 不得把“头部客户”“主流晶圆厂”“国内外领先客户”改写成具体公司名。
"""
    user = f"""请生成《{title}》的第 {section_no} 节。

输出要求：
- 只输出这一节 Markdown，以 `## {section_no}. {section_name}` 开头。
- 使用中文，保留必要的英文缩写和代码值，例如 Tushare、THS、PE_TTM、PB、688012.SH。
- 只能使用证据包中已有的数据、公司、来源和 URL；证据不足时写“需核实”或“未见明确披露”。
- 不新增 Obsidian wikilink；如需写中微公司，只用普通文本“中微公司”。
- 结论要把事实映射成“利好 / 利空 / 中性 / 需核实”，不要只罗列新闻。
- 研究辅助，不写买入、卖出、仓位、目标价或收益承诺。
{section_rules}

证据包如下：
<<<EVIDENCE
{evidence}
EVIDENCE
"""
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def backup_output(output: Path, backup_dir: Path | None) -> Path | None:
    if not output.exists():
        return None
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    if backup_dir is None:
        backup_dir = output.parent / ".modelhub-backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / f"{output.stem}.{stamp}{output.suffix}"
    shutil.copy2(output, backup_path)
    return backup_path


def assemble_note(
    *,
    title: str,
    generated_at: str,
    model: str,
    source_note_label: str,
    sections: list[str],
    metas: list[dict[str, object]],
) -> str:
    section_ids = ", ".join(str(meta.get("id")) for meta in metas if meta.get("id"))
    body = "\n\n".join(section.strip() for section in sections)
    return f"""---
title: {title}
company: 中微公司
ts_code: 688012.SH
framework: Serenity company supply-demand checkup
generated_by: ModelHub API
generated_at: {generated_at}
用途: 研究辅助
---

# {title}

> 本文由 ModelHub Chat Completions API 按 Serenity “公司产业链供需体检”清单逐节生成。证据包来自 `{source_note_label}` 及其中列出的公开财报、业绩公告和本地行情快照；未重新写入 API key，也不构成投资建议。

关联主档：[[THS Full Stock - 688012.SH 中微公司|中微公司]]

相关行业：[[THS Full Parent - 881121.TI 半导体|半导体]]、[[THS Full Child - 884229.TI 半导体设备|半导体设备]]

ModelHub 调用：模型 `{model}`；逐节生成请求数 `{len(metas)}`；请求 id `{section_ids}`。

{body}

## 生成边界与回滚

- 本文是 ModelHub API 逐节生成版本，交易决策仍由用户自行负责。
- 本文没有修改中微公司的主股票档。
- 如需回滚本次替换，恢复同目录 `.modelhub-backups/` 中对应时间戳备份即可。
"""


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a ModelHub-backed Serenity company analysis note."
    )
    parser.add_argument("--company", default="中微公司")
    parser.add_argument("--ts-code", default="688012.SH")
    parser.add_argument("--title", default=None)
    parser.add_argument("--evidence-note", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--backup-dir", type=Path, default=None)
    parser.add_argument("--max-completion-tokens", type=int, default=2800)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-sleep", type=float, default=3.0)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.evidence_note.exists():
        raise SystemExit(f"Evidence note not found: {args.evidence_note}")

    title = args.title or f"{args.company} - ModelHub Serenity 供需链路分析 - {dt.date.today().isoformat()}"
    evidence = args.evidence_note.read_text(encoding="utf-8")
    config = modelhub_config()

    generated_sections: list[str] = []
    metas: list[dict[str, object]] = []
    for section_no, section_name in SECTIONS:
        print(f"generating section {section_no}: {section_name}", file=sys.stderr)
        content, meta = chat_completion(
            config=config,
            messages=build_messages(
                title=title,
                section_no=section_no,
                section_name=section_name,
                evidence=evidence,
            ),
            max_completion_tokens=args.max_completion_tokens,
            retries=args.retries,
            retry_sleep=args.retry_sleep,
        )
        generated_sections.append(content)
        metas.append(meta)

    generated_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    backup_path = backup_output(args.output, args.backup_dir)
    source_note_label = str(args.evidence_note)
    try:
        if backup_path and args.evidence_note.resolve() == args.output.resolve():
            source_note_label = str(backup_path)
    except FileNotFoundError:
        pass

    note = assemble_note(
        title=title,
        generated_at=generated_at,
        model=config["model"],
        source_note_label=source_note_label,
        sections=generated_sections,
        metas=metas,
    )

    args.output.write_text(note, encoding="utf-8")

    result = {
        "output": str(args.output),
        "backup": str(backup_path) if backup_path else None,
        "model": config["model"],
        "section_count": len(generated_sections),
        "request_ids": [meta.get("id") for meta in metas],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
