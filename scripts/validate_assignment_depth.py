#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

REQUIRED = ["## Purpose", "## Step-by-step instructions", "## Deliverables", "## Acceptance criteria"]


def main() -> int:
    errors = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        for w in range(1, 9):
            p = ROOT / "assignment_bodies" / "by_course" / cid / f"assignment_{w:02d}.md"
            if not p.exists():
                errors.append(f"missing {p}")
                continue
            text = p.read_text(encoding="utf-8")
            for sec in REQUIRED:
                if sec not in text:
                    errors.append(f"{cid} a{w:02d}: missing {sec}")
            if len(text) < 800:
                errors.append(f"{cid} a{w:02d}: too shallow")
    if errors:
        print("FAIL", len(errors))
        return 1
    print("PASS validate-assignment-depth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
