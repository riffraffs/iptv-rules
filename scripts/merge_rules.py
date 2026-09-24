#!/usr/bin/env python3
"""Pull upstream Clash rule lists, dedupe, domains first, IP rules last."""
import sys
import urllib.request

SOURCES = [
    "https://raw.githubusercontent.com/marcuccilli/gary/main/iptv_clash.yaml",
    "https://raw.githubusercontent.com/marcuccilli/Cathy/main/cathy_clash.yaml",
]
OUT = "iptv_merged.yaml"
IP_TYPES = {"IP-CIDR", "IP-CIDR6", "IP-ASN", "SRC-IP-CIDR"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "iptv-merge"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        if resp.status != 200:
            raise SystemExit(f"download failed {resp.status}: {url}")
        return resp.read().decode("utf-8")


def rules_of(text: str, url: str) -> list[str]:
    found = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("- "):
            continue
        item = line[2:].strip()
        if "," not in item:
            continue
        found.append(item)
    if not found:
        raise SystemExit(f"no rules parsed: {url}")
    return found


def main() -> None:
    domains, ips, seen = [], [], set()
    for url in SOURCES:
        for item in rules_of(fetch(url), url):
            key = item.upper()
            if key in seen:
                continue
            seen.add(key)
            kind = item.split(",", 1)[0].strip().upper()
            (ips if kind in IP_TYPES else domains).append(item)
    domains.sort(key=str.lower)
    ips.sort(key=str.lower)
    body = ["payload:"]
    body += [f"  - {item}" for item in domains]
    body += [f"  - {item}" for item in ips]
    body.append("")
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(body))
    print(f"wrote {OUT}: {len(domains)} domain, {len(ips)} ip")


if __name__ == "__main__":
    sys.exit(main())
