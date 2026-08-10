# Changelog

## v0.2.2 — 2026-08-10

Risk-proportional audit and execution-calibration update:
- added `protocols/risk-proportional-audit.md` with R0/R1/R2/R3 review tiers covering read-only diagnostics, reversible isolated implementation, claim-bearing experiments, and final-test/destructive/shared/irreversible operations;
- added explicit audit-budget targets for low-risk work: roughly 10–15% of planned effort/context before first execution for R0 and roughly 20–25% before implementation/smoke for R1, unless a concrete blocker is discovered;
- introduced finding severities `BLOCK-EXECUTION`, `BLOCK-INTERPRETATION`, `BOUNDS-CLAIM`, and `FOLLOW-UP` so non-blocking hardening cannot silently become an execution blocker;
- added a Challenger stopping rule: once tier-required checks pass and no execution blocker remains, further audit expansion requires a named plausible failure mode, the decision it could reverse, and a bounded resolving check;
- added `PROCESS-ISSUE: OVER-AUDITING` for review drift where repeated non-blocking checks consume a low-risk task instead of allowing the smallest safe discriminative experiment to run;
- updated execution gates so bounded read-only diagnostics do not inherit release/final-test/destructive controls that are irrelevant to their safety or validity;
- extended scope/complexity control to count audit/process overhead, not only model/code complexity;
- updated the behavioral rubric so both under-processing and over-processing are workflow-governance failures while preserving hard scientific-integrity and operational-safety blockers;
- added benchmark case `E17 Low-risk diagnostic trapped in review` and made `audit-budget` mandatory benchmark coverage;
- added the new protocol to package validation and documented ResearchOS v0.2.2 in `SKILL.md` and `README.md`.

## v0.2.1 — 2026-08-10

Handoff and context-continuity hardening:
- made HANDOFF/current-truth maintenance a mandatory completion gate for every non-trivial work session that changes durable scientific, code, data/protocol, experiment, job, blocker, or next-step state;
- added `protocols/handoff-continuity.md` with end-of-work, context-limit, agent/session switch, pause, and emergency rescue-handoff triggers;
- added a conservative context-limit rule: when context is becoming low or prior state is at material risk of loss, stop starting optional work and preserve current truth first;
- added `BLOCKED-CONTINUITY` for sessions whose durable handoff cannot be written because of an external failure;
- extended HANDOFF content to record session/context boundary, dirty/uncommitted state when material, superseded conclusions, exact job/release/checkpoint/protocol identities, and the next safe action;
- updated the HANDOFF template and linter to require a `Session / Context Continuity` section;
- added the continuity protocol to repository package validation and progressive-disclosure guidance;
- documented v0.2.1 in the root README.

## v0.2.0 — 2026-08-09

Premise, data-integrity, and evaluation upgrade:
- added a mandatory premise/logic audit before consequential research decisions;
- added explicit independent-judgment behavior: user preference, seniority, prestige, or an attractive narrative are not evidence;
- expanded epistemic labels with USER-REPORTED, ALTERNATIVE, and JUDGMENT;
- added verification guidance for decision-critical numbers, people, publication status, benchmark results, dates, and dataset properties;
- added proactive ignored-variable, confounder, cost, bias, and opportunity-cost scanning;
- added a Dataset Integrity Gate covering dataset identity/version, file/schema validity, coordinates/units/orientation, pairing/correspondence semantics, sampling, split leakage, annotations, transforms/resampling, corruption/OOB, provenance, and representativeness;
- added the Data and Benchmark Curator role and a reusable dataset-integrity checklist;
- updated Prompt and Experiment Contracts plus their linters to require premise and dataset status fields;
- added behavior-eval cases for authority/prestige premise pressure and invalid cross-sample row-index pairing;
- expanded the behavioral rubric from 12 to 14 dimensions and added dataset/premise hard-fail boundaries;
- expanded repository linting so the new protocols/role/checklist cannot silently disappear.

Validation and evaluation infrastructure included in this release:
- 16-case domain-generic ResearchOS behavioral benchmark (expanded from the earlier 14-case suite);
- benchmark schema/coverage validation;
- regression tests for Prompt/Experiment/HANDOFF linters;
- repository/package linter and self-test;
- GitHub Actions CI across Python 3.11–3.13;
- static-CI vs real agent/model behavioral-evaluation distinction;
- Experiment Contract template handling that accepts the canonical decision placeholder while real contracts still require one decision status.

## v0.1.0 — 2026-08-08

Initial complete ResearchOS skill package.

Highlights:
- prompt-first Prompt Contract compiler;
- just-in-time literature/GitHub/docs/dataset evidence acquisition;
- functional role selection with objective, bias, authority, and failure mode;
- explicit epistemic labels and competing-hypothesis discipline;
- minimal discriminative experiment design with information-gain/cost prioritization;
- Builder/Challenger review pattern;
- frozen baseline and final-test governance;
- preflight → smoke → pilot → full execution gates;
- KEEP / REJECT / DEFER / INVALID decision vocabulary;
- scope and complexity gates;
- immediate experiment/decision/HANDOFF retention;
- standard-library linters for Prompt Contract, Experiment Contract, and HANDOFF files.
