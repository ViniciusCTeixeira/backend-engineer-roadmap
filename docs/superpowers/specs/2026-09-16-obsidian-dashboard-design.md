# Obsidian Dashboard Design

**Status:** Approved for implementation  
**Approved:** 2026-09-16

## Goal

Provide a clean Obsidian-first interface for the roadmap without making Obsidian plugins or dashboard notes the source of truth.

## Design decision

Use a **plugin-optional** model:

1. public Markdown dashboard works in a clean clone;
2. learner-specific dashboard lives only under `.study/`;
3. canonical learner state remains in private schema files;
4. Dataview/Tasks may enhance the experience but are never required for core study;
5. no custom web application is introduced.

## Architecture

```text
public curriculum / templates / docs
                │
                │ initialize-study
                ▼
          private .study/
          ├── state.yaml
          ├── metrics.yaml
          ├── current-plan.md
          ├── reviews/queue.yaml
          ├── progress/
          ├── career/
          └── dashboard.md
                ▲
                │ sync-dashboard
                │
          derived view only
```

The dashboard is never canonical storage.

## Public dashboard

`00 Dashboard/Dashboard.md` is a safe landing page for a fresh clone.

It contains:

- start/setup links;
- Week 0 link;
- current public curriculum entry points;
- projects/resources/agent/career links;
- instructions for opening the private dashboard after initialization.

It contains no learner-specific values and no live query that fails when `.study/` does not exist.

## Private dashboard

`90 Templates/private-dashboard.md` is copied/generated to `.study/dashboard.md` by `initialize-study`.

It displays only values supported by canonical private records:

- current week/phase;
- today's work;
- due/overdue reviews;
- active gaps;
- skill evidence;
- SOLO/HYBRID/AI-ASSISTED comparison;
- weekly hours;
- assessment trend;
- Project A/Project B status;
- English progress;
- career funnel when active.

When a source value is absent, the dashboard must state `Not available yet` rather than invent data.

## Templates

Add:

- `90 Templates/private-dashboard.md`
- `90 Templates/daily-progress.md`
- `90 Templates/weekly-retrospective.md`

The templates contain reusable placeholders only and no personal data.

## Obsidian configuration

Commit only portable settings:

- `.obsidian/app.json`
- `.obsidian/core-plugins.json`
- `.obsidian/templates.json`

Do not commit a workspace layout because panes/open files are personal.

No community plugin is required or automatically installed.

## Core-plugin baseline

Enable a conservative set of long-standing core features used by the roadmap:

- File explorer
- Search
- Quick switcher
- Backlinks
- Outgoing links
- Templates
- Command palette
- Outline
- File recovery

The roadmap remains readable even if a learner changes these settings.

## Optional enhancements

Dataview and Tasks may be installed manually.

If installed, they may provide dynamic views over private notes, but:

- their queries are optional;
- canonical state remains `.study/*.yaml` and historical records;
- the public dashboard must not depend on them;
- community plugin failure must not block study.

## Agent integration

### `initialize-study`

Must:

- read the private-dashboard template;
- create/validate `.study/dashboard.md`;
- never overwrite existing learner content unnecessarily;
- create the canonical private structure first;
- finish by pointing the learner to the private dashboard and Week 0.

### `sync-dashboard`

Must:

- read canonical private state;
- update `.study/dashboard.md` only as a derived view;
- never mutate raw assessments/errors/interview history merely to update the dashboard;
- never invent unavailable values.

## Clean-clone behavior

Without `.study/`:

- `00 Dashboard/Dashboard.md` remains useful;
- no query errors appear;
- setup instructions point to `initialize-study`;
- Week 0 remains accessible.

## Public/private boundary

Public repository may contain:

- dashboard structure;
- placeholders;
- synthetic examples;
- Obsidian setup documentation.

Public repository must not contain:

- actual learner scores;
- real review backlog;
- career funnel values;
- personal gap lists;
- interview/application information.

## Acceptance criteria

- public dashboard works before private initialization;
- private dashboard is a derived view;
- no community plugin is mandatory;
- template directory is configured;
- `initialize-study` creates/validates `.study/dashboard.md`;
- `sync-dashboard` has explicit read/write boundaries;
- no workspace-specific layout is committed;
- all learner-specific information remains private.
