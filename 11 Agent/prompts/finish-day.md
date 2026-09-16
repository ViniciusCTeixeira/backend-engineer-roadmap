# Finish Day

## Purpose

Record completed work, evidence, errors, metrics, and new reviews after a study session.

## Preconditions

Today's session has finished.

## Files the agent must read

- `AGENTS.md`
- `today's private plan`
- `today's assessment/progress records`
- `docs/adaptive-learning.md`
- `docs/assessments.md`

## Files it may write

- `.study/progress/`
- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/reviews/queue.yaml`
- `.study/errors/`

## Files it must not alter

- `raw submitted attempts`
- `public curriculum`

## Ready-to-copy prompt

```text
Review today's completed study session and update only private learner state.

1. Preserve all raw attempts exactly.
2. Record actual time and completed/pending tasks.
3. Update current aggregates from evidence; do not invent scores.
4. Classify new errors using the approved schema.
5. Create D+1/D+7/D+30 review events as required by error type.
6. Detect confidence mismatch and possible AI-dependence.
7. Update future priorities only.
8. Do not change public curriculum.
9. Do not mark passive rereading as a completed review.
10. Show every file you changed and summarize why.

Do not commit unless explicitly requested.
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
