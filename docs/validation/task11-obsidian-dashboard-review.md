# Task 11 Validation — Obsidian Dashboard

**Date:** 2026-09-16  
**Status:** Requires Task 11.1 repository correction, then revalidation

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

Repository validation after the first Task 11 implementation showed that Obsidian generated or rewrote:

- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/core-plugins.json`
- `.obsidian/workspace.json`

This invalidated the earlier assumption that these files were suitable shared configuration.

Task 11.1 changes the rule:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

Expected after correction:

- opening/using Obsidian may modify local files;
- those files remain ignored;
- no workspace/recent-file state enters Git;
- only `.obsidian/templates.json` is tracked.

Result before correction: **FAIL — regression discovered**

Result after applying Task 11.1 must be confirmed from GitHub before Task 11 is approved.

## Portable configuration

Only this file is repository configuration:

```text
.obsidian/templates.json
```

Expected content:

```json
{
  "folder": "90 Templates"
}
```

No shared `core-plugins.json` is required. Templates core plugin is recommended locally, not enforced globally.

## Public/private boundary

- public dashboard contains navigation only: PASS
- private-dashboard template contains placeholders only: PASS
- learner values remain under `.study/`: PASS
- dashboard explicitly marked derived: PASS
- workspace/recent-file state must not be public: pending repository correction

## Post-correction commands

```bash
python -m json.tool .obsidian/templates.json >/dev/null
git check-ignore .obsidian/workspace.json
git check-ignore .obsidian/core-plugins.json
git check-ignore .obsidian/app.json
git check-ignore .obsidian/appearance.json
git ls-files .obsidian
git diff --check
```

Expected:

```text
.obsidian/templates.json
```

is the only output from `git ls-files .obsidian`.

## Conclusion

Task 11 is approved only after the Task 11.1 correction is committed, pushed, and the repository confirms that `.obsidian/templates.json` is the sole tracked Obsidian configuration file.
