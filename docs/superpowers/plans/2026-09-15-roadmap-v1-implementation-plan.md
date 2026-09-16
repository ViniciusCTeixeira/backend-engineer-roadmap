# Adaptive Backend Engineer Roadmap V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build V1 of a public, reusable, Obsidian-based adaptive 52-week Backend Engineer roadmap for experienced PHP developers, with a separately versioned private learner state and first-class Codex/Claude/AI-engineering workflows.

**Architecture:** The public repository contains curriculum, assessments, projects, resources, agent rules, templates, and documentation. Learner-specific data lives only in an ignored nested `.study/` Git repository. Public curriculum changes are reviewable and generic; personal adaptation changes future private planning while preserving immutable historical evidence.

**Tech Stack:** Markdown, YAML/frontmatter, Obsidian, Git/GitHub, Obsidian Tasks/Dataview where justified, shell/Python validation scripts only where static Markdown validation cannot reasonably be done manually, Codex-compatible `AGENTS.md`, Claude Code-compatible `CLAUDE.md`.

**Spec:** `docs/superpowers/specs/2026-09-15-adaptive-backend-roadmap-design.md`

## Global Constraints

- Public repository language is primarily English.
- V1 target profile is experienced PHP developer → Senior Backend Engineer / Senior Software Engineer — Backend.
- Year 1 lasts 52 weeks and includes study, portfolio, English, AI-assisted development, assessments, and progressive job search.
- AI/Codex/Claude/LLM/RAG/agents/MCP are mandatory curriculum areas, not optional appendices.
- `.study/` is a nested independent private Git repository and is never a Git submodule.
- `.study/` must be ignored by the public repository from the first public commit.
- Historical learner evidence is immutable; agents may append feedback but never overwrite raw attempts/results.
- Every practical activity declares one study mode: `SOLO`, `AI-ASSISTED`, or `HYBRID`.
- Public curriculum cannot be automatically rewritten from one learner's performance or one job posting.
- Material curation prioritizes official/free primary sources and records verification date/version relevance.
- Major curriculum changes are proposal-first; low-risk public maintenance and future private schedule adaptation may be autonomous within documented rules.
- Daily-file mass generation is forbidden until the 52-week matrix, Week 0 diagnostic design, schemas, assessment model, and agent rules have each passed their checkpoint review.
- Obsidian remains the human interface; V1 must not become a custom web application.
- No personally identifying learner data is required by public files.

---

## File Structure Locked for V1 Planning

The implementation should converge on this structure before mass content generation:

```text
backend-engineer-roadmap/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── 00 Dashboard/
├── 01 Curriculum/
├── 02 Daily Assessments/
├── 03 Weekly Simulations/
├── 04 Question Bank/
├── 05 Projects/
├── 06 Error Notebook/
├── 07 Career/
├── 08 Reviews/
├── 09 Resources/
├── 10 AI Engineering/
├── 11 Agent/
│   ├── methodology/
│   ├── prompts/
│   ├── rules/
│   └── examples/
├── 12 Year 2/
├── 90 Templates/
├── docs/
├── scripts/
└── .obsidian/
```

Private learner state template/documentation describes, but the public repo does not commit, this structure:

```text
.study/
├── README.md
├── profile.md
├── state.yaml
├── metrics.yaml
├── current-plan.md
├── progress/
├── assessments/
├── reviews/
├── errors/
├── projects/
├── career/
├── agent/
└── archive/
```

---

### Task 1: Freeze the Approved Architecture and Scaffold Planning Boundaries

**Files:**
- Modify: `docs/superpowers/specs/2026-09-15-adaptive-backend-roadmap-design.md`
- Create: `.gitignore`
- Create: `docs/decision-log.md`
- Create: `docs/checkpoints.md`

**Produces:** An explicit approved-spec state, non-negotiable public/private boundary, and named approval gates for later tasks.

- [ ] **Step 1: Mark the design specification as approved**

Change the spec header from `Status: Draft for user review` to:

```markdown
**Status:** Approved for V1 implementation
**Approved:** 2026-09-15
```

Do not change the approved architectural decisions while making this status edit.

- [ ] **Step 2: Protect private state before any public content exists**

Create `.gitignore` containing at minimum:

```gitignore
# Private learner state — independent nested Git repository
.study/

# Secrets / local environment
.env
.env.*
!.env.example

# OS/editor noise
.DS_Store
Thumbs.db
```

- [ ] **Step 3: Create the decision log**

`docs/decision-log.md` must record these decisions as V1 locked:

1. public core + private nested `.study/`;
2. no submodule;
3. English-first public repository;
4. PHP-experienced target for V1;
5. Obsidian + Markdown + Git, no custom app;
6. AI is mandatory across both tool-use and AI-system-building tracks;
7. historical evidence is immutable;
8. curriculum changes use proposal-first governance;
9. first-year goal includes obtaining a stronger job, not merely finishing study;
10. US campaign begins after approximately one year of consolidation at the stronger professional level, triggered by readiness rather than a hard date.

- [ ] **Step 4: Create checkpoint definitions**

`docs/checkpoints.md` must define these human-review gates:

- C1 — 52-week matrix + Week 0 diagnostic blueprint approved;
- C2 — schemas + assessment/scoring model approved;
- C3 — agent rules + command recipes approved;
- C4 — project progression + resource policy approved;
- C5 — generated sample month validated;
- C6 — full 52-week generation allowed;
- C7 — public-release QA passed.

- [ ] **Step 5: Validate Task 1**

Checks:

```bash
grep -n "Status:.*Approved" docs/superpowers/specs/2026-09-15-adaptive-backend-roadmap-design.md
grep -n "\.study/" .gitignore
grep -n "C1" docs/checkpoints.md
```

Expected: each command returns at least one matching line.

- [ ] **Step 6: Commit**

```bash
git add .gitignore docs/
git commit -m "docs: freeze roadmap v1 architecture"
```

---

### Task 2: Design Week 0 Diagnostic Blueprint

**Files:**
- Create: `docs/design/week-0-diagnostic-design.md`
- Create: `01 Curriculum/00 - Week 0 Diagnostic/README.md`
- Create: `90 Templates/diagnostic-result.md`

**Consumes:** Approved V1 target profile and study-mode definitions.

**Produces:** A diagnostic specification, not the full question bank yet.

- [ ] **Step 1: Define diagnostic domains**

The design must cover:

- PHP language and runtime fundamentals;
- OOP/SOLID/design reasoning;
- Composer/dependency management;
- CakePHP depth;
- Laravel familiarity;
- MySQL/data modeling/indexing/transactions;
- Redis/caching/data structures;
- Git/GitHub;
- HTTP/API/security fundamentals;
- testing/static analysis;
- Linux/networking basics;
- Docker;
- AWS/cloud fundamentals;
- CI/CD;
- system design/distributed systems;
- algorithms/data structures;
- English technical comprehension/speaking/writing;
- Codex/Claude/agentic development;
- LLM/AI engineering fundamentals.

- [ ] **Step 2: Define evidence types per domain**

Each domain must use at least two of the following where appropriate:

```text
concept explanation
code reading
hands-on task
debugging task
architecture reasoning
English explanation
SOLO practical task
HYBRID comparison task
```

- [ ] **Step 3: Define diagnostic output**

The Week 0 result must produce private state entries for:

```yaml
skill_state:
  <skill-id>:
    demonstrated_score: 0
    confidence_self_report: 0
    study_priority: normal
    evidence: []
    recommended_entry_depth: foundation
```

Scores are placeholders for schema shape here; exact scoring weights are Task 5.

- [ ] **Step 4: Define diagnostic duration ceiling**

Design target:

- total diagnostic work spread across 5–7 days;
- no single weekday block > 2.5 hours unless learner opts in;
- at least one closed SOLO assessment;
- at least one AI-assisted engineering exercise;
- English observed across multiple tasks rather than one grammar test.

- [ ] **Step 5: Create learner-facing Week 0 README skeleton**

It must explain purpose, rules, allowed AI use, what is recorded privately, and that poor results do not block entry — they change depth and review frequency.

- [ ] **Step 6: Create diagnostic-result template**

Template headings:

```markdown
# Diagnostic Result — {{date}}

## Domain
## Mode
## Raw attempt
## Score
## Reasoning quality
## Communication quality
## English quality (when applicable)
## Gaps detected
## Evidence links
## Recommended adaptation
```

- [ ] **Step 7: Checkpoint C1-A**

Do not author the final Week 0 questions until the blueprint has been reviewed against the 52-week matrix in Task 3.

- [ ] **Step 8: Commit**

```bash
git add "01 Curriculum/00 - Week 0 Diagnostic" "90 Templates/diagnostic-result.md" docs/design/week-0-diagnostic-design.md
git commit -m "docs: design week zero diagnostic"
```

---

### Task 3: Create the Exact 52-Week Curriculum Matrix

**Files:**
- Create: `docs/design/52-week-curriculum-matrix.md`
- Create: `01 Curriculum/README.md`
- Create: `01 Curriculum/year-1-matrix.yaml`

**Consumes:** Week 0 diagnostic blueprint and approved spec.

**Produces:** Exact week-by-week outcomes without generating daily files.

- [ ] **Step 1: Define transversal tracks**

Every week matrix entry must explicitly account for applicable tracks:

```text
Core Backend Engineering
English
AI-Assisted Development
Project
Review/Assessment
Career
```

Not every track needs equal hours each week, but no track may silently disappear for long periods without a stated reason.

- [ ] **Step 2: Allocate macro phases**

Use the approved progression as the starting constraint:

```text
Weeks 01–08  PHP/OOP/Composer/Git/Linux basics + agent workflows
Weeks 09–16  MySQL/Redis/HTTP/APIs/testing
Weeks 17–24  Laravel/CakePHP modernization/architecture/security/Docker
Weeks 25–32  AWS/CI-CD/queues/observability/Terraform
Weeks 33–40  system design/distributed systems/LLM + AI engineering
Weeks 41–46  algorithms/interviews/advanced project/agentic engineering
Weeks 47–52  intensive applications/interviews/market-driven remediation
```

- [ ] **Step 3: Make AI present from Week 1**

The matrix must not postpone AI until Weeks 33–40. Early weeks cover developing *with* agents; later weeks deepen building *with* LLMs/agents.

Required early progression:

```text
Week 1  safe agent use, repository instructions, review-before-accepting
Week 2  context quality and task decomposition
Week 3  agent-assisted testing/review
Week 4  debugging with agent + independent verification
Weeks 5–8 increasingly realistic Codex/Claude workflows
```

Later AI-building topics must include structured outputs, tool calling, embeddings/RAG, evals, security, agent workflows, and MCP.

- [ ] **Step 4: Integrate progressive job search**

The matrix must include:

```text
Months 1–2  no application quota; role-market observation allowed
Month 3     structured vacancy analysis starts
Month 4     CV/LinkedIn/GitHub positioning
Month 5     first selective applications
Month 6     experimental interviews
Months 7–9 regular applications
Months 10–12 intensive campaign + real-feedback remediation
```

- [ ] **Step 5: Define one primary outcome per week**

Each week must include fields equivalent to:

```yaml
week: 1
phase: foundations
primary_outcome: "Explain and experimentally verify PHP type behavior"
core_topics: []
english_outcome: "..."
ai_outcome: "..."
project_milestone: "..."
assessment_mode: "..."
career_action: "..."
prerequisites: []
phase_gate: false
```

- [ ] **Step 6: Integrate four phase gates**

Place gates near the ends of Months 3, 6, 9, and 12. Each gate must test cumulative capability and may trigger recovery work without erasing future schedule history.

- [ ] **Step 7: Check sequencing constraints**

Verify at minimum:

- indexing precedes advanced query tuning;
- transactions/locking precede distributed transaction patterns;
- HTTP precedes API auth/security design;
- Docker precedes container orchestration discussion;
- cloud basics precede Terraform automation of cloud resources;
- queues/events precede advanced event-driven patterns;
- LLM API basics precede RAG and agents;
- tool calling precedes MCP server/client exercises;
- foundational system design precedes senior mock interviews;
- Git fundamentals precede agent-driven repository automation.

- [ ] **Step 8: Checkpoint C1-B — approve exact weekly matrix**

No daily task generation proceeds until C1-B is accepted.

- [ ] **Step 9: Commit**

```bash
git add "01 Curriculum" docs/design/52-week-curriculum-matrix.md
git commit -m "docs: define year one curriculum matrix"
```

---

### Task 4: Design Public/Private Schemas and Note Frontmatter

**Files:**
- Create: `docs/design/data-schemas.md`
- Create: `90 Templates/daily-plan.md`
- Create: `90 Templates/daily-assessment.md`
- Create: `90 Templates/weekly-simulation.md`
- Create: `90 Templates/error-entry.md`
- Create: `90 Templates/review-event.md`
- Create: `90 Templates/job-analysis.md`
- Create: `90 Templates/interview-retrospective.md`
- Create: `90 Templates/curriculum-proposal.md`
- Create: `docs/examples/private-state/` with synthetic-only examples

**Produces:** Stable schemas that agents and dashboards can rely on.

- [ ] **Step 1: Define canonical IDs**

Use stable kebab-case IDs for topics/tasks/reviews, e.g.:

```text
php-strict-types
mysql-composite-indexes
redis-cache-stampede
ai-tool-calling
review-2026-10-14-mysql-composite-indexes-d7
```

- [ ] **Step 2: Define frontmatter for learning tasks**

Minimum shape:

```yaml
id: task-unique-id
week: 1
day: 1
track: core
skill_ids: []
mode: SOLO
estimated_minutes: 50
resources: []
deliverables: []
review_policy: adaptive
```

- [ ] **Step 3: Define immutable assessment record structure**

Raw attempt and grading feedback must be separate sections/fields. The schema must make overwriting the raw answer visibly incorrect.

- [ ] **Step 4: Define private state examples using synthetic learner data only**

Include examples for `state.yaml`, `metrics.yaml`, `reviews/queue.yaml`, one job analysis, and one interview retrospective.

- [ ] **Step 5: Define schema versioning rule**

Every machine-readable private file includes `schema_version`. Migration guidance must state that schema changes never rewrite historical raw evidence.

- [ ] **Step 6: Checkpoint C2-A**

Review schema ergonomics in plain Obsidian before building dashboards or automation.

- [ ] **Step 7: Commit**

```bash
git add "90 Templates" docs/design/data-schemas.md docs/examples/private-state
git commit -m "docs: define roadmap data schemas"
```

---

### Task 5: Define Assessment, Scoring, Mastery, and Adaptation Rules

**Files:**
- Create: `docs/assessments.md`
- Create: `docs/adaptive-learning.md`
- Create: `11 Agent/rules/adaptation.md`
- Create: `11 Agent/rules/assessment-integrity.md`

**Consumes:** Schemas from Task 4.

**Produces:** Deterministic rules used by agents and humans.

- [ ] **Step 1: Define scoring dimensions**

Use separate dimensions rather than one opaque score:

```text
factual correctness
reasoning/explanation
practical execution
validation/testing
communication
English quality (only when relevant)
AI supervision quality (AI-ASSISTED/HYBRID only)
```

- [ ] **Step 2: Define task-type weighting tables**

Create explicit weights for at least:

- conceptual assessment;
- coding/lab;
- SQL/debugging lab;
- system-design interview;
- AI-assisted engineering challenge;
- English technical explanation.

Weights must sum to 100% within each task type.

- [ ] **Step 3: Encode approved performance thresholds**

```text
>=85%   maintenance / spaced review
70–84%  keep load
50–69%  targeted reinforcement
<50%    recovery block before advanced dependent topics
```

- [ ] **Step 4: Define confidence mismatch rule**

If self-confidence is high and demonstrated score is low, flag a calibration gap; do not merely schedule more content.

- [ ] **Step 5: Define SOLO vs AI dependence signals**

Example rule: repeated strong AI-ASSISTED performance with weak SOLO conceptual performance keeps the topic active and adds SOLO reconstruction tasks.

- [ ] **Step 6: Define D+1/D+7/D+30 generation behavior**

Specify which error categories generate which review style. D+30 must prioritize transfer/diagnosis over rereading.

- [ ] **Step 7: Define workload ceiling behavior**

When remediation would exceed configured weekly hours, optional new material is deferred before mandatory foundational remediation.

- [ ] **Step 8: Checkpoint C2-B**

Review sample calculations for at least three synthetic learner scenarios before implementation in agents/scripts.

- [ ] **Step 9: Commit**

```bash
git add docs/assessments.md docs/adaptive-learning.md "11 Agent/rules"
git commit -m "docs: define assessment and adaptation model"
```

---

### Task 6: Define Agent Governance and Shared Codex/Claude Instructions

**Files:**
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Create: `01 Curriculum/AGENTS.md`
- Create: `02 Daily Assessments/AGENTS.md`
- Create: `05 Projects/AGENTS.md`
- Create: `07 Career/AGENTS.md`
- Create: `10 AI Engineering/AGENTS.md`
- Create: `docs/agents.md`
- Create: `11 Agent/rules/public-private-boundary.md`
- Create: `11 Agent/rules/history-integrity.md`
- Create: `11 Agent/rules/source-quality.md`

**Produces:** Canonical behavior contract for coding agents.

- [ ] **Step 1: Write concise root `AGENTS.md`**

It must require agents to inspect, before personal adaptation:

```text
.study/profile.md
.study/state.yaml
.study/metrics.yaml
.study/current-plan.md
.study/reviews/queue.yaml
recent assessment records
recent error records
```

when those files exist.

- [ ] **Step 2: Encode public/private write classes**

Root rules must distinguish:

```text
AUTO-PRIVATE
AUTO-PUBLIC-LOW-RISK
PROPOSAL-REQUIRED
NEVER-SILENTLY-MODIFY
```

and point to detailed rule files.

- [ ] **Step 3: Add scoped rules**

Assessment scope must forbid answer-key leakage; career scope must forbid changing public curriculum from a single vacancy; AI scope must require freshness checks for fast-moving vendor/tool material.

- [ ] **Step 4: Create Claude bootstrap**

Keep `CLAUDE.md` minimal. During implementation, verify current Claude Code instruction/import behavior and either reference/import `AGENTS.md` in the supported manner or explicitly instruct Claude to read it first. Avoid duplicating the full policy.

- [ ] **Step 5: Define destructive-action prohibitions**

Agents must never force-push/rewrite Git history, delete historical learner evidence, expose secrets, or move private content into public files without explicit human review.

- [ ] **Step 6: Checkpoint C3-A**

Run a tabletop review of at least six scenarios: failing assessment, stale URL, one unusual job posting, repeated market signal, interview failure, and proposed curriculum topic removal.

- [ ] **Step 7: Commit**

```bash
git add AGENTS.md CLAUDE.md "01 Curriculum/AGENTS.md" "02 Daily Assessments/AGENTS.md" "05 Projects/AGENTS.md" "07 Career/AGENTS.md" "10 AI Engineering/AGENTS.md" docs/agents.md "11 Agent/rules"
git commit -m "feat: define shared agent governance"
```

---

### Task 7: Build the Public Agent Command Recipe Catalog

**Files:**
- Create one file per recipe under `11 Agent/prompts/`
- Create: `11 Agent/prompts/README.md`

**Produces:** Ready-to-copy tool-agnostic workflows with Codex/Claude notes where behavior differs.

- [ ] **Step 1: Implement the required recipe set**

Files:

```text
initialize-study.md
start-day.md
finish-day.md
start-week.md
weekly-retrospective.md
review-errors.md
adapt-plan.md
run-review.md
prepare-assessment.md
review-project.md
analyze-job.md
analyze-market.md
prepare-interview.md
post-interview.md
audit-resources.md
propose-curriculum-improvement.md
sync-dashboard.md
```

- [ ] **Step 2: Use one recipe template**

Every recipe must contain:

```markdown
# Command name

## Purpose
## Preconditions
## Files the agent must read
## Files it may write
## Files it must not alter
## Ready-to-copy prompt
## Expected output
## Validation checklist
## Codex notes
## Claude Code notes
```

- [ ] **Step 3: Protect assessment integrity in prompts**

`prepare-assessment` and `run-review` must state that answer keys remain hidden until submission/explicit abandonment.

- [ ] **Step 4: Make curriculum proposals evidence-based**

`propose-curriculum-improvement` must separate personal gaps from generic curriculum gaps and produce no public edit automatically.

- [ ] **Step 5: Checkpoint C3-B**

Test at least five recipes manually against synthetic `.study/` examples before considering agent behavior stable.

- [ ] **Step 6: Commit**

```bash
git add "11 Agent/prompts"
git commit -m "feat: add agent command recipe catalog"
```

---

### Task 8: Design the Progressive Project Portfolio

**Files:**
- Create: `docs/design/project-progression.md`
- Create: `05 Projects/README.md`
- Create project specification directories/files under `05 Projects/`

**Produces:** Projects that evolve with curriculum rather than unrelated CRUD samples.

- [ ] **Step 1: Define Project A — PHP/CakePHP modernization lab**

Must exercise:

```text
legacy understanding
refactoring
tests
PHPStan/static analysis
query analysis
Redis/caching
Docker
CI
architecture documentation
```

- [ ] **Step 2: Define Project B — modern Laravel backend**

Must progressively add:

```text
API design
MySQL
Redis
auth/authorization
queues
idempotency
webhooks
tests
observability
Docker
CI/CD
AWS
Terraform
```

- [ ] **Step 3: Add AI capabilities to a normal product, not a standalone chatbot**

Later milestones must include at least:

```text
structured extraction/classification
tool calling
RAG/semantic search when justified
evals
prompt-injection/data-boundary considerations
MCP exposure or consumption
human approval for consequential AI actions
```

- [ ] **Step 4: Require engineering artifacts**

Projects must produce selected artifacts such as architecture diagrams, ADRs, trade-off notes, load-test results, incident/debug notes, API docs, and deployment docs.

- [ ] **Step 5: Declare AI mode per milestone**

Some milestones are SOLO-first, some HYBRID, and some explicitly AI-ASSISTED. The project must make learner dependence visible.

- [ ] **Step 6: Checkpoint C4-A**

Validate that project milestones align with the week matrix and do not require technologies before they are taught.

- [ ] **Step 7: Commit**

```bash
git add "05 Projects" docs/design/project-progression.md
git commit -m "docs: define progressive backend project portfolio"
```

---

### Task 9: Build and Verify the Resource Catalog

**Files:**
- Create: `09 Resources/README.md`
- Create topic resource files under `09 Resources/`
- Create: `90 Templates/resource-entry.md`
- Create: `docs/resource-policy.md`

**Produces:** Curated sources mapped to curriculum topics, emphasizing free/official material.

- [ ] **Step 1: Define resource metadata**

Each resource records:

```yaml
title: ""
url: ""
topic_ids: []
type: docs
source_authority: official
language: en
cost: free
last_verified: YYYY-MM-DD
version_scope: ""
notes: ""
```

- [ ] **Step 2: Curate in curriculum order**

Do not collect hundreds of links first. Curate only what is needed for the approved weekly matrix, generally one primary source plus one complementary video/practical source per major learning unit.

- [ ] **Step 3: Verify fast-moving sources on the web at curation time**

Mandatory freshness verification for Codex, Claude Code, OpenAI/Anthropic APIs, MCP, AWS certification/version details, PHP/Laravel active versions, and similar changing topics.

- [ ] **Step 4: Prefer free sources**

Paid material is included only when it provides material value not reasonably replaced by free sources; label it clearly and keep the free path complete.

- [ ] **Step 5: Checkpoint C4-B**

Sample-review resource quality for at least one unit from each macro phase before full catalog completion.

- [ ] **Step 6: Commit**

```bash
git add "09 Resources" "90 Templates/resource-entry.md" docs/resource-policy.md
git commit -m "docs: curate roadmap learning resources"
```

---

### Task 10: Create Career and Market-Feedback Workflows

**Files:**
- Create: `07 Career/README.md`
- Create: `07 Career/role-target.md`
- Create: `07 Career/job-analysis-method.md`
- Create: `07 Career/interview-retrospective-method.md`
- Create: `12 Year 2/README.md`
- Create: `12 Year 2/us-readiness-checklist.md`

**Produces:** Progressive first-year job search and second-year consolidation model.

- [ ] **Step 1: Lock first-year target role language**

Primary target:

```text
Senior Backend Engineer / Senior Software Engineer — Backend
```

Core positioning:

```text
PHP/Laravel | MySQL | Redis | AWS | Distributed Systems | AI-Assisted Development
```

CakePHP appears as valuable commercial/legacy-modernization experience, not as the primary identity.

- [ ] **Step 2: Define employer-quality criteria**

Evaluate roles for backend depth, tests, code review, CI/CD, cloud, system complexity, observability, engineering maturity, English/international exposure, and future mobility potential — not salary alone.

- [ ] **Step 3: Implement progressive campaign stages**

Align to the matrix: observation → positioning → selective applications → experimental interviews → regular campaign → intensive campaign.

- [ ] **Step 4: Define market evidence rule**

A single vacancy only changes private gap analysis. Public curriculum proposals require recurring signals across a meaningful sample with time window recorded.

- [ ] **Step 5: Define Year 2 readiness dimensions**

Track impact/ownership, architecture, professional English, international client exposure, interview maintenance, target-company research, and sponsorship/transfer readiness.

- [ ] **Step 6: Commit**

```bash
git add "07 Career" "12 Year 2"
git commit -m "docs: define career feedback and year two workflows"
```

---

### Task 11: Implement Obsidian Templates and Dashboard Model

**Files:**
- Create/modify files under `00 Dashboard/`, `90 Templates/`, `.obsidian/`
- Create: `docs/obsidian-setup.md`

**Consumes:** Stable schemas and adaptation rules.

**Produces:** A usable human interface over public curriculum + optional private state.

- [ ] **Step 1: Keep canonical state outside dashboard**

Document that dashboards are derived views only; `.study/` raw/history files remain canonical.

- [ ] **Step 2: Build generic dashboard sections**

Target sections:

```text
Current week and phase
Today's work
Pending reviews
Skill progress
SOLO vs AI-ASSISTED vs HYBRID
Project milestones
English progress
Active gaps
Career funnel when active
```

- [ ] **Step 3: Use Obsidian plugins only when they materially help**

If Dataview/Tasks are required, document exact plugin requirement and provide a graceful manual fallback for core study use.

- [ ] **Step 4: Validate a clean-clone experience**

A new learner without `.study/` should see useful setup instructions rather than broken queries/errors.

- [ ] **Step 5: Commit**

```bash
git add "00 Dashboard" "90 Templates" .obsidian docs/obsidian-setup.md
git commit -m "feat: add obsidian study interface"
```

---

### Task 12: Author the Week 0 Assessment Content

**Files:**
- Create diagnostic assessment files under `01 Curriculum/00 - Week 0 Diagnostic/`
- Create private-safe answer keys in public assessment structure only where leakage can be controlled by agent instructions/workflow
- Add question-bank references under `04 Question Bank/`

**Consumes:** Approved matrix, diagnostic blueprint, schemas, assessment rules.

**Produces:** Executable diagnostic week.

- [ ] **Step 1: Author domain assessments at the planned depth**

Questions/tasks must distinguish "can perform familiar framework task" from "understands underlying engineering behavior."

- [ ] **Step 2: Add at least one realistic debugging task**

Use synthetic code/data only; no employer-confidential examples.

- [ ] **Step 3: Add English observation tasks**

Include technical reading plus at least one spoken/self-recorded or written explanation prompt.

- [ ] **Step 4: Add Codex/Claude task**

Require agent use followed by learner review/validation, plus a short SOLO explanation of the accepted changes.

- [ ] **Step 5: Validate answer-key isolation**

Ensure learner-facing instructions do not expose expected answers before submission.

- [ ] **Step 6: Commit**

```bash
git add "01 Curriculum/00 - Week 0 Diagnostic" "04 Question Bank"
git commit -m "feat: add week zero diagnostic"
```

---

### Task 13: Generate and Validate a Single Representative Month

**Files:**
- Create daily/weekly content for one representative four-week segment only
- Create: `docs/validation/sample-month-review.md`

**Produces:** A pilot proving that schemas, workload, resources, assessments, agent rules, reviews, and project tasks work together before 52-week generation.

- [ ] **Step 1: Select a representative month**

Prefer a segment that combines theory, practical backend work, English, AI-assisted development, project work, and at least one weekly simulation.

- [ ] **Step 2: Generate daily plans**

Each day must specify exact objective, resource, practice, deliverable, mode, estimated time, and review hooks.

- [ ] **Step 3: Generate daily assessments and weekly simulations**

Use the defined integrity rules and scoring dimensions.

- [ ] **Step 4: Simulate one strong learner and one struggling learner**

Using synthetic private state, verify that adaptation produces different future plans without modifying historical records.

- [ ] **Step 5: Verify weekly-hour ceiling**

Total planned load must remain compatible with the default 12-hour target and be configurable upward to approximately 15 hours.

- [ ] **Step 6: Checkpoint C5**

Human review covers clarity, realistic workload, source quality, difficulty, AI dependence, and Obsidian usability.

- [ ] **Step 7: Commit**

```bash
git add "01 Curriculum" "02 Daily Assessments" "03 Weekly Simulations" docs/validation/sample-month-review.md
git commit -m "feat: validate representative study month"
```

---

### Task 14: Implement Static Repository Validation

**Files:**
- Create: `scripts/validate_repo.py`
- Create: `scripts/README.md`
- Create: `.github/workflows/validate.yml`
- Create: `tests/fixtures/` only if fixtures are needed for the validator

**Produces:** Automated checks for repository invariants; no adaptive-learning web application.

- [ ] **Step 1: Write failing validation cases first**

Validator must detect at least:

```text
public reference/path containing .study data
missing required frontmatter keys
invalid study mode
broken internal Markdown links where statically detectable
duplicate canonical IDs
resource entry missing last_verified
historical template lacking raw-attempt/feedback separation
```

- [ ] **Step 2: Run validator tests and verify failure**

Use Python standard library where practical; do not add large dependencies for simple Markdown/YAML checks.

- [ ] **Step 3: Implement minimal validator**

If YAML parsing requires a dependency, justify and pin the minimal package rather than adding a framework.

- [ ] **Step 4: Add GitHub Actions workflow**

Run repository validation on pull requests and pushes to the main branch.

- [ ] **Step 5: Run locally**

Expected command:

```bash
python scripts/validate_repo.py
```

Expected output ends with a clear success line and non-zero exit on validation failures.

- [ ] **Step 6: Commit**

```bash
git add scripts .github tests
git commit -m "ci: validate roadmap repository invariants"
```

---

### Task 15: Generate the Full 52-Week Public Curriculum

**Files:**
- Populate `01 Curriculum/`
- Populate `02 Daily Assessments/`
- Populate `03 Weekly Simulations/`
- Populate `04 Question Bank/`
- Populate relevant review/project references

**Consumes:** C1–C5 approved artifacts and passing repository validator.

**Produces:** Complete first-year roadmap.

- [ ] **Step 1: Require Checkpoint C6 approval**

Do not start full generation without explicit approval that the representative month is acceptable.

- [ ] **Step 2: Generate phase-by-phase, not all at once**

Recommended batches:

```text
Weeks 01–08
Weeks 09–16
Weeks 17–24
Weeks 25–32
Weeks 33–40
Weeks 41–46
Weeks 47–52
```

Each batch gets validation before the next batch.

- [ ] **Step 3: Enforce daily structure**

Every planned day must make clear:

```text
what to learn
why it matters
primary source
optional complementary source
hands-on exercise
deliverable
mode
estimated time
review implications
```

- [ ] **Step 4: Enforce weekly structure**

Every week must contain a measurable outcome, assessment/simulation, project progression where applicable, English practice, AI/agent practice, and review/retrospective action.

- [ ] **Step 5: Run repository validator after every batch**

```bash
python scripts/validate_repo.py
```

- [ ] **Step 6: Commit each phase independently**

Example:

```bash
git commit -m "content: add weeks 01-08 foundations curriculum"
```

Do not use one giant commit for all 52 weeks.

---

### Task 16: Create Public README, Contribution Guide, and Release Documentation

**Files:**
- Create/finalize: `README.md`
- Create/finalize: `CONTRIBUTING.md`
- Create/finalize: `docs/getting-started.md`
- Create/finalize: `docs/private-progress.md`
- Create/finalize: `docs/study-methodology.md`
- Create/finalize: `docs/projects.md`
- Create/finalize: `docs/career.md`
- Choose and add: `LICENSE`

**Produces:** Public open-source entry experience.

- [ ] **Step 1: README explains the product, not one learner**

It must describe the roadmap as designed for experienced developers who can already ship software but want deeper engineering understanding and senior/international readiness.

- [ ] **Step 2: Add quick start**

Quick start must cover clone → open in Obsidian → initialize private `.study/` → run Week 0 → use agent command recipe.

- [ ] **Step 3: Add Codex/Claude examples**

README includes a few common commands and links to the full recipe catalog rather than duplicating every prompt.

- [ ] **Step 4: Explain public/private Git model clearly**

Warn that learner progress must not be committed to the public repository.

- [ ] **Step 5: Define contribution standards**

Require evidence/source quality, no private learner data, no answer-key leakage, and proposals for major curriculum changes.

- [ ] **Step 6: Choose license deliberately**

Evaluate permissive code/content implications before choosing. Record rationale in the decision log.

- [ ] **Step 7: Commit**

```bash
git add README.md CONTRIBUTING.md LICENSE docs
git commit -m "docs: prepare public roadmap release"
```

---

### Task 17: Public-Release QA and V1 Tag

**Files:**
- Create: `docs/validation/v1-release-checklist.md`
- Modify files only as needed to fix release blockers

**Produces:** Release-ready repository that meets the approved success criteria.

- [ ] **Step 1: Clean-clone test**

From a separate directory, clone/open the repository without `.study/`. Verify onboarding is understandable and there are no broken dashboard assumptions.

- [ ] **Step 2: Private-state initialization test**

Follow public instructions to create an independent nested `.study/.git` and confirm the parent repository still reports `.study/` as ignored.

- [ ] **Step 3: Agent tabletop test**

Run representative commands for Codex/Claude using synthetic state:

```text
initialize-study
start-day
finish-day
weekly-retrospective
analyze-job
post-interview
propose-curriculum-improvement
```

Verify write boundaries.

- [ ] **Step 4: Assessment integrity test**

Verify an agent following repository instructions does not reveal answer keys before a synthetic submission.

- [ ] **Step 5: Resource freshness audit**

Re-check fast-moving technology references immediately before V1 release.

- [ ] **Step 6: Run all static validation**

```bash
python scripts/validate_repo.py
```

Expected: success with zero validation errors.

- [ ] **Step 7: Checkpoint C7**

Complete `docs/validation/v1-release-checklist.md` and review V1 success criteria from the approved spec line-by-line.

- [ ] **Step 8: Commit and tag**

```bash
git add .
git commit -m "release: prepare adaptive backend roadmap v1"
git tag -a v1.0.0 -m "Adaptive Backend Engineer Roadmap v1.0.0"
```

---

## Execution Order and Approval Gates

```text
Task 1
  ↓
Tasks 2–3 ── C1
  ↓
Tasks 4–5 ── C2
  ↓
Tasks 6–7 ── C3
  ↓
Tasks 8–10 ─ C4
  ↓
Tasks 11–12
  ↓
Task 13 ───── C5
  ↓
Task 14
  ↓
C6 approval
  ↓
Task 15
  ↓
Task 16
  ↓
Task 17 ───── C7 / V1
```

## Self-Review Results

**Spec coverage:** All locked decisions in the approved design are represented by an implementation task or global constraint. Deferred items from the spec are explicitly covered: weekly matrix (Task 3), Week 0 (Tasks 2/12), schemas (Task 4), Obsidian queries/templates (Task 11), naming/scaffolding (Tasks 1/4), README (Task 16), commands (Task 7), validation (Task 14), projects (Task 8), assessment weights (Task 5).

**Placeholder scan:** No `TBD`, `TODO`, or "implement later" placeholders are used as execution instructions. Human approval checkpoints are intentional gates, not missing implementation detail.

**Consistency check:** Public/private boundaries, study modes, AI requirements, 52-week horizon, job-search timing, and Year 2 transition match the approved spec.

**Scope check:** The project is large, so implementation is deliberately decomposed into independently reviewable tasks and seven approval checkpoints. Full daily generation is postponed until schemas and one representative month are validated.
