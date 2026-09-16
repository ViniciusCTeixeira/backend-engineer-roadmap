# Adaptive Backend Engineer Roadmap — Design Specification

**Status:** Draft for user review  
**Date:** 2026-09-15  
**Primary profile for V1:** Experienced PHP developer progressing toward Senior Backend / Software Engineer  
**Primary study horizon:** 52 weeks to strengthen engineering depth and obtain a stronger role  
**Second horizon:** ~12 months of consolidation after the new role, followed by an active US relocation/sponsorship campaign

## 1. Purpose

Build a public, open-source, Obsidian-based adaptive study system for experienced developers who can already deliver software but want deeper engineering foundations, stronger senior-level backend skills, modern AI-assisted development capability, and preparation for competitive Brazilian and international roles.

The public repository is a reusable learning product. A learner's personal progress is never stored in the public repository. Personal state lives in a separately versioned private nested repository under `.study/`.

V1 is intentionally optimized for an experienced PHP developer. It must be designed so other tracks can be added later without making V1 generic or shallow.

## 2. Product principles

1. **Depth before breadth.** The curriculum prioritizes understanding why systems work, not accumulating tools or certificates.
2. **Theory → experiment → project → explanation.** Every major topic must move through all four stages.
3. **Assessment drives adaptation.** Plans change based on demonstrated performance, not calendar progression alone.
4. **AI amplifies engineering; it does not replace it.** Learners must practice both unaided and agent-assisted work.
5. **History is immutable.** Completed assessments, recorded mistakes, interview notes, and historical scores must never be silently rewritten.
6. **Public curriculum and private learner state are separate.** Personal data never becomes a public commit by default.
7. **The agent proposes broadly and edits narrowly.** Large curriculum changes require review; personal scheduling adaptations can be more autonomous.
8. **Official sources first.** Documentation and materials should prefer official and primary sources.
9. **Git is part of the learning system.** Public curriculum and private learner state are independently versioned.
10. **The roadmap is a product, not a diary.** Public copy must not depend on one learner's identity or personal history.

## 3. Target professional outcome

The main V1 target role is:

> **Senior Backend Engineer / Senior Software Engineer — Backend**, using modern PHP/Laravel plus MySQL, Redis, Docker, AWS, distributed systems, observability, CI/CD, system design, and AI-assisted engineering.

CakePHP remains valuable professional experience and is explicitly used in legacy-modernization exercises, but the roadmap does not position the learner as a CakePHP-only developer.

By the end of the first 52 weeks, the system should prepare the learner to compete for stronger roles in Brazil, remote international contracts, or companies with mature engineering practices. Job search begins before curriculum completion and becomes progressively more intensive.

## 4. Two-repository model

### 4.1 Public repository

Suggested working name:

`backend-engineer-roadmap`

Responsibilities:

- curriculum;
- public study schedules and templates;
- assessments and answer keys where appropriate;
- project specifications;
- resources;
- agent instructions;
- prompt recipes;
- study methodology;
- career preparation templates;
- contribution guidelines;
- examples containing only synthetic data.

### 4.2 Private learner repository

Location inside the Obsidian vault:

`.study/`

The public repository must ignore `.study/` entirely.

`.study/` is initialized as a separate Git repository by each learner. It is not a submodule, because a submodule would expose repository metadata/URL and create unnecessary coupling.

Responsibilities:

- learner profile;
- diagnostic results;
- current state;
- scores;
- error notebook;
- spaced-repetition queue;
- personal schedule adaptations;
- interview history;
- job applications;
- private retrospectives;
- private agent logs;
- personally generated practice artifacts when they contain private data.

## 5. Proposed public repository structure

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
│   ├── getting-started.md
│   ├── study-methodology.md
│   ├── adaptive-learning.md
│   ├── private-progress.md
│   ├── assessments.md
│   ├── projects.md
│   ├── agents.md
│   └── career.md
└── .obsidian/
```

The exact naming can be normalized during implementation. English names are preferred for the public repository.

## 6. Proposed private state structure

```text
.study/
├── README.md
├── profile.md
├── state.yaml
├── metrics.yaml
├── current-plan.md
├── progress/
│   ├── daily/
│   ├── weekly/
│   └── milestones/
├── assessments/
│   ├── daily/
│   ├── weekly/
│   ├── monthly/
│   └── phase-gates/
├── reviews/
│   ├── queue.yaml
│   └── completed/
├── errors/
│   └── error-log.md
├── projects/
│   └── private-notes/
├── career/
│   ├── jobs/
│   ├── applications/
│   ├── interviews/
│   └── market-signals/
├── agent/
│   ├── last-analysis.md
│   ├── change-log.md
│   └── proposals/
└── archive/
```

### 6.1 `profile.md`

Human-readable learner context. May contain experience, available weekly study time, current stack, target role, English goal, constraints, and optional personal notes.

### 6.2 `state.yaml`

Machine-friendly current state. Minimum fields:

```yaml
schema_version: 1
current_week: 0
current_phase: diagnostic
start_date: null
target_role: senior-backend-engineer
weekly_hours_target: 12
study_modes:
  solo: true
  ai_assisted: true
  hybrid: true
skill_state: {}
active_gaps: []
current_milestones: []
```

### 6.3 `metrics.yaml`

Aggregated metrics only. Raw history remains in dated assessment files.

Minimum categories:

- completion rate;
- weekly study hours;
- assessment average;
- trailing four-week average;
- skill confidence versus demonstrated score;
- SOLO score;
- AI-ASSISTED score;
- HYBRID score;
- review backlog;
- project progress;
- job-market funnel once active.

### 6.4 Review queue

`reviews/queue.yaml` tracks review events without modifying historical notes.

Minimum item shape:

```yaml
- id: review-unique-id
  topic: mysql-composite-indexes
  source: assessment-2026-09-20
  reason: recurring-error
  due_date: 2026-09-21
  interval: D+1
  status: pending
```

## 7. Public/private write boundary

### Agent may autonomously change private learner state

Within `.study/`, agents may update future plans, review queues, aggregated metrics, current priorities, and private recommendations, provided historical records are preserved.

### Agent may autonomously make low-risk public maintenance changes

Examples:

- fix broken internal links;
- fix obvious typos;
- update stale URLs after verifying the replacement;
- normalize formatting;
- add cross-references;
- correct metadata that is objectively wrong.

### Agent must create a proposal before substantial public changes

Examples:

- add/remove curriculum topics;
- change phase ordering;
- substantially change assessment difficulty;
- replace a major resource;
- change the target professional profile;
- introduce a new certification;
- add a new technology track;
- change adaptation thresholds.

Proposals go to `11 Agent/...` or `.study/agent/proposals/` depending on whether the motivation is generic or learner-specific.

### Agent must never silently modify

- completed assessment answers;
- historical scores;
- original interview notes;
- recorded job-application outcomes;
- historical error entries;
- Git history using force-push or destructive rewriting;
- public files using private learner data as evidence without anonymization and explicit generalization.

## 8. Agent instruction architecture

### 8.1 Root `AGENTS.md`

The root file is intentionally concise and acts as an index/map rather than a large encyclopedia. This follows current Codex guidance that scoped AGENTS files can apply hierarchically and that overly large root instruction files are counterproductive.

It must define:

- product purpose;
- public/private boundary;
- immutable-history rule;
- required files to inspect before adaptation;
- allowed autonomy levels;
- study-mode rules;
- links to detailed rules under `11 Agent/rules/` and `docs/`;
- validation checklist before commits.

### 8.2 Scoped `AGENTS.md`

Potential scoped files:

- `01 Curriculum/AGENTS.md` — curriculum editing constraints;
- `02 Daily Assessments/AGENTS.md` — assessment integrity and answer-key constraints;
- `05 Projects/AGENTS.md` — project standards and anti-spoon-feeding rules;
- `07 Career/AGENTS.md` — market evidence and job-analysis rules;
- `10 AI Engineering/AGENTS.md` — fast-changing source freshness requirements.

Nested rules override general rules only within their directory scope.

### 8.3 `CLAUDE.md`

Claude-specific bootstrap file. It should be minimal and point Claude Code at the canonical shared instructions rather than duplicating them. Exact import syntax must be validated against the current Claude Code documentation during implementation; if direct import is unavailable or changes, `CLAUDE.md` will contain a concise compatibility layer that instructs Claude to read `AGENTS.md` and the referenced rule files before work.

## 9. Study modes and AI-dependence controls

Every practical task and assessment must declare one mode:

### SOLO

No coding agent or LLM assistance. Appropriate for diagnostics, closed assessments, selected debugging exercises, SQL reasoning, algorithms, system-design explanations, and interview simulations.

### AI-ASSISTED

Agent use is expected. Measures ability to delegate, constrain, review, validate, and integrate agent work.

### HYBRID

Learner attempts the task independently first, records the first result, then uses an agent. The system compares both phases.

The agent must distinguish productivity gain from knowledge substitution. If the learner repeatedly cannot perform the conceptual part in SOLO mode but succeeds only with agents, that topic remains an active knowledge gap.

## 10. Adaptation engine

The first implementation uses transparent rules, not opaque scoring.

Default topic-performance policy:

| Demonstrated performance | Action |
|---|---|
| >= 85% | reduce active repetition; retain spaced maintenance |
| 70–84% | keep planned load |
| 50–69% | increase targeted practice and schedule earlier review |
| < 50% | create recovery block before further advanced dependency topics |

Additional rules:

- three related errors across separate assessments promote the topic to `high` priority;
- two consecutive strong weekly results may reduce repetition, but not remove mandatory phase-gate coverage;
- a failed job interview may create private remediation tasks immediately;
- one job posting may not alter the public curriculum;
- recurring requirements across a meaningful job sample may generate a public curriculum proposal;
- overdue reviews must be considered before adding optional new material;
- workload adaptation must respect the learner's configured weekly-hour ceiling.

Thresholds must be configurable later, but V1 uses these defaults.

## 11. Spaced review model

The PRF study vault's D+1 / D+7 / D+30 idea is retained and expanded.

A review may be scheduled because of:

- unknown concept;
- confused concepts;
- forgotten concept;
- repeated error;
- poor explanation despite correct implementation;
- interview failure;
- project bug caused by a knowledge gap.

Review format evolves with mastery:

- D+1 may ask for explanation or a small exercise;
- D+7 should require reconstruction or applied use;
- D+30 should prefer diagnosis, transfer, or use in a realistic scenario.

Repeated rereading alone does not count as successful review.

## 12. Assessment model

### Daily assessment

Short, generally 15–30 minutes. Mixes conceptual questions, code reading, practical exercises, and occasional English explanation.

### Weekly simulation

Rotates among:

- closed technical assessment;
- coding/lab challenge;
- agentic engineering challenge;
- interview/system-design simulation.

### Monthly checkpoint

Longer assessment integrating multiple subjects and project work.

### Phase gate

Four major gates during Year 1. Advancement depends on evidence, not date alone.

Historical attempts and scores are immutable.

## 13. Curriculum strategy for V1

Year 1 is organized around the following progression:

- Weeks 1–8: PHP foundations, OOP, Composer, Git, Linux basics, Codex/Claude workflows;
- Weeks 9–16: MySQL, Redis, HTTP, APIs, testing;
- Weeks 17–24: Laravel, CakePHP modernization, architecture, security, Docker;
- Weeks 25–32: AWS, CI/CD, queues, observability, Terraform;
- Weeks 33–40: system design, distributed systems, AI engineering fundamentals and LLM integration;
- Weeks 41–46: algorithms, technical interviews, advanced project work, agentic engineering;
- Weeks 47–52: intensive applications, interviews, remediation based on real market feedback.

English, project work, AI-assisted development, review, and career preparation are transversal tracks from early in the roadmap.

The exact weekly matrix is a separate design artifact and must be approved before daily-file generation.

## 14. AI engineering curriculum scope

V1 includes both **developing with AI** and **building AI-enabled systems**.

Developing with AI includes:

- Codex;
- Claude Code;
- repository instructions;
- context engineering;
- task decomposition;
- agent review;
- debugging with agents;
- test generation and validation;
- safe Git workflows;
- agentic workflows;
- MCP usage for engineering tools.

Building AI-enabled systems includes:

- LLM fundamentals;
- tokens and context;
- model selection;
- latency and cost;
- streaming;
- structured outputs;
- tool/function calling;
- embeddings;
- semantic search;
- vector storage;
- RAG;
- evaluations;
- tracing/observability;
- prompt injection and data leakage;
- guardrails;
- agents/workflows;
- human-in-the-loop patterns;
- MCP server/client concepts.

AI topics must use fresh sources and avoid hard-coding model-specific trivia unless it is deliberately versioned and date-stamped.

## 15. Career-feedback loop

The private system stores job descriptions and interview outcomes.

A job-analysis workflow must classify:

- skills already demonstrated;
- skills in progress;
- missing skills;
- interview risk;
- role fit;
- recurring market signals.

A single vacancy never changes the public curriculum. Public proposals require recurring evidence across multiple relevant roles and must record the evidence window and sample assumptions without leaking private employer information.

## 16. Public README experience

The public README is the product entry point and should explain:

- who the roadmap is for;
- the 52-week outcome;
- how adaptive learning works;
- how SOLO / AI-ASSISTED / HYBRID modes work;
- how to open the repository as an Obsidian vault;
- how to initialize `.study/` privately;
- how to run Week 0 diagnostics;
- how to use Codex or Claude Code;
- how to execute common prompt recipes;
- how to contribute;
- privacy warnings;
- that the roadmap is educational and does not guarantee employment or immigration outcomes.

The README must not present the repository as one person's personal diary. It may state that the V1 track is informed by experienced PHP/backend practice, while being explicit that curriculum recommendations are maintained through source review, assessments, and market feedback rather than personal tenure alone.

## 17. Agent command / prompt recipe catalog

The public repository should include ready-to-copy prompts for at least these actions:

| Command recipe | Purpose |
|---|---|
| `initialize-study` | create/validate private learner state and start diagnostics |
| `start-day` | prepare today's study session and pending reviews |
| `finish-day` | record completion, metrics, errors, and review events |
| `start-week` | prepare weekly goals from curriculum + private state |
| `weekly-retrospective` | analyze the previous week and adapt the next one |
| `review-errors` | classify recurring mistakes and schedule remediation |
| `adapt-plan` | adjust future private schedule within autonomy rules |
| `run-review` | conduct due D+1/D+7/D+30 review without leaking answers |
| `prepare-assessment` | prepare an assessment session without exposing answer keys |
| `review-project` | review project code against the current learning goals |
| `analyze-job` | compare one job description to learner state |
| `analyze-market` | aggregate recurring requirements from multiple jobs |
| `prepare-interview` | generate targeted interview practice from learner gaps |
| `post-interview` | turn interview feedback into private remediation |
| `audit-resources` | detect stale/broken/outdated public resources |
| `propose-curriculum-improvement` | create a reviewable public improvement proposal |
| `sync-dashboard` | recompute dashboard views from private state |

Recipes must be tool-agnostic where possible, with short Codex/Claude notes only when behavior differs.

## 18. Prompt safety and assessment integrity

Agents must not reveal an answer key before an assessment is submitted unless the learner explicitly abandons the assessment.

When grading:

- preserve the learner's original answer;
- create separate feedback;
- distinguish factual correctness, reasoning quality, communication quality, and English quality when relevant;
- never overwrite raw attempts with corrected answers;
- mark agent assistance level.

For AI-assisted assignments, the learner must be able to explain and validate agent-generated changes.

## 19. Resource maintenance

Resources are tagged with metadata such as:

- topic;
- type;
- source authority;
- language;
- cost (`free`, `freemium`, `paid`);
- last verified date;
- version applicability when relevant.

Resource audit prioritizes:

1. official documentation;
2. official/free training from vendors or universities;
3. respected open-source educational material;
4. high-quality community material;
5. paid material only when the benefit is material and a free equivalent is inadequate.

Fast-moving topics such as Codex, Claude Code, AWS, PHP/Laravel versions, and AI APIs require more frequent verification.

## 20. Git and contribution workflow

Public repository:

- normal public Git history;
- feature/fix branches or fork-based contribution depending on chosen governance;
- reviewable commits;
- no private learner files;
- `.study/` in `.gitignore` from the first commit.

Private `.study/` repository:

- independent Git history;
- may point to a private GitHub repository or remain local;
- no requirement to expose remote metadata publicly;
- frequent checkpoint commits encouraged;
- destructive history rewriting discouraged.

When an agent discovers a generic curriculum improvement through private study, it must produce an anonymized proposal. The proposal must explain the generic curriculum issue without copying personal data.

## 21. Dashboard behavior

The public repository ships a generic dashboard template. The learner-specific dashboard reads from `.study/` when available.

Target dashboard domains:

- current week/phase;
- task completion;
- skill progress;
- SOLO vs AI-ASSISTED vs HYBRID performance;
- spaced-review backlog;
- project milestones;
- English progress;
- interview/application funnel once activated;
- active knowledge gaps.

The dashboard is a view over source data, not the canonical storage location.

## 22. Privacy requirements

The public repository must never require personally identifying data.

Examples and templates use synthetic values.

The setup guide must warn learners not to commit:

- personal contact information;
- confidential employer code/data;
- private interview material subject to NDA;
- credentials/tokens;
- customer information;
- sensitive employment documents.

Secrets must be covered by `.gitignore` examples and environment-variable guidance where code projects are involved.

## 23. Year 2 scope

Year 2 is not another full-time curriculum. It is a consolidation system that tracks:

- impact in the new role;
- ownership and architecture experience;
- English in professional settings;
- international freelance/contract work where appropriate;
- system-design maintenance;
- interview readiness;
- target-company research;
- sponsorship/relocation readiness.

The active US campaign begins roughly 12 months after reaching the stronger professional level, but the trigger is milestone-based rather than hard-coded to a specific calendar date.

## 24. V1 non-goals

V1 does not attempt to:

- support every programming language;
- create separate Java/.NET/Node tracks;
- guarantee a job;
- guarantee US immigration;
- replace legal or immigration advice;
- automatically publish private data;
- automatically merge major curriculum changes;
- build a custom web application when Obsidian + Markdown + Git can satisfy the requirement;
- optimize for beginners with no professional programming experience.

## 25. Success criteria for the repository V1

V1 is ready when a new experienced PHP learner can clone the public repository, open it in Obsidian, initialize an ignored/private `.study/` repository, run Week 0 diagnostics, receive an individualized plan, complete tasks in all three study modes, record immutable assessments, receive adaptive D+1/D+7/D+30 reviews, use Codex or Claude through documented prompt recipes, complete the core project progression, and enter the job-search phase without adding any personal information to public Git history.

## 26. Decisions locked by this spec

- One public reusable repository plus one nested ignored private learner repository.
- `.study/` is not a Git submodule.
- Public repository language is primarily English.
- V1 profile is experienced PHP → Senior Backend Engineer.
- AI/Codex/Claude/LLM/MCP are mandatory parts of the roadmap.
- Public curriculum is not automatically rewritten from one learner's results.
- Historical learner evidence is immutable.
- Adaptation occurs primarily in private future planning.
- `AGENTS.md` is concise and points to scoped/detail documentation.
- Obsidian remains the primary human interface.
- Git remains the audit/versioning mechanism.

## 27. Items deliberately deferred to the next design artifacts

The following are not decided in this document and require dedicated follow-up design before implementation:

- exact 52-week curriculum matrix;
- exact Week 0 diagnostic question set;
- exact YAML/frontmatter schemas for all note types;
- exact Obsidian Dataview/Tasks queries;
- final naming of every directory/file;
- final public repository name;
- license choice;
- detailed README copy;
- exact prompt text for every command recipe;
- exact agent validation scripts/checks;
- exact project requirements and milestones;
- exact scoring weights for multi-dimensional assessments.

