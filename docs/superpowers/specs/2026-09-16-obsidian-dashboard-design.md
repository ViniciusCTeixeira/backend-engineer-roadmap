# Obsidian Dashboard Design

**Status:** Approved for implementation — amended after repository validation  
**Approved:** 2026-09-16  
**Amended:** 2026-09-16

## Goal

Provide a clean Obsidian-first interface for the roadmap without making Obsidian plugins, local vault state, or dashboard notes the source of truth.

## Design decision

Use a **plugin-optional** model:

1. public Markdown dashboard works in a clean clone;
2. learner-specific dashboard lives only under `.study/`;
3. canonical learner state remains in private schema files;
4. Dataview/Tasks may enhance the experience but are never required for core study;
5. no custom web application is introduced;
6. Obsidian-generated local state is not versioned.

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

Public reusable templates include:

- `90 Templates/private-dashboard.md`
- `90 Templates/daily-progress.md`
- `90 Templates/weekly-retrospective.md`

The templates contain reusable placeholders only and no personal data.

## Obsidian configuration

Repository validation showed that Obsidian rewrites local vault configuration while the vault is open. Therefore the public repository versions **only** the portable template-folder setting:

```text
.obsidian/templates.json
```

It configures:

```text
90 Templates
```

All other `.obsidian/` state is local and ignored by Git by default.

Examples of local state that must not be tracked:

```text
.obsidian/app.json
.obsidian/appearance.json
.obsidian/core-plugins.json
.obsidian/workspace.json
.obsidian/workspace-mobile.json
community-plugin state
future Obsidian-generated local configuration
```

The `.gitignore` policy is:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

This is intentional: future Obsidian-generated files are private/local by default unless a later reviewed design explicitly promotes one to portable repository configuration.

## Core-plugin behavior

The roadmap does not enforce a shared `core-plugins.json`.

Learners may enable/disable Obsidian core plugins according to local preference.

For convenient template insertion, the Obsidian **Templates** core plugin is recommended and should use `90 Templates`, but the roadmap's core learning workflow does not depend on that plugin being enabled.

## Optional enhancements

Dataview and Tasks may be installed manually.

If installed, they may provide dynamic views over private notes, but:

- their queries are optional;
- canonical state remains `.study/*.yaml` and historical records;
- the public dashboard must not depend on them;
- community plugin failure must not block study;
- plugin configuration remains local.

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
- Week 0 remains accessible;
- the repository does not require a particular personal Obsidian workspace/plugin selection.

## Public/private boundary

Public repository may contain:

- dashboard structure;
- placeholders;
- synthetic examples;
- Obsidian setup documentation;
- `.obsidian/templates.json`.

Public repository must not contain:

- actual learner scores;
- real review backlog;
- career funnel values;
- personal gap lists;
- interview/application information;
- personal Obsidian workspace/recent-file state.

## Acceptance criteria

- public dashboard works before private initialization;
- private dashboard is a derived view;
- no community plugin is mandatory;
- `90 Templates` folder configuration is portable;
- local Obsidian state is ignored;
- `initialize-study` creates/validates `.study/dashboard.md`;
- `sync-dashboard` has explicit read/write boundaries;
- no workspace-specific layout is committed;
- opening the vault does not create tracked Obsidian configuration noise;
- all learner-specific information remains private.
