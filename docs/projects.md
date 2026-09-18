# Project Portfolio — V1.1

The roadmap uses two cumulative projects to generate credible engineering evidence across the year.

## Evidence rule

Feature count is not the goal.

A strong milestone normally contains:

```text
implementation / artifact
+ validation or measurement
+ explanation / trade-off
```

Prefer a smaller system with strong evidence over a large system assembled to collect technology logos.

## Project A — CakePHP Modernization Lab

Path:

```text
05 Projects/01-cakephp-modernization/
```

Primary period:

```text
Weeks 1–24
```

Project A intentionally remains:

```text
CakePHP
MySQL
Redis
```

Purpose:

- understand a legacy PHP/CakePHP runtime;
- characterize behavior before changing it;
- preserve deep MySQL evidence;
- improve boundaries safely;
- practice Redis/data/cache failure reasoning;
- practice production troubleshooting;
- containerize the system;
- produce a public-safe modernization case study.

Keeping MySQL here is deliberate: V1.1 adds PostgreSQL through Project B rather than erasing the learner's MySQL depth.

## Project B — Production Backend Platform

Path:

```text
05 Projects/02-production-backend-platform/
```

Primary stack:

```text
Laravel
PostgreSQL
Redis
Docker
AWS
Terraform
```

Bounded additions:

```text
Python / FastAPI secondary backend
gRPC / Protobuf where a service boundary is justified
DynamoDB AWS modeling lab
MongoDB document-modeling lab
Kubernetes application-operations evidence
```

### Boundary rule

New technology does not automatically become permanent architecture.

Before adding a separate service or datastore, preserve evidence answering:

1. Which access pattern / failure / ownership / ecosystem need exists?
2. Why does the current Laravel/PostgreSQL/Redis system not solve it cleanly?
3. What operational cost is introduced?
4. How will the choice be tested and observed?
5. What evidence would justify removing/reversing it?

### Evidence areas

- Laravel lifecycle and DI;
- PostgreSQL relational design, plans, migrations, transactions;
- comparison with Project A MySQL evidence;
- Redis;
- REST/OpenAPI and gRPC trade-offs;
- authentication/authorization;
- Python/FastAPI bounded service;
- Docker and Nginx;
- AWS and DynamoDB modeling;
- asynchronous messaging;
- observability across PHP/Python paths;
- Terraform;
- Kubernetes application operations;
- capacity/reliability/distributed-system design;
- MongoDB document modeling and datastore selection;
- structured output/tool calling/RAG/evals;
- bounded MCP integration.

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

1. freeze the SOLO design or attempt;
2. ask the agent for an alternative/review;
3. compare;
4. validate;
5. implement deliberately.

Agent-generated multi-stack code without independent understanding is weak portfolio evidence.

## Portfolio narrative

A public case study should answer:

1. What problem or constraint existed?
2. What evidence did you collect?
3. What decision did you make?
4. What alternatives/trade-offs did you consider?
5. How did you validate the result?
6. What remains imperfect or intentionally out of scope?

See `05 Projects/02-production-backend-platform/README.md` and `docs/design/project-progression.md`.
