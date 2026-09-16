# Propose Curriculum Improvement

## Purpose

Create a reviewable public improvement proposal while separating private learner gaps from generic curriculum issues.

## Preconditions

Potential generic curriculum problem identified.

## Files the agent must read

- `AGENTS.md`
- `01 Curriculum/AGENTS.md`
- `11 Agent/rules/public-private-boundary.md`
- `relevant curriculum`
- `generalized evidence`

## Files it may write

- `proposal file only`

## Files it must not alter

- `direct curriculum edit`
- `private identifying evidence`

## Ready-to-copy prompt

```text
Evaluate the suspected curriculum issue.

First separate:
A. learner-specific gap;
B. genuinely generic curriculum deficiency.

If only A exists, stop and recommend private adaptation.

If B is supported, create a curriculum proposal containing:
- problem;
- generalized evidence;
- why it is generic;
- proposed change;
- affected files/weeks;
- prerequisites;
- workload impact;
- technology-depth impact;
- alternatives considered;
- validation plan.

Do not implement the curriculum change.
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
