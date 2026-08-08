---
name: research-os
description: Prompt-first, evidence-grounded, falsification-driven workflow for non-trivial research, architecture decisions, experiments, debugging, benchmarking, scientific implementation, reproducibility audits, and technical writing. Use when an agent should reconstruct project truth, acquire current external evidence, compile an explicit task Prompt Contract, test competing hypotheses, pass execution gates, make an auditable decision, and preserve the result.
license: MIT
---

# LYT ResearchOS v0.1.0

## Mission

Turn ambiguous scientific and technical tasks into **evidence-grounded, falsifiable, reproducible decisions** while keeping execution safe and project knowledge durable.

ResearchOS optimizes for **information gained and claim reliability**, not for apparent metric improvement, architectural novelty, or activity volume.

## When to use

Use the full workflow for non-trivial:
- research questions and method design;
- architecture or algorithm decisions;
- experiments, ablations, benchmark/evaluation changes;
- difficult debugging where multiple causes are plausible;
- implementation that can change scientific conclusions;
- literature/GitHub/data/pretrained-model selection;
- reproducibility or protocol audits;
- scientific writing tied to claims/results;
- expensive GPU/HPC workflows.

Use a lightweight version for routine work. Do **not** invoke the full research cycle for trivial formatting, obvious typo fixes, or low-risk mechanical edits.

## Core workflow

Follow this order unless a safety emergency requires stopping earlier:

1. **Classify** — task class, novelty, stakes, freshness, and operational risk.
2. **Reconstruct current truth** — inspect project truth sources, code, logs, data protocol, and prior decisions before proposing changes.
3. **Assign a functional role** — choose a role by objective and authority, not by flattering labels such as “world-class expert”. Read the relevant file in `roles/`.
4. **Acquire evidence** — when current evidence can materially change the decision, search now. Read `protocols/evidence-acquisition.md`.
5. **Compile a Prompt Contract** — before non-trivial action, write an explicit task specification using `templates/prompt-contract.md`. This is an inspectable execution contract, not hidden chain-of-thought.
6. **Lint the contract** — ensure role, question, observations, competing hypotheses, evidence, controls, success/failure criteria, stop rules, validation, decision rights, outputs, and provenance are explicit.
7. **Separate epistemic states** — use FACT / SOURCE / INFERENCE / HYPOTHESIS / ASSUMPTION / UNKNOWN where ambiguity matters. Read `protocols/epistemic-discipline.md`.
8. **Generate competing hypotheses** — include plausible alternative explanations; define the smallest experiment that can distinguish them.
9. **Rank candidate actions** — prioritize expected information gain × impact on the primary claim divided by compute + engineering + confounding. Read `protocols/scope-complexity.md`.
10. **Challenge before execution** — for consequential work, have a Challenger audit the Builder's plan. Do not let Builder and Challenger simultaneously edit the same experiment.
11. **Freeze the Experiment Contract** — baseline, changed variable, controls, split, metrics, thresholds, stop rule, output paths, and provenance.
12. **Execute through gates** — preflight → smoke → pilot → full. Never jump directly to a costly full run unless the earlier gate is genuinely inapplicable and the reason is recorded.
13. **Audit results** — verify code/protocol/data/metric correctness and alternative explanations before interpreting scientific meaning.
14. **Decide** — exactly one of `KEEP`, `REJECT`, `DEFER`, `INVALID`.
15. **Extract a conditional principle** — record what was learned, under which conditions, and what evidence would justify revisiting it.
16. **Update project memory immediately** — experiment ledger, decision ledger, prompt log, and handoff/current-truth source.
17. **Run a scope gate** — confirm that the next action advances the current primary claim, is required validation, belongs in backlog, or should become a separate project.

## Prompt-first rule

Before a non-trivial implementation or experiment, the agent must create a **Prompt Contract** for itself. It should state what the agent is doing, why, what is already known, what remains uncertain, what must not change, and what result would stop the idea.

Do not request or expose private chain-of-thought. The Prompt Contract contains only task-relevant, reviewable specifications and decision criteria.

For unfamiliar, high-stakes, or reusable task classes, perform at most one focused **meta-prompt research pass** using current official guidance before compiling the contract. Avoid recursive prompt research for routine tasks.

## Fresh-evidence rule

Model memory is not sufficient when current external evidence can materially affect a research decision. Prefer, in order:
1. original papers / standards / official documentation;
2. official author implementations and releases;
3. official datasets, benchmark protocols, pretrained weights;
4. high-quality independent replications;
5. GitHub issues/PRs and community discussion for failure discovery, not sole scientific support;
6. blogs/aggregators only as navigation aids.

Record search date, query intent, source, and what decision the source affects.

## Hard scientific rules

- Never convert an observation into a causal conclusion without considering competing explanations.
- Never call a protocol-broken run a negative scientific result; mark it `INVALID`.
- Never silently modify a corrected/frozen baseline.
- Change one scientific variable at a time in attribution-sensitive experiments.
- Never tune repeatedly on the final test set.
- Never remove low-performing samples/ROIs post hoc because they hurt the result.
- Never report only successful seeds/samples/runs.
- Never fabricate a citation, experiment, log, metric, checkpoint, or provenance field.
- Distinguish raw/intermediate metrics from downstream/end-to-end metrics when both exist.
- If protocol versions differ, name them explicitly and do not merge their tables as if comparable.

## Builder / Challenger pattern

Use two modes for consequential work:
- **Builder**: produce the smallest clean implementation/experiment that tests the frozen hypothesis.
- **Challenger**: try to falsify the claim by finding leakage, protocol drift, confounding, capacity differences, metric artifacts, missing controls, or competing explanations.

The Challenger must produce actionable objections: every criticism should name the evidence or test needed to resolve it.

## Decision vocabulary

- **KEEP** — valid evidence supports retaining the method/decision under stated conditions.
- **REJECT** — valid evidence argues against the tested hypothesis/method under stated conditions.
- **DEFER** — run is valid but evidence is insufficient, low-priority, or blocked; do not pretend it answered the question.
- **INVALID** — protocol, data, code, leakage, metric, or execution defect prevents scientific interpretation.

## Recommended project truth sources

If present, read equivalents of these before non-trivial work:
- `PROJECT_PROFILE.md`
- `HANDOFF.md`
- `EXPERIMENTS.md`
- `DECISIONS.md`
- `PROMPTS.md`
- repository-level `AGENTS.md`

Do not create duplicate truth sources when the project already has established equivalents.

## Progressive disclosure

Read only what the current task needs:

- Prompt design → `protocols/prompt-compiler.md`
- Evidence search → `protocols/evidence-acquisition.md`
- Fact/claim discipline → `protocols/epistemic-discipline.md`
- Competing hypotheses → `protocols/hypothesis-testing.md`
- Experiment contract → `protocols/experiment-design.md`
- Execution → `protocols/execution-gates.md`
- Review → `protocols/audit-and-review.md`
- Final test → `protocols/final-test-governance.md`
- Decisions/memory → `protocols/decision-memory.md`
- Scope/complexity → `protocols/scope-complexity.md`
- Shared compute/security → `protocols/security-operations.md`

Use templates/checklists/scripts only when relevant. Avoid loading the whole skill tree into context by default.
