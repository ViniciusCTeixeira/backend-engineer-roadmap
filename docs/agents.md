# Coding Agents in This Roadmap

**Last verified:** 2026-09-17

This repository uses one shared instruction system for Codex and Claude Code while preserving tool-specific bootstrap behavior.

## Canonical repository instructions

`AGENTS.md` is the shared canonical project policy.

It is intentionally a map to deeper sources of truth rather than a giant prompt.

Scoped `AGENTS.md` files may add instructions for specific subtrees.

## Codex

Codex can use repository `AGENTS.md` instructions and applicable nested instructions to guide work in the codebase.

Official references verified 2026-09-17:

- https://openai.com/codex/
- https://openai.com/index/introducing-codex/
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/

Repository usage example:

1. start Codex from the repository root;
2. ask it to read the applicable `AGENTS.md`;
3. open a recipe such as `11 Agent/prompts/start-day.md`;
4. give the recipe's Ready-to-copy prompt;
5. inspect every consequential change/evidence;
6. run the required validation.

Do not bypass a `SOLO` learning task by asking Codex to solve it.

## Claude Code

Claude Code loads project instructions from `CLAUDE.md`.

The repository root `CLAUDE.md` begins with:

```text
@AGENTS.md
```

so the shared policy remains canonical.

Claude Code documentation supports imports from `CLAUDE.md` and recommends keeping persistent project instructions concise.

Official references verified 2026-09-17:

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/claude-directory

Repository usage example:

1. start Claude Code from the repository root;
2. confirm project instructions are loaded;
3. open the relevant roadmap recipe;
4. provide the recipe prompt;
5. respect its allowed/prohibited writes;
6. inspect diff/state and run validation.

`CLAUDE.local.md` is ignored and may be used for personal local preferences.

## Shared study behavior

Both agents must respect:

- public/private separation;
- historical integrity;
- assessment integrity;
- SOLO/HYBRID/AI-ASSISTED modes;
- source freshness;
- scoped repository instructions;
- validation before claiming completion.

## Permission and risk model

Markdown instructions are behavioral policy, not a hard security boundary.

Use each tool's permission/sandbox mechanisms for stronger technical controls.

Never grant broad destructive access merely to make an exercise convenient.

For tool-calling, agents, or MCP tasks:

- keep tool schemas/capabilities narrow;
- validate arguments;
- make authorization application-owned;
- require explicit human approval for consequential side effects where appropriate;
- preserve logs/evidence needed to audit the result.

## Recipe catalog

Ready-to-copy workflows live under:

```text
11 Agent/prompts/
```

Common examples:

```text
initialize-study
start-week
start-day
finish-day
weekly-retrospective
review-errors
adapt-plan
review-project
analyze-job
prepare-interview
post-interview
sync-dashboard
```

The recipes are deliberately tool-agnostic where possible.

## Local validation

Agents modifying public repository files must run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
git status
```

This repository does not use hosted GitHub Actions for routine validation.
