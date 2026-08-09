# Dataset Integrity Gate

## Purpose

Before interpreting model behavior, changing architecture, or launching an expensive experiment, verify that the dataset and its derived supervision actually represent the task being claimed.

A model cannot rescue invalid pairing, wrong coordinates, corrupted labels, split leakage, or inconsistent preprocessing. Dataset defects discovered after a run can make the run `INVALID`, not merely "noisy".

Use this gate for any data-bearing experiment. The depth should scale with stakes and novelty.

## Gate status

Record exactly one status before claim-bearing execution:
- **PASS** — required checks are complete and no material defect is known;
- **PASS-WITH-LIMITATIONS** — known limitations are documented and do not invalidate the planned claim;
- **BLOCKED** — required evidence is missing; inspect before execution;
- **INVALID-DATA** — a material dataset/supervision defect is confirmed; affected experiments cannot be scientifically interpreted.

## 1. Dataset identity and provenance

Verify:
- dataset name, version/date, source, license/usage restrictions where relevant;
- immutable manifest or equivalent sample inventory;
- raw vs cleaned vs derived data are distinguishable;
- checksums/hashes for claim-bearing frozen artifacts when practical;
- every derived artifact can be traced to its source and transformation pipeline.

Do not assume a newly copied file is a new dataset version or that a recently modified file contains recent data.

## 2. File-format and schema integrity

Check what is relevant to the modality:
- files open successfully and are not truncated/corrupted;
- expected extension/container matches actual content;
- dtype, byte order, channel count, shape/rank, compression and metadata are plausible;
- image orientation/affine/header/spacing are internally consistent;
- units are explicit and consistent;
- missing/empty files, NaN/Inf, impossible ranges, empty masks, duplicate coordinates, and malformed rows are detected;
- serialization/deserialization preserves values and ordering.

For multidimensional scientific data, explicitly audit axis conventions such as `xyz` vs `zyx`, channel-first vs channel-last, physical coordinates vs voxel coordinates, and normalized `[-1,1]` coordinates vs index coordinates.

## 3. Coordinate, geometry, and resampling integrity

Verify:
- coordinate frame and transform direction (fixed→moving vs moving→fixed);
- voxel spacing and physical-to-index conversion;
- origin/orientation/affine consistency;
- feature-grid/input-grid mappings and actual receptive/search-window geometry;
- `align_corners`, padding, clipping and boundary behavior where grid sampling is used;
- interpolation is appropriate to data type: labels/categorical masks normally require nearest-neighbor semantics;
- round-trip coordinate tests on corners, center, random points, and known correspondences;
- out-of-bounds rates are measured rather than silently clamped.

A coordinate bug invalidates conclusions about search coverage, correspondence error, deformation quality, or metric performance.

## 4. Sample identity, pairing, and correspondence semantics

Verify:
- sample IDs are unique and stable;
- paired files actually belong to the same subject/specimen/timepoint/task;
- row/index identity across files is documented rather than assumed;
- landmark/correspondence arrays have compatible counts only when count equality is scientifically meaningful;
- cross-sample landmark identity uses an explicit canonical ID or validated mapping;
- duplicate or near-duplicate subjects/derived versions are identified;
- synthetic or propagated labels are marked as derived supervision, not manual ground truth.

Never infer anatomical correspondence from equal row number alone unless the annotation protocol guarantees shared identity.

## 5. Split and leakage audit

Check leakage at all relevant levels:
- exact file/sample ID overlap;
- subject/specimen overlap;
- repeated acquisition/session overlap;
- near-duplicate or transformed-copy overlap;
- atlas/template construction using test subjects;
- normalization/statistics/feature dictionaries fitted using final-test data;
- labels or annotations created using information from the evaluated target;
- hyperparameter, threshold, checkpoint, ROI, or candidate selection influenced by final-test performance.

Development selection belongs on train/validation data. The final test is confirmatory after the method and selection rule are frozen.

## 6. Sampling audit

Verify:
- what the sampling unit is: subject, image, patch, voxel, landmark, pair, ROI, frame, etc.;
- sampling probabilities and replacement rules;
- stratification, class/ROI weighting, oversampling, hard-negative mining and filtering;
- deterministic seed/state where reproducibility matters;
- whether multiple sampled units from one subject create pseudo-replication;
- whether the evaluation sample distribution represents the target use case;
- whether excluded/missing samples are prespecified or post hoc.

Report both sample counts and independent experimental-unit counts when they differ.

## 7. Annotation and ground-truth audit

Verify:
- label IDs, ontology, canonical merges/splits and background semantics;
- missing labels/regions and whether absence means "not present" or "not annotated";
- annotator protocol and, when material, inter/intra-rater variability;
- manual, semi-automatic, propagated, synthetic and model-generated labels are distinguished;
- correspondence/landmark identity is validated on a small visual/manual subset;
- label transformations preserve categorical semantics;
- annotation changes are versioned and applied symmetrically where required;
- evaluation exclusions are fixed before viewing model performance.

Do not use low model performance itself as evidence that an annotation/ROI should be removed.

## 8. Distribution and representativeness audit

Inspect train/validation/test for differences in:
- modality/scanner/protocol/site/batch;
- spatial resolution and field of view;
- intensity statistics and preprocessing;
- subject attributes relevant to the task;
- label prevalence and ROI availability;
- corruption/missingness rates.

Distinguish intentional domain shift from accidental split bias.

## 9. Sanity checks before scale

Before a full run, inspect a small set end-to-end:
- at least one normal sample;
- one boundary/extreme sample;
- one labeled/paired sample when available;
- visual overlay or equivalent domain-appropriate check;
- known identity/no-op case when possible;
- metric calculation on a hand-checkable toy example.

Automated checks should fail fast on material violations rather than silently clamp, skip, relabel, or continue.

## 10. Dataset Integrity Report

For claim-bearing experiments, record:
- dataset/version/manifest/hash or equivalent;
- split definition and leakage result;
- format/schema/shape/dtype checks;
- coordinate/unit/orientation result;
- pairing/correspondence identity result;
- sampling policy;
- annotation/label protocol;
- missing/OOB/corrupt/duplicate statistics;
- known distribution shifts;
- unresolved limitations;
- gate status and date.

If a later audit changes any material item, version the dataset/protocol and reclassify affected evidence explicitly.
