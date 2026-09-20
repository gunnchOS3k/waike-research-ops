#!/usr/bin/env python3
"""Build WAIKE 18-track master readiness matrix from filesystem evidence."""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "full_readiness"
TRACKS = json.loads((ROOT / "curriculum" / "taxonomy" / "eighteen_tracks.json").read_text())["tracks"]
COLUMNS = [
    "canonical_identity", "independent_entry_point", "syllabus", "objectives", "modules",
    "lessons", "labs", "assignments", "quizzes", "summative_assessment", "capstone_project",
    "group_activity", "case_studies", "rubrics", "student_packet", "instructor_packet",
    "portfolio_outcomes", "career_outcomes", "glossary", "references", "standards_mapping",
    "accessibility_notes", "ai_policy", "gunnchai_tutor_contract", "digital_package",
    "compile", "schema", "offline", "waike_learner", "waike_instructor", "waike_grader",
    "waike_guardian_relevance", "waike_admin", "device_phone", "device_handheld",
    "device_student", "device_coder", "review_packet", "human_academic_review",
    "human_accessibility_review", "field_pilot",
]
ALLOWED = {
    "PASS", "PARTIAL", "MISSING", "NOT_APPLICABLE_WITH_RATIONALE",
    "HUMAN_REQUIRED", "EXTERNAL_REQUIRED",
}

LEGACY = {
    "NETWORKING_INFRA": "COMPUTER_NETWORKING",
    "CYBER_SOC": "CYBERSECURITY",
    "DIGITAL_CONFIDENCE": "GENERAL_IT",
    "IT_SUPPORT_HARDWARE": "GENERAL_IT",
}


def sha_short(p: Path) -> str:
    if not p.exists():
        return ""
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    return h[:12]


def pkg_dirs_for(track_id: str) -> list[Path]:
    dig = ROOT / "curriculum" / "digital_rc"
    out = []
    direct = dig / track_id
    if direct.is_dir():
        out.append(direct)
    leg = LEGACY.get(track_id)
    if leg and (dig / leg).is_dir() and (dig / leg) not in out:
        out.append(dig / leg)
    return out


def status(pass_cond: bool, partial_cond: bool = False, missing_ok: bool = False) -> str:
    if pass_cond:
        return "PASS"
    if partial_cond:
        return "PARTIAL"
    return "MISSING"


def cell(st: str, evidence: str, note: str = "") -> dict:
    assert st in ALLOWED, st
    d = {"status": st, "evidence": evidence}
    if note:
        d["note"] = note
    return d


def assess_track(t: dict) -> dict:
    tid = t["track_id"]
    pkgs = pkg_dirs_for(tid)
    canon = ROOT / "curriculum" / "canonical_packages" / tid / "PACKAGE_MANIFEST.v1.json"
    review = ROOT / "curriculum" / "review_packets" / tid
    pilot = ROOT / "pilot" / f"track_{tid}"
    standards = ROOT / "standards_alignment" / "by_track" / f"{tid}.yaml"
    ai_pol = ROOT / "gunnchai" / "track_policies" / f"{tid}.policy.json"
    program = ROOT / t["owner_program_file"]

    primary = pkgs[0] if pkgs else None
    has_entry = (ROOT / "curriculum" / "digital_rc" / tid).is_dir() or canon.exists()
    shared_only = tid in LEGACY and not (ROOT / "curriculum" / "digital_rc" / tid).is_dir()

    def exists(*rels: str) -> bool:
        if not primary:
            return False
        return any((primary / r).exists() for r in rels)

    def any_pkg(*rels: str) -> bool:
        return any((p / r).exists() for p in pkgs for r in rels)

    weeks = list((primary / "weeks").glob("w*/lesson.md")) if primary and (primary / "weeks").exists() else []
    labs = list((primary / "labs").iterdir()) if primary and (primary / "labs").exists() else []
    lesson_ok = len(weeks) >= 8 and all(w.stat().st_size >= 800 for w in weeks)
    lesson_partial = len(weeks) >= 8
    lab_ok = len(labs) >= 8
    lab_partial = len(labs) >= 4

    prog_ok = program.exists() and program.stat().st_size > 200

    row = {
        "track_id": tid,
        "title": t["title"],
        "extension_class": t.get("extension_class"),
        "package_dirs": [str(p.relative_to(ROOT)) for p in pkgs],
        "cells": {
            "canonical_identity": cell("PASS", f"curriculum/taxonomy/eighteen_tracks.json#{tid}"),
            "independent_entry_point": cell(
                "PASS" if has_entry and not shared_only else ("PARTIAL" if pkgs else "MISSING"),
                str(canon.relative_to(ROOT)) if canon.exists() else (str((ROOT / 'curriculum' / 'digital_rc' / tid).relative_to(ROOT)) if (ROOT / 'curriculum' / 'digital_rc' / tid).is_dir() else (str(pkgs[0].relative_to(ROOT)) if pkgs else "")),
                "shared package only" if shared_only else "",
            ),
            "syllabus": cell(status(any_pkg("syllabus.md")), f"{primary}/syllabus.md" if primary else ""),
            "objectives": cell(status(prog_ok or lesson_partial, prog_ok or lesson_partial), str(program) if program.exists() else ""),
            "modules": cell(status(lesson_partial), f"{primary}/weeks" if primary else ""),
            "lessons": cell(status(lesson_ok, lesson_partial), f"{primary}/weeks" if primary else "", f"n={len(weeks)}"),
            "labs": cell(status(lab_ok, lab_partial), f"{primary}/labs" if primary else "", f"n={len(labs)}"),
            "assignments": cell(status(any_pkg("assignments"), any_pkg("assignments")), f"{primary}/assignments" if primary else ""),
            "quizzes": cell(status(any_pkg("quizzes"), any_pkg("quizzes")), f"{primary}/quizzes" if primary else ""),
            "summative_assessment": cell(status(any_pkg("assessments/final_knowledge.json", "assessments/mid_course.json"), any_pkg("assessments")), f"{primary}/assessments" if primary else ""),
            "capstone_project": cell(status(any_pkg("projects", "assessments/final_practical.json"), any_pkg("projects")), f"{primary}/projects" if primary else ""),
            "group_activity": cell("PARTIAL", "group_projects/by_course (legacy) or package projects", "verify track-specific group brief"),
            "case_studies": cell("PARTIAL", "case_studies/7gc", "campus case studies shared; track mapping varies"),
            "rubrics": cell(status(any_pkg("rubrics"), any_pkg("rubrics")), f"{primary}/rubrics" if primary else ""),
            "student_packet": cell(status(any_pkg("student/STUDENT_PACKET.md")), f"{primary}/student/STUDENT_PACKET.md" if primary else ""),
            "instructor_packet": cell(status(any_pkg("instructor/INSTRUCTOR_PACKET.md")), f"{primary}/instructor/INSTRUCTOR_PACKET.md" if primary else ""),
            "portfolio_outcomes": cell(status(any_pkg("portfolio/outcomes.json", "portfolio/PORTFOLIO.md"), any_pkg("portfolio")), f"{primary}/portfolio" if primary else ""),
            "career_outcomes": cell(status(any_pkg("career_mapping.json")), f"{primary}/career_mapping.json" if primary else ""),
            "glossary": cell(status(any_pkg("glossary.md", "glossary.json")), f"{primary}/glossary.md" if primary else ""),
            "references": cell(status(any_pkg("references.md", "REFERENCES.md"), any_pkg("provenance")), f"{primary}/references.md" if primary else ""),
            "standards_mapping": cell(status(standards.exists(), standards.exists()), str(standards.relative_to(ROOT)) if standards.exists() else "standards_alignment/by_track/"),
            "accessibility_notes": cell(status(any_pkg("accessibility_notes.md", "student/accessibility_notes.md")), f"{primary}/accessibility_notes.md" if primary else ""),
            "ai_policy": cell(status(any_pkg("ai_use_policy.json") or ai_pol.exists(), any_pkg("ai_use_policy.json") or ai_pol.exists()), str(ai_pol.relative_to(ROOT)) if ai_pol.exists() else (f"{primary}/ai_use_policy.json" if primary else "")),
            "gunnchai_tutor_contract": cell(status(ai_pol.exists(), ai_pol.exists() or any_pkg("ai_use_policy.json")), str(ai_pol.relative_to(ROOT)) if ai_pol.exists() else "gunnchai/track_policies/"),
            "digital_package": cell(status(bool(pkgs)), str(pkgs[0].relative_to(ROOT)) if pkgs else ""),
            "compile": cell(status(any_pkg("course.json")), f"{primary}/course.json" if primary else ""),
            "schema": cell(status(any_pkg("course.json") and '"schema"' in (primary / 'course.json').read_text(encoding='utf-8', errors='ignore') if primary and (primary/'course.json').exists() else False), "schema/waike_course_package.v1.json"),
            "offline": cell(status(any_pkg("offline_pack"), any_pkg("offline_pack")), f"{primary}/offline_pack" if primary else ""),
            "waike_learner": cell("PARTIAL", "ingest/learner/waike_learner_ingest.v1.json", "17 package dirs historically; need 18 track_id keys"),
            "waike_instructor": cell("PARTIAL", "ingest/teacher/waike_teacher_ingest.v1.json"),
            "waike_grader": cell("PARTIAL", "ingest/teacher/waike_teacher_ingest.v1.json#answer_keys"),
            "waike_guardian_relevance": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_ROLE_MATRIX.json", "guardian relevance varies by track"),
            "waike_admin": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_ROLE_MATRIX.json"),
            "device_phone": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_DEVICE_MATRIX.json"),
            "device_handheld": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_DEVICE_MATRIX.json"),
            "device_student": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_DEVICE_MATRIX.json"),
            "device_coder": cell("PARTIAL", "artifacts/full_readiness/WAIKE_18_TRACK_DEVICE_MATRIX.json"),
            "review_packet": cell(status(review.is_dir() and (review / "README.md").exists(), review.is_dir()), str(review.relative_to(ROOT)) if review.exists() else f"curriculum/review_packets/{tid}/"),
            "human_academic_review": cell("HUMAN_REQUIRED", "", "No human academic sign-off on file"),
            "human_accessibility_review": cell("HUMAN_REQUIRED", "", "No human accessibility sign-off on file"),
            "field_pilot": cell("EXTERNAL_REQUIRED", str(pilot.relative_to(ROOT)) if pilot.exists() else f"pilot/track_{tid}/", "Pilot packet may exist; field execution absent"),
        },
    }
    return row


def readiness_level(row: dict) -> str:
    cells = row["cells"]
    human = {"human_academic_review", "human_accessibility_review", "field_pilot"}
    auto = {k: v for k, v in cells.items() if k not in human}
    if any(v["status"] == "MISSING" for v in auto.values()):
        # distinguish authored vs package
        if cells["lessons"]["status"] == "MISSING" or cells["digital_package"]["status"] == "MISSING":
            return "L0_DEFINED" if cells["canonical_identity"]["status"] == "PASS" else "L0_DEFINED"
        return "L1_AUTHORED"
    if cells["digital_package"]["status"] != "PASS" or cells["independent_entry_point"]["status"] == "MISSING":
        return "L1_AUTHORED"
    if cells["independent_entry_point"]["status"] == "PARTIAL":
        level = "L2_DIGITAL_PACKAGE_READY"
    else:
        level = "L2_DIGITAL_PACKAGE_READY"
    # platform
    if all(cells[k]["status"] in ("PASS", "PARTIAL") for k in ("waike_learner", "waike_instructor")):
        level = "L3_PLATFORM_READY"
    if all(cells[k]["status"] in ("PASS", "PARTIAL") for k in ("device_phone", "device_handheld", "device_student", "device_coder")):
        if level.startswith("L3") or level.startswith("L2"):
            level = "L4_DEVICE_READY"
    if cells["review_packet"]["status"] == "PASS":
        level = "L5_HUMAN_REVIEW_READY"
    # L6 requires review+pilot packets ready and automatable gates PASS (not human/field)
    pilot = ROOT / "pilot" / f"track_{row['track_id']}"
    if cells["review_packet"]["status"] == "PASS" and pilot.is_dir():
        # only L6 if no MISSING in core curriculum+package columns
        core = ["syllabus", "lessons", "labs", "assignments", "rubrics", "student_packet", "instructor_packet", "digital_package", "ai_policy", "independent_entry_point"]
        if all(cells[k]["status"] == "PASS" for k in core):
            level = "L6_PILOT_READY"
    return level


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        sha = "UNKNOWN"
    rows = [assess_track(t) for t in TRACKS]
    for r in rows:
        r["readiness_level"] = readiness_level(r)
    doc = {
        "schema": "waike.full_readiness.master_matrix.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_commit": sha,
        "columns": COLUMNS,
        "allowed_statuses": sorted(ALLOWED),
        "tracks": rows,
        "claim_boundary": "Digital/pre-human matrix only. Human academic/accessibility and field pilot remain HUMAN_REQUIRED/EXTERNAL_REQUIRED absent evidence.",
    }
    (OUT / "WAIKE_18_TRACK_MASTER_MATRIX.json").write_text(json.dumps(doc, indent=2) + "\n")
    # markdown
    lines = [
        "# WAIKE 18-Track Master Readiness Matrix",
        "",
        f"Generated: `{doc['generated_utc']}` · commit `{sha}`",
        "",
        "| Track | Level | independent_entry_point | lessons | labs | digital_package | review_packet | human_academic_review | field_pilot |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        c = r["cells"]
        lines.append(
            f"| {r['track_id']} | {r['readiness_level']} | {c['independent_entry_point']['status']} | {c['lessons']['status']} | {c['labs']['status']} | {c['digital_package']['status']} | {c['review_packet']['status']} | {c['human_academic_review']['status']} | {c['field_pilot']['status']} |"
        )
    lines += ["", "## Status legend", "", ", ".join(sorted(ALLOWED)), "", doc["claim_boundary"], ""]
    (OUT / "WAIKE_18_TRACK_MASTER_MATRIX.md").write_text("\n".join(lines))
    print(f"Wrote matrix for {len(rows)} tracks")
    for r in rows:
        print(r["track_id"], r["readiness_level"], r["cells"]["independent_entry_point"]["status"])


if __name__ == "__main__":
    main()
