#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

REQ = ["syllabus.md", "weekly_schedule.md", "7gc_case_study_map.md"]


def main() -> int:
    missing = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        for f in REQ:
            if not (ROOT / "syllabi" / cid / f).exists():
                missing.append(f"{cid}/{f}")
    if missing:
        print("FAIL", missing)
        return 1
    print("PASS validate-syllabi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
