# V1.1 US Market Alignment Amendment

**Status:** Approved  
**Approved:** 2026-09-18  
**Applies to:** Adaptive Backend Engineer Roadmap V1.1  
**Parent proposal:** `docs/proposals/2026-09-17-v1-1-us-market-alignment.md`

## Decision

V1.1 keeps PHP/Laravel as the primary backend stack and expands the Year-1 target to a broader US Senior Backend profile without increasing the 52-week / 12-hour-per-week budget.

The V1.0.0 tag and historical release remain immutable.

## Target profile

```text
Senior Backend Engineer

Primary backend:
PHP / Laravel

Secondary backend:
Python / FastAPI

Data:
MySQL / PostgreSQL / Redis
MongoDB
DynamoDB

Platform:
Docker / Kubernetes
AWS / Terraform
Queues / messaging
Observability

Architecture:
REST / OpenAPI / gRPC
Distributed Systems
System Design
Reliability

AI:
LLM APIs
Structured Outputs
Tool Calling
RAG
Evals
Agents / MCP

Polyglot literacy:
Go
Java / Spring Boot
TypeScript / Node.js
```

## Technology depth

### Core

- PHP
- Laravel
- CakePHP modernization
- Python
- FastAPI
- MySQL
- PostgreSQL
- Redis
- Git/GitHub
- HTTP/API/security
- Linux
- Docker
- AWS
- Terraform
- testing/static analysis
- system design/distributed systems
- AI-assisted development / AI engineering

### Supporting

- MongoDB
- DynamoDB
- Kubernetes
- gRPC / Protobuf
- Nginx
- Cloudflare
- OpenAPI
- Bruno/Postman
- k6
- OpenTelemetry
- Prometheus/Grafana
- Sentry
- SQS and bounded broker practice

### Professional exposure

- Go
- Java / Spring Boot
- TypeScript / Node.js
- GraphQL
- Cassandra
- Helm
- Argo CD / GitOps
- OpenSearch / Elasticsearch
- SonarQube
- Trivy
- Vault concepts
- Datadog / New Relic

## Project decisions

### Project A

Project A remains the legacy-modernization vehicle:

```text
CakePHP
MySQL
Redis
```

It preserves deep MySQL and legacy-production evidence.

### Project B

Project B becomes the modern multi-stack vehicle:

```text
Laravel
PostgreSQL
Redis

+ bounded Python/FastAPI service when justified
+ gRPC service-to-service lab
+ DynamoDB AWS data-model lab
+ MongoDB document-model lab
+ Kubernetes application-operation lab
```

MongoDB, DynamoDB, Python service boundaries, or gRPC must not be added to the architecture merely to satisfy the curriculum. Each production-facing choice needs an ADR or equivalent evidence.

## Workload invariants

```text
52 weeks
12 hours/week
624 planned hours
Gate 1 — Week 13
Gate 2 — Week 26
Gate 3 — Week 39
Gate 4 — Week 52
```

New content is funded by redistribution.

## Relational strategy

Weeks 9–11 teach relational concepts once and require evidence in both MySQL and PostgreSQL.

Project A continues MySQL.

Project B uses PostgreSQL so PostgreSQL becomes repeated practice rather than a one-off tutorial.

## NoSQL strategy

The learner must be able to distinguish data models and access patterns:

| Model | Technology | Depth |
|---|---|---|
| relational | MySQL | core |
| relational | PostgreSQL | core |
| in-memory/key-value | Redis | core |
| document | MongoDB | supporting |
| managed key-value | DynamoDB | supporting |
| search/index | OpenSearch | professional exposure |
| wide-column | Cassandra | professional exposure |

## Python strategy

Week 24 establishes a bounded Python/FastAPI backend service.

Weeks 36–40 reinforce Python through structured outputs, tool calling, RAG, and evals.

PHP/Laravel remains the primary backend identity.

## Kubernetes boundary

V1.1 supporting-level Kubernetes includes:

- Deployment;
- Service;
- ConfigMap;
- Secret concepts;
- readiness/liveness probes;
- resource requests/limits;
- rollout observation;
- logs/events for application troubleshooting.

Cluster administration, CNI internals, operators, service mesh, and production GitOps ownership remain out of scope.

## Polyglot boundary

Go, Java/Spring Boot, and TypeScript/Node are code-reading and bounded-change skills.

The learner must be able to map:

```text
entry point
handler/controller
service/domain
configuration/DI
data access
tests
build/run workflow
```

No additional large project is required.

## Release rule

Implementation occurs on `v1.1-market-alignment`.

Before merge:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
```

A V1.1 release tag may be created only after clean-clone QA and a new release checkpoint.

Never move or rewrite `v1.0.0`.
