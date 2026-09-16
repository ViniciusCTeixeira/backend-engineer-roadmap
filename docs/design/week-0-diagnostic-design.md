# Week 0 Diagnostic Blueprint

**Status:** C1-A candidate for review  
**Purpose:** Establish evidence-based entry depth for an experienced PHP developer without treating professional tenure as proof of conceptual mastery.

## Principles

1. Week 0 is diagnostic, not pass/fail.
2. Poor results do not block the roadmap; they change depth, review frequency, and remediation priority.
3. Historical raw attempts are immutable once submitted.
4. The diagnostic must distinguish familiar framework usage from underlying engineering understanding.
5. English is observed through technical work rather than reduced to a grammar test.
6. AI competence is measured both as tool supervision and as conceptual understanding.
7. At least one closed SOLO assessment and one AI-ASSISTED/HYBRID engineering exercise are mandatory.
8. No single required day should exceed 150 minutes.
9. Final numeric weighting is intentionally deferred to the assessment/scoring design checkpoint.

## Diagnostic domains

| ID | Domain | What the diagnostic must distinguish | Evidence types |
|---|---|---|---|
| `php-language-runtime` | PHP language/runtime | syntax familiarity vs type/runtime understanding | concept explanation, code reading, hands-on |
| `oop-design` | OOP / SOLID / design reasoning | framework habits vs design reasoning | code reading, refactoring reasoning, explanation |
| `composer-dependencies` | Composer | command usage vs dependency/autoload/version understanding | concept explanation, hands-on |
| `cakephp-depth` | CakePHP | routine delivery vs framework lifecycle/ORM/architecture depth | code reading, debugging, architecture reasoning |
| `laravel-familiarity` | Laravel | prior exposure and transferable framework knowledge | concept mapping, code reading |
| `mysql-core` | MySQL | CRUD usage vs modeling/indexing/query/transaction understanding | SQL reasoning, EXPLAIN task, concept explanation |
| `redis-core` | Redis | cache usage vs structures/TTL/persistence/eviction/caching trade-offs | scenario reasoning, hands-on |
| `git-github` | Git / GitHub | routine add/commit/push vs history/recovery/collaboration | command reasoning, recovery scenario |
| `http-api-security` | HTTP / APIs / security | framework API building vs protocol/security understanding | request analysis, design scenario |
| `testing-static-analysis` | Testing / static analysis | test writing vs test strategy/feedback quality | test-design task, code review |
| `linux-networking` | Linux / networking | deployment familiarity vs process/filesystem/network understanding | troubleshooting scenario, commands |
| `docker` | Docker | compose usage vs image/layer/network/volume/runtime understanding | Dockerfile reading, troubleshooting |
| `aws-cloud` | AWS / cloud | service-name familiarity vs architectural reasoning | architecture scenario, concepts |
| `cicd` | CI/CD | pipeline usage vs build/test/deploy/recovery reasoning | pipeline review |
| `system-design` | System design / distributed systems | vocabulary vs trade-off reasoning | architecture reasoning |
| `algorithms` | Algorithms / data structures | implementation fluency vs complexity/pattern recognition | SOLO coding, explanation |
| `english-technical` | Technical English | passive reading vs speaking/writing for engineering work | reading, writing, spoken/self-recorded explanation |
| `agentic-development` | Codex / Claude / coding agents | prompt use vs delegation/review/validation discipline | HYBRID repository task |
| `llm-ai-engineering` | LLM / AI engineering | product familiarity vs backend integration fundamentals | concept explanation, system scenario |

## Evidence rules

- Every domain uses at least two evidence types where practical.
- A correct implementation with a weak explanation is not treated as full mastery.
- AI-assisted success does not erase a SOLO knowledge gap.
- Confidence self-report is recorded separately from demonstrated evidence.
- The learner may mark a technology as “never used”; the diagnostic then tests prerequisites rather than forcing advanced tasks.

## Proposed 6-day schedule

### Day 1 — Language, design, dependency management, Git — 130 min
- Profile/self-assessment: 15 min
- PHP language/runtime: 35 min — `SOLO`
- OOP/SOLID/design reasoning: 30 min — `SOLO`
- Composer: 20 min — `SOLO`
- Git/GitHub scenario: 30 min — `SOLO`

### Day 2 — Data layer — 135 min
- MySQL modeling/SQL: 35 min — `SOLO`
- Indexing + EXPLAIN reasoning: 35 min — `SOLO`
- Transactions/locking concepts: 25 min — `SOLO`
- Redis/caching/data structures: 40 min — `SOLO`

### Day 3 — Web engineering and quality — 140 min
- HTTP request/response analysis: 30 min — `SOLO`
- API/security scenario: 30 min — `SOLO`
- Testing/static analysis task: 35 min — `HYBRID`
- Linux/network troubleshooting: 25 min — `SOLO`
- Technical English written explanation: 20 min — `SOLO`

### Day 4 — Frameworks, containers, delivery — 145 min
- CakePHP depth/debugging: 40 min — `SOLO`
- Laravel transfer/familiarity: 20 min — `SOLO`
- Docker troubleshooting: 30 min — `SOLO`
- AWS/cloud architecture fundamentals: 30 min — `SOLO`
- CI/CD pipeline review: 25 min — `SOLO`

### Day 5 — Architecture, algorithms, communication — 135 min
- System design scenario: 45 min — `SOLO`
- Algorithms/data structures: 35 min — `SOLO`
- English technical reading: 20 min — `SOLO`
- English spoken/self-recorded explanation: 20 min — `SOLO`
- Reflection/confidence calibration: 15 min

### Day 6 — Agentic development and AI engineering — 140 min
- Repository task with Codex or Claude Code: 50 min — `HYBRID`
- Review generated diff and identify risks: 25 min — `SOLO`
- Explain accepted/rejected agent changes: 20 min — `SOLO`
- LLM/API/tool-calling concepts: 25 min — `SOLO`
- AI system design mini-scenario: 20 min — `SOLO`

### Optional Day 7 — Initialization and review — up to 90 min
- Initialize `.study/` repository.
- Store diagnostic evidence privately.
- Review detected gaps.
- Produce the initial Week 1–4 private adaptation.
- No extra graded content.

## Required diagnostic artifacts

The completed Week 0 must eventually produce private records for:

```yaml
skill_state:
  <skill-id>:
    demonstrated_score: 0
    confidence_self_report: 0
    study_priority: normal
    evidence: []
    recommended_entry_depth: foundation
```

The exact score calculation is deferred to the scoring checkpoint. `demonstrated_score` remains a schema placeholder until that model is approved.

## Entry-depth vocabulary

- `foundation` — conceptual gaps require explicit reconstruction.
- `standard` — normal roadmap depth.
- `accelerated` — evidence supports reduced repetition, but mandatory gates remain.
- `recovery` — prerequisites must be remediated before dependent advanced work.

## Week 0 output

The diagnostic should generate, privately:

1. skill-state baseline;
2. confidence-vs-evidence mismatches;
3. active high-priority gaps;
4. recommended entry depth by topic;
5. initial D+1 / D+7 review events for diagnostic errors;
6. initial private adaptation for Weeks 1–4;
7. English baseline observations;
8. SOLO vs AI-assisted capability baseline;
9. no edits to the public 52-week curriculum.

## C1-A acceptance criteria

- All required domains are covered.
- No required day exceeds 150 minutes.
- Closed SOLO evidence exists.
- HYBRID/AI-assisted evidence exists.
- English is observed across multiple tasks.
- Framework familiarity is not treated as equivalent to engineering mastery.
- The blueprint does not expose final diagnostic questions or answer keys.
