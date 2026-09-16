# Review Project

## Purpose

Review project code/artifacts against current curriculum goals without doing inappropriate learner work.

## Preconditions

A current project milestone and declared mode exist.

## Files the agent must read

- `AGENTS.md`
- `05 Projects/AGENTS.md`
- `current project milestone`
- `relevant current curriculum`
- `project files`

## Files it may write

- `project files only when mode permits`
- `.study private review/evidence if applicable`

## Files it must not alter

- `confidential code/data`
- `SOLO implementation for learner`

## Ready-to-copy prompt

```text
Review the current project milestone against the learning goals.

First identify its declared study mode.

Evaluate:
- correctness;
- architecture/trade-offs;
- tests/validation;
- database/query behavior where relevant;
- security;
- observability/operability;
- documentation;
- whether technologies were introduced before prerequisites.

For SOLO, provide review only after my submitted implementation.
For HYBRID, compare my first attempt with agent suggestions.
For AI-ASSISTED, you may propose/implement bounded changes, but require me to review and validate them.

Return evidence-backed findings ordered by severity and learning value.
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
