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
- every non-trivial work session that changes durable project/scientific/operational state;
- a phase completes;
- a bug invalidates prior results;
- split/metric/protocol/checkpoint changes;
- a major route becomes KEEP/REJECT/DEFER;
- a long-running job starts with important state;
- context/token capacity is becoming low enough that prior state could be lost;
- control is about to pass to another agent/person/session/model;
- work is about to pause while important uncommitted/running state exists.

For the full trigger and emergency rules, read `handoff-continuity.md`.

## End-of-work continuity gate

For non-trivial work, updating HANDOFF/current-truth state is part of completion. Do not declare the session fully done until the durable handoff records what changed, what is trusted/invalid, what remains unresolved, running external state, and the next safe continuation step when one exists.

If the host or user indicates the context window is close to its limit, stop starting optional new work and write the handoff first. When exact remaining capacity is unavailable, use conservative qualitative judgment.

If continuity cannot be durably written because of an external failure, report `BLOCKED-CONTINUITY` rather than pretending the work has been handed off.

## Handoff content

A handoff should preserve:
- session/context continuity state and timestamp;
- current truth;
- trusted results;
- invalid/untrusted results;
- frozen defaults;
- rejected/deferred routes;
- active hypotheses;
- known risks/blockers;
- running jobs and ownership boundaries;
- dirty/clean workspace or uncommitted-state warning when material;
- exact next action/command when appropriate;
- provenance, including file/protocol/checkpoint/release/job hashes or IDs when material.

Do not turn HANDOFF into an unstructured diary. Preserve superseded conclusions explicitly instead of silently deleting history, and never store secrets.
