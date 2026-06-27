# Serenity.skill Prompt Pack

Use these prompts when you want to start quickly.

## Deep theme research

```text
Use serenity-skill to deeply research [market] [theme].
Map the value chain, investigate current sources, find the scarce layers,
build a broad candidate universe, rank the top research priorities, explain what each company constrains,
explain the evidence, and say what could prove each idea wrong.
```

## A-share scan

```text
用 serenity-skill 深度调研现在 A 股 [行业/主题]。
请联网查公告、财报、问询函、互动易、招投标、环评/能评、专利、客户认证和财务质量，
先排产业链层级，再找 5 个最值得优先研究的标的，并说明卡住的环节、产业链位置、证据、排序理由和主要风险。
```

## Hong Kong scan

```text
用 serenity-skill 研究港股 [主题]。
重点过滤流动性、配售融资、关联交易、内地政策暴露、南向资金和估值重新定价条件。
给出优先研究排序和下一步核验路径。
```

## US scan

```text
Use serenity-skill to research US-listed [theme] companies.
Check SEC filings, transcripts, customer concentration, financing risk, margin evidence,
and the parts of the value chain investors may be underpricing.
```

## Single-company challenge

```text
Use serenity-skill to challenge [company/ticker].
Where does it sit in the value chain? Does it control a scarce layer?
What evidence supports the idea, what evidence is missing, and what would weaken the judgment?
```

## Concept to value chain

```text
用 serenity-skill 解释 [概念]：
先用一句话讲清楚它是什么，再说明它和相邻概念的区别，按产业链拆成上游/核心产品/模块或系统/下游应用，比较关键产品或技术路线，解释 AI/EV/光伏/储能/机器人/工业自动化等需求为什么会拉动它，并列出 A股/美股或ADR/韩股/日股等相关公司候选 universe。
最后先排细分赛道景气度，不要直接给买卖建议。功率半导体可以作为示例，但这个框架要能迁移到 PCB、光通信、半导体设备等概念。
```

## Company in concept chain

```text
用 serenity-skill 分析 [公司/股票代码] 在 [概念/产业链] 中是哪一环：
判断它属于上游材料、设备、核心器件、模块、系统集成、下游客户还是仅主题相关；拆它靠什么业务赚钱，收入或利润是否真实暴露，受哪些需求拉动，需要哪些财报、公告、客户、订单或产能证据验证，以及什么情况说明这个概念暴露不成立。
```

## Sub-sector ranking

```text
用 serenity-skill 把 [概念] 的细分赛道按景气度排序：
先拆技术路线和产业链层级，再按需求强度、供给扩张难度、客户认证、收入兑现、竞争格局、估值压力和失败条件排序。每层给代表公司候选和下一步验证证据。
```

## Company supply-demand checkup

```text
用 serenity-skill 对 [公司/股票代码] 做公司产业链供需体检：
1. 梳理产业链上下游，判断它在其中哪一环；
2. 判断这一环是否存在涨价、产能不足、扩产困难；
3. 拆主营业务和业绩占比，识别是否有 AI 产业链转型业务及占比提升可能；
4. 真实联网抓取供给侧和需求侧上下游公司的最新公告、年报、季报或业绩材料，提取 capex、订单、库存、毛利、现金流、指引等信号，并判断对公司的利好/利空/中性/需核实；
5. 列出美股、A 股、韩股、日股同类或同细分方向股票，并计算最近 30 日涨跌幅；
6. 给出股东人数、流通市值、总市值。
请标注证据来源、缺口和什么情况说明判断错了。
```

## ModelHub generated company note

```text
用 serenity-skill 先完成 [公司/股票代码] 的公开证据包，然后通过 ModelHub API 逐节生成并替换 Obsidian 分析笔记。
要求：覆盖产业链位置、供需和扩产、主营业务与 AI 链条、上下游财报影响、跨市场同类股票 30 日涨跌幅、股东人数/流通市值/总市值、结论与降级条件；覆盖前先备份旧笔记，不修改股票主档，不写入 API key。
```

## Compare candidates

```text
Use serenity-skill to compare [A], [B], and [C].
Rank them by supply-chain position, evidence quality, customer urgency, valuation pressure,
main risk, and next verification step.
```

## Research partner mode

```text
用 serenity-skill 陪我讨论 [主题/公司]。
不要直接写报告，每轮先给判断，再问我一个最关键的问题，带我从故事拆到产业链卡点和证据。
```

## Scorecard

```text
Use serenity-skill's local scorecard to score [company].
Explain every rating in plain language and mark the evidence as strong, medium, weak, or needs checking.
```
