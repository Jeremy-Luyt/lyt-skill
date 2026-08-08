#!/usr/bin/env python3
"""Basic repository-local self-test for ResearchOS templates and linters."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ("prompt_linter.py", ROOT / "templates" / "prompt-contract.md"),
    ("experiment_linter.py", ROOT / "templates" / "experiment-contract.md"),
    ("handoff_linter.py", ROOT / "templates" / "handoff.md"),
]


def main() -> int:
    # Templates intentionally contain placeholder text, so heading-level validation is the goal.
    failures = 0
    for script, target in CASES:
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).with_name(script)), str(target)],
            text=True,
            capture_output=True,
        )
        print(f"[{script}] {target.name}: rc={proc.returncode}")
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
