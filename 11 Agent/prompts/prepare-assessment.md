# Prepare Assessment

## Purpose

Start an assessment session while protecting answer-key integrity.

## Preconditions

Assessment definition exists.

## Files the agent must read

- `AGENTS.md`
- `assessment definition`
- `02 Daily Assessments/AGENTS.md`
- `docs/assessments.md`

## Files it may write

- `new private assessment attempt metadata/raw attempt as learner submits`

## Files it must not alter

- `answer key before submission/abandonment`
- `existing raw attempts`

## Ready-to-copy prompt

```text
Prepare the requested assessment.

1. State timebox, allowed tools, declared mode, skills, and deliverables.
2. Do not reveal the answer key, model solution, rubric secrets, or expected output that would solve the task.
3. In SOLO mode, do not help solve it.
4. In HYBRID mode, preserve my first SOLO attempt before assistance.
5. Only grade after I explicitly submit.
6. If I request help during SOLO, offer to mark the attempt abandoned before teaching the solution.

Start the assessment and wait for my answer.
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
