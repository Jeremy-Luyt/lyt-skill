# Epistemic Discipline

## Labels

Use these labels in research notes when the distinction matters:

- **FACT** — directly observed in project data/logs/code/results.
- **SOURCE** — supported by an external source; cite it.
- **INFERENCE** — reasoned conclusion from facts/sources, not directly observed.
- **HYPOTHESIS** — falsifiable explanation or prediction awaiting adequate test.
- **ASSUMPTION** — accepted temporarily to proceed; must be visible.
- **UNKNOWN** — evidence currently insufficient.

## Observation / interpretation split

Write observations before mechanisms. Example:

- FACT: intermediate metric improved substantially.
- FACT: end-to-end metric changed little.
- HYPOTHESIS: intermediate outputs may be structurally inconsistent.
- ALTERNATIVE: downstream model capacity/regularization may be insufficient.
- UNKNOWN: which explanation dominates under a protocol-correct controlled test.

Do not collapse this into “the intermediate outputs are inconsistent” until alternatives are excluded.

## Claim strength ladder

Prefer the strongest claim actually supported:
1. observed association;
2. robust association across controls;
3. mechanism consistent with evidence;
4. competing explanations materially excluded;
5. causal/mechanistic claim.

Do not jump levels because the narrative is attractive.

## Invalid evidence

A run with leakage, wrong coordinate convention, broken metric, mismatched checkpoint, wrong split, silent protocol drift, failed dependency, or other material defect is `INVALID`. It is not evidence for or against the scientific hypothesis.

## Negative-result discipline

A valid negative result should specify:
- exact configuration tested;
- conditions under which it failed;
- what conclusion is justified;
- what conclusion is not justified;
- what new evidence would justify revisiting it.

Never generalize “this configuration failed” into “this method class never works” without evidence.
