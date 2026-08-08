#!/usr/bin/env python3
"""Validate the ResearchOS behavioral benchmark specification with stdlib only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_CASE_FIELDS = {
    "id", "title", "task", "tags", "workflow_depth", "fresh_evidence",
    "required_behaviors", "forbidden_behaviors", "expected_decision",
}
ALLOWED_DEPTH = {"light", "standard", "high-stakes"}
ALLOWED_EVIDENCE = {"none", "targeted", "current", "latest"}
ALLOWED_DECISIONS = {"KEEP", "REJECT", "DEFER", "INVALID", "NO_FIXED_DECISION"}
REQUIRED_COVERAGE = {
    "trivial", "hypothesis", "fresh-evidence", "final-test", "invalid-run",
    "scope", "security", "frozen-baseline", "gpu", "meta-prompt",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path)
    ns = ap.parse_args()
    errors: list[str] = []

    try:
        data = json.loads(ns.path.read_text(encoding="utf-8"))
    except Exception as exc:  # JSON errors and IO errors are both fatal here.
        print(f"EVAL_SPEC_INVALID\n- cannot load JSON: {exc}")
        return 1

    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if not isinstance(data.get("skill_version"), str) or not data.get("skill_version"):
        errors.append("skill_version must be a non-empty string")

    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 10:
        errors.append("cases must contain at least 10 representative cases")
        cases = cases if isinstance(cases, list) else []

    seen_ids: set[str] = set()
    all_tags: set[str] = set()
    light_seen = False
    high_seen = False

    for index, case in enumerate(cases):
        prefix = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_CASE_FIELDS - case.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue

        cid = case["id"]
        if not isinstance(cid, str) or not cid:
            errors.append(f"{prefix} id must be a non-empty string")
        elif cid in seen_ids:
            errors.append(f"duplicate id: {cid}")
        else:
            seen_ids.add(cid)

        for field in ("title", "task"):
            if not isinstance(case[field], str) or not case[field].strip():
                errors.append(f"{cid}: {field} must be non-empty")

        tags = case["tags"]
        if not isinstance(tags, list) or not tags or not all(isinstance(x, str) and x for x in tags):
            errors.append(f"{cid}: tags must be a non-empty string list")
        else:
            all_tags.update(tags)

        if case["workflow_depth"] not in ALLOWED_DEPTH:
            errors.append(f"{cid}: invalid workflow_depth")
        light_seen |= case["workflow_depth"] == "light"
        high_seen |= case["workflow_depth"] == "high-stakes"

        if case["fresh_evidence"] not in ALLOWED_EVIDENCE:
            errors.append(f"{cid}: invalid fresh_evidence")
        if case["expected_decision"] not in ALLOWED_DECISIONS:
            errors.append(f"{cid}: invalid expected_decision")

        for field in ("required_behaviors", "forbidden_behaviors"):
            value = case[field]
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
                errors.append(f"{cid}: {field} must be a non-empty string list")

    missing_coverage = REQUIRED_COVERAGE - all_tags
    if missing_coverage:
        errors.append(f"missing benchmark coverage tags: {sorted(missing_coverage)}")
    if not light_seen:
        errors.append("benchmark must include a lightweight-workflow case")
    if not high_seen:
        errors.append("benchmark must include a high-stakes case")

    if errors:
        print("EVAL_SPEC_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"EVAL_SPEC_OK cases={len(cases)} tags={len(all_tags)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
