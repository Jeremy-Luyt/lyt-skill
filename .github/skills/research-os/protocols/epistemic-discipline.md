# Epistemic Discipline

## Labels

Use these labels in research notes when the distinction matters:

- **FACT** — directly observed in project data/logs/code/results.
- **SOURCE** — supported by an external source; cite it.
- **USER-REPORTED** — supplied by a user/collaborator but not independently verified.
- **INFERENCE** — reasoned conclusion from facts/sources, not directly observed.
- **HYPOTHESIS** — falsifiable explanation or prediction awaiting adequate test.
- **ASSUMPTION** — accepted temporarily to proceed; must be visible.
- **ALTERNATIVE** — plausible competing explanation that could account for the same observation.
- **JUDGMENT** — recommendation or value-laden assessment based on stated criteria; not an empirical fact.
- **UNKNOWN** — evidence currently insufficient.

Do not silently promote USER-REPORTED, INFERENCE, ASSUMPTION, JUDGMENT, or UNKNOWN content into FACT/SOURCE.

## Observation / interpretation split

Write observations before mechanisms. Example:

- FACT: intermediate metric improved substantially.
- FACT: end-to-end metric changed little.
- HYPOTHESIS: intermediate outputs may be structurally inconsistent.
- ALTERNATIVE: downstream model capacity/regularization may be insufficient.
- UNKNOWN: which explanation dominates under a protocol-correct controlled test.

Do not collapse this into “the intermediate outputs are inconsistent” until alternatives are excluded.

## Premise and logic discipline

Before answering a consequential question, inspect whether the framing contains:
- an unsupported or contradicted premise;
- an observation→mechanism or correlation→causation jump;
- an intermediate→downstream metric substitution;
- an unjustified generalization from one dataset/configuration;
- decision-critical missing information.

Use `premise-audit.md` when any of these can change the recommendation.

## Independent judgment

The user's preferred answer is not evidence. Do not preserve a narrative because it is motivating, convenient, prestigious, or already implemented.

When evidence conflicts with the requested framing:
- state the disagreement directly;
- distinguish what is verified from what is inferred;
- identify the risk of proceeding under the disputed premise;
- name plausible alternative explanations;
- propose the smallest resolving check.

Avoid both reflexive agreement and reflexive contrarianism.

## Verification of concrete claims

When a precise number, date, person, paper/publication status, dataset property, benchmark result, or other concrete claim materially affects a decision, verify it from the strongest available source when feasible.

If only a collaborator/user statement is available, label it USER-REPORTED. If sources conflict, preserve the conflict instead of choosing the more convenient version silently.

## Claim strength ladder

Prefer the strongest claim actually supported:
1. observed association;
2. robust association across controls;
3. mechanism consistent with evidence;
4. competing explanations materially excluded;
5. causal/mechanistic claim.

Do not jump levels because the narrative is attractive.

## Material omitted-factor scan

Before a recommendation, ask whether any omitted factor could reverse the decision:
- confounding or hidden variable;
- label/measurement error;
- sampling or selection bias;
- dataset shift/representativeness;
- leakage or repeated final-test feedback;
- unequal capacity/compute;
- runtime, annotation, engineering, maintenance, and opportunity cost;
- metric mismatch with the actual scientific objective.

Surface material factors proactively. Do not pad answers with generic caveats that do not affect the decision.

## Invalid evidence

A run with leakage, wrong coordinate convention, broken metric, mismatched checkpoint, invalid pairing/supervision, wrong split, silent protocol drift, failed dependency, corrupted data, or other material defect is `INVALID`. It is not evidence for or against the scientific hypothesis.

## Negative-result discipline

A valid negative result should specify:
- exact configuration tested;
- conditions under which it failed;
- what conclusion is justified;
- what conclusion is not justified;
- what new evidence would justify revisiting it.

Never generalize “this configuration failed” into “this method class never works” without evidence.
