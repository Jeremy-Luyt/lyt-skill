# Risk-Proportional Audit Protocol

## Purpose

Prevent a valid safety/review process from becoming the dominant failure mode of the task. Audit depth must be proportional to the **scientific risk, operational risk, irreversibility, and claim stakes** of the action being reviewed.

The goal is not to minimize auditing. The goal is to spend audit effort where it can change whether execution is safe or whether the resulting claim is valid.

A review that keeps expanding after all material blockers are resolved is process drift, not rigor.

## Risk tiers

Classify the task before Challenger review. Escalate immediately if a newly discovered fact changes the risk tier.

### R0 — Read-only diagnostic

Typical properties:
- no training or optimizer step;
- no model/checkpoint/data/protocol mutation;
- no final-test access;
- no destructive/shared-resource action;
- no overwrite of claim-bearing artifacts;
- output is isolated diagnostic evidence.

Required pre-execution checks are intentionally narrow:
1. correct source/checkpoint/state identity;
2. correct development/validation sample set and no final-test leakage;
3. the compared inputs/candidate pool/masks/metric semantics are actually held fixed when attribution depends on them;
4. output path is isolated and cannot overwrite frozen artifacts;
5. no hidden write/destructive behavior is present.

After these pass, execute the diagnostic. Release-hardening, immutable-publication, hard-link, cluster-ownership, or other higher-tier concerns are `FOLLOW-UP` unless they are concretely relevant to this run.

**Budget target:** normally no more than roughly 10–15% of the task's planned effort/context before the first executable diagnostic. When exact budgeting is impossible, use one bounded preflight pass rather than open-ended review.

### R1 — Reversible isolated implementation

Typical properties:
- local or isolated code change;
- reversible branch/worktree/overlay;
- feature disabled by default or not yet claim-bearing;
- no final test, destructive action, or shared-resource interference.

Add to R0 checks as relevant:
- focused unit tests;
- baseline containment/equivalence when disabled;
- RNG/state-drift checks if construction can perturb comparisons;
- syntax/schema/config validation;
- smallest smoke path.

**Budget target:** normally no more than roughly 20–25% of planned task effort before implementation/smoke, unless a concrete blocker is discovered.

### R2 — Claim-bearing experiment

Typical properties:
- validation/development metrics will influence a scientific decision;
- GPU/long-running execution;
- checkpoint/release/protocol identity matters;
- new training/evaluation behavior can change a paper claim.

Use full task-relevant dataset/protocol/provenance checks, frozen Experiment Contract, output isolation, smoke, bounded pilot where applicable, and post-run audit. Review may block execution or interpretation when a defect could invalidate the claim.

There is no fixed percentage cap if a concrete validity risk remains unresolved, but the Challenger must still stop expanding scope once all claim-relevant blockers are resolved.

### R3 — Final-test, destructive, irreversible, or shared-resource operation

Typical properties:
- final held-out test access or model selection risk;
- destructive data/checkpoint/file action;
- shared-cluster operations affecting other users;
- credentials/security-sensitive behavior;
- irreversible publication/release action whose provenance is claim-critical.

Use the strongest applicable final-test, provenance, ownership, immutability, security, and authorization gates. Risk-budget guidance never overrides a real safety or integrity blocker at this tier.

## Finding severity

Every audit finding must be assigned exactly one operational consequence:

- `BLOCK-EXECUTION` — proceeding could cause unsafe/irreversible action or the requested execution itself is invalid.
- `BLOCK-INTERPRETATION` — execution may proceed for debugging, but the result cannot support the intended scientific claim until resolved.
- `BOUNDS-CLAIM` — result remains usable, but the conclusion must be narrowed or caveated.
- `FOLLOW-UP` — useful hardening or cleanup that does not affect the safety/validity of the current bounded task.

Only `BLOCK-EXECUTION` stops execution. `BLOCK-INTERPRETATION` stops claim-bearing interpretation, not necessarily a safe diagnostic run. `BOUNDS-CLAIM` and `FOLLOW-UP` must not silently become execution blockers.

## Audit stopping rule

The Challenger must stop the pre-execution audit and allow the next gate when:
1. the task's risk tier is explicit;
2. the tier-required checks have passed;
3. no unresolved `BLOCK-EXECUTION` remains;
4. any `BLOCK-INTERPRETATION`, `BOUNDS-CLAIM`, and `FOLLOW-UP` items are recorded with a resolving check or scope note.

Do not continue auditing merely because additional checks exist in the repository or because a higher-risk protocol contains stricter controls.

A new audit branch after the stopping rule requires a concrete statement of:
- the failure mode being investigated;
- why it is plausible for this task;
- which current decision it could reverse;
- what bounded check resolves it.

Otherwise place it in `FOLLOW-UP` and continue execution.

## Audit-drift detector

Treat the review process as drifting when one or more of these occur:
- multiple consecutive review expansions produce no new blocking evidence;
- most of a low-risk diagnostic's effort is spent on controls that only matter to release/final-test/shared-resource operations;
- the Challenger repeatedly discovers `FOLLOW-UP` items and uses them to postpone a safe minimal experiment;
- safety review starts redesigning the experiment or architecture rather than checking the frozen contract;
- the expected information gain from one more audit branch is lower than the expected information gain from the already-safe discriminative experiment.

When drift is detected, record `PROCESS-ISSUE: OVER-AUDITING`, preserve unresolved non-blockers, and return to the smallest safe execution step.

## Builder / Challenger handoff

For R0/R1 tasks, prefer:

`bounded preflight → Builder diagnostic/implementation → smoke/result → Challenger stable-diff/result audit`.

For R2/R3 tasks, Challenger review may be heavier before execution because protocol, data, provenance, authorization, or final-test mistakes can invalidate or damage the run.

The Challenger is not rewarded for the number of objections. It is rewarded for finding objections that can materially change safety, validity, attribution, or the decision.

## Non-negotiable escalation

Risk-proportional review must never be used to bypass a material scientific-integrity or safety issue. Regardless of initial tier, escalate and block as appropriate if review discovers:
- final-test leakage/tuning;
- invalid dataset identity, pairing, supervision, coordinate, or metric semantics that affect the claim;
- destructive or other-user/shared-resource action without authorization;
- credential/secret exposure;
- frozen-baseline/protocol drift that destroys attribution;
- output overwrite or provenance ambiguity that would make the intended claim unrecoverable.
