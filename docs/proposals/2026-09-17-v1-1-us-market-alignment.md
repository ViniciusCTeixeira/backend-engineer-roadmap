---
type: curriculum-proposal
schema_version: 1
id: "v1-1-us-market-alignment-2026-09-17"
status: proposed
created_at: "2026-09-17"
proposal_type: curriculum-change
affected_skill_ids:
  - backend-polyglot
  - python-fastapi
  - postgresql
  - mongodb
  - dynamodb
  - grpc-protobuf
  - kubernetes
  - system-design
evidence_scope: generalized
breaking_change: false
---

# Curriculum Proposal — V1.1 US Market Alignment

## Problem

V1.0.0 successfully builds a deep Senior Backend profile around PHP/Laravel, MySQL, Redis, AWS, distributed systems, observability, infrastructure, AI engineering, and interview readiness.

The current target identity is intentionally broader than a framework, but the generated Year-1 curriculum still has several market-coverage gaps for the proposed US Senior Backend / Senior Software Engineer — Backend profile:

1. PHP/Laravel is the only deeply practiced application-language ecosystem.
2. PostgreSQL is not practiced as a core relational engine even though it is highly prominent in modern backend roles.
3. Redis is the only non-relational data technology practiced deeply; there is no real document-database lab.
4. DynamoDB is absent despite the roadmap's AWS depth.
5. Kubernetes remains professional exposure rather than normal backend-operational literacy.
6. REST/OpenAPI is strong, but service-to-service gRPC/Protobuf is absent.
7. Go, Java/Spring, and TypeScript/Node are absent from structured code-reading/interoperability practice.
8. The current curriculum does not explicitly test database-selection trade-offs across relational, cache, document, cloud key-value, and search models.

The goal is not to turn Year 1 into a technology checklist. The goal is to expand role eligibility while preserving depth, evidence, and the 12-hour weekly ceiling.

## Evidence

### Public ecosystem signals

Freshly reviewed on 2026-09-17:

- GitHub Octoverse 2025 reports TypeScript as the most-used language on GitHub, Python as #2 with approximately +48.78% YoY contributor growth, and continued Java growth.
  - https://github.blog/news-insights/octoverse/what-the-fastest-growing-tools-reveal-about-how-software-is-being-built/
- Stack Overflow Developer Survey 2025 reports a 7-point Python adoption increase, explicitly connecting Python to AI, data science, and backend development; FastAPI gained roughly 5 points among web frameworks; Docker usage increased sharply; PostgreSQL remains a highly desired/admired database.
  - https://survey.stackoverflow.co/2025/technology
- CNCF's 2025 State of Cloud Native Development report shows cloud-native tooling as a normal part of modern backend environments.
  - https://www.cncf.io/reports/state-of-cloud-native-development/

### Directional current-job signals

Indeed US/New York searches performed on 2026-09-17 are used only as directional signals, not market-share measurements. Search counts overlap and depend on query wording.

The sample showed strong recurring demand around:

- Python backend;
- Java backend;
- Go backend;
- TypeScript/Node backend;
- PostgreSQL;
- MongoDB;
- DynamoDB;
- Cassandra;
- AWS;
- Docker/Kubernetes;
- Terraform;
- Kafka/messaging;
- observability;
- distributed systems and system design.

The sample also included PHP/Laravel roles and roles that accept multiple backend languages, reinforcing the value of positioning the learner as a backend engineer whose primary language is PHP rather than filtering only for PHP-labeled roles.

### Technology-specific learning value

PostgreSQL:
- current supported PostgreSQL documentation is 18.x;
- its planner, MVCC, indexing, JSONB, transactional behavior, and ecosystem provide transferable relational depth.
- https://www.postgresql.org/docs/18/

MongoDB:
- official guidance emphasizes access-pattern-driven document modeling and the embed-vs-reference decision;
- sharding and replica-set concepts provide useful distributed-data practice.
- https://www.mongodb.com/docs/manual/data-modeling/
- https://www.mongodb.com/docs/manual/sharding/

DynamoDB:
- data modeling is explicitly partition-key/sort-key and access-pattern driven;
- secondary indexes and partition distribution expose different trade-offs from relational/document databases.
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling.html

gRPC:
- provides service-definition, Protobuf, streaming, and service-to-service RPC concepts across Go, Java, Node, PHP, Python, and other supported languages.
- https://grpc.io/docs/

FastAPI:
- provides a modern Python API path that naturally complements the roadmap's AI engineering weeks.
- https://fastapi.tiangolo.com/tutorial/

## Why this is generic rather than learner-specific

The proposal is based on:

- public ecosystem data;
- a multi-query sample of current US backend vacancies;
- the existing generic target-role definition;
- transferable backend architecture concerns.

It does not rely on one learner score, one company, one interview, or one vacancy.

## Proposed target identity

V1.0.0:

```text
Senior Backend Engineer
PHP / Laravel
MySQL / Redis
AWS
Distributed Systems
AI-Assisted Development
```

Proposed V1.1 positioning:

```text
Senior Backend Engineer

Primary backend:
PHP / Laravel

Secondary backend:
Python / FastAPI

Data:
MySQL / PostgreSQL / Redis
MongoDB
DynamoDB exposure in AWS

Platform:
Docker / Kubernetes
AWS / Terraform
Queues / Kafka ecosystem
Observability

Architecture:
REST / OpenAPI / gRPC
Distributed Systems
System Design
Reliability

AI:
LLM APIs / Structured Outputs
Tool Calling
RAG / Evals
Agents / MCP

Polyglot literacy:
Go
Java / Spring
TypeScript / Node
```

CakePHP remains modernization/production evidence, not the learner's only identity.

## Proposed technology-depth changes

### CORE

Keep:
- PHP
- Laravel
- CakePHP modernization
- MySQL
- Redis
- Git/GitHub
- HTTP/API/security
- Linux
- Docker
- AWS
- Terraform
- CI/CD concepts
- testing/static analysis
- system design/distributed systems
- AI-assisted development / AI engineering

Add:
- PostgreSQL
- Python
- FastAPI

Interpretation:

Python/FastAPI is a **secondary core**, not a replacement for PHP/Laravel. The learner must be able to build, test, debug, and explain one bounded backend service independently.

### SUPPORTING

Keep the approved V1 set and promote/add:

- MongoDB
- DynamoDB
- Kubernetes
- gRPC / Protobuf

Kubernetes is promoted from professional exposure to supporting. The learner must be able to understand and operate normal backend application manifests and failure evidence, but Year 1 does not target cluster-administrator depth.

### PROFESSIONAL EXPOSURE

Add:

- Go
- Java / Spring Boot
- TypeScript / Node.js
- GraphQL
- Cassandra

Keep:

- Helm
- Argo CD / GitOps
- OpenSearch / Elasticsearch
- SonarQube
- Trivy
- Vault concepts
- Datadog / New Relic

Polyglot exposure means code reading, architecture mapping, build/run/test discovery, and a small bounded change. It does not mean production-level language mastery.

## Data strategy

### Project A

Keep the legacy-modernization project on:

```text
CakePHP
MySQL
Redis
```

This preserves realistic legacy/production evidence and gives MySQL continued deep practice.

### Project B

Change the modern platform's primary relational engine from generic/MySQL-oriented persistence to:

```text
Laravel
PostgreSQL
Redis
```

This gives PostgreSQL repeated real use after Weeks 9–11 instead of a one-off comparison lab.

Add only justified bounded components:

- Python/FastAPI service from Week 24;
- MongoDB comparison/lab in Week 34;
- DynamoDB AWS modeling lab in Week 27.

MongoDB or DynamoDB must not be inserted into the production architecture merely to satisfy the curriculum. Their use must be justified by an access pattern and recorded in an ADR.

## NoSQL strategy

The learner should finish Year 1 able to distinguish:

| Model | Technology | Depth | Primary learning |
|---|---|---|---|
| relational | MySQL | core | SQL, indexes, transactions, legacy/production depth |
| relational | PostgreSQL | core | planner/MVCC/modern backend relational depth |
| in-memory/key-value | Redis | core | cache/data structures/TTL/failure modes |
| document | MongoDB | supporting | embedding vs references, denormalization, indexing, replication/sharding |
| managed key-value | DynamoDB | supporting | access-pattern-first design, partition/sort keys, GSIs, hot partitions |
| search/index | OpenSearch | professional exposure | search/indexing boundary |
| wide-column/distributed | Cassandra | professional exposure | partition-oriented distributed-data comparison |

The objective is database selection, not logo collection.

## API and communication strategy

REST/OpenAPI remains the default public API path.

Add:

- gRPC/Protobuf as supporting service-to-service communication;
- GraphQL as bounded professional exposure.

The learner must be able to explain why an interface is REST, gRPC, async messaging, or another model rather than treating them as interchangeable frameworks.

## Kubernetes promotion boundary

V1.1 supporting-level Kubernetes must include a real backend lab covering:

- Deployment;
- Service;
- ConfigMap;
- Secret concepts;
- readiness/liveness probes;
- resource requests/limits;
- rolling update/rollout observation;
- application logs/events for troubleshooting.

Still professional exposure:

- cluster administration;
- advanced networking/CNI;
- operators/controllers;
- service mesh;
- Helm authoring beyond a bounded chart/values exercise;
- Argo CD/GitOps production ownership.

## Workload impact

**No weekly workload increase.**

Invariant:

```text
52 weeks
12 hours/week default
624 total Year-1 planned hours
4 phase gates at Weeks 13, 26, 39, 52
```

The proposal creates space by redistribution, not by adding weeks.

### Main reallocations

1. Weeks 9–11 teach relational concepts once and run evidence in both MySQL and PostgreSQL.
2. Project B then uses PostgreSQL continuously, avoiding a duplicate standalone PostgreSQL course.
3. Week 24 replaces the generic integration week with Python/FastAPI + practical gRPC; integration responsibilities move into Weeks 22–23 and Gate 2.
4. Week 27 adds a bounded DynamoDB model inside the existing AWS data/runtime week.
5. Week 32 spends more hands-on time on Kubernetes while Helm/Argo remain exposure.
6. Week 34 converts the existing distributed-data week into the real MongoDB/NoSQL practical week.
7. Weeks 36–40 use Python as the default AI-feature implementation language, reinforcing Python without new hours.
8. Week 41 uses approximately half of its time for polyglot backend literacy while retaining Big-O/arrays/hash-map interview fundamentals; Weeks 42–45 keep the rest of the DSA progression.
9. Company-specific deeper Go/Java/TypeScript work remains market-triggered in Week 51.

## What is intentionally not added

V1.1 does not add:

- a second full frontend track;
- deep Spring Boot application development;
- deep Go distributed-systems implementation;
- deep Node/NestJS production project;
- Cassandra operations;
- Kubernetes administration;
- a second cloud provider;
- additional certifications;
- extra weekly hours.

Those would dilute the core backend objective.

## Phase-gate changes

### Gate 1 — Week 13

Add transfer evidence for:
- PostgreSQL alongside MySQL;
- explaining engine-specific behavior rather than assuming SQL behavior is universal.

### Gate 2 — Week 26

Add bounded evidence for:
- Python/FastAPI service;
- service-boundary reasoning;
- basic REST vs gRPC choice.

### Gate 3 — Week 39

Add:
- Kubernetes backend-operations evidence;
- MongoDB vs PostgreSQL vs DynamoDB data-selection reasoning;
- Python-based AI/backend implementation evidence.

### Gate 4 — Week 52

Require final evidence that the learner can:
- defend deep PHP/Laravel decisions;
- implement a bounded Python/FastAPI service independently;
- reason across MySQL and PostgreSQL;
- select Redis/MongoDB/DynamoDB appropriately;
- operate an application in Docker/Kubernetes concepts;
- explain REST/gRPC/async trade-offs;
- read unfamiliar Go/Java/TypeScript backend code;
- use AI tools without losing independent engineering judgment.

## Affected files if approved

No implementation is authorized by this proposal alone.

Expected implementation scope:

```text
07 Career/role-target.md
01 Curriculum/year-1-matrix.yaml
01 Curriculum/README.md
00 Dashboard/Dashboard.md

01 Curriculum/09..52 selected week/day files
02 Daily Assessments/selected weeks
03 Weekly Simulations/selected weeks

05 Projects/02-production-backend-platform/*
09 Resources/catalog.yaml
09 Resources/*

docs/superpowers/specs/... V1.1 amendment
docs/validation/v1-1-*.md
```

Project A should require little or no structural change.

## Implementation order if approved

1. Lock V1.1 technology-depth amendment.
2. Update target-role positioning.
3. Update the machine-readable 52-week matrix.
4. Update Project B data/runtime architecture.
5. Add/verify official resources.
6. Regenerate only affected public week/day/assessment/simulation files.
7. Run validator tests and clean-clone QA.
8. Review V1.1 diff against V1.0.0.
9. Tag V1.1 only after a new release checkpoint passes.

Do not rewrite or delete the V1.0.0 tag/history.

## Alternatives considered

### Add all technologies without changing existing weeks

Rejected: violates the 12-hour ceiling and creates shallow checklist learning.

### Replace PHP with Python

Rejected: discards the learner profile's strongest commercial experience and unnecessarily restarts framework depth.

### Choose Java as the secondary core language

Strong market case, but lower combined return for this roadmap because Python also supports AI/RAG/evals/agent work already present in Weeks 36–40.

Java remains structured professional exposure and can be promoted by recurring market evidence.

### Choose Go as the secondary core language

Strong cloud/platform fit, but Python has broader combined backend + AI utility for this Year-1 goal. Go remains structured professional exposure.

### MongoDB only, no DynamoDB

Rejected: MongoDB teaches document modeling well, but DynamoDB adds distinct AWS access-pattern/partition-key reasoning that fits the existing cloud phase.

### DynamoDB only, no MongoDB

Rejected: would make NoSQL learning too AWS-specific and would not provide the same document-modeling/embedding-vs-reference practice.

### Keep Kubernetes as professional exposure

Rejected for V1.1 proposal because current backend-market/cloud-native evidence supports normal application-level Kubernetes literacy, while the proposal still avoids cluster-administration depth.

## Validation plan

Before implementation approval:

- [ ] human reviews technology-depth changes;
- [ ] human reviews exact 52-week redistribution;
- [ ] confirm Week 24 scope is achievable in 12h;
- [ ] confirm Week 34 scope is achievable in 12h;
- [ ] confirm Week 41 polyglot exposure does not break interview preparation;
- [ ] confirm Project B PostgreSQL migration does not erase MySQL evidence;
- [ ] confirm no new technology is promoted based on one vacancy.

After implementation:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_repo.py
git diff --check
git status
```

Additional V1.1 QA should prove:

- every week remains 720 minutes;
- four phase gates remain present;
- new resource IDs resolve;
- PostgreSQL/MongoDB/DynamoDB/Python/Kubernetes/gRPC assessments do not expose answer keys;
- V1.0.0 tag remains untouched;
- clean clone still initializes private `.study/` correctly.

## Human decision

- [ ] Approved
- [ ] Rejected
- [ ] Needs revision
