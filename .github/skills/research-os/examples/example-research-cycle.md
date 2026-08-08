# Example: from an attractive explanation to a valid experiment

## Observation
A new intermediate scoring method cuts pointwise error substantially, but the downstream model's final error barely changes.

## Bad shortcut
“Therefore the selected points are geometrically impossible.”

This overclaims: downstream capacity, regularization, coordinate conventions, or distribution shift could produce the same observation.

## Competing hypotheses
- H1: selected points are mutually/structurally inconsistent.
- H2: downstream model lacks capacity.
- H3: downstream regularization is too strong.
- H4: downstream model is out of distribution for these points.
- H5: evaluation or coordinate protocol is wrong.

## Minimal plan
1. Audit protocol/coordinates first.
2. Freeze the candidate correspondences.
3. Compare fixed, prespecified downstream hypothesis classes on development data.
4. Separate fit residual from spatially held-out residual and final downstream error.
5. Do not use final test to choose downstream capacity.

## Decision logic
If the phenomenon disappears after a protocol fix, mark prior evidence `INVALID`.
If it persists only in one downstream class, do not claim universal structural inconsistency.
If it persists across controlled classes and a structural diagnostic predicts downstream utility, the structural hypothesis gains support.

The lesson is the workflow: **observation → alternatives → discriminative experiment**, not the domain-specific mechanism.
