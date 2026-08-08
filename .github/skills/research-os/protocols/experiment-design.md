# Experiment Design Protocol

## Experiment contract

Use `../templates/experiment-contract.md` before implementation when attribution matters.

Required commitments:
- hypothesis;
- frozen baseline;
- exactly named scientific variable(s) changed;
- controlled variables;
- development split and final-test status;
- primary/secondary metrics;
- success, failure, and stop criteria;
- runtime/compute budget;
- output paths;
- provenance.

## One-variable principle

For attribution-sensitive ablations, change one scientific variable at a time. Engineering changes that are provably semantics-preserving may be grouped, but record them separately and validate equivalence.

Do not combine multiple unvalidated ideas into the first run.

## Minimal baseline ladder

Before a high-capacity learned module, ask whether the question can be tested with:
- identity/no-op;
- analytic or heuristic baseline;
- linear model;
- bounded residual model;
- small local model;
- only then higher-capacity architecture.

## Information-gain priority

Rank candidate experiments qualitatively by:

`priority ~ expected information gain × impact on primary claim / (compute + engineering + confounding)`

Use High/Medium/Low if numeric scoring would be artificial.

## Metric contracts

Name metric scope explicitly. Distinguish, when applicable:
- raw/intermediate metric;
- fit-subset metric;
- held-out metric;
- downstream/end-to-end metric;
- topology/safety metric;
- runtime/memory metric.

Never substitute one for another because it looks better.

## Capacity comparisons

If comparing model/projector classes with different parameterizations or energy definitions, do not directly compare raw regularization energies unless they are on a justified common scale. Prefer separate panels/within-class comparisons.

## Replication

For stochastic experiments that become claim-bearing, define seeds/replicates and report the full prespecified set, not only the best run.
