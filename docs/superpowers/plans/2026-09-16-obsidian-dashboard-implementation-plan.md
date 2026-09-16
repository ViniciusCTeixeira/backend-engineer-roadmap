# Obsidian Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a plugin-optional Obsidian interface with a safe public landing page and a derived private learner dashboard while preventing local Obsidian state from polluting Git history.

**Architecture:** Public Markdown files provide navigation and setup without requiring `.study/`. Learner state remains canonical under `.study/`, while `.study/dashboard.md` is generated from a public template and refreshed by agent recipes. Only `.obsidian/templates.json` is portable/versioned; all other Obsidian-generated state remains local.

**Tech Stack:** Markdown, YAML/frontmatter, Obsidian, Git, existing `.study/` schemas and agent recipes.

**Spec:** `docs/superpowers/specs/2026-09-16-obsidian-dashboard-design.md`

## Global Constraints

- Obsidian is the human interface; no custom web application.
- `.study/` remains private, ignored, and independently versioned.
- Dashboard content is derived and never canonical.
- No community plugin is required.
- No learner-specific value may be committed publicly.
- Missing private data is displayed as unavailable rather than inferred.
- Historical evidence remains immutable.
- Only `.obsidian/templates.json` is portable repository configuration.
- All other `.obsidian/` local state is ignored.
- Existing C1–C6 curriculum/scoring/adaptation rules are unchanged.

---

### Task 1: Add the public clean-clone dashboard

**Files:**
- Create: `00 Dashboard/README.md`
- Create: `00 Dashboard/Dashboard.md`

**Interfaces:**
- Consumes: public curriculum, projects, resources, career docs, agent recipes.
- Produces: stable public landing page usable before `.study/` exists.

- [x] **Step 1: Create dashboard directory documentation**
- [x] **Step 2: Create the public dashboard**
- [x] **Step 3: Validate no mandatory Dataview/Tasks query**
- [x] **Step 4: Commit**

---

### Task 2: Add private-state view/progress templates

**Files:**
- Create: `90 Templates/private-dashboard.md`
- Create: `90 Templates/daily-progress.md`
- Create: `90 Templates/weekly-retrospective.md`

**Interfaces:**
- Consumes: schemas from `docs/design/data-schemas.md`.
- Produces: public-safe reusable templates copied/generated into `.study/`.

- [x] **Step 1: Create private dashboard template**
- [x] **Step 2: Create daily-progress template**
- [x] **Step 3: Create weekly-retrospective template**
- [x] **Step 4: Validate no personal values are embedded**
- [x] **Step 5: Commit**

---

### Task 3: Keep only portable Obsidian configuration

**Files:**
- Modify: `.gitignore`
- Create/keep: `.obsidian/templates.json`
- Remove from Git tracking: `.obsidian/app.json`
- Remove from Git tracking: `.obsidian/appearance.json`
- Remove from Git tracking: `.obsidian/core-plugins.json`
- Remove from Git tracking: `.obsidian/workspace.json`
- Ignore any future `.obsidian/*` except `templates.json`
- Modify: `docs/obsidian-setup.md`

**Interfaces:**
- Consumes: `90 Templates/`.
- Produces: portable template-folder configuration without sharing personal/local Obsidian state.

- [ ] **Step 1: Add allowlist-style ignore rule**

Use:

```gitignore
.obsidian/*
!.obsidian/templates.json
```

This makes future Obsidian state local by default.

- [ ] **Step 2: Untrack existing local files without deleting them locally**

Run:

```bash
git rm --cached --ignore-unmatch \
  .obsidian/app.json \
  .obsidian/appearance.json \
  .obsidian/core-plugins.json \
  .obsidian/workspace.json \
  .obsidian/workspace-mobile.json
```

Expected: tracked copies are staged for deletion; local files remain on disk.

- [ ] **Step 3: Add portable template-folder configuration**

`.obsidian/templates.json` must contain:

```json
{
  "folder": "90 Templates"
}
```

- [ ] **Step 4: Document local-plugin behavior**

`docs/obsidian-setup.md` must explain:
- only `templates.json` is shared;
- Templates core plugin is recommended but not required;
- all other Obsidian preferences/plugin/workspace state remains local;
- opening the vault should not create public Git noise.

- [ ] **Step 5: Validate ignore behavior**

Run:

```bash
git check-ignore .obsidian/workspace.json
git check-ignore .obsidian/core-plugins.json
git check-ignore .obsidian/app.json
git check-ignore .obsidian/appearance.json
git check-ignore -v .obsidian/templates.json || true
git ls-files .obsidian
```

Expected:
- local files are ignored;
- `templates.json` is not ignored and is the only tracked `.obsidian` file.

- [ ] **Step 6: Validate JSON**

Run:

```bash
python -m json.tool .obsidian/templates.json >/dev/null
```

Expected: exit zero.

- [ ] **Step 7: Commit**

```bash
git add .gitignore .obsidian/templates.json docs/obsidian-setup.md
git add -u .obsidian
git commit -m "fix: keep obsidian local state out of git"
```

---

### Task 4: Integrate agent recipes

**Files:**
- Modify: `11 Agent/prompts/initialize-study.md`
- Modify: `11 Agent/prompts/sync-dashboard.md`

**Interfaces:**
- Consumes: `90 Templates/private-dashboard.md`, canonical private state.
- Produces: `.study/dashboard.md` creation and synchronization behavior.

- [x] **Step 1: Update initialize-study**
- [x] **Step 2: Update sync-dashboard**
- [x] **Step 3: Validate write boundaries**
- [x] **Step 4: Commit**

---

### Task 5: Validate Task 11

**Files:**
- Modify: `docs/validation/task11-obsidian-dashboard-review.md`

**Interfaces:**
- Consumes: all Task 11 artifacts.
- Produces: recorded evidence that the dashboard is safe in clean-clone, initialized, and actively-used Obsidian states.

- [ ] **Step 1: Record clean-clone tabletop**
- [ ] **Step 2: Record initialized-state tabletop**
- [ ] **Step 3: Record plugin-failure tabletop**
- [ ] **Step 4: Record open-vault Git-noise regression check**
- [ ] **Step 5: Confirm only `templates.json` is tracked under `.obsidian/`**
- [ ] **Step 6: Run final diff checks**

```bash
git diff --check
git status --short
git ls-files .obsidian
```

Expected:
- no whitespace errors;
- Task 11 correction only;
- `.obsidian/templates.json` is the only tracked Obsidian configuration file.

- [ ] **Step 7: Commit**

```bash
git add docs/validation/task11-obsidian-dashboard-review.md
git commit -m "docs: validate portable obsidian configuration"
```
