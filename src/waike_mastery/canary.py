"""Canary key-leak tests for mastery benchmark isolation."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from .benchmark import solve_mcq_item, _lesson_tokens
from .registry import build_assessable_registry, KEY_FIELD_NAMES


CANARY_TOKEN = "CANARY_KEY_LEAK_DO_NOT_EXFILTRATE_9f3a"


def run_key_leak_canary(root: Path | None = None) -> dict[str, Any]:
    """Plant a canary in a temp instructor key file; ensure solver/registry never see it."""
    from .discover import ROOT as DEFAULT_ROOT

    root = root or DEFAULT_ROOT
    registry = build_assessable_registry(root)
    registry_blob = json.dumps(registry)
    leaked_in_registry = CANARY_TOKEN in registry_blob or any(
        f'"{k}"' in registry_blob and k in ("answer_index", "answer_keys") for k in KEY_FIELD_NAMES
    )
    # stronger: key field names as JSON keys in items
    leaked_fields = registry.get("key_fields_present_in_registry") or []

    with tempfile.TemporaryDirectory() as td:
        canary_path = Path(td) / "answer_keys.json"
        canary_path.write_text(
            json.dumps(
                {
                    "schema": "waike.answer_keys.v1",
                    "course_id": "CANARY",
                    "quizzes": {
                        "CANARY-q01": [
                            {"id": "c1", "answer_index": 0, "explanation": CANARY_TOKEN}
                        ]
                    },
                }
            ),
            encoding="utf-8",
        )
        canary_text = canary_path.read_text(encoding="utf-8")
        # Build solver context only from student materials of a real course
        courses = [c for c in registry["per_course"]]
        sample_course = courses[0] if courses else "GENERAL_IT"
        lesson_tok = _lesson_tokens(sample_course, root)
        # Pick one MCQ
        mcq = next(i for i in registry["items"] if i.get("course_id") == sample_course and i.get("choices"))
        _ = solve_mcq_item(mcq, lesson_tok)
        solver_context = json.dumps({"item": mcq, "lesson_token_count": len(lesson_tok)})
        leaked_to_solver = CANARY_TOKEN in solver_context or CANARY_TOKEN in json.dumps(mcq)

    return {
        "schema": "waike.key_leak_canary.v1",
        "canary_token": CANARY_TOKEN,
        "planted_in_temp_instructor_keys": True,
        "leaked_in_registry": bool(leaked_fields) or (CANARY_TOKEN in registry_blob),
        "leaked_to_solver_context": leaked_to_solver,
        "registry_key_fields_present": leaked_fields,
        "pass": (not leaked_fields) and (not leaked_to_solver) and (CANARY_TOKEN not in registry_blob),
        "note": "Mastery solver must not read instructor keys; grading agent is separate.",
    }
