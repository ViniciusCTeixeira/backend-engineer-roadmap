# Sync Dashboard

## Purpose

Recompute `.study/dashboard.md` from canonical private state without making the dashboard canonical.

## Preconditions

Private `.study/` state exists.

## Files the agent must read

When present:

- `AGENTS.md`
- `90 Templates/private-dashboard.md`
- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/current-plan.md`
- `.study/reviews/queue.yaml`
- recent `.study/progress/` aggregates/records needed for the view
- relevant `.study/projects/` progress
- relevant `.study/career/` aggregates

Historical assessments/errors may be read only when a current aggregate/source link needs verification.

## Files it may write

- `.study/dashboard.md` only

## Files it must not alter

- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/current-plan.md`
- `.study/reviews/queue.yaml`
- raw historical assessments
- original error entries
- interview/application history
- public files

If canonical state itself needs an update, use the appropriate study/adaptation workflow first; do not hide that mutation inside dashboard synchronization.

## Ready-to-copy prompt

```text
Synchronize `.study/dashboard.md` from canonical private state.

Read the private dashboard template and available canonical state.

Display only values supported by source records:
- current week/phase;
- weekly target/ceiling and current hours;
- today's work;
- reviews due/overdue/pending;
- active gaps and priorities;
- skill demonstrated scores/evidence confidence;
- SOLO vs HYBRID vs AI-ASSISTED evidence;
- confidence/AI-dependence flags when already supported by state;
- assessment trend;
- Project A/Project B progress;
- English evidence;
- career funnel/stage when active;
- next actions from the current plan.

Rules:
1. Write only `.study/dashboard.md`.
2. The dashboard is a derived view, not canonical storage.
3. Do not mutate metrics/state/plan/review queue merely to make the dashboard look complete.
4. Do not read private values into public files.
5. If a value is absent or cannot be derived reliably, show `Not available yet`.
6. Do not infer conceptual mastery from AI-assisted evidence alone.
7. Preserve the dashboard structure unless a public template change explicitly requires migration.
8. Report source files used and any stale/missing canonical data.

Finish with a short synchronization report.
```

## Expected output

A concise execution report containing:
- source files read;
- `.study/dashboard.md` updated;
- missing/stale values;
- validation performed;
- any separate state-update workflow that may be needed.

## Validation checklist

- [ ] Root agent rules were followed.
- [ ] Only `.study/dashboard.md` was written.
- [ ] Canonical state was not mutated.
- [ ] Historical evidence was not changed.
- [ ] Missing values use `Not available yet`.
- [ ] SOLO/HYBRID/AI-ASSISTED evidence remains distinguishable.
- [ ] No private data was written publicly.
- [ ] Dashboard remains a derived view.

## Codex notes

Codex reads applicable `AGENTS.md` files by directory scope. Run this recipe from the repository root.

## Claude Code notes

Claude Code loads the root `CLAUDE.md`, which imports `AGENTS.md`.
