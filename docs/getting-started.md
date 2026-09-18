# Getting Started

This guide takes a clean clone to the first real study action without mixing public curriculum with private learner data.

## Prerequisites

Required:

- Git
- Python 3 for repository validation

Recommended:

- Obsidian
- a PHP development environment as required by the current week
- Codex or Claude Code if you want agent-assisted workflows

The roadmap remains usable without Obsidian or a coding agent because the source of truth is Markdown + Git.

## 1. Clone

```bash
git clone <your-fork-or-repository-url> backend-engineer-roadmap
cd backend-engineer-roadmap
```

Inspect:

```bash
git status
```

The public worktree should start clean.

## 2. Open the public dashboard

In Obsidian, open the repository root as a vault.

Start at:

```text
00 Dashboard/Dashboard.md
```

Without Obsidian, open the same file in any Markdown viewer/editor.

## 3. Understand the two-repository model

The public repository is reusable curriculum.

Your learner state belongs in:

```text
.study/
```

`.study/` is:

- ignored by the parent repository;
- an independent nested Git repository;
- not a submodule;
- private by default.

See `docs/private-progress.md`.

## 4. Initialize `.study/`

Open:

```text
11 Agent/prompts/initialize-study.md
```

Copy its `Ready-to-copy prompt`.

### Codex example

Run Codex from the repository root and give it the copied prompt.

The root `AGENTS.md` supplies persistent project rules. Applicable nested `AGENTS.md` files add scoped instructions.

Ask Codex to show the intended `.study/` structure before it creates/changes private state, exactly as required by the recipe.

### Claude Code example

Run Claude Code from the repository root and give it the same copied prompt.

The root `CLAUDE.md` imports `AGENTS.md`, so the shared repository rules stay canonical.

For both agents:

- only `.study/` may be written during initialization;
- do not ask the agent to solve Week 0 questions;
- inspect the resulting files and private Git status.

## 5. Verify private initialization

Expected high-level structure:

```text
.study/
├── profile.md
├── state.yaml
├── metrics.yaml
├── current-plan.md
├── dashboard.md
├── progress/
├── assessments/
├── reviews/
├── errors/
├── projects/
├── career/
├── agent/
└── archive/
```

Check the public parent ignores it:

```bash
git check-ignore .study
```

Then inspect the nested private repository:

```bash
git -C .study status
```

If you want remote backup, create a **private** remote/repository and configure it from inside `.study/`. Do not convert `.study/` into a public submodule.

## 6. Complete Week 0

Open:

```text
01 Curriculum/00 - Week 0 Diagnostic/README.md
```

Follow its daily schedule and declared modes.

Week 0 measures current evidence and produces private adaptation inputs. It is not an admission exam.

## 7. Start Week 1 / normal study

Useful recipes:

```text
11 Agent/prompts/start-week.md
11 Agent/prompts/start-day.md
11 Agent/prompts/finish-day.md
11 Agent/prompts/weekly-retrospective.md
```

You may follow the Markdown manually if you do not use an agent.

## 8. Daily loop

A normal study day is:

1. open the current public daily plan;
2. check due private reviews;
3. respect the declared mode;
4. study the primary source;
5. predict before experimenting;
6. implement/diagnose;
7. create the requested evidence;
8. complete the SOLO daily assessment;
9. record errors/reviews privately;
10. update private progress.

## 9. Public repository validation

When you intentionally edit the public roadmap:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
git status
```

The repository intentionally uses local-only validation and does not enable hosted GitHub Actions.

## 10. If something looks wrong

Do not repair public/private mismatches by moving personal data into the public tree.

Useful references:

- `docs/private-progress.md`
- `docs/obsidian-setup.md`
- `docs/study-methodology.md`
- `docs/agents.md`
- `AGENTS.md`
