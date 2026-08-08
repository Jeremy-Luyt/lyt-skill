# Preflight Checklist

Use only relevant items; record failures before GPU/long execution.

- [ ] Data paths exist and expected sample counts match.
- [ ] Train/validation/test sets are disjoint as required.
- [ ] Shapes, axes, coordinates, units, spacing, and orientation are explicit.
- [ ] Label/annotation protocol version is explicit.
- [ ] Checkpoint architecture/keys are compatible; no silent fallback.
- [ ] Baseline checkpoint/config is frozen and identifiable.
- [ ] Metric implementation and scope are known.
- [ ] Changed variable and controls match the Experiment Contract.
- [ ] Environment/tool versions are recorded.
- [ ] Output directory is isolated; no unintended overwrite.
- [ ] Resume behavior is understood and provenance-preserving.
- [ ] Resource request, runtime, storage, and permissions are plausible.
- [ ] Destructive/shared-resource actions are authorized.
- [ ] Final-test data are not being used for development decisions.
