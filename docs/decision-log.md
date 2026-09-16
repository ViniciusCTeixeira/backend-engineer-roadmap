# V1 Decision Log

This log records architectural decisions locked for V1. Changes to these decisions require an explicit review of the approved design specification.

## Locked decisions

1. **Public core plus private nested state** — The public repository contains the reusable curriculum product. Learner-specific state lives in a separate nested `.study/` repository and is ignored by the public repository.
2. **No submodule** — `.study/` is an independent nested Git repository, not a Git submodule.
3. **English-first public repository** — Public repository content is primarily written in English.
4. **PHP-experienced V1 target** — V1 is designed for an experienced PHP developer progressing toward Senior Backend Engineer / Senior Software Engineer — Backend.
5. **Obsidian + Markdown + Git** — Obsidian remains the primary human interface, with Markdown and Git as the core storage/versioning mechanisms; V1 does not become a custom application.
6. **AI is mandatory** — AI-assisted development and building AI-enabled systems are first-class, mandatory tracks rather than optional appendices.
7. **Immutable historical evidence** — Raw assessment attempts, scores, errors, interview notes, and other historical learner evidence are preserved and never silently overwritten.
8. **Proposal-first curriculum governance** — Substantial public curriculum changes require a reviewable proposal; one learner result or one job posting does not automatically rewrite the public curriculum.
9. **First-year professional outcome** — The first-year goal includes obtaining a stronger job, not merely finishing the study plan.
10. **Readiness-based US campaign** — The US relocation/sponsorship campaign begins after approximately one year of consolidation at the stronger professional level, triggered by readiness milestones rather than a hard calendar date.
11. **Supporting / Industry Platforms track** — Year 1 has seven transversal tracks, adding Supporting / Industry Platforms alongside Core Backend Engineering, English, AI-Assisted Development / AI Engineering, Project, Review & Assessment, and Career.
12. **Technology depth classification** — Every platform is classified as `core`, `supporting`, `professional-exposure`, or `market-triggered`; additions or depth changes follow proposal-first governance and must not displace foundational depth or the default 12-hour weekly workload.
