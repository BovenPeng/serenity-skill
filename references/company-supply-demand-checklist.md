# Company Supply-Demand Checklist

Use this file when a user asks for a single-company checkup that includes industry-chain position, supply-demand tightness, price increases, capacity shortages, expansion difficulty, revenue mix, customers and orders by business line, AI-chain transition, upstream/downstream report impact, cross-market peers, recent performance, shareholder count, float market cap, or total market cap.

Keep the analysis grounded in public evidence. Do not turn "AI exposure" or "scarce layer" into a conclusion unless filings, company disclosures, customer evidence, or reliable industry sources support it.

## Required Output Shape

For a full company checkup, answer in these sections:

1. **产业链位置**
   - State the company's exact upstream/downstream position.
   - Name the scarce layer it controls, supplies, or only benefits from.
   - Link the position to customer capex, manufacturing process, component, material, equipment, software, or infrastructure constraints.
   - If the request starts from a concept or theme, first use `references/concept-to-chain-framework.md` to identify the company's exact chain layer and product or technology route.
   - Separate real business exposure from a loose concept label. State whether the company is a direct producer, upstream supplier, equipment/material vendor, module/system integrator, downstream customer, or only theme-adjacent.

2. **供需与涨价/产能/扩产**
   - Check whether this layer shows price increases, tight capacity, long lead times, high utilization, customer prepayments, capacity reservations, order backlog, certification queues, permits, or specialized equipment bottlenecks.
   - Separate layer-level tightness from company-specific proof.
   - State "未见强证据" when only the theme is strong but company-level proof is missing.

3. **主营业务、客户与订单证据**
   - Break down revenue and profit by disclosed business segment.
   - For each material segment or product line, include customers, order quantity, order amount, and evidence status when the user asks "客户是谁", "订单量", "订单金额", or similar.
   - Only name customers or orders when supported by financial reports, exchange filings, official announcements, official IR records, tender/winning-bid documents, customer certifications, customer-side filings, or confirmed news.
   - If a segment's customers, order quantity, or order amount are not publicly disclosed, write `未披露`; if the claim is rumored, inferred, or only from an unsourced channel check, write `未证实`.
   - Do not turn downstream proxy companies into confirmed customers. A wafer fab, OEM, hyperscaler, or end-market company can be used as a `需求侧 proxy` only after it is clearly labeled as such.
   - Do not treat phrases such as "头部客户", "国内外领先客户", or "主流晶圆厂" as named customers unless the source names them.
   - If segment profit is not disclosed, state that and use revenue, gross margin, or qualitative disclosures instead.
   - Identify AI-chain exposure only when supported by filings, product disclosures, customers, confirmed orders, or industry-chain logic.
   - Estimate whether the AI-related share can rise from demand-side pull and supply-side constraints. Label any estimate as qualitative unless a company disclosure gives numbers.
   - When a concept has multiple product or technology routes, map each disclosed segment to the route it actually belongs to before discussing growth.
   - Do not call a company a beneficiary only because the concept is hot. Confirm product fit, revenue exposure, customer adoption, qualification, orders, or segment guidance.

   Recommended customer/order matrix:

   | 业务/产品线 | 收入/占比 | 毛利/利润贡献 | 客户名称 | 订单量 | 订单金额 | 证据来源 | 证据状态/缺口 |
   |---|---:|---:|---|---:|---:|---|---|
   | Segment A | disclosed value or `未披露` | disclosed value or `未披露` | named customers or `未披露` | disclosed quantity or `未披露` | disclosed amount or `未披露` | filing/news/IR/tender | confirmed/gap |

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
- Customer and order claims require stronger proof than industry logic. Prefer signed-contract announcements, tender/winning-bid notices, official shipment or certification statements, named-customer filings, customer-side filings, and official IR answers. If only a research note, forum post, broker channel check, or unsourced media article mentions a customer or order, mark it `未证实`.
- Use reputable market data for prices, market caps, shareholder data, and peer performance. Always state the source and date.
- For A-share Tushare usage, keep requests small and read-only. Clear local proxy environment variables when proxy stability matters. If Tushare returns `IP 数量超限`, an IP/frequency-limit message, or a transient request failure, do not skip the data point immediately: sleep 45 seconds and retry, up to 5 total attempts. Only after 5 failed attempts should the run stop using that endpoint and label the missing data.
- Never write secrets, API keys, tokens, private endpoints, or account identifiers into outputs.
- Avoid direct buy/sell commands and guaranteed return language. Rank research priority only.

## Business Customer Order Workflow

Use this workflow before writing conclusions when the request asks for "每块业务的客户是谁", "订单量", "订单金额", "客户结构", "订单结构", or similar:

1. Build the disclosed segment list from the latest annual/interim report and reconcile it with current product names used in announcements, IR, and official website materials.
2. For each segment, search the target company's filings, official announcements, exchange Q&A, investor presentations, and official website for named customers, orders, shipments, certifications, backlog, or contract liabilities.
3. Search customer-side filings and tender/winning-bid sources for the same product line; only accept them as customer/order evidence when the target company is named.
4. Record values exactly as disclosed. Distinguish revenue, order amount, contract liabilities, backlog, shipment count, installed base, capacity, and qualification progress; do not mix these concepts.
5. Fill missing cells with `未披露` or `未证实`, then explain the missing evidence and the next source that would verify it.
6. In the final answer, separate `已证实客户/订单` from `需求侧 proxy` and `行业推断`.

## ModelHub API Generation Workflow

Use this workflow when the user explicitly asks to generate, replace, or rerun the single-company note through ModelHub API.

1. **Collect evidence first**
   - Finish the public-source evidence pack before calling ModelHub.
   - Include target-company filings, the business-segment customer/order evidence matrix, upstream/downstream report extracts, peer performance, shareholder count, market cap, and explicit data gaps.
   - Do not ask ModelHub to invent or fetch facts that were not collected.

2. **Call ModelHub section by section**
   - Prefer `scripts/modelhub_company_analysis.py` when Python and network access are available.
   - The script reads `MODELHUB_API_KEY` or `ASUKAQT_CODEX_MODELHUB_API_KEY` from the environment or local `~/.codex/.env`; never write the key into the repo, prompt files, notes, logs, or command output.
   - The script uses the Azure-style Chat Completions path: `/openai/deployments/{model}/chat/completions`.
   - Use `max_completion_tokens`, not `max_tokens`, for newer reasoning models that reject `max_tokens`.
   - Prefer ModelHub API for note generation/replacement when the user requests it. If ModelHub has an HTTP error, timeout, empty response, or other transient API issue, sleep 45 seconds and retry, up to 5 total attempts, before falling back or marking the generation gap.
   - Disable proxy use for the ModelHub request unless the user's network requires it.

3. **Replace safely**
   - Before overwriting an existing note, create a timestamped backup outside the user's main reading flow or in a hidden backup directory.
   - Keep the target company's master stock note unchanged unless the user explicitly requests a merge.
   - Add a short generation boundary in the output: generated by ModelHub API, evidence source path, model name, section count, and no investment-advice claim.

4. **Verify**
   - Confirm the output includes every required section in this checklist.
   - Confirm upstream/downstream report signals still map back to `利好`, `利空`, `中性`, or `需核实`.
   - Check Obsidian wikilinks for broken links if the note is written into an Obsidian vault.
   - Confirm no API key or private token was written.

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
- `业务/产品线 / 收入或占比 / 客户名称 / 订单量 / 订单金额 / 证据来源 / 证据状态或缺口`
- `公司 / 上下游角色 / 最新报告 / 关键财报信号 / 对目标公司的影响 / 证据强度`
- `市场 / 股票 / 业务相似度 / 30日涨跌幅 / 数据来源 / 备注`
