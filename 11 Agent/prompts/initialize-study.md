# Initialize Study

## Purpose

Initialize or validate the private learner repository, create the derived private dashboard, and prepare Week 0 without modifying public curriculum.

## Preconditions

Run from repository root. `.study/` may be absent or already initialized.

## Files the agent must read

- `AGENTS.md`
- `docs/design/week-0-diagnostic-design.md`
- `docs/design/data-schemas.md`
- `docs/obsidian-setup.md`
- `90 Templates/private-dashboard.md`
- `01 Curriculum/00 - Week 0 Diagnostic/README.md`

## Files it may write

- `.study/ only`

## Files it must not alter

- `public curriculum`
- `historical private evidence if .study/ already exists`

## Ready-to-copy prompt

```text
Read AGENTS.md, the Week 0/schema documentation, Obsidian setup documentation, and the private-dashboard template.

Initialize or validate my private `.study/` learner state.

Requirements:
1. Keep all learner-specific data under `.study/`.
2. Do not edit public curriculum.
3. If `.study/` does not exist, show the intended structure, then create it and initialize it as an independent Git repository.
4. Create/validate profile, state, metrics, current-plan, review queue, progress, assessment, error, project, career, agent, and archive locations.
5. Use schema_version 1.
6. Create or validate `.study/dashboard.md` from `90 Templates/private-dashboard.md` only after canonical state files exist.
7. The dashboard is derived; never use dashboard values as a substitute for canonical state.
8. When a dashboard value has no source evidence, render `Not available yet` rather than inventing a value.
9. If `.study/dashboard.md` already exists, preserve learner-specific/custom content unless regeneration is clearly safe; report conflicts instead of overwriting blindly.
10. Prepare Week 0 as the next action; do not answer diagnostic questions.
11. Report any missing required public files.
12. Do not commit unless I explicitly request it.

Finish with:
- a validation summary;
- the path `.study/dashboard.md`;
- the command/prompt I should use to start Week 0.
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
- [ ] Canonical private state was created before the derived dashboard.
- [ ] `.study/dashboard.md` exists or an explicit conflict/blocker was reported.
- [ ] Missing dashboard data was not invented.
- [ ] Historical evidence was preserved.
- [ ] Assessment integrity was preserved where applicable.
- [ ] No unrelated public files changed.
- [ ] Final private-state diff/status was reviewed.
- [ ] No commit was created unless explicitly requested.

## Codex notes

Codex reads applicable `AGENTS.md` files by directory scope. Run this recipe from the repository root unless the recipe explicitly requires another working directory.

## Claude Code notes

Claude Code loads the root `CLAUDE.md`, which imports `AGENTS.md`. Confirm project memory/rules are loaded when setting up Claude Code for the first time.
