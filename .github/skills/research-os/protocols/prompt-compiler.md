# Prompt Compiler Protocol

## Purpose

Before consequential action, convert the user's goal and current project state into a reviewable **Prompt Contract**. The contract is an external task specification, not private reasoning.

## 1. Classify the task

Identify:
- task class: research design, mathematical definition, implementation, debugging, evaluation, review, literature search, data/benchmark audit, HPC, writing;
- novelty: routine / unfamiliar;
- stakes: low / medium / high;
- freshness need: stable / slow-changing / current / latest;
- operational risk: read-only / reversible write / destructive or shared-resource write.

## 2. Audit the premise

Before selecting a method, inspect the question for:
- false, unsupported, contradicted, or stale premises;
- observation→mechanism, correlation→causation, intermediate→downstream, or one-case→general-class logic jumps;
- concrete numbers/names/publication statuses/dataset properties that materially affect the decision and should be verified;
- decision-critical missing information;
- ignored variables, confounders, costs, biases, or alternative explanations.

Do not optimize for agreement with the user's preferred conclusion. Read `premise-audit.md` when this audit is non-trivial.

## 3. Run the data gate when applicable

For data-bearing tasks, inspect the actual dataset/supervision before architecture or interpretation. Read `dataset-integrity.md` and record one dataset gate status:
- PASS;
- PASS-WITH-LIMITATIONS;
- BLOCKED;
- INVALID-DATA.

At minimum check the task-relevant subset of: dataset identity/version, format/schema, axis/unit/coordinate conventions, sample pairing, correspondence identity, split leakage, sampling, annotation/label protocol, transforms/resampling, OOB/corruption, derived-data provenance, and representativeness.

A material data defect blocks scientific interpretation even if the code runs.

## 4. Select a functional role

A role must define four things:
1. **objective** — what it optimizes;
2. **default bias** — e.g. simplicity, falsification, reproducibility;
3. **authority** — what it may decide/change;
4. **failure mode to avoid**.

Avoid empty status labels such as “world-class expert”. Read the closest file in `../roles/`. Use `data-benchmark-curator.md` when the primary uncertainty is in data, splits, labels, sampling, pairing, or benchmark protocol.

## 5. Meta-prompt research

Use one focused meta-research pass when the task class is unfamiliar, high-stakes, or expected to become reusable. Prefer current official model/agent/tool guidance. Stop after one pass unless official sources conflict materially.

Do not research prompting recursively for ordinary edits.

## 6. Compile the Prompt Contract

Use `../templates/prompt-contract.md`. Required sections:
- Role
- Mission
- Context / Current Truth
- Premise Audit
- Dataset Integrity Status
- Research Question
- Observations
- Competing Hypotheses
- Evidence
- Ignored Variables / Costs / Biases
- Constraints / Frozen Components
- Method / Minimal Discriminative Action
- Changed Variable and Controlled Variables
- Success Criteria
- Failure Criteria
- Scientific Kill Switch / Stop Conditions
- Validation Plan
- Decision Rights
- Output Contract
- Provenance

For non-data tasks, `Dataset Integrity Status` may be `N/A` with a reason. Do not omit it silently in a claim-bearing data task.

## 7. Explain constraints when useful

Prefer `constraint + reason` over unexplained prohibitions. Example: “Do not alter the final-test split because repeated test tuning would invalidate the held-out claim.”

## 8. Use examples sparingly

Examples should clarify output structure or a subtle invariant. Keep them consistent with the actual task. Do not add examples merely to make the prompt longer.

## 9. Freeze before execution

Once Builder and Challenger agree on the contract, freeze attribution-sensitive fields. If a material field changes during execution, version the contract and record why.

## Prompt quality test

A good Prompt Contract lets a competent new agent answer:
- Is the question built on verified premises?
- What exact question are we testing?
- Has the task-relevant dataset/supervision passed integrity checks?
- What evidence already exists and what is only user-reported/inferred?
- What plausible alternatives remain?
- Which ignored variable/cost/bias could reverse the decision?
- What one thing changes?
- What must not change?
- What result supports/rejects the hypothesis?
- What would stop the line of work?
- Which data can be used for development?
- What artifacts/provenance must be produced?
