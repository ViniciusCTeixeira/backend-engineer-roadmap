---
type: daily-plan
schema_version: 1
id: task-w05-d03-php-runtime-and-fpm
week: 5
day: 3
date: null
track: core
skill_ids:
- web-request-lifecycle
- fastcgi
- nginx
- runtime-routing
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- nginx-beginners-guide
- php-fpm-manual
deliverables:
- request-path diagram
- three-case diagnosis
- Project A lifecycle map increment
review_policy: adaptive
prerequisites:
- week-04
status: planned
---

# Day 03 — Trace Web Server to FastCGI to PHP Application

## Outcome

> Understand the PHP web runtime from request arrival through FPM/process execution, configuration, Composer bootstrap, and application response.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Request-path reading | `SOLO` | 20 |
| Trace construction | `SOLO` | 35 |
| Misconfiguration diagnosis | `SOLO` | 20 |
| Project lifecycle map | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `nginx-beginners-guide`
- `php-fpm-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Request-path reading — 20 min — `SOLO`

Read FastCGI/Nginx and FPM references with focus on component boundaries.

### Trace construction — 35 min — `SOLO`

Draw a path from HTTP server through FastCGI/FPM, PHP entry point, framework bootstrap, action, and response.

### Misconfiguration diagnosis — 20 min — `SOLO`

Diagnose synthetic wrong-socket, wrong-script-path, and missing-front-controller cases.

### Project lifecycle map — 10 min — `SOLO`

Add evidence-backed runtime steps to `legacy-runtime-map`.

### Daily micro-assessment — 20 min — `SOLO`

Complete the request-path assessment.

## Deliverables

- request-path diagram
- three-case diagnosis
- Project A lifecycle map increment

## Daily assessment

Run `02 Daily Assessments/Week 05/Day 03.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
