# Evaluation Checklist

- [ ] Evaluation question and metric scope are explicit.
- [ ] Dataset/split/sample list matches the frozen protocol.
- [ ] Checkpoint and code snapshot are verified.
- [ ] Coordinate/unit/direction conventions are verified.
- [ ] Raw/intermediate and downstream metrics are not conflated.
- [ ] Missing/invalid values are handled explicitly, not silently dropped.
- [ ] Per-sample results are retained when feasible.
- [ ] Mean is accompanied by dispersion/CI when the claim needs it.
- [ ] Statistical comparison is paired when the design is paired.
- [ ] Safety/topology/runtime metrics use the same scope across compared methods.
- [ ] Different protocol versions are not merged into one comparison table.
- [ ] Final-test results did not influence development choices.
