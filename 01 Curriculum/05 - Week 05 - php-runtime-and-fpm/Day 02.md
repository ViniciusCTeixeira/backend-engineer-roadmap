---
type: daily-plan
schema_version: 1
id: task-w05-d02-php-runtime-and-fpm
week: 5
day: 2
date: null
track: core
skill_ids:
- php-fpm
- process-management
- runtime-capacity
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- php-fpm-manual
deliverables:
- FPM pool annotated note
- capacity assumptions
- failure-mode checklist
review_policy: adaptive
prerequisites:
- week-04
status: planned
---

# Day 02 — Reason About PHP-FPM Pools and Process Management

## Outcome

> Understand the PHP web runtime from request arrival through FPM/process execution, configuration, Composer bootstrap, and application response.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| FPM configuration reading | `SOLO` | 20 |
| Capacity thought experiment | `SOLO` | 35 |
| Config inspection | `SOLO` | 20 |
| Failure-mode note | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `php-fpm-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### FPM configuration reading — 20 min — `SOLO`

Study pools, listen endpoints, process-management modes, limits, logs, status and slowlog concepts.

### Capacity thought experiment — 35 min — `SOLO`

Given synthetic request duration/memory numbers, reason about worker concurrency and what pm.max_children constrains. State assumptions.

### Config inspection — 20 min — `SOLO`

Inspect safe read-only FPM config/status evidence when available, otherwise annotate a synthetic pool configuration.

### Failure-mode note — 10 min — `SOLO`

List signals for worker exhaustion, wrong ownership/permissions, and a wrong listen target.

### Daily micro-assessment — 20 min — `SOLO`

Complete the FPM process-model assessment.

## Deliverables

- FPM pool annotated note
- capacity assumptions
- failure-mode checklist

## Daily assessment

Run `02 Daily Assessments/Week 05/Day 02.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
