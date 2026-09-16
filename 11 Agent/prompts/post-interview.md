# Post Interview

## Purpose

Turn an interview outcome into private evidence and remediation while separating facts from interpretation.

## Preconditions

Interview has occurred.

## Files the agent must read

- `AGENTS.md`
- `07 Career/AGENTS.md`
- `learner interview notes`
- `existing private skill/error state`

## Files it may write

- `.study/career/interviews/`
- `.study/errors/`
- `.study/reviews/queue.yaml`
- `.study/current-plan.md`

## Files it must not alter

- `original interview notes`
- `public curriculum directly`
- `NDA content`

## Ready-to-copy prompt

```text
Create a post-interview retrospective.

Separate:
1. factual questions/tasks I remember;
2. what I answered/did;
3. direct interviewer feedback;
4. my interpretation;
5. inferred gaps with confidence level.

Classify gaps into technical knowledge, reasoning, coding, system design, communication/English, behavioral, or time management.

Preserve original notes.
Create private remediation/review tasks only where evidence supports them.
One interview does not automatically change public curriculum.
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
