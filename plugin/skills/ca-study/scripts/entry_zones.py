"""Calculate the user's ATH drawdown presets; no market fetch or trade execution."""

import argparse
import json
from decimal import Decimal, InvalidOperation


def positive_decimal(value, name):
    try:
        number = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"{name} must be a finite positive number") from exc
    if not number.is_finite() or number <= 0:
        raise ValueError(f"{name} must be a finite positive number")
    return number


def entry_zones(ath, current=None, basis="market_cap"):
    """Use aligned USD valuation inputs. Decimal comparisons preserve boundary rules."""
    if basis not in ("market_cap", "fdv"):
        raise ValueError("basis must be market_cap or fdv")
    ath = positive_decimal(ath, "ath")
    current = None if current is None else positive_decimal(current, "current")
    if current is not None and current > ath:
        raise ValueError("current exceeds ATH; refresh ATH or align valuation bases")

    small = ath < Decimal("10000000")
    shallow = Decimal("0.75") if small else Decimal("0.70")
    extreme_deep = Decimal("0.89") if small else Decimal("0.88")
    regular_low = ath * Decimal("0.15")
    regular_high = ath * (1 - shallow)
    extreme_low = ath * (1 - extreme_deep)
    extreme_high = ath * Decimal("0.12")
    position = "not_assessed"
    if current is not None:
        if current < extreme_low:
            position = "beyond_deep_drawdown_limit"
        elif current <= extreme_high:
            position = "extreme_reference"
        elif current < regular_low:
            position = "extended_watch"
        elif current <= regular_high:
            position = "regular_candidate"
        else:
            position = "shallower_than_regular"

    return {
        "preset": "user_2026-09-30",
        "basis": basis,
        "currency": "USD",
        "ath_tier": "below_10m" if small else "at_or_above_10m",
        "ath_usd": ath,
        "current_usd": current,
        "drawdown_pct": None if current is None else (1 - current / ath) * 100,
        "regular_drawdown_pct": [shallow * 100, Decimal("85")],
        "regular_zone_usd": [regular_low, regular_high],
        "reference_78_6_usd": ath * Decimal("0.214"),
        "extreme_drawdown_pct": [Decimal("88"), extreme_deep * 100],
        "extreme_zone_usd": [extreme_low, extreme_high],
        "exclude_below_usd": extreme_low,
        "exclude_boundary_is_strict": True,
        "position": position,
        "scope": "Arithmetic only; verify ATH, supply basis, charts, continuity and tradability separately.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ath", required=True, help="Verified same-basis ATH USD valuation")
    parser.add_argument("--current", help="Current USD valuation using the same supply basis")
    parser.add_argument("--basis", choices=("market_cap", "fdv"), default="market_cap")
    args = parser.parse_args()
    try:
        result = entry_zones(args.ath, args.current, args.basis)
    except ValueError as exc:
        parser.error(str(exc))
    # Exact decimal strings avoid rounding a boundary into a different zone.
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
