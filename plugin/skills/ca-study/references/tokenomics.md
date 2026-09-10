# Tokenomics: distribution, dilution, and holder economics

Read for every asset assessment. Tokenomics has its own substantial weight in [rating-framework.md](rating-framework.md): operating application 35/100, early application 30/100, and meme 25/100. Show how the findings strengthen or weaken the final current-buy grade and entry conditions. Do not merely append a token-allocation description after assigning the grade.

The user's reference [post by @sunburneugo](https://x.com/sunburneugo/status/2097580793388540096) motivates attention to holder capture and remaining dilution. Its token examples, payout ratios, returns and forecasts are the author's claims, not verified facts or permanent recommendations. Apply the general principle with fresh asset-specific evidence; do not adopt its numeric rejection thresholds or named favorites as rules.

## Supply and ownership ledger

Record chain, exact token, observation time/block, source and denominator for each material ratio. Reconcile the launch allocation with current ownership; a published allocation pie chart does not establish today's distribution.

- Establish genesis issuance, maximum supply if enforceable, cumulative later minting and actual supply-reducing burns, current on-chain total supply, circulating supply, locked/vesting balances and remaining mint authority. For rebasing/bridged tokens account for those mechanics and avoid counting escrow plus its wrapped representation twice. If no hard maximum exists, label the FDV convention and show horizon supply scenarios.
- Reconcile `current total supply = issued supply + subsequent issuance - supply-reducing burns`, adjusted for the token's mechanics. A transfer to a provably irrecoverable address may remove economically available tokens without reducing `totalSupply`; report it separately. Do not subtract those tokens twice from an aggregator's already adjusted supply. Distinguish original, current-total and circulating denominators.
- Report circulation as `circulating / stated total-or-max basis`, with exclusions and method. Separately estimate economically saleable float, including unlocked insider inventory. Staked tokens with instant withdrawals are not equivalent to irrevocably locked tokens. A claim of 100% circulation does not mean broad public ownership or no selling pressure.
- Break down team/founder, investor/private sale, public/community, treasury/ecosystem/rewards, liquidity and other allocations. State cost/discount, beneficial-control clusters, vesting, cliffs, unlock authority and withdrawal rights. Separate observable addresses from inferred common control; use [holders-and-launch.md](holders-and-launch.md) for bundle and wallet tracing.
- Show future releases over 7/30/60 days for memes and the application's chosen horizon: tokens, percentage of current circulation, recipient type and likely sellable inventory. Unlocks increase float without necessarily increasing total supply; emissions increase total supply. Compare potential selling with organic demand and executable depth, not headline market cap alone.

Low circulating market cap with high FDV or a large cheap insider reserve may be expensive on a future-supply basis. High circulation, limited future issuance, fair acquisition costs and distributed ownership can support a higher grade when verified. Neither a fixed supply nor a tiny unit price proves value.

## Burns: distinguish a large percentage from real economic impact

Report cumulative burn amount/ratio and recent burn flow separately, identifying the denominator, origin of tokens, dates and transactions. Distinguish initial uncirculated inventory destruction, market-purchased token burns, transaction-tax burns and transfers to a purported burn wallet. LP-token burns concern liquidity custody, not the asset token's supply burn rate.

A launch that destroys 90% of an arbitrary initial supply but leaves insiders controlling most remaining tokens is not automatically superior to a fairly distributed token with no burn. Measure insider shares against remaining supply/float as well as original allocation. Check whether privileged minting can reverse scarcity.

For a matched interval, reconcile new issuance with verified irreversible removals to estimate net total-supply change. Separately model changes in sellable float from unlocks, rewards, treasury redistributions and burns of circulating tokens. A burn of never-circulating treasury inventory does not cancel an equal upcoming float unlock. Do not equate token-count net deflation with net market buying pressure.

## Revenue routing, buybacks and dividends

Use the configured → funded → allocated → paid → repeatable evidence ladder in [cashflow-and-contracts.md](cashflow-and-contracts.md). Trace actual collection and final use over the same interval. Separate promised routing, implemented rules, executed amounts and sustainable economics.

1. **Revenue denominator:** identify gross trading taxes/fees, protocol-retained fees, net operating profit or distributable cash after costs. State what LPs, creators, referrers, operators and treasury retain. A percentage of a fee is not that percentage of trading volume. Separate revenue sources from fresh financing, customer principal, treasury depletion and newly issued tokens.
2. **Buyback ratio:** show committed and executed spending divided by the stated revenue/cash-flow denominator, plus actual quote-asset/USD amounts where conversion is supported. Identify purchases and destination: burn, treasury, staking rewards or later resale. Funds merely allocated to a buyback wallet are not purchases. Treasury-funded buying can exceed period revenue; label the funding source instead of calling it sustainable capture.
3. **Dividend ratio:** show the stated allocation and actual holder payouts relative to the same defined revenue basis. Identify payout asset, eligible token/holder set, staked versus all supply, claim cost, lock/exit conditions and who can change recipients or rates. Use amounts and actual eligible holdings to assess holder yield; do not infer a paid yield from an advertised distribution percentage.
4. **Effective holder capture:** assess what a holder of this exact token receives or benefits from after operating needs, leakage and dilution. Buyback followed by burn is one use of cash, not two additive revenue shares. A combined buyback-plus-dividend share needs non-overlapping cash uses and a common denominator. Burn percentages, circulation percentages and revenue percentages are different measures and must not be summed.
5. **Sustainability and control:** compare recurring external earnings with incentive expense, operating runway, issuance and insider/treasury selling. A high payout percentage on negligible fees may matter less than a lower share of substantial durable cash flow. High trading taxes may suppress use, trading and exit. A team retaining reasonable operating funds can be healthier than an unfunded promise to distribute 100%. Separate revocable incentives from enforceable token rights; revenue sharing does not establish equity ownership.

No dividend or buyback is required for every token. For an application, evaluate an evidenced alternative demand/capture mechanism if present. For a pure meme without an income thesis, assess fair distribution, dilution, holder incentives and liquidity alignment; absence of dividends alone is not a deduction. If a meme makes buyback/dividend claims, verify them and reflect misleading claims in the integrity assessment.

## How to award the tokenomics points

Use the subweights below inside the selected mode, never as an extra bonus on top of its 100-point table. Evidence labels and unknowns apply to each component; do not invent measured percentages or treat unavailable data as a clean bill of health.

| Component | Operating application | Early application | Meme |
| --- | ---: | ---: | ---: |
| Supply, circulation and net dilution | 8 | 8 | 10 |
| Allocation, acquisition terms and alignment | 7 | 7 | 10 |
| Holder capture, incentives and economic sustainability | 20 | 15 | 5 |
| Total | 35 | 30 | 25 |

- **Strong contribution:** verified supply and meaningful distribution coverage, bounded future dilution, aligned insider terms, and credible benefits for outside holders. An operating cash-flow thesis needs realized, repeatable capture for strong capture points. A sound fee-free, fixed-supply meme can earn high tokenomics points without inventing dividends.
- **Mixed contribution:** a plausible mechanism or reasonably aligned structure with manageable uncertainty, some concentration/dilution, or limited execution history. In early applications, score mechanism credibility and feasible future capture rather than requiring a mature payout history. Show which uncertainty the valuation discount compensates for and what evidence is needed before adding.
- **Weak contribution:** verified extractive allocation, substantial cheap inventory coming to market, economically weak holder capture, unsustainable subsidies or readily redirected value. An announced high payout/burn ratio alone earns no execution credit. Missing evidence earns no verified benefit but is not itself proof of bad conduct.

Explain earned/available points if publishing numeric detail, otherwise give a clear strong/mixed/weak judgment, decisive evidence and direction of rating impact. Do not automatically assign every unknown a zero or midpoint to manufacture a score. If material uncertainty prevents bounded assessment, use the framework's confidence/ceiling rules.

Tokenomics scores ownership structure and economic design; the holder/liquidity dimension scores current profits, remaining overhang, observed sales and executable exits. Operating-economics points assess the business's earning quality, while capture points assess its transmission to holders. The valuation dimension prices those findings. Do not repeat an identical bonus or penalty under all three headings. Apply a binding risk ceiling instead of stacking arbitrary deductions for the same defect.

## Required assessment output and decision effects

Before the unchanged five-line final verdict, include a compact tokenomics assessment covering allocation/insider share, circulation/FDV, upcoming dilution, burn ratio, buyback ratio and dividend ratio. For each material number show basis/time and verified versus claimed state; use `Unknown` for unavailable data and `N/A` only for mechanisms confirmed inapplicable. Include actual amounts as well as percentages where available. On short follow-ups, summarize material changes or unresolved items and reference the dated prior evidence rather than silently omitting this dimension.

Explain whether the structure improves or weakens the current grade, why a low valuation does or does not compensate for it, and what changes would alter entry/add/review conditions. Better verified capture and limited dilution may justify a better grade or valuation range; concentrated low-cost supply and weak capture can reduce both despite an attractive product.

Feed the resulting net issuance, float releases, sustainable holder cash flow and control assumptions into [valuation-and-strategy.md](valuation-and-strategy.md). Keep per-token upside distinct from market-cap growth. Confirmed overwhelming supply/exit risk can impose a D/F ceiling under the framework; cosmetic burns and advertised distributions cannot undo it. Incomplete payout history alone must not erase a credible low-valued early expectation trade.
