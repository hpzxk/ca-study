# Pools, launchpads, and stock/RWA pairs

Use this reference for launchpad attribution, DEX pools, liquidity, valuation, stock-token provenance, and the underlying listed company.

## Launchpad attribution

Do not attribute a token from branding or ticker format alone. Seek a creation event from the launchpad factory, matching documented factory/deployer, factory call trace, or a launchpad page linking the exact CA and corroborated by the explorer. Distinguish `created on`, `uses liquidity from`, `listed by`, and `endorsed by`.

## Meme launchpad support and control

This assessment is mandatory for every meme rating, not just a launchpad-specific question. Resolve an ambiguous platform name to its exact factory/program, official website/accounts, chain and relevant sector before attributing support. No named platform or sector is a permanent whitelist.

Evaluate three distinct questions: **can the platform help, why would it choose this token, and what has it actually done?** Examine fee/equity/token incentives, reputation and competition, flagship/sector fit, available distribution and capital/liquidity resources, and support for comparable recent launches. Include failed or unsupported launches and the observation window where available; a handful of winners does not establish a support success rate.

Use an evidence ladder:

- `Created/listed only`: launch provenance with no token-specific assistance established.
- `Support hypothesis`: credible platform incentives/resources and relevant track record, but no action for this exact token yet. State what would confirm or invalidate it within the next week.
- `Observed promotion`: exact-token official posts, featured placement, campaign/event or documented distribution support; distinguish generic launch announcements from selective promotion.
- `Observed economic support`: attributable funding, token purchases, LP provision/incentives, retained inventory or documented market-making arrangements, with dates, amounts and transaction evidence where available.

Treat plausible future support as a conditional near-term catalyst and confirmed action as stronger evidence. Absence of an explicit public promise does not make support impossible; the platform label alone does not make it likely. Record `Unknown` when evidence is unavailable rather than asserting the platform is uninvolved.

When the question is whether the platform may `扶持/做市/控盘/坐庄`, separate legitimate market making or promotion from suspected coordinated price control and proven manipulation. Trace attributed wallets and LP control, initial/remaining inventory, purchases versus sales, and who can withdraw support. Common funding or synchronized trades alone do not prove ownership or intent. Concentrated control can amplify a short-term move and abrupt exits; report both, with holder/liquidity risk deductions. Do not describe alleged price control as guaranteed support or a safety benefit.

The rating must state the platform, the support evidence level, the next 7-day action to watch, and the effect on breakout prospects and exit risk. Score support/distribution in the meme's 15-point dimension; avoid counting the same action again as a separate bonus elsewhere. Strong organic distribution can support that dimension even without a sponsor.

## Find the real market

Enumerate all pools before selecting the main one. Record chain, DEX/version, pool address and age, exact base/quote CAs, liquidity, 24h volume/trades, price, FDV, reported market cap, fee tier, and LP custody/lock. Rank by executable liquidity, not volume, UI ordering, or ticker. Flag suspicious turnover when volume is extreme versus liquidity and trader activity is repetitive or thin.

Never merge FDV with circulating market cap. If circulating supply is not independently known, report FDV and mark market cap unverified. LP value is not equivalent to the amount that can exit without material slippage.

## Launch structure and profit overhang

For meme coins, identify the launchpad and its actual mechanics: bonding curve or auction, migration path, creator allocation, launch buy, fee recipients, liquidity custody, anti-sniper rules, and whether the paired asset adds a genuine narrative link or only cosmetic branding.

For both application and meme tokens, apply [holders-and-launch.md](holders-and-launch.md): trace large-holder profits and launch-cohort purchases, sales/proceeds, and remaining positions. Do not stop at current concentration or a bundle flag. Separate a launchpad's configured fairness claims from observed distribution; same-block buying alone does not prove a coordinated bundle. Missing cost-basis or launch history is unknown, not a clean launch.

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
