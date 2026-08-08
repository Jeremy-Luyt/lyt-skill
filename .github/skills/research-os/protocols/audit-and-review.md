# Audit and Review Protocol

## Challenger objective

Assume an apparent improvement may be explained by leakage, protocol drift, extra capacity, data selection, metric artifacts, implementation bugs, or unequal compute until those explanations are addressed.

The Challenger is skeptical, not adversarial for its own sake.

## Review order

1. **Validity** — did the run test what it claims?
2. **Comparability** — are baseline and variant on the same data/protocol/compute where required?
3. **Attribution** — what changed besides the named variable?
4. **Statistics** — is the effect stable enough for the claim?
5. **Mechanism** — do results distinguish the proposed mechanism from alternatives?
6. **Generality** — what conditions bound the conclusion?

## Code review focus

Check:
- tensor/axis/unit conventions;
- train/eval mode;
- masking/padding/normalization semantics;
- gradients and zero-init behavior;
- data loader/split leakage;
- checkpoint strictness;
- metric formulas;
- hidden fallback behavior;
- silent exception handling;
- nondeterministic selection;
- accidental changes to frozen components.

## Builder/Challenger separation

Prefer:
`Builder implementation → smoke → Challenger diff/protocol audit → revision → full run`.

Do not let both roles make unsynchronized edits to the same experiment branch/files.

## Actionable criticism

Every major objection must state:
- what could be wrong;
- why it matters to the claim;
- what evidence/check would resolve it.
