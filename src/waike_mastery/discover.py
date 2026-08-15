"""Discover digital RC courses from the filesystem — no hardcoded course-name list."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DIGITAL_RC = ROOT / "curriculum" / "digital_rc"

CONTRACT_SCHEMA = "waike.gunnchai.learning_contract.v1"


def discover_courses(root: Path | None = None) -> list[dict[str, Any]]:
    base = (root or ROOT) / "curriculum" / "digital_rc"
    courses: list[dict[str, Any]] = []
    if not base.is_dir():
        return courses
    for course_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        course_json = course_dir / "course.json"
        if not course_json.is_file():
            continue
        data = json.loads(course_json.read_text(encoding="utf-8"))
        quizzes = sorted((course_dir / "quizzes").glob("q*.json")) if (course_dir / "quizzes").is_dir() else []
        labs = sorted(
            p.name
            for p in (course_dir / "labs").iterdir()
            if p.is_dir() and (p / "README.md").is_file()
        ) if (course_dir / "labs").is_dir() else []
        assessments = []
        for name in ("mid_course.json", "final_knowledge.json", "final_practical.json"):
            p = course_dir / "assessments" / name
            if p.is_file():
                assessments.append(f"assessments/{name}")
        courses.append(
            {
                "course_id": data.get("course_id") or course_dir.name,
                "title": data.get("title") or course_dir.name,
                "path": str(course_dir.relative_to(root or ROOT)),
                "academy_id": data.get("academy_id"),
                "track_ids": data.get("track_ids") or [],
                "weeks": len(data.get("weeks") or []),
                "quiz_files": [str(q.relative_to(course_dir)) for q in quizzes],
                "lab_ids": labs,
                "assessment_files": assessments,
                "has_instructor_keys": (course_dir / "instructor" / "answer_keys.json").is_file(),
                "student_facing_course_json": True,
            }
        )
    return courses


def emit_learning_contract(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    courses = discover_courses(root)
    return {
        "schema": CONTRACT_SCHEMA,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "owner_repo": "waike-research-ops",
        "consumer_repo": "gunnchAI3k",
        "discovery": {
            "method": "filesystem_scan",
            "glob": "curriculum/digital_rc/*/course.json",
            "hardcoded_course_names": False,
            "course_count": len(courses),
        },
        "permissions": {
            "MASTERY_BENCHMARK": {
                "may_read_student_materials": True,
                "may_read_instructor_keys": False,
                "may_self_grade": False,
                "grading_agent": "isolated_after_submission",
            },
            "LEARNER_TUTOR": {
                "may_read_student_materials": True,
                "may_read_instructor_keys": False,
                "may_disclose_answers": False,
                "socratic_default": True,
            },
            "EDUCATOR_COPILOT": {
                "may_read_student_materials": True,
                "may_read_instructor_keys": True,
                "hitl_grading_required": True,
                "may_publish_grades_without_human": False,
            },
        },
        "courses": courses,
        "claim_boundary": (
            "Machine-readable WAIKE↔gunnchAI learning contract from discoverable digital RC courses. "
            "Not an accredited program; not a claim that a live student/teacher cohort was evaluated."
        ),
    }
