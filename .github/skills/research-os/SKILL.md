---
name: research-os
description: Prompt-first, evidence-grounded, falsification-driven workflow for non-trivial research, architecture decisions, experiments, debugging, benchmarking, scientific implementation, reproducibility audits, technical writing, dataset integrity, risk-proportional review, and context-safe handoff continuity. Use when an agent should audit the premise, validate dataset integrity, reconstruct project truth, acquire current external evidence, compile an explicit task Prompt Contract, test competing hypotheses, scale review to actual risk, pass execution gates, make an auditable decision, and preserve the result before work or context is lost.
license: MIT
---

# LYT ResearchOS v0.2.2

## Mission

Turn ambiguous scientific and technical tasks into **evidence-grounded, falsifiable, reproducible decisions** while keeping execution safe and project knowledge durable.

ResearchOS optimizes for **information gained and claim reliability**, not for apparent metric improvement, architectural novelty, activity volume, review volume, or agreement with the user's preferred conclusion.

## When to use

Use the full workflow for non-trivial:
- research questions and method design;
- architecture or algorithm decisions;
- experiments, ablations, benchmark/evaluation changes;
- difficult debugging where multiple causes are plausible;
- implementation that can change scientific conclusions;
- literature/GitHub/data/pretrained-model selection;
- dataset, annotation, split, pairing, sampling, or coordinate audits;
- reproducibility or protocol audits;
- scientific writing tied to claims/results;
- expensive GPU/HPC workflows.

Use a lightweight version for routine work. Do **not** invoke the full research cycle for trivial formatting, obvious typo fixes, low-risk mechanical edits, or bounded read-only diagnostics that only need a narrow preflight.

## Core workflow

Follow this order unless a safety emergency requires stopping earlier:

1. **Classify** — task class, novelty, stakes, freshness, operational risk, and review tier (R0/R1/R2/R3). Read `protocols/risk-proportional-audit.md` when review depth matters.
2. **Audit the premise** — check for false/unsupported premises, logic jumps, decision-critical missing information, stale concrete claims, and omitted variables/costs/biases. Read `protocols/premise-audit.md`.
3. **Reconstruct current truth** — inspect project truth sources, code, logs, prior decisions, and actual artifacts before proposing changes.
4. **Run the Dataset Integrity Gate** — for data-bearing work, validate dataset identity/version, format/schema, coordinates/units, pairing, sampling, annotations, transforms, split/leakage, derived-data provenance, and representativeness before interpreting model behavior. Read `protocols/dataset-integrity.md`.
5. **Assign a functional role** — choose a role by objective and authority, not by flattering labels such as “world-class expert”. Read the relevant file in `roles/`; use `roles/data-benchmark-curator.md` when dataset validity is central.
6. **Acquire evidence** — when current evidence can materially change the decision, search now. Read `protocols/evidence-acquisition.md`.
7. **Compile a Prompt Contract** — before non-trivial action, write an explicit task specification using `templates/prompt-contract.md`. This is an inspectable execution contract, not hidden chain-of-thought.
8. **Lint the contract** — ensure premise audit, role, question, observations, competing hypotheses, evidence, dataset status where applicable, controls, success/failure criteria, stop rules, validation, decision rights, outputs, and provenance are explicit.
9. **Separate epistemic states** — use FACT / SOURCE / USER-REPORTED / INFERENCE / HYPOTHESIS / ASSUMPTION / ALTERNATIVE / JUDGMENT / UNKNOWN where ambiguity matters. Read `protocols/epistemic-discipline.md`.
10. **Generate competing hypotheses** — include plausible alternative explanations; define the smallest experiment that can distinguish them.
11. **Rank candidate actions** — prioritize expected information gain × impact on the primary claim divided by compute + engineering + annotation + coordination + confounding. Read `protocols/scope-complexity.md`.
12. **Challenge before execution, proportional to risk** — for consequential work, have a Challenger audit the Builder's plan, but do not apply final-test/release/destructive controls to a low-risk diagnostic without a concrete reason. Every finding must state whether it blocks execution, blocks interpretation, bounds the claim, or is follow-up. Read `protocols/audit-and-review.md` and `protocols/risk-proportional-audit.md`.
13. **Freeze the Experiment Contract** — premise, dataset/split status, baseline, changed variable, controls, metrics, thresholds, stop rule, output paths, and provenance.
14. **Execute through applicable gates** — data/preflight → smoke → pilot → full. Never jump directly to a costly full run unless earlier gates are genuinely inapplicable and the reason is recorded; likewise, do not manufacture unnecessary gates for a bounded R0 diagnostic.
15. **Audit results** — verify code/protocol/data/metric correctness and alternative explanations before interpreting scientific meaning.
16. **Decide** — exactly one of `KEEP`, `REJECT`, `DEFER`, `INVALID`.
17. **Extract a conditional principle** — record what was learned, under which conditions, and what evidence would justify revisiting it.
18. **Update project memory and HANDOFF before completion** — experiment ledger, decision ledger, prompt log, dataset/protocol state, and handoff/current-truth source are part of the work product. Every non-trivial work session that changes durable state must update HANDOFF before being called done. If context is becoming low, write the handoff before starting optional new work. Read `protocols/handoff-continuity.md` and `protocols/decision-memory.md`.
19. **Run a scope gate** — confirm that the next action advances the current primary claim, is required validation, belongs in backlog, or should become a separate project.

## Premise-first rule

Before solving a consequential question, test whether the question is built on valid premises. Do not inherit the user's preferred explanation, publication claim, metric interpretation, or causal story as fact.

When a concrete number, person, paper status, benchmark result, date, dataset property, or conclusion materially affects the decision, verify it from the strongest available source when feasible. If it cannot be verified, label its status instead of inventing certainty.

If the evidence contradicts the requested framing, disagree directly and state the evidence, risk, plausible alternatives, and smallest resolving check.

## Dataset-first rule

For data-bearing research, dataset correctness is a gate, not a cleanup task after modeling. Before claim-bearing architecture changes or long runs, inspect the actual data and supervision for:
- file/schema/shape/dtype validity;
- axis, coordinate, orientation, spacing, unit, and transform-direction correctness;
- sample identity, pairing, correspondence semantics, duplicate/derived samples;
- train/validation/test leakage at subject and derived-data levels;
- sampling unit, weighting, pseudo-replication, filtering and representativeness;
- label ontology, missing-vs-unannotated semantics, annotator/provenance differences, and interpolation;
- OOB/NaN/empty/corrupt artifacts and distribution shifts.

Never infer correspondence identity from equal row index unless the data-generation protocol guarantees it. Never interpret a run scientifically when a material data/protocol defect invalidates the supervision or metric.

## Prompt-first rule

Before a non-trivial implementation or experiment, the agent must create a **Prompt Contract** for itself. It should state what the agent is doing, why, what is already known, what remains uncertain, what premises/data have been audited, what must not change, and what result would stop the idea.

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

## Independent-judgment rule

- Do not optimize for agreement, reassurance, or preserving an attractive narrative.
- Distinguish what is observed, externally sourced, user-reported, inferred, hypothesized, assumed, alternative, unknown, or a subjective judgment.
- Proactively surface material ignored variables, confounders, costs, biases, and alternative explanations that could reverse the decision.
- Do not dump generic caveats; prioritize factors that materially affect the claim or action.
- When disagreeing, be explicit about the basis and propose a resolving test rather than merely asserting a contrary opinion.

## Risk-proportional audit rule

Audit depth must be proportional to scientific risk, operational risk, irreversibility, and claim stakes. Review is a means to valid action, not an end in itself.

- **R0 read-only diagnostic** — one bounded preflight, then execute when source/checkpoint identity, development/validation scope, fixed comparison semantics, output isolation, and no hidden write risk are established. As a planning target, pre-execution review should normally consume no more than roughly 10–15% of task effort/context.
- **R1 reversible isolated implementation** — add focused unit/baseline-containment/state-drift checks and a smoke path. As a planning target, pre-execution review should normally consume no more than roughly 20–25% before implementation/smoke unless a concrete blocker appears.
- **R2 claim-bearing experiment** — use full task-relevant data/protocol/provenance gates, smoke/pilot, and post-run audit; unresolved validity risks may justify deeper review.
- **R3 final-test/destructive/shared/irreversible** — use the strongest applicable final-test, authorization, provenance, immutability, and security controls. Budget guidance never overrides a real blocker.

Every finding must be classified as `BLOCK-EXECUTION`, `BLOCK-INTERPRETATION`, `BOUNDS-CLAIM`, or `FOLLOW-UP`. Only a real execution blocker stops a safe bounded diagnostic. Interpretation blockers stop claim-bearing interpretation; bounded-claim and follow-up findings must not silently postpone execution.

Once tier-required checks pass and no execution blocker remains, the Challenger must stop expanding pre-execution review unless the next audit branch names a plausible failure mode, the decision it could reverse, and a bounded resolving check. Repeated non-blocking audit expansion is `PROCESS-ISSUE: OVER-AUDITING` and should return to the smallest safe discriminative experiment.

This rule never weakens final-test governance, dataset validity, frozen-baseline attribution, authorization, credential security, or destructive/shared-resource safeguards. Escalate the risk tier when a material issue is discovered.

## Handoff and context-continuity rule

HANDOFF/current-truth maintenance is a mandatory completion gate for non-trivial work, not optional documentation.

- After every non-trivial work session that changes code, data/protocol state, experiments, jobs, conclusions, blockers, or next-step intent, update the established `HANDOFF.md` (or exact equivalent) before declaring the work complete.
- Do not wait until a whole phase or project ends. Preserve state while it is still fresh.
- If the user/host indicates the context window is becoming low, or the conversation has become long enough that prior state is at material risk of loss, stop starting optional new work and write HANDOFF first.
- Before switching agent/person/session/model, pausing a long task, or leaving important running/uncommitted state, write HANDOFF.
- If exact remaining context is unavailable, use conservative qualitative judgment; continuity takes priority over one more speculative task.
- If context loss is imminent, write the minimal rescue handoff defined in `protocols/handoff-continuity.md` before cleanup or further experimentation.
- Preserve superseded conclusions explicitly, record dirty/uncommitted state when material, record exact job/release/checkpoint/protocol identities when continuation depends on them, and never store secrets.
- A non-trivial session whose durable handoff could not be written must be reported as `BLOCKED-CONTINUITY`, not silently called done.

## Hard scientific rules

- Never convert an observation into a causal conclusion without considering competing explanations.
- Never call a protocol-broken or data-invalid run a negative scientific result; mark it `INVALID`.
- Never silently modify a corrected/frozen baseline.
- Change one scientific variable at a time in attribution-sensitive experiments.
- Never tune repeatedly on the final test set.
- Never remove low-performing samples/ROIs post hoc because they hurt the result.
- Never report only successful seeds/samples/runs.
- Never fabricate a citation, experiment, log, metric, checkpoint, data property, publication status, or provenance field.
- Never assume same-index rows across samples are corresponding entities without an explicit identity contract.
- Distinguish raw/intermediate metrics from downstream/end-to-end metrics when both exist.
- If protocol versions differ, name them explicitly and do not merge their tables as if comparable.
- If a dataset, annotation, coordinate, split, or evaluation defect can change the scientific interpretation, stop interpretation until the defect is resolved or bounded.
- Never let a non-blocking audit tangent silently replace the frozen primary task; preserve it as `FOLLOW-UP` unless evidence justifies escalation.

## Builder / Challenger pattern

Use two modes for consequential work:
- **Builder**: produce the smallest clean implementation/experiment that tests the frozen hypothesis.
- **Challenger**: try to falsify the claim by finding false premises, data defects, leakage, protocol drift, confounding, capacity differences, metric artifacts, implementation bugs, missing controls, or competing explanations, at a depth proportional to task risk.

The Challenger must produce actionable objections: every criticism should name the evidence/test needed to resolve it and its operational severity. The Challenger is not rewarded for objection count or token use.

## Decision vocabulary

- **KEEP** — valid evidence supports retaining the method/decision under stated conditions.
- **REJECT** — valid evidence argues against the tested hypothesis/method under stated conditions.
- **DEFER** — run is valid but evidence is insufficient, low-priority, or blocked; do not pretend it answered the question.
- **INVALID** — protocol, data, code, leakage, metric, or execution defect prevents scientific interpretation.

Dataset gate statuses (`PASS`, `PASS-WITH-LIMITATIONS`, `BLOCKED`, `INVALID-DATA`) describe dataset readiness and do not replace the final experiment decision vocabulary.

## Recommended project truth sources

If present, read equivalents of these before non-trivial work:
- `PROJECT_PROFILE.md`
- `HANDOFF.md`
- `EXPERIMENTS.md`
- `DECISIONS.md`
- `PROMPTS.md`
- dataset manifest / split manifest / annotation protocol / metric protocol
- repository-level `AGENTS.md`

Do not create duplicate truth sources when the project already has established equivalents.

## Progressive disclosure

Read only what the current task needs:

- Premise/logic audit → `protocols/premise-audit.md`
- Dataset/split/annotation/sampling audit → `protocols/dataset-integrity.md`
- Prompt design → `protocols/prompt-compiler.md`
- Evidence search → `protocols/evidence-acquisition.md`
- Fact/claim discipline → `protocols/epistemic-discipline.md`
- Competing hypotheses → `protocols/hypothesis-testing.md`
- Experiment contract → `protocols/experiment-design.md`
- Risk tier / audit budget / blocker severity → `protocols/risk-proportional-audit.md`
- Execution → `protocols/execution-gates.md`
- Review → `protocols/audit-and-review.md`
- Final test → `protocols/final-test-governance.md`
- Decisions/memory → `protocols/decision-memory.md`
- Handoff/context continuity → `protocols/handoff-continuity.md`
- Scope/complexity → `protocols/scope-complexity.md`
- Shared compute/security → `protocols/security-operations.md`

Use templates/checklists/scripts only when relevant. Avoid loading the whole skill tree into context by default.
