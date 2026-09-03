---
name: ca-study
description: Evidence-first investigation of crypto contract addresses and projects, including chain identity, launchpad attribution, pools and paired assets, tokenized-stock provenance, fees or holder distributions, contract control, website and X authenticity, community strength, and separate application or meme ratings. Use when the user supplies a CA, token, launchpad, pool, project URL, or X account and wants current due diligence rather than generic crypto education.
---

# CA Study

Produce a decision-useful investigation whose factual spine can be reproduced. Do not equate a polished site, ticker, blue check, liquidity, or advertised payout with legitimacy.

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
- Whenever assigning a grade, read [references/rating-framework.md](references/rating-framework.md).

Read only the references required by the request. For a full project audit, read all four.

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

Lead with a short verdict in the user's language: what it actually is, what is genuinely distinctive, and the largest unresolved risk. Then give the smallest useful evidence table with exact CAs and direct links. Cover only requested modules; a full audit should include:

- Identity and launchpad
- Main pool and exact paired asset
- If stock-paired: one-sentence underlying stock profile with current market cap, company business, and main revenue/profit engine
- Token/contract control
- Fees, revenue, and holder distributions
- Website, X, team, and community
- Market snapshot and concentration
- Red flags, invalidated claims, and unknowns
- Category and grade: application, meme, or both; `S/A/B/C/D` plus confidence

Grades rank current evidence-adjusted project quality/attention worthiness, with `S` strongest and `D` weakest; they are not price forecasts or instructions to buy. State the evidence that would upgrade or invalidate the grade. Give pivotal transaction hashes for cash-flow or ownership claims when available. Keep raw tool output out of the answer unless requested.

If chain identity or exact quote CA cannot be resolved, say so prominently and do not issue a strong legitimacy conclusion. Ask one focused question only when multiple plausible chains/projects remain and the difference materially changes the result.
