# Tokenomics: distribution, dilution, and holder economics

Read for every asset assessment. Tokenomics has its own substantial weight in [rating-framework.md](rating-framework.md): operating application 35/100, early application 30/100, and meme 25/100. Show how the findings strengthen or weaken the final current-buy grade and entry conditions. Do not merely append a token-allocation description after assigning the grade.

The user's reference [post by @sunburneugo](https://x.com/sunburneugo/status/2097580793388540096) motivates attention to holder capture and remaining dilution. Its token examples, payout ratios, returns and forecasts are the author's claims, not verified facts or permanent recommendations. Apply the general principle with fresh asset-specific evidence; do not adopt its numeric rejection thresholds or named favorites as rules.

## Fixed output contract

Use the exact `代币经济` labels and order in [SKILL.md](../SKILL.md#mandatory-tokenomics-format) for every asset investigation, even a short follow-up. The block must remain visible and self-contained; narrative elsewhere does not replace it. Retain unknown fields. Follow-up values may reference the dated earlier check, but say `沿用 YYYY-MM-DD 核查，未刷新` instead of presenting them as newly verified current data. Add sources/time/evidence state beside the relevant lines or immediately below the block.

### Field definitions

- **总量 / 流通百分比:** name the token and distinguish initial issuance, current `totalSupply` and enforceable maximum when they differ. Show circulating quantity divided by an explicitly named supply basis, with exclusions. Do not infer 100% circulation from fixed supply or subtract dead-address balances twice.
- **营收分配:** start with the income source and denominator (for example, total trading fees rather than trading volume). For every share, name the recipient, use and token: `平台 30%，发币者 35%，购买该发行项目代币并销毁 35%`. A launchpad project's buyback is not a buyback of the platform token. Give each real version its own line, with current/historical status, applicability and date when available. If only one model exists, use `当前版`; do not manufacture versions from this template. If a split is incomplete, label the remainder unknown instead of assigning it to the team.
- **利润分配:** preserve this user-requested label, but explicitly state whether the denominator is net profit after costs, distributable cash, or the platform's retained gross revenue. If the project calls gross revenue profit, write `实际口径为平台所得收入，未扣成本，非已核实净利润`. Name each destination and purpose, including operating budget, project-retained funds, holder dividends and protocol-owned liquidity. A team/operating allocation is not proof of realized net profit. A headline `75% / 20% / 5%` without this explanation fails the required format.
- **回购机制 / 当前回购比例:** state existence and execution separately (`有，已核实执行` / `项目方声称有，执行未核实` / `无，依据...` / `未核实`). In this fixed field, report cumulative verified market-purchased units of the exact assessed token divided by a named supply basis, normally initial issuance where meaningful, and give the observation cutoff. Show the numerator. A revenue allocation such as `75% 用于回购` belongs in the routing lines and must not be substituted here. Report revenue-funded versus treasury/deployer-funded purchases separately where known. If only one transaction or an incomplete period is checked, label that limited-period amount/ratio and leave the full cumulative ratio `未核实`. Do not extrapolate a lifetime figure from partial coverage. Transfers into a buyback wallet are not purchases. Repeated resale/repurchase can make cumulative purchases exceed 100%; flag turnover and distinguish net retained/burned amounts rather than calling that a removed-supply share.
- **销毁机制 / 当前销毁比例:** show verified irreversible removals of this token divided by a named supply basis and cutoff, normally the same initial basis used above. Separate supply-reducing burns from provably irrecoverable-address transfers that leave `totalSupply` unchanged. Identify initial/team inventory burns, transaction burns and market-buyback burns; deduplicate transfers followed by burns. LP-token destruction is not destruction of the assessed asset. Do not equate all dead-address balances with revenue-funded buybacks. Buyback and burn ratios may match only when independent purchase and irreversible-removal evidence supports both over the same scope; never fill one by copying the other.

For rebases, ongoing issuance, migrations or incomplete genesis data, use a defensible explicitly dated basis or `未核实`, not a fabricated common denominator. The numerical fields must identify their scope/time; record any source's differently defined displayed percentage separately. Supply percentages and cash-allocation percentages are different units and cannot be added. Sum only allocations with the same version, interval and denominator; explain any residual, rounding, overlap or conflict. Where useful, translate nested splits into an effective share of trading volume using the verified fee rate, without applying platform-wide volume to this specific asset without evidence.

### User-supplied Pons formatting example — not verified current facts

The following preserves the user's requested layout and illustrative numbers. It is not a factual Pons research result, an endorsement or a default parameter set. In actual research, independently verify every number, version, denominator, recipient and cutoff; replace the example values, add amounts/bases/status, and do not assume `30.34%` is still current or even uses the same definition for both fields.

```text
代币经济：
总量：未核实 / 流通百分比：未核实
营收分配：
v1版：平台 30%，发币者 70%
v2版：平台 30%，发币者 35%，回购发币项目并销毁 35%
利润分配：80% 购买 Pons 并销毁，20% 项目利润
回购机制：有   当前回购比例：30.34%
销毁机制：有   当前销毁比例：30.34%
```

When rendering an evidence-backed version, clarify that `回购发币项目` means buying that project's token, name the assessed platform token separately, and establish whether `项目利润` actually means retained revenue before costs. The abbreviated user example does not waive the field definitions above.

### Worked denominator example — fictional, arithmetic only

Assume token EXAMPLE has initial and current supply of 1,000,000,000 units, 800,000,000 independently verified circulating units, a 1% trading fee split 30% to the platform and 70% to creators, and a second split of platform receipts into 75% buyback-and-burn, 20% operations and 5% protocol-owned liquidity. Assume complete purchase history proves 20,000,000 units bought and transferred irrecoverably, while another 100,000,000 initial treasury units were also transferred irrecoverably; neither removal reduces `totalSupply`.

```text
代币经济：
总量：10 亿 EXAMPLE（初始发行及当前链上总量） / 流通百分比：8 亿 ÷ 10 亿 = 80%
营收分配：
当前版：每笔交易收取成交额 1% 的手续费；该手续费中平台获得 30%，发币者获得 70%
利润分配：实际分配平台所得收入，未扣成本；75% 购买 EXAMPLE 并销毁，20% 支付运营费用，5% 建立协议自有流动性；净利润未核实
回购机制：有，已执行   当前回购比例：累计回购 2,000 万 EXAMPLE ÷ 初始 10 亿 = 2%
销毁机制：有，已执行   当前销毁比例：累计不可恢复移除 1.2 亿 EXAMPLE ÷ 初始 10 亿 = 12%（初始库存 10%，回购销毁 2%；链上总量未减少）
```

In this fictional example, each $1,000 of eligible trading volume generates $10 fees: creators receive $7, and the platform's $3 routes $2.25 to buybacks, $0.60 to operations and $0.15 to liquidity. Thus the buyback budget is 0.225% of eligible trading volume, the cumulative purchased-supply ratio is 2%, and the cumulative burn/removal ratio is 12%. These are three distinct metrics. Buying and then burning the same tokens is one cash use. Real output needs primary sources and a dated verification scope instead of these fictional assumptions.

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

Before the unchanged five-line final verdict, include the mandatory fixed `代币经济` block defined above and in SKILL.md, then supplement allocation/insider share, circulation/FDV, upcoming dilution, dividends and rating impact. For each material number show basis/time and verified versus claimed state; use `未核实` for unavailable data and `不适用` only for mechanisms confirmed inapplicable. Include actual amounts as well as percentages where available. On short follow-ups, retain the fixed block, summarize material changes or unresolved items and label any reuse of dated prior evidence.

Explain whether the structure improves or weakens the current grade, why a low valuation does or does not compensate for it, and what changes would alter entry/add/review conditions. Better verified capture and limited dilution may justify a better grade or valuation range; concentrated low-cost supply and weak capture can reduce both despite an attractive product.

Feed the resulting net issuance, float releases, sustainable holder cash flow and control assumptions into [valuation-and-strategy.md](valuation-and-strategy.md). Keep per-token upside distinct from market-cap growth. Confirmed overwhelming supply/exit risk can impose a D/F ceiling under the framework; cosmetic burns and advertised distributions cannot undo it. Incomplete payout history alone must not erase a credible low-valued early expectation trade.
