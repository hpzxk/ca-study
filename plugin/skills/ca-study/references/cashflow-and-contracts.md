# Cash flow, distributions, and contract control

Use this reference for taxes, revenue, yield, dividends, rebates, buybacks, burns, holder rights, and privileged controls.

## Prove a distribution in layers

Separate: **configured** in code/storage, **funded** with actual value, **allocated** into entitlements, **paid** to holders, and **repeatable** without discretionary treasury action. Trace a representative flow when possible: swap/fee → collector/escrow → conversion/deposit → distribution/claim → recipient. Give pivotal addresses and transaction hashes and reconcile inflows, retained balances, payouts, and withdrawals over the same interval.

Do not infer holder income from a website counter or treasury balance. Use `0 paid` only after querying the correct contract and interval; otherwise say `not verified`. For stock-token rewards, independently verify the exact payout CA under the pool/issuer rules.

State payout asset, eligibility, snapshot timing, exclusions, claim/push model, formula/denominator, frequency, accrual, gas payer, and operator powers. Distinguish enforceable rights from revocable incentives.

## Contract controls

Inspect verified source and implementations for proxy/admin/upgrades, roles, minting, pause/blacklist/whitelist, wallet/trading gates, fee setters/ceilings/exemptions/recipients, arbitrary calls, delegatecall, sweeps/withdrawals, and router/sell-path differences. Check renounce claims against owner, roles, and proxy state.

Honeypot simulations are supporting evidence only and may miss delayed, allowlist, proxy-upgrade, router-specific, or targeted restrictions.

For concentrated liquidity, resolve the position NFT owner; an ERC-20 LP burn-address check is insufficient. Distinguish custody, timelock, and irrevocable lock. Admin-controlled withdrawal remains liquidity risk.
