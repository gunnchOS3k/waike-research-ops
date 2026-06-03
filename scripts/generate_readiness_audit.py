#!/usr/bin/env python3
"""Regenerate student/instructor/course readiness audit copies under .audit/."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "validate_student_ready.py",
    "validate_instructor_ready.py",
    "validate_placeholder_files.py",
]


def main() -> int:
    rc = 0
    for name in SCRIPTS:
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / name)], cwd=ROOT)
        if r.returncode:
            rc = 1
    # Course matrix from results
    src = ROOT / "results/audit/student_ready_audit.md"
    dst_s = ROOT / ".audit/STUDENT_READY_AUDIT.md"
    dst_i = ROOT / ".audit/INSTRUCTOR_READY_AUDIT.md"
    dst_p = ROOT / ".audit/PLACEHOLDER_AUDIT.md"
    if src.exists():
        dst_s.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    ins = ROOT / "results/audit/instructor_ready_audit.md"
    if ins.exists():
        dst_i.write_text(ins.read_text(encoding="utf-8"), encoding="utf-8")
    ph = ROOT / "results/audit/placeholder_audit.md"
    if ph.exists():
        dst_p.write_text(ph.read_text(encoding="utf-8"), encoding="utf-8")
    courses = []
    if src.exists():
        for line in src.read_text(encoding="utf-8").splitlines():
            if line.startswith("|") and "STUDENT_READY" in line:
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if parts and parts[0] != "Course":
                    courses.append((parts[0], parts[1] if len(parts) > 1 else ""))
    matrix = ["# Course readiness matrix\n\n", "| Course | Student | Instructor (see instructor audit) |\n", "|--------|---------|----------------------------------|\n"]
    for c, st in courses:
        matrix.append(f"| {c} | {st} | see results/audit/instructor_ready_audit.md |\n")
    (ROOT / ".audit/COURSE_READINESS_MATRIX.md").write_text("".join(matrix), encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts/map_issues_to_artifacts.py")], cwd=ROOT, check=False)
    print("Readiness audits synced to .audit/")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
