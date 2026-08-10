# Handoff and Context Continuity Protocol

## Purpose

Prevent loss of scientific state, operational state, provenance, and next-step intent when a work session ends, an agent changes, or the conversation approaches its context limit.

A HANDOFF is part of the work product, not optional documentation reconstructed later.

## Mandatory end-of-work gate

For every non-trivial work session that changes any of the following, update the project's established `HANDOFF.md` (or exact equivalent) before declaring the work complete:

- code, configuration, protocol, dataset/split/annotation state;
- experiment, checkpoint, metric, evaluation, release, or job state;
- a scientific conclusion, invalidation, blocker, risk, or route priority;
- an external resource, environment, dependency, server, or operational boundary;
- the exact next action needed for safe continuation.

Routine explanation-only conversation, trivial formatting, or mechanical edits with no durable project-state change do not require a handoff update.

## Context-limit trigger

Do not wait for the context window to be exhausted.

Update HANDOFF immediately and stop starting optional new work when any of these occurs:

- the host warns that context/token capacity is low;
- the user says the conversation/context is close to its limit;
- the conversation has become long enough that earlier decisions or state are at material risk of being compressed or omitted;
- control is about to pass to another agent, person, session, or model;
- a long-running task is active and its exact state would be costly or unsafe to reconstruct;
- the agent is about to pause work for a substantial period.

If exact remaining-context capacity is unavailable, use conservative qualitative judgment. Preserving the current truth takes priority over starting another experiment or implementation branch.

## Emergency continuity mode

When context loss is imminent and a full cleanup is impossible, write a minimal rescue handoff first. It must contain at least:

1. timestamp/session state;
2. current truth and what changed in this session;
3. trusted versus invalid/untrusted results;
4. active jobs/processes and ownership/safety boundaries;
5. dirty-worktree or uncommitted-state warning when relevant;
6. exact files/artifacts/protocols/checkpoints/releases touched, with hashes/IDs when available;
7. unresolved blockers and competing explanations;
8. the exact next safe action.

A later session may expand the record, but must not erase the rescue provenance.

## Handoff update discipline

- Prefer updating the established project truth source instead of creating parallel handoff files.
- Preserve historical corrections. When a newer section supersedes an older conclusion, state the supersession explicitly rather than silently rewriting history.
- Record observation separately from interpretation and use the project's epistemic labels where ambiguity matters.
- Record `INVALID` runs and why they are invalid; do not delete them merely because they are inconvenient.
- Record running job IDs, dependency state, immutable release/checkpoint/protocol identity, and ownership boundaries when operational continuation depends on them.
- Record the dirty/clean workspace state when uncommitted files could change reproducibility.
- Never put passwords, private keys, tokens, transient credentials, or secret URLs in HANDOFF.
- Do not turn HANDOFF into a raw diary or copy of chat. Preserve decision-relevant state needed to continue correctly.

## Completion rule

A non-trivial work session is not `DONE` until:

1. durable project state has been written to HANDOFF/current-truth source;
2. the entry names what is verified, unverified, blocked, invalid, running, or deferred;
3. the next safe continuation step is explicit when one exists;
4. the HANDOFF passes the available linter/checklist when practical.

If HANDOFF cannot be updated because of an external failure, report the session as `BLOCKED-CONTINUITY`, preserve a local/temporary rescue record if safe, and do not pretend the work has been durably handed off.

## Context restart rule

At the start of a new session after handoff/context loss:

1. read the latest HANDOFF section first;
2. verify any time-sensitive external/job state before acting;
3. prefer newer explicitly superseding sections over historical sections;
4. do not infer that a previously running job completed successfully without checking;
5. reconstruct only the minimum additional context required for the next action.
