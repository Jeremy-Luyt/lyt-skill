#!/usr/bin/env python3
"""Lint a ResearchOS Experiment Contract using only the Python standard library."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

REQUIRED = [
    "Experiment ID", "Question", "Hypothesis", "Baseline", "Changed Variable",
    "Controlled Variables", "Data / Split", "Metrics", "Success Criterion",
    "Failure Criterion", "Stop Condition", "Compute Budget", "Execution Gates",
    "Output Paths", "Provenance", "Final Decision", "Reusable Lesson",
]
VALID_DECISIONS = {"KEEP", "REJECT", "DEFER", "INVALID"}


def sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    result = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result[m.group(1).strip()] = text[m.end():end].strip()
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path)
    ns = ap.parse_args()
    data = sections(ns.path.read_text(encoding="utf-8"))
    errors = []
    for name in REQUIRED:
        if name not in data:
            errors.append(f"missing heading: {name}")
    decision = data.get("Final Decision", "")
    tokens = set(re.findall(r"\b(?:KEEP|REJECT|DEFER|INVALID)\b", decision))
    if decision and len(tokens) > 1:
        errors.append("Final Decision contains multiple decision statuses")
    if decision and tokens and not tokens.issubset(VALID_DECISIONS):
        errors.append("invalid decision status")
    if errors:
        print("EXPERIMENT_CONTRACT_INVALID")
        for e in errors:
            print(f"- {e}")
        return 1
    print("EXPERIMENT_CONTRACT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
