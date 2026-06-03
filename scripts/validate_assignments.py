#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog


def main() -> int:
    missing = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        adir = ROOT / "assignments" / "by_course" / cid
        if not adir.exists() or len(list(adir.glob("*.yaml"))) < 4:
            missing.append(cid)
    if missing:
        print("FAIL assignments", missing)
        return 1
    print("PASS validate-assignments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
