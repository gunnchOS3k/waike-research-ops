"""Isolated grading agent — loads instructor keys only after submission, never for solving."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def load_answer_keys(course_id: str, root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    path = root / "curriculum" / "digital_rc" / course_id / "instructor" / "answer_keys.json"
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def grade_mcq_submission(
    course_id: str,
    assessment_kind: str,
    assessment_id: str,
    answers: dict[str, int],
    root: Path | None = None,
) -> dict[str, Any]:
    """Grade a submitted answer map. Keys are loaded here — not by the solver."""
    keys = load_answer_keys(course_id, root)
    if assessment_kind == "quiz":
        key_items = keys.get("quizzes", {}).get(assessment_id) or []
    elif assessment_kind == "mid":
        key_items = keys.get("mid") or []
    elif assessment_kind == "final":
        key_items = keys.get("final") or []
    else:
        raise ValueError(f"unknown assessment_kind={assessment_kind}")

    detail = []
    correct = 0
    for item in key_items:
        iid = item["id"]
        expected = int(item["answer_index"])
        got = answers.get(iid)
        ok = got is not None and int(got) == expected
        if ok:
            correct += 1
        detail.append({"id": iid, "ok": ok, "expected": expected, "got": got})
    total = len(key_items)
    return {
        "course_id": course_id,
        "assessment_id": assessment_id,
        "assessment_kind": assessment_kind,
        "correct": correct,
        "total": total,
        "score": (correct / total) if total else 0.0,
        "self_graded": False,
        "grader": "isolated_grading_agent",
        "items": detail,
    }
