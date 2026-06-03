#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog
from waike_curriculum.depth_generators import GROUP_PROJECT_FILES


def main() -> int:
    errors = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        for f in GROUP_PROJECT_FILES:
            if not (ROOT / "group_projects" / "by_course" / cid / f).exists():
                errors.append(f"{cid}: {f}")
    if errors:
        print("FAIL", len(errors))
        return 1
    print("PASS validate-group-project-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
