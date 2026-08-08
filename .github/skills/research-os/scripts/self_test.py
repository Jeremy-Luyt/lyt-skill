#!/usr/bin/env python3
"""Repository-local self-test for ResearchOS templates, benchmark, and package."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
CASES = [
    ("prompt_linter.py", ROOT / "templates" / "prompt-contract.md"),
    ("experiment_linter.py", ROOT / "templates" / "experiment-contract.md"),
    ("handoff_linter.py", ROOT / "templates" / "handoff.md"),
    ("eval_spec_linter.py", ROOT / "evals" / "benchmark.json"),
]


def main() -> int:
    failures = 0
    for script, target in CASES:
        proc = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / script), str(target)],
            text=True,
            capture_output=True,
        )
        print(f"[{script}] {target.name}: rc={proc.returncode}")
        if proc.stdout:
            print(proc.stdout.strip())
        if proc.stderr:
            print(proc.stderr.strip(), file=sys.stderr)
        failures += int(proc.returncode != 0)

    proc = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "repository_linter.py")],
        text=True,
        capture_output=True,
    )
    print(f"[repository_linter.py] rc={proc.returncode}")
    if proc.stdout:
        print(proc.stdout.strip())
    if proc.stderr:
        print(proc.stderr.strip(), file=sys.stderr)
    failures += int(proc.returncode != 0)

    if failures:
        print(f"SELF_TEST_FAILED failures={failures}")
        return 1
    print("SELF_TEST_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
