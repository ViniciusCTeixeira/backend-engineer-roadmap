# Weekly Retrospective

## Purpose

Analyze the prior week and adapt the next private week.

## Preconditions

Week has ended with at least progress evidence.

## Files the agent must read

- `AGENTS.md`
- `last 7 days private progress`
- `assessments`
- `errors`
- `reviews`
- `metrics`
- `project status`
- `career feedback if active`

## Files it may write

- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/current-plan.md`
- `.study/reviews/queue.yaml`
- `.study/agent/`

## Files it must not alter

- `historical evidence`
- `public curriculum directly`

## Ready-to-copy prompt

```text
Run my weekly retrospective.

Analyze:
- planned vs actual study time;
- completion;
- assessment performance by skill and mode;
- recurring errors;
- overdue reviews;
- SOLO vs HYBRID vs AI-ASSISTED gaps;
- confidence calibration;
- project progress;
- English evidence;
- career funnel/feedback when active.

Classify each important skill as maintenance, normal, reinforcement, or recovery.
Adapt only future private planning.
If you detect a possible generic curriculum problem, create a proposal suggestion; do not edit public curriculum.

End with:
1. wins backed by evidence;
2. top 3 gaps;
3. next-week adaptations;
4. deferred work;
5. any human decision needed.
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
