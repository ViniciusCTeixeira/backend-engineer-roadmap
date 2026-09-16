# Progressive Project Portfolio — C4-A

**Status:** C4-A candidate for review  
**Purpose:** Turn the 52-week curriculum into cumulative engineering evidence instead of unrelated tutorial projects.

## Portfolio strategy

V1 uses two complementary projects:

1. **Project A — CakePHP Modernization Lab**
   - exploits existing commercial/legacy experience;
   - proves the learner can understand, stabilize, measure, refactor, test, and modernize an existing backend;
   - runs mainly through Weeks 1–24.

2. **Project B — Production Backend Platform**
   - a modern Laravel backend that grows from data modeling into production operations, cloud, distributed systems, and AI-enabled product capabilities;
   - begins conceptually in Week 9 and becomes the primary project from Week 17 onward.

The projects are not judged by feature count. They are judged by engineering evidence.

## Shared project rules

Every milestone must declare one of:

- `SOLO`
- `HYBRID`
- `AI-ASSISTED`

Project work must never require a technology before the curriculum introduces its prerequisite concepts.

Project evidence should include, where appropriate:

- automated tests;
- static-analysis results;
- SQL/query-plan evidence;
- benchmarks/load tests;
- ADRs;
- architecture diagrams;
- API contracts;
- incident/debug notes;
- runbooks;
- observability evidence;
- CI/CD evidence;
- infrastructure plans;
- security/threat notes;
- trade-off explanations.

## Project A — CakePHP Modernization Lab

### Goal

Take a deliberately legacy-style CakePHP backend and turn it into a documented, testable, measurable, safer system without hiding the original constraints.

The public roadmap may provide a synthetic starter codebase later. A learner may also use a personal synthetic fork. Confidential employer code is forbidden.

### Milestones

| Weeks | Milestone | Mode emphasis | Evidence |
|---|---|---|---|
| 1 | Baseline | SOLO | run instructions, architecture inventory, known risks |
| 2–3 | Boundaries + characterization tests | HYBRID | tests before refactor, design note |
| 4 | Debugging discipline | SOLO | reproducible bug + root-cause note |
| 5–6 | Runtime/CakePHP lifecycle | SOLO/HYBRID | request lifecycle map, ORM/layer analysis |
| 7–8 | Linux/Git operational workflow | SOLO | troubleshooting runbook, clean Git workflow |
| 9–11 | MySQL evidence | SOLO | schema review, EXPLAIN evidence, transaction/concurrency experiment |
| 12 | Redis/caching | HYBRID | cache strategy ADR, invalidation/failure tests |
| 14–16 | HTTP/API/security/testing | SOLO/HYBRID | API behavior notes, security review, stronger test/static-analysis baseline |
| 20 | Modernization case study | HYBRID | before/after architecture, trade-offs, measured improvements |
| 22–24 | Docker + runtime packaging | AI-ASSISTED with validation | reproducible Docker environment, Nginx/PHP-FPM runbook, local release |

### Completion evidence

Project A is complete when the learner can show:

- what the original system did;
- what risks were discovered;
- how behavior was protected before refactoring;
- database/cache improvements backed by evidence;
- a reproducible development/runtime environment;
- what was intentionally **not** modernized and why;
- a public-safe case study with no confidential data.

## Project B — Production Backend Platform

### Product domain

A reusable **Operations Platform API**:

- organizations/tenants;
- users/roles;
- work items/workflows;
- documents/attachments;
- integrations/webhooks;
- asynchronous jobs;
- audit history;
- optional billing/payment workflow.

The domain is intentionally broad enough to exercise realistic backend patterns without becoming a fake social network or tutorial CRUD.

AI features are added to this normal product later; the project is never “just a chatbot”.

### Milestones

| Weeks | Milestone | Mode emphasis | Evidence |
|---|---|---|---|
| 9–12 | Data model design pre-work | SOLO | relational model, index rationale, transaction/caching scenarios |
| 14–16 | API contract + security/test strategy | SOLO | OpenAPI draft, auth/authz design, test strategy |
| 17 | Laravel bootstrap/runtime | HYBRID | lifecycle/container notes, app skeleton |
| 18 | Persistence | SOLO/HYBRID | migrations, Eloquent with SQL evidence, N+1 checks |
| 19 | Authentication/authorization | SOLO | policy matrix, threat notes |
| 21 | Architecture boundaries | HYBRID | ADRs, service/domain boundaries |
| 22–24 | Local production topology | AI-ASSISTED | Docker, Nginx, MySQL, Redis, health checks, k6 baseline |
| 25–27 | AWS architecture/deployment | HYBRID | IAM/VPC diagram, deployment evidence, RDS/cache choices |
| 28 | Async processing | HYBRID | SQS jobs, retries, DLQ, idempotency tests |
| 29 | CI/CD | AI-ASSISTED | GitHub Actions pipeline, security/quality gates |
| 30 | Observability | HYBRID | structured logs, OpenTelemetry, metrics/traces/dashboard |
| 31–32 | Infrastructure as Code + edge | AI-ASSISTED | Terraform, Cloudflare, production-readiness checklist |
| 33–35 | Scale/reliability | SOLO/HYBRID | capacity estimate, failure-mode ADRs, retry/outbox/saga trade-offs |
| 36 | Structured LLM feature | HYBRID | schema-validated extraction/classification, cost/latency/failure handling |
| 37 | Tool calling | HYBRID | bounded tools, allowlist, validation, human approval for consequential action |
| 38 | Retrieval/RAG | HYBRID | retrieval dataset, search evaluation, citation/grounding evidence |
| 40 | AI evals/security | SOLO/HYBRID | evaluation set, prompt-injection tests, tracing and failure analysis |
| 41–45 | Interview-hardening | SOLO | targeted performance/architecture fixes, portfolio walkthrough |
| 46 | Agentic/MCP integration | HYBRID | bounded MCP client/server capability with explicit permissions |
| 47–51 | Market-driven hardening | varies | fixes only when backed by interview/job/project evidence |
| 52 | Year 1 release | SOLO + AI-ASSISTED separately | final architecture, runbook, portfolio evidence, retrospective |

## AI feature progression

AI features must preserve the backend engineering discipline.

### Week 36 — structured extraction/classification

Example:
- upload a document or work-item description;
- extract a strict schema;
- validate on server side;
- store provenance/model metadata;
- handle timeout/retry/fallback;
- measure cost and latency.

### Week 37 — tool calling

Example read tool:
- retrieve work-item status.

Example consequential tool:
- draft a workflow status change.

The model must not execute consequential state change without deterministic validation and explicit human approval.

### Week 38 — retrieval

Use retrieval only if the product has a real knowledge-search use case.

Evidence must include:
- chunking rationale;
- retrieval test cases;
- false-positive/false-negative inspection;
- citations/source IDs;
- comparison to simpler keyword/full-text search where relevant.

### Week 40 — evals/security

Test:
- expected behavior;
- malformed input;
- prompt injection;
- private-data boundary;
- tool misuse;
- unsupported answer behavior.

### Week 46 — MCP

Expose or consume only a bounded capability. Document:
- tools/resources available;
- auth/permissions;
- data boundary;
- failure modes;
- which actions require a human.

## Supporting / Industry Platforms

Supporting platforms are embedded in normal project work:

- Xdebug -> Project A debugging;
- Nginx -> Project A/B runtime;
- OpenAPI + Bruno/Postman -> Project B API contract;
- k6 -> Project B performance baseline;
- Cloudflare -> Project B edge/DNS/CDN/WAF;
- OpenTelemetry/Prometheus/Grafana -> observability;
- RabbitMQ/Kafka -> bounded comparison/lab against SQS;
- Kubernetes/Helm -> exposure lab only unless market evidence promotes depth;
- OpenSearch -> bounded search/indexing comparison where product requirements justify it;
- Trivy/quality tooling -> CI/security exposure.

## Portfolio quality bar

A project milestone is not complete because “the code works”.

For major milestones, require at least three kinds of evidence:

1. working implementation;
2. validation/test/measurement;
3. explanation/trade-off artifact.

## C4-A sequencing validation

The project plan obeys:

- MySQL before ORM performance decisions;
- HTTP before API/security;
- Docker before Kubernetes exposure;
- AWS basics before Terraform;
- SQS/queues before saga/outbox reliability work;
- observability basics before advanced production diagnosis;
- LLM integration before tool calling/RAG;
- tool calling before MCP;
- system design before senior architecture mocks.

No project milestone should force the learner into an advanced technology before its curriculum week.
