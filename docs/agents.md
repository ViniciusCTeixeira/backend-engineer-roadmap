# Coding Agents in This Roadmap

**Last verified:** 2026-09-15

This repository uses one shared instruction system for Codex and Claude Code while preserving tool-specific bootstrap behavior.

## Canonical instructions

`AGENTS.md` is the canonical shared project policy.

The root file is intentionally a map, not an encyclopedia. Detailed rules live under `11 Agent/rules/`, `docs/`, and scoped `AGENTS.md` files.

## Codex

Codex supports `AGENTS.md` files with directory-tree scope. More deeply nested instructions apply to files under their subtree and take precedence over broader scoped instructions on conflicts.

Official references verified 2026-09-15:

- https://openai.com/index/introducing-codex/
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/

Operational consequence:

- keep the root instructions concise;
- put specialized rules close to the files they govern;
- require validation after changes.

## Claude Code

Claude Code uses `CLAUDE.md`. Current official documentation explicitly recommends importing an existing `AGENTS.md` when a repository already shares instructions with other coding agents.

The root `CLAUDE.md` therefore starts with:

```text
@AGENTS.md
```

Claude Code supports `@path/to/import` in `CLAUDE.md`.

Official reference verified 2026-09-15:

- https://code.claude.com/docs/en/memory

`CLAUDE.local.md` is intended for personal project-specific preferences and should remain uncommitted.

## Shared behavior

Both tools must obey:
- public/private separation;
- historical integrity;
- assessment integrity;
- adaptation rules;
- source-quality/freshness rules;
- scoped directory rules.

## Risk model

Instructions in Markdown are behavioral context, not a hard security boundary.

Use tool/runtime permission mechanisms when available to technically block risky actions. Repository rules still explicitly prohibit force-push, destructive history rewriting, secrets exposure, and historical-evidence deletion.

## How recipes work

Ready-to-copy recipes live under `11 Agent/prompts/`.

A recipe declares:
- preconditions;
- required reads;
- allowed writes;
- prohibited changes;
- prompt;
- expected output;
- validation.

The prompt recipes are designed to be portable between coding agents. Tool-specific notes appear only when needed.
