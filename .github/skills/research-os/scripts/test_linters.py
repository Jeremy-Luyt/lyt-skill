#!/usr/bin/env python3
"""Regression tests for ResearchOS contract linters using only stdlib."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"


def run(script: str, target: Path) -> int:
    return subprocess.run(
        [sys.executable, str(SCRIPT_DIR / script), str(target)],
        text=True,
        capture_output=True,
    ).returncode


def main() -> int:
    failures: list[str] = []
    valid = [
        ("prompt_linter.py", ROOT / "templates" / "prompt-contract.md"),
        ("experiment_linter.py", ROOT / "templates" / "experiment-contract.md"),
        ("handoff_linter.py", ROOT / "templates" / "handoff.md"),
    ]
    for script, target in valid:
        if run(script, target) != 0:
            failures.append(f"valid template rejected by {script}: {target.name}")

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        invalid_cases = {
            "prompt_linter.py": "# Prompt Contract\n## Role\nResearch Scientist\n",
            "experiment_linter.py": "# Experiment Contract\n## Experiment ID\nE-bad\n",
            "handoff_linter.py": "# HANDOFF\n## Current Truth\nUnknown\n",
        }
        for script, text in invalid_cases.items():
            path = tmpdir / f"{script}.md"
            path.write_text(text, encoding="utf-8")
            if run(script, path) == 0:
                failures.append(f"invalid fixture accepted by {script}")

        leaked = tmpdir / "handoff-secret.md"
        leaked.write_text((ROOT / "templates" / "handoff.md").read_text(encoding="utf-8") + "\npassword=do-not-commit\n", encoding="utf-8")
        if run("handoff_linter.py", leaked) == 0:
            failures.append("handoff_linter failed to reject secret-like material")

    if failures:
        print("LINTER_TESTS_FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("LINTER_TESTS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
