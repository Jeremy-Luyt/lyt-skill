# Evidence Acquisition Protocol

## Trigger

Search externally when fresh information could materially change the decision: new methods, current APIs/toolchains, baselines, benchmark protocols, datasets, pretrained weights, journal requirements, hardware/runtime behavior, or an unfamiliar high-stakes workflow.

Do not search merely to decorate an answer.

## Source priority

1. Original paper, standard, official documentation.
2. Official author/project repository and release notes.
3. Official dataset/benchmark/pretrained-weight page.
4. Strong independent replication or systematic comparison.
5. GitHub Issues/PRs/discussions for implementation failure modes.
6. Community posts/blogs only as discovery aids unless independently verified.

A GitHub issue can establish that users observed a problem; it does not by itself establish a scientific conclusion.

## Freshness classes

- **stable** — mathematics/classic theory; old sources may be fine.
- **slow-changing** — established algorithms and mature libraries; verify when implementation details matter.
- **current** — frameworks, journal guidelines, benchmarks, tool behavior; prefer recent official sources.
- **latest** — SOTA claims, active APIs, fast-moving agent/LLM tooling; search current sources before deciding.

## Search layers for a new method

When relevant, investigate:
- paper definition and assumptions;
- supplementary/evaluation protocol;
- official code path actually implementing the claimed mechanism;
- checkpoint and data requirements;
- open issues/PRs that reveal practical constraints;
- recent competing methods;
- public datasets and split rules;
- pretrained weights/licenses;
- runtime/compute requirements.

## Evidence log

For consequential decisions, record:
- date;
- query intent, not just raw query text;
- source URL/DOI/repository;
- source type and authority;
- exact claim supported;
- what decision it changes;
- unresolved conflict or limitation.

Use `../templates/evidence-log.md`.

## Search stopping rule

Stop when additional sources are unlikely to change the current decision or when the evidence conflict itself becomes the next research question. Do not turn evidence acquisition into endless browsing.
