#!/usr/bin/env python3
"""Honest COURSE_DIGITAL_RC writer. File presence and week counts are not PASS."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402
from waike_course_ready.provenance import strip_lesson_padding  # noqa: E402

BATCH_001 = ("GENERAL_IT", "COMPUTER_NETWORKING", "CYBERSECURITY")


def _lesson_depth_ok(cid: str) -> tuple[bool, list[str]]:
    """Reject operator-note padding; require stripped lesson ≥800 chars."""
    reasons: list[str] = []
    course = COURSES.get(cid) or {}
    for w in course.get("weeks") or []:
        raw = w.get("lesson") or ""
        low = raw.lower()
        if "operator note: record evidence before changing shared systems" in low:
            reasons.append(f"week {w.get('week')}: operator-note depth padding")
        if "evidence discipline week" in low:
            reasons.append(f"week {w.get('week')}: evidence-discipline depth padding")
        if "evidence for this week lives in the submitted lab json" in low:
            reasons.append(f"week {w.get('week')}: lab-JSON-evidence depth padding")
        if "not in a screenshot of a green checkmark" in low:
            reasons.append(f"week {w.get('week')}: green-checkmark evidence padding")
        if "detail mark" in low:
            reasons.append(f"week {w.get('week')}: Detail-mark trailer padding")
        if "operators keep a numbered ticket trail for" in low:
            reasons.append(f"week {w.get('week')}: rotating ticket-trail trailer padding")
        if "whiteboard the worked numbers before opening any gui" in low:
            reasons.append(f"week {w.get('week')}: whiteboard-trailer padding")
        if "if a volunteer asks for a certificate selfie" in low:
            reasons.append(f"week {w.get('week')}: certificate-selfie trailer padding")
        if "ticket arithmetic checkpoint" in low:
            reasons.append(f"week {w.get('week')}: Ticket-arithmetic checkpoint trailer padding")
        if "restate the worked example in your own symbols" in low:
            reasons.append(f"week {w.get('week')}: worked-example-checkpoint trailer padding")
        stripped = strip_lesson_padding(raw)
        if len(stripped) < 800:
            reasons.append(f"week {w.get('week')}: stripped lesson {len(stripped)} < 800")
        # Prefer #45 post-collapse floor for new batches (871) when course is batch-004.
        if cid in ("WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE", "COMM_PD_ETHICS", "DATA_DASHBOARDS") and len(stripped) < 871:
            reasons.append(f"week {w.get('week')}: stripped lesson {len(stripped)} < 871 (#45 floor)")
    return (not reasons), reasons


def _earned(cid: str, c: dict, labs: dict, prov: dict, tmpl: dict, proof: dict) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    def need(ok: bool, msg: str) -> None:
        if not ok:
            reasons.append(msg)

    need(c.get("syllabus", 0) >= 1, "syllabus < 1")
    need(c.get("weeks", 0) >= 10, "weeks < 10")
    need(c.get("full_lessons", 0) >= 10, "full_lessons < 10")
    need(c.get("assignments", 0) >= 10, "assignments < 10")
    need(c.get("runnable_labs", 0) >= 6, "runnable_labs < 6")
    need(c.get("quizzes", 0) >= 10, "quizzes < 10")
    need(c.get("quiz_items", 0) >= 60, "quiz_items < 60")
    need(c.get("mid_course_items", 0) >= 20, "mid_course_items < 20")
    need(c.get("final_items", 0) >= 24, "final_items < 24")
    need(c.get("mid_course_items_original", 0) >= 20, "mid original < 20 (cloned stems)")
    need(c.get("final_items_original", 0) >= 24, "final original < 24 (cloned stems)")
    need(c.get("practicals", 0) >= 1, "practicals < 1")
    need(c.get("projects", 0) >= 1, "projects < 1")
    need(c.get("presentation_materials", 0) >= 10, "presentations < 10")
    need(c.get("student_materials", 0) >= 1, "student packet missing")
    need(c.get("instructor_materials", 0) >= 11, "instructor materials < 11")
    need(c.get("offline_pack", 0) >= 1, "offline pack missing")
    need(c.get("portfolio_artifacts", 0) >= 1, "portfolio missing")
    need(c.get("rubrics", 0) >= 8, "rubrics < 8")
    need(bool(labs.get("ok")), "lab execution bundle not ok")
    need(bool(labs.get("empty_submission_fails")), "empty student artifacts still pass")
    need(bool(labs.get("wrong_submission_fails")), "wrong student artifacts still pass")
    need(bool(labs.get("print_pass_raises")), "_fail_if_print_pass never raised")
    need(bool(labs.get("ttl1_from_parsed_header")), "TTL=1 check is tautology, not parsed header")
    need(bool(labs.get("no_submission_fails")), "no-submission golden path still passes")
    need(all(n.get("ok") for n in labs.get("negatives_must_fail_and_did") or []), "package negatives did not fail")
    # Coexistence: #43 labs must still execute when this RC writer runs on the union product path.
    need(int(labs.get("lab_count") or 0) >= 130, f"lab_count {labs.get('lab_count')} < 130 (#43∪#44∪#45∪#46∪Stream-B)")
    need(int(labs.get("batch_001_lab_count") or 0) == 20, "#43 labs orphaned from run_all")
    need(int(labs.get("batch_002_lab_count") or 0) == 30, "#44 labs orphaned from run_all")
    need(int(labs.get("batch_003_lab_count") or 0) == 30, "#45 labs orphaned from run_all")
    need(int(labs.get("batch_004_lab_count") or 0) == 30, "#46 labs orphaned from run_all")
    need(int(labs.get("batch_005_lab_count") or 0) == 10, "Stream-B COMM_PD labs orphaned from run_all")
    need(int(labs.get("batch_006_lab_count") or 0) == 10, "Stream-B DATA_DASHBOARDS labs orphaned from run_all")
    need(set(BATCH_001).issubset(set(COURSES)), "#43 courses missing from COURSES product path")
    depth_ok, depth_reasons = _lesson_depth_ok(cid)
    need(depth_ok, "lesson depth/padding: " + "; ".join(depth_reasons[:3]))
    need(int(prov.get("lesson_padding_rejected") or 0) == 0, "provenance rejected lesson padding")
    need(not (prov.get("repeated_trailer_findings") or {}).get(cid), "repeated near-identical trailers")
    need(
        int((prov.get("stripped_lesson_mins") or {}).get(cid) or 0) >= (
            871 if cid in ("WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE", "COMM_PD_ETHICS", "DATA_DASHBOARDS") else 800
        ),
        f"stripped lesson min {(prov.get('stripped_lesson_mins') or {}).get(cid)} below floor",
    )
    need(prov.get("status") == "PASS", f"provenance {prov.get('status')}")
    need(bool(prov.get("key_balance_ok")), "answer keys collapsed")
    need(bool(prov.get("exam_items_original")), "mid/final not original")
    need(int(prov.get("exam_token_identical") or 0) == 0, "token-identical exam restatements remain")
    need(int(prov.get("exam_token_jaccard_ge_0_80") or 0) == 0, "exam stems Jaccard≥0.80 vs weekly remain")
    need(tmpl.get("BATCH_TEMPLATED_COURSES") == 0, "BATCH_TEMPLATED_COURSES != 0")
    need(tmpl.get("BATCH_STUB_COURSES") == 0, "BATCH_STUB_COURSES != 0")
    need(float(prov.get("worst_packaging_jaccard") or 0) < 0.35, "packaging shells cloned")
    need(bool(proof.get("ok")), "product consumption proof failed")
    return (not reasons), reasons


def main() -> int:
    counts = json.loads((ROOT / "artifacts" / "COURSE_COUNTS.json").read_text(encoding="utf-8"))
    labs = json.loads((ROOT / "artifacts" / "LAB_EXECUTION_RESULTS.json").read_text(encoding="utf-8"))
    prov = json.loads((ROOT / "artifacts" / "CURRICULUM_PROVENANCE_AUDIT.json").read_text(encoding="utf-8"))
    tmpl = json.loads((ROOT / "artifacts" / "TEMPLATE_DETECTOR.json").read_text(encoding="utf-8"))
    proof = json.loads((ROOT / "artifacts" / "PRODUCT_CONSUMPTION_PROOF.json").read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "sources" / "benchmark_registry.json").read_text(encoding="utf-8"))
    per_course = {}
    batch_ok = True
    for cid in COURSES:
        c = counts[cid]
        earned, reasons = _earned(cid, c, labs, prov, tmpl, proof)
        per_course[cid] = {
            **c,
            "benchmark_sources": len(registry["sources"]),
            "provenance_status": prov["status"],
            "template_status": "ORIGINAL" if tmpl["status"] == "PASS" else "TEMPLATED_OR_STUB",
            "key_balance_ok": prov.get("key_balance_ok"),
            "exam_items_original": prov.get("exam_items_original"),
            "COURSE_DIGITAL_RC": bool(earned),
            "rc_fail_reasons": reasons,
        }
        batch_ok = batch_ok and earned
    payload = {
        "packet": "STREAM-B-PKT-003",
        "COURSE_DIGITAL_RC_BATCH": batch_ok,
        "DATA_DASHBOARDS_COURSE_DIGITAL_RC": bool(
            (per_course.get("DATA_DASHBOARDS") or {}).get("COURSE_DIGITAL_RC")
        ),
        "REAL_STUDENT_E6": False,
        "REAL_TEACHER_E6": False,
        "HUMAN_E6": False,
        "full_18_course_digital_rc": False,
        "device_os_curriculum_pr": False,
        "courses": per_course,
        "lab_execution_ok": labs["ok"],
        "lab_count": labs["lab_count"],
        "empty_submission_fails": labs.get("empty_submission_fails"),
        "wrong_submission_fails": labs.get("wrong_submission_fails"),
        "print_pass_raises": labs.get("print_pass_raises"),
        "ttl1_from_parsed_header": labs.get("ttl1_from_parsed_header"),
        "product_consumption_ok": proof["ok"],
        "registry_size": len(registry["sources"]),
        "key_distribution": prov.get("key_distribution"),
        "worst_packaging_jaccard": prov.get("worst_packaging_jaccard"),
        "exam_token_identical": prov.get("exam_token_identical"),
        "exam_token_jaccard_ge_0_80": prov.get("exam_token_jaccard_ge_0_80"),
        "worst_exam_weekly_token_jaccard": prov.get("worst_exam_weekly_token_jaccard"),
        "claim_boundary": (
            "COURSE_DIGITAL_RC is earned only when original mid/final items, balanced keys, "
            "non-cloned packaging, stripped lesson depth ≥800 without operator-note padding, "
            "and labs that fail empty/wrong/print-PASS all hold. Product path keeps #43 "
            "(IT/Networking/Cyber) ∪ #44 (Software/Hardware/PM) ∪ #45 (AI/Data/Cloud) ∪ #46 "
            "(Wireless/Robotics/Game) ∪ Stream-B (COMM_PD_ETHICS ∪ DATA_DASHBOARDS). "
            "Commercial standardized 6G does not exist today. "
            "Not a student/teacher E6. Not all 18 courses."
        ),
    }
    out = ROOT / "artifacts" / "COURSE_DIGITAL_RC.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"COURSE_DIGITAL_RC_BATCH": batch_ok, "wrote": str(out)}, indent=2))
    return 0 if batch_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
