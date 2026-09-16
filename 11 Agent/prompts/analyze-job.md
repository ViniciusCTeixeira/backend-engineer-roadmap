# Analyze Job

## Purpose

Compare one vacancy to demonstrated learner state without changing public curriculum.

## Preconditions

Job description available and private learner state initialized.

## Files the agent must read

- `AGENTS.md`
- `07 Career/AGENTS.md`
- `job description`
- `private skill/project/career state`

## Files it may write

- `.study/career/jobs/`
- `private gap/current-plan suggestions`

## Files it must not alter

- `public curriculum`
- `fabricated employer claims`

## Ready-to-copy prompt

```text
Analyze this single job description against my demonstrated state.

Classify:
- demonstrated skills;
- skills in progress;
- missing skills;
- interview risks;
- employer-quality signals;
- requirements vs preferences;
- location/English/international exposure signals stated in the posting.

Create only private preparation actions.
This single vacancy must not alter the public curriculum or promote a technology globally.
Clearly separate facts from the posting from your inference.
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
