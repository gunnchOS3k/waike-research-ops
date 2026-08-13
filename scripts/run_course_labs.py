#!/usr/bin/env python3
"""Execute WAIKE digital RC labs with computing validators."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.labs import LABS, run_all, run_lab  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--lab", help="single lab id")
    p.add_argument("--submission", help="path to student JSON")
    p.add_argument("--empty", action="store_true", help="run with empty {} (must fail)")
    args = p.parse_args()
    if args.lab:
        if args.lab not in LABS:
            print(json.dumps({"ok": False, "error": "unknown_lab", "lab": args.lab}))
            return 1
        kwargs = {}
        if args.empty:
            kwargs["submission"] = {}
        elif args.submission:
            kwargs["submission"] = json.loads(Path(args.submission).read_text(encoding="utf-8"))
        result = run_lab(args.lab, **kwargs)
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    bundle = run_all()
    out = ROOT / "artifacts" / "LAB_EXECUTION_RESULTS.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": bundle["ok"], "lab_count": bundle["lab_count"], "wrote": str(out)}, indent=2))
    return 0 if bundle["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
