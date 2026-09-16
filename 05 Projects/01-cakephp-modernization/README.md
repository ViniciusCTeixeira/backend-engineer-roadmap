# Project A — CakePHP Modernization Lab

## Scenario

You inherited a synthetic CakePHP backend that works but has weak tests, mixed responsibilities, implicit framework conventions, inefficient queries, fragile caching, and poor operational documentation.

Your task is not to rewrite it from scratch.

Your task is to make it safer to understand, change, test, debug, and operate.

## Non-goals

- framework rewrite for its own sake;
- microservices decomposition;
- adding every modern pattern;
- hiding legacy constraints behind generated code.

## Required outcomes

### Baseline
- reproducible run instructions;
- system/context diagram;
- framework/runtime inventory;
- initial risk list.

### Behavior protection
- characterization tests around risky behavior;
- unit/integration tests where boundaries permit;
- clear statement of untested risk.

### PHP/design modernization
- stronger type usage where appropriate;
- dependency boundaries;
- reduced hidden coupling;
- PHPStan baseline/improvement;
- ADR for one meaningful refactor.

### Database
- identify slow/fragile access patterns;
- use `EXPLAIN`/`EXPLAIN ANALYZE`;
- justify indexes;
- demonstrate a transaction/concurrency scenario.

### Redis
- justify data type and TTL;
- define invalidation;
- discuss persistence/eviction implications;
- test failure/stale-data behavior.

### Runtime
- Dockerized local environment;
- Nginx/PHP-FPM topology;
- health/troubleshooting commands;
- logs/runbook.

### Final case study
- original problem;
- constraints;
- changes;
- measurements;
- trade-offs;
- what remains;
- lessons transferable to other frameworks.

## Evidence rule

Each major change should answer:

1. What problem existed?
2. What evidence showed it?
3. What did you change?
4. How did you validate it?
5. What trade-off did you accept?
