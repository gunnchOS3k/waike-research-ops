"""Project owner packages into learner/teacher ingest and product catalog UI schema."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.labs import COURSE_LABS

ROOT = Path(__file__).resolve().parents[2]
KEY_FIELD_NAMES = (
    "answer_index",
    "answer_keys",
    "instructor_keys",
    "solution_key",
    "explanation",
    "correct",
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _strip_keys(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _strip_keys(v) for k, v in obj.items() if k not in KEY_FIELD_NAMES}
    if isinstance(obj, list):
        return [_strip_keys(x) for x in obj]
    return obj


def build_learner() -> dict[str, Any]:
    courses = []
    for cid, c in COURSES.items():
        extras = extra_assessment_items(cid)
        quizzes = []
        for w in c["weeks"]:
            quizzes.append(
                {
                    "quiz_id": f"{cid}-q{w['week']:02d}",
                    "week": w["week"],
                    "items": [{"id": i["id"], "kind": i["kind"], "stem": i["stem"], "choices": i["choices"]} for i in w["quiz"]],
                }
            )
        courses.append(
            {
                "course_id": cid,
                "title": c["title"],
                "track_ids": c["track_ids"],
                "academy_id": c["academy_id"],
                "kinesthetic_hook": c["kinesthetic_hook"],
                "lesson_excerpt": c["weeks"][0]["lesson"][:280],
                "worked_example": c["weeks"][0]["worked_example"],
                "assignment": c["weeks"][0]["assignment"],
                "lab_hint": c["weeks"][0]["lab_id"],
                "syllabus": {"weeks": 10, "hook": c["syllabus_hook"]},
                "weeks": [
                    {
                        "week": w["week"],
                        "title": w["title"],
                        "lesson_id": f"{cid}-w{w['week']:02d}",
                        "body_md": w["lesson"],
                        "worked_example": w["worked_example"],
                    }
                    for w in c["weeks"]
                ],
                "assignments": [{"id": f"a{w['week']:02d}", "prompt": w["assignment"]} for w in c["weeks"]],
                "labs": COURSE_LABS[cid],
                "quizzes": quizzes,
                "assessments": {
                    "mid_course": [{"id": i["id"], "stem": i["stem"], "choices": i["choices"]} for i in extras["mid"]],
                    "final_knowledge": [{"id": i["id"], "stem": i["stem"], "choices": i["choices"]} for i in extras["final"]],
                    "practical_labs": COURSE_LABS[cid],
                },
                "portfolio": {"no_pii": True},
                "offline_pack": {
                    "lesson_ids": [f"{cid}-w{w['week']:02d}" for w in c["weeks"]],
                    "session_shape": {
                        "lesson_id": f"{cid}-w01",
                        "role": "learner",
                        "offline_pack": f"{cid}-offline",
                        "labs": COURSE_LABS[cid][:2],
                    },
                },
            }
        )
    doc = {"schema": "waike.learner_ingest.v1", "role": "learner", "generated_utc": _now(), "courses": courses}
    return _strip_keys(doc)


def build_teacher() -> dict[str, Any]:
    learner = build_learner()
    courses = []
    for raw, src in zip(learner["courses"], COURSES.values(), strict=True):
        cid = raw["course_id"]
        extras = extra_assessment_items(cid)
        keys = {
            "quizzes": {
                f"{cid}-q{w['week']:02d}": [
                    {"id": i["id"], "answer_index": i["answer_index"], "explanation": i["explanation"]}
                    for i in w["quiz"]
                ]
                for w in src["weeks"]
            },
            "mid": [{"id": i["id"], "answer_index": i["answer_index"]} for i in extras["mid"]],
            "final": [{"id": i["id"], "answer_index": i["answer_index"]} for i in extras["final"]],
        }
        teacher_course = dict(raw)
        teacher_course["answer_keys"] = keys
        teacher_course["rubrics"] = [f"{cid}-lab", f"{cid}-assignment", f"{cid}-practical", f"{cid}-project"]
        teacher_course["instructor_notes"] = "Keys stay out of learner ingest. Run labs with computing validators."
        teacher_course["presentation"] = [f"week_{w['week']:02d}.md" for w in src["weeks"]]
        courses.append(teacher_course)
    return {
        "schema": "waike.teacher_ingest.v1",
        "role": "educator",
        "generated_utc": _now(),
        "courses": courses,
    }


def build_product_catalog() -> dict[str, Any]:
    """waike.course_catalog.ui.v1 — fields the current WAIKE catalog renderer expects."""
    courses = []
    for cid, c in COURSES.items():
        courses.append(
            {
                "course_id": cid,
                "title": c["title"],
                "kinesthetic_hook": c["kinesthetic_hook"],
                "lesson_excerpt": c["weeks"][0]["lesson"].split("\n\n")[0][:400],
                "worked_example": c["weeks"][0]["worked_example"],
                "assignment": c["weeks"][0]["assignment"],
                "lab_hint": c["weeks"][0]["lab_id"],
                "track_ids": c["track_ids"],
                "academy_id": c["academy_id"],
            }
        )
    return {
        "schema": "waike.course_catalog.ui.v1",
        "full_curriculum_complete": False,
        "owner_repo": "waike-research-ops",
        "packet": "WAIKE-COURSE-READY-001",
        "courses": courses,
    }


def write_ingest() -> dict[str, Path]:
    learner = build_learner()
    teacher = build_teacher()
    catalog = build_product_catalog()
    paths = {
        "learner": ROOT / "ingest" / "learner" / "waike_learner_ingest.v1.json",
        "teacher": ROOT / "ingest" / "teacher" / "waike_teacher_ingest.v1.json",
        "catalog": ROOT / "ingest" / "waike_product_catalog.ui.v1.json",
    }
    for p, obj in (
        (paths["learner"], learner),
        (paths["teacher"], teacher),
        (paths["catalog"], catalog),
    ):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    return paths
