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

## Architecture escalation

Do not move from a local failure to a large architecture rewrite without evidence that the simpler intervention cannot answer the question.
