# Project B — Production Backend Platform

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

## Engineering requirements

### API
- versioned HTTP contract where justified;
- consistent errors;
- pagination/filtering;
- OpenAPI contract;
- authentication + authorization;
- idempotency where duplicate requests matter.

### Data
- explicit schema/index rationale;
- measured query behavior;
- transactions for integrity;
- Redis only where a cache/data-structure use case is justified.

### Async/integrations
- SQS as the primary AWS-path queue;
- retry/backoff;
- dead-letter handling;
- idempotent consumers;
- webhook delivery/retry model;
- optional bounded RabbitMQ/Kafka comparison lab.

### Production
- Docker;
- Nginx/runtime;
- GitHub Actions;
- AWS;
- Terraform;
- Cloudflare edge/security;
- structured logs;
- traces/metrics;
- performance baseline.

### Reliability
- timeout budgets;
- retry policy;
- idempotency;
- outbox/saga discussion/implementation where appropriate;
- failure-mode analysis.

### AI
- structured extraction/classification;
- tool calling;
- retrieval only when justified;
- evals;
- prompt-injection/data-boundary testing;
- human approval for consequential action;
- bounded MCP capability.

## Public portfolio artifacts

By Week 52 the project should contain:

- README with local/cloud setup;
- architecture diagram;
- API documentation;
- key ADRs;
- database/index notes;
- observability/runbook;
- CI/CD description;
- Terraform overview;
- performance evidence;
- one synthetic incident/debug report;
- AI evaluation/security note;
- short “what I would change at 10x scale” document.
