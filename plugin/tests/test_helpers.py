import importlib.util, pathlib, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "ca-study" / "scripts"
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py"); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module
dex, evm = load("dex_snapshot"), load("evm_probe")

class Helpers(unittest.TestCase):
    def test_pair_identity_and_valuation(self):
        ca = "0x1111111111111111111111111111111111111111"
        pair = {"baseToken": {"address": ca, "symbol": "CA"}, "quoteToken": {"address": "0x"+"2"*40, "symbol": "RWA"}, "liquidity": {"usd": 10}, "marketCap": 20, "fdv": 30}
        out = dex.compact(pair, ca); self.assertEqual(out["queriedTokenRole"], "base"); self.assertEqual(out["marketCapUsd"], 20); self.assertEqual(out["fdvUsd"], 30)
    def test_evm_abi_decoding(self):
        self.assertEqual(evm.decode("0x"+(18).to_bytes(32,"big").hex(), "uint"), 18)
        value=b"CA"; encoded=(32).to_bytes(32,"big")+len(value).to_bytes(32,"big")+value.ljust(32,b"\x00")
        self.assertEqual(evm.decode("0x"+encoded.hex(), "string"), "CA")

if __name__ == "__main__": unittest.main()
