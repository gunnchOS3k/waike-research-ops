#!/usr/bin/env python3
"""Validate all 18 canonical package entry manifests are present and addressable."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CANONICAL_TRACK_IDS = [
    "DIGITAL_CONFIDENCE",
    "IT_SUPPORT_HARDWARE",
    "SOFTWARE_BUILDER",
    "NETWORKING_INFRA",
    "CYBER_SOC",
    "DATA_DASHBOARDS",
    "AI_ML_EDGE",
    "EMBEDDED_PROTOTYPING",
    "WIRELESS_6G",
    "PM_AGILE_LSS",
    "GAME_DEV_INTERACTIVE",
    "SEVEN_GC_APPRENTICESHIP",
    "CLOUD_DEVOPS",
    "COMM_PD_ETHICS",
    "ROBOTICS_CONTROL",
    "GUNNCHOS_PRODUCT_LAB",
    "HARDWARE_ENGINEERING",
    "DATA_VIZ_BI",
]

REQUIRED_FIELDS = (
    "schema_version",
    "track_id",
    "title",
    "package_version",
    "compatibility_version",
    "source_commit",
    "content_hash",
    "dependencies",
    "shared_content_refs",
    "digital_rc_path",
    "deprecation",
)


def main() -> int:
    errors: list[str] = []
    ok = 0
    for track_id in CANONICAL_TRACK_IDS:
        path = ROOT / "curriculum" / "canonical_packages" / track_id / "PACKAGE_MANIFEST.v1.json"
        if not path.is_file():
            errors.append(f"MISSING_MANIFEST: {path.relative_to(ROOT)}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"INVALID_JSON: {path.relative_to(ROOT)} ({exc})")
            continue
        for field in REQUIRED_FIELDS:
            if field not in data:
                errors.append(f"MISSING_FIELD:{track_id}:{field}")
        if data.get("track_id") != track_id:
            errors.append(f"TRACK_ID_MISMATCH:{track_id}:{data.get('track_id')}")
        if data.get("schema_version") != "waike.canonical_package_manifest.v1":
            errors.append(f"BAD_SCHEMA_VERSION:{track_id}:{data.get('schema_version')}")
        content_hash = data.get("content_hash")
        if not isinstance(content_hash, str) or len(content_hash) != 64:
            errors.append(f"BAD_CONTENT_HASH:{track_id}")
        rc_rel = data.get("digital_rc_path")
        if not isinstance(rc_rel, str):
            errors.append(f"BAD_DIGITAL_RC_PATH:{track_id}")
            continue
        rc_path = ROOT / rc_rel
        course_json = rc_path / "course.json"
        if not rc_path.is_dir():
            errors.append(f"UNADDRESSABLE_RC_DIR:{track_id}:{rc_rel}")
        elif not course_json.is_file():
            errors.append(f"UNADDRESSABLE_COURSE_JSON:{track_id}:{rc_rel}/course.json")
        else:
            ok += 1

    report = {
        "schema": "waike.full_readiness.canonical_package_entry_validation.v1",
        "expected_tracks": len(CANONICAL_TRACK_IDS),
        "addressable_ok": ok,
        "error_count": len(errors),
        "errors": errors,
        "pass": len(errors) == 0 and ok == len(CANONICAL_TRACK_IDS),
    }
    out = ROOT / "artifacts" / "full_readiness" / "CANONICAL_PACKAGE_ENTRY_VALIDATION.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
