#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

CORE = [
    ("assignment_bodies/by_course/{cid}/assignment_01.md", "Step-by-step instructions"),
    ("results/deep_student_packets/{cid}_student_packet.md", "Weekly roadmap"),
    ("group_projects/by_course/{cid}/project_brief.md", ""),
]


def main() -> int:
    rows = []
    fail = 0
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        missing = []
        for tpl, needle in CORE:
            p = ROOT / tpl.format(cid=cid)
            if not p.exists():
                missing.append(tpl.format(cid=cid))
            elif needle and needle not in p.read_text(encoding="utf-8", errors="ignore"):
                missing.append(f"{tpl.format(cid=cid)}:{needle}")
        status = "STUDENT_READY" if not missing else "NOT_STUDENT_READY"
        if missing:
            fail += 1
        rows.append((cid, status, missing))
    out = ROOT / "results/audit/student_ready_audit.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    body = "# Student-ready audit\n\n| Course | Status | Missing |\n|--------|--------|--------|\n"
    for cid, st, miss in rows:
        body += f"| {cid} | {st} | {', '.join(miss[:3]) or '—'} |\n"
    out.write_text(body, encoding="utf-8")
    (ROOT / ".audit/STUDENT_READY_AUDIT.md").write_text(body, encoding="utf-8")
    if fail:
        print("FAIL validate-student-ready", fail, "courses")
        return 1
    print("PASS validate-student-ready")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
