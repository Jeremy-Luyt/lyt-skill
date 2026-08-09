# Experiment Design Protocol

## Experiment contract

Use `../templates/experiment-contract.md` before implementation when attribution matters.

Required commitments:
- premise status and unresolved logic/missing-information risks;
- dataset integrity status for data-bearing work;
- hypothesis;
- frozen baseline;
- exactly named scientific variable(s) changed;
- controlled variables;
- development split and final-test status;
- primary/secondary metrics;
- success, failure, and stop criteria;
- runtime/compute/annotation/engineering budget where material;
- output paths;
- provenance.

A claim-bearing experiment must not start from a `BLOCKED` or `INVALID-DATA` Dataset Integrity Gate. Debugging runs may proceed only if explicitly labeled as non-scientific diagnostics.

## Premise-before-variable principle

Before deciding what to change, ask whether the proposed variable is actually implicated by valid evidence. If the apparent bottleneck depends on an unverified assumption, wrong metric interpretation, stale publication claim, or incomplete data audit, resolve that first.

Do not spend compute optimizing a hypothesis built on a broken premise.

## Data-before-model principle

Before architecture changes, validate task-relevant data semantics: sample identity, pairing, coordinate/axis/unit conventions, split leakage, sampling, annotation protocol, preprocessing/resampling, and derived-supervision provenance.

If a dataset defect is discovered after a run, reclassify affected evidence instead of retrofitting the narrative around the result.

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

`priority ~ expected information gain × impact on primary claim / (compute + engineering + annotation + confounding)`

Use High/Medium/Low if numeric scoring would be artificial.

Include opportunity cost when a long experiment delays a more discriminative audit or baseline.

## Metric contracts

Name metric scope explicitly. Distinguish, when applicable:
- raw/intermediate metric;
- fit-subset metric;
- held-out metric;
- downstream/end-to-end metric;
- topology/safety metric;
- runtime/memory metric.

Never substitute one for another because it looks better.

For every primary metric, state the evaluation population, aggregation rule, units, direction, missing-value handling, and protocol version when ambiguity is possible.

## Sampling/statistical unit contract

Name both:
- the **sampled unit** used by the loader/evaluator (patch, point, pair, image, ROI, etc.);
- the **independent experimental unit** used for scientific/statistical inference (often subject/specimen).

Do not inflate effective sample size by treating many dependent patches/points from one subject as independent subjects.

## Capacity comparisons

If comparing model/projector classes with different parameterizations or energy definitions, do not directly compare raw regularization energies unless they are on a justified common scale. Prefer separate panels/within-class comparisons.

## Replication

For stochastic experiments that become claim-bearing, define seeds/replicates and report the full prespecified set, not only the best run.

## Post-run validity check

Before assigning KEEP/REJECT/DEFER, rerun the relevant premise/data/protocol checks against the artifacts actually used. If the experiment did not test the frozen contract, use `INVALID` rather than forcing a scientific interpretation.
