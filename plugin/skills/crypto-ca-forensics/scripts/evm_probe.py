#!/usr/bin/env python3
"""Probe EVM bytecode, EIP-1967 implementation, and common token/pool views."""

from __future__ import annotations
import argparse, datetime as dt, json, re, sys, urllib.error, urllib.request
from typing import Any

SLOT = "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
CALLS = {"name": ("0x06fdde03", "string"), "symbol": ("0x95d89b41", "string"), "decimals": ("0x313ce567", "uint"),
         "totalSupplyRaw": ("0x18160ddd", "uint"), "owner": ("0x8da5cb5b", "address"), "paused": ("0x5c975abb", "bool"),
         "token0": ("0x0dfe1681", "address"), "token1": ("0xd21220a7", "address"), "factory": ("0xc45a0155", "address")}

def rpc(url: str, method: str, params: list[Any], timeout: float, ident: int) -> Any:
    body = json.dumps({"jsonrpc": "2.0", "id": ident, "method": method, "params": params}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", "User-Agent": "crypto-ca-forensics/1.1"})
    with urllib.request.urlopen(req, timeout=timeout) as response: payload = json.load(response)
    if "error" in payload: raise RuntimeError(json.dumps(payload["error"]))
    return payload.get("result")

def raw(value: str) -> bytes:
    return bytes.fromhex(value[2:] if value.startswith("0x") else value)

def decode(value: str, kind: str) -> Any:
    data = raw(value)
    if kind == "uint": return int.from_bytes(data, "big")
    if kind == "bool": return bool(int.from_bytes(data, "big"))
    if kind == "address": return "0x" + data[-20:].hex() if len(data) >= 20 and any(data[-20:]) else None
    if len(data) >= 64:
        offset = int.from_bytes(data[:32], "big")
        if offset + 32 <= len(data):
            size = int.from_bytes(data[offset:offset+32], "big"); end = offset + 32 + size
            if end <= len(data): return data[offset+32:end].decode(errors="replace")
    return data.rstrip(b"\x00").decode(errors="replace")

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("address"); p.add_argument("--rpc", required=True); p.add_argument("--timeout", type=float, default=15)
    a = p.parse_args(); observed = dt.datetime.now(dt.timezone.utc).isoformat()
    if not re.fullmatch(r"0x[0-9a-fA-F]{40}", a.address): p.error("address must be a 20-byte EVM address")
    try:
        chain = rpc(a.rpc, "eth_chainId", [], a.timeout, 1); block = rpc(a.rpc, "eth_blockNumber", [], a.timeout, 2)
        code = rpc(a.rpc, "eth_getCode", [a.address, "latest"], a.timeout, 3)
        impl = rpc(a.rpc, "eth_getStorageAt", [a.address, SLOT, "latest"], a.timeout, 4)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "observedAt": observed}, indent=2)); return 2
    views, failures = {}, {}
    for ident, (label, (selector, kind)) in enumerate(CALLS.items(), 10):
        try:
            value = rpc(a.rpc, "eth_call", [{"to": a.address, "data": selector}, "latest"], a.timeout, ident)
            if value in (None, "0x"): raise ValueError("empty result")
            views[label] = decode(value, kind)
        except Exception as exc: failures[label] = str(exc)
    code_bytes = max((len(code)-2)//2, 0); implementation = decode(impl, "address")
    print(json.dumps({"address": a.address, "observedAt": observed, "chainId": int(chain, 16), "blockNumber": int(block, 16),
                      "hasCode": code_bytes > 0, "codeBytes": code_bytes, "eip1967Implementation": implementation,
                      "successfulViews": views, "failedViews": failures,
                      "warnings": ["Other proxy patterns may exist.", "Failed owner/paused calls do not prove absence.", "Inspect source, roles and transactions."]}, indent=2)); return 0

if __name__ == "__main__": sys.exit(main())
