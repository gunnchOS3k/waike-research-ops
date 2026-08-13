#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.emit import emit_all  # noqa: E402
from waike_course_ready.ingest import write_ingest  # noqa: E402


def main() -> int:
    packages = emit_all()
    write_ingest()
    counts = {cid: pkg["counts"] for cid, pkg in packages.items()}
    out = ROOT / "artifacts" / "COURSE_COUNTS.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"courses": sorted(packages), "wrote": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
