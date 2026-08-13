#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402


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
        earned = (
            c["syllabus"] >= 1
            and c["weeks"] >= 8
            and c["full_lessons"] >= 8
            and c["assignments"] >= 8
            and c["runnable_labs"] >= 4
            and c["quizzes"] >= 8
            and c["quiz_items"] >= 48
            and c["mid_course_items"] >= 8
            and c["final_items"] >= 8
            and c["practicals"] >= 1
            and c["projects"] >= 1
            and c["rubrics"] >= 4
            and labs["ok"]
            and prov["status"] == "PASS"
            and tmpl["BATCH_TEMPLATED_COURSES"] == 0
            and tmpl["BATCH_STUB_COURSES"] == 0
        )
        per_course[cid] = {
            **c,
            "benchmark_sources": len(registry["sources"]),
            "provenance_status": prov["status"],
            "template_status": "ORIGINAL" if tmpl["status"] == "PASS" else "TEMPLATED_OR_STUB",
            "COURSE_DIGITAL_RC": bool(earned),
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
        "product_consumption_ok": proof["ok"],
        "registry_size": len(registry["sources"]),
        "claim_boundary": (
            "COURSE_DIGITAL_RC is earned only for this 3-course batch if labs, provenance, "
            "and depth gates pass. Not a student/teacher E6. Not all 18 courses."
        ),
    }
    out = ROOT / "artifacts" / "COURSE_DIGITAL_RC.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"COURSE_DIGITAL_RC_BATCH": batch_ok, "wrote": str(out)}, indent=2))
    return 0 if batch_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
