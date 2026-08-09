# Audit and Review Protocol

## Challenger objective

Assume an apparent improvement may be explained by a false premise, dataset/supervision defect, leakage, protocol drift, extra capacity, data selection, metric artifacts, implementation bugs, unequal compute, or an untested alternative explanation until those possibilities are addressed.

The Challenger is skeptical, not adversarial for its own sake. Agreement with the Builder or user is not a goal.

## Review order

0. **Premise** — is the question/claim built on verified premises, or does it contain a logic jump or stale/unverified concrete claim?
1. **Data validity** — are files, coordinates, pairing, sampling, annotations, splits, transforms, and derived supervision correct for the claimed task?
2. **Validity** — did the run test what it claims?
3. **Comparability** — are baseline and variant on the same data/protocol/compute where required?
4. **Attribution** — what changed besides the named variable?
5. **Statistics** — is the effect stable enough for the claim?
6. **Mechanism** — do results distinguish the proposed mechanism from alternatives?
7. **Generality** — what conditions bound the conclusion?
8. **Cost/bias** — do compute, annotation, engineering cost, selection bias, representativeness, or metric incentives change the recommendation?

Do not discuss mechanism or novelty before premise/data validity is adequate.

## Dataset review focus

Use `dataset-integrity.md` and check the task-relevant subset of:
- dataset identity/version/source and derived-data provenance;
- file readability, shape, dtype, metadata, value range, missing/corrupt artifacts;
- axis/order/coordinate/unit/orientation/spacing conventions;
- transform direction, interpolation, normalized-grid semantics, OOB behavior;
- sample IDs, subject identity, duplicate/near-duplicate material;
- pairing and correspondence/landmark row identity;
- train/validation/test leakage including template/statistics construction;
- sampling unit, weighting, filtering, pseudo-replication and representativeness;
- label ontology, missing-vs-unannotated semantics, annotation provenance and post-hoc exclusions.

A material dataset/supervision defect makes affected scientific evidence `INVALID` even if the optimizer converged normally.

## Code review focus

Check:
- tensor/axis/unit conventions;
- train/eval mode;
- masking/padding/normalization semantics;
- gradients and zero-init behavior;
- data loader/split leakage;
- checkpoint strictness;
- metric formulas;
- hidden fallback behavior;
- silent exception handling;
- nondeterministic selection;
- accidental changes to frozen components.

## Epistemic review focus

Check that the report distinguishes:
- FACT/SOURCE from USER-REPORTED content;
- INFERENCE/HYPOTHESIS from observed result;
- ALTERNATIVE explanations from the preferred mechanism;
- JUDGMENT/recommendation from empirical findings;
- UNKNOWN from assumed truth.

For decision-critical numbers, people, dates, paper/publication status, benchmark results, and dataset properties, verify from the strongest feasible source or preserve the uncertainty explicitly.

## Builder/Challenger separation

Prefer:
`Builder implementation → smoke → Challenger diff/data/protocol audit → revision → full run`.

Do not let both roles make unsynchronized edits to the same experiment branch/files.

## Actionable criticism

Every major objection must state:
- what could be wrong;
- why it matters to the claim;
- what evidence/check would resolve it;
- whether the issue blocks execution, blocks interpretation, or only bounds the claim.
