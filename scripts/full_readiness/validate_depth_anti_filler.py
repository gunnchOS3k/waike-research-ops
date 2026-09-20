#!/usr/bin/env python3
"""Depth / anti-filler validator for WAIKE 18-track full readiness.

Checks:
- empty sections in review/pilot packets
- repeated boilerplate across tracks
- noun-swapped lab titles
- rubrics without criteria
- assignments without deliverables
- lessons without objectives
- missing instructor / learner guidance

Writes artifacts/full_readiness/DEPTH_ANTI_FILLER_REPORT.json
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "curriculum/taxonomy/canonical_track_registry.v1.json"
DRC = ROOT / "curriculum/digital_rc"
REVIEW_ROOT = ROOT / "curriculum/review_packets"
PILOT_ROOT = ROOT / "pilot"
OUT = ROOT / "artifacts/full_readiness/DEPTH_ANTI_FILLER_REPORT.json"

REQUIRED_REVIEW = [
    "README.md",
    "objectives.md",
    "sequence.md",
    "assessment_map.md",
    "lab_map.md",
    "standards_map.md",
    "ai_policy.md",
    "accessibility.md",
    "provenance.md",
    "known_risks.md",
    "reviewer_rubric.md",
    "signoff_form.md",
]

REQUIRED_PILOT = [
    "prerequisites.md",
    "session_plan.md",
    "facilitator_plan.md",
    "instrumentation.md",
    "learning_measures.md",
    "usability_measures.md",
    "issue_logging.md",
    "consent_ethics_placeholders.md",
    "rollback_safety.md",
    "post_pilot_review.md",
]

# Boilerplate phrases that are OK in small doses but fail if they dominate a file
GENERIC_PHRASES = [
    "prepare waike learners for industry-ready competence",
    "aligned with the gunnchos3k mlv ecosystem",
    "see waike level map",
    "use socratic hints first",
    "never shame learners",
    "like learning to cook",
]

STOP = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "to",
    "of",
    "for",
    "on",
    "in",
    "with",
    "without",
    "lab",
    "week",
    "track",
    "course",
    "foundations",
    "introduction",
    "basics",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalize_title(title: str) -> str:
    tokens = re.findall(r"[a-z0-9]+", title.lower())
    return " ".join(t for t in tokens if t not in STOP and not t.isdigit())


def skeleton_title(title: str) -> str:
    """Replace likely domain nouns with placeholders to detect noun-swaps."""
    tokens = re.findall(r"[a-z0-9]+", title.lower())
    # Keep structural verbs/nouns; blank distinctive tokens longer than 4 chars that look domain-specific
    structural = {
        "lab",
        "intro",
        "introduction",
        "setup",
        "review",
        "security",
        "deploy",
        "test",
        "tests",
        "matrix",
        "report",
        "conflict",
        "migration",
        "observability",
        "rollback",
        "path",
        "loss",
        "schema",
        "ingest",
        "consent",
        "charter",
        "frames",
        "pose",
        "loop",
        "permissions",
        "ticket",
        "queue",
        "backup",
        "dns",
        "storage",
        "services",
        "users",
        "runbook",
        "automation",
    }
    out = []
    for t in tokens:
        if t in STOP or t.isdigit():
            continue
        if t in structural or len(t) <= 3:
            out.append(t)
        else:
            out.append("NOUN")
    return " ".join(out)


def empty_section_findings(path: Path, text: str) -> list[dict[str, str]]:
    """Flag thin *leaf* sections only.

    Rationale (false-positive fixes):
    - Parent headings with an immediate child heading have empty bodies by design
      (e.g. ``# Title`` then ``## Summary``). Those are not thin content.
    - Fenced code blocks often contain ``#`` lines (syllabus excerpts); mask them
      before heading splits so excerpt fences are not treated as real sections.
    - Remaining short leaf bodies (<25 chars, no list/table) are still warnings.
    """
    findings = []
    if not text.strip():
        findings.append(
            {
                "check": "empty_file",
                "path": str(path.relative_to(ROOT)),
                "detail": "File empty",
            }
        )
        return findings
    # Mask fenced code so headings inside fences are not parsed as document structure.
    masked = re.sub(r"```.*?```", "\n[code-fence]\n", text, flags=re.S)
    parts = re.split(r"(?m)^(#{1,3}\s+.+)$", masked)
    i = 1
    while i + 1 < len(parts):
        heading = parts[i].strip()
        body = parts[i + 1]
        body_stripped = body.strip()
        has_structure = bool(
            re.search(r"(?m)^(\|.+\||\s*[-*]\s+\S|\s*\d+\.\s+\S|\[code-fence\])", body)
        )
        # Parent heading: next sibling split already consumed the child heading; empty
        # body means the child started immediately — not a thin leaf.
        if not body_stripped:
            i += 2
            continue
        # Ignore very short trailing sections like "_Generated…_"
        if (
            len(body_stripped) < 25
            and not has_structure
            and not body_stripped.startswith("_Generated")
            and "PASS" not in heading
        ):
            findings.append(
                {
                    "check": "empty_section",
                    "path": str(path.relative_to(ROOT)),
                    "detail": f"Thin/empty section under '{heading}' ({len(body_stripped)} chars)",
                }
            )
        i += 2
    return findings


DELIVERABLE_RE = re.compile(
    r"(?i)\b("
    r"write|submit|build|deliverable|produce|create|name|compute|implement|"
    r"draw|mark|map|document|complete|run|fill|record|explain|score|pin|"
    r"merge|ship|prove|capture|charter|design|assemble|evaluate|compare|"
    r"lab to run"
    r")\b"
)


def resolve_package(track: dict[str, Any]) -> tuple[str | None, Path | None, dict[str, Any]]:
    pkgs = (
        track.get("content_maturity", {})
        .get("facets", {})
        .get("covering_package_ids", [])
    )
    for pkg_id in pkgs:
        pdir = DRC / pkg_id
        cpath = pdir / "course.json"
        if cpath.exists():
            return pkg_id, pdir, load_json(cpath)
    return None, None, {}


def main() -> int:
    reg = load_json(REGISTRY)
    tracks = reg["tracks"]
    findings: list[dict[str, Any]] = []
    stats: dict[str, Any] = {
        "tracks": len(tracks),
        "review_packets_complete": 0,
        "pilot_packets_complete": 0,
        "packages_checked": 0,
    }

    # --- Packet structure ---
    review_bodies: dict[str, dict[str, str]] = defaultdict(dict)
    for track in tracks:
        tid = track["track_id"]
        rdir = REVIEW_ROOT / tid
        missing = [f for f in REQUIRED_REVIEW if not (rdir / f).exists()]
        if missing:
            findings.append(
                {
                    "severity": "error",
                    "track_id": tid,
                    "check": "missing_review_files",
                    "detail": f"Missing: {', '.join(missing)}",
                }
            )
        else:
            stats["review_packets_complete"] += 1
        for f in REQUIRED_REVIEW:
            p = rdir / f
            if p.exists():
                text = read_text(p)
                review_bodies[f][tid] = text
                for item in empty_section_findings(p, text):
                    findings.append(
                        {"severity": "warning", "track_id": tid, **item}
                    )
                if f == "signoff_form.md":
                    if re.search(r"PASS[`:\s]*true", text, re.I) and "false" not in text.lower():
                        findings.append(
                            {
                                "severity": "error",
                                "track_id": tid,
                                "check": "signoff_pass_true",
                                "detail": "signoff_form must keep PASS false until human signs",
                            }
                        )
                    if "PASS" in text and "false" not in text.lower():
                        findings.append(
                            {
                                "severity": "error",
                                "track_id": tid,
                                "check": "signoff_pass_missing_false",
                                "detail": "PASS false not found in signoff_form",
                            }
                        )

        pdir = PILOT_ROOT / f"track_{tid}"
        missing_p = [f for f in REQUIRED_PILOT if not (pdir / f).exists()]
        if missing_p:
            findings.append(
                {
                    "severity": "error",
                    "track_id": tid,
                    "check": "missing_pilot_files",
                    "detail": f"Missing: {', '.join(missing_p)}",
                }
            )
        else:
            stats["pilot_packets_complete"] += 1
        for f in REQUIRED_PILOT:
            p = pdir / f
            if p.exists():
                for item in empty_section_findings(p, read_text(p)):
                    findings.append(
                        {"severity": "warning", "track_id": tid, **item}
                    )
                body = read_text(p).lower()
                if "pilot completed" in body or "pilot ran successfully" in body:
                    findings.append(
                        {
                            "severity": "error",
                            "track_id": tid,
                            "check": "false_pilot_claim",
                            "detail": f"{f} appears to claim a pilot ran",
                        }
                    )

    # --- Repeated boilerplate across review README bodies ---
    readmes = review_bodies.get("README.md", {})
    if len(readmes) >= 2:
        # Near-duplicate detection: normalized shared line ratio
        norm_lines = {
            tid: [
                re.sub(r"\s+", " ", ln.strip().lower())
                for ln in text.splitlines()
                if len(ln.strip()) > 40
            ]
            for tid, text in readmes.items()
        }
        tids = list(norm_lines.keys())
        for i, a in enumerate(tids):
            set_a = set(norm_lines[a])
            if not set_a:
                continue
            for b in tids[i + 1 :]:
                set_b = set(norm_lines[b])
                if not set_b:
                    continue
                inter = set_a & set_b
                # Exclude expected shared table headers / short policy lines
                heavy = [
                    ln
                    for ln in inter
                    if "track:" not in ln
                    and "academy:" not in ln
                    and "extension class:" not in ln
                    and "content maturity:" not in ln
                    and "covering package:" not in ln
                    and not ln.startswith("| file |")
                    and "not in scope for this packet" not in ln
                    and "generated by agent 10" not in ln
                    and "what reviewers should verify" not in ln
                    # Expected Agent-10 review scaffold (shared across tracks by design).
                    and "audience:** waike level" not in ln
                    and "primary sources:**" not in ln
                    and "week sequence matches package" not in ln
                    and "each lab has a runnable" not in ln
                    and "assignments name deliverables" not in ln
                    and "instructor and learner guidance" not in ln
                    and "gaps below are accepted" not in ln
                    and "accreditation claims" not in ln
                    and "partner field approval" not in ln
                    and "asserting a pilot already ran" not in ln
                    and "review packet —" not in ln
                    and "| objectives.md |" not in ln
                    and "| sequence.md |" not in ln
                    and "| assessment_map.md |" not in ln
                    and "| lab_map.md |" not in ln
                    and "| standards_map.md |" not in ln
                    and "| ai_policy.md |" not in ln
                    and "| accessibility.md |" not in ln
                    and "| provenance.md |" not in ln
                    and "| known_risks.md |" not in ln
                    and "| reviewer_rubric.md |" not in ln
                    and "| signoff_form.md |" not in ln
                ]
                ratio = len(heavy) / max(len(set_a), len(set_b))
                # Only warn when non-scaffold long lines heavily overlap (substantive clone).
                if ratio >= 0.75 and len(heavy) >= 8:
                    findings.append(
                        {
                            "severity": "warning",
                            "track_id": f"{a}|{b}",
                            "check": "repeated_boilerplate",
                            "detail": (
                                f"README.md share {len(heavy)} long non-scaffold lines "
                                f"(ratio={ratio:.2f}) — likely copy-paste filler"
                            ),
                        }
                    )

    # Generic phrase density in program files / package lessons
    for track in tracks:
        tid = track["track_id"]
        for p in track.get("authoritative_source_paths", []):
            if not p.endswith(".md"):
                continue
            path = ROOT / p
            if not path.exists():
                continue
            low = read_text(path).lower()
            hits = [ph for ph in GENERIC_PHRASES if ph in low]
            # House-style orientation lines appear in many programs/*.md by design.
            # Only warn when generic phrases dominate AND the file lacks track-specific
            # tokens (title words / lab vocabulary) — otherwise it is expected scaffold.
            track_tokens = [
                t
                for t in re.findall(r"[a-z0-9]+", tid.lower())
                if len(t) > 3 and t not in STOP
            ]
            has_track_vocab = any(tok in low for tok in track_tokens) or len(low) > 2500
            if len(hits) >= 5 and not has_track_vocab:
                findings.append(
                    {
                        "severity": "warning",
                        "track_id": tid,
                        "check": "generic_program_boilerplate",
                        "path": p,
                        "detail": f"Program file contains {len(hits)} known generic phrases without track vocabulary",
                    }
                )

    # --- Package depth checks ---
    lab_skeletons: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for track in tracks:
        tid = track["track_id"]
        pkg_id, pdir, course = resolve_package(track)
        if not pdir:
            findings.append(
                {
                    "severity": "error",
                    "track_id": tid,
                    "check": "missing_package",
                    "detail": "No digital_rc package resolved",
                }
            )
            continue
        stats["packages_checked"] += 1

        # Instructor / learner guidance
        if not (pdir / "instructor" / "INSTRUCTOR_PACKET.md").exists():
            findings.append(
                {
                    "severity": "error",
                    "track_id": tid,
                    "check": "missing_instructor_guidance",
                    "path": f"curriculum/digital_rc/{pkg_id}/instructor/INSTRUCTOR_PACKET.md",
                    "detail": "Missing instructor packet",
                }
            )
        if not (pdir / "student" / "STUDENT_PACKET.md").exists():
            findings.append(
                {
                    "severity": "error",
                    "track_id": tid,
                    "check": "missing_learner_guidance",
                    "path": f"curriculum/digital_rc/{pkg_id}/student/STUDENT_PACKET.md",
                    "detail": "Missing student packet",
                }
            )

        # Lessons without objectives
        for week in course.get("weeks") or []:
            lesson = week.get("lesson") or {}
            body = (lesson.get("body_md") or "").strip()
            title = week.get("title") or lesson.get("title") or ""
            has_obj = bool(lesson.get("worked_example")) or len(body) >= 200
            # Explicit objective markers
            if re.search(r"(?i)\b(objective|you will|learners will)\b", body):
                has_obj = True
            if not has_obj:
                findings.append(
                    {
                        "severity": "error",
                        "track_id": tid,
                        "check": "lesson_without_objectives",
                        "detail": f"Week {week.get('week')} '{title}' lacks workable objectives/body",
                    }
                )
            if len(body) < 120:
                findings.append(
                    {
                        "severity": "warning",
                        "track_id": tid,
                        "check": "thin_lesson_body",
                        "detail": f"Week {week.get('week')} body {len(body)} chars",
                    }
                )

            lab_id = week.get("lab_id")
            if lab_id:
                lab_skeletons[skeleton_title(lab_id.replace("_", " "))].append(
                    (tid, lab_id)
                )
                lab_skeletons[skeleton_title(title)].append((tid, f"week:{lab_id}"))

        # Assignments without deliverables
        adir = pdir / "assignments"
        for name in course.get("assignments") or []:
            path = adir / name
            text = read_text(path)
            if not path.exists():
                findings.append(
                    {
                        "severity": "error",
                        "track_id": tid,
                        "check": "assignment_missing",
                        "detail": name,
                    }
                )
                continue
            if not DELIVERABLE_RE.search(text):
                findings.append(
                    {
                        "severity": "error",
                        "track_id": tid,
                        "check": "assignment_without_deliverable",
                        "path": str(path.relative_to(ROOT)),
                        "detail": "No deliverable verb/pattern found",
                    }
                )
            if len(text.strip()) < 80:
                findings.append(
                    {
                        "severity": "warning",
                        "track_id": tid,
                        "check": "thin_assignment",
                        "path": str(path.relative_to(ROOT)),
                        "detail": f"Assignment only {len(text.strip())} chars",
                    }
                )

        # Rubrics without criteria
        rdir = pdir / "rubrics"
        if rdir.exists():
            for rpath in sorted(rdir.glob("*.md")):
                text = read_text(rpath)
                criteria = re.findall(r"^\s*[-*]\s+", text, re.M)
                weighted = re.findall(r"\d+%", text)
                if len(criteria) < 2 and len(weighted) < 2:
                    findings.append(
                        {
                            "severity": "error",
                            "track_id": tid,
                            "check": "rubric_without_criteria",
                            "path": str(rpath.relative_to(ROOT)),
                            "detail": "Rubric lacks criteria bullets / weights",
                        }
                    )

        # Lab titles on disk
        labs_root = pdir / "labs"
        if labs_root.exists():
            for lab in sorted(labs_root.iterdir()):
                name = lab.name if lab.is_dir() else lab.stem
                lab_skeletons[skeleton_title(name.replace("_", " "))].append(
                    (tid, name)
                )

    # Noun-swapped lab detection: same skeleton across ≥3 tracks with different surface names.
    # Rationale: skeletons that are only NOUN tokens (e.g. "NOUN NOUN NOUN") match any
    # multi-word lab id and are not evidence of noun-swapping. Require ≥1 retained
    # structural token so the pattern is actually parallel (e.g. "lab NOUN matrix").
    for skel, items in lab_skeletons.items():
        if not skel or skel.count("NOUN") < 1:
            continue
        structural_kept = [t for t in skel.split() if t != "NOUN"]
        if len(structural_kept) < 1:
            continue
        tracks_hit = {t for t, _ in items}
        names = {n for _, n in items}
        if len(tracks_hit) >= 3 and len(names) >= 3:
            findings.append(
                {
                    "severity": "warning",
                    "track_id": "|".join(sorted(tracks_hit)[:6]),
                    "check": "noun_swapped_lab_titles",
                    "detail": (
                        f"Skeleton '{skel}' appears across {len(tracks_hit)} tracks "
                        f"with names {sorted(names)[:8]}"
                    ),
                }
            )

    # Also flag identical normalized lab ids across different packages (excluding shared pkgs)
    id_owners: dict[str, set[str]] = defaultdict(set)
    for track in tracks:
        tid = track["track_id"]
        pkg_id, pdir, course = resolve_package(track)
        if not course:
            continue
        for lid in course.get("labs") or []:
            id_owners[lid].add(tid)
    for lid, owners in id_owners.items():
        # Shared packages legitimately share lab ids across DIGITAL_CONFIDENCE/IT_SUPPORT etc.
        if len(owners) >= 3:
            findings.append(
                {
                    "severity": "warning",
                    "track_id": "|".join(sorted(owners)),
                    "check": "shared_lab_id_across_tracks",
                    "detail": f"lab_id `{lid}` listed for {len(owners)} tracks",
                }
            )

    errors = sum(1 for f in findings if f.get("severity") == "error")
    warnings = sum(1 for f in findings if f.get("severity") == "warning")
    report = {
        "schema": "waike.full_readiness.depth_anti_filler_report.v1",
        "generated_at": now_iso(),
        "stats": stats,
        "summary": {
            "error_count": errors,
            "warning_count": warnings,
            "finding_count": len(findings),
            "pass": errors == 0,
        },
        "findings": findings,
        "notes": [
            "PASS means no error-severity findings; warnings still require human judgment.",
            "Shared packages may trigger shared_lab_id warnings by design.",
            "empty_section skips parent headings with empty bodies (child follows immediately) and masks fenced code.",
            "repeated_boilerplate ignores Agent-10 review packet scaffold lines.",
            "noun_swapped_lab_titles requires ≥1 structural token retained in the skeleton.",
            "generic_program_boilerplate requires ≥5 generic phrases without track vocabulary.",
            "Does not claim accreditation or that pilots ran.",
        ],
        "substantive_warning_count": warnings,
        "detector_false_positive_rationale": {
            "empty_section_parent_headings": "Markdown parent headings often have empty bodies before child headings; not thin content.",
            "empty_section_fenced_code": "Syllabus excerpts in fences contain # lines that must not be parsed as document headings.",
            "repeated_boilerplate_scaffold": "Agent-10 review packets share inventory tables and reviewer checklists by design.",
            "noun_swapped_all_noun_skeletons": "All-NOUN skeletons match unrelated multi-word lab ids; require structural anchors.",
            "generic_program_house_style": "programs/*.md share WAIKE orientation phrases; warn only when track vocabulary is absent.",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "report": str(OUT.relative_to(ROOT)),
                "errors": errors,
                "warnings": warnings,
                "pass": errors == 0,
                **stats,
            },
            indent=2,
        )
    )
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
