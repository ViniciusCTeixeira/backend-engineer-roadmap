# Week 0 — Diagnostic

Week 0 establishes where the learner should enter the roadmap in depth and review frequency. It is **not** an elimination test.

## What it measures

The diagnostic samples all 19 approved domains:

- PHP language/runtime
- OOP/design
- Composer/dependencies
- CakePHP depth
- Laravel familiarity
- MySQL
- Redis
- Git/GitHub
- HTTP/API/security
- testing/static analysis
- Linux/networking
- Docker
- AWS/cloud
- CI/CD
- system design/distributed systems
- algorithms/data structures
- technical English
- agentic development
- LLM/AI engineering

## Rules

- Follow the declared `SOLO`, `HYBRID`, or `AI-ASSISTED` mode.
- Do not use an agent during `SOLO` blocks.
- Preserve the original attempt before feedback or assistance.
- Completed attempts/results belong only under `.study/`.
- Do not publish employer code, interview NDA material, secrets, customer data, or personal information.
- Low scores change private depth/review priority; they do not block participation.
- Framework familiarity is not treated as proof of underlying engineering mastery.
- AI-assisted success does not replace SOLO conceptual evidence.

## Before Day 1

Run:

`11 Agent/prompts/initialize-study.md`

The private `.study/` state should exist before storing diagnostic attempts.

## Schedule

| Day | Focus | Time | Required |
|---|---|---:|---|
| [[Day 01 - PHP-OOP-Composer-Git]] | PHP, OOP, Composer, Git | 130 min | yes |
| [[Day 02 - MySQL-Redis]] | MySQL, transactions, Redis | 135 min | yes |
| [[Day 03 - Web-Quality-Linux-English]] | HTTP, security, testing, Linux, English | 140 min | yes |
| [[Day 04 - Frameworks-Docker-AWS-CICD]] | CakePHP, Laravel, Docker, AWS, CI/CD | 145 min | yes |
| [[Day 05 - System-Design-Algorithms-English]] | system design, algorithms, English | 135 min | yes |
| [[Day 06 - Agentic-AI-Engineering]] | coding agents and AI engineering | 140 min | yes |
| [[Day 07 - Initialize-and-Adapt]] | consolidate evidence and adapt Weeks 1–4 | up to 90 min | optional |

No required day exceeds 150 minutes.

## Question Bank

Prompts are stored under:

`04 Question Bank/diagnostic/`

The question bank contains **prompts only**. It intentionally contains no answer keys or model solutions.

## How to record results

For each diagnostic evidence event, instantiate:

`90 Templates/diagnostic-result.md`

under private `.study/assessments/`.

Preserve the learner's raw attempt exactly as submitted. Feedback and regrades are appended separately.

## Scoring and adaptation

Use:

- `docs/assessments.md`
- `docs/adaptive-learning.md`
- `11 Agent/rules/adaptation.md`
- `11 Agent/rules/assessment-integrity.md`

Default adaptation bands:

```text
>=85  maintenance / reduced active repetition
70–84 normal planned load
50–69 targeted reinforcement
<50   recovery before dependent advanced work
```

Critical dimension floors still apply.

## After Week 0

Private state should contain:

1. skill-state baseline;
2. confidence-vs-evidence mismatches;
3. active high-priority gaps;
4. recommended entry depth per domain;
5. D+1 / D+7 review events for diagnostic errors;
6. D+30 transfer review where justified;
7. initial private adaptation for Weeks 1–4;
8. English baseline observations;
9. SOLO vs HYBRID/AI-assisted capability baseline.

The public 52-week curriculum remains unchanged.

See `docs/design/week-0-diagnostic-design.md` for the approved blueprint.
