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
   - Check upstream suppliers and downstream customers when public peers exist.
   - Look for positive signals: capex expansion, order backlog, utilization, pricing, gross margin, inventory digestion, cash conversion, or customer qualification progress.
   - Look for negative signals: order cuts, margin pressure, slower capex, inventory build, receivable stress, weak operating cash flow, delays, or substitute technologies.
   - Explain how those signals help or hurt the target company.

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
- Use reputable market data for prices, market caps, shareholder data, and peer performance. Always state the source and date.
- For A-share Tushare usage, keep requests small and read-only. Clear local proxy environment variables when proxy stability matters. If an IP or frequency limit occurs, wait 10 seconds and retry up to 5 times, then stop and label the missing data.
- Never write secrets, API keys, tokens, private endpoints, or account identifiers into outputs.
- Avoid direct buy/sell commands and guaranteed return language. Rank research priority only.

## Compact Table Suggestions

Use tables only when they improve comparison:

- `问题 / 结论 / 证据强度 / 关键来源 / 待验证`
- `业务 / 收入占比 / 毛利率或利润贡献 / AI 链条关系 / 趋势判断`
- `市场 / 股票 / 业务相似度 / 30日涨跌幅 / 数据来源 / 备注`
