# Prompt Compiler Protocol

## Purpose

Before consequential action, convert the user's goal and current project state into a reviewable **Prompt Contract**. The contract is an external task specification, not private reasoning.

## 1. Classify the task

Identify:
- task class: research design, mathematical definition, implementation, debugging, evaluation, review, literature search, HPC, writing;
- novelty: routine / unfamiliar;
- stakes: low / medium / high;
- freshness need: stable / slow-changing / current / latest;
- operational risk: read-only / reversible write / destructive or shared-resource write.

## 2. Select a functional role

A role must define four things:
1. **objective** — what it optimizes;
2. **default bias** — e.g. simplicity, falsification, reproducibility;
3. **authority** — what it may decide/change;
4. **failure mode to avoid**.

Avoid empty status labels such as “world-class expert”. Read the closest file in `../roles/`.

## 3. Meta-prompt research

Use one focused meta-research pass when the task class is unfamiliar, high-stakes, or expected to become reusable. Prefer current official model/agent/tool guidance. Stop after one pass unless official sources conflict materially.

Do not research prompting recursively for ordinary edits.

## 4. Compile the Prompt Contract

Use `../templates/prompt-contract.md`. Required sections:
- Role
- Mission
- Context / Current Truth
- Research Question
- Observations
- Competing Hypotheses
- Evidence
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

## 5. Explain constraints when useful

Prefer `constraint + reason` over unexplained prohibitions. Example: “Do not alter the final-test split because repeated test tuning would invalidate the held-out claim.”

## 6. Use examples sparingly

Examples should clarify output structure or a subtle invariant. Keep them consistent with the actual task. Do not add examples merely to make the prompt longer.

## 7. Freeze before execution

Once Builder and Challenger agree on the contract, freeze attribution-sensitive fields. If a material field changes during execution, version the contract and record why.

## Prompt quality test

A good Prompt Contract lets a competent new agent answer:
- What exact question are we testing?
- What evidence already exists?
- What plausible alternatives remain?
- What one thing changes?
- What must not change?
- What result supports/rejects the hypothesis?
- What would stop the line of work?
- Which data can be used for development?
- What artifacts/provenance must be produced?
