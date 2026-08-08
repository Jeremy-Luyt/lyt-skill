# ResearchOS behavioral evaluations

This directory treats the methodology itself as a versioned system that can regress.

`benchmark.json` contains representative scenarios and the behavior ResearchOS should induce. It is intentionally domain-generic so changes are tested against the workflow rather than one research project.

## Two evaluation layers

### 1. Static CI validation

CI validates:
- benchmark schema and coverage;
- required package files and SKILL frontmatter;
- Prompt/Experiment/HANDOFF linter behavior;
- Python syntax and repository-local self-tests.

Static CI **does not prove** that an LLM will follow the methodology correctly.

### 2. Agent/model behavioral evaluation

For a real behavior eval, present each case's `task` to an agent with ResearchOS enabled, retain the externally visible response/plan/artifacts, and score them with `rubric.md`.

Do not request private chain-of-thought. Score only observable behavior: evidence acquisition, task contract, controls, governance, execution gates, decisions, and memory updates.

## Regression policy

A methodology change should not silently improve one case while weakening scientific boundaries elsewhere. Hard-fail violations such as final-test tuning, fabrication, treating a protocol-broken run as valid evidence, or destructive shared-resource action without authorization fail the behavioral suite regardless of aggregate score.

Add a benchmark case whenever a real project reveals a recurring failure mode that is general enough to transfer across domains.
