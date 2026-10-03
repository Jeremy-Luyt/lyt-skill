# Source & Metric Semantic Audit

Use this protocol whenever a research conclusion depends on the exact behavior of an external repository, API, metric implementation, benchmark script, license, pretrained artifact, data loader, deformation convention, or runtime protocol.

## Principle

**Claims must descend from evidence; never ascend from memory.**

Do not begin with a remembered symbol, API, benchmark convention, or "standard" and then search for something that sounds similar. Reconstruct the claim from primary evidence.

## 1. Evidence authority

For external software and benchmark semantics, prefer:

1. exact source code at a pinned commit/tag;
2. official documentation tied to that release;
3. paper Methods / Supplementary / benchmark specification;
4. official README / release notes;
5. high-quality independent reproduction;
6. issues/PRs/community discussion for failure discovery;
7. secondary summaries or model memory only as navigation aids.

For project-local facts, the project's own current-truth hierarchy overrides this generic list. Immutable receipts/current source/frozen contracts outrank stale handoffs, archives, or conversational memory.

If two authorities conflict, record the conflict. Do not silently reconcile it.

## 2. Audit status

For implementation-semantic audits, every decision-critical claim should have one of:

- **VERIFIED** — directly supported by inspected primary evidence.
- **OBSERVED** — directly observed in a local run/artifact, but not necessarily generalized.
- **INFERRED** — follows from verified/observed facts but was not directly stated or executed.
- **UNVERIFIED** — evidence is missing, blocked, ambiguous, or stale.
- **CONTRADICTED** — inspected evidence directly conflicts with the prior claim.

These audit statuses complement, rather than replace, the general epistemic labels in `epistemic-discipline.md`.

## 3. Symbol existence is not semantic use

Never collapse these questions:

1. Does the symbol/function/file exist?
2. Is it actually reachable/called in the relevant code path?
3. Is it used in training, inference, evaluation, or only as a helper?
4. Is it the implementation used for the paper's reported result?
5. Is it a main benchmark metric, an auxiliary diagnostic, or a loss?
6. Does its numerical semantics match the claim being made?

A function named `jacobian_determinant`, `dice`, `fold`, `runtime`, etc. is not evidence that the repository reports the corresponding benchmark quantity.

## 4. Metric semantic contract

Before a metric can enter a claim-bearing table, record and freeze at least:

- input representation;
- transformation direction;
- grid on which it is defined;
- tensor/component/axis order;
- units and spacing semantics;
- interpolation mode;
- evaluation mask/domain;
- finite-difference or discretization scheme;
- boundary handling and cropping;
- threshold convention;
- reduction/aggregation;
- empty-case/NaN/Inf policy;
- per-case versus pooled aggregation;
- fraction versus percentage;
- exact source/commit or wrapper version.

Do not compare identically named metrics across methods or papers until these semantics are shown compatible.

## 5. Regression gate for evaluators

No evaluator may produce a paper/benchmark-table number until deterministic synthetic regression tests pass.

Choose task-specific tests, but for deformation/Jacobian metrics the minimum gate is:

1. **Identity** — zero displacement gives the analytically expected result.
2. **Analytic transform** — a transform with known Jacobian/metric value matches expectation, including a deliberately invalid case when applicable.
3. **Independent numerical cross-check** — compare against an independent implementation on the common valid interior/domain with explicit tolerance.
4. **Background/mask test** — constant or irrelevant background cannot dilute or create the measured event; crop and mask semantics remain aligned.
5. **Unit/normalization conversion test** — normalized coordinates/flows, voxel units, physical units, and component order are converted explicitly and verified.

For other metrics, define an analogous set of analytic and adversarial fixtures.

All required tests must pass before the metric is admitted to a main table.

## 6. Independent cross-check is not ground truth

A second implementation is an **independent numerical cross-check**, not automatically a gold standard.

Before expecting equality, align:
- units/spacing;
- axis and component order;
- finite-difference stencil;
- boundary conditions;
- valid interior/crop;
- masks;
- thresholds;
- reduction.

If implementations intentionally differ, compare only the common semantic domain and record the residual difference rather than forcing equality.

## 7. Versioned correction rule

If new evidence shows that a frozen metric/protocol is materially wrong:

1. identify the defect and affected claims;
2. preserve the old artifact unchanged;
3. create a new versioned contract/artifact;
4. state the reason and semantic delta;
5. rerun every affected method under the new contract;
6. never rerun only the preferred method;
7. keep old and new results traceable.

"One method performs poorly" is never a valid reason to change the evaluator or protocol.

## 8. "Standard", "official", and "SOTA" claims

Do not use words such as:
- standard protocol;
- official metric;
- canonical implementation;
- commonly used;
- state of the art;
- reference implementation;

unless primary evidence supports the exact claim.

If a project adopts its own fair convention, name it as such, e.g. "our standardized runtime protocol", and state how it differs from external challenge/paper timing.

## 9. Fail closed on semantic uncertainty

If any of the following is unresolved and could change the conclusion, stop the claim-bearing path and mark the item `UNVERIFIED` or `BLOCKED`:

- official repository or exact revision unavailable;
- multiple forks conflict and provenance is unclear;
- API/symbol is not present where claimed;
- license is unclear and distribution depends on it;
- transformation direction/order/unit is ambiguous;
- benchmark script contradicts the paper;
- metric behavior cannot be reconstructed;
- source can only be inferred from naming or memory.

State exactly which missing evidence would unblock the claim.

## 10. Research output requirements

For a source/metric audit, preserve:
- search/access date;
- repository + commit/tag;
- exact file/function path;
- inspected code path;
- paper/benchmark citation when relevant;
- audit status;
- semantic contract;
- regression-test receipt;
- conflicts/limitations;
- decision impact.

Do not erase negative or contradictory findings. They are part of the evidence chain.
