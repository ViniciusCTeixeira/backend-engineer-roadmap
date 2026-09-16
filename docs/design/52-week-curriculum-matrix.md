# Year 1 — Exact 52-Week Curriculum Matrix

**Status:** C1-B candidate for review  
**Default workload:** 12 hours/week, configurable up to approximately 15 hours  
**Target role:** Senior Backend Engineer / Senior Software Engineer — Backend

## Transversal tracks

Every week accounts for six tracks:

1. Core Backend Engineering
2. English
3. AI-Assisted Development / AI Engineering
4. Project
5. Review & Assessment
6. Career

The curriculum is intentionally not “finish studying, then job hunt.” Market observation begins immediately, structured vacancy analysis starts in Month 3, first selective applications start in Month 5, experimental interviews begin around Month 6, regular applications run through Months 7–9, and the final quarter is an intensive campaign.

## Phase gates

- **Week 13 — Gate 1:** foundations + data-layer reasoning
- **Week 26 — Gate 2:** production backend fundamentals
- **Week 39 — Gate 3:** cloud + distributed systems + AI engineering
- **Week 52 — Gate 4:** job-ready cumulative evidence

A gate may trigger private recovery work. It never rewrites historical schedules or assessment records.

## Sequencing constraints verified

- SQL modeling and indexes precede advanced query tuning.
- Transactions/locking precede distributed transaction/reliability patterns.
- HTTP precedes API authentication/security design.
- Docker precedes production container/runtime discussion.
- AWS fundamentals precede Terraform automation.
- Queues precede outbox/saga and advanced event-driven reliability.
- LLM/API fundamentals precede RAG and agent workflows.
- Tool calling precedes MCP implementation.
- System-design foundations precede senior system-design mocks.
- Git fundamentals precede repository-wide agent automation.

## Weekly matrix


## Foundations

### Week 01 — Explain and experimentally verify PHP type behavior and establish safe Git/agent habits
- **Core topics:** PHP type system, strict_types, type coercion, Git working tree/staging/commit
- **English:** Give a 2-minute technical self-introduction and explain one PHP behavior in English.
- **AI:** Use Codex/Claude only after a SOLO attempt; inspect every diff before acceptance.
- **Project:** Initialize the modernization lab and record a clean baseline.
- **Assessment:** closed technical assessment
- **Career:** Observe target-role job descriptions only; no application quota.
- **Prerequisites:** Week 0 diagnostic
- **Phase gate:** no

### Week 02 — Use OOP deliberately and understand Composer/autoloading rather than only framework conventions
- **Core topics:** classes/interfaces/abstract/final, composition vs inheritance, Composer, PSR-4, semantic versioning
- **English:** Write a short English design note explaining composition vs inheritance.
- **AI:** Practice context engineering and task decomposition; provide bounded instructions to an agent.
- **Project:** Extract one responsibility from legacy-style PHP into a testable class boundary.
- **Assessment:** hybrid code/design exercise
- **Career:** Continue passive market observation and collect recurring role titles.
- **Prerequisites:** 1
- **Phase gate:** no

### Week 03 — Apply SOLID and testing feedback to refactor PHP without changing behavior
- **Core topics:** SOLID, dependency inversion, unit-test boundaries, PHPUnit fundamentals, Git branches
- **English:** Write an English pull-request description for the refactor.
- **AI:** Use an agent for test suggestions/code review, then independently validate usefulness.
- **Project:** Add characterization/unit tests before a small refactor.
- **Assessment:** coding/lab challenge
- **Career:** Record common requirements seen in Senior Backend/PHP roles.
- **Prerequisites:** 2
- **Phase gate:** no

### Week 04 — Debug failures systematically and recover safely with Git
- **Core topics:** exceptions/errors, debugging method, Git merge/rebase concepts, revert/reset/reflog, basic CLI
- **English:** Explain a debugging timeline aloud in English.
- **AI:** Debug with an agent but require hypotheses, evidence, and independent reproduction.
- **Project:** Create and fix a reproducible bug; document root cause.
- **Assessment:** debugging simulation
- **Career:** No applications yet; create a private list of interesting employers.
- **Prerequisites:** 1, 2, 3
- **Phase gate:** no

### Week 05 — Understand the PHP web runtime from request to process and dependency execution
- **Core topics:** PHP runtime model, PHP-FPM concept, web request lifecycle, Composer scripts, environment/config
- **English:** Read an English PHP/runtime source and summarize it without translation.
- **AI:** Use an agent to map a repository, then verify its claims against actual files/config.
- **Project:** Document the current request lifecycle of the modernization lab.
- **Assessment:** closed technical assessment
- **Career:** Classify observed vacancies by backend depth and engineering maturity.
- **Prerequisites:** 1, 2, 3, 4
- **Phase gate:** no

### Week 06 — Go deeper than CakePHP CRUD by reasoning about framework lifecycle, ORM behavior, and boundaries
- **Core topics:** CakePHP request lifecycle, ORM/query building, entities/tables, framework conventions vs domain logic
- **English:** Record a short English explanation of where business logic should live.
- **AI:** Constrain an agent to propose a refactor without editing; compare its plan to your own.
- **Project:** Identify one CakePHP-style legacy smell and design a modernization path.
- **Assessment:** architecture/code-reading simulation
- **Career:** Continue market observation; identify whether Laravel appears more frequently than CakePHP.
- **Prerequisites:** 2, 3, 5
- **Phase gate:** no

### Week 07 — Operate comfortably in Linux and reason about processes, files, permissions, ports, and logs
- **Core topics:** Linux filesystem, permissions, processes/signals, SSH, ports/sockets, curl/log inspection
- **English:** Run a five-minute English troubleshooting narration.
- **AI:** Use an agent as a troubleshooting partner without allowing it to execute destructive commands.
- **Project:** Create a local troubleshooting runbook for PHP service failures.
- **Assessment:** hands-on troubleshooting lab
- **Career:** No application quota; note common Linux/infra expectations in target roles.
- **Prerequisites:** 4, 5
- **Phase gate:** no

### Week 08 — Integrate PHP, OOP, Composer, Git, CakePHP reasoning, and Linux into a reproducible engineering workflow
- **Core topics:** integration/refactoring, Git collaboration workflow, dependency hygiene, runtime troubleshooting
- **English:** Present the modernization lab architecture in English for 5 minutes.
- **AI:** Compare Codex and Claude Code on the same bounded review task; assess quality, not style preference.
- **Project:** Publish the first public-safe modernization milestone with README and decisions.
- **Assessment:** weekly integrated simulation
- **Career:** Prepare a list of 20 target-role postings for structured analysis starting Week 9.
- **Prerequisites:** 1, 2, 3, 4, 5, 6, 7
- **Phase gate:** no


## Data and Web

### Week 09 — Model relational data deliberately and write SQL without relying on an ORM
- **Core topics:** relational modeling, normalization, keys/constraints, joins, aggregation, SQL
- **English:** Explain one schema decision in written English.
- **AI:** Ask an agent to critique a schema; accept changes only with SQL reasoning.
- **Project:** Design the data model for the modern Laravel backend project.
- **Assessment:** SQL/modeling assessment
- **Career:** Begin structured vacancy analysis; capture recurring skills and seniority signals.
- **Prerequisites:** 8
- **Phase gate:** no

### Week 10 — Understand B-tree indexing and prove query improvements with EXPLAIN/EXPLAIN ANALYZE
- **Core topics:** indexes, composite indexes, selectivity, covering indexes, EXPLAIN, query plans
- **English:** Write an English before/after performance note with evidence.
- **AI:** Use an agent to propose indexes, then independently validate with query plans and measurements.
- **Project:** Create a repeatable dataset and query-performance benchmark.
- **Assessment:** SQL performance lab
- **Career:** Analyze at least 5 relevant vacancies; do not change public curriculum from this sample.
- **Prerequisites:** 9
- **Phase gate:** no

### Week 11 — Reason about ACID, isolation, locks, deadlocks, and concurrent updates
- **Core topics:** transactions, ACID, isolation levels, locking, deadlocks, optimistic/pessimistic concurrency
- **English:** Explain a deadlock scenario aloud in English.
- **AI:** Use an agent to generate concurrency experiments, but predict expected behavior before running them.
- **Project:** Implement and test a transaction-sensitive workflow.
- **Assessment:** concurrency/debugging lab
- **Career:** Continue vacancy analysis and identify common database depth expectations.
- **Prerequisites:** 9, 10
- **Phase gate:** no

### Week 12 — Use Redis by data model and failure mode, not merely as a generic fast cache
- **Core topics:** Redis data structures, TTL, eviction, RDB/AOF concepts, cache-aside, cache stampede, hot keys
- **English:** Write an English cache-strategy ADR.
- **AI:** Review an agent-proposed caching strategy for stale data, invalidation, and failure behavior.
- **Project:** Add measured cache-aside behavior and invalidation to a project use case.
- **Assessment:** scenario + hands-on lab
- **Career:** Create first draft of your skills inventory against observed market demand.
- **Prerequisites:** 9, 10, 11
- **Phase gate:** no


## Gate 1

### Week 13 — Demonstrate foundations and data-layer understanding without framework or agent dependence
- **Core topics:** PHP/OOP/Composer, Git/Linux, MySQL modeling/indexes/transactions, Redis fundamentals
- **English:** Complete part of the gate explanation and retrospective in English.
- **AI:** Agents are prohibited during closed sections; use them only after submission for feedback comparison.
- **Project:** Freeze Gate 1 project evidence and remediation list.
- **Assessment:** PHASE GATE 1 — cumulative SOLO + practical
- **Career:** Start CV/LinkedIn/GitHub positioning work from evidence, not self-description.
- **Prerequisites:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- **Phase gate:** yes


## Data and Web

### Week 14 — Reason about HTTP semantics before designing APIs
- **Core topics:** DNS/TCP overview, HTTP methods, headers, status codes, cookies/sessions, caching, idempotency
- **English:** Explain an HTTP request lifecycle in English.
- **AI:** Use an agent to inspect HTTP traces/logs, but independently identify protocol-level facts.
- **Project:** Expose a simple API endpoint and document protocol behavior.
- **Assessment:** HTTP analysis assessment
- **Career:** Draft role-focused headline/about positioning; no mass applications yet.
- **Prerequisites:** 13
- **Phase gate:** no

### Week 15 — Design secure, evolvable APIs with explicit auth and authorization trade-offs
- **Core topics:** REST constraints, pagination/filtering, versioning, JWT, OAuth2/OIDC concepts, RBAC, rate limiting, OWASP API risks
- **English:** Write an English API design review comment.
- **AI:** Use an agent for threat brainstorming, then verify each risk against actual architecture.
- **Project:** Add authentication/authorization and API error conventions.
- **Assessment:** API/security design simulation
- **Career:** Finalize first resume draft and GitHub profile cleanup.
- **Prerequisites:** 14
- **Phase gate:** no

### Week 16 — Build a reliable PHP quality loop with tests, static analysis, and useful failure feedback
- **Core topics:** unit/integration/functional tests, test doubles, PHPUnit, PHPStan, coverage trade-offs, testability
- **English:** Explain your testing strategy in English.
- **AI:** Use an agent for test generation only after defining expected behavior and missing cases yourself.
- **Project:** Create a repeatable test/static-analysis command and quality baseline.
- **Assessment:** coding + test-strategy simulation
- **Career:** Prepare a public-safe portfolio narrative for the modernization project.
- **Prerequisites:** 3, 15
- **Phase gate:** no


## Modern Backend

### Week 17 — Understand Laravel request lifecycle, service container, dependency injection, and configuration
- **Core topics:** Laravel lifecycle, service container, dependency injection, routing/middleware, configuration
- **English:** Compare CakePHP and Laravel lifecycle concepts in English.
- **AI:** Use an agent to map a Laravel repository, then verify container bindings and execution path manually.
- **Project:** Bootstrap the modern Laravel backend with explicit architecture notes.
- **Assessment:** framework architecture assessment
- **Career:** Begin selective applications to high-fit roles; quality over volume.
- **Prerequisites:** 16
- **Phase gate:** no

### Week 18 — Use Eloquent and migrations without losing SQL/data-model awareness
- **Core topics:** Eloquent, migrations, relationships, query scopes, N+1, validation
- **English:** Write an English code-review note identifying an N+1 risk.
- **AI:** Use an agent to flag ORM performance issues; validate every claim with SQL/query evidence.
- **Project:** Implement core entities and migrations for the modern backend.
- **Assessment:** ORM/SQL integration lab
- **Career:** Track application outcomes and role-fit privately.
- **Prerequisites:** 9, 10, 17
- **Phase gate:** no

### Week 19 — Implement application security as a design property, not a framework checkbox
- **Core topics:** authentication, authorization/policies, input validation, secrets, CSRF/CORS, secure defaults
- **English:** Explain one auth/authz trade-off in English.
- **AI:** Use an agent for security review with explicit scope and false-positive validation.
- **Project:** Add role/permission rules and a security checklist.
- **Assessment:** security review simulation
- **Career:** Continue selective applications; refine CV based on recurring requirements, not one vacancy.
- **Prerequisites:** 15, 17, 18
- **Phase gate:** no

### Week 20 — Modernize legacy CakePHP code using tests, boundaries, and measured database/cache improvements
- **Core topics:** legacy characterization, refactoring, strangler thinking, CakePHP modernization, technical debt
- **English:** Write an English modernization proposal.
- **AI:** Run a HYBRID refactor: design SOLO, ask agent for alternative, then compare and implement deliberately.
- **Project:** Complete a public-safe CakePHP modernization case study.
- **Assessment:** take-home style modernization challenge
- **Career:** Review first application feedback and update private gap analysis.
- **Prerequisites:** 6, 12, 16, 19
- **Phase gate:** no

### Week 21 — Apply pragmatic architecture patterns without overengineering
- **Core topics:** application services, repositories trade-offs, domain boundaries, DTO/value objects, dependency direction, ADRs
- **English:** Defend an architecture decision in English.
- **AI:** Use an agent as an architecture critic, not as final authority.
- **Project:** Refactor one Laravel flow into clearer boundaries and create an ADR.
- **Assessment:** architecture reasoning simulation
- **Career:** Start interview question bank from real recruiter/technical-screen patterns.
- **Prerequisites:** 17, 18, 19, 20
- **Phase gate:** no

### Week 22 — Containerize a PHP application with reproducible images, networks, volumes, and health checks
- **Core topics:** Docker images/layers, Dockerfile, Compose, networks, volumes, multi-stage builds, health checks
- **English:** Explain the container topology in English.
- **AI:** Use an agent to review Dockerfile/Compose, then verify build reproducibility and runtime behavior.
- **Project:** Containerize Laravel + MySQL + Redis locally.
- **Assessment:** hands-on Docker lab
- **Career:** Continue applications; prioritize roles with mature engineering practices.
- **Prerequisites:** 7, 17, 18
- **Phase gate:** no

### Week 23 — Understand Nginx/PHP-FPM/runtime behavior inside and outside containers
- **Core topics:** Nginx basics, PHP-FPM pools, process model, reverse proxy, timeouts, logs, resource limits
- **English:** Troubleshoot a simulated incident in English.
- **AI:** Use an agent to help form hypotheses from logs, while you choose and validate the next experiment.
- **Project:** Add reverse proxy/runtime configuration and an incident runbook.
- **Assessment:** production-troubleshooting simulation
- **Career:** Run first recruiter/technical mock interview if not yet reached through applications.
- **Prerequisites:** 7, 22
- **Phase gate:** no

### Week 24 — Integrate API, security, tests, architecture, Docker, and runtime operations into one deployable local system
- **Core topics:** integration, configuration hygiene, failure modes, documentation, performance baseline
- **English:** Deliver a 7-minute English project walkthrough.
- **AI:** Use an agent for repository-wide review under bounded goals; triage findings by evidence.
- **Project:** Release modern backend local milestone v1.
- **Assessment:** integrated take-home simulation
- **Career:** Continue selective applications and prepare for experimental interviews.
- **Prerequisites:** 17, 18, 19, 21, 22, 23
- **Phase gate:** no


## Cloud and Delivery

### Week 25 — Build a mental model of AWS identity, networking, regions, and shared responsibility
- **Core topics:** AWS IAM, regions/AZs, VPC/subnets, security groups, shared responsibility, cost awareness
- **English:** Explain a basic AWS deployment architecture in English.
- **AI:** Use an agent for cloud-design questions but verify service behavior in official docs during resource phase.
- **Project:** Draft the AWS target architecture for the Laravel backend.
- **Assessment:** cloud architecture assessment
- **Career:** Prepare for experimental interviews; track cloud gaps surfaced by vacancies.
- **Prerequisites:** 24
- **Phase gate:** no


## Gate 2

### Week 26 — Demonstrate production-ready backend fundamentals through a cumulative implementation and design review
- **Core topics:** HTTP/API/security, testing, Laravel/CakePHP modernization, Docker/runtime, AWS foundations
- **English:** Perform part of the gate as an English design walkthrough.
- **AI:** Closed gate sections remain SOLO; post-gate agent review is allowed.
- **Project:** Freeze Gate 2 evidence and remediation backlog.
- **Assessment:** PHASE GATE 2 — practical + architecture + interview
- **Career:** Run at least one experimental interview or equivalent mock loop.
- **Prerequisites:** 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
- **Phase gate:** yes


## Cloud and Delivery

### Week 27 — Deploy core backend infrastructure using managed AWS compute, storage, database, and cache choices
- **Core topics:** EC2/ECS concepts, ECR, S3, RDS, ElastiCache, load balancer, secrets
- **English:** Explain managed-vs-self-hosted trade-offs in English.
- **AI:** Use an agent to compare deployment options, then document cost/ops/security trade-offs yourself.
- **Project:** Deploy a minimal environment manually before automating it.
- **Assessment:** cloud deployment lab
- **Career:** Move from selective to regular applications.
- **Prerequisites:** 25, 26
- **Phase gate:** no

### Week 28 — Design asynchronous work with queues, retries, DLQs, idempotency, and event boundaries
- **Core topics:** SQS, SNS concept, workers, retry/backoff, DLQ, idempotency, outbox introduction
- **English:** Explain an asynchronous failure path in English.
- **AI:** Use an agent to generate failure scenarios; validate them against your queue design.
- **Project:** Add background job processing and failure handling.
- **Assessment:** event-driven backend simulation
- **Career:** Regular applications; capture messaging/queue requirements in market signals.
- **Prerequisites:** 11, 19, 27
- **Phase gate:** no

### Week 29 — Build CI/CD that produces evidence, not just automated commands
- **Core topics:** GitHub Actions, build/test/static analysis, artifact/image build, deployment gates, rollback concepts
- **English:** Write an English CI failure/rollback note.
- **AI:** Delegate pipeline boilerplate to an agent but independently validate permissions, secrets, triggers, and failure behavior.
- **Project:** Create CI and a controlled deployment pipeline.
- **Assessment:** CI/CD engineering challenge
- **Career:** Regular applications; use pipeline/project evidence in interviews.
- **Prerequisites:** 16, 22, 27
- **Phase gate:** no

### Week 30 — Make the backend observable with structured logs, metrics, traces, and actionable signals
- **Core topics:** structured logging, metrics, tracing, OpenTelemetry concepts, CloudWatch, SLI/SLO basics
- **English:** Explain how you would diagnose high p95 latency in English.
- **AI:** Use an agent to propose observability signals, then remove vanity/noise metrics.
- **Project:** Instrument one critical request path end-to-end.
- **Assessment:** incident/observability simulation
- **Career:** Regular applications and interview remediation.
- **Prerequisites:** 23, 27, 29
- **Phase gate:** no

### Week 31 — Represent cloud infrastructure declaratively with Terraform and safe state practices
- **Core topics:** Terraform providers/resources, variables/outputs, state, remote state concepts, plan/apply, modules basics
- **English:** Write an English infrastructure change summary.
- **AI:** Use an agent to draft Terraform only after defining desired architecture; inspect every resource and IAM implication.
- **Project:** Codify a subset of the manually deployed AWS environment.
- **Assessment:** infrastructure-as-code lab
- **Career:** Regular applications; identify IaC frequency in target market.
- **Prerequisites:** 25, 27, 29
- **Phase gate:** no

### Week 32 — Integrate cloud, queues, CI/CD, observability, and IaC into a production-oriented deployment
- **Core topics:** resilience, backup/restore, secrets, cost, autoscaling concepts, deployment verification
- **English:** Deliver a 10-minute English production-readiness review.
- **AI:** Use an agent for a pre-production checklist, then independently verify critical controls.
- **Project:** Release cloud milestone v2 with deployment/runbook evidence.
- **Assessment:** production-readiness simulation
- **Career:** Regular applications; start prioritizing roles with international exposure when fit is comparable.
- **Prerequisites:** 27, 28, 29, 30, 31
- **Phase gate:** no


## Architecture and AI Engineering

### Week 33 — Design scalable services using load balancing, caching, replication, and capacity reasoning
- **Core topics:** latency/throughput, vertical/horizontal scaling, load balancing, caching, replication, capacity estimation
- **English:** Run a system-design explanation in English for 15 minutes.
- **AI:** Do the first architecture pass SOLO; use an agent only for critique and missing failure modes.
- **Project:** Create a system-design document for scaling the backend.
- **Assessment:** system-design interview simulation
- **Career:** Regular applications; log system-design feedback from interviews/mocks.
- **Prerequisites:** 32
- **Phase gate:** no

### Week 34 — Reason about partitioning, consistency, CAP trade-offs, and distributed data ownership
- **Core topics:** partitioning/sharding, consistency, CAP, quorums concepts, data ownership, eventual consistency
- **English:** Defend a consistency trade-off in English.
- **AI:** Compare your SOLO design to an agent critique; record disagreements and evidence.
- **Project:** Add scaling/data-consistency ADRs.
- **Assessment:** architecture trade-off assessment
- **Career:** Regular applications and targeted remediation.
- **Prerequisites:** 33
- **Phase gate:** no

### Week 35 — Use reliability patterns deliberately across synchronous and asynchronous boundaries
- **Core topics:** timeouts, retries/backoff, circuit breaker, bulkheads concept, outbox, saga, distributed locks trade-offs
- **English:** Explain a failure/recovery sequence in English.
- **AI:** Use an agent to attack the architecture with failure scenarios; prioritize realistic ones.
- **Project:** Implement or simulate at least two reliability patterns with tests.
- **Assessment:** failure-mode design challenge
- **Career:** Regular applications; use reliability stories in behavioral/technical interviews.
- **Prerequisites:** 11, 28, 34
- **Phase gate:** no

### Week 36 — Integrate an LLM API as a backend dependency with structured outputs, latency, cost, and failure controls
- **Core topics:** LLM fundamentals, tokens/context, model selection concepts, streaming, structured outputs, timeouts/retries, cost/latency
- **English:** Explain the AI feature architecture in English without marketing language.
- **AI:** Build with an LLM API but require schemas, validation, observability, and fallback behavior.
- **Project:** Add a small structured extraction/classification feature to the normal product.
- **Assessment:** AI integration lab
- **Career:** Regular applications; begin noting AI-integration requirements where relevant.
- **Prerequisites:** 15, 30, 35
- **Phase gate:** no

### Week 37 — Use tool/function calling safely and distinguish deterministic application logic from model decisions
- **Core topics:** tool calling, JSON schema, tool permissions, validation, idempotent tools, human approval boundaries
- **English:** Explain which actions the model may and may not take.
- **AI:** Implement bounded tool calling with explicit allowlists and validation.
- **Project:** Add one safe read tool and one consequential action requiring approval.
- **Assessment:** AI tool-calling challenge
- **Career:** Regular applications; prepare to discuss AI supervision as engineering, not prompting.
- **Prerequisites:** 36
- **Phase gate:** no

### Week 38 — Build and evaluate retrieval when semantic search is justified
- **Core topics:** embeddings, semantic search, chunking, vector storage concepts, RAG, retrieval quality, citations
- **English:** Write an English RAG trade-off note: when to use it and when not to.
- **AI:** Use agents/LLMs to help generate evaluation queries, but manually inspect retrieval failures.
- **Project:** Add a small document-retrieval feature with measurable retrieval checks.
- **Assessment:** RAG/retrieval lab
- **Career:** Regular applications; keep AI work secondary to core backend fit unless role requires it.
- **Prerequisites:** 36, 37
- **Phase gate:** no


## Gate 3

### Week 39 — Demonstrate cloud, distributed-system, system-design, and foundational AI-engineering capability
- **Core topics:** AWS/CI/CD/observability/Terraform, system design, distributed reliability, LLM integration/tool calling/RAG fundamentals
- **English:** Complete a senior-level architecture walkthrough partly in English.
- **AI:** Closed sections SOLO; HYBRID section measures agent supervision explicitly.
- **Project:** Freeze Gate 3 evidence and remediation backlog.
- **Assessment:** PHASE GATE 3 — system design + production + AI
- **Career:** Transition to intensive campaign if baseline criteria are met; otherwise remediate while continuing applications.
- **Prerequisites:** 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38
- **Phase gate:** yes


## Architecture and AI Engineering

### Week 40 — Evaluate AI behavior, trace failures, and defend against prompt injection/data-boundary failures
- **Core topics:** evals, test datasets, AI tracing, prompt injection, data leakage, guardrails, human-in-the-loop
- **English:** Present one AI failure analysis in English.
- **AI:** Use agents to generate adversarial cases, but keep acceptance criteria deterministic where possible.
- **Project:** Add evals/security checks and an AI observability note.
- **Assessment:** AI safety/evals simulation
- **Career:** Intensive applications begin; convert real feedback into private remediation tasks.
- **Prerequisites:** 36, 37, 38, 39
- **Phase gate:** no


## Interviews and Agentic Engineering

### Week 41 — Build coding-interview fundamentals around complexity, arrays, strings, and hash maps
- **Core topics:** Big O, arrays/strings, hash maps/sets, two-sum style patterns, coding communication
- **English:** Solve and explain one problem in English under time pressure.
- **AI:** Use AI only after the timed SOLO attempt; compare solution clarity and complexity.
- **Project:** Maintain project; no major new feature this week.
- **Assessment:** timed coding interview
- **Career:** Intensive applications; begin systematic interview loop tracking.
- **Prerequisites:** 39
- **Phase gate:** no

### Week 42 — Recognize stack, queue, linked-list, and binary-search patterns
- **Core topics:** stack, queue, linked list, binary search, problem decomposition
- **English:** Narrate assumptions and complexity in English.
- **AI:** Use an agent to review post-solution reasoning, not during timed SOLO work.
- **Project:** Address one project remediation item from Gate 3.
- **Assessment:** timed coding interview
- **Career:** Intensive applications and targeted recruiter/technical-screen practice.
- **Prerequisites:** 41
- **Phase gate:** no

### Week 43 — Use trees and graphs with DFS/BFS while communicating trade-offs clearly
- **Core topics:** trees/BST, graphs, DFS, BFS, visited state, complexity
- **English:** Complete a graph/tree explanation in English.
- **AI:** Use an agent to create variant problems after SOLO mastery, not to solve the timed attempt.
- **Project:** Create one engineering note connecting graph concepts to real backend dependencies if useful.
- **Assessment:** timed coding interview
- **Career:** Intensive applications; prepare company-specific technical topics from upcoming interviews.
- **Prerequisites:** 41, 42
- **Phase gate:** no

### Week 44 — Use common interview patterns such as sliding window, two pointers, heap, and priority queue
- **Core topics:** two pointers, sliding window, heap/priority queue, top-k patterns
- **English:** Run a 45-minute coding mock primarily in English.
- **AI:** Post-mock agent review may identify communication and edge-case gaps.
- **Project:** Keep production project healthy; focus on interview readiness.
- **Assessment:** full coding mock
- **Career:** Intensive applications; prioritize quality of interview conversion over raw application count.
- **Prerequisites:** 41, 42, 43
- **Phase gate:** no

### Week 45 — Handle recursion, backtracking, and introductory dynamic programming without memorizing templates blindly
- **Core topics:** recursion, backtracking, memoization, dynamic programming basics
- **English:** Explain state, recurrence, and complexity in English.
- **AI:** Use an agent only after SOLO attempt to compare alternative formulations.
- **Project:** Complete a project architecture/portfolio polish pass.
- **Assessment:** coding + system-design mixed simulation
- **Career:** Intensive applications; practice behavioral stories using measurable impact.
- **Prerequisites:** 41, 42, 43, 44
- **Phase gate:** no

### Week 46 — Build an agentic engineering workflow using repository instructions, tool boundaries, MCP concepts, and human review
- **Core topics:** agent workflows, context management, repository instructions, MCP client/server concepts, tool boundaries, human-in-the-loop
- **English:** Explain an agent architecture and its safety boundaries in English.
- **AI:** Implement an MCP-based or equivalent tool integration after defining permissions and contracts.
- **Project:** Expose or consume a bounded project capability through MCP where justified.
- **Assessment:** agentic engineering challenge
- **Career:** Intensive applications; be prepared to discuss AI-assisted engineering practices with evidence.
- **Prerequisites:** 37, 40, 45
- **Phase gate:** no


## Market Campaign

### Week 47 — Convert real interview/application feedback into targeted backend remediation without derailing the curriculum
- **Core topics:** gap triage, backend deep dive, SQL/API/runtime review, evidence-based remediation
- **English:** Practice recruiter + technical answers in English from actual gaps.
- **AI:** Use agents to cluster feedback; humans decide whether the signal is real and generalizable.
- **Project:** Fix the highest-value project gap discovered through market feedback.
- **Assessment:** backend deep-dive mock
- **Career:** Set a sustainable intensive application cadence and track funnel metrics.
- **Prerequisites:** 46
- **Phase gate:** no

### Week 48 — Perform a complete senior backend interview loop across PHP, SQL, APIs, runtime, and architecture
- **Core topics:** PHP deep dive, SQL performance, HTTP/API, Docker/cloud, system design
- **English:** Run the majority of a full mock loop in English.
- **AI:** Keep timed/closed sections SOLO; use agent only for retrospective.
- **Project:** Polish project walkthrough and incident/debug stories.
- **Assessment:** full senior backend mock loop
- **Career:** Intensive applications; review funnel conversion and role-fit quality.
- **Prerequisites:** 47
- **Phase gate:** no

### Week 49 — Demonstrate production troubleshooting and data-performance reasoning under interview constraints
- **Core topics:** query diagnosis, locks/concurrency, cache failures, logs/metrics/traces, incident reasoning
- **English:** Run an English incident explanation using STAR + technical detail.
- **AI:** Use an agent after the mock to challenge root-cause assumptions.
- **Project:** Create a concise public incident/postmortem-style case study from synthetic/project data.
- **Assessment:** production incident simulation
- **Career:** Intensive applications; target companies where engineering maturity matches goals.
- **Prerequisites:** 48
- **Phase gate:** no

### Week 50 — Combine coding, system design, and behavioral communication in one realistic interview day
- **Core topics:** DSA review, system design, behavioral stories, trade-off communication
- **English:** Conduct an end-to-end mock interview day in English.
- **AI:** Agents remain outside closed mocks; use them for structured retrospective only.
- **Project:** Final portfolio documentation polish.
- **Assessment:** multi-round interview simulation
- **Career:** Intensive applications; company-specific preparation for active pipelines.
- **Prerequisites:** 48, 49
- **Phase gate:** no

### Week 51 — Prepare selectively for active companies while maintaining general engineering readiness
- **Core topics:** company-specific gaps, backend review, architecture review, offer/role evaluation criteria
- **English:** Practice questions, clarification, and negotiation language in English.
- **AI:** Use agents for research organization and mock generation; verify factual company claims externally when needed.
- **Project:** Freeze a release candidate of the public-safe portfolio evidence.
- **Assessment:** targeted interview simulation
- **Career:** Focus on active pipelines, referrals, follow-ups, and role-quality evaluation.
- **Prerequisites:** 47, 48, 49, 50
- **Phase gate:** no


## Gate 4

### Week 52 — Demonstrate job-ready Senior Backend capability and produce the transition plan for the next professional year
- **Core topics:** cumulative backend engineering, cloud/architecture, AI-assisted engineering, interview readiness, career evidence
- **English:** Complete final technical/behavioral presentation in English and define next English goals.
- **AI:** Complete both SOLO and AI-ASSISTED sections to measure independence and leverage.
- **Project:** Tag Year 1 portfolio milestone and archive evidence without rewriting history.
- **Assessment:** PHASE GATE 4 — final cumulative assessment
- **Career:** Evaluate job outcome/funnel; start Year 2 consolidation when a stronger role is obtained, otherwise continue a focused campaign with remediation.
- **Prerequisites:** 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
- **Phase gate:** yes

## C1-B acceptance criteria

- All 52 weeks have one primary outcome.
- English, AI, project, assessment, and career tracks remain visible.
- AI-assisted development starts in Week 1.
- Building AI-enabled systems starts only after adequate backend/production foundations.
- Job search is progressive and begins before curriculum completion.
- Four cumulative gates are present at Weeks 13, 26, 39, and 52.
- Advanced topics respect prerequisite ordering.
- Default planned workload is 12 hours/week and can be adapted privately without rewriting the public matrix.
