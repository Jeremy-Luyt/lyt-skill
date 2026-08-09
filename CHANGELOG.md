# Changelog

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
