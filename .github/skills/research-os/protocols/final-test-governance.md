# Final-Test Governance

## Development vs final test

Use training/development/validation data to choose:
- architecture;
- hyperparameters;
- thresholds;
- candidate methods;
- projector/model capacity;
- metric variants;
- block/split protocol;
- early stopping and selection rules.

Freeze these before the final test.

## Final-test rule

Once the protocol is frozen, evaluate the final test as a confirmatory run. Do not repeatedly inspect test outcomes and then change the model/protocol to improve them.

## If a test protocol bug is discovered

1. Mark affected results `INVALID`.
2. Document the bug and affected claims.
3. Fix and version the protocol.
4. Re-freeze using development evidence.
5. Re-run the test transparently.

Do not pretend the corrected rerun was the original untouched confirmatory test.

## Post-hoc exclusions

Do not remove samples, regions, seeds, or metrics after seeing poor model performance unless the exclusion rule was prespecified or the data are objectively invalid under a protocol-independent criterion. Preserve excluded-item results and rationale when scientifically relevant.

## Test-set publication language

State which decisions were made on development data and when the test protocol was frozen. Avoid claims of untouched generalization if test feedback influenced model selection.
