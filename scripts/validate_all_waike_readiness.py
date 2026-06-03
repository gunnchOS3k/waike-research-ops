#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "validate_issue_completion.py",
    "validate_student_ready.py",
    "validate_instructor_ready.py",
    "validate_placeholder_files.py",
    "validate_depth_all.py",
    "validate_no_exam_heavy_courses.py",
]


def main() -> int:
    results = []
    rc = 0
    for s in SCRIPTS:
        p = ROOT / "scripts" / s
        if not p.exists():
            continue
        r = subprocess.run([sys.executable, str(p)], cwd=ROOT)
        results.append((s, "PASS" if r.returncode == 0 else "FAIL"))
        if r.returncode:
            rc = 1
    out = ROOT / "results/validation/waike_readiness_validation_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    body = f"# WAIKE readiness validation\n\n{datetime.now(timezone.utc).isoformat()}\n\n"
    for n, st in results:
        body += f"- {n}: {st}\n"
    out.write_text(body, encoding="utf-8")
    (ROOT / "results/audit/issue_completion_audit.md").write_text(
        "# Issue completion audit\n\nSee .audit/ISSUE_COMPLETION_MASTER_TABLE.csv\n", encoding="utf-8"
    )
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
