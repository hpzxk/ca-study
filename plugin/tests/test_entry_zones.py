import importlib.util
import pathlib
import unittest
from decimal import Decimal


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "ca-study" / "scripts" / "entry_zones.py"
SPEC = importlib.util.spec_from_file_location("entry_zones", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EntryZones(unittest.TestCase):
    def test_small_ath_example(self):
        result = MODULE.entry_zones(5000000, 1000000)
        self.assertEqual(result["drawdown_pct"], Decimal("80"))
        self.assertEqual(result["regular_zone_usd"], [750000, 1250000])
        self.assertEqual(result["reference_78_6_usd"], 1070000)
        self.assertEqual(result["extreme_zone_usd"], [550000, 600000])
        self.assertEqual(result["position"], "regular_candidate")

    def test_large_ath_example(self):
        result = MODULE.entry_zones(20000000, 4000000)
        self.assertEqual(result["regular_zone_usd"], [3000000, 6000000])
        self.assertEqual(result["reference_78_6_usd"], 4280000)
        self.assertEqual(result["extreme_zone_usd"], [2400000, 2400000])

    def test_exact_ten_million_uses_large_tier(self):
        result = MODULE.entry_zones(10000000)
        self.assertEqual(result["ath_tier"], "at_or_above_10m")
        self.assertEqual(result["regular_zone_usd"], [1500000, 3000000])
        self.assertEqual(result["exclude_below_usd"], 1200000)
        self.assertEqual(MODULE.entry_zones("9999999.99")["ath_tier"], "below_10m")

    def test_small_tier_edges_and_gap(self):
        for current, expected in [
            ("250000.01", "shallower_than_regular"),
            ("250000", "regular_candidate"),
            ("150000", "regular_candidate"),
            ("149999.99", "extended_watch"),
            ("120000.01", "extended_watch"),
            ("120000", "extreme_reference"),
            ("110000", "extreme_reference"),
            ("109999.99", "beyond_deep_drawdown_limit"),
        ]:
            with self.subTest(current=current):
                self.assertEqual(MODULE.entry_zones(1000000, current)["position"], expected)

    def test_large_tier_edges_and_gap(self):
        for current, expected in [
            ("3000000.01", "shallower_than_regular"),
            ("3000000", "regular_candidate"),
            ("1500000", "regular_candidate"),
            ("1499999.99", "extended_watch"),
            ("1200000.01", "extended_watch"),
            ("1200000", "extreme_reference"),
            ("1199999.99", "beyond_deep_drawdown_limit"),
        ]:
            with self.subTest(current=current):
                self.assertEqual(MODULE.entry_zones(10000000, current)["position"], expected)

    def test_fdv_remains_explicit(self):
        self.assertEqual(MODULE.entry_zones(5000000, basis="fdv")["basis"], "fdv")
        with self.assertRaises(ValueError):
            MODULE.entry_zones(5000000, basis="price")

    def test_rejects_bad_or_inconsistent_inputs(self):
        for value in (0, -1, "NaN", "Infinity", "invalid"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    MODULE.entry_zones(value)
                with self.assertRaises(ValueError):
                    MODULE.entry_zones(1000000, value)
        with self.assertRaises(ValueError):
            MODULE.entry_zones(1000000, 1000001)

    def test_without_current_only_derives_levels(self):
        result = MODULE.entry_zones(5000000)
        self.assertIsNone(result["drawdown_pct"])
        self.assertEqual(result["position"], "not_assessed")


if __name__ == "__main__":
    unittest.main()
