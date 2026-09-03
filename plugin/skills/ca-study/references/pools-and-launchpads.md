# Pools, launchpads, and stock/RWA pairs

Use this reference for launchpad attribution, DEX pools, liquidity, valuation, stock-token provenance, and the underlying listed company.

## Launchpad attribution

Do not attribute a token from branding or ticker format alone. Seek a creation event from the launchpad factory, matching documented factory/deployer, factory call trace, or a launchpad page linking the exact CA and corroborated by the explorer. Distinguish `created on`, `uses liquidity from`, `listed by`, and `endorsed by`.

## Find the real market

Enumerate all pools before selecting the main one. Record chain, DEX/version, pool address and age, exact base/quote CAs, liquidity, 24h volume/trades, price, FDV, reported market cap, fee tier, and LP custody/lock. Rank by executable liquidity, not volume, UI ordering, or ticker. Flag suspicious turnover when volume is extreme versus liquidity and trader activity is repetitive or thin.

Never merge FDV with circulating market cap. If circulating supply is not independently known, report FDV and mark market cap unverified. LP value is not equivalent to the amount that can exit without material slippage.

## Robinhood Stock Tokens

For any claimed Robinhood official stock token, open the current [Robinhood Chain Token Contracts](https://docs.robinhood.com/chain/contracts/) page. Its stock/ETF table is generated live from the on-chain asset registry. Compare the pool's exact quote CA with the canonical CA on that page.

- Exact CA match: describe it as the canonical Robinhood Stock Token for that underlying.
- Same symbol/name but different CA: explicitly say it is **not** a Robinhood Stock Token.
- Missing/unavailable page or unresolved quote CA: status is `unknown`, not official.

An official Robinhood quote token does not mean Robinhood created, reviewed, or endorsed the other token in the pool.

## Non-Robinhood stock tokens

Identify the claimed issuer and classify the asset before describing it as tokenized stock:

1. **Issuer-listed security token:** exact CA appears on the identified issuer's official contract list and legal documents describe the holder claim.
2. **Third-party backed representation:** identifiable issuer/custodian claims matching reserves and redemption; verify current attestations, custody, eligibility and terms.
3. **Synthetic exposure:** value follows a stock through collateral/oracles/derivatives without granting ownership of a share.
4. **Self-issued ticker token:** only the project or an anonymous party claims stock linkage, with no independently verifiable backing or redemption.

For categories 1–3, verify legal entity, jurisdiction, relevant registration/authorization, custodian, beneficial-owner or derivative rights, reserve segregation, redemption process, eligible countries/users, attestations/audits, insolvency treatment, and operator powers. Do not call a token `guaranteed` merely because collateral is advertised. State whether protection is legal, contractual, collateral-based, discretionary, or unknown.

Require reciprocal issuer confirmation or authoritative records. A token website naming a broker, listed company, charity, custodian, or regulator is not proof of a relationship. When authority is uncertain, say so without offering a legal conclusion.

## Underlying stock one-liner

Whenever a pool is paired with a stock token or uses a stock narrative, add one sentence containing:

- underlying ticker and company name;
- current equity market cap with observation date;
- what the company does;
- the segment/product that generates most revenue or operating profit; if currently loss-making, say so and identify the main revenue source.

Use current market data for market cap and the latest company filing/earnings materials for business and profit mix. Do not treat the token's FDV as the listed company's market cap, and do not imply holders of an unbacked/synthetic token own the stock.

## Snapshot rules

Put observation time beside volatile values. Preserve conflicts rather than averaging them away. When sources disagree, prefer pool contract/reserve data and explain whether the difference is token ordering, oracle choice, circulating supply, stale indexing, or a different pool.
