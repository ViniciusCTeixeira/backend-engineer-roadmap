# Review Errors

## Purpose

Aggregate recurring mistakes and create evidence-based remediation/review actions.

## Preconditions

Private error records exist.

## Files the agent must read

- `AGENTS.md`
- `.study/errors/`
- `.study/assessments/`
- `.study/reviews/queue.yaml`
- `docs/adaptive-learning.md`

## Files it may write

- `.study/errors/ append-only recurrence/resolution data`
- `.study/reviews/queue.yaml`
- `.study/current-plan.md`

## Files it must not alter

- `original error descriptions`
- `public curriculum`

## Ready-to-copy prompt

```text
Review my active error notebook.

1. Group only genuinely related errors.
2. Count recurrence across separate evidence events, not repeated mistakes inside one assessment.
3. Promote to high priority at three separate related events.
4. Identify prerequisite/recovery risks.
5. Create or adjust D+1/D+7/D+30 active-recall reviews.
6. Distinguish knowledge gaps, reasoning gaps, validation failures, English issues, and AI-dependence.
7. Preserve all original error entries.
8. Do not change public curriculum.

Return the active error map and remediation actions.
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
