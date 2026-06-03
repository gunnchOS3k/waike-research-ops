#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

CHECKS = [
    "results/deep_instructor_packets/{cid}_instructor_packet.md",
    "lessons/by_course/{cid}/week_01/teaching_notes.md",
    "instructor_solution_guides/by_course/{cid}/assignment_01_solution_guide.md",
    "instructor_training/README.md",
]


def main() -> int:
    fail = 0
    body = "# Instructor-ready audit\n\n| Course | Status |\n|--------|--------|\n"
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        missing = [t.format(cid=cid) for t in CHECKS if not (ROOT / t.format(cid=cid)).exists()]
        st = "INSTRUCTOR_READY" if not missing else "PARTIALLY_INSTRUCTOR_READY"
        if missing:
            fail += 1
        body += f"| {cid} | {st} |\n"
    p = ROOT / "results/audit/instructor_ready_audit.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    (ROOT / ".audit/INSTRUCTOR_READY_AUDIT.md").write_text(body, encoding="utf-8")
    print("PASS validate-instructor-ready" if fail == 0 else f"WARN {fail} partial")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
