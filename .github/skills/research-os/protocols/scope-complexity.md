# Scope and Complexity Protocol

## Complexity budget

Before adding a new module/process, answer:
1. Which observed failure mode does it address?
2. What is the simplest alternative?
3. Is there a no-learning/linear/small baseline?
4. What new parameters/compute/confounders does it add?
5. Can it be independently ablated?
6. If it fails, what information will we gain?

If these cannot be answered, prefer `DEFER`.

## Hypothesis-driven architecture admission

Deep-learning architecture is **not module collection**. Treat each proposed module as a falsifiable hypothesis about an observed failure in the current information flow.

Before admitting a new architecture component, require all of the following where applicable:
1. **Observed failure** — name the concrete baseline behavior that is inadequate. "This module is newer/stronger/published" is not a failure observation.
2. **Information-flow location** — identify where useful information is missing, destroyed, poorly mixed, poorly normalized, insufficiently contextualized, or prematurely compressed.
3. **Mechanism match** — state why the proposed operation should address that specific failure rather than merely add capacity.
4. **Simplest alternative** — compare against the smallest credible intervention, including removing redundant transforms, a plain convolution/residual block, linear/no-learning control, or doing nothing.
5. **Discriminative test** — define the smallest experiment that can distinguish the proposed mechanism from plausible alternatives before a broad architecture rewrite.
6. **Downstream utility** — specify which task-relevant downstream metric must improve. A prettier intermediate representation/ranking metric is not sufficient when the production objective does not depend on it.
7. **Ablation/removal criterion** — define what evidence would justify keeping, removing, or deferring the component.
8. **Cost and interaction** — account for parameters, FLOPs/runtime, memory, optimization difficulty, reproducibility, attribution, and interaction with existing modules.

A paper citation, popularity, architectural novelty, or isolated success on another task is **evidence that a mechanism can work somewhere**, not evidence that the current model needs it.

Do not assume independently useful modules combine additively. `A > baseline` and `B > baseline` does not imply `A+B > A` or `A+B > B`. Multiple new modules in one attribution-sensitive experiment require either prior independent evidence for each component or an explicit interaction hypothesis.

Prefer the simplest architecture that preserves the required downstream behavior. If a simpler baseline matches a more complex variant within the decision-relevant uncertainty/cost tradeoff, prefer the simpler baseline unless the complex component enables a separate necessary capability.

When two adjacent modules perform substantially the same transformation, require evidence of complementarity. Redundant capacity or repeated projection/downsampling/mixing should not be retained merely because both operations are individually plausible.

Recommended sequence for architecture work:

`minimal baseline → locate failure → propose mechanism → one-component intervention → ablation → cumulative simplification → interaction test only if needed`

For architecture decisions, use the standard outcomes consistently:
- `KEEP` — valid evidence shows decision-relevant downstream benefit or a necessary capability under stated conditions;
- `REJECT` — a valid controlled comparison shows the component does not justify its cost/complexity under the tested conditions;
- `DEFER` — the component is plausible, but the corresponding failure mode or expected utility has not yet been established;
- `INVALID` — the comparison cannot support an architecture decision because attribution, data, protocol, loading, or evaluation is broken.

## Scope gate

For every major next step, classify it:
- **PRIMARY** — directly advances the paper/project's current primary claim;
- **VALIDATION** — necessary to make the primary claim credible;
- **BACKLOG** — useful extension but not required now;
- **SEPARATE PROJECT** — changes the research question enough to deserve independent scope.

Do not allow an attractive extension to silently redefine the project.

## Over-engineering detector

Watch the ratio:

`new scientific information / new code + rules + runtime + coordination cost`

If it falls, simplify the experiment or return to diagnosis.

This detector applies to **process complexity as well as model complexity**. Safety/review work that no longer changes execution safety, claim validity, attribution, or the decision can itself become over-engineering. Use `risk-proportional-audit.md` to distinguish blockers from non-blocking hardening.

## Architecture escalation

Do not move from a local failure to a large architecture rewrite without evidence that the simpler intervention cannot answer the question.

Likewise, do not move a low-risk diagnostic into a high-assurance release/final-test review regime without a concrete risk that justifies escalation.
