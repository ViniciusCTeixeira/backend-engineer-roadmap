# Resource Policy — C4-B

**Last policy review:** 2026-09-15

## Purpose

Keep the roadmap's learning material high-signal, current, and maintainable without collecting hundreds of links.

## Source priority

Prefer, in order:

1. official documentation / specifications;
2. official free training/tutorials;
3. university or respected open-source educational material;
4. high-quality community material;
5. paid material only when materially better and the free path remains complete.

## Resource metadata

Every catalog item records:

```yaml
id: ""
title: ""
url: ""
topic_ids: []
type: docs
source_authority: official
language: en
cost: free
last_verified: YYYY-MM-DD
version_scope: ""
technology_depth: core
notes: ""
```

Allowed `technology_depth`:

```text
core
supporting
professional-exposure
market-triggered
```

## Curation rule

Do not collect resources for hypothetical future topics.

Curate in curriculum order and prefer:
- one primary authoritative source;
- one practical/tutorial source when the primary source is reference-heavy.

A single excellent source may serve both roles.

## Version policy

Version-pin only when version differences materially affect the lesson.

Examples:
- MySQL 8.4 LTS reference may be version-scoped.
- Laravel framework docs should record the current major used by the project.
- durable HTTP/system-design concepts should not be coupled unnecessarily to one product version.

## Fast-moving topics

Re-verify more frequently:

- Codex / Claude Code;
- OpenAI / Anthropic APIs;
- MCP;
- AI models/SDKs;
- AWS product guidance;
- Cloudflare;
- Kubernetes/Helm;
- PHP/Laravel current supported versions;
- CI actions/toolchain versions.

Do not hard-code model prices, limits, or transient aliases into durable curriculum text unless dated/versioned.

## Link maintenance

An agent may autonomously repair a broken URL only when:
- the replacement is clearly the same official resource;
- lesson meaning does not change;
- `last_verified` is updated.

Major resource replacement is proposal-required.

## Cost policy

The complete V1 path must remain possible with free resources, excluding unavoidable optional infrastructure usage.

Paid resources are supplements, never prerequisites.

## Language

English is preferred when the official source is strongest and the material contributes to technical-English practice.

Portuguese official translations may be listed as a complement.

## Hands-on requirement

Reading alone is insufficient.

A resource is attached to a task only when the task defines what the learner must do with it:
- explain;
- experiment;
- implement;
- diagnose;
- benchmark;
- compare;
- review.

## AI/resource use

Coding agents may summarize or help navigate resources, but learners should still read primary sections directly for critical concepts and verify fast-moving vendor facts.

## Audit cadence

Suggested:
- fast-moving resources: at least quarterly or when used;
- stable official references: at least annually or when a link/version changes;
- before public release: full catalog link/freshness audit.

## C4-B quality bar

The catalog is acceptable when:
- every macro phase has verified primary resources;
- resources match the approved matrix;
- supporting platforms are clearly depth-labeled;
- no paid resource is required;
- fast-moving sources have recent verification dates.
