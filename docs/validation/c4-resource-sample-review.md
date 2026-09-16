# C4 Resource Sample Review

**Date:** 2026-09-15  
**Scope:** At least one representative unit from each Year 1 macro phase.

## Phase 1 — Foundations

Sample:
- PHP Manual — Types
- Composer Basic Usage / schema
- Pro Git
- CakePHP 5 ORM/testing
- PHPStan

Result: PASS

Why:
- primary/official sources;
- free;
- directly aligned to Weeks 1–8;
- PHP support lifecycle is separately tracked instead of freezing the roadmap to an obsolete version.

## Phase 2 — Data and Web

Sample:
- MySQL 8.4 Reference Manual
- Redis data types/persistence/eviction
- OpenAPI specification

Result: PASS

Why:
- MySQL reference explicitly covers 8.4 LTS;
- Redis sources cover behavior needed for cache/data-structure decisions;
- OpenAPI is a supporting contract/specification tool, not a replacement for HTTP understanding.

## Phase 3 — Modern Backend

Sample:
- Laravel current documentation
- Docker Get Started
- NGINX Beginner's Guide

Result: PASS

Why:
- current Laravel documentation verified as 13.x;
- Docker/Nginx are official, practical, and map directly to project runtime milestones;
- CakePHP remains in Project A while Laravel becomes the modern Project B framework.

## Phase 4 — Cloud and Delivery

Sample:
- AWS IAM/VPC/RDS/SQS/CloudWatch
- GitHub Actions
- Terraform AWS tutorials
- OpenTelemetry PHP / Prometheus / Grafana

Result: PASS

Why:
- official primary sources;
- AWS remains core cloud;
- Terraform tutorials are hands-on;
- OpenTelemetry provides vendor-neutral instrumentation while CloudWatch remains relevant to AWS.

## Phase 5 — Architecture and AI

Sample:
- Amazon Builders' Library
- OpenAI developer docs/API references
- MCP 2026-07-28 specification release

Result: PASS WITH FRESHNESS CONDITION

Why:
- Builders' Library provides real-world distributed-systems articles;
- AI platform docs are fast-moving and therefore must be re-verified at use time;
- curriculum should teach durable concepts and avoid baking transient model names/prices into permanent lessons.

## Phase 6 — Interviews / Advanced Work

Primary sources are the accumulated core references plus assessment/project evidence, rather than a separate interview-trivia resource.

Result: PASS

Reason:
- interview preparation should reconstruct core knowledge and practice explanation/problem solving;
- public question banks and mock interviews are authored from approved curriculum rather than copied from proprietary interview banks.

## Phase 7 — Market Campaign

Resources are job postings/interview evidence stored privately and analyzed by the career workflow.

Result: PASS

Reason:
- this phase is evidence-driven and should not depend on a static public list of companies/questions.

## Supporting / Industry Platforms sample

Verified:
- Cloudflare DNS/cache/WAF/Workers/Terraform;
- k6;
- Kubernetes basics;
- Helm;
- RabbitMQ;
- Kafka;
- OpenSearch;
- Trivy.

Depth labels match the approved C1 amendment.

## Deferred catalog items

Do not add a resource merely because a platform appears in the Supporting list.

Examples such as commercial APM/quality platforms can be added when:
- an official high-quality resource is verified;
- the exact curriculum use is defined;
- it does not displace core learning.

## Conclusion

C4-B sample quality gate: PASS.

Full resource audit is still required before public release and before generated daily content relies on fast-moving resources.
