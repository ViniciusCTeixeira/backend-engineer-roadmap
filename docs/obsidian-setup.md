# Obsidian Setup

## Goal

Use the repository as one Obsidian vault while keeping public curriculum and private learner state separate.

## 1. Open the repository as a vault

Clone the repository normally, then in Obsidian choose **Open folder as vault** and select the repository root.

The first public page to open is:

```text
00 Dashboard/Dashboard.md
```

## 2. Core experience requires no community plugin

The committed `.obsidian/` configuration only enables portable core features used for navigation and templates.

The roadmap is designed to work with standard Markdown.

Community plugins are optional.

## 3. Templates

The Obsidian Templates core plugin is configured to use:

```text
90 Templates
```

Public templates contain placeholders and synthetic structure only.

Learner-specific instantiated notes belong under `.study/`.

## 4. Initialize private learner state

From the repository root, run the agent recipe:

```text
11 Agent/prompts/initialize-study.md
```

The workflow creates or validates the independent ignored private state, including:

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

`.study/dashboard.md` is created from `90 Templates/private-dashboard.md`.

## 5. Open the private dashboard

After initialization, use the Obsidian File explorer to open:

```text
.study/dashboard.md
```

If it does not exist, rerun/validate `initialize-study`.

## 6. Canonical state vs dashboard

Canonical private state includes:

```text
.study/state.yaml
.study/metrics.yaml
.study/current-plan.md
.study/reviews/queue.yaml
.study/progress/
.study/assessments/
.study/errors/
.study/career/
```

The dashboard is only a presentation layer.

To refresh it, use:

```text
11 Agent/prompts/sync-dashboard.md
```

Never repair a dashboard mismatch by rewriting historical evidence.

## 7. Clean clone behavior

A learner who has not created `.study/` can still:

- read the public dashboard;
- read all public curriculum;
- inspect Week 0;
- inspect projects/resources;
- read agent commands.

No Dataview or Tasks query is required, so a clean clone does not show plugin-query errors.

## 8. Optional Dataview

Dataview may be installed manually for richer note queries.

Example use after private state exists:

```dataview
TABLE date, week, actual_minutes
FROM ".study/progress/daily"
SORT date DESC
LIMIT 7
```

This is optional convenience only.

A Dataview query does not become canonical data.

## 9. Optional Tasks

The Tasks community plugin may be installed manually if a learner wants interactive task views over Markdown checkboxes.

Do not make completion depend on Tasks metadata. Canonical progress is still recorded using the roadmap's private schemas.

## 10. Workspace files

Personal workspace layout is intentionally not committed.

Open panes, recent files, local window state, and personal layout should remain learner-specific.

## 11. Public/private safety check

Before committing public repository changes:

```bash
git status
git check-ignore .study
```

`.study` should be ignored by the parent public repository.

If learner-specific values appear in a public diff, remove them before committing.
