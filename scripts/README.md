# Repository Validator

`scripts/validate_repo.py` performs deterministic static checks over the public roadmap repository.

It does **not** grade learner work, mutate files, fetch the network, or inspect ignored private `.study/` state.

## Run locally

From the repository root:

```bash
python scripts/validate_repo.py
```

Expected success:

```text
Validation passed: 0 errors.
```

Validation failures print one line per issue and exit with status `1`:

```text
[BROKEN_LINK] path/file.md:12: internal link target does not resolve: missing.md
Validation failed: 1 error(s).
```

Invalid CLI/root usage exits with status `2`.

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The fixtures under `tests/fixtures/` intentionally contain invalid repository fragments. The main repository validator ignores this fixture directory when validating the real repository.

## Checks

### Public/private boundary

- tracked/public `.study/` files are rejected;
- prose may document `.study/`;
- public Markdown links into `.study/` are rejected;
- only `.obsidian/templates.json` may be public under `.obsidian/`.

### Frontmatter and enums

For known content types, required top-level frontmatter keys are checked.

Study modes:

```text
SOLO
HYBRID
AI-ASSISTED
```

Technology depth:

```text
core
supporting
professional-exposure
market-triggered
```

### Canonical IDs

The validator detects duplicates across:

- public frontmatter `id`;
- resource catalog IDs;
- diagnostic question IDs.

Template placeholders such as `{{assessment_id}}` are excluded.

### Resources

`09 Resources/catalog.yaml` entries require:

- a canonical `id`;
- `last_verified` with an ISO `YYYY-MM-DD` date.

Technology depth is also validated.

Daily-plan `resource_ids` must resolve to the catalog.

The validator does not make live HTTP requests; freshness/content review remains a human/release activity.

### Week 0 Question Bank

- diagnostic question IDs must be unique;
- Week 0 day references must resolve;
- `answer_key_public: true` is rejected;
- public `## Solution` / `## Answer Key` headings are rejected.

### Historical assessment integrity

Assessment-style templates must contain separate:

```text
## Raw attempt
## Feedback
```

sections.

This is a structural safeguard only; immutability is still enforced by agent rules and Git history.

### Internal Markdown links

The validator checks statically resolvable:

- standard Markdown links;
- Obsidian `[[wikilinks]]`.

It ignores:

- external URLs;
- anchor-only links;
- fenced code examples;
- dynamic template targets.

For basename-only Obsidian links with multiple possible matches, the validator does not guess.

## Design constraints

The validator intentionally uses the Python standard library only.

It validates stable repository invariants, not stylistic preferences. New checks should be added only when they protect an approved invariant and have a failing fixture/test first.
