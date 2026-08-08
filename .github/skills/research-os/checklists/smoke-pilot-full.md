# Smoke → Pilot → Full Checklist

## Smoke
- [ ] Smallest real input reaches intended code path.
- [ ] Forward succeeds and shapes/ranges are sane.
- [ ] Loss/metrics finite.
- [ ] Backward finite when applicable.
- [ ] New trainable module receives gradient when expected.
- [ ] One optimizer step succeeds when applicable.
- [ ] Logging/output fields exist.
- [ ] No baseline/checkpoint/data overwrite.

## Pilot
- [ ] Bounded runtime/epochs/steps declared.
- [ ] No NaN/OOM/systemic instability.
- [ ] No obvious severe regression.
- [ ] Checkpoint/resume/logging works.
- [ ] Trend is informative enough to justify or stop full run.

## Full
- [ ] Contract frozen/versioned.
- [ ] Development/final-test boundary preserved.
- [ ] Full logs and provenance retained.
- [ ] Mid-run protocol changes trigger stop/version, not silent continuation.
- [ ] Post-run audit completed before scientific interpretation.
