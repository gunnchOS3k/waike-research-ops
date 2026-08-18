"""Build pathway overlays from on-disk digital-RC packages.

Counts come from filesystem discovery. Do not hardcode a course universe.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DIGITAL_RC = ROOT / "curriculum" / "digital_rc"
PATHWAY_SCHEMA = "waike.pathway.v1"
COMPLETION_SCHEMA = "waike.completion_tracking.v1"

PII_KEYS = {"email", "name", "grade", "transcript", "gpa", "student_id", "ssn", "password"}


def discover_course_dirs(root: Path | None = None) -> list[Path]:
    base = (root or ROOT) / "curriculum" / "digital_rc"
    if not base.is_dir():
        return []
    return sorted(p for p in base.iterdir() if p.is_dir() and (p / "course.json").is_file())


def load_course(course_dir: Path) -> dict[str, Any]:
    return json.loads((course_dir / "course.json").read_text(encoding="utf-8"))


def load_prereqs(course_dir: Path, course_id: str) -> dict[str, Any]:
    path = course_dir / "prerequisites.json"
    if not path.is_file():
        raise FileNotFoundError(f"missing prerequisites.json for {course_id}: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("course_id") != course_id:
        raise ValueError(f"prerequisites course_id mismatch: {data.get('course_id')} != {course_id}")
    required = data.get("required")
    recommended = data.get("recommended")
    if not isinstance(required, list) or not isinstance(recommended, list):
        raise ValueError(f"prerequisites lists missing for {course_id}")
    return {
        "course_id": course_id,
        "required": required,
        "recommended": recommended,
    }


def build_pathway(course_dir: Path) -> dict[str, Any]:
    course = load_course(course_dir)
    course_id = course["course_id"]
    weeks = course["weeks"]
    week1 = weeks[0]
    lesson = week1["lesson"]
    student_ref = course["student_materials_ref"]
    instructor_ref = course["instructor_materials_ref"]
    if not (course_dir / student_ref).is_file():
        raise FileNotFoundError(student_ref)
    if not (course_dir / instructor_ref).is_file():
        raise FileNotFoundError(instructor_ref)
    lessons = []
    for w in weeks:
        les = w["lesson"]
        body_ref = f"weeks/w{w['week']:02d}/lesson.md"
        lessons.append(
            {
                "week": w["week"],
                "lesson_id": les["lesson_id"],
                "title": les["title"],
                "body_ref": body_ref,
            }
        )
    return {
        "schema": PATHWAY_SCHEMA,
        "course_id": course_id,
        "title": course["title"],
        "start": {
            "student_packet_ref": student_ref,
            "kinesthetic_hook": course["kinesthetic_hook"],
            "week_1_title": lesson["title"],
        },
        "prereqs": load_prereqs(course_dir, course_id),
        "objectives": [w["lesson"]["title"] for w in weeks],
        "lessons": lessons,
        "labs": list(course["labs"]),
        "assessment": {
            "quizzes_ref": list(course["quizzes"]),
            "assessments": dict(course["assessments"]),
        },
        "rubrics": list(course["rubrics"]),
        "completion_tracking": {
            "schema": COMPLETION_SCHEMA,
            "mode": "anonymous_artifact_checklist",
            "pii_forbidden": True,
        },
        "instructor_guidance": {
            "instructor_packet_ref": instructor_ref,
        },
    }


def build_all_pathways(root: Path | None = None) -> list[dict[str, Any]]:
    dirs = discover_course_dirs(root)
    return [build_pathway(d) for d in dirs]


def anonymous_completion(
    course_id: str,
    week: int,
    artifact_id: str,
    *,
    lab_id: str | None = None,
    lab_ok: bool | None = None,
    opaque_learner_ref: str = "fixture-learner",
) -> dict[str, Any]:
    record = {
        "schema": COMPLETION_SCHEMA,
        "course_id": course_id,
        "week": week,
        "artifact_id": artifact_id,
        "artifact_submitted": True,
        "opaque_learner_ref": opaque_learner_ref,
    }
    if lab_id is not None:
        record["lab_id"] = lab_id
    if lab_ok is not None:
        record["lab_ok"] = lab_ok
    leaked = PII_KEYS.intersection(record)
    if leaked:
        raise ValueError(f"PII keys forbidden: {leaked}")
    if "@" in opaque_learner_ref:
        raise ValueError("opaque_learner_ref must not look like an email")
    return record
