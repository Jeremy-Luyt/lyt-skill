# Security and Operations Protocol

Research reliability includes operational safety.

## Decision rights

Agents may usually perform, when allowed by the host/project:
- read-only inspection;
- literature/GitHub/documentation search;
- static analysis;
- drafting plans/contracts;
- isolated reversible experiments;
- adding logs/documentation.

Require explicit authority or stronger review before:
- changing data splits or evaluation protocols;
- deleting/overwriting checkpoints or source data;
- destructive shared-server actions;
- modifying system Python/CUDA/drivers/shared environments;
- changing the paper's primary metric/claim;
- publishing/releasing sensitive data.

## Shared compute

- use isolated user directories/environments;
- do not inspect/stop other users' jobs unless authorized;
- use scheduler-native job control;
- request only necessary resources;
- keep outputs/checkpoints in owned paths;
- record job IDs for long experiments.

## Credentials

Never write passwords, private keys, tokens, temporary SSH secrets, or credential-bearing URLs into prompts, repositories, logs, HANDOFF, or experiment records.

## Data mutation

Prefer copy/staging/atomic replacement over in-place destructive edits. Preserve source data and provenance unless mutation is explicitly intended and authorized.
