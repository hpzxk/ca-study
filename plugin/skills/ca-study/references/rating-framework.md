# Application and Meme current-buy rating framework

Read this reference for every project/token investigation and always give one overall `A/B/C/D/F` current-buy grade per assessed asset, without plus/minus suffixes. First classify the token as `application`, `meme`, or `hybrid`. A pure meme receives `Application: N/A`, not a failing application grade. For a hybrid, assess both categories, choose and explain the dominant investment thesis before scoring, and use that category as the base. If both are material, disclose explicit weights summing to 100% and combine the two base scores. Do not cherry-pick the higher score or let a meme narrative bypass a material application failure. Apply valuation once and the strongest relevant asset-level risk cap to the overall result. Always include the strategy and development scenarios in [valuation-and-strategy.md](valuation-and-strategy.md).

Grades measure evidence-adjusted **buying attractiveness at the current price/market cap**, including valuation and exit risk. A good project can be an unattractive purchase; a modest project can deserve a higher current-buy grade at a sufficiently low, defensible valuation. Neither outcome is automatic.

- `A` 80–100 / 8.0–10.0: attractive current buying case, supported development upside and practical exit liquidity; a conditional phased-entry candidate
- `B` 65–79 / 6.5–7.9: some buying merit with material uncertainty; a cautious initial position only where the entry conditions hold
- `C` 50–64 / 5.0–6.4: marginal/speculative at this valuation; observe and wait for better price or evidence
- `D` 30–49 / 3.0–4.9: poor current entry; avoid new buying and reassess only after specified improvements
- `F` 0–29 / 0.0–2.9, or an exclusion override: **当前不考虑**; unsuitable current economics, unresolved critical investability, confirmed failure, or verified malicious conduct

Show confidence `high/medium/low` and two to four decisive reasons before the final verdict. Compute internally in whole points out of 100; numeric scoring is optional supporting detail, never appended to the final `综合: A` line. Do not add plus/minus grades. `F` does not itself allege fraud: specify `估值/风险收益不合适`, `关键证据不足，暂不考虑`, `已确认失败/弃项`, or `已证实恶意行为`, as applicable. Missing evidence is not a neutral passing score.

## Build one overall grade

1. Choose the investment thesis and scoring mode before assigning points: `operating application`, `early application expectation trade`, or `meme near-term breakout`. Use the matching table (100 total) rather than selecting whichever produces the highest grade. For an early low-valued application, explicitly run the expectation-trade assessment; a weak product-maturity assessment alone cannot end the current-buy analysis. Always assess [tokenomics.md](tokenomics.md): allocation, circulation, dilution, burns, buybacks, dividends and effective holder capture. Include ownership design in tokenomics, current holder/launch selling and profits in holder health, and distinct operator conduct in integrity without duplicate deductions.
2. For operating applications and memes, add the existing **valuation adjustment from -30 to +15 points**, keeping price attractiveness out of the base score. The early-application table already gives relative valuation and rerating room 30 points: do **not** add the valuation adjustment again. Expectations can earn points for their evidenced plausibility and market opportunity, not for pretending future users/revenue already exist.
3. Clamp the adjusted score to 0–100, then apply justified evidence/risk ceilings. For a numeric ceiling, cap the effective score at that band's maximum (for example, `C` at 64 and `D` at 49) so the final letter agrees with the internal score. Explain any uncapped arithmetic and binding reason before the final block. A disqualifying override sets the grade to `F`; if numeric evidence is inadequate, do not fabricate zero or another score. The final `综合` field is always the letter alone.
4. Put the scoring explanation before the final five-line verdict. For operating applications/memes, explain `base + valuation adjustment; caps; final grade`; for early applications, explain the expectation score and its embedded valuation contribution. State how tokenomics strengthens or weakens the grade and which distribution/capture evidence drives that effect. Confidence, price zones and the choice of a small entry versus waiting must agree with that judgment. Neither a product-maturity score nor a large hypothetical target substitutes for the overall grade.

## Current valuation adjustment

Obtain a current timestamped price, circulating market cap and supply basis, FDV, circulating/total supply relationship, liquidity/quote depth, volume quality, and material unlocks. Keep token market cap, FDV, treasury assets, and any underlying company's equity value separate. If circulation is unverified, explicitly label an FDV-based assessment; do not relabel FDV as market cap.

- **Applications:** compare current valuation with product/narrative credibility, development expectations, live usage where present and token capture. For pre-revenue/early projects, compare matched peers and the discount for uncertain delivery rather than requiring mature earnings first. Use dated sources and consistent definitions, or scenarios where no peers exist. Avoid annualizing launch fees as durable earnings. Unreconciled treasury value receives no verified floor credit, but does not automatically prohibit a small thesis based on relative valuation or a credible near-term catalyst.
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

Build downside, base and conditional upper valuation ranges from development milestones under [valuation-and-strategy.md](valuation-and-strategy.md), then derive entry zones from that opportunity and its risks. Mark unsupported valuation `Unknown` and use no positive adjustment, with the evidence treatment below. If no numeric range is supportable, say so and use a concrete condition. An ordinary but credible project may move up on price, while an excellent expensive project may move down. Cheapness never overrides safety failures or justified critical-risk caps. An economic `F` may improve after sufficient repricing or verified development; a confirmed rug is not rehabilitated by a lower price.

## Tokenomics, holder risk and evidence ceilings

Use current positions, cost coverage, realized and unrealized profits, and launch-cohort sales together; the companion reference defines the calculations and evidence boundaries.

- Tokenomics is a substantial standalone component: **35 points for operating applications, 30 for early applications, and 25 for memes**. Use the component weights and evidence anchors in [tokenomics.md](tokenomics.md). A large burn percentage, low reported market cap or high promised payout never earns an automatic upgrade. Assess remaining insider ownership, net dilution, actual holder benefit and the revenue denominator together.
- If an operating-application thesis depends on product earnings but verified rules direct value elsewhere and provide neither meaningful holder capture nor credible required token demand, cap that thesis at `C`. Explain the actual missing economic link. An early plausible capture mechanism awaiting delivery is different: lack of mature payout history alone does not trigger this ceiling. A pure meme is not required to distribute income.
- Apply the inventory/exit ceilings below to verified material unlocks, emissions or treasury releases within the investment horizon as well as current holder inventory. No fixed team-allocation, burn or payout percentage automatically forces a grade; quantify who can sell, at what cost, when, and against what demand/depth. Confirmed deceptive payout or burn claims used to sell the token fall under the integrity overrides.
- Large unrealized gains combined with concentrated remaining low-cost supply, little verified cost-basis reset, and shallow executable depth reduce the holder-health score. High profits alone do not prove low turnover or an imminent dump.
- If verified remaining insider/early-winner inventory could overwhelm observed exit depth and observed selling or weak demand corroborates that risk, cap at `D`; use `F / 当前不考虑` for an extreme overhang with negligible practical exit capacity. State quantities, dates, and the liquidity comparison. There is no universal profit multiple that proves this condition.
- A substantially exited launch cohort may have less remaining overhang; a wallet transfer is not proof of exit. Past realized profit without a remaining position is not current sellable inventory. Confirmed rug behavior still forces `F` even after insiders finish selling.
- Missing/stale price, supply basis or liquidity that prevents a meaningful current-entry comparison must be refreshed or reported as unrateable for price attractiveness; do not invent an undervaluation bonus. Distinguish this from incomplete product delivery, treasury reconciliation, or detailed holder cost basis. Those maturity/history gaps alone do **not** impose a blanket `C/D` cap or require waiting for full proof. Attempt the holder/launch checks, state what is unknown and how much remaining concentration is observable, and use lower confidence, smaller initial exposure and stricter add conditions for manageable uncertainty. If even a bounded view of material insider inventory/control cannot be established, explain that specific risk and cap at `C` or lower; this is not a missing-field shortcut.
- If target token identity, sellability, or usable liquidity itself cannot be established, an identified candidate receives **provisional `F / 当前不考虑：关键证据不足`, low confidence**, with no manufactured numeric score. Do not call it a scam. If no unique token can be identified at all, mark rating `无法评级：标的未确认` and resolve identity rather than grading an invented asset.
- `A` requires supported favorable/fair valuation, credible near-term upside, bounded material holder/launch risk, practical exit liquidity, at least medium confidence, and no unresolved critical flaw. Full product maturity or every holder's exact cost is not required. A large theoretical upside alone cannot award `A`. If only these requirements fail, cap at `B` (79), unless another ceiling is stricter. An early speculative `B` can justify `少量买入` despite low confidence when tradability, observable risk, relative discount and catalysts support it; label the speculation explicitly.

Confidence reflects source quality, freshness and coverage, not enthusiasm. API errors and missing fields never count as zero profits, zero bundles, zero sales, or passing checks.

## Application score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Tokenomics and holder economics | 35 | Supply/net dilution 8, allocation/alignment 7, effective holder capture 20; verified burn/buyback/dividend ratios, funding, execution and rights |
| Live product and usage proof | 20 | Usable product, retained users, real activity rather than wallet farming |
| Operating revenue quality | 10 | Real recurring external revenue, cost and incentive coverage; holder allocation is scored in tokenomics |
| Differentiation and moat | 10 | Real advantage, integrations, switching costs, defensibility |
| Team, contract and operations | 10 | Delivery history, transparency, security, admin/custody controls |
| Current holder and liquidity health | 10 | Exit depth, large-holder cost/profit/remaining inventory, turnover and launch-cohort sales; structural allocation belongs in tokenomics |
| Execution and regulatory durability | 5 | Roadmap credibility, dependencies, jurisdiction/RWA exposure |

Announced features do not count as live usage. Reported revenue does not count as holder value capture unless the link is verified.

## Early application expectation score

Use for a pre-revenue or incompletely delivered application whose buy thesis is a small, early position before a near-term milestone or narrative repricing. Select it because of the actual investment stage, not to rescue a proven failed project. Keep the operating application's maturity assessment as context, not a ceiling on the expectation trade.

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Relative valuation and repricing room | 30 | Current market cap/FDV versus genuinely comparable tokens; justified discount, supply, realistic nearby valuation range |
| Tokenomics and plausible holder economics | 30 | Supply/net dilution 8, allocation/alignment 7, plausible capture 15; distinguish credible future rights/demand from already executed burns/buybacks/dividends |
| Product/narrative credibility and near-term milestone | 15 | Coherent proposition, independent implementation/development evidence, a concrete catalyst and feasible timing |
| Attention, demand and executable liquidity | 10 | Early discovery, independent interest/buyers, sufficient entry/exit capacity and remaining room before saturation |
| Operator and contract risk | 5 | Observable delivery/identity/code evidence, controls and sellability; unknown is not verified safety |
| Current holder and launch overhang | 10 | Traced remaining early inventory, holder profits, observed sales and bounded cost/launch uncertainty; avoid repeating allocation-design deductions |

Before giving a low-valued application `D`, answer: what matched peer costs more today, is its premium justified, what can reprice this token before full delivery, and is a small entry attractive at the present discount? If there is no suitable peer, use a stated scenario instead of manufacturing one. Missing mature product metrics cannot be the sole reason to stop at `D`.

If the expectation case supports a higher grade, recompute the **final current-buy grade** using this mode. Do not leave a maturity-derived `D` in the headline while appending a contradictory small-buy suggestion. Conversely, a small market cap alone does not force an upgrade when demand, credibility, liquidity or relative value is absent.

Show a compact peer comparison when peers exist: exact tokens, observation time, circulating market cap/FDV, product/stage, rights/capture, liquidity, holder risk, near-term catalyst, and reasons for premium/discount. Similar ticker/category alone is not similarity. A substantially cheaper comparable token can receive a higher current-buy grade even with ordinary fundamentals; a more developed expensive token can receive a lower one.

Explicitly compare **small entry now** with **wait for confirmation**. Identify what uncertainty the current discount compensates for, what verification could unlock a rerating, and the possible valuation cost of waiting. Use incomplete delivery/full treasury reconciliation/detailed holder costs as add-position or reassessment conditions when they are not essential to the current small-entry thesis. Do not erase a material unresolved custody/solvency or sellability failure by calling it early stage.

If later price outcomes are supplied as feedback, use them to inspect the decision process, not to retroactively manufacture a winning forecast. A hypothetical $600k token versus a materially higher-valued similar peer can justify a different entry grade on contemporaneous evidence; a later 6× price move is not itself evidence that the earlier rating should have been `A`. Keep user-reported retrospective prices unverified unless separately researched. Do not hardcode any named example, launchpad or dollar threshold as an automatic buy.

## Meme score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Tokenomics and distribution alignment | 25 | Supply/float/net dilution 10, allocation/alignment 10, holder incentives 5; verify burns/buybacks/dividends when claimed, without requiring income for a pure meme |
| Meme power and emotional transmission | 15 | Recognition, clarity, originality, remixability, crypto relevance and timely emotional appeal |
| Organic community formation | 15 | Independent creators/participants, growth velocity, non-official mentions and conversion into traders/holders |
| Current holder and liquidity health | 5 | Pool depth, verified turnover, large-holder realized/unrealized profits, launch-bundle sales and remaining inventory; severe risks still impose binding ceilings |
| Near-term breakout setup | 20 | Concrete 24–72 hour / 7-day catalyst, accelerating independent attention and demand, room to expand within 1–2 months |
| Launchpad support and distribution | 15 | Exact platform, incentives/capability, token-specific promotion/funding/liquidity actions, relevant recent track record and organic alternatives |
| Contract/operator integrity | 5 | Sellability, privileged controls, launchpad/operator behavior; integrity overrides remain binding regardless of weight |

Do not penalize a pure Meme merely for lacking application utility. Do penalize fake partnerships, purchased/botted community, manufactured engagement, insider concentration, or a meme that has no reach beyond the official account.

Default to a **1–2 month** opportunity horizon and prioritize whether an outbreak can form in the **next 7 days**, with 24–72 hour checkpoints for very new coins. Assess narrative ignition, independent spread, buyer conversion, liquidity and low-cost supply together. Do not substitute a 6–12 month vision for the current entry. No credible near-term catalyst plus fading attention/demand materially weakens the grade and favors reducing the waiting window; one quiet week alone is not proof of death or an automatic `F`.

Always assess launchpad support using [pools-and-launchpads.md](pools-and-launchpads.md). A platform's incentives, resources and relevant successes can support an explicitly conditional hypothesis of assistance; token-specific actions are stronger evidence. Being created on a platform does not establish endorsement or guaranteed price support. Concentrated platform/market-maker control may create both a short-term catalyst and exit risk; score these separately and never reward suspected manipulation as a safety feature.

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

## Project age and stage uncertainty

Newness is not automatically fraud. Its rating effect depends on category. It materially reduces evidence for an application's delivery, reputation, usage, revenue, and operator integrity. For a pure meme or genuine event coin, rapid creation can be part of the opportunity: newness primarily limits confidence and proof of durability, while the current grade should be driven by catalyst quality, emotional transmission, independent reach, launch fairness, distribution, and profit overhang. Never award points for a polished launch package merely because it looks complete.

Use these default signals, adjusted when the chain or market context makes another window more meaningful:

- **Acute freshness:** domain, first project-relevant X activity, token deployment, or pool/trading start occurred within the last 7 days.
- **New footprint:** the same evidence is no older than 30 days.
- **Uncorroborated launch:** no credible independent developer, user, investor, partner, established account, usage record, or code history predates or independently supports the launch.
- **Template shell:** the site/docs present a product or revenue concept, but there is no working flow or independently verifiable usage, revenue, integrations, repository history, or operator record.

Apply the following constraints:

- For applications, recent domain/social/token dates weaken delivery-history evidence; record them and score only what is supported. They do not create an automatic letter downgrade or `C/D` ceiling on an expectation-based entry. Evaluate the early-application mode, relative valuation and the cost of waiting before deciding the final grade.
- A recent anonymous template shell without credible implementation, independent demand or a feasible catalyst earns weak credibility/demand points. If it also lacks a defensible relative-value case, `D` or `F` can be appropriate. Explain the combination rather than treating newness or missing mature metrics alone as disqualifying.
- For memes, same-day creation can be part of the opportunity. Judge the next week's catalyst, emotional transmission, independent propagation, launchpad support, distribution and current valuation. Apply lower confidence where history is short, and downgrade for fabricated endorsement, attention hijacking presented as official support, insider-heavy launches, excessive profit overhang or engagement confined to raid accounts.
- A new meme with no real catalyst, no independent propagation, poor distribution, and only a newly created promotional account remains `D` or `C` as the evidence supports; newness alone is not the reason.
- Verified abandonment, deleted socials/site with no surviving official operation, a liquidity rug/drain, blocked selling, deployer dumping that collapses the market, deliberate fabricated partnerships/metrics used to sell the token, or a launch shell that has already collapsed forces `F`.

Use `F` for outcome failure as well as proven malicious conduct. A token/project that has effectively gone to zero, lost functional liquidity, and no longer has a working product or active operator is `F` even when intent cannot be proven. State whether the basis is `confirmed malicious/rug` or `failed/abandoned`; do not accuse operators of fraud when only failure is proven.

Do not double-count the same fact across dimensions. Explain how short history limits evidence and what observable action could improve confidence or justify adding. Do not demand time to pass for its own sake or require full maturity before a small expectation trade.

End with what could change the current-buy grade: a better or worse valuation, verified holder cost-basis reset and remaining launch exposure, a verified issuer listing, real distribution transactions, retained-user data, audited controls, improved liquidity, or sustained organic community growth. On follow-ups, compare with the previous dated snapshot and explain whether the change came from fundamentals, price, holder inventory, or new evidence.
