# Start Week

## Purpose

Build the learner's private weekly plan from the public matrix and accumulated evidence.

## Preconditions

Private state exists and current week is known.

## Files the agent must read

- `AGENTS.md`
- `.study state/metrics/reviews`
- `public year matrix`
- `current week curriculum`
- `recent assessments/errors`

## Files it may write

- `.study/current-plan.md`
- `future private review/remediation scheduling`

## Files it must not alter

- `public matrix`
- `history`

## Ready-to-copy prompt

```text
Prepare my next study week.

Merge:
- the approved public curriculum week;
- overdue/due reviews;
- active gaps/recovery blocks;
- project milestones;
- English;
- AI/agent practice;
- career actions.

Use the adaptation priority rules.
Keep the normal target within my configured hours and never exceed the ceiling silently.
If foundational recovery cannot fit, propose a private resequencing instead of overbooking.

Return a day-by-day private plan with modes, estimated minutes, deliverables, reviews, and the reason for every adaptation from the public baseline.
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
