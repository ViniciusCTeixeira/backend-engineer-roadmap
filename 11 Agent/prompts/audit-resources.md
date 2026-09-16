# Audit Resources

## Purpose

Audit public learning resources for freshness, authority, breakage, and version relevance.

## Preconditions

Resource files exist; web/current docs access available for freshness claims.

## Files the agent must read

- `AGENTS.md`
- `11 Agent/rules/source-quality.md`
- `09 Resources/ relevant files`
- `curriculum topics using those resources`

## Files it may write

- `low-risk verified URL/metadata fixes`
- `proposal for major replacements`

## Files it must not alter

- `unverified freshness claims`
- `major resource replacement without proposal`

## Ready-to-copy prompt

```text
Audit the selected public resources.

For each resource verify:
- URL accessibility;
- source authority;
- free/freemium/paid label;
- last-verified date;
- version applicability;
- whether it still teaches the intended curriculum concept.

For fast-moving topics, use current official sources.

You may make objective low-risk URL/metadata corrections.
For replacing a major resource or changing curriculum scope, create a proposal instead.

Report checked resources, evidence, changes, and unresolved items.
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
