---
type: daily-plan
schema_version: 1
id: task-w25-d03-v1-1
week: 25
day: 3
date: null
track: core
skill_ids:
- aws
- iam
- vpc
- multi-service-networking
mode: SOLO
estimated_minutes: 105
technology_depth: core
resource_ids:
- cloudflare-dns
- cloudflare-cache
deliverables:
- edge-to-origin trace
- cache/TLS responsibility note
review_policy: adaptive
prerequisites:
- week-24
status: planned
---

# Day 03 — Trace Cloudflare DNS/CDN/TLS to the AWS Origin

## Outcome

> Separate DNS, proxy/CDN, TLS, load-balancer, and application responsibilities for the public path.

## Timebox

| Block | Mode | Minutes |
|---|---|---:|
| Primary-source study | `SOLO` | 20 |
| Hands-on lab | `SOLO` | 40 |
| Project/evidence update | `SOLO` | 15 |
| Technical English | `SOLO` | 10 |
| Daily assessment | `SOLO` | 20 |
| **Total** |  | **105** |

## Resources

- `cloudflare-dns`
- `cloudflare-cache`

## Activities

### Primary-source study — 20 min — `SOLO`

Read only the sections required for the day's reasoning.

### Hands-on lab — 40 min — `SOLO`

Separate DNS, proxy/CDN, TLS, load-balancer, and application responsibilities for the public path.

### Project/evidence update — 15 min — `SOLO`

Connect the result to Project B or preserve reproducible standalone evidence.

### Technical English — 10 min — `SOLO`

Explain one decision/assumption/failure mode in English.

### Daily assessment — 20 min — `SOLO`

Complete the scored transfer prompt without assistance.

## Deliverables

- edge-to-origin trace
- cache/TLS responsibility note

## Daily assessment

Run `02 Daily Assessments/Week 25/Day 03.md`. Store attempts privately.

## Review hook

Create D+1/D+7 reviews from demonstrated errors and D+30 transfer review where justified.

## AI integrity

Scored attempts are SOLO. HYBRID work preserves independent evidence before agent use.

## Completion rule

Required evidence must exist; reading or agent conversation alone is not completion.
