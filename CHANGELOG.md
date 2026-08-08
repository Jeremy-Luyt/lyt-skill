# Changelog

## Unreleased — 2026-08-08

Validation and evaluation infrastructure:
- added a 14-case domain-generic ResearchOS behavioral benchmark;
- added a 12-dimension observable-behavior scoring rubric with hard-fail integrity rules;
- added benchmark schema/coverage validation;
- added regression tests for Prompt/Experiment/HANDOFF linters;
- added repository/package linter and expanded self-test;
- added GitHub Actions CI across Python 3.11–3.13;
- documented the distinction between static CI validation and real agent/model behavioral evaluation.

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
