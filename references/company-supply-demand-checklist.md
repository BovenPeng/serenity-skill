# Company Supply-Demand Checklist

Use this file when a user asks for a single-company checkup that includes industry-chain position, supply-demand tightness, price increases, capacity shortages, expansion difficulty, revenue mix, AI-chain transition, upstream/downstream report impact, cross-market peers, recent performance, shareholder count, float market cap, or total market cap.

Keep the analysis grounded in public evidence. Do not turn "AI exposure" or "scarce layer" into a conclusion unless filings, company disclosures, customer evidence, or reliable industry sources support it.

## Required Output Shape

For a full company checkup, answer in these sections:

1. **产业链位置**
   - State the company's exact upstream/downstream position.
   - Name the scarce layer it controls, supplies, or only benefits from.
   - Link the position to customer capex, manufacturing process, component, material, equipment, software, or infrastructure constraints.

2. **供需与涨价/产能/扩产**
   - Check whether this layer shows price increases, tight capacity, long lead times, high utilization, customer prepayments, capacity reservations, order backlog, certification queues, permits, or specialized equipment bottlenecks.
   - Separate layer-level tightness from company-specific proof.
   - State "未见强证据" when only the theme is strong but company-level proof is missing.

3. **主营业务与 AI 产业链转型**
   - Break down revenue and profit by disclosed business segment.
   - If segment profit is not disclosed, state that and use revenue, gross margin, or qualitative disclosures instead.
   - Identify AI-chain exposure only when supported by filings, product disclosures, customers, or industry-chain logic.
   - Estimate whether the AI-related share can rise from demand-side pull and supply-side constraints. Label any estimate as qualitative unless a company disclosure gives numbers.

4. **上下游财报影响**
   - Actively identify upstream supply-side companies and downstream demand-side companies from the target's filings, customer/supplier disclosures, industry-chain logic, and public peers.
   - Fetch current public filings or reports from the web for those companies. Use annual reports, interim reports, quarterly reports, earnings releases, exchange announcements, SEC 10-K/10-Q/8-K, HKEX filings, TDnet materials, DART filings, company IR decks, transcripts, or official press releases.
   - Minimum standard: check at least two supply-side and two demand-side public companies when the chain has available listed companies. If fewer are available or sources cannot be fetched, state the exact gap.
   - Extract report signals that can affect the target company: capex expansion, order backlog, utilization, pricing, gross margin, inventory digestion, cash conversion, customer qualification progress, purchasing cadence, supplier lead time, and segment guidance.
   - Look for negative signals: order cuts, margin pressure, slower capex, inventory build, receivable stress, weak operating cash flow, delivery delays, substitute technologies, or customers reducing tool spend.
   - Map every upstream/downstream signal back to the target as `利好`, `利空`, `中性`, or `需核实`; do not leave the report facts as an unconnected news list.

5. **跨市场同类股票与近期表现**
   - Build peers from the same or closest segment across A-shares, US, Japan, Korea, and other relevant markets.
   - For each peer, include ticker, market, business similarity, and recent performance when current data is available.
   - Use a 30-calendar-day window by default: latest available close versus the closest available trading close around 30 calendar days earlier.
   - If data is adjusted close, say so. If the market was closed or data is missing, mark the gap instead of fabricating a number.

6. **股东人数、流通市值、总市值**
   - Report latest shareholder count, float market cap, total market cap, closing price, PE/PB when available.
   - For A-shares, prefer Tushare `stk_holdernumber`, `daily_basic`, `daily`, `stock_company`, and filings.
   - For other markets, prefer exchange data, filings, company IR, or reputable market data.

7. **结论与降级条件**
   - Lead with the research judgment, not a trade instruction.
   - State the strongest evidence, missing proof, and the facts that would weaken or reverse the judgment.

## Evidence And Data Rules

- Prefer primary sources: filings, exchange announcements, company IR, earnings calls, product disclosures, tenders, permits, customer certification, patents, standards, and official project records.
- For upstream/downstream report impact, do real web/source fetching. Do not rely only on memory, industry common sense, or the target company's own statements. Cite the report or filing name, period, source URL, and publication date when available.
- Use reputable market data for prices, market caps, shareholder data, and peer performance. Always state the source and date.
- For A-share Tushare usage, keep requests small and read-only. Clear local proxy environment variables when proxy stability matters. If an IP or frequency limit occurs, wait 10 seconds and retry up to 5 times, then stop and label the missing data.
- Never write secrets, API keys, tokens, private endpoints, or account identifiers into outputs.
- Avoid direct buy/sell commands and guaranteed return language. Rank research priority only.

## Upstream And Downstream Report Workflow

Use this workflow inside the `上下游财报影响` section:

1. **Build the chain sample**
   - Start from the target's disclosed customers, suppliers, related parties, product categories, and industry peers.
   - If exact customers or suppliers are not disclosed, use listed companies in the closest demand-side and supply-side layers, and label them as "proxy peers".
   - Keep the sample small and explainable: usually 2-4 supply-side names and 2-4 demand-side names.

2. **Fetch filings and reports**
   - A-shares: use SSE/SZSE/CNINFO announcements, annual/interim/quarterly reports, exchange Q&A, and company IR.
   - US: use SEC 10-K, 10-Q, 8-K, earnings releases, transcripts, and investor presentations.
   - Hong Kong: use HKEX filings, annual/interim reports, placings, and connected transactions.
   - Japan: use TDnet, company earnings materials, integrated reports, and segment disclosures.
   - Korea: use DART filings, company IR, export/customer ecosystem disclosures, and earnings materials.

3. **Extract comparable signals**
   - Demand-side customers: capex, fab/plant expansion, tool spend, utilization, production ramps, inventory, backlog, and guidance.
   - Supply-side suppliers: input cost, lead time, delivery capacity, gross margin, quality/certification, inventory, and production bottlenecks.
   - Same-layer peers: revenue growth, order backlog, margins, customer validation, and segment comments that confirm or contradict the target's story.

4. **Translate to impact**
   - `利好`: customer capex/order growth, supplier capacity stabilization, peer confirmation, higher utilization, repeated orders, or cash conversion improving.
   - `利空`: customer capex cuts, inventory digestion pressure, supplier delays or cost inflation, margin compression, slower tool qualification, or substitute technology.
   - `中性`: mixed reports or signals that affect the industry but not the target's exact layer.
   - `需核实`: source is weak, proxy is distant, or the report lacks a direct link to the target's products.

5. **Show the evidence**
   - Include a compact table with `公司 / 上下游角色 / 最新报告 / 关键财报信号 / 对目标公司的影响 / 证据强度`.
   - Follow with a short synthesis: what the upstream and downstream reports collectively say about the target's demand, pricing power, delivery risk, and margin risk.

## Compact Table Suggestions

Use tables only when they improve comparison:

- `问题 / 结论 / 证据强度 / 关键来源 / 待验证`
- `业务 / 收入占比 / 毛利率或利润贡献 / AI 链条关系 / 趋势判断`
- `公司 / 上下游角色 / 最新报告 / 关键财报信号 / 对目标公司的影响 / 证据强度`
- `市场 / 股票 / 业务相似度 / 30日涨跌幅 / 数据来源 / 备注`
