# Execution Gates

## Gate 0 — Static/preflight

Before expensive execution, verify what can be checked without a full run:
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

## Gate 1 — Smoke

Use the smallest real example that exercises the intended path:
- forward succeeds;
- outputs have correct shape/range;
- loss finite;
- backward finite if training;
- gradient reaches newly introduced trainable components;
- one optimizer step succeeds;
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

## Gate 3 — Full

Only after prior gates pass:
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
