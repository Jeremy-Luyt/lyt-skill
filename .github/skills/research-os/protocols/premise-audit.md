# Premise and Reasoning Audit

## Purpose

Before solving a consequential research question, check whether the question itself is well-formed. Do not optimize an answer to a false premise, unsupported causal story, incomplete specification, or stale fact.

This protocol runs before method selection and before expensive implementation.

## 1. Premise check

For each material premise, classify it as one of:
- **VERIFIED** — supported by direct project evidence or a current authoritative source;
- **USER-REPORTED** — supplied by the user/collaborator but not independently verified;
- **INFERRED** — follows from evidence but is not directly observed;
- **ASSUMED** — temporarily accepted to proceed;
- **UNKNOWN** — evidence is insufficient;
- **CONTRADICTED** — available evidence argues against it.

Do not silently upgrade USER-REPORTED, INFERRED, ASSUMED, or UNKNOWN material into fact.

## 2. Logic-jump check

Look explicitly for:
- observation → mechanism jumps;
- correlation → causation jumps;
- intermediate metric → end-to-end performance jumps;
- one configuration → whole method-class generalization;
- benchmark improvement → scientific novelty;
- model capacity → explanation of failure;
- absence of evidence → evidence of absence;
- a plausible story presented as the only explanation.

When a jump exists, state it plainly and name the missing evidence.

## 3. Missing-information check

Ask what missing information could materially reverse the decision. Typical examples:
- dataset identity/version or split;
- coordinate, unit, axis, or preprocessing conventions;
- checkpoint/config provenance;
- sample/subject pairing semantics;
- annotation protocol;
- exact metric definition;
- baseline compute/capacity;
- publication/version status;
- hardware/software version;
- statistical uncertainty.

Do not ask for information that is irrelevant to the decision. Prefer direct inspection when available.

## 4. Independent-judgment rule

The user's preferred conclusion is not evidence. Agreement is not an objective.

If the evidence disagrees with the requested framing:
1. say what you disagree with directly;
2. cite or name the evidence;
3. explain the risk of proceeding under the false premise;
4. give plausible alternative explanations;
5. propose the smallest check that resolves the disagreement.

Do not soften a scientific disagreement merely to preserve the narrative.

## 5. Verification rule for concrete claims

When a number, person, paper status, benchmark result, date, dataset property, or other concrete claim materially affects the decision, verify it from the strongest available source when feasible.

Priority:
1. direct project artifact / raw data / log / code;
2. primary paper, official repository, official dataset or documentation;
3. reputable independent source;
4. collaborator/user report, explicitly labeled as such.

If verification is not possible, preserve the uncertainty instead of inventing precision.

## 6. Ignored-variable, cost, and bias scan

Before recommending a path, surface material factors the initial framing may omit:
- confounders and hidden controlled variables;
- selection/survivorship/publication bias;
- label or measurement error;
- dataset shift and representativeness;
- compute, engineering, annotation, runtime, maintenance, and opportunity cost;
- leakage risk and repeated-test feedback;
- unequal model capacity or training budget;
- metric incentives that may not match the scientific claim.

Only mention factors capable of changing the decision; avoid generic caveat dumping.

## Output

For high-stakes work, the Prompt Contract should contain a short **Premise Audit** with:
- verified premises;
- unverified/contradicted premises;
- logic jumps;
- decision-critical missing information;
- material ignored variables/costs/biases;
- resulting action: proceed / inspect first / reframe / block.
