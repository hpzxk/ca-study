---
name: ca-study
description: Evidence-first crypto CA and project due diligence with a mandatory current-buy S/A/B/C/D/E/F rating, separate application and meme criteria, current valuation, large-holder profits, and launch-bundle exits. Use when the user supplies a CA, token, launchpad, pool, project URL, or X account and wants current due diligence rather than generic crypto education.
---

# ca-study

Produce a decision-useful investigation whose factual spine can be reproduced. Do not equate a polished site, ticker, blue check, liquidity, or advertised payout with legitimacy.

Every project/token investigation using this skill must include one **综合评级（当前买入性价比）：S/A/B/C/D/E/F** per assessed asset, without waiting for the user to request a rating. This includes short questions and follow-up updates. The grade answers whether buying at the observed price and valuation is attractive after accounting for project/category quality, token rights, liquidity, and on-chain sell pressure. It is not merely a product-quality or attention score. Refresh the material market and holder evidence; do not reuse a previous grade as current by default. Plugin maintenance or a request with no identifiable investable asset does not justify inventing a token or rating.

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
- For every project/token investigation, read [references/rating-framework.md](references/rating-framework.md) and [references/holders-and-launch.md](references/holders-and-launch.md). The overall current-buy grade, valuation review, large-holder profit analysis, and launch-bundle exit check are mandatory.

Read other references as needed for the requested modules. For a full project audit, read all five.

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
- Website, X, team, and community
- Project-age timeline: for applications, domain, first site evidence, X creation and first relevant post, token deployment, and pool/trading start; for pure memes, prioritize the initiating event, first coin post, launch, pool start, and subsequent attention/price inflections
- Market snapshot: observation time/timezone, price, circulating market cap or explicit unknown, FDV, executable liquidity, volume quality, and dilution/unlocks
- Large-holder positions and cost basis: realized profit, unrealized profit, remaining position, concentration, turnover evidence, and potential sell pressure versus liquidity
- Launch-bundle/insider cohort: initial buys, sales and proceeds, remaining balances, attribution confidence, and data coverage
- Red flags, invalidated claims, and unknowns
- Category and overall current-buy grade: application, meme, or hybrid; `S/A/B/C/D/E/F` plus confidence

The mandatory rating summary contains: **overall grade + confidence + category + timestamp + current market cap/FDV**, the category base score and valuation adjustment, any binding risk cap, and two to four decisive reasons. State explicitly how valuation and holder/launch sell pressure affected the result. Missing material data must be marked `Unknown` with a provisional conservative grade under the framework, not omitted or silently treated as safe. A hybrid may show both category assessments but still needs one overall grade.

`S` is strongest current buying attractiveness; `E` means extremely poor current risk/reward or a material inability to establish investability; `F` is the disqualifying failure/rug override. Grades are research judgments at a stated price, not guaranteed returns or authorization to trade. State the price/valuation or observable evidence that would upgrade, downgrade, or invalidate the grade. Give pivotal transaction hashes for cash-flow, holder-sale, and ownership claims when available. Keep raw tool output out of the answer unless requested.

If chain identity or exact quote CA cannot be resolved, say so prominently and do not issue a strong legitimacy conclusion. Ask one focused question only when multiple plausible chains/projects remain and the difference materially changes the result.
