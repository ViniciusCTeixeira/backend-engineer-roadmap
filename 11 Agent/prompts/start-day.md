# Start Day

## Purpose

Prepare today's study work from the public curriculum plus the learner's private state.

## Preconditions

Private state initialized.

## Files the agent must read

- `AGENTS.md`
- `.study/profile.md`
- `.study/state.yaml`
- `.study/metrics.yaml`
- `.study/current-plan.md`
- `.study/reviews/queue.yaml`
- `current public week`

## Files it may write

- `.study/current-plan.md`
- `future/pending private planning only`

## Files it must not alter

- `historical attempts/scores`
- `public curriculum`

## Ready-to-copy prompt

```text
Read AGENTS.md, my private current state, pending reviews, current public curriculum week, and today's private plan.

Prepare today's study session.

Return:
1. due/overdue reviews first;
2. today's core outcome;
3. supporting/industry-platform work if scheduled;
4. English task;
5. AI/agent task;
6. project task;
7. career action if active;
8. estimated time by item and total;
9. mode (SOLO/HYBRID/AI-ASSISTED) for each task;
10. concrete deliverables.

Respect my weekly workload target/ceiling.
Do not reveal assessment answers.
Do not rewrite historical records.
If remediation conflicts with optional work, defer optional/exposure work first.
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
