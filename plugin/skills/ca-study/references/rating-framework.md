# Application and Meme current-buy rating framework

Read this reference for every project/token investigation and always give one overall `A/B/C/D/F` current-buy grade per assessed asset, without plus/minus suffixes. First classify the token as `application`, `meme`, or `hybrid`. A pure meme receives `Application: N/A`, not a failing application grade. For a hybrid, assess both categories, choose and explain the dominant investment thesis before scoring, and use that category as the base. If both are material, disclose explicit weights summing to 100% and combine the two base scores. Do not cherry-pick the higher score or let a meme narrative bypass a material application failure. Apply valuation once and the strongest relevant asset-level risk cap to the overall result. Always include the strategy and development scenarios in [valuation-and-strategy.md](valuation-and-strategy.md).

Grades measure evidence-adjusted **buying attractiveness at the current price/market cap**, including valuation and exit risk. A good project can be an unattractive purchase; a modest project can deserve a higher current-buy grade at a sufficiently low, defensible valuation. Neither outcome is automatic.

- `A` 80–100 / 8.0–10.0: attractive current buying case, supported development upside and practical exit liquidity; a conditional phased-entry candidate
- `B` 65–79 / 6.5–7.9: some buying merit with material uncertainty; a cautious initial position only where the entry conditions hold
- `C` 50–64 / 5.0–6.4: marginal/speculative at this valuation; observe and wait for better price or evidence
- `D` 30–49 / 3.0–4.9: poor current entry; avoid new buying and reassess only after specified improvements
- `F` 0–29 / 0.0–2.9, or an exclusion override: **当前不考虑**; unsuitable current economics, unresolved critical investability, confirmed failure, or verified malicious conduct

Always show confidence `high/medium/low` and two to four decisive reasons. Compute internally in whole points out of 100; show the supported final score divided by 10 to one decimal, such as `综合：A / 8.4（满分 10）`. Do not add plus/minus grades. `F` does not itself allege fraud: specify `估值/风险收益不合适`, `关键证据不足，暂不考虑`, `已确认失败/弃项`, or `已证实恶意行为`, as applicable. Missing evidence is not a neutral passing score.

## Build one overall grade

1. Score the relevant category below using the existing weights (100 total). Include current holder-cost, launch-sale, and liquidity findings from [holders-and-launch.md](holders-and-launch.md) in its 15-point token/holder-health dimension. Include proven operator conduct in integrity, explaining distinct effects instead of duplicating deductions.
2. Add a separate **current valuation adjustment from -30 to +15 points**. Keep price attractiveness out of the base score: product revenue and token capture belong in the base, while their relationship to price belongs in this adjustment. Never add a second holder-risk adjustment for facts already scored in holder health.
3. Clamp the adjusted score to 0–100, then apply evidence/risk ceilings. For a numeric ceiling, cap the effective score at that band's maximum (for example, `C` at 64 and `D` at 49), so the headline grade and score agree. Retain the uncapped arithmetic and name the binding reason in the explanation. A disqualifying override produces `F / 不考虑（否决项）`; when evidence cannot support a numeric result, show `暂不评分` instead of fabricating zero or pairing `F` with a misleading high headline score.
4. Report the headline grade/score, confidence, odds and strategy using the companion format. Under it explain `category base X/100; valuation +Y/-Y; adjusted Z/100; cap/override; final result`. Explain valuation and on-chain contributions even in a short answer. Neither a category base score nor a large hypothetical market-cap target substitutes for the overall grade.

## Current valuation adjustment

Obtain a current timestamped price, circulating market cap and supply basis, FDV, circulating/total supply relationship, liquidity/quote depth, volume quality, and material unlocks. Keep token market cap, FDV, treasury assets, and any underlying company's equity value separate. If circulation is unverified, explicitly label an FDV-based assessment; do not relabel FDV as market cap.

- **Applications:** compare valuation with live usage, retained/paying customers, sustainable revenue, growth, and the portion that actually reaches this token. Compare matched peers with dated sources and consistent definitions; use scenarios where no suitable peers exist. Avoid annualizing a launch-day fee spike as durable earnings. Treasury value or protocol revenue is not a holder valuation floor without enforceable rights and a usable realization route.
- **Memes:** compare valuation with independent reach, catalyst strength/lifecycle, community formation and staying power, holder/trader growth, and liquid peers at a comparable stage. Explain how much narrative success is already priced in. Do not require application revenue or use historical meme peaks as a guaranteed target.
- **Both:** distinguish genuinely inexpensive from merely a small number. A low unit price, tiny float/high FDV, manipulated pool price, nearly empty pool, collapsing demand, or large pending supply is not proof of cheapness. High absolute market cap alone is not proof of overvaluation.

Use these adjustment anchors, with a reason for the chosen whole-number value:

| Adjustment | Evidence needed |
| --- | --- |
| +10 to +15 | Substantial undervaluation supported by a defensible peer/scenario range and executable liquidity; no binding critical risk |
| +1 to +9 | Modestly favorable price relative to category evidence, with acknowledged uncertainty |
| 0 | Broadly fair valuation or no supported pricing advantage; never call missing data fair value |
| -1 to -14 | Meaningful optimism already priced in or a valuation premium unsupported by adoption/attention |
| -15 to -30 | Extreme premium, weak remaining upside relative to downside, or price requiring implausible growth/attention |

Build downside, base and conditional upper valuation ranges from development milestones under [valuation-and-strategy.md](valuation-and-strategy.md), then derive entry zones from that opportunity and its risks. Mark unsupported valuation `Unknown` and use no positive adjustment, with the evidence cap below. If no numeric range is supportable, say so and use a concrete condition. An ordinary but credible project may move up on price, while an excellent expensive project may move down. Cheapness never overrides safety failures, severe sell-pressure caps, or freshness/evidence ceilings. An economic `F` may improve after sufficient repricing or verified development; a confirmed rug is not rehabilitated by a lower price.

## Holder risk and evidence ceilings

Use current positions, cost coverage, realized and unrealized profits, and launch-cohort sales together; the companion reference defines the calculations and evidence boundaries.

- Large unrealized gains combined with concentrated remaining low-cost supply, little verified cost-basis reset, and shallow executable depth reduce the holder-health score. High profits alone do not prove low turnover or an imminent dump.
- If verified remaining insider/early-winner inventory could overwhelm observed exit depth and observed selling or weak demand corroborates that risk, cap at `D`; use `F / 当前不考虑` for an extreme overhang with negligible practical exit capacity. State quantities, dates, and the liquidity comparison. There is no universal profit multiple that proves this condition.
- A substantially exited launch cohort may have less remaining overhang; a wallet transfer is not proof of exit. Past realized profit without a remaining position is not current sellable inventory. Confirmed rug behavior still forces `F` even after insiders finish selling.
- Materially missing/stale valuation or an inability to assess large-holder cost/remaining-inventory or launch-sale exposure prevents a strong current-buy call: use a **provisional grade no higher than `C`, low confidence**, specify coverage and the missing evidence, and use lower grades where known risks warrant them. Partial gaps need not trigger this ceiling if bounded evidence still answers the material risk; explain why.
- If target token identity, sellability, or usable liquidity itself cannot be established, an identified candidate receives **provisional `F / 当前不考虑：关键证据不足`, low confidence**, with no manufactured numeric score. Do not call it a scam. If no unique token can be identified at all, mark rating `无法评级：标的未确认` and resolve identity rather than grading an invented asset.
- `A` requires a supported favorable/fair entry valuation, credible development upside, adequate holder/launch coverage, practical exit liquidity, at least medium confidence, and no unresolved critical flaw. A large theoretical upside alone cannot award `A`. If only these requirements fail, cap at `B` (79), unless another ceiling is stricter.

Confidence reflects source quality, freshness and coverage, not enthusiasm. API errors and missing fields never count as zero profits, zero bundles, zero sales, or passing checks.

## Application score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Live product and usage proof | 25 | Usable product, retained users, real activity rather than wallet farming |
| Revenue and token value capture | 20 | Verified revenue, sustainability, enforceable holder capture; price relationship is assessed separately |
| Differentiation and moat | 15 | Real advantage, integrations, switching costs, defensibility |
| Team, contract and operations | 15 | Delivery history, transparency, security, admin/custody controls |
| Token/liquidity/distribution | 15 | Supply/unlocks, concentration, exit depth, large-holder cost/profit/remaining inventory, launch-bundle sales |
| Execution and regulatory durability | 10 | Roadmap credibility, dependencies, jurisdiction/RWA exposure |

Announced features do not count as live usage. Reported revenue does not count as holder value capture unless the link is verified.

## Meme score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Meme power and cultural impact | 25 | Recognition, clarity, originality, remixability, crypto relevance |
| Organic community voice | 25 | Unique creators/participants, non-official mentions, sustained discussion |
| Holder and liquidity health | 15 | Concentration/clusters, pool depth, verified turnover, large-holder realized/unrealized profits, launch-bundle sales and remaining inventory |
| Narrative durability | 15 | Longevity beyond one event/KOL, adaptability without identity loss |
| Catalysts and distribution | 10 | Reach, integrations/listings/events, breadth rather than one-account dependence |
| Contract/operator integrity | 10 | Sellability, privileged controls, launchpad/operator behavior |

Do not penalize a pure Meme merely for lacking application utility. Do penalize fake partnerships, purchased/botted community, manufactured engagement, insider concentration, or a meme that has no reach beyond the official account.

For meme and event coins, prioritize the following evidence inside the dimensions above:

- **Event heat and timing:** reach, recency, rate of propagation, whether the token captured the event before saturation, and whether price/volume followed a verifiable catalyst.
- **Emotional force:** how strongly the meme transmits humor, outrage, conflict, nostalgia, aspiration, identity, or surprise; clarity and remixability matter more than elaborate lore.
- **Celebrity/supporter distance:** official origin, explicit exact-token endorsement, direct project interaction, underlying-event participation, or mere attention hijacking. Only the first three count as token-specific support, with materially different strength.
- **Community fit:** established organic community for older memes; for newly occurring events, formation velocity, breadth, independent creators, holder/trader conversion, and continued activity after the initial spike. Do not demand pre-existing coin community from a same-day event.
- **Launch quality:** launchpad mechanics, bundle and sniper exposure, creator/insider clusters, current concentration, liquidity custody, and the narrative relevance of the paired asset.
- **Profit overhang:** early cost bases, realized and unrealized winner concentration, extreme multiples, and whether liquidity can absorb likely exits. Current holder percentages alone are insufficient.

When useful, supplement the mandatory overall current-buy grade with three distinct judgments: `meme/catalyst quality`, `token launch and distribution`, and `current valuation/entry risk`.

## F exclusions and integrity overrides

Use `F` whenever the current buying case should not be considered, including an extremely poor score or unresolved critical investability. Distinguish these potentially revisable exclusions from verified misconduct/failure. For any `F`, the strategy must be `不买入/不考虑`; do not append a routine dip-buy zone or phased-buy plan that contradicts the exclusion. State the evidence or economic changes needed for a new review, where meaningful.

A verified honeypot, actual unauthorized mint/drain, deliberate false official-stock/issuer claim, confirmed compromised account used to promote the token, or removable liquidity deliberately misrepresented as irrevocably locked forces `F` regardless of narrative strength or low valuation. Confirmed rug liquidity removal, deployer/insider dumping that collapses the market, blocked selling, stolen funds, or other completed rug conduct also forces `F`. Explain the exact evidence and do not disguise it as an ordinary low score. Ordinary creator sales, LP rebalancing, or a verified liquidity migration alone are not completed rug conduct.

## Freshness downgrades and rating caps

Newness is not automatically fraud. Its rating effect depends on category. It materially reduces evidence for an application's delivery, reputation, usage, revenue, and operator integrity. For a pure meme or genuine event coin, rapid creation can be part of the opportunity: newness primarily limits confidence and proof of durability, while the current grade should be driven by catalyst quality, emotional transmission, independent reach, launch fairness, distribution, and profit overhang. Never award points for a polished launch package merely because it looks complete.

Use these default signals, adjusted when the chain or market context makes another window more meaningful:

- **Acute freshness:** domain, first project-relevant X activity, token deployment, or pool/trading start occurred within the last 7 days.
- **New footprint:** the same evidence is no older than 30 days.
- **Uncorroborated launch:** no credible independent developer, user, investor, partner, established account, usage record, or code history predates or independently supports the launch.
- **Template shell:** the site/docs present a product or revenue concept, but there is no working flow or independently verifiable usage, revenue, integrations, repository history, or operator record.

Apply the following constraints:

- For applications, two or more freshness signals concentrated within days must lower the relevant grade by at least one band versus the feature-only assessment, and the report must name the dates causing the downgrade.
- For applications, a recent domain + recent/recycled X presence + new token + no credible independent corroboration is normally capped at `C`, even if the narrative and website are polished.
- If that application cluster also includes an anonymous/no-history operator and a template shell with no live product or usage, the application grade is normally `D`.
- Do **not** mechanically apply those application freshness caps to a pure meme. A same-day event meme may earn a strong category score when the catalyst is authentic and high-reach, emotional transmission is strong, independent propagation is visible, and launch/distribution are healthy. Its overall current-buy grade must still account for valuation, profit overhang, and evidence ceilings. Apply lower confidence or weak durability where history is short, and downgrade for fabricated endorsement, attention hijacking presented as official support, bundled/insider-heavy launches, excessive early-profit overhang, or engagement confined to official/raid accounts.
- A new meme with no real catalyst, no independent propagation, poor distribution, and only a newly created promotional account remains `D` or `C` as the evidence supports; newness alone is not the reason.
- Verified abandonment, deleted socials/site with no surviving official operation, a liquidity rug/drain, blocked selling, deployer dumping that collapses the market, deliberate fabricated partnerships/metrics used to sell the token, or a launch shell that has already collapsed forces `F`.

Use `F` for outcome failure as well as proven malicious conduct. A token/project that has effectively gone to zero, lost functional liquidity, and no longer has a working product or active operator is `F` even when intent cannot be proven. State whether the basis is `confirmed malicious/rug` or `failed/abandoned`; do not accuse operators of fraud when only failure is proven.

Do not double-count the same fact mechanically across every dimension. Explain how short history prevents verification of product usage, team execution, community durability, or operator integrity. State what minimum passage of time and observable evidence could lift the cap.

End with what could change the current-buy grade: a better or worse valuation, verified holder cost-basis reset and remaining launch exposure, a verified issuer listing, real distribution transactions, retained-user data, audited controls, improved liquidity, or sustained organic community growth. On follow-ups, compare with the previous dated snapshot and explain whether the change came from fundamentals, price, holder inventory, or new evidence.
