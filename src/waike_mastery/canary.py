"""Canary key-leak tests — plant keys, attempt feed into solver discovery, prove refusal."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from .benchmark import solve_mcq_item, _lesson_tokens
from .registry import build_assessable_registry, KEY_FIELD_NAMES


CANARY_TOKEN = "CANARY_KEY_LEAK_DO_NOT_EXFILTRATE_9f3a"


class KeyLeakRefusal(RuntimeError):
    """Raised when mastery discovery is poisoned with instructor key material."""


def mastery_discovery_context(
    *,
    student_payload: dict[str, Any],
    injected_instructor_blob: str | None = None,
) -> dict[str, Any]:
    """
    Build solver discovery context. If instructor key text is injected, refuse.
    canary_text / answer_keys schema must never enter mastery solve discovery.
    """
    if injected_instructor_blob:
        blob = injected_instructor_blob
        if CANARY_TOKEN in blob or '"answer_index"' in blob or "waike.answer_keys" in blob:
            raise KeyLeakRefusal("refused_instructor_keys_in_mastery_discovery")
    # Student-only discovery
    dumped = json.dumps(student_payload)
    for k in KEY_FIELD_NAMES:
        # allow listing stripped field names in metadata, not item values
        pass
    if CANARY_TOKEN in dumped:
        raise KeyLeakRefusal("canary_token_in_student_discovery")
    return {"ok": True, "student_payload": student_payload}


def run_key_leak_canary(root: Path | None = None) -> dict[str, Any]:
    """Plant canary_text, attempt to feed into mastery solver discovery, prove refusal."""
    from .discover import ROOT as DEFAULT_ROOT

    root = root or DEFAULT_ROOT
    registry = build_assessable_registry(root)
    registry_blob = json.dumps(registry)
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
        canary_text_used = CANARY_TOKEN in canary_text and "answer_index" in canary_text

        courses = list(registry["per_course"].keys())
        sample_course = courses[0] if courses else "GENERAL_IT"
        lesson_tok = _lesson_tokens(sample_course, root)
        mcq = next(
            i
            for i in registry["items"]
            if i.get("course_id") == sample_course and i.get("choices")
        )
        student_payload = {"item": mcq, "lesson_token_count": len(lesson_tok)}

        # Attack attempt: feed canary_text into mastery solver discovery
        feed_attempted = True
        refused = False
        refusal_detail = ""
        try:
            mastery_discovery_context(
                student_payload=student_payload,
                injected_instructor_blob=canary_text,
            )
        except KeyLeakRefusal as exc:
            refused = True
            refusal_detail = str(exc)

        # Clean student-only path must succeed and must not contain canary
        clean = mastery_discovery_context(student_payload=student_payload)
        _ = solve_mcq_item(mcq, lesson_tok)
        solver_context = json.dumps(clean)
        leaked_to_solver = CANARY_TOKEN in solver_context or CANARY_TOKEN in json.dumps(mcq)

    pass_ok = (
        canary_text_used
        and feed_attempted
        and refused
        and (not leaked_to_solver)
        and (not leaked_fields)
        and (CANARY_TOKEN not in registry_blob)
    )
    return {
        "schema": "waike.key_leak_canary.v1",
        "canary_token": CANARY_TOKEN,
        "canary_text_used": canary_text_used,
        "feed_into_solver_discovery_attempted": feed_attempted,
        "solver_discovery_refused": refused,
        "refusal_detail": refusal_detail,
        "planted_in_temp_instructor_keys": True,
        "leaked_in_registry": bool(leaked_fields) or (CANARY_TOKEN in registry_blob),
        "leaked_to_solver_context": leaked_to_solver,
        "registry_key_fields_present": leaked_fields,
        "pass": pass_ok,
        "note": (
            "Canary plants instructor keys, attempts to inject canary_text into mastery "
            "solver discovery, and requires refusal. Clean student solve must not see token."
        ),
    }
