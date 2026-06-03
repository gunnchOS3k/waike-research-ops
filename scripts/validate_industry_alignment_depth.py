#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

REQ = ["industry_skill_map.md", "job_role_map.md", "certification_alignment.md", "toolchain_alignment.md", "employer_evidence.md"]


def main() -> int:
    errors = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        for f in REQ:
            if not (ROOT / "industry_alignment" / "by_course" / cid / f).exists():
                errors.append(f"{cid}: {f}")
    if errors:
        print("FAIL", len(errors))
        return 1
    print("PASS validate-industry-alignment-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
