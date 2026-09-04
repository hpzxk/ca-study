# Application and Meme rating framework

Use this reference whenever assigning `S/A/B/C/D/F`. First classify the token as `application`, `meme`, or `hybrid`. A pure Meme receives `Application: N/A`, not a failing application grade. A hybrid receives both grades; do not average them unless the user requests one overall score.

Grades measure current evidence-adjusted quality/attention worthiness, not future returns:

- `S` 85–100: exceptional, broad strong evidence, no unresolved critical flaw
- `A` 75–84: strong with limited material weaknesses
- `B` 60–74: credible or interesting but meaningful gaps/risks
- `C` 40–59: mostly speculative, weak proof, or structurally fragile
- `D` below 40: poor, highly speculative, structurally unsafe, or likely a short-lived shell, but not yet proven malicious, abandoned, or economically dead
- `F` override, not a numeric band: verified fraud/rug, disqualifying integrity or safety failure, confirmed abandonment, or an economically dead/near-zero project

Always show confidence `high/medium/low` and two to four decisive reasons. Scores are guides, not false precision; round to whole numbers and do not fill missing evidence with neutral points.

## Application score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Live product and usage proof | 25 | Usable product, retained users, real activity rather than wallet farming |
| Revenue and token value capture | 20 | Verified revenue, sustainability, holder capture and valuation relationship |
| Differentiation and moat | 15 | Real advantage, integrations, switching costs, defensibility |
| Team, contract and operations | 15 | Delivery history, transparency, security, admin/custody controls |
| Token/liquidity/distribution | 15 | Supply, concentration, exit liquidity, incentives, unlock pressure |
| Execution and regulatory durability | 10 | Roadmap credibility, dependencies, jurisdiction/RWA exposure |

Announced features do not count as live usage. Reported revenue does not count as holder value capture unless the link is verified.

## Meme score

| Dimension | Weight | What matters |
| --- | ---: | --- |
| Meme power and cultural impact | 25 | Recognition, clarity, originality, remixability, crypto relevance |
| Organic community voice | 25 | Unique creators/participants, non-official mentions, sustained discussion |
| Holder and liquidity health | 15 | Concentration, insider clusters, pool depth, turnover quality |
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

When useful, report three separate judgments instead of hiding the distinction in one score: `meme/catalyst quality`, `token launch and distribution`, and `current price-position risk`.

## Overrides

A verified honeypot, actual unauthorized mint/drain, deliberate false official-stock/issuer claim, confirmed compromised account used to promote the token, or removable liquidity deliberately misrepresented as irrevocably locked forces `F` regardless of narrative strength. Confirmed liquidity removal, deployer/insider dumping that collapses the market, blocked selling, stolen funds, or other completed rug conduct also forces `F`. Explain the exact evidence and do not disguise it as an ordinary low score.

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
- Do **not** mechanically apply those application freshness caps to a pure meme. A same-day event meme may earn a high current-attention grade when the catalyst is authentic and high-reach, emotional transmission is strong, independent propagation is visible, and launch/distribution are healthy. Apply low confidence or weak durability where history is short, and downgrade for fabricated endorsement, attention hijacking presented as official support, bundled/insider-heavy launches, excessive early-profit overhang, or engagement confined to official/raid accounts.
- A new meme with no real catalyst, no independent propagation, poor distribution, and only a newly created promotional account remains `D` or `C` as the evidence supports; newness alone is not the reason.
- Verified abandonment, deleted socials/site with no surviving official operation, drained or abruptly removed liquidity, blocked selling, deployer dumping, fabricated partnerships/metrics used to sell the token, or a launch shell that has already collapsed forces `F`.

Use `F` for outcome failure as well as proven malicious conduct. A token/project that has effectively gone to zero, lost functional liquidity, and no longer has a working product or active operator is `F` even when intent cannot be proven. State whether the basis is `confirmed malicious/rug` or `failed/abandoned`; do not accuse operators of fraud when only failure is proven.

Do not double-count the same fact mechanically across every dimension. Explain how short history prevents verification of product usage, team execution, community durability, or operator integrity. State what minimum passage of time and observable evidence could lift the cap.

End with what could change the grade: a verified issuer listing, real distribution transactions, retained-user data, audited controls, improved liquidity/distribution, or sustained organic community growth.
