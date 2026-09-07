# Large-holder profits and launch-cohort exits

Use this reference in every application, meme, or hybrid investigation. Answer how much current large holders have made, how much they can still sell, whether early supply actually changed hands, and how much the launch bundle/insider cohort has already sold. These findings feed the holder-health score and risk ceilings in [rating-framework.md](rating-framework.md).

## Current snapshot and coverage

Record chain, exact token CA, observation time/timezone, block/slot where available, price source, supply denominator, primary pools and quote CAs. Prefer current explorer/RPC transfers, swaps, receipts and balances. Available analytics providers can supply discovery, cost/P&L, and bundle labels, but disclose their methodology/window and corroborate material findings with transaction records. Do not assume a particular plugin or API is installed, or that a missing provider field is zero. If primary history is unavailable, try a bounded independent read-only source and report the limitation.

Start with the top 20 economically relevant holders by current balance; examine at least the top 10 in detail, or all if fewer exist. Also include the creator, material related clusters, and launch participants that have exited the top-holder list. Expand the sample when a linked cluster or a large winner changes the risk conclusion. Report how many wallets were checked, their combined supply share, the history interval, cost-basis coverage, and exclusions. Do not imply a sample is the whole holder population.

Exclude pools, burn addresses, bridges, exchange omnibus wallets, routers and custodial/staking/vesting contracts from the ordinary whale ranking when their function is supported by evidence. Report relevant custody, unlock and beneficial-owner concentration separately rather than erasing those risks. Labels alone do not prove common ownership. Consolidate a holder's token accounts and supported related wallets; retain uncertainty for suspected links and do not double-count a wallet and its cluster.

## Profit and remaining position

For each material wallet/cluster, obtain or estimate:

| Field | Required interpretation |
| --- | --- |
| Current balance and supply share | Remaining sellable or locked inventory, with the supply denominator |
| Entry/receipt history and cost | Purchase quantities, entry dates/prices, quote spent, cost coverage and method |
| Realized profit | Sale proceeds minus allocated cost of units sold and included fees, in USD and/or quote units |
| Unrealized profit | Current marked value of remaining units minus their remaining cost basis |
| Gain multiple/return | State whether value/cost multiple or profit/cost percentage; never use an unlabeled multiple |
| Recent exits | Sale quantities and proceeds over the last 24h and 7d, or since launch if younger, subject to history coverage |
| Liquidity burden | Remaining marked value and a plausible partial-sale size versus executable depth, not headline market cap |

Use a consistent accounting method (such as FIFO or weighted average), disclose it, and do not mix provider definitions. Value historical cash flows at their transaction-time conversion rates; current quote prices can materially misstate historical USD profit. State whether gas, trading fees and token taxes are included. For partial histories show known cash flows or lower bounds, not a fabricated lifetime P&L or exact average entry.

Transferred-in tokens do not have zero cost merely because this wallet did not buy them. Trace the sender when material; otherwise mark inherited cost unknown and limit P&L coverage. Same-owner transfers preserve cost and are not sales. Airdrops/creator allocations may have a zero recorded token-purchase cost but unknown broader costs; report that basis and avoid infinite ROI. Distinguish buy/sell swaps from transfers, liquidity provision/withdrawals, bridging, and custody deposits. An exchange deposit is a possible sale signal, not verified sale proceeds.

Show a compact table of the decisive large holders (normally 5–10) plus an aggregate row for the full inspected sample. Use exact wallet/explorer links and pivotal sale hashes. Separate realized gains already taken from unrealized gains still exposed. If aggregating profitable holders, label whether losses elsewhere were excluded; do not silently mix gross winner gains and net cohort P&L. Do not extrapolate incomplete cost coverage to all holders.

## Turnover and potential selling

High profit is a warning to investigate, not proof of low turnover or certain dumping. Check retained early allocations, holder age, verified sales to new buyers, changing entry costs, unique traders, and changes in concentration. A transfer to a related wallet, self-churn, wash volume, or a large volume/market-cap ratio does not establish a cost-basis reset or independent demand.

Compare the remaining low-cost cohort inventory with quote-side reserves and, where obtainable, read-only route quotes for plausible partial exits (for example 10% and 25% of its remaining position). Mark these as stress scenarios, not predictions. Account for concentrated-liquidity ranges, correlated pools, fees/taxes and quote-asset quality; total displayed LP value and paper profits are not cash available to sellers. If executable depth is unavailable, label a reserve comparison as a rough bound and leave slippage unknown.

State one of: supported low-cost supply overhang; evidence of distribution/cost reset with residual risks; or insufficient history. Include the quantities and evidence behind the conclusion. A heavily profitable but fully exited wallet is historical evidence, not remaining sell pressure. A large still-held winner can matter even after some profits were realized.

## Launch bundles: bought, sold, and still held

Find the first tradable block/slot and distinguish deployment, trading enablement, bonding-curve start, and DEX migration. By default inspect the launch block/slot and first five minutes; extend to the actual distribution/migration period if necessary. Report the exact window and whether history is complete. Trace this initial cohort's subsequent activity through the current snapshot, rather than stopping at the launch window.

Identify creator launch buys, bundled transactions and suspected coordinated/sniper clusters using transaction ordering, funding trails, explicit bundle records where available, and subsequent flows. Separate **verified bundle**, **suspected coordination**, and **unaffiliated early buyer**. Same block/time, a common exchange funder, or a vendor label alone does not prove a common beneficial owner or an atomic bundle. Keep confirmed and suspected totals separate, and separate creator allocations from purchased tokens.

For each material cohort and the deduplicated total, report:

- Number of wallets; initial token purchases and allocation quantities; their percentage of supply; purchase quote spent when known.
- Verified token sales and quote/USD proceeds **during the launch window**, then **cumulative through the snapshot**, with the former explicitly included in the latter. Add recent sales when decision-relevant; never add overlapping intervals.
- Remaining balances across traced wallets, current marked value and supply share; distinguish original launch inventory from later reacquisition when attribution permits.
- Sold share of the initial purchased/allotted inventory when traceable. Later buys, mixed holdings and transfers can make raw cumulative sales exceed initial buys; label that gross turnover and do not report it as an impossible percentage of original inventory sold.
- Unresolved transfers/exchange deposits and history gaps. Reconcile `opening balance + buys + allocations + transfers in - sales - transfers out - burns/other disposals = closing balance` over a consistent window. Eliminate internal transfers within a confirmed cluster. Adjust for rebases or transfer taxes where applicable; an unexplained residual is missing evidence, not an inferred sale.

Answer explicitly: **发射捆绑/关联地址最初拿了多少，开盘期间卖了多少，截至现在累计卖了多少、收到多少，还剩多少？** Unknown amounts stay unknown. If only a sample or one venue is covered, label observed sales as partial/lower-bound data. A shrinking bundle balance alone cannot establish sales, and creator fees or LP withdrawals are not token-sale proceeds.

End by stating how the findings change current holder health and any overall rating cap. Missing bundle/P&L data must remain visible in the final rating; do not describe the launch as clean or the holders as unprofitable by default.
