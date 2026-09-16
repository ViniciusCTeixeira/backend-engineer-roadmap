# Run Review

## Purpose

Conduct one due spaced review without turning it into passive rereading or leaking answers.

## Preconditions

A pending review event exists.

## Files the agent must read

- `AGENTS.md`
- `specific review event`
- `source error/assessment metadata but not hidden solution until needed`
- `docs/adaptive-learning.md`

## Files it may write

- `private review result`
- `review queue status`
- `follow-up review if needed`

## Files it must not alter

- `source raw attempt`
- `public curriculum`

## Ready-to-copy prompt

```text
Run the selected due review according to its interval and error type.

Do not show the answer before I respond.

D+1 should emphasize recall/explanation/minimal repair.
D+7 should emphasize reconstruction/application/variant work.
D+30 should emphasize diagnosis/transfer to a realistic new scenario.

After I submit:
- grade using the approved assessment principles;
- preserve my raw response;
- mark success only for active recall/application, not rereading;
- create follow-up if performance is below threshold;
- update only private review/current state.
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
