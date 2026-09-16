# Task 11 Validation — Obsidian Dashboard

**Date:** 2026-09-16  
**Status:** PASS — approved after Task 11.1 repository revalidation

## Scope

Validate the plugin-optional Obsidian interface without changing canonical schemas, scoring, adaptation rules, curriculum, or historical data.

## Clean-clone tabletop

Starting state:

```text
public repository exists
.study/ absent
community plugins absent
```

Expected:

- `00 Dashboard/Dashboard.md` opens normally;
- onboarding/setup/Week 0 links remain usable;
- no live Dataview/Tasks query produces an error;
- learner is told to run `initialize-study`.

Result: **PASS**

## Initialized-state tabletop

Expected:

- `initialize-study` creates/validates `.study/dashboard.md` from public template;
- canonical state is created before derived dashboard;
- existing learner dashboard content is not blindly overwritten;
- missing values render `Not available yet`.

Result: **PASS**

## Dashboard synchronization tabletop

Expected:

- `sync-dashboard` reads canonical private state;
- writes only `.study/dashboard.md`;
- does not alter raw assessments, historical errors, metrics, current plan, review queue, or public files;
- does not invent unavailable values.

Result: **PASS**

## Community-plugin failure tabletop

Starting state:

```text
Dataview absent
Tasks absent
```

Expected:

- public dashboard remains normal Markdown;
- private dashboard remains normal Markdown;
- core study workflow remains available.

Result: **PASS**

## Open-vault Git-noise regression

The first Task 11 implementation revealed that Obsidian generated or rewrote local vault files such as:

- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/core-plugins.json`
- `.obsidian/workspace.json`

Task 11.1 corrected the repository rule to:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

Repository revalidation on `master` after commit:

```text
d2a06d58354f45853cc64e4ee12e80394170b318
fix: keep obsidian local state out of git
```

confirmed:

- local Obsidian files were removed from repository tracking;
- `.obsidian/templates.json` is the only public Obsidian configuration file;
- `.gitignore` keeps future `.obsidian/*` state local by default.

Result after correction: **PASS**

## Portable configuration

The sole tracked Obsidian configuration is:

```text
.obsidian/templates.json
```

with:

```json
{
  "folder": "90 Templates"
}
```

No shared `core-plugins.json` is required. The Templates core plugin is recommended locally, not enforced globally.

Result: **PASS**

## Public/private boundary

- public dashboard contains navigation only: PASS
- private-dashboard template contains placeholders only: PASS
- learner values remain under `.study/`: PASS
- dashboard explicitly marked derived: PASS
- workspace/recent-file state is not public: PASS
- future Obsidian-local state is ignored by default: PASS

## Repository evidence

GitHub `master` was revalidated after Task 11.1:

```text
.obsidian/
└── templates.json
```

The parent `.gitignore` contains:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

## Conclusion

**Task 11 is approved.**

The Obsidian interface is plugin-optional, clean-clone safe, keeps learner state private, treats the dashboard as a derived view, and no longer tracks volatile workspace/plugin/preference state.
