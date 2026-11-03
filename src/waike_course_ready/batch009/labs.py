"""Runnable labs for batch009 — the four catalog tracks that were alias-only.

Each course owns ten labs that recompute their answers; a memorized number with
altered inputs fails.
"""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch009 import labs_dco, labs_ish, labs_nif, labs_soc
from waike_course_ready.batch009.content import BATCH_COURSE_IDS

_MODULES = {
    labs_soc.COURSE: (labs_soc, "SOC"),
    labs_dco.COURSE: (labs_dco, "DCO"),
    labs_ish.COURSE: (labs_ish, "ISH"),
    labs_nif.COURSE: (labs_nif, "NIF"),
}

LABS_009: dict[str, Any] = {}
COURSE_LABS_009: dict[str, list[str]] = {}
REFERENCE_009: dict[str, dict[str, Any]] = {}
WRONG_009: dict[str, dict[str, Any]] = {}
LAB_SPECS_009: dict[str, dict[str, Any]] = {}
for _course in BATCH_COURSE_IDS:
    _mod, _tag = _MODULES[_course]
    LABS_009.update(getattr(_mod, f"LABS_{_tag}"))
    COURSE_LABS_009[_course] = list(getattr(_mod, f"LAB_ORDER_{_tag}"))
    REFERENCE_009.update(getattr(_mod, f"REFERENCE_{_tag}"))
    WRONG_009.update(getattr(_mod, f"WRONG_{_tag}"))
    for _lab_id, _spec in getattr(_mod, f"LAB_SPECS_{_tag}").items():
        LAB_SPECS_009[_lab_id] = {**_spec, "course_id": _course, "required_keys": []}

# One dishonest field on an otherwise-correct reference; each must fail.
_NEGATIVES: dict[str, list[tuple[str, dict[str, Any]]]] = {
    labs_soc.COURSE: [
        ("lab_soc_shift_handoff", {"offensive_tooling": True}),
        ("lab_soc_attack_map", {"actor_attribution_claim": True}),
        ("lab_soc_detection_metrics", {"needs_tuning": False}),
    ],
    labs_dco.COURSE: [
        ("lab_dco_safety_plan", {"real_passwords_included": True}),
        ("lab_dco_link_check", {"safe_to_open": True}),
        ("lab_dco_backup_321", {"restore_tested": False}),
    ],
}


def negatives_009() -> list[dict[str, Any]]:
    rows = []
    for course in BATCH_COURSE_IDS:
        for lab_id, override in _NEGATIVES[course]:
            res = LABS_009[lab_id]({**REFERENCE_009[lab_id], **override})
            rows.append({"lab_id": f"{lab_id}_negative", "ok": not res.ok})
    return rows
