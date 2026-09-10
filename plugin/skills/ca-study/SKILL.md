---
name: ca-study
description: Evidence-first crypto due diligence with a mandatory line-by-line A/B/C/D/F buy verdict, heavily weighted tokenomics and holder capture, near-term meme/launchpad catalysts, early application valuation opportunities, large-holder profits, and launch-bundle exits. Use for current investigation of a supplied CA, token, launchpad, pool, project URL, or X account rather than generic crypto education.
---

# ca-study

Produce a decision-useful investigation whose factual spine can be reproduced. Do not equate a polished site, ticker, blue check, liquidity, or advertised payout with legitimacy.

Every project/token investigation using this skill must end with the five-line plain-text **最终投资评级** format in [references/valuation-and-strategy.md](references/valuation-and-strategy.md): **综合 A/B/C/D/F; 当前赔率 using ⭐; 当前策略; 买入策略 with a valuation range/action**. `A` is highest; `F` means **当前不考虑**, not necessarily fraud. The final `综合` line contains only the letter, without a numeric score or plus/minus suffix. This applies to short questions and follow-up updates without prompting. Put evidence, confidence, scenario tables and any scoring detail before the final block. Judge the current entry price, including early expectation-driven opportunities; do not substitute product maturity for buying attractiveness. Refresh material market/holder evidence; do not reuse old ratings or screenshot target ranges as current. Plugin maintenance or a request with no identifiable investable asset does not justify inventing a token or rating.

For memes, prioritize the next 7 days' breakout opportunity within a default 1–2 month scenario horizon, and always assess the exact launchpad's ability, incentive and observed actions to support the token. For low-valued early applications, explicitly assess a small expectation-based entry against dated, comparable tokens before concluding `D` or waiting for full delivery. Incomplete maturity/accounting/holder history alone is not a prohibition on a small speculative entry; confirmed safety failures remain disqualifying.

Tokenomics must materially affect every current-buy rating: **35/100 points for operating applications, 30/100 for early applications, and 25/100 for memes**. Assess allocation/insider terms, actual circulation, remaining unlocks/emissions, burn ratio, buyback ratio and dividend ratio with denominators, execution evidence and effective holder benefit. Distinguish promised percentages from realized flows; weigh net dilution and sustainable capture together. Strong verified economics may improve the grade; extractive distribution and weak holder capture may lower it despite a good product or small headline market cap. Pure memes need no income mechanism, and early applications need no mature payout history merely to qualify for a small expectation trade.

## Mandatory tokenomics format

Every CA/project investigation, including short follow-ups, must visibly include the following `代币经济` block before the final investment verdict. Keep these labels and order; do not replace the block with scattered prose, a score, or an unlabeled ratio such as `75% / 20% / 5%`. Fill every field with asset-specific evidence; unavailable information stays `未核实`, not zero or an omitted line. Plugin maintenance itself does not require an asset block.

```text
代币经济：
总量：{数量、代币、初始/当前/最大供应口径} / 流通百分比：{流通数量 ÷ 明示供应基数 = 百分比，或未核实}
营收分配：
{v1版／当前版}：{分母是什么收入或手续费；平台 X%，发币者 Y%，其余比例分别给谁、做什么、涉及哪个代币}
{v2版等，仅确有版本时逐版列出}：{同上；注明适用对象、当前/历史状态}
利润分配：{明确是净利润还是平台所得收入；X% 用于购买哪个代币并销毁/持有，Y% 给谁或支付什么，剩余用途}
回购机制：{有／无／未核实；已执行／仅宣布等状态}   当前回购比例：{累计已核实回购本币数量 ÷ 明示供应基数 = 百分比，或未核实}
销毁机制：{有／无／未核实；已执行／仅宣布等状态}   当前销毁比例：{累计已核实不可恢复销毁本币数量 ÷ 明示供应基数 = 百分比，或未核实}
```

Use `当前版` when there is only one evidenced version; never invent v1/v2. Attach observation time, direct sources and `已验证／项目方声称／未核实` to the block or relevant lines. These cumulative supply ratios are distinct from the revenue/profit allocation percentages above. Explain each percentage's recipient, purpose, denominator and exact token. Do not call operating allocations net profit, count buyback-and-burn twice, copy a buyback ratio into the burn field, or reuse the user's Pons example as live data. Apply the detailed field definitions and examples in [references/tokenomics.md](references/tokenomics.md#fixed-output-contract), then add allocation/unlocks, dividends and rating impact as needed.

Treat project age as material evidence, not a footnote, but apply it differently by category. For applications, a newly assembled website, social presence, product claim, and token materially weaken claims of delivery history. For a pure meme—especially a new event coin—same-day creation may be normal and must not by itself force a downgrade; report the short observation window and judge catalyst strength, propagation, launch fairness, holder cost basis, and whether attention survives the initiating event. Explicitly report the dates relevant to the category when obtainable. Distinguish an old recycled X account from real operating or community history.

## Start from identity, not narrative

1. Record every supplied identifier: chain, CA, pool, URL, X handle, ticker, and claimed launchpad.
2. Resolve the chain before interpreting the address. Search the exact CA and confirm it on a current explorer or RPC. The same EVM address can exist on several chains; never infer the chain from checksum, ticker, or UI styling.
3. Build the minimum identity graph: token CA → deployer/factory → launchpad/template → primary pool → exact base and quote CAs → project site/X cross-links.
4. Treat a ticker or name as a label only. Contract addresses and transaction hashes are the identifiers.

For current data, browse live sources. Prefer explorer/RPC records, verified source code, protocol docs, issuer contract lists, company filings, and historical first-party posts. Use aggregators for discovery and market snapshots, not as sole proof of official status, ownership, or cash flow. Include observation time and timezone for volatile values.

Run `scripts/dex_snapshot.py` when a CA needs DEX pair discovery or primary-pool ranking. Run `scripts/evm_probe.py` when an EVM RPC URL is available and a baseline code/proxy/interface check reduces ambiguity. These are triage helpers, not substitutes for source-code and transaction review.

## Route the investigation

- For launchpads, pools, liquidity, Robinhood Stock Tokens, other stock/RWA issuers, or an underlying-company summary, read [references/pools-and-launchpads.md](references/pools-and-launchpads.md).
- For taxes, revenue, dividends, rebates, buybacks, burns, holder rights, or privileged contract controls, read [references/cashflow-and-contracts.md](references/cashflow-and-contracts.md).
- For website, X, team, community, impersonation, account compromise, or rug risk, read [references/identity-and-community.md](references/identity-and-community.md).
- For every project/token investigation, read [references/rating-framework.md](references/rating-framework.md), [references/tokenomics.md](references/tokenomics.md), [references/holders-and-launch.md](references/holders-and-launch.md), and [references/valuation-and-strategy.md](references/valuation-and-strategy.md). The overall grade, tokenomics assessment and rating impact, entry strategy, valuation, large-holder profit analysis, and launch-bundle exit check are mandatory. For memes, also always read [references/pools-and-launchpads.md](references/pools-and-launchpads.md) for launchpad support and control-risk assessment.

Read other references as needed for the requested modules. For a full project audit, read all seven.

## Evidence labels

Use one of these states for material claims:

- **Verified:** directly supported by current on-chain data or a primary authoritative record.
- **Corroborated:** supported by multiple independent records but not fully provable on-chain.
- **Claimed:** stated by the project or community without adequate independent proof.
- **Inferred:** reasoned from evidence; state the evidence and uncertainty.
- **Unknown:** unavailable, ambiguous, or not checked.

Never turn `Unknown` into `No`. No observed payout is not proof that no payout mechanism exists; an unavailable owner call is not proof of renounced ownership.

Separate four risk layers: token contract, pool/liquidity, operator/project, and underlying stock/RWA. A safe ERC-20 does not make an unbacked stock claim legitimate, and an official stock quote asset does not endorse the meme or application token paired with it.

## Required answer shape

Lead with a short verdict in the user's language: what it actually is, the overall current-buy grade, what drives its value at today's valuation, and the largest unresolved risk. Always include the rating summary below; keep other modules scoped to the question. Use compact tables with direct sources where useful. A full audit should include:

- Identity and launchpad
- Main pool and exact paired asset
- If stock-paired: one-sentence underlying stock profile with current market cap, company business, and main revenue/profit engine
- Token/contract control
- Fees, revenue, and holder distributions
- Tokenomics: the mandatory `代币经济` block above, followed by allocation and insider share, circulation/FDV, upcoming unlocks/emissions, dividend ratios, actual execution and net holder benefit; state how these affect the grade
- Website, X, team, and community
- Project-age timeline: for applications, domain, first site evidence, X creation and first relevant post, token deployment, and pool/trading start; for pure memes, prioritize the initiating event, first coin post, launch, pool start, and subsequent attention/price inflections
- Market snapshot: observation time/timezone, price, circulating market cap or explicit unknown, FDV, executable liquidity, volume quality, and dilution/unlocks
- Large-holder positions and cost basis: realized profit, unrealized profit, remaining position, concentration, turnover evidence, and potential sell pressure versus liquidity
- Launch-bundle/insider cohort: initial buys, sales and proceeds, remaining balances, attribution confidence, and data coverage
- Red flags, invalidated claims, and unknowns
- Category and overall current-buy grade: application, meme, or hybrid; `A/B/C/D/F` plus confidence
- Current risk/reward and buy/wait/do-not-consider strategy: preferred entry zone, conditional first-entry zone, add/reduce triggers, no-chase boundary, and invalidation
- Development-based market-cap space: downside, base, and conditional upper range with milestones, value capture, supply and failure conditions; memes default to 1–2 months with 24–72 hour and 7-day catalyst checkpoints
- For early applications: current relative valuation, expectation-trade rationale, small-entry versus waiting-for-confirmation tradeoff, and why a peer premium is or is not justified

Before the final five-line block, give confidence, category, timestamp, current market cap/FDV, scenarios and two to four decisive reasons. Explain the selected scoring mode, valuation effect and any binding cap when useful. State how tokenomics, valuation and holder/launch sell pressure changed the entry decision. Missing data stays `Unknown`; distinguish unproven maturity from evidence of failure, and reflect manageable uncertainty in confidence, speculative position size and add conditions. Do not invent scores, prices, stars, or a market-cap ceiling. A hybrid still needs one overall grade. Keep each final field on its own visibly separate line.

`F` means the asset is outside the current buy consideration set; distinguish unfavorable economics, insufficient critical evidence, and confirmed failure/rug. Grades and strategies are research judgments at a stated price, not trade authorization. A market-cap upper range is conditional on development and a time horizon, not a hard maximum or guaranteed target. Give pivotal transaction hashes for cash-flow, holder-sale, and ownership claims when available. Keep raw tool output out of the answer unless requested.

If chain identity or exact quote CA cannot be resolved, say so prominently and do not issue a strong legitimacy conclusion. Ask one focused question only when multiple plausible chains/projects remain and the difference materially changes the result.
