---
type: daily-plan
schema_version: 1
id: task-w07-d02-linux-operations-and-network-troubleshooting
week: 7
day: 2
date: null
track: core
skill_ids:
- linux-processes
- signals
- procfs
- runtime-observability
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- linux-proc-manpage
- php-fpm-manual
deliverables:
- process evidence table
- FPM process connection note
- incident-state distinctions
review_policy: adaptive
prerequisites:
- week-06
status: planned
---

# Day 02 — Inspect Processes, Signals, and Runtime State

## Outcome

> Operate comfortably in Linux and troubleshoot PHP service failures through processes, files, permissions, ports, DNS, HTTP evidence, and logs.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Process model reading | `SOLO` | 20 |
| Process inspection lab | `SOLO` | 35 |
| FPM connection | `SOLO` | 20 |
| Incident note | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `linux-proc-manpage`
- `php-fpm-manual`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Process model reading — 20 min — `SOLO`

Study `/proc`, PID/PPID, signals, descriptors, and process-owned runtime state.

### Process inspection lab — 35 min — `SOLO`

Start safe sandbox processes, inspect PID/PPID/cmdline/open descriptors, then terminate with appropriate signals.

### FPM connection — 20 min — `SOLO`

Relate process observations back to FPM parent/worker concepts.

### Incident note — 10 min — `SOLO`

Distinguish crashed, stuck, saturated, and idle process evidence.

### Daily micro-assessment — 20 min — `SOLO`

Complete the process/signal assessment.

## Deliverables

- process evidence table
- FPM process connection note
- incident-state distinctions

## Daily assessment

Run `02 Daily Assessments/Week 07/Day 02.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
