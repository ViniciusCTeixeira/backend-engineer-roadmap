---
type: daily-plan
schema_version: 1
id: task-w07-d04-linux-operations-and-network-troubleshooting
week: 7
day: 4
date: null
track: core
skill_ids:
- dns
- sockets
- ports
- curl
- dig
- ss
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- bind9-dig-manpage
- linux-ss-manpage
- curl-manpage
deliverables:
- DNS/socket/HTTP evidence table
- failure localization
- English network narration
review_policy: adaptive
prerequisites:
- week-06
status: planned
---

# Day 04 — Trace DNS, Ports, Sockets, and HTTP With dig, ss, and curl

## Outcome

> Operate comfortably in Linux and troubleshoot PHP service failures through processes, files, permissions, ports, DNS, HTTP evidence, and logs.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Network-tool reading | `SOLO` | 20 |
| Layered troubleshooting lab | `SOLO` | 40 |
| Failure localization | `SOLO` | 15 |
| English narration | `SOLO` | 10 |
| Daily micro-assessment | `SOLO` | 20 |
| **Total** |  | **105** |

Assessment time is included in this total.

## Resources

- `bind9-dig-manpage`
- `linux-ss-manpage`
- `curl-manpage`

Resource IDs resolve through `09 Resources/catalog.yaml`.

## Activities

### Network-tool reading — 20 min — `SOLO`

Review `dig`, `ss`, and `curl`; focus on what evidence each can and cannot provide.

### Layered troubleshooting lab — 40 min — `SOLO`

Capture DNS, socket/connection, HTTP status/header/timing evidence with a stated hypothesis before each command.

### Failure localization — 15 min — `SOLO`

Classify synthetic failures as name resolution, listening socket, transport, HTTP server, or application.

### English narration — 10 min — `SOLO`

Narrate the troubleshooting layers in English.

### Daily micro-assessment — 20 min — `SOLO`

Complete the network-evidence assessment.

## Deliverables

- DNS/socket/HTTP evidence table
- failure localization
- English network narration

## Daily assessment

Run `02 Daily Assessments/Week 07/Day 04.md`. Store learner attempts privately.

## Review hook

Create D+1/D+7 review events from demonstrated errors; add D+30 transfer review when justified.

## AI integrity

SOLO work remains independent evidence. HYBRID/AI-assisted work must preserve pre-agent evidence and independently validate consequential claims.

## Completion rule

Reading or agent conversation alone is not completion; required evidence must exist.
