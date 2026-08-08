# Competing-Hypothesis Protocol

## Start with one question

Reduce the task to one falsifiable research question whenever possible.

## Generate alternatives

For any important unexplained result, list plausible causes from multiple categories:
- data / labels / split;
- coordinate or preprocessing protocol;
- metric implementation;
- model representation;
- optimization;
- downstream capacity / regularization;
- distribution shift;
- random variation / sample selection;
- systems/runtime defect.

Do not create alternatives merely for symmetry; include those that could realistically explain the observation.

## Hypothesis table

For each hypothesis record:
- predicted observations if true;
- current supporting evidence;
- counter-evidence;
- confounders;
- smallest discriminative test;
- result that would weaken/reject it.

## Prefer discriminatory tests

Choose experiments that make competing hypotheses predict different outcomes. A test that improves a metric but cannot distinguish why it improved has low scientific information value.

## Scientific kill switch

Every major line needs a predeclared answer to:

> What valid result would make us stop believing or stop prioritizing this idea?

If no possible result can reject/deprioritize the idea, the hypothesis is not operationally falsifiable.

## Correlation with downstream utility

When proposing a new diagnostic metric, require more than intuitive plausibility. Test whether it predicts or explains the downstream quantity better than existing simpler diagnostics, under frozen validation protocols.
