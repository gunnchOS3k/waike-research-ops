#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES
from waike_curriculum.depth_generators import CASE_DEPTH_FILES

REQ = ["case_brief.md", "human_story.md", "learner_tasks.md", "local_validation_needed.md"]


def main() -> int:
    errors = []
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        for case in cases:
            base = ROOT / "case_studies" / "7gc" / site / case["case_id"]
            for f in REQ:
                if not (base / f).exists():
                    errors.append(f"{site}/{case['case_id']}: {f}")
    if errors:
        print("FAIL", len(errors))
        return 1
    print("PASS validate-case-study-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
