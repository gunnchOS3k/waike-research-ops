"""Machine-readable assessable-item registry — student stems only, no answer keys."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .discover import discover_courses

ROOT = Path(__file__).resolve().parents[2]

KEY_FIELD_NAMES = frozenset(
    {
        "answer_index",
        "answer_keys",
        "instructor_keys",
        "solution_key",
        "explanation",
        "correct",
        "correct_choice",
        "gold",
        "reference_submission",
    }
)


def _strip_keys(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _strip_keys(v) for k, v in obj.items() if k not in KEY_FIELD_NAMES}
    if isinstance(obj, list):
        return [_strip_keys(x) for x in obj]
    return obj


def _domain_for(course_id: str, kind: str) -> str:
    if kind.startswith("lab"):
        return f"{course_id}.labs"
    if kind in ("mid", "final", "quiz"):
        return f"{course_id}.knowledge"
    return f"{course_id}.other"


def build_assessable_registry(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    courses = discover_courses(root)
    items: list[dict[str, Any]] = []
    per_course: dict[str, dict[str, int]] = {}

    for meta in courses:
        cid = meta["course_id"]
        course_dir = root / meta["path"]
        counts = {"quiz": 0, "mid": 0, "final": 0, "lab": 0, "total": 0}
        # quizzes
        for qrel in meta["quiz_files"]:
            qpath = course_dir / qrel
            quiz = json.loads(qpath.read_text(encoding="utf-8"))
            for raw in quiz.get("items") or []:
                item = _strip_keys(raw)
                items.append(
                    {
                        "item_id": f"{cid}:{item.get('id')}",
                        "course_id": cid,
                        "assessment_id": quiz.get("quiz_id"),
                        "assessment_kind": "quiz",
                        "domain": _domain_for(cid, "quiz"),
                        "kind": item.get("kind") or "mcq",
                        "stem": item.get("stem"),
                        "choices": item.get("choices"),
                        "source": str(qpath.relative_to(root)),
                    }
                )
                counts["quiz"] += 1
        # mid / final
        for fname, kind in (
            ("mid_course.json", "mid"),
            ("final_knowledge.json", "final"),
        ):
            apath = course_dir / "assessments" / fname
            if not apath.is_file():
                continue
            blob = json.loads(apath.read_text(encoding="utf-8"))
            for raw in blob.get("items") or []:
                item = _strip_keys(raw)
                items.append(
                    {
                        "item_id": f"{cid}:{item.get('id')}",
                        "course_id": cid,
                        "assessment_id": blob.get("assessment_id") or f"{cid}-{kind}",
                        "assessment_kind": kind,
                        "domain": _domain_for(cid, kind),
                        "kind": item.get("kind") or "mcq",
                        "stem": item.get("stem"),
                        "choices": item.get("choices"),
                        "source": str(apath.relative_to(root)),
                    }
                )
                counts[kind] += 1
        # labs
        for lab_id in meta["lab_ids"]:
            readme = course_dir / "labs" / lab_id / "README.md"
            items.append(
                {
                    "item_id": f"{cid}:{lab_id}",
                    "course_id": cid,
                    "assessment_id": lab_id,
                    "assessment_kind": "lab",
                    "domain": _domain_for(cid, "lab"),
                    "kind": "tool_use_lab",
                    "stem": readme.read_text(encoding="utf-8")[:500] if readme.is_file() else lab_id,
                    "choices": None,
                    "source": str((course_dir / "labs" / lab_id).relative_to(root)),
                }
            )
            counts["lab"] += 1
        counts["total"] = counts["quiz"] + counts["mid"] + counts["final"] + counts["lab"]
        per_course[cid] = counts

    # prove no key leakage in registry payload
    dumped = json.dumps(items)
    leaked = [k for k in KEY_FIELD_NAMES if f'"{k}"' in dumped]
    return {
        "schema": "waike.assessable_item_registry.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "course_count": len(courses),
        "item_count": len(items),
        "per_course": per_course,
        "key_fields_stripped": sorted(KEY_FIELD_NAMES),
        "key_fields_present_in_registry": leaked,
        "self_grading_forbidden": True,
        "items": items,
        "claim_boundary": (
            "Student-facing assessable registry only. Instructor keys are not embedded. "
            "Scoring requires an isolated grading agent after submission."
        ),
    }
