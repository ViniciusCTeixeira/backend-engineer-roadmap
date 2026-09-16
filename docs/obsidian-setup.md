# Obsidian Setup

## Goal

Use the repository as one Obsidian vault while keeping public curriculum, private learner state, and personal Obsidian preferences separate.

## 1. Open the repository as a vault

Clone the repository normally, then in Obsidian choose **Open folder as vault** and select the repository root.

The first public page to open is:

```text
00 Dashboard/Dashboard.md
```

## 2. Core study requires no community plugin

The roadmap is designed to work with standard Markdown.

Dataview and Tasks are optional convenience layers.

## 3. What the repository versions from `.obsidian/`

The repository intentionally versions only:

```text
.obsidian/templates.json
```

Its purpose is to point Obsidian's Templates feature to:

```text
90 Templates
```

All other Obsidian state is local and ignored by Git.

This includes, for example:

```text
app.json
appearance.json
core-plugins.json
workspace.json
workspace-mobile.json
community plugin configuration
future Obsidian-generated settings
```

This prevents simply opening/using the vault from creating unrelated public Git changes.

## 4. Templates core plugin

The Obsidian **Templates** core plugin is recommended if you want to insert templates interactively.

Enable it locally in Obsidian if desired.

The roadmap does not version your `core-plugins.json`, so one learner's enabled plugins do not become global repository policy.

Even without the Templates plugin, public template Markdown files can still be copied/used manually or by an agent.

## 5. Initialize private learner state

From the repository root, run:

```text
11 Agent/prompts/initialize-study.md
```

The workflow creates or validates:

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

## 6. Open the private dashboard

After initialization, open:

```text
.study/dashboard.md
```

If it does not exist, rerun/validate `initialize-study`.

## 7. Canonical state vs dashboard

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

The dashboard is only a derived presentation layer.

Refresh it with:

```text
11 Agent/prompts/sync-dashboard.md
```

Never repair a dashboard mismatch by rewriting historical evidence.

## 8. Clean clone behavior

Without `.study/`, a learner can still:

- use `00 Dashboard/Dashboard.md`;
- read curriculum;
- inspect Week 0;
- inspect projects/resources;
- read agent commands.

No community plugin query is required.

## 9. Optional Dataview

Dataview may be installed manually for richer note queries.

Example after private state exists:

```dataview
TABLE date, week, actual_minutes
FROM ".study/progress/daily"
SORT date DESC
LIMIT 7
```

This is optional convenience only and does not become canonical data.

## 10. Optional Tasks

Tasks may be installed manually for interactive Markdown task views.

Do not make completion depend on Tasks metadata. Canonical progress remains in the roadmap's private schemas.

## 11. Local Obsidian state and Git

The repository uses:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

Therefore normal Obsidian-generated settings remain local.

If local state was previously tracked, remove it from the Git index without deleting local files:

```bash
git rm --cached --ignore-unmatch \
  .obsidian/app.json \
  .obsidian/appearance.json \
  .obsidian/core-plugins.json \
  .obsidian/workspace.json \
  .obsidian/workspace-mobile.json
```

## 12. Public/private safety check

Before public commits:

```bash
git status
git check-ignore .study
git ls-files .obsidian
```

Expected tracked Obsidian configuration:

```text
.obsidian/templates.json
```

If learner-specific values or local workspace state appear in a public diff, remove them before committing.
