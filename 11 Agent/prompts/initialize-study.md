# Initialize Study

## Purpose

Initialize or validate the private learner repository and prepare Week 0 without modifying public curriculum.

## Preconditions

Run from repository root. `.study/` may be absent or already initialized.

## Files the agent must read

- `AGENTS.md`
- `docs/design/week-0-diagnostic-design.md`
- `docs/design/data-schemas.md`
- `01 Curriculum/00 - Week 0 Diagnostic/README.md`

## Files it may write

- `.study/ only`

## Files it must not alter

- `public curriculum`
- `historical private evidence if `.study/` already exists`

## Ready-to-copy prompt

```text
Read AGENTS.md and the Week 0/schema documentation.

Initialize or validate my private `.study/` learner state.

Requirements:
1. Keep all learner-specific data under `.study/`.
2. Do not edit public curriculum.
3. If `.study/` does not exist, create the documented private structure and initialize it as an independent Git repository only after showing me the intended structure.
4. Create/validate profile, state, metrics, current-plan, review queue, progress, assessment, error, project, career, agent, and archive locations.
5. Use schema_version 1.
6. Prepare Week 0 as the next action; do not answer diagnostic questions.
7. Report any missing required public files.
8. Do not commit unless I explicitly request it.

Finish with a validation summary and the command/prompt I should use to start Week 0.
```

## Expected output

A concise execution report containing:
- evidence/input used;
- files created/changed;
- decisions/adaptations made;
- validation performed;
- unresolved human decisions.

## Validation checklist

- [ ] Root and scoped agent rules were followed.
- [ ] Public/private boundary was preserved.
- [ ] Historical evidence was preserved.
- [ ] Assessment integrity was preserved where applicable.
- [ ] No unrelated files changed.
- [ ] Workload/technology-depth rules were respected when applicable.
- [ ] Final diff/state was reviewed.
- [ ] No commit was created unless explicitly requested.

## Codex notes

Codex reads applicable `AGENTS.md` files by directory scope. Run this recipe from the repository root unless the recipe explicitly requires another working directory.

## Claude Code notes

Claude Code loads the root `CLAUDE.md`, which imports `AGENTS.md`. Confirm project memory/rules are loaded when setting up Claude Code for the first time.
