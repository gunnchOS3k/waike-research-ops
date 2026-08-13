#!/usr/bin/env python3
"""Shallow/swapped-noun detector for the WAIKE-COURSE-READY-001 batch only."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.provenance import audit  # noqa: E402


def main() -> int:
    result = audit()
    payload = {
        "BATCH_TEMPLATED_COURSES": result["BATCH_TEMPLATED_COURSES"],
        "BATCH_STUB_COURSES": result["BATCH_STUB_COURSES"],
        "worst_jaccard": result["worst_jaccard"],
        "worst_pair": result["worst_pair"],
        "status": "PASS"
        if result["BATCH_TEMPLATED_COURSES"] == 0 and result["BATCH_STUB_COURSES"] == 0
        else "FAIL",
    }
    out = ROOT / "artifacts" / "TEMPLATE_DETECTOR.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
