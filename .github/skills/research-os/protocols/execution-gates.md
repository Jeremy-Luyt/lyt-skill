# Execution Gates

Before applying the gates, classify the action's scientific/operational risk using `risk-proportional-audit.md`. Gates must be strong enough to protect validity and safety, but low-risk diagnostics must not be blocked by controls that only matter to final-test, destructive, shared-resource, or immutable-release operations.

## Gate 0 — Static/preflight

Before expensive or claim-bearing execution, verify the task-relevant subset of what can be checked without a full run:
- data split and leakage;
- required files and shapes;
- units/axes/coordinate conventions;
- label/metric protocol version;
- checkpoint architecture and strict key compatibility;
- configuration/CLI validity;
- output path isolation;
- environment/tool versions;
- storage quota and permissions;
- expected resource request;
- resume semantics and checkpoint provenance.

Use `../checklists/preflight.md`.

For an R0 read-only diagnostic, Gate 0 should normally be a single bounded pass covering source/checkpoint identity, development/validation split, fixed comparison inputs/masks/metric semantics, output isolation, and hidden-write risk. When those pass and no `BLOCK-EXECUTION` finding remains, proceed instead of expanding into unrelated release/security audits.

## Gate 1 — Smoke

Use the smallest real example that exercises the intended path:
- forward succeeds;
- outputs have correct shape/range;
- loss finite;
- backward finite if training;
- gradient reaches newly introduced trainable components;
- one optimizer step succeeds when training is part of the task;
- no unintended file overwrite;
- key metrics/log fields exist.

A smoke test proves executability, not scientific value.

## Gate 2 — Pilot

Run a short, bounded experiment sufficient to detect:
- divergence/NaN/OOM;
- obvious regression;
- dead gradients;
- broken logging/checkpointing;
- whether the hypothesized trend is plausible.

Do not over-interpret pilot metrics.

R0 read-only diagnostics often do not need a separate pilot after the smallest real diagnostic succeeds. Record why a gate is inapplicable instead of manufacturing unnecessary work.

## Gate 3 — Full

Only after applicable prior gates pass:
- execute the frozen contract;
- preserve logs/checkpoints;
- do not tune mid-run based on final-test behavior;
- if a material protocol change is required, stop/version the experiment instead of silently continuing.

## Gate 4 — Post-run audit

Before scientific interpretation:
- verify actual checkpoint/config used;
- verify sample set;
- verify metric protocol;
- verify output completeness;
- inspect anomalies/missing values;
- distinguish run failure from hypothesis failure.

Use finding severities from `risk-proportional-audit.md`: `BLOCK-EXECUTION`, `BLOCK-INTERPRETATION`, `BOUNDS-CLAIM`, or `FOLLOW-UP`. Non-blocking hardening items should be retained without retroactively pretending that a valid bounded diagnostic could not have run.
