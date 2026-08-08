# Decision and Memory Protocol

## Decision

Every completed experiment receives exactly one primary status:

- KEEP
- REJECT
- DEFER
- INVALID

Record the reason in one or two sentences before elaboration.

## Conditional principle extraction

Convert results into reusable knowledge using four fields:
1. local conclusion;
2. generalizable lesson;
3. conditions under which it holds;
4. evidence that would justify revisiting it.

Avoid unconditional rules from a single configuration.

## Immediate updates

Update project truth sources immediately after:
- a phase completes;
- a bug invalidates prior results;
- split/metric/protocol/checkpoint changes;
- a major route becomes KEEP/REJECT/DEFER;
- a long-running job starts with important state;
- context is about to be handed to another agent/person.

## Handoff content

A handoff should preserve:
- current truth;
- trusted results;
- invalid/untrusted results;
- frozen defaults;
- rejected/deferred routes;
- active hypotheses;
- known risks/blockers;
- running jobs and ownership boundaries;
- exact next action/command when appropriate;
- provenance.

Do not turn HANDOFF into an unstructured diary.
