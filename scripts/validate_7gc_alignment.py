#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES, load_catalog

CASE_FILES = [
    "README.md", "case_brief.md", "learner_context.md", "ethical_considerations.md",
    "group_project_prompt.md", "rubric.md",
]


def main() -> int:
    errors = []
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        for case in cases:
            base = ROOT / "case_studies" / "7gc" / site / case["case_id"]
            for f in CASE_FILES:
                if not (base / f).exists():
                    errors.append(f"{site}/{case['case_id']}: missing {f}")
    for course in load_catalog().get("courses", []):
        if not course.get("7gc_sites"):
            errors.append(f"{course['course_id']}: no 7gc_sites")
    if errors:
        print("FAIL", len(errors), "issues")
        for e in errors[:15]:
            print(" ", e)
        return 1
    print("PASS validate-7gc-alignment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
