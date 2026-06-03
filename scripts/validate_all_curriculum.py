#!/usr/bin/env python3
"""Run all curriculum validators and write report."""
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATORS = [
    "validate_curriculum.py",
    "validate_syllabi.py",
    "validate_assignments.py",
    "validate_group_projects.py",
    "validate_7gc_alignment.py",
    "validate_rubrics.py",
]


def main() -> int:
    results = []
    rc = 0
    for v in VALIDATORS:
        script = ROOT / "scripts" / v
        if not script.exists():
            results.append((v, "SKIP"))
            continue
        r = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        results.append((v, "PASS" if r.returncode == 0 else "FAIL"))
        if r.returncode:
            rc = 1
    out = ROOT / "results" / "validation"
    out.mkdir(parents=True, exist_ok=True)
    body = f"# Curriculum validation report\n\nGenerated: {datetime.now(timezone.utc).isoformat()}\n\n"
    for name, status in results:
        body += f"- {name}: {status}\n"
    (out / "curriculum_validation_report.md").write_text(body, encoding="utf-8")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
