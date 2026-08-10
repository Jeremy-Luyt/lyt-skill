#!/usr/bin/env python3
"""Validate ResearchOS package structure and minimal SKILL frontmatter."""
from __future__ import annotations

import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[2]

REQUIRED_ROOT = ["README.md", "AGENTS.md", "CHANGELOG.md", "LICENSE"]
REQUIRED_SKILL = [
    "SKILL.md", "REFERENCES.md", "protocols/premise-audit.md",
    "protocols/dataset-integrity.md", "protocols/prompt-compiler.md",
    "protocols/evidence-acquisition.md", "protocols/prompt-evals.md",
    "protocols/final-test-governance.md", "protocols/handoff-continuity.md",
    "roles/data-benchmark-curator.md", "checklists/dataset-integrity-checklist.md",
    "templates/prompt-contract.md", "templates/experiment-contract.md",
    "templates/handoff.md", "evals/benchmark.json", "evals/rubric.md",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_ROOT:
        if not (REPO_ROOT / rel).is_file():
            errors.append(f"missing repository file: {rel}")
    for rel in REQUIRED_SKILL:
        if not (SKILL_ROOT / rel).is_file():
            errors.append(f"missing skill file: {rel}")

    skill_path = SKILL_ROOT / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm.get("name") != "research-os":
            errors.append("SKILL frontmatter name must be research-os")
        if len(fm.get("description", "")) < 80:
            errors.append("SKILL frontmatter description is missing or too short")
        if fm.get("license") != "MIT":
            errors.append("SKILL frontmatter license must remain MIT unless explicitly changed")
        if re.search(r"(?mi)^allowed-tools\s*:", text.split("---", 2)[1] if text.startswith("---") else ""):
            errors.append("SKILL frontmatter must not pre-approve allowed-tools without explicit methodology change")

    scripts = list((SKILL_ROOT / "scripts").glob("*.py"))
    if len(scripts) < 6:
        errors.append("expected ResearchOS validation scripts are missing")

    if errors:
        print("REPOSITORY_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"REPOSITORY_OK scripts={len(scripts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
