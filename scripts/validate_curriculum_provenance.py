#!/usr/bin/env python3
"""Fail on copied passages, dumps, missing attribution, or templated batch courses."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.provenance import audit  # noqa: E402


def main() -> int:
    result = audit()
    out = ROOT / "artifacts" / "CURRICULUM_PROVENANCE_AUDIT.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "findings": result["findings"], "wrote": str(out)}, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
