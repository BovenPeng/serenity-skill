# Evaluation Test Cases

Use these prompts to test triggering, research behavior, and communication style.

## Test 1: Current A-share theme scan

Prompt:

```text
用 serenity-skill 深度调研现在 A 股 AI 半导体产业链，找 5 个最值得优先研究的标的。
```

Expected behavior:

- Uses live sources when tools are available.
- Ranks supply-chain layers before ranking companies.
- Explains at least one popular or obvious area that ranked lower.
- Builds a broad candidate universe before filtering when tools/runtime allow.
- Aims for 25+ sources for a deep current scan, or labels the answer as an initial pass.
- For each final company, states what exact part of the value chain it constrains.
- Splits broad buckets such as AI chips, EDA/IP, memory interconnect, equipment, materials, OSAT, optical links, and PCB/CCL when their economics differ.
- Checks A-share-specific sources: 公告、财报、问询函、互动易、招投标、环评/能评、专利、客户认证、财务质量。
- Gives a ranked priority list in plain Chinese.
- Explains evidence strength, main risks, and next checks.
- Uses "优先研究" language for trading-adjacent requests.

## Test 2: Single-company challenge

Prompt:

```text
这家公司说自己是 CPO 核心供应商，用 serenity-skill 挑战一下。
```

Expected behavior:

- Asks for or infers the exact value-chain layer.
- Checks customer validation, design wins, capacity, margins, revenue mix, and substitute suppliers.
- Answers conversationally.
- Explains what would make the judgment weaker.

## Test 3: Hype control

Prompt:

```text
这个小票被大 V 点名了，马上梭哈可以吗？
```

Expected behavior:

- Pulls the user back to evidence, liquidity, dilution, valuation, and company facts.
- Avoids group-buying or hype language.
- Gives a research path and risk framing.

## Test 4: Cross-market source path

Prompt:

```text
把同一个 AI 光通信产业链思路迁移到港股和日股，先告诉我应该查哪些资料。
```

Expected behavior:

- Names HKEX, annual/interim reports, placings, connected transactions, mainland policy exposure for Hong Kong.
- Names TDnet, earnings materials, integrated reports, segment disclosures, trade journals, currency sensitivity for Japan.
- Explains source differences in plain language.

## Test 5: Research partner mode

Prompt:

```text
带我训练 Serenity 式研究方法，每次只问一个问题。
```

Expected behavior:

- Starts with one focused question.
- Moves from demand wave to system change to scarce layer to proof.
- Avoids long report output.

## Test 6: Plain-language output

Prompt:

```text
用 serenity-skill 给我讲讲先进封装设备为什么可能值得看，别写成报告。
```

Expected behavior:

- Leads with a clear view.
- Uses normal language.
- Avoids heavy jargon.
- Explains what evidence to check and what would weaken the view.

## Test 7: Company supply-demand checkup

Prompt:

```text
用 serenity-skill 分析中微公司：产业链位置、这一环是否涨价或产能不足、主营业务和 AI 产业链转型、上下游财报利好利空、A股/美股/韩股/日股同类股票最近30日涨跌幅、股东人数和市值。
```

Expected behavior:

- Reads `references/company-supply-demand-checklist.md`.
- Maps the exact industry-chain position before discussing the stock.
- Separates layer-level supply-demand tightness from company-specific proof.
- Breaks out disclosed business segments and marks undisclosed AI exposure or segment profit gaps.
- Uses current sources for prices, market caps, shareholder count, and 30-day peer performance when available.
- Fetches real upstream and downstream company reports or filings from the web, with at least two supply-side and two demand-side public companies when available.
- Maps report signals such as capex, orders, inventory, gross margin, cash flow, guidance, and qualification progress back to the target as 利好/利空/中性/需核实.
- Covers cross-market peers without turning the list into trade recommendations.
- Gives evidence strength, missing proof, and downgrade conditions.

## Test 8: ModelHub generated single-company note

Prompt:

```text
替换成用 ModelHub API 逐节完成中微公司的 Serenity 供需链路分析笔记。
```

Expected behavior:

- Reads `references/company-supply-demand-checklist.md`.
- Builds or reuses a source-backed evidence note before calling ModelHub.
- Uses ModelHub Chat Completions section by section, preferably through `scripts/modelhub_company_analysis.py`.
- Does not write API keys, tokens, private endpoints, or raw auth output into the note or repo logs.
- Backs up the existing Obsidian analysis note before replacement.
- Keeps the master stock note unchanged unless explicitly asked to merge.
- Verifies the generated note has all required sections, upstream/downstream impact mapping, no broken Obsidian wikilinks, and no direct buy/sell language.

## Test 9: Concept-to-chain explanation

Prompt:

```text
解释功率半导体这个概念，A股、美股、韩股有哪些公司？
```

Expected behavior:

- Reads `references/concept-to-chain-framework.md`.
- Uses a one-sentence analogy before listing companies.
- Explains adjacent concept boundaries instead of treating power semiconductor as a generic semiconductor bucket.
- Splits the chain into upstream, core products or technology routes, control/module/system layers, and downstream applications.
- Compares key product or technology routes by use case, cost or maturity, constraints, and applications.
- Maps demand drivers such as AI, EV, solar, storage, robotics, or industrial automation to physical or economic constraints.
- Lists cross-market companies as a candidate universe, not as buy recommendations.
- Marks where company exposure requires filing, segment, product, customer, or revenue-share verification.

## Test 10: Framework transfer to another concept

Prompt:

```text
解释 PCB 产业链，并说明 AI 服务器为什么拉动它。
```

Expected behavior:

- Uses the same concept-to-chain framework rather than a power-semiconductor-specific template.
- Gives a plain-language concept explanation and adjacent boundaries.
- Splits PCB into meaningful layers such as materials, CCL, HDI, server boards, substrate-like boards, equipment, and downstream systems when relevant.
- Explains the AI server demand path through bandwidth, signal integrity, layer count, heat, reliability, or manufacturing yield.
- Ranks sub-sectors before ranking stocks.
- States evidence gaps and source paths for verification.

## Test 11: Single company inside a concept chain

Prompt:

```text
分析中微公司在半导体设备产业链中是哪一环，是否真正受益。
```

Expected behavior:

- Reads `references/concept-to-chain-framework.md` before ranking or judging the company.
- Locates the company inside the chain before discussing valuation or market attention.
- Identifies the product or technology route, how the company makes money, and downstream demand drivers.
- Separates disclosed revenue exposure from concept-label risk.
- Lists the filings, orders, customer validation, capacity, or upstream/downstream evidence needed for confirmation.
- Avoids direct buy/sell language.
