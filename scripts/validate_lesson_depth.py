#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog
from waike_curriculum.depth_generators import LESSON_FILES


def main() -> int:
    errors = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        for w in range(1, 9):
            for f in LESSON_FILES:
                if not (ROOT / "lessons" / "by_course" / cid / f"week_{w:02d}" / f).exists():
                    errors.append(f"{cid} w{w:02d} {f}")
    if errors:
        print("FAIL", len(errors))
        return 1
    print("PASS validate-lesson-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
