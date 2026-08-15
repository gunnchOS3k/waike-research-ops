"""Dynamic corpus inventory — courses, assessments, labs, skill graph inputs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .discover import discover_courses
from .registry import build_assessable_registry
from .skill_graph import build_skill_graph

ROOT = Path(__file__).resolve().parents[2]


def _count_glob(base: Path, pattern: str) -> int:
    return sum(1 for _ in base.glob(pattern)) if base.exists() else 0


def inventory_course(course_dir: Path) -> dict[str, Any]:
    weeks = sorted((course_dir / "weeks").glob("w*")) if (course_dir / "weeks").is_dir() else []
    lessons = sum(1 for w in weeks if (w / "lesson.md").is_file())
    readings = _count_glob(course_dir, "weeks/*/reading*.md") + _count_glob(course_dir, "readings/**/*.md")
    quizzes = _count_glob(course_dir, "quizzes/q*.json")
    labs = (
        sum(1 for p in (course_dir / "labs").iterdir() if p.is_dir() and (p / "README.md").is_file())
        if (course_dir / "labs").is_dir()
        else 0
    )
    assessments = {
        name: (course_dir / "assessments" / name).is_file()
        for name in ("mid_course.json", "final_knowledge.json", "final_practical.json")
    }
    assignments = _count_glob(course_dir, "assignments/**/*.md") + _count_glob(course_dir, "weeks/*/assignment*.md")
    projects = _count_glob(course_dir, "projects/**/*") + _count_glob(course_dir, "capstone/**/*")
    rubrics = _count_glob(course_dir, "rubrics/**/*")
    return {
        "course_id": course_dir.name,
        "units_weeks": len(weeks),
        "lessons": lessons,
        "readings": readings,
        "quiz_files": quizzes,
        "labs": labs,
        "assignments": assignments,
        "midterm": assessments["mid_course.json"],
        "final_knowledge": assessments["final_knowledge.json"],
        "final_practical": assessments["final_practical.json"],
        "projects_capstones_files": projects,
        "rubrics_files": rubrics,
        "has_instructor_keys": (course_dir / "instructor" / "answer_keys.json").is_file(),
    }


def build_corpus_inventory(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    courses = discover_courses(root)
    base = root / "curriculum" / "digital_rc"
    per = [inventory_course(base / c["course_id"]) for c in courses if (base / c["course_id"]).is_dir()]
    registry = build_assessable_registry(root)
    graph = build_skill_graph(root)
    course_ids = [c["course_id"] for c in courses]
    blob = json.dumps(
        {"course_ids": course_ids, "item_count": registry["item_count"], "per_course": registry["per_course"]},
        sort_keys=True,
    )
    return {
        "schema": "waike.corpus_inventory.v1",
        "method": "filesystem_scan",
        "hardcoded_course_names": False,
        "course_count": len(courses),
        "course_ids": course_ids,
        "assessable_items": registry["item_count"],
        "per_course_assessable": registry["per_course"],
        "per_course_inventory": per,
        "totals": {
            "units_weeks": sum(p["units_weeks"] for p in per),
            "lessons": sum(p["lessons"] for p in per),
            "readings": sum(p["readings"] for p in per),
            "quiz_files": sum(p["quiz_files"] for p in per),
            "labs": sum(p["labs"] for p in per),
            "assignments": sum(p["assignments"] for p in per),
            "midterms": sum(1 for p in per if p["midterm"]),
            "finals_knowledge": sum(1 for p in per if p["final_knowledge"]),
            "finals_practical": sum(1 for p in per if p["final_practical"]),
            "projects_capstones_files": sum(p["projects_capstones_files"] for p in per),
            "rubrics_files": sum(p["rubrics_files"] for p in per),
        },
        "skill_graph_nodes": graph["node_count"],
        "skill_graph_edges": graph["edge_count"],
        "corpus_hash_sha256": hashlib.sha256(blob.encode()).hexdigest(),
        "ai_policy": {
            "may_read_instructor_keys_in_mastery_solve": False,
            "self_grading_forbidden": True,
            "educator_hitl_required": True,
        },
    }
