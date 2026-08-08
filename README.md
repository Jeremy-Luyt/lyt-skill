# LYT ResearchOS

[![ResearchOS CI](https://github.com/Jeremy-Luyt/lyt-skill/actions/workflows/researchos-ci.yml/badge.svg)](https://github.com/Jeremy-Luyt/lyt-skill/actions/workflows/researchos-ci.yml)

**Prompt-first, evidence-grounded, falsification-driven research engineering.**

LYT ResearchOS is a reusable Agent Skill for scientific and technical work. It turns ambiguous research tasks into auditable decisions by forcing an agent to reconstruct the current truth, acquire fresh evidence when needed, compile a task-specific execution prompt, test competing hypotheses with minimal discriminative experiments, pass engineering gates, and immediately preserve the resulting knowledge.

The methodology grew out of a personal research-engineering workflow. External prompting/agent documentation informs packaging and interoperability; the workflow itself is maintained as an explicit, versioned research protocol.

## Core ideas

- **Prompt first** — before any non-trivial implementation or experiment, the agent writes an inspectable Prompt Contract for the task. This is a task specification, not hidden chain-of-thought.
- **Just-in-time evidence acquisition** — if current external evidence can materially change a decision, search primary literature, official docs, GitHub implementations/issues/PRs, datasets, pretrained weights, and evaluation protocols before acting.
- **Observation before explanation** — keep facts, sources, inferences, hypotheses, assumptions, and unknowns separate.
- **Competing hypotheses before architecture changes** — do not turn one plausible mechanism into a conclusion until alternatives are tested.
- **Minimal discriminative experiments** — maximize information gained per unit of compute, engineering effort, and confounding.
- **Frozen baselines and protocols** — corrected baselines, splits, metrics, and final-test rules cannot drift silently.
- **Preflight → smoke → pilot → full** — expensive execution is earned through progressively stronger gates.
- **Builder / Challenger separation** — implementation and adversarial review are distinct roles; they should not edit the same experiment simultaneously.
- **KEEP / REJECT / DEFER / INVALID** — every completed experiment ends in an explicit decision.
- **Immediate knowledge retention** — prompts, evidence, experiments, decisions, and handoffs are updated as part of the work, not reconstructed later.

## Skill location

```text
.github/skills/research-os/
```

The package uses `SKILL.md` with YAML frontmatter plus optional protocols, roles, templates, checklists, examples, evals, and scripts.

## Install

With an agent host that supports repository skills, use `.github/skills/research-os/` directly or copy that directory into the host's supported project/user skill location.

## Recommended project truth sources

ResearchOS works best when the target project maintains equivalents of:

```text
PROJECT_PROFILE.md   # project definition, claims, frozen components, data/protocols
HANDOFF.md           # current truth and exact next action
EXPERIMENTS.md       # experiment ledger
DECISIONS.md         # KEEP / REJECT / DEFER / INVALID records
PROMPTS.md           # generated Prompt Contracts
```

If a project already has equivalent files, use them instead of duplicating state.

## Structure

```text
.github/skills/research-os/
├── SKILL.md
├── protocols/
├── roles/
├── templates/
├── checklists/
├── examples/
├── evals/
└── scripts/
```

Root-level `AGENTS.md` and `.github/copilot-instructions.md` explain how agents should maintain this repository itself.

## Validation and behavioral evals

ResearchOS tests the workflow itself as a versioned artifact.

Local static validation:

```bash
python .github/skills/research-os/scripts/self_test.py
python .github/skills/research-os/scripts/test_linters.py
python .github/skills/research-os/scripts/eval_spec_linter.py .github/skills/research-os/evals/benchmark.json
python .github/skills/research-os/scripts/repository_linter.py
```

GitHub Actions runs these checks on push and pull request across Python 3.11–3.13.

The 14-case behavioral benchmark covers workflow calibration, current evidence, hypothesis discipline, leakage/final-test governance, invalid runs, frozen baselines, GPU execution gates, scope control, shared-resource safety, metric semantics, source conflicts, and Builder/Challenger separation.

Static CI validates the package and benchmark specification; it does **not** prove that an LLM follows the methodology. Real behavioral evaluation requires running the benchmark tasks with ResearchOS enabled and scoring observable outputs using `evals/rubric.md`.

## Scientific integrity

ResearchOS forbids silent final-test tuning, post-hoc removal of inconvenient samples/ROIs, selective reporting, fabricated citations or experiments, unrecorded protocol changes, and treating a broken run as a scientific negative result.

Operational safety is part of research quality: destructive actions, shared compute, credential handling, checkpoint provenance, and data mutation require explicit boundaries.

## Version

Current release: **v0.1.0**. Evaluation/CI additions after v0.1.0 are tracked under `Unreleased` in `CHANGELOG.md`.

License: MIT (see `LICENSE`).
