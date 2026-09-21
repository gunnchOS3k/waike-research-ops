#!/usr/bin/env python3
"""Emit CANONICAL_LEGACY_PACKAGE_RECONCILIATION.json (18 tracks ↔ 17 legacy packages)."""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402

OUT = ROOT / "artifacts/full_readiness/CANONICAL_LEGACY_PACKAGE_RECONCILIATION.json"

LEGACY_MAP = {
    "DIGITAL_CONFIDENCE": "GENERAL_IT",
    "IT_SUPPORT_HARDWARE": "GENERAL_IT",
    "NETWORKING_INFRA": "COMPUTER_NETWORKING",
    "CYBER_SOC": "CYBERSECURITY",
}


def main() -> int:
    tracks = json.loads((ROOT / "curriculum/taxonomy/eighteen_tracks.json").read_text(encoding="utf-8"))[
        "tracks"
    ]
    track_ids = [t["track_id"] for t in tracks]
    for tid in track_ids:
        LEGACY_MAP.setdefault(tid, tid)

    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        sha = "UNKNOWN"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    legacy_courses = sorted(COURSES.keys())
    rows = []
    all_ok = True
    for tid in track_ids:
        legacy = LEGACY_MAP[tid]
        canon_pkg = ROOT / "curriculum/canonical_packages" / tid / "PACKAGE_MANIFEST.v1.json"
        manifest = json.loads(canon_pkg.read_text(encoding="utf-8")) if canon_pkg.exists() else {}
        digital_rc_path = manifest.get("digital_rc_path") or f"curriculum/digital_rc/{legacy}"
        addressable = (ROOT / digital_rc_path / "course.json").exists()
        in_product = legacy in COURSES
        shared = legacy != tid
        ok = bool(addressable and canon_pkg.exists() and in_product)
        all_ok = all_ok and ok
        rows.append(
            {
                "track_id": tid,
                "legacy_digital_rc_id": legacy,
                "shared_package": shared,
                "canonical_manifest": str(canon_pkg.relative_to(ROOT)) if canon_pkg.exists() else None,
                "digital_rc_path": digital_rc_path,
                "legacy_in_COURSES_product_path": in_product,
                "addressable": addressable,
                "ok": ok,
            }
        )

    recon = {
        "schema": "waike.full_readiness.canonical_legacy_package_reconciliation.v1",
        "generated_at": now,
        "source_commit": sha,
        "canonical_track_count": len(track_ids),
        "legacy_product_course_count": len(legacy_courses),
        "legacy_product_courses": legacy_courses,
        "mapping": rows,
        "shared_package_groups": [
            {"legacy": "GENERAL_IT", "tracks": ["DIGITAL_CONFIDENCE", "IT_SUPPORT_HARDWARE"]},
            {"legacy": "COMPUTER_NETWORKING", "tracks": ["NETWORKING_INFRA"]},
            {"legacy": "CYBERSECURITY", "tracks": ["CYBER_SOC"]},
        ],
        "all_canonical_tracks_addressable": all(r["addressable"] for r in rows),
        "ok": all_ok and len(track_ids) == 18 and len(legacy_courses) == 17,
        "claim_boundary": (
            "Reconciles 18 canonical track_ids to 17 legacy digital_rc product courses. "
            "Not a field/human claim."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(recon, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": recon["ok"], "wrote": str(OUT.relative_to(ROOT))}, indent=2))
    return 0 if recon["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
