# Sync Dashboard

## Purpose

Recompute learner-facing dashboard views from canonical private state without making the dashboard canonical.

## Preconditions

Private state exists; dashboard templates may exist.

## Files the agent must read

- `AGENTS.md`
- `.study state/metrics/current plan/reviews/project/career aggregates`
- `public dashboard template`

## Files it may write

- `derived private/dashboard view files as defined by implementation`

## Files it must not alter

- `raw historical evidence`
- `invented metrics`
- `public learner-specific data`

## Ready-to-copy prompt

```text
Synchronize the learner dashboard from canonical private state.

Display only values supported by source records:
- current week/phase;
- today's work;
- reviews due/overdue;
- skill progress/evidence confidence;
- SOLO vs HYBRID vs AI-ASSISTED;
- project milestones;
- English progress;
- active gaps;
- career funnel when active.

Do not invent missing metrics.
Do not move learner-specific values into committed public files.
The dashboard is a derived view; canonical data remains under `.study/`.
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
