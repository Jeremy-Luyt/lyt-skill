# Repository agent instructions

This repository contains the LYT ResearchOS Agent Skill. Treat it as a methodology package, not as an application project.

## Before editing

1. Read `README.md` and `.github/skills/research-os/SKILL.md`.
2. Read only the protocol/role/template files relevant to the requested change; preserve progressive disclosure.
3. Distinguish methodology changes from wording/packaging changes.
4. Do not silently weaken scientific-integrity, final-test, provenance, or operational-safety rules.

## Change discipline

- Prefer small, reviewable changes.
- A new rule should solve a named failure mode or recurring workflow problem.
- Avoid duplicating the same rule across many files; keep the canonical version in one protocol and reference it elsewhere.
- Do not add shell execution to `allowed-tools` in `SKILL.md` without explicit approval.
- Never commit credentials, tokens, private server addresses, private datasets, or user-identifying secrets.
- Keep examples generic; do not leak private project data into this public repository.

## Validation

After editing skill contracts/templates, run the standard-library-only linters in `.github/skills/research-os/scripts/` against representative templates. If you cannot run them, inspect required headings manually and state that validation was not executed.

## Versioning

Behavioral changes should update `CHANGELOG.md`. Major changes to the core workflow should increment the documented version in `README.md` and `SKILL.md` together.
