# Dashboard

This directory is the **public, safe entry point** for the Obsidian vault.

Open `Dashboard.md` after cloning/opening the repository in Obsidian.

## Two dashboards, two responsibilities

### Public dashboard

`00 Dashboard/Dashboard.md`

Purpose:

- onboarding;
- navigation;
- public curriculum links;
- setup instructions.

It contains no learner-specific state and must work when `.study/` does not exist.

### Private learner dashboard

`.study/dashboard.md`

Purpose:

- current week/phase;
- today's work;
- review backlog;
- gaps;
- evidence by study mode;
- project progress;
- English progress;
- career funnel.

It is generated from `90 Templates/private-dashboard.md` after `initialize-study`.

## Canonical-state rule

The private dashboard is a **derived view**.

Canonical state remains in files such as:

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

Never treat a value typed only into the dashboard as canonical evidence.

## Plugins

No community plugin is required.

Dataview and Tasks may be installed later for convenience, but the roadmap must remain usable with standard Markdown and Obsidian core features.
