# Obsidian Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a plugin-optional Obsidian interface with a safe public landing page and a derived private learner dashboard.

**Architecture:** Public Markdown files provide navigation and setup without requiring `.study/`. Learner state remains canonical under `.study/`, while `.study/dashboard.md` is generated from a public template and refreshed by agent recipes. Minimal portable Obsidian settings configure core navigation/templates only.

**Tech Stack:** Markdown, YAML/frontmatter, Obsidian core plugins, Git, existing `.study/` schemas and agent recipes.

**Spec:** `docs/superpowers/specs/2026-09-16-obsidian-dashboard-design.md`

## Global Constraints

- Obsidian is the human interface; no custom web application.
- `.study/` remains private, ignored, and independently versioned.
- Dashboard content is derived and never canonical.
- No community plugin is required.
- No learner-specific value may be committed publicly.
- Missing private data is displayed as unavailable rather than inferred.
- Historical evidence remains immutable.
- Existing C1–C6 curriculum/scoring/adaptation rules are unchanged.

---

### Task 1: Add the public clean-clone dashboard

**Files:**
- Create: `00 Dashboard/README.md`
- Create: `00 Dashboard/Dashboard.md`

**Interfaces:**
- Consumes: public curriculum, projects, resources, career docs, agent recipes.
- Produces: stable public landing page usable before `.study/` exists.

- [ ] **Step 1: Create dashboard directory documentation**

Create `00 Dashboard/README.md` explaining public vs private dashboards and clean-clone behavior.

- [ ] **Step 2: Create the public dashboard**

Create `00 Dashboard/Dashboard.md` with links to setup, Week 0, curriculum, projects, resources, agent commands, and career track.

Do not include active Dataview/Tasks queries.

- [ ] **Step 3: Validate clean-clone assumptions**

Run:

```bash
grep -n "initialize-study" "00 Dashboard/Dashboard.md"
grep -n "Week 0" "00 Dashboard/Dashboard.md"
! grep -R '```dataview' "00 Dashboard"
```

Expected: first two commands return matches; no active Dataview query exists.

- [ ] **Step 4: Commit**

```bash
git add "00 Dashboard"
git commit -m "feat: add clean-clone obsidian dashboard"
```

---

### Task 2: Add private-state view/progress templates

**Files:**
- Create: `90 Templates/private-dashboard.md`
- Create: `90 Templates/daily-progress.md`
- Create: `90 Templates/weekly-retrospective.md`

**Interfaces:**
- Consumes: schemas from `docs/design/data-schemas.md`.
- Produces: public-safe reusable templates copied/generated into `.study/`.

- [ ] **Step 1: Create private dashboard template**

Include placeholders for current week, today's work, reviews, gaps, mode evidence, projects, English, assessment trend, weekly hours, and career funnel.

Every section names its canonical source file.

- [ ] **Step 2: Create daily-progress template**

Use `type: daily-progress`, `schema_version: 1`, ISO-date placeholder, planned/actual minutes, task IDs, completed task IDs, and private notes.

- [ ] **Step 3: Create weekly-retrospective template**

Include planned-vs-actual hours, assessment/mode evidence, reviews, recurring errors, project/English/career state, adaptations, and deferred work.

- [ ] **Step 4: Validate no personal values are embedded**

Run:

```bash
grep -R "{{" "90 Templates/private-dashboard.md" "90 Templates/daily-progress.md" "90 Templates/weekly-retrospective.md"
```

Expected: placeholder matches exist and no real learner data is present.

- [ ] **Step 5: Commit**

```bash
git add "90 Templates/private-dashboard.md" "90 Templates/daily-progress.md" "90 Templates/weekly-retrospective.md"
git commit -m "feat: add private study dashboard templates"
```

---

### Task 3: Add portable Obsidian configuration and setup docs

**Files:**
- Create: `.obsidian/app.json`
- Create: `.obsidian/core-plugins.json`
- Create: `.obsidian/templates.json`
- Create: `docs/obsidian-setup.md`

**Interfaces:**
- Consumes: `90 Templates/`.
- Produces: a usable vault configuration with no community-plugin requirement.

- [ ] **Step 1: Add minimal app settings**

Create valid JSON enabling readable lines and inline titles only.

- [ ] **Step 2: Add conservative core-plugin list**

Enable File explorer, Search, Quick switcher, Backlinks, Outgoing links, Templates, Command palette, Outline, and File recovery.

- [ ] **Step 3: Configure templates folder**

Set the Obsidian Templates core plugin folder to `90 Templates`.

- [ ] **Step 4: Document setup and manual fallback**

`docs/obsidian-setup.md` must explain:
- open repository as vault;
- community plugins are optional;
- run `initialize-study`;
- open `.study/dashboard.md`;
- public files remain read-only baseline during personal adaptation;
- Dataview/Tasks are optional enhancements.

- [ ] **Step 5: Validate JSON**

Run:

```bash
python -m json.tool .obsidian/app.json >/dev/null
python -m json.tool .obsidian/core-plugins.json >/dev/null
python -m json.tool .obsidian/templates.json >/dev/null
```

Expected: all three commands exit zero.

- [ ] **Step 6: Commit**

```bash
git add .obsidian docs/obsidian-setup.md
git commit -m "feat: configure portable obsidian vault"
```

---

### Task 4: Integrate agent recipes

**Files:**
- Modify: `11 Agent/prompts/initialize-study.md`
- Modify: `11 Agent/prompts/sync-dashboard.md`

**Interfaces:**
- Consumes: `90 Templates/private-dashboard.md`, canonical private state.
- Produces: `.study/dashboard.md` creation and synchronization behavior.

- [ ] **Step 1: Update initialize-study**

Require reading the dashboard template/setup docs and creating/validating `.study/dashboard.md` after canonical private state exists.

- [ ] **Step 2: Update sync-dashboard**

Specify exact canonical input files and `.study/dashboard.md` as the derived output.

Missing values must display `Not available yet`.

- [ ] **Step 3: Validate write boundaries**

Run:

```bash
grep -n ".study/dashboard.md" "11 Agent/prompts/initialize-study.md"
grep -n ".study/dashboard.md" "11 Agent/prompts/sync-dashboard.md"
grep -n "derived" "11 Agent/prompts/sync-dashboard.md"
```

Expected: all commands return matches.

- [ ] **Step 4: Commit**

```bash
git add "11 Agent/prompts/initialize-study.md" "11 Agent/prompts/sync-dashboard.md"
git commit -m "feat: integrate private dashboard agent workflow"
```

---

### Task 5: Validate Task 11

**Files:**
- Create: `docs/validation/task11-obsidian-dashboard-review.md`

**Interfaces:**
- Consumes: all Task 11 artifacts.
- Produces: recorded evidence that the dashboard is safe in clean-clone and initialized states.

- [ ] **Step 1: Record clean-clone tabletop**

Verify public dashboard works when `.study/` is absent.

- [ ] **Step 2: Record initialized-state tabletop**

Verify `initialize-study` creates private dashboard and `sync-dashboard` reads canonical state but only writes the derived dashboard.

- [ ] **Step 3: Record plugin-failure tabletop**

Verify absence of Dataview/Tasks does not block public or private Markdown dashboards.

- [ ] **Step 4: Run final diff checks**

```bash
git diff --check
git status --short
```

Expected: no whitespace errors and only Task 11 files are changed.

- [ ] **Step 5: Commit**

```bash
git add docs/validation/task11-obsidian-dashboard-review.md
git commit -m "docs: validate obsidian dashboard interface"
```
