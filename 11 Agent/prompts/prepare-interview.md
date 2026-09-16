# Prepare Interview

## Purpose

Create targeted interview preparation from an upcoming role and demonstrated gaps.

## Preconditions

Upcoming interview/role context available.

## Files the agent must read

- `AGENTS.md`
- `07 Career/AGENTS.md`
- `private relevant job analysis`
- `recent assessment/error state`
- `public interview curriculum`

## Files it may write

- `private interview-prep plan/practice records`

## Files it must not alter

- `NDA/confidential interview banks`
- `public curriculum`

## Ready-to-copy prompt

```text
Prepare me for the upcoming interview using only legitimate role context and my demonstrated gaps.

Create a timeboxed plan covering the most relevant combination of:
- backend/PHP;
- SQL/data;
- HTTP/API/security;
- cloud/production;
- system design;
- coding;
- English communication;
- behavioral stories.

Prioritize weak, high-probability areas over broad cramming.
Mark mock sections SOLO.
Do not invent company-specific interview questions as facts.
Store only private preparation state.
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
