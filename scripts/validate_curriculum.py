#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

try:
    import yaml
except ImportError:
    yaml = None

REQUIRED_SYLLABI_FILES = [
    "README.md", "syllabus.md", "learning_outcomes.yaml", "weekly_schedule.md",
    "assignment_sequence.md", "group_project_brief.md", "rubric.md",
    "portfolio_artifact_requirements.md", "instructor_notes.md", "student_packet.md",
    "gunnchai_tutor_cards.md", "7gc_case_study_map.md",
]


def main() -> int:
    catalog_path = ROOT / "curriculum" / "catalog.yaml"
    if not catalog_path.exists():
        print("FAIL missing catalog.yaml")
        return 1
    catalog = yaml.safe_load(catalog_path.read_text()) if yaml else {}
    errors = []
    for course in catalog.get("courses", []):
        cid = course["course_id"]
        if course.get("exam_weight_max", 0) > 0.10:
            errors.append(f"{cid}: exam weight > 10%")
        sdir = ROOT / "syllabi" / cid
        for f in REQUIRED_SYLLABI_FILES:
            if not (sdir / f).exists():
                errors.append(f"{cid}: missing {f}")
        if not (ROOT / "group_projects" / "by_course" / f"{cid}.yaml").exists():
            errors.append(f"{cid}: missing group project")
        if not (ROOT / "assignments" / "by_course" / cid).exists():
            errors.append(f"{cid}: missing assignments dir")
    if errors:
        print("FAIL", errors[:20], f"... total {len(errors)}" if len(errors) > 20 else "")
        return 1
    print("PASS validate-curriculum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
