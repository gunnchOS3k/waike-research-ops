#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    "validate_course_depth.py",
    "validate_assignment_depth.py",
    "validate_lesson_depth.py",
    "validate_group_project_depth.py",
    "validate_case_study_depth.py",
    "validate_industry_alignment_depth.py",
    "validate_no_exam_heavy_courses.py",
]


def main() -> int:
    results = []
    rc = 0
    for script in CHECKS:
        path = ROOT / "scripts" / script
        if not path.exists():
            results.append((script, "SKIP"))
            continue
        r = subprocess.run([sys.executable, str(path)], cwd=ROOT)
        results.append((script, "PASS" if r.returncode == 0 else "FAIL"))
        if r.returncode:
            rc = 1
    out = ROOT / "results" / "validation" / "depth_validation_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    body = f"# Depth validation report\n\nGenerated: {datetime.now(timezone.utc).isoformat()}\n\n"
    for name, st in results:
        body += f"- {name}: {st}\n"
    out.write_text(body, encoding="utf-8")
    (ROOT / "results" / "validation" / "industry_alignment_report.md").write_text(
        "# Industry alignment\n\nSee industry_alignment/by_course/\n", encoding="utf-8"
    )
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
