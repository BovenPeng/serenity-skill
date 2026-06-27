# Concept To Chain Framework

Use this file when the user asks to explain a market concept, list related stocks, split a theme into sub-sectors, or locate a company inside a concept or value chain.

This is a reusable reasoning shape, not a fixed industry database. Power semiconductors, PCB, optical communication, semiconductor equipment, copper links, liquid cooling, robotics, and other themes should all follow the same structure before moving into security-specific research.

## Core Idea

Start from the user's concept and turn it into an investable map:

`concept explanation -> adjacent concept boundary -> value-chain layers -> product or technology routes -> demand drivers -> cross-market company universe -> sub-sector priority -> single-company positioning -> evidence gaps`

The goal is to help the user understand where a company really sits, how it makes money, what demand can pull it, and what evidence is still missing.

Do not treat a concept label as proof. A company is relevant only after its filings, announcements, IR materials, product disclosures, or customer evidence show real exposure.

## Output Shape

For concept questions, use these sections unless the user asks for a shorter answer:

1. **一句话解释**
   - Use one concrete analogy. The analogy should separate the concept from adjacent technologies.
   - Example shape: "If X is responsible for [visible function], Y is responsible for [less visible but critical physical/economic function]."

2. **它和相邻概念的区别**
   - State what this concept is not.
   - Separate devices, materials, equipment, modules, software, systems, and end applications when they are often mixed together.
   - If a term is a broad market theme rather than a product category, say so.

3. **产业链分层**
   - Map upstream to downstream in a simple chain.
   - Keep layers granular enough to locate companies: materials, components, process equipment, modules, system integrators, end customers.
   - Mark which layers are closer to the real scaling constraint.

4. **产品或技术路线对比**
   - Split the concept into the key product or technology routes.
   - Compare `用途 / 性能或约束 / 成本或成熟度 / 典型应用 / 代表公司候选`.
   - Do not imply a route is superior in all cases. Tie it to the application.

5. **为什么当前需求会拉动它**
   - Explain the system change: AI, EV, solar, storage, robotics, industrial automation, consumer electronics, policy, or another driver.
   - Translate the driver into a physical or economic constraint: power, bandwidth, heat, latency, yield, purity, voltage, cycle time, reliability, capex, or certification.
   - State which value-chain layers benefit first and which are only downstream beneficiaries.

6. **跨市场公司地图**
   - Build a candidate universe by market only after the chain is clear.
   - Use market labels precisely: A-share, HK, US-listed, ADR/OTC, Europe, Japan, Korea, Taiwan.
   - Treat the list as a research universe, not a recommendation list.
   - If a company is a conglomerate or only partly exposed, label the exposure as partial and require segment proof.

7. **细分赛道排序**
   - Rank sub-sectors before ranking stocks.
   - Rank by demand urgency, closeness to bottleneck, supplier concentration, expansion difficulty, evidence quality, valuation pressure, and failure risk.
   - State at least one crowded or obvious area that may rank lower and why.

8. **个股产业链定位**
   - For any named company, answer:
     - It sits in which layer?
     - Which product or technology route does it map to?
     - How does it make money in this chain?
     - Which downstream demand can pull it?
     - What evidence proves real exposure?
     - What evidence is still missing?
     - What would make the concept exposure weak or wrong?

## Company Map Table

Use this compact table when the user asks "有哪些公司":

| 市场 | 公司 | 候选产业链层级 | 可能相关产品/业务 | 主要下游 | 证据状态 | 主要风险 |
|---|---|---|---|---|---|---|

Rules:

- `证据状态` should be one of `已由财报/公告验证`, `需核实收入占比`, `仅主题相关`, or `不确定`.
- Avoid presenting candidates as final picks.
- For current stock lists, use live sources when available. If not checked, say which filings or data sources should be checked next.

## Technology Route Table

Use this table when the concept contains multiple product routes:

| 路线 | 解决什么问题 | 优势 | 限制 | 典型应用 | 候选公司层级 |
|---|---|---|---|---|---|

The table should explain why different routes coexist. A mature route can still be attractive if the demand is large and evidence is strong. A newer route can still be risky if adoption, cost, yield, or qualification is weak.

## Single-Company Positioning Template

For a named company inside a concept, use this structure before deeper financial analysis:

```text
结论先行：
[公司] 更像是 [产业链层级] 的 [产品/技术路线] 公司，而不是 [容易混淆的概念]。它是否真正受益，关键看 [证据点 1]、[证据点 2]、[证据点 3]。

产业链位置：
- 上游：
- 公司所在层：
- 下游：

主营暴露：
- 已披露收入或利润占比：
- 未披露但需要验证：
- 只是概念标签的部分：

需求驱动：
- 利好：
- 中性：
- 利空或需核实：

下一步证据：
- 财报/公告：
- 客户或订单：
- 产能/认证：
- 同业或上下游交叉验证：
```

## Evidence Rules

- Use company filings, exchange announcements, annual/interim/quarterly reports, investor presentations, earnings calls, official product pages, tenders, customer certification, and credible industry sources.
- For A-shares, check annual reports, interim reports, quarterly reports, exchange Q&A, interactive platforms, project filings, patents, receivables, inventory, contract liabilities, and operating cash flow.
- For cross-market maps, use local source paths from `references/market-source-playbook.md`.
- If the user asks for current prices, recent returns, market cap, or latest company lists, verify with live market data or clearly mark the gap.
- Do not give buy/sell commands, target prices, or guaranteed return language.

## Example Use

Power semiconductor can be used as an example of this framework, but it must not become the hard-coded pattern.

The useful abstraction from that example is:

- explain the concept by contrasting invisible infrastructure with visible headline chips;
- split the chain into upstream input, core product, control layer, and end system;
- compare product routes by use case rather than hype level;
- show why AI, EV, solar, storage, robotics, or industrial demand changes the physical constraint;
- list companies by market as a candidate universe;
- rank sub-sectors first, then map individual companies to the layer where they truly earn money.
