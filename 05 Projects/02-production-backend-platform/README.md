# Project B — Production Backend Platform — V1.1

## Product

Build a multi-tenant **Operations Platform API** for teams that manage work items, documents, integrations, and asynchronous workflows.

Suggested entities:

- Organization
- User
- Role / Permission
- WorkItem
- WorkflowTransition
- Document
- Integration
- WebhookDelivery
- AuditEvent

An optional billing/payment workflow may be added when it creates useful concurrency/idempotency exercises.

## Architecture principle

The project is **not** a technology checklist.

Start as a coherent backend and introduce new data stores or service boundaries only when an access pattern, failure boundary, scale characteristic, or learning objective justifies them.

Every consequential technology addition should have a short ADR or equivalent evidence.

## Primary stack

```text
Laravel
PostgreSQL
Redis
Docker
AWS
Terraform
```

PostgreSQL is the primary relational engine for Project B.

Project A remains the primary MySQL evidence path.

## Secondary backend service

From Week 24, add one bounded **Python/FastAPI** capability.

The boundary must be justified.

Acceptable examples include:

- document/extraction service;
- AI-oriented classification service;
- retrieval/evaluation service;
- workload whose Python ecosystem materially improves implementation.

Do not split a normal CRUD feature into a microservice merely to claim Python experience.

The learner must be able to build, test, debug, and explain the Python service independently.

## API and service communication

### Public/external contract

- versioned HTTP contract where justified;
- consistent errors;
- pagination/filtering;
- OpenAPI;
- authentication + authorization;
- idempotency where duplicate requests matter.

### Internal/bounded communication

Use gRPC/Protobuf only where a service boundary exists and the trade-off is justified.

Evidence should compare:

```text
REST
gRPC
asynchronous messaging
```

rather than treating them as interchangeable.

## Data

### PostgreSQL

Required:

- explicit relational schema/index rationale;
- measured query behavior;
- transactions/concurrency evidence;
- query-plan evidence;
- migration discipline.

### Redis

Use only where cache/data-structure behavior is justified.

### MongoDB

Week 34 provides a real document-modeling lab.

MongoDB becomes part of the project architecture only if an ADR shows why PostgreSQL/JSONB is not the better choice for the relevant access pattern.

### DynamoDB

Week 27 provides an AWS modeling lab around:

- access patterns;
- partition/sort keys;
- GSIs;
- hot-partition risk;
- RDS vs DynamoDB trade-offs.

It does not need to become a permanent production component.

## Async/integrations

- SQS as the primary AWS-path queue;
- retry/backoff;
- dead-letter handling;
- idempotent consumers;
- webhook delivery/retry model;
- optional bounded RabbitMQ/Kafka comparison.

A Laravel or Python worker may be used when justified.

## Production

- Docker;
- Nginx/runtime;
- CI/CD design and local validation;
- AWS;
- Terraform;
- Cloudflare edge/security;
- structured logs;
- traces/metrics;
- performance baseline.

## Kubernetes

V1.1 adds application-level Kubernetes evidence:

- Deployment;
- Service;
- ConfigMap;
- Secret concepts;
- readiness/liveness;
- requests/limits;
- rollout behavior;
- logs/events.

Cluster administration is not a project requirement.

## Reliability

- timeout budgets;
- retry policy;
- idempotency;
- outbox/saga where appropriate;
- failure-mode analysis;
- datastore-specific failure assumptions.

## AI

Python/FastAPI is the default reference implementation for selected AI capabilities, while Laravel remains able to consume/integrate them.

Required AI evidence:

- structured extraction/classification;
- tool calling;
- retrieval only when justified;
- evals;
- prompt-injection/data-boundary testing;
- human approval for consequential action;
- bounded MCP capability.

## Polyglot evidence

The project does not need Go/Java/TypeScript production services.

Week 41 uses external/synthetic service samples for polyglot code-reading and bounded-change evidence.

## Public portfolio artifacts

By Week 52 the project should contain:

- README with local/cloud setup;
- architecture diagram;
- API documentation;
- key ADRs;
- PostgreSQL schema/index/query notes;
- Redis/cache rationale;
- NoSQL selection ADR/lab evidence;
- Python/FastAPI service evidence;
- REST vs gRPC decision evidence;
- Kubernetes application-operation note;
- observability/runbook;
- CI/CD description;
- Terraform overview;
- performance evidence;
- one synthetic incident/debug report;
- AI evaluation/security note;
- short "what I would change at 10x scale" document.
