# Adaptive Backend Engineer Roadmap

A one-year, evidence-driven roadmap for experienced PHP developers who want to grow into stronger **Senior Backend Engineer / Senior Software Engineer — Backend** roles.

This repository is not a list of links and it is not a personal study diary. It is a reusable study system built around:

- a complete Week 0 diagnostic;
- 52 generated curriculum weeks;
- daily practice and assessments;
- weekly simulations and four phase gates;
- two cumulative backend projects;
- technical English;
- AI-assisted development and AI engineering;
- adaptive review rules;
- an evidence-driven career track;
- optional Obsidian and coding-agent workflows.

The public repository stays reusable. Learner-specific progress lives in a separate private `.study/` repository that is ignored by this repository.

## V1 target

V1 is optimized for developers who already have meaningful PHP experience and want to strengthen the engineering foundations behind production backend work.

The target profile is broader than a framework:

```text
Senior Backend Engineer
PHP / Laravel
MySQL
Redis
Linux
Docker
AWS
Distributed Systems
Testing / Observability / IaC
AI-assisted Development
AI Engineering
```

CakePHP is deliberately treated as valuable legacy/modernization experience rather than as the learner's professional identity.

## What you will build

### Project A — CakePHP Modernization Lab

Weeks 1–24 use a synthetic legacy-oriented PHP/CakePHP system to practice:

- characterization tests;
- runtime/framework understanding;
- SQL and Redis diagnosis;
- safe refactoring;
- production-style troubleshooting;
- Docker, Nginx, and PHP-FPM;
- a public-safe modernization case study.

### Project B — Production Backend Platform

Data/API pre-work starts before Week 17. The main implementation runs through the rest of Year 1 and covers:

- Laravel;
- MySQL and Redis;
- API security;
- asynchronous workflows;
- AWS;
- observability;
- Terraform;
- reliability and distributed-system trade-offs;
- bounded AI features;
- RAG, evals, agents, and MCP.

See [`docs/projects.md`](docs/projects.md).

## Year 1 at a glance

| Weeks | Focus |
|---|---|
| Week 0 | Diagnostic and private-state initialization |
| 1–8 | PHP/OOP/Composer/Git/Linux/CakePHP foundations |
| 9–16 | MySQL, Redis, HTTP, APIs, security, testing + Phase Gate 1 |
| 17–24 | Laravel, modernization, architecture, Docker/Nginx |
| 25–32 | AWS, queues, delivery, observability, Terraform + Phase Gate 2 |
| 33–40 | Scalability, distributed systems, LLM/RAG/evals + Phase Gate 3 |
| 41–46 | Algorithms, interviews, agents, MCP |
| 47–52 | Remediation, full interview campaign + Phase Gate 4 |

The default workload is **12 hours per week**. Learner-specific adaptation may change future private planning, but it does not silently rewrite public curriculum or historical evidence.

## Study method

The default learning loop is:

```text
theory
→ prediction / experiment
→ implementation or diagnosis
→ project evidence
→ explanation
→ assessment
→ spaced review
```

The roadmap uses three explicit study modes:

- **SOLO** — no LLM assistance during the scored/independent task.
- **HYBRID** — preserve the first SOLO attempt, then use an agent and compare.
- **AI-ASSISTED** — agent use is expected, but the learner still reviews and validates the result.

AI-assisted performance alone is not treated as proof of conceptual mastery.

See [`docs/study-methodology.md`](docs/study-methodology.md).

## Quick start

### 1. Clone

```bash
git clone https://github.com/ViniciusCTeixeira/backend-engineer-roadmap.git
cd backend-engineer-roadmap
```

### 2. Open in Obsidian

Obsidian is the intended human interface, but the repository remains plain Markdown + Git.

Open the repository root as an Obsidian vault, then open:

```text
00 Dashboard/Dashboard.md
```

See [`docs/obsidian-setup.md`](docs/obsidian-setup.md).

### 3. Initialize your private learner state

Use the recipe:

```text
11 Agent/prompts/initialize-study.md
```

With Codex or Claude Code, copy the recipe's **Ready-to-copy prompt** and run it from the repository root.

It creates or validates an independent ignored repository under:

```text
.study/
```

Your real scores, progress, weaknesses, applications, interview notes, and private project notes belong there.

See [`docs/private-progress.md`](docs/private-progress.md).

### 4. Complete Week 0

Start at:

[`01 Curriculum/00 - Week 0 Diagnostic/README.md`](01%20Curriculum/00%20-%20Week%200%20Diagnostic/README.md)

Week 0 establishes evidence for entry depth and private adaptation. It is not a pass/fail admission test.

### 5. Start your normal study loop

Agent recipes live under [`11 Agent/prompts/`](11%20Agent/prompts/README.md).

Useful starting points:

```text
initialize-study
start-week
start-day
finish-day
weekly-retrospective
run-review
review-errors
adapt-plan
```

You can also follow every daily Markdown file manually without a coding agent.

## Codex and Claude Code

Repository-level rules are shared through:

```text
AGENTS.md
```

Claude Code compatibility is provided by:

```text
CLAUDE.md
```

which imports the canonical repository instructions.

The roadmap does **not** require one specific coding agent. The important behavior is preserving study mode, private/public boundaries, historical evidence, and independent validation.

See [`docs/agents.md`](docs/agents.md).

## Public repository vs private learner state

Public:

```text
curriculum
assessment prompts
weekly simulations
question banks without answer leakage
projects
resources
templates
agent rules
documentation
validation scripts
```

Private `.study/`:

```text
profile
scores
raw attempts
progress
review queue
active gaps
private project notes
job/application/interview data
agent analysis/proposals
```

`.study/` is intentionally an **independent nested Git repository**, not a submodule.

This design makes it possible to update or fork the public roadmap without publishing personal learner state.

## Repository structure

```text
00 Dashboard/          public navigation
01 Curriculum/         Week 0 + Weeks 1–52
02 Daily Assessments/  daily prompts
03 Weekly Simulations/ weekly simulations / phase gates
04 Question Bank/      diagnostic question banks
05 Projects/           cumulative projects
06 Error Notebook/     public method/templates
07 Career/             career-track methods
08 Reviews/            review system
09 Resources/          curated resource catalog
10 AI Engineering/     AI-engineering guidance
11 Agent/              rules, methodology, prompts, examples
12 Year 2/             post-Year-1 consolidation
90 Templates/          reusable public templates
docs/                  design, methodology, release documentation
scripts/               local repository validator
tests/                 validator regression tests
.study/                private learner state — ignored
```

## Assessments and adaptation

The public repository never stores learner solutions beside assessment prompts.

Raw attempts and historical evidence are immutable after submission. Feedback/regrades are appended rather than rewriting the original attempt.

Default score-driven adaptation:

```text
>= 85  reduce repetition / spaced maintenance
70–84  keep planned load
50–69  targeted practice + earlier review
< 50   recovery before advanced dependencies
```

Critical-dimension floors and prerequisite relationships still matter; total score alone does not establish readiness.

See:

- [`docs/assessments.md`](docs/assessments.md)
- [`docs/adaptive-learning.md`](docs/adaptive-learning.md)

## Local validation

This repository intentionally does **not** run hosted GitHub Actions.

Before public commits:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
git status
```

The validator checks repository invariants including private-state leakage, broken links, canonical IDs, resource references/freshness metadata, assessment integrity, and generated artifacts.

GitHub Actions is still studied in the curriculum in a dedicated learning context; it is simply not enabled as always-on CI for this roadmap repository.

## Resources

Primary/official sources are preferred.

The full V1 learning path must remain possible using free learning resources, excluding optional infrastructure usage.

Fast-moving resources are re-verified more frequently.

See [`docs/resource-policy.md`](docs/resource-policy.md).

## Career track

The career track progressively moves from market observation to selective applications, interviews, remediation, and an intensive late-year campaign.

One vacancy or one interview may influence private preparation. It may not silently rewrite the public curriculum.

See [`docs/career.md`](docs/career.md).

## Contributing

Contributions are welcome when they preserve the roadmap's public/private model and evidence standards.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a change.

## License

Licensed under the [MIT License](LICENSE).

The single permissive license keeps reuse of the curriculum, Markdown, templates, and repository scripts straightforward. See [`docs/licensing.md`](docs/licensing.md) for the project rationale.

## Scope and expectations

This roadmap provides a structured learning system, not a guarantee of employment, promotion, compensation, immigration eligibility, sponsorship, or interview success.

Cloud/vendor exercises may incur optional costs depending on the environment you choose. Prefer local/free-tier/sandbox alternatives when the learning objective does not require paid infrastructure.
