# Job Analysis Method

Use this method for one vacancy at a time. Store the completed analysis privately under `.study/career/jobs/` using `90 Templates/job-analysis.md`.

## 1. Preserve the source

Record capture date/time, role title, company identity privately, location model, source reference, and active/inactive status when checked.

Do not copy private recruiter correspondence into public files.

## 2. Separate facts from interpretation

Create four categories.

### Explicit requirements

Items stated as required.

### Explicit preferences

Items stated as preferred or nice-to-have.

### Role signals

Reasonable observations from the text, such as backend/data depth, production ownership, cloud maturity, English usage, or architectural expectations.

Mark these as interpretation rather than hard requirements.

### Unknowns

Important information not present in the posting.

Do not infer employer practices, sponsorship, salary, culture, interview process, or technology usage when the source does not establish them.

## 3. Map requirements to demonstrated evidence

Classify each important requirement:

```text
demonstrated
in-progress
missing
uncertain
```

`demonstrated` requires evidence such as roadmap assessments, Project A/Project B artifacts, public-safe portfolio evidence, or professional experience that can be explained concretely.

## 4. Classify interview risk

Use relevant categories:

- PHP/runtime;
- OOP/design;
- SQL/data modeling/performance;
- Redis/caching;
- HTTP/API/security;
- testing/static analysis;
- Linux/networking;
- Docker/runtime;
- AWS/cloud;
- CI/CD;
- queues/distributed systems;
- observability;
- system design;
- algorithms/coding;
- English communication;
- behavioral/impact;
- AI-assisted development;
- AI engineering.

Prioritize by relevance to the role and evidence gap.

## 5. Evaluate employer-quality signals

Review dimensions from `role-target.md`.

Use:

```text
positive signal
neutral/unknown
question to investigate
```

Avoid a simplistic employer score.

## 6. Decide private preparation

A single vacancy may create a short interview-preparation task, targeted review, company-specific research task, or private project-evidence reminder.

It must not automatically create months of new study.

## 7. Application decision

The learner makes the application decision.

Useful private considerations include role relevance, evidence fit, growth opportunity, workload/location constraints, compensation/benefits when known, timing, and personal priorities.

The roadmap does not require 100% match before applying.

## 8. Market-signal contribution

Record structured signals for later aggregation.

```yaml
market_signals:
  php: required
  laravel: required
  aws: required
  kubernetes: preferred
  system_design: inferred-senior-scope
```

One observation is not a curriculum signal.

## 9. Public curriculum threshold

A public proposal may be considered only after a meaningful sample shows a recurring relevant pattern.

Record:

- sample size;
- date window;
- role family;
- geography/location model when relevant;
- required vs preferred frequency;
- existing curriculum coverage;
- workload impact.

Even then, create a proposal rather than directly editing curriculum.

## 10. Freshness rule

Current public claims about a company, vacancy, salary, relocation, sponsorship, benefits, technologies, or hiring process must be verified from current sources.

Historical/private records retain their original capture date.
