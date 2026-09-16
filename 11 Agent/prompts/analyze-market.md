# Analyze Market

## Purpose

Aggregate multiple job records into recurring market signals and possible public proposals.

## Preconditions

A meaningful sample of private job analyses exists.

## Files the agent must read

- `AGENTS.md`
- `07 Career/AGENTS.md`
- `.study/career/jobs/`
- `.study/career/market-signals/`
- `public target role`

## Files it may write

- `.study/career/market-signals/`
- `proposal draft/suggestion when justified`

## Files it must not alter

- `automatic public curriculum edits`
- `private employer details in public proposal`

## Ready-to-copy prompt

```text
Analyze my collected relevant job records as a market sample.

Report:
- sample size and date window;
- recurring role titles;
- recurring required/preferred technologies;
- engineering-practice signals;
- English/international signals;
- gaps between market demand and my demonstrated evidence.

Separate weak from strong signals.

If a recurring signal plausibly justifies a public roadmap change, create an anonymized proposal draft with workload/trade-offs. Do not edit the public curriculum automatically.
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
