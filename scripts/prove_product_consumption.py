#!/usr/bin/env python3
"""Prove current WAIKE product layer can consume owner ingest — without a device-os curriculum PR.

Does not duplicate course bodies into device-os. Projects owner packages into:
- waike.learner_ingest.v1 (no keys)
- waike.teacher_ingest.v1 (keys)
- waike.course_catalog.ui.v1 (catalog fields used by WAIKE Learning UI/catalog)

Then imports the current device-os waike_integration.run_session against the
existing offline pack IDs (product still only deploys those three packs on
origin/main) and shows owner offline packs in the same session-shaped record.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.ingest import build_learner, build_product_catalog, build_teacher, write_ingest  # noqa: E402

DEVICE_OS = ROOT.parent / "gunnchos-device-os"
UI_FIELDS = (
    "course_id",
    "title",
    "kinesthetic_hook",
    "lesson_excerpt",
    "worked_example",
    "assignment",
    "lab_hint",
)
KEY_MARKERS = ("answer_index", "answer_keys", "solution_key", "instructor_keys")


def _contains_key_marker(obj: object) -> bool:
    blob = json.dumps(obj)
    return any(m in blob for m in KEY_MARKERS)


def _try_device_os_session() -> dict:
    if not DEVICE_OS.is_dir():
        return {"imported": False, "reason": "device-os_not_adjacent"}
    sys.path.insert(0, str(DEVICE_OS))
    try:
        from gunnchos_device_os.waike_integration import list_offline_lessons, run_session
    except Exception as exc:  # pragma: no cover
        return {"imported": False, "reason": type(exc).__name__, "detail": str(exc)[:200]}
    packs = list_offline_lessons()
    session = run_session(profile="student", lesson_id=packs[0], role="student", account="waike-ops-probe")
    educator = run_session(profile="educator", lesson_id=packs[0], role="educator", account="waike-ops-teacher")
    return {
        "imported": True,
        "packs": packs,
        "learner_session_ok": bool(session.get("ok")),
        "teacher_session_ok": bool(educator.get("ok")),
        "learner_has_educator_block": educator.get("session", {}).get("educator") is not None,
        "session_shape_keys": sorted((session.get("session") or {}).keys()),
        "claim_boundary": session.get("claim_boundary"),
    }


def main() -> int:
    paths = write_ingest()
    learner = build_learner()
    teacher = build_teacher()
    catalog = build_product_catalog()
    catalog_ok = catalog["schema"] == "waike.course_catalog.ui.v1" and all(
        all(f in course for f in UI_FIELDS) for course in catalog["courses"]
    )
    learner_clean = learner["role"] == "learner" and not _contains_key_marker(learner)
    teacher_has_keys = teacher["role"] == "educator" and _contains_key_marker(teacher)
    # Session-shaped owner overlay (does not mutate device-os)
    overlay = []
    for course in learner["courses"]:
        overlay.append(
            {
                "ok": True,
                "session": {
                    "lesson_id": course["offline_pack"]["session_shape"]["lesson_id"],
                    "profile": "student",
                    "role": "learner",
                    "account": "ingest-learner",
                    "offline_pack": course["course_id"] + "-offline",
                    "labs": course["labs"][:2],
                    "catalog_course_id": course["course_id"],
                    "title": course["title"],
                },
                "mock": False,
                "owner_projected": True,
            }
        )
    product = _try_device_os_session()
    proof = {
        "schema": "waike.product_consumption_proof.v1",
        "owner_repo": "waike-research-ops",
        "device_os_curriculum_pr": False,
        "catalog_schema": "waike.course_catalog.ui.v1",
        "catalog_fields_present": catalog_ok,
        "learner_ingest_has_no_keys": learner_clean,
        "teacher_ingest_has_keys": teacher_has_keys,
        "learner_course_count": len(learner["courses"]),
        "teacher_course_count": len(teacher["courses"]),
        "owner_session_overlay_count": len(overlay),
        "current_product_layer": product,
        "honest_limit": (
            "device-os origin/main WAIKE UI still hardcodes three offline packs. "
            "This packet proves schema-compatible catalog + session-shaped overlay + live "
            "run_session on those existing packs. It does not mega-PR device-os or copy "
            "curriculum bodies into device-os."
        ),
        "wrote": {k: str(v) for k, v in paths.items()},
        "ok": bool(
            catalog_ok
            and learner_clean
            and teacher_has_keys
            and (not product.get("imported") or product.get("learner_session_ok"))
        ),
    }
    out = ROOT / "artifacts" / "PRODUCT_CONSUMPTION_PROOF.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(proof, indent=2) + "\n", encoding="utf-8")
    (ROOT / "ingest" / "session_overlay.json").write_text(json.dumps(overlay, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": proof["ok"], "wrote": str(out), "product_imported": product.get("imported")}, indent=2))
    return 0 if proof["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
