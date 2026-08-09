# Experiment Contract

## Experiment ID

## Premise Status
Verified premises, remaining assumptions/unknowns, logic jumps already resolved, and any blocking uncertainty.

## Question

## Hypothesis

## Baseline
Frozen reference and exact checkpoint/config.

## Changed Variable

## Controlled Variables

## Dataset Integrity Status
PASS / PASS-WITH-LIMITATIONS / BLOCKED / INVALID-DATA / N/A. Reference the dataset manifest/report and unresolved limitations.

## Data / Split
Training, validation/development, final test. State leakage checks, independent experimental unit, sample/pair/patch sampling policy, and final-test isolation.

## Annotation / Pairing / Coordinate Contract
Label ontology and missing-vs-unannotated semantics; pairing/correspondence identity; axis/order/spacing/unit/transform direction; derived-supervision provenance; interpolation/OOB handling where applicable.

## Metrics
### Primary
### Secondary
### Safety / topology / runtime

State units, direction, aggregation population/rule, missing-value handling, and protocol version for claim-bearing primary metrics.

## Ignored Variables / Costs / Biases
Confounders, distribution shift, selection bias, label/measurement error, unequal capacity/compute, annotation/engineering/opportunity cost, and other material threats to interpretation.

## Success Criterion

## Failure Criterion

## Stop Condition

## Compute Budget
GPU/CPU, expected runtime, memory, pilot limit, and material annotation/engineering cost.

## Execution Gates
- Dataset gate:
- Preflight:
- Smoke:
- Pilot:
- Full:
- Audit:

## Output Paths

## Provenance
Commit or code snapshot hash, dataset/split/annotation manifest or version, config, checkpoint, seeds, environment, protocol/metric version.

## Final Decision
KEEP / REJECT / DEFER / INVALID

## Reusable Lesson
Conclusion, conditions, and revisit criterion.
