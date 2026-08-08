#!/usr/bin/env python3
"""Lint a ResearchOS HANDOFF file using only the Python standard library."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

REQUIRED = [
    "Current Truth", "Trusted Results", "Invalid / Untrusted Results",
    "Frozen Defaults and Protocols", "Rejected / Deferred Routes",
    "Active Hypotheses", "Known Risks / Blockers", "Running Jobs / External State",
    "Exact Next Action", "Provenance",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path)
    ns = ap.parse_args()
    text = ns.path.read_text(encoding="utf-8")
    headings = set(re.findall(r"(?m)^##\s+(.+?)\s*$", text))
    missing = [h for h in REQUIRED if h not in headings]
    if missing:
        print("HANDOFF_INVALID")
        for h in missing:
            print(f"- missing heading: {h}")
        return 1
    forbidden = ["password=", "api_key=", "private key", "BEGIN OPENSSH PRIVATE KEY"]
    lowered = text.lower()
    leaks = [x for x in forbidden if x.lower() in lowered]
    if leaks:
        print("HANDOFF_INVALID")
        for leak in leaks:
            print(f"- possible secret material: {leak}")
        return 1
    print("HANDOFF_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
