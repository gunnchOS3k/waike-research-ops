#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.catalog import load_catalog
from waike_curriculum.depth_content import TECHNICAL_FLAGSHIP
from waike_curriculum.depth_generators import LESSON_FILES

MIN_LESSON_PLAN = 400


def main() -> int:
    errors = []
    for course in load_catalog().get("courses", []):
        cid = course["course_id"]
        for week in range(1, 9):
            wdir = ROOT / "lessons" / "by_course" / cid / f"week_{week:02d}"
            for f in LESSON_FILES:
                p = wdir / f
                if not p.exists():
                    errors.append(f"{cid}/week_{week:02d}: missing {f}")
            lp = wdir / "lesson_plan.md"
            if lp.exists() and len(lp.read_text(encoding="utf-8")) < MIN_LESSON_PLAN:
                errors.append(f"{cid}/week_{week:02d}: lesson_plan too short")
        for w in range(1, 9):
            ap = ROOT / "assignment_bodies" / "by_course" / cid / f"assignment_{w:02d}.md"
            if not ap.exists():
                errors.append(f"{cid}: missing assignment_{w:02d}.md")
            elif "Step-by-step instructions" not in ap.read_text(encoding="utf-8"):
                errors.append(f"{cid}: assignment_{w:02d} missing steps")
        lab_count = len(list((ROOT / "labs" / "by_course" / cid).glob("week_*_lab"))) if (ROOT / "labs" / "by_course" / cid).exists() else 0
        min_labs = 8 if cid in TECHNICAL_FLAGSHIP or cid == "digital_confidence" else 4
        if lab_count < min_labs:
            errors.append(f"{cid}: labs {lab_count} < {min_labs}")
        gp = ROOT / "group_projects" / "by_course" / cid / "project_brief.md"
        if not gp.exists():
            errors.append(f"{cid}: missing group project_brief")
    if errors:
        print("FAIL validate-course-depth", len(errors))
        for e in errors[:20]:
            print(" ", e)
        return 1
    print("PASS validate-course-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
