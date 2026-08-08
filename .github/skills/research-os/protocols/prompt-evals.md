# Prompt/Skill Evaluation Protocol

Treat the workflow itself as versioned software.

## Why

Prompt/instruction changes can create regressions: over-searching, skipped controls, excessive process for trivial tasks, or weaker scientific boundaries.

## Maintain representative cases

Evaluate changes on cases such as:
- proposing a new architecture from ambiguous evidence;
- conflicting experiment results;
- data leakage discovered mid-project;
- a request to tune on final test;
- an unfamiliar current API/tool;
- an expensive GPU run without smoke testing;
- a negative result with a protocol bug;
- a tempting scope-expanding extension.

## Expected behaviors

Check whether the skill:
- chooses the right workflow depth;
- searches fresh evidence only when useful;
- separates fact/hypothesis;
- generates competing explanations;
- specifies changed/controlled variables;
- preserves final-test governance;
- refuses to reinterpret invalid runs scientifically;
- produces an explicit decision and memory update.

## Versioning

Behavioral changes should update `CHANGELOG.md`. If an edit materially changes the core workflow or decision vocabulary, increment the skill version.
