# LYT ResearchOS

[![ResearchOS CI](https://github.com/Jeremy-Luyt/lyt-skill/actions/workflows/researchos-ci.yml/badge.svg)](https://github.com/Jeremy-Luyt/lyt-skill/actions/workflows/researchos-ci.yml)

**Prompt-first, premise-audited, data-validated, evidence-grounded, falsification-driven research engineering.**

LYT ResearchOS is a reusable Agent Skill for scientific and technical work. It turns ambiguous research tasks into auditable decisions by forcing an agent to audit the question's premises, validate task-relevant dataset integrity, reconstruct the current truth, acquire fresh evidence when needed, compile a task-specific execution prompt, test competing hypotheses with minimal discriminative experiments, scale review effort to actual risk, pass engineering gates, and immediately preserve the resulting knowledge before the work session or context is lost.

The methodology grew out of a personal research-engineering workflow. External prompting/agent documentation informs packaging and interoperability; the workflow itself is maintained as an explicit, versioned research protocol.

## Core ideas

- **Premise first** — before solving a consequential question, check false/unsupported premises, logic jumps, missing information, and stale decision-critical claims.
- **Data before model interpretation** — validate dataset identity/version, format/schema, coordinates/units, sample pairing, split leakage, sampling, annotations, transforms/resampling, derived-data provenance, and representativeness before claim-bearing training or interpretation.
- **Independent judgment** — the user's preferred conclusion is not evidence. Disagree directly when evidence conflicts, and give the basis, risks, alternative explanations, and smallest resolving check.
- **Epistemic labels** — distinguish FACT, SOURCE, USER-REPORTED, INFERENCE, HYPOTHESIS, ASSUMPTION, ALTERNATIVE, JUDGMENT, and UNKNOWN when the distinction matters.
- **Prompt first** — before any non-trivial implementation or experiment, the agent writes an inspectable Prompt Contract for the task. This is a task specification, not hidden chain-of-thought.
- **Just-in-time evidence acquisition** — if current external evidence can materially change a decision, search primary literature, official docs, GitHub implementations/issues/PRs, datasets, pretrained weights, and evaluation protocols before acting.
- **Observation before explanation** — do not convert a plausible mechanism into a conclusion until alternatives are tested.
- **Competing hypotheses before architecture changes** — identify the smallest experiment that distinguishes plausible explanations.
- **Minimal discriminative experiments** — maximize information gained per unit of compute, engineering/annotation effort, opportunity cost, and confounding.
- **Risk-proportional audit** — classify review as R0/R1/R2/R3; low-risk read-only diagnostics get a bounded preflight, while claim-bearing/final-test/destructive/shared-resource work gets progressively stronger controls. Non-blocking findings do not silently become execution blockers.
- **Frozen baselines and protocols** — corrected baselines, splits, metrics, and final-test rules cannot drift silently.
- **Data gate → preflight → smoke → pilot → full** — expensive execution is earned through progressively stronger gates, while inapplicable gates are recorded rather than manufactured.
- **Builder / Challenger separation** — implementation and adversarial review are distinct roles; they should not edit the same experiment simultaneously, and the Challenger is judged by decision-relevant objections rather than objection count.
- **KEEP / REJECT / DEFER / INVALID** — every completed experiment ends in an explicit decision.
- **Immediate knowledge retention** — prompts, evidence, dataset/protocol state, experiments, decisions, and handoffs are updated as part of the work, not reconstructed later.
- **Handoff before context loss** — every non-trivial work session that changes durable project state must update HANDOFF before being called complete; if context capacity is becoming low, preserving current truth takes priority over starting optional new work.

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
HANDOFF.md           # current truth, context continuity, and exact next action
EXPERIMENTS.md       # experiment ledger
DECISIONS.md         # KEEP / REJECT / DEFER / INVALID records
PROMPTS.md           # generated Prompt Contracts
DATA_MANIFEST.*      # dataset identity/version/splits/annotation/protocol provenance
```

If a project already has equivalent files, use them instead of duplicating state.

## Structure

```text
.github/skills/research-os/
├── SKILL.md
├── protocols/
│   ├── premise-audit.md
│   ├── dataset-integrity.md
│   ├── risk-proportional-audit.md
│   ├── handoff-continuity.md
│   └── ...
├── roles/
│   ├── data-benchmark-curator.md
│   └── ...
├── templates/
├── checklists/
│   ├── dataset-integrity-checklist.md
│   └── ...
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

The 17-case behavioral benchmark covers workflow calibration, premise/logic auditing, dataset/pairing integrity, current evidence, hypothesis discipline, leakage/final-test governance, invalid runs, frozen baselines, GPU execution gates, scope control, shared-resource safety, metric semantics, source conflicts, Builder/Challenger separation, and risk-proportional audit budgeting.

Static CI validates the package and benchmark specification; it does **not** prove that an LLM follows the methodology. Real behavioral evaluation requires running the benchmark tasks with ResearchOS enabled and scoring observable outputs using `evals/rubric.md`.

## Scientific integrity

ResearchOS forbids silent final-test tuning, post-hoc removal of inconvenient samples/ROIs, selective reporting, fabricated citations/results/data properties/publication status, unrecorded protocol changes, assuming cross-sample correspondence from row index without an identity contract, and treating a protocol/data-invalid run as scientific evidence.

Operational safety is part of research quality: destructive actions, shared compute, credential handling, checkpoint provenance, data mutation, and context/handoff continuity require explicit boundaries. Risk-proportional auditing never weakens a real safety or scientific-integrity blocker; it prevents unrelated higher-tier controls from consuming low-risk diagnostic work.

## Version

Current release: **v0.2.2**.

License: MIT (see `LICENSE`).
