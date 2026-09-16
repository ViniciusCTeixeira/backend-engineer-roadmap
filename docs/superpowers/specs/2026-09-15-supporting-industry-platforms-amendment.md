# Supporting / Industry Platforms — C1 Amendment

**Status:** Approved direction; implementation amendment before C2  
**Date:** 2026-09-15  
**Applies to:** Adaptive Backend Engineer Roadmap V1

## Decision

Add **Supporting / Industry Platforms** as the seventh transversal Year 1 track.

The roadmap must teach concepts first and use real industry tools to make those concepts concrete. It must not become a logo checklist or require deep mastery of every vendor product.

## Technology depth classes

### CORE
Technologies the learner must understand deeply enough to design, implement, debug, explain trade-offs, and use independently.

Current V1 core remains centered on:
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
- CI/CD
- system design/distributed systems
- testing/static analysis
- AI-assisted engineering and AI engineering

### SUPPORTING
Technologies the learner must use in realistic practical exercises and understand well enough to operate/debug in normal backend work.

Initial V1 set:
- Nginx
- Cloudflare
- OpenAPI / Swagger
- Bruno or Postman
- Xdebug
- k6
- OpenTelemetry
- Prometheus
- Grafana
- Sentry
- GitHub CLI
- AWS CLI
- command-line tools such as curl, jq, dig, ss/lsof
- messaging ecosystem comparison/practice: SQS plus RabbitMQ/Kafka where appropriate

### PROFESSIONAL EXPOSURE
Technologies the learner should understand, run in a small lab where useful, and be able to discuss in an interview, without requiring production-level mastery in Year 1.

Initial V1 set:
- Kubernetes
- Helm
- Kafka or RabbitMQ not selected for the deeper messaging lab
- OpenSearch / Elasticsearch
- SonarQube
- Trivy
- HashiCorp Vault concepts
- Datadog / New Relic concepts
- GitOps / Argo CD concepts

### MARKET-TRIGGERED
Technologies are promoted only when recurring evidence from relevant vacancies/interviews justifies additional depth.

Examples may include:
- Backstage
- specific APM vendors
- alternative brokers
- alternative cloud services
- organization-specific developer platforms

A single vacancy must never promote a technology in the public curriculum.

## Selection rule

A platform belongs in the roadmap only if it satisfies most of these:

1. It solves a recurring backend/production engineering problem.
2. It teaches a transferable concept.
3. It appears meaningfully in real engineering environments or target vacancies.
4. It can be practiced without displacing foundational depth.
5. The roadmap does not already teach the same lesson adequately with another tool.
6. Its required depth can be explicitly classified.

## Year 1 transversal tracks

1. Core Backend Engineering
2. Supporting / Industry Platforms
3. English
4. AI-Assisted Development / AI Engineering
5. Project
6. Review & Assessment
7. Career

## Initial week integration

| Week | Industry platform integration |
|---|---|
| 4 | Xdebug as a practical debugging tool |
| 7 | curl, jq, dig, ss/lsof in Linux/network troubleshooting |
| 8 | GitHub CLI exposure in repository workflow |
| 14 | OpenAPI/Swagger + Bruno or Postman for API inspection/contracts |
| 16 | quality-tooling context; keep PHPStan/PHPUnit core |
| 22 | Docker Compose as part of container workflow |
| 23 | Nginx as reverse proxy in front of PHP-FPM |
| 24 | k6 for basic API load/performance testing |
| 25 | Cloudflare DNS/CDN/TLS/reverse-proxy fundamentals; AWS CLI |
| 28 | SQS as core queue; compare RabbitMQ and Kafka and perform one bounded lab based on project fit |
| 29 | SonarQube/quality-gate concepts and Trivy/container/dependency scanning exposure |
| 30 | OpenTelemetry + Prometheus + Grafana; Sentry as error-monitoring practice; Datadog/New Relic as commercial equivalents |
| 31 | Terraform may manage selected Cloudflare/AWS resources; Vault concepts alongside secrets management |
| 32 | Cloudflare WAF/rate limiting/origin protection; Kubernetes + Helm professional exposure; GitOps/Argo CD concepts |
| 33 | k6/capacity measurements support scaling exercises |
| 34 | OpenSearch/Elasticsearch exposure when discussing search/indexing/data-access trade-offs |
| 35 | messaging platform trade-offs revisited in reliability/event-driven design |
| 46 | MCP remains part of Agentic Engineering; supporting platforms may be exposed through bounded tools when useful |

This table defines intended integration points, not additional full subjects. Daily workload must remain within the configured weekly-hour ceiling.

## Matrix schema change

Each week entry in `01 Curriculum/year-1-matrix.yaml` gains:

```yaml
industry_platforms: []
```

Only relevant tools are listed. Empty weeks are valid when the week intentionally focuses on core concepts.

Example:

```yaml
week: 30
core_topics:
  - structured logging
  - metrics
  - tracing
industry_platforms:
  - opentelemetry
  - prometheus
  - grafana
  - sentry
```

## Resource catalog change

Resource metadata gains:

```yaml
technology_depth: supporting
```

Allowed values:

```text
core
supporting
professional-exposure
market-triggered
```

## Agent governance

Agents may:
- update stale resources for an already-approved platform;
- suggest practice improvements within existing depth.

Agents must create a proposal before:
- adding a new public platform;
- promoting/demoting a platform's depth;
- replacing a primary platform;
- materially increasing total curriculum workload.

Market evidence must be aggregated across a meaningful sample before a public promotion proposal.

## Project principle

Supporting tools should appear inside normal backend engineering workflows.

Examples:

```text
Client
  ↓
Cloudflare
  ↓
Nginx / AWS Load Balancer
  ↓
Laravel/PHP
  ├── MySQL
  ├── Redis
  └── Queue

Application
  ↓
OpenTelemetry
  ├── Prometheus/Grafana
  └── traces/logs
```

The learner must be able to explain the concept without relying on the vendor name.

## C1 amendment acceptance criteria

- The seventh track exists in human- and machine-readable curriculum artifacts.
- Supporting tools are mapped to concepts rather than added as isolated courses.
- AWS remains the primary cloud platform.
- Cloudflare is explicitly complementary edge/DNS/CDN/security infrastructure.
- Kubernetes is exposure-level in V1 unless market evidence promotes it.
- Messaging teaches models/trade-offs, not mandatory mastery of all brokers.
- New tools cannot be added automatically from a single vacancy.
- Default 12-hour/week workload remains unchanged.
