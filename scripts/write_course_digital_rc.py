#!/usr/bin/env python3
"""Honest COURSE_DIGITAL_RC writer. File presence and week counts are not PASS."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402


def _earned(cid: str, c: dict, labs: dict, prov: dict, tmpl: dict, proof: dict) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    def need(ok: bool, msg: str) -> None:
        if not ok:
            reasons.append(msg)

    need(c.get("syllabus", 0) >= 1, "syllabus < 1")
    need(c.get("weeks", 0) >= 8, "weeks < 8")
    need(c.get("full_lessons", 0) >= 8, "full_lessons < 8")
    need(c.get("assignments", 0) >= 8, "assignments < 8")
    need(c.get("runnable_labs", 0) >= 4, "runnable_labs < 4")
    need(c.get("quizzes", 0) >= 8, "quizzes < 8")
    need(c.get("quiz_items", 0) >= 48, "quiz_items < 48")
    need(c.get("mid_course_items", 0) >= 20, "mid_course_items < 20")
    need(c.get("final_items", 0) >= 24, "final_items < 24")
    need(c.get("mid_course_items_original", 0) >= 20, "mid original < 20 (cloned stems)")
    need(c.get("final_items_original", 0) >= 24, "final original < 24 (cloned stems)")
    need(c.get("practicals", 0) >= 1, "practicals < 1")
    need(c.get("projects", 0) >= 1, "projects < 1")
    need(c.get("rubrics", 0) >= 4, "rubrics < 4")
    need(bool(labs.get("ok")), "lab execution bundle not ok")
    need(bool(labs.get("empty_submission_fails")), "empty student artifacts still pass")
    need(bool(labs.get("wrong_submission_fails")), "wrong student artifacts still pass")
    need(bool(labs.get("print_pass_raises")), "_fail_if_print_pass never raised")
    need(bool(labs.get("ttl1_from_parsed_header")), "TTL=1 check is tautology, not parsed header")
    need(bool(labs.get("no_submission_fails")), "no-submission golden path still passes")
    need(all(n.get("ok") for n in labs.get("negatives_must_fail_and_did") or []), "package negatives did not fail")
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
        "packet": "WAIKE-COURSE-READY-001",
        "COURSE_DIGITAL_RC_BATCH": batch_ok,
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
            "non-cloned packaging, and labs that fail empty/wrong/print-PASS all hold. "
            "Not a student/teacher E6. Not all 18 courses."
        ),
    }
    out = ROOT / "artifacts" / "COURSE_DIGITAL_RC.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"COURSE_DIGITAL_RC_BATCH": batch_ok, "wrote": str(out)}, indent=2))
    return 0 if batch_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
