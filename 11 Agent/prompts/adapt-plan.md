# Adapt Plan

## Purpose

Apply the approved adaptation algorithm to future private planning.

## Preconditions

Private state/evidence exists.

## Files the agent must read

- `AGENTS.md`
- `docs/adaptive-learning.md`
- `docs/assessments.md`
- `private state/metrics/current plan/reviews/recent evidence`
- `public prerequisites`

## Files it may write

- `future `.study/` planning/state/review queue`

## Files it must not alter

- `public curriculum`
- `historical raw evidence`

## Ready-to-copy prompt

```text
Apply the approved adaptive-learning rules to my future private plan.

For each active skill:
- compute/inspect mode-specific evidence;
- determine demonstrated score/evidence confidence;
- check critical dimension floors;
- check repeated errors;
- check confidence mismatch;
- check AI-dependence.

Generate mandatory remediation/reviews, then merge them with the public curriculum.

If workload exceeds target, defer optional enrichment/professional exposure/nonessential supporting labs first.
Never exceed the ceiling silently.
If foundations cannot fit under the ceiling, propose private resequencing.

Show a before/after plan summary and evidence for each change.
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
