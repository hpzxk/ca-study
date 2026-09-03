#!/usr/bin/env python3
"""Fetch and normalize DEX pools for a token using DexScreener."""

from __future__ import annotations
import argparse, datetime as dt, json, sys, urllib.error, urllib.parse, urllib.request
from typing import Any

API = "https://api.dexscreener.com/latest/dex/tokens/{address}"

def ident(value: str) -> str:
    return value.lower() if value.startswith("0x") else value

def same(left: str | None, right: str) -> bool:
    return bool(left) and ident(left) == ident(right)

def token(value: Any) -> dict[str, Any]:
    value = value if isinstance(value, dict) else {}
    return {"address": value.get("address"), "symbol": value.get("symbol"), "name": value.get("name")}

def compact(pair: dict[str, Any], address: str) -> dict[str, Any]:
    base, quote = pair.get("baseToken") or {}, pair.get("quoteToken") or {}
    liq, vol, txns = pair.get("liquidity") or {}, pair.get("volume") or {}, pair.get("txns") or {}
    created = pair.get("pairCreatedAt")
    return {
        "chain": pair.get("chainId"), "dex": pair.get("dexId"), "poolAddress": pair.get("pairAddress"),
        "url": pair.get("url"), "queriedTokenRole": "base" if same(base.get("address"), address) else "quote",
        "baseToken": token(base), "quoteToken": token(quote), "priceUsd": pair.get("priceUsd"),
        "marketCapUsd": pair.get("marketCap"), "fdvUsd": pair.get("fdv"), "liquidityUsd": liq.get("usd"),
        "volume24hUsd": vol.get("h24"), "txns24h": txns.get("h24"),
        "createdAt": dt.datetime.fromtimestamp(created / 1000, tz=dt.timezone.utc).isoformat() if isinstance(created, (int, float)) else None,
    }

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("address"); p.add_argument("--chain"); p.add_argument("--limit", type=int, default=20); p.add_argument("--timeout", type=float, default=15)
    a = p.parse_args(); observed = dt.datetime.now(dt.timezone.utc).isoformat()
    url = API.format(address=urllib.parse.quote(a.address, safe=""))
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "ca-study/1.1"})
        with urllib.request.urlopen(req, timeout=a.timeout) as response: payload = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc), "observedAt": observed}, indent=2)); return 2
    pairs = []
    for pair in payload.get("pairs") or []:
        base, quote = pair.get("baseToken") or {}, pair.get("quoteToken") or {}
        if not (same(base.get("address"), a.address) or same(quote.get("address"), a.address)): continue
        if a.chain and str(pair.get("chainId", "")).lower() != a.chain.lower(): continue
        pairs.append(compact(pair, a.address))
    pairs.sort(key=lambda x: x.get("liquidityUsd") or 0, reverse=True); pools = pairs[:max(a.limit, 0)]
    out = {"query": {"address": a.address, "chainFilter": a.chain}, "observedAt": observed, "source": url,
           "pairCount": len(pairs), "chains": sorted({x["chain"] for x in pairs if x.get("chain")}),
           "primaryPool": pools[0] if pools else None, "primaryPoolMethod": "highest reported USD liquidity", "pools": pools,
           "warnings": ["Confirm discovery data against pool contracts/explorers.", "Ticker matches do not establish official stock/RWA status.", "Market cap and FDV are kept separate."]}
    print(json.dumps(out, ensure_ascii=False, indent=2)); return 0

if __name__ == "__main__": sys.exit(main())
