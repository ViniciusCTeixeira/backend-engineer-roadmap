#!/usr/bin/env python3
"""Static repository validator for the Adaptive Backend Engineer Roadmap.

Standard-library only by design. It validates repository invariants that are
deterministic from the public tree; it does not grade learner work or mutate files.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import unquote
import argparse
import re
import subprocess
import sys

ALLOWED_MODES = {"SOLO", "HYBRID", "AI-ASSISTED"}
ALLOWED_TECHNOLOGY_DEPTHS = {
    "core",
    "supporting",
    "professional-exposure",
    "market-triggered",
}

REQUIRED_KEYS_BY_TYPE = {
    "daily-plan": {
        "schema_version", "id", "week", "day", "track", "skill_ids", "mode",
        "estimated_minutes", "resource_ids", "deliverables", "review_policy", "status",
    },
    "assessment": {
        "schema_version", "id", "week", "assessment_type", "mode", "skill_ids", "status",
    },
    "weekly-simulation": {
        "schema_version", "id", "week", "mode", "simulation_type",
        "skill_ids", "estimated_minutes", "status",
    },
    "diagnostic-day": {
        "schema_version", "day", "required", "estimated_minutes", "domains", "status",
    },
    "question-bank": {
        "schema_version", "bank", "domain", "question_ids", "answer_key_public",
    },
    "diagnostic-result": {
        "schema_version", "id", "assessment_type", "mode", "status",
    },
}

HISTORICAL_TEMPLATE_TYPES = {"assessment", "weekly-simulation", "diagnostic-result"}
IGNORED_PREFIXES = (
    "tests/fixtures/",
    ".git/",
    "__pycache__/",
)
EXTERNAL_SCHEMES = (
    "http://", "https://", "mailto:", "tel:", "data:", "obsidian:",
)

@dataclass(frozen=True)
class ValidationError:
    code: str
    path: str
    message: str
    line: int | None = None

    def render(self) -> str:
        location = self.path
        if self.line is not None:
            location += f":{self.line}"
        return f"[{self.code}] {location}: {self.message}"


def _norm_rel(path: Path) -> str:
    value = path.as_posix()
    return value[2:] if value.startswith("./") else value


def _is_ignored(rel: str) -> bool:
    return any(rel.startswith(prefix) for prefix in IGNORED_PREFIXES)


def repository_files(root: Path) -> list[Path]:
    """Return tracked + nonignored untracked public files.

    In a real checkout, Git is authoritative so ignored local `.study/` and Obsidian
    state never enter validation. For standalone test fixtures, walk the directory.
    """
    root = root.resolve()
    git_marker = root / ".git"
    if git_marker.exists():
        proc = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            capture_output=True,
            text=False,
        )
        if proc.returncode == 0:
            out = []
            for raw in proc.stdout.split(b"\0"):
                if not raw:
                    continue
                rel = raw.decode("utf-8", errors="strict")
                if _is_ignored(rel):
                    continue
                p = root / rel
                if p.is_file():
                    out.append(p)
            return sorted(set(out))

    out = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = _norm_rel(p.relative_to(root))
        if _is_ignored(rel):
            continue
        out.append(p)
    return sorted(out)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def parse_scalar(raw: str):
    value = raw.strip()
    if not value:
        return None
    if value in {"[]", "{}"}:
        return [] if value == "[]" else {}
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "~"}:
        return None
    if ((value.startswith('"') and value.endswith('"')) or
        (value.startswith("'") and value.endswith("'"))):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            pass
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return value


def parse_frontmatter(text: str) -> tuple[dict, int]:
    """Parse enough YAML frontmatter for repository invariants.

    We intentionally parse only top-level scalar/list keys. Nested mappings are
    represented as `{}` because the validator currently checks their presence only.
    """
    if not text.startswith("---"):
        return {}, 0
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, 0

    fm: dict = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith((" ", "\t", "- ")):
            i += 1
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not match:
            i += 1
            continue
        key, raw_value = match.group(1), match.group(2) or ""
        if raw_value.strip():
            fm[key] = parse_scalar(raw_value)
            i += 1
            continue

        # Empty top-level value: recognize a following YAML list. Otherwise keep
        # an empty mapping-like marker; required-key checks care about presence.
        items = []
        j = i + 1
        while j < end:
            next_line = lines[j]
            if re.match(r"^[A-Za-z0-9_-]+:", next_line):
                break
            m_item = re.match(r"^\s*-\s+(.*)$", next_line)
            if m_item:
                items.append(parse_scalar(m_item.group(1)))
            elif next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            j += 1
        fm[key] = items if items else {}
        i = j
    return fm, end + 1


def strip_fenced_code(text: str) -> str:
    kept = []
    in_fence = False
    fence_char = None
    for line in text.splitlines():
        m = re.match(r"^\s*(```|~~~)", line)
        if m:
            token = m.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token
            elif token == fence_char:
                in_fence = False
                fence_char = None
            kept.append("")
            continue
        kept.append("" if in_fence else line)
    return "\n".join(kept)


def strip_code_for_link_scan(text: str) -> str:
    """Remove fenced and inline code before interpreting Markdown link syntax."""
    without_fences = strip_fenced_code(text)
    return "\n".join(
        re.sub(r"(`+)(.+?)\1", "", line)
        for line in without_fences.splitlines()
    )


def is_content_file_requiring_frontmatter(rel: str) -> bool:
    p = Path(rel)
    name = p.name
    if rel.startswith("01 Curriculum/") and name.startswith("Day ") and name.endswith(".md"):
        return True
    if rel.startswith("02 Daily Assessments/") and name.startswith("Day ") and name.endswith(".md"):
        return True
    if rel.startswith("03 Weekly Simulations/") and name.startswith("Week ") and name.endswith(".md"):
        return True
    if rel.startswith("04 Question Bank/diagnostic/") and name.endswith(".md"):
        return True
    return False


def validate_frontmatter_and_modes(
    root: Path, files: list[Path], metadata: dict[str, dict]
) -> list[ValidationError]:
    errors = []
    for path in files:
        rel = _norm_rel(path.relative_to(root))
        if path.suffix.lower() != ".md":
            continue
        fm = metadata.get(rel, {})
        if is_content_file_requiring_frontmatter(rel) and not fm:
            errors.append(ValidationError(
                "MISSING_FRONTMATTER", rel,
                "content file requires YAML frontmatter",
            ))
            continue

        doc_type = fm.get("type")
        if doc_type in REQUIRED_KEYS_BY_TYPE:
            missing = sorted(REQUIRED_KEYS_BY_TYPE[doc_type] - set(fm))
            if missing:
                errors.append(ValidationError(
                    "MISSING_FRONTMATTER", rel,
                    f"type {doc_type!r} is missing required keys: {', '.join(missing)}",
                ))

        mode = fm.get("mode")
        if isinstance(mode, str) and mode not in ALLOWED_MODES and "{{" not in mode:
            errors.append(ValidationError(
                "INVALID_MODE", rel,
                f"mode {mode!r} is invalid; allowed: {', '.join(sorted(ALLOWED_MODES))}",
            ))

        depth = fm.get("technology_depth")
        if isinstance(depth, str) and depth not in ALLOWED_TECHNOLOGY_DEPTHS and "{{" not in depth:
            errors.append(ValidationError(
                "INVALID_TECHNOLOGY_DEPTH", rel,
                f"technology_depth {depth!r} is invalid",
            ))

    return errors


def parse_resource_catalog(path: Path) -> list[dict]:
    text = read_text(path)
    if text is None:
        return []
    entries = []
    current = None
    for lineno, line in enumerate(text.splitlines(), 1):
        m_start = re.match(r"^-\s+id:\s*(.+?)\s*$", line)
        if m_start:
            if current:
                entries.append(current)
            current = {"id": parse_scalar(m_start.group(1)), "_line": lineno}
            continue
        if current is None:
            continue
        m_field = re.match(r"^\s{2}([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if m_field:
            key, raw = m_field.groups()
            current[key] = parse_scalar(raw)
    if current:
        entries.append(current)
    return entries


def validate_resources(root: Path) -> tuple[list[ValidationError], dict[str, tuple[str, int]]]:
    errors = []
    ids: dict[str, tuple[str, int]] = {}
    catalog = root / "09 Resources" / "catalog.yaml"
    if not catalog.exists():
        return errors, ids

    for entry in parse_resource_catalog(catalog):
        rid = entry.get("id")
        line = entry.get("_line")
        if not isinstance(rid, str) or not rid:
            errors.append(ValidationError(
                "RESOURCE_ID", "09 Resources/catalog.yaml",
                "resource entry is missing id", line,
            ))
            continue
        ids[rid] = ("09 Resources/catalog.yaml", line)

        verified = entry.get("last_verified")
        if not isinstance(verified, str) or not verified.strip():
            errors.append(ValidationError(
                "RESOURCE_LAST_VERIFIED", "09 Resources/catalog.yaml",
                f"resource {rid!r} is missing last_verified", line,
            ))
        else:
            try:
                date.fromisoformat(verified)
            except ValueError:
                errors.append(ValidationError(
                    "RESOURCE_LAST_VERIFIED", "09 Resources/catalog.yaml",
                    f"resource {rid!r} has invalid ISO date {verified!r}", line,
                ))

        depth = entry.get("technology_depth")
        if isinstance(depth, str) and depth not in ALLOWED_TECHNOLOGY_DEPTHS:
            errors.append(ValidationError(
                "INVALID_TECHNOLOGY_DEPTH", "09 Resources/catalog.yaml",
                f"resource {rid!r} has invalid technology_depth {depth!r}", line,
            ))

    return errors, ids


def validate_private_and_obsidian_boundary(root: Path, files: list[Path]) -> list[ValidationError]:
    errors = []
    for path in files:
        rel = _norm_rel(path.relative_to(root))
        if rel == ".study" or rel.startswith(".study/"):
            errors.append(ValidationError(
                "PRIVATE_TRACKED", rel,
                "private learner state must not be part of the public repository",
            ))
        if rel.startswith(".obsidian/") and rel != ".obsidian/templates.json":
            errors.append(ValidationError(
                "OBSIDIAN_LOCAL_STATE", rel,
                "only .obsidian/templates.json may be public; other Obsidian state is local",
            ))
    return errors


def collect_markdown_links(text: str) -> list[tuple[str, int]]:
    clean = strip_code_for_link_scan(text)
    links = []
    lines = clean.splitlines()
    md_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    wiki_re = re.compile(r"\[\[([^\]]+)\]\]")
    for lineno, line in enumerate(lines, 1):
        for match in md_re.finditer(line):
            target = match.group(1).strip()
            # Strip optional Markdown title: path "title"
            if re.search(r'\s+["\']', target):
                target = re.split(r'\s+(?=["\'])', target, maxsplit=1)[0]
            links.append((target.strip("<>"), lineno))
        for match in wiki_re.finditer(line):
            target = match.group(1).split("|", 1)[0].strip()
            links.append((target, lineno))
    return links


def _target_is_external_or_dynamic(target: str) -> bool:
    low = target.lower()
    return (
        not target
        or target.startswith("#")
        or low.startswith(EXTERNAL_SCHEMES)
        or "{{" in target
        or "}}" in target
    )


def _candidate_paths(root: Path, source: Path, raw_target: str) -> list[Path]:
    target = unquote(raw_target).split("#", 1)[0].strip()
    if not target:
        return []
    tpath = Path(target)
    bases = []
    if tpath.is_absolute():
        bases.append(root / str(tpath).lstrip("/"))
    else:
        bases.append(source.parent / tpath)
        bases.append(root / tpath)

    candidates = []
    for base in bases:
        candidates.append(base)
        if base.suffix == "":
            candidates.append(Path(str(base) + ".md"))
            candidates.append(base / "README.md")
    # Preserve order, remove duplicates.
    seen = set()
    unique = []
    for c in candidates:
        resolved = c.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def link_resolves(root: Path, source: Path, target: str, public_files: set[Path]) -> bool:
    for candidate in _candidate_paths(root, source, target):
        if candidate in public_files and candidate.exists():
            return True

    # Obsidian supports basename-only links. If exactly one public Markdown file
    # matches the requested stem, the link is statically resolvable.
    base_target = unquote(target).split("#", 1)[0].strip()
    if "/" not in base_target and "\\" not in base_target:
        stem = Path(base_target).stem
        matches = [p for p in public_files if p.suffix.lower() == ".md" and p.stem == stem]
        if len(matches) == 1:
            return True
        if len(matches) > 1:
            # Ambiguous Obsidian links are not safely decidable statically here.
            return True
    return False


def validate_links(root: Path, files: list[Path]) -> list[ValidationError]:
    errors = []
    public_files = {p.resolve() for p in files}
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        rel = _norm_rel(path.relative_to(root))
        text = read_text(path)
        if text is None:
            continue
        for target, lineno in collect_markdown_links(text):
            normalized = unquote(target).replace("\\", "/")
            if normalized.startswith("./"):
                normalized = normalized[2:]
            if normalized == ".study" or normalized.startswith(".study/"):
                errors.append(ValidationError(
                    "PRIVATE_LINK", rel,
                    f"public Markdown must not link to private learner state: {target}", lineno,
                ))
                continue
            if _target_is_external_or_dynamic(target):
                continue
            if not link_resolves(root, path, target, public_files):
                errors.append(ValidationError(
                    "BROKEN_LINK", rel,
                    f"internal link target does not resolve: {target}", lineno,
                ))
    return errors


def validate_question_integrity(
    root: Path, files: list[Path], metadata: dict[str, dict]
) -> list[ValidationError]:
    errors = []
    question_ids = set()
    locations: dict[str, str] = {}

    for rel, fm in metadata.items():
        if fm.get("type") != "question-bank":
            continue
        qids = fm.get("question_ids")
        if isinstance(qids, list):
            for qid in qids:
                if not isinstance(qid, str):
                    continue
                if qid in locations:
                    errors.append(ValidationError(
                        "DUPLICATE_ID", rel,
                        f"question id {qid!r} duplicates {locations[qid]}",
                    ))
                else:
                    locations[qid] = rel
                    question_ids.add(qid)

        if fm.get("answer_key_public") is True:
            errors.append(ValidationError(
                "PUBLIC_ANSWER_KEY", rel,
                "diagnostic question bank must not expose public answer keys",
            ))

        path = root / rel
        text = read_text(path) or ""
        if re.search(r"(?im)^##\s+(solution|answer\s+key)\b", text):
            errors.append(ValidationError(
                "PUBLIC_ANSWER_KEY", rel,
                "question bank contains a public solution/answer-key heading",
            ))

    for path in files:
        rel = _norm_rel(path.relative_to(root))
        if not (
            rel.startswith("01 Curriculum/00 - Week 0 Diagnostic/")
            and path.name.startswith("Day ")
            and path.suffix.lower() == ".md"
        ):
            continue
        text = strip_fenced_code(read_text(path) or "")
        for qid in sorted(set(re.findall(r"`(diag-[a-z0-9-]+)`", text))):
            if qid not in question_ids:
                errors.append(ValidationError(
                    "UNKNOWN_QUESTION_ID", rel,
                    f"Week 0 day references unknown question id {qid!r}",
                ))
    return errors


def validate_resource_references(
    root: Path, metadata: dict[str, dict], resource_ids: set[str]
) -> list[ValidationError]:
    errors = []
    for rel, fm in metadata.items():
        refs = fm.get("resource_ids")
        if not isinstance(refs, list):
            continue
        for rid in refs:
            if not isinstance(rid, str) or "{{" in rid:
                continue
            if rid not in resource_ids:
                errors.append(ValidationError(
                    "UNKNOWN_RESOURCE_ID", rel,
                    f"frontmatter references unknown resource id {rid!r}",
                ))
    return errors


def validate_historical_templates(
    root: Path, files: list[Path], metadata: dict[str, dict]
) -> list[ValidationError]:
    errors = []
    for path in files:
        rel = _norm_rel(path.relative_to(root))
        if not rel.startswith("90 Templates/") or path.suffix.lower() != ".md":
            continue
        fm = metadata.get(rel, {})
        if fm.get("type") not in HISTORICAL_TEMPLATE_TYPES:
            continue
        text = (read_text(path) or "").lower()
        raw_pos = text.find("## raw attempt")
        feedback_pos = text.find("## feedback")
        if raw_pos == -1 or feedback_pos == -1 or raw_pos == feedback_pos:
            errors.append(ValidationError(
                "HISTORY_SEPARATION", rel,
                "historical assessment template must separate Raw attempt and Feedback sections",
            ))
    return errors


def validate_duplicate_canonical_ids(
    root: Path,
    metadata: dict[str, dict],
    resource_entries: list[dict],
) -> list[ValidationError]:
    errors = []
    seen: dict[str, str] = {}

    def add(value, location):
        if not isinstance(value, str) or not value or "{{" in value:
            return
        if value in seen:
            errors.append(ValidationError(
                "DUPLICATE_ID", location,
                f"canonical id {value!r} duplicates {seen[value]}",
            ))
        else:
            seen[value] = location

    for rel, fm in metadata.items():
        add(fm.get("id"), rel)

    for entry in resource_entries:
        add(entry.get("id"), "09 Resources/catalog.yaml")

    for rel, fm in metadata.items():
        if fm.get("type") == "question-bank" and isinstance(fm.get("question_ids"), list):
            for qid in fm["question_ids"]:
                add(qid, rel)
    return errors


def validate_repository(root: Path) -> list[ValidationError]:
    root = root.resolve()
    files = repository_files(root)

    metadata: dict[str, dict] = {}
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        if text is None:
            continue
        fm, _ = parse_frontmatter(text)
        metadata[_norm_rel(path.relative_to(root))] = fm

    errors: list[ValidationError] = []
    errors.extend(validate_private_and_obsidian_boundary(root, files))
    errors.extend(validate_frontmatter_and_modes(root, files, metadata))
    errors.extend(validate_links(root, files))

    resource_errors, resource_locations = validate_resources(root)
    errors.extend(resource_errors)
    resource_entries = parse_resource_catalog(root / "09 Resources" / "catalog.yaml") \
        if (root / "09 Resources" / "catalog.yaml").exists() else []
    errors.extend(validate_duplicate_canonical_ids(root, metadata, resource_entries))
    errors.extend(validate_resource_references(root, metadata, set(resource_locations)))
    errors.extend(validate_question_integrity(root, files, metadata))
    errors.extend(validate_historical_templates(root, files, metadata))

    # De-duplicate exact errors while preserving stable ordering.
    unique = {}
    for error in errors:
        key = (error.code, error.path, error.line, error.message)
        unique[key] = error
    return sorted(
        unique.values(),
        key=lambda e: (e.path, e.line or 0, e.code, e.message),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate roadmap repository invariants.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    if not root.exists() or not root.is_dir():
        print(f"[INVALID_ROOT] {root}: repository root does not exist", file=sys.stderr)
        return 2

    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(error.render())
        print(f"Validation failed: {len(errors)} error(s).")
        return 1

    print("Validation passed: 0 errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
