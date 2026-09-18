# Project Portfolio

The roadmap uses two cumulative projects to generate credible engineering evidence across the year.

## Evidence rule

Feature count is not the goal.

A strong milestone normally contains:

```text
implementation / artifact
+ validation or measurement
+ explanation / trade-off
```

Prefer a smaller system with strong evidence over a large system built mostly by an agent.

## Project A — CakePHP Modernization Lab

Path:

```text
05 Projects/01-cakephp-modernization/
```

Primary period:

```text
Weeks 1–24
```

Purpose:

- understand a legacy PHP/CakePHP runtime;
- characterize behavior before changing it;
- improve boundaries safely;
- deepen SQL/Redis reasoning;
- practice production troubleshooting;
- containerize the system;
- produce a public-safe modernization case study.

The project should remain synthetic or otherwise safe to publish.

Do not paste confidential employer/customer code into it.

## Project B — Production Backend Platform

Path:

```text
05 Projects/02-production-backend-platform/
```

Pre-work begins during the Data & Web phase.

Main progression starts around Week 17 and continues through the rest of Year 1.

Evidence areas include:

- Laravel lifecycle and DI;
- relational design and migrations;
- MySQL performance/concurrency;
- Redis;
- API contracts/security;
- containers;
- AWS;
- asynchronous messaging;
- delivery concepts;
- observability;
- Terraform;
- resilience and distributed-system design;
- AI structured output/tool calling/RAG/evals;
- bounded agent/MCP integration.

## Public vs private project material

Public-safe:

- synthetic code/data;
- architecture diagrams;
- ADRs;
- benchmarks;
- test strategy;
- sanitized incident write-ups;
- reproducible setup instructions.

Private `.study/`:

- personal implementation diary;
- unpublished ideas;
- employer/customer references;
- private credentials;
- application-specific portfolio tailoring;
- personal assessment/reflection.

## AI use

Respect the current task's mode.

For HYBRID work:

1. create/freeze the SOLO design or attempt;
2. ask the agent for an alternative/review;
3. compare;
4. validate;
5. implement deliberately.

An agent-generated feature without independent validation is weak portfolio evidence.

## Portfolio narrative

A public case study should answer:

1. What problem or constraint existed?
2. What evidence did you collect?
3. What decision did you make?
4. What alternatives/trade-offs did you consider?
5. How did you validate the result?
6. What remains imperfect or intentionally out of scope?

See `docs/design/project-progression.md` for the milestone design.
