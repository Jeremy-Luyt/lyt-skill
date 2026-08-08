#!/usr/bin/env python3
"""Lint a ResearchOS Prompt Contract using only the Python standard library."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

REQUIRED = [
    "Role", "Mission", "Context / Current Truth", "Research Question",
    "Observations", "Competing Hypotheses", "Evidence",
    "Constraints / Frozen Components", "Method / Minimal Discriminative Action",
    "Changed Variable", "Controlled Variables", "Success Criteria",
    "Failure Criteria", "Scientific Kill Switch / Stop Conditions",
    "Validation Plan", "Decision Rights", "Output Contract", "Provenance",
]


def headings(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    out: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[match.group(1).strip()] = text[match.end():end].strip()
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    text = args.path.read_text(encoding="utf-8")
    sections = headings(text)
    errors = []
    for name in REQUIRED:
        if name not in sections:
            errors.append(f"missing heading: {name}")
        elif not sections[name]:
            errors.append(f"empty section: {name}")
    if "Competing Hypotheses" in sections:
        n = len(re.findall(r"(?m)^\s*[-*]?\s*H\d+\s*:", sections["Competing Hypotheses"]))
        if n < 2:
            errors.append("Competing Hypotheses should normally contain at least H1 and H2")
    if errors:
        print("PROMPT_CONTRACT_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PROMPT_CONTRACT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
