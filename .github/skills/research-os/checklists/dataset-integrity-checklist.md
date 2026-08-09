# Dataset Integrity Checklist

Use before claim-bearing training/evaluation. Mark `N/A` explicitly when a check does not apply.

## Identity / provenance
- [ ] Dataset/version/source is identified.
- [ ] Raw, cleaned, derived, and evaluation artifacts are distinguishable.
- [ ] Sample manifest exists and sample IDs are unique.
- [ ] Claim-bearing frozen artifacts have hashes or equivalent provenance where practical.

## Format / schema
- [ ] Files open and are not truncated/corrupt.
- [ ] Shape, rank, dtype, channels, metadata, and value ranges are plausible.
- [ ] NaN/Inf, empty masks/files, malformed rows, and duplicate coordinates are checked.
- [ ] Axis/order conventions are explicit (`xyz/zyx`, channel order, etc.).
- [ ] Units and coordinate representation are explicit.

## Geometry / transforms
- [ ] Physical spacing/origin/orientation/affine are checked.
- [ ] Fixed↔moving transform direction is explicit.
- [ ] Input↔feature-grid/normalized-coordinate mapping is tested.
- [ ] Interpolation mode matches data semantics.
- [ ] OOB/boundary behavior is measured, not silently hidden.
- [ ] Round-trip coordinate tests pass on known points.

## Pairing / correspondence
- [ ] Paired files belong to the intended specimen/task.
- [ ] Landmark/correspondence identity is guaranteed by ID/protocol, not row-index assumption.
- [ ] Cross-sample correspondence mappings are independently validated.
- [ ] Manual vs propagated/synthetic/model-generated supervision is labeled.

## Split / leakage
- [ ] Train/validation/test IDs are disjoint.
- [ ] Subject/specimen/session and near-duplicate leakage are checked.
- [ ] Templates/atlases/statistics fitted from test subjects are excluded unless protocol explicitly allows it.
- [ ] Final test has not influenced checkpoint/threshold/ROI/candidate selection.

## Sampling
- [ ] Independent experimental unit is defined.
- [ ] Sampling/stratification/oversampling/filtering policy is recorded.
- [ ] Pseudo-replication risk is checked.
- [ ] Seeds/state are recorded when required.
- [ ] Exclusions/missing samples are prespecified or transparently reported.

## Annotation
- [ ] Label ontology/IDs/merges/background semantics are defined.
- [ ] Missing vs not-annotated labels are distinguished.
- [ ] Annotation provenance and annotator protocol are known where material.
- [ ] Label transforms preserve categorical values.
- [ ] ROI/sample exclusions are frozen before model-result inspection.

## Distribution / representativeness
- [ ] Train/validation/test modality/site/batch/resolution/intensity differences are summarized.
- [ ] Target-use distribution is represented or the shift is explicitly intentional.
- [ ] Missingness/corruption/label prevalence differences are checked.

## Sanity / gate
- [ ] Normal, boundary/extreme, and labeled/paired examples were inspected end-to-end.
- [ ] Identity/no-op or toy metric case passes when applicable.
- [ ] Dataset Integrity Report is written.
- [ ] Gate status is exactly one: PASS / PASS-WITH-LIMITATIONS / BLOCKED / INVALID-DATA.
