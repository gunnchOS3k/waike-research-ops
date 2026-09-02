#!/usr/bin/env python3
"""Generate taxonomy reconciliation reports under reports/."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.taxonomy import (  # noqa: E402
    compute_registry_hash,
    digital_rc_package_dirs,
    git_head_sha,
    load_alias_map,
    load_registry,
    validate_registry,
)

REPORT_MD = ROOT / "reports" / "WAIKE_TAXONOMY_RECONCILIATION.md"
REPORT_JSON = ROOT / "reports" / "waike_taxonomy_reconciliation.json"


def _build() -> dict:
    reg = load_registry()
    amap = load_alias_map()
    errors = validate_registry(reg, amap)
    pkgs = digital_rc_package_dirs(ROOT)
    tracks = reg["tracks"]
    aliases = []
    for t in tracks:
        for a in t["historical_aliases"]:
            aliases.append({"alias": a, "canonical_track_id": t["track_id"]})

    package_status = []
    for t in tracks:
        tid = t["track_id"]
        covering = [
            m
            for m in reg["package_mappings"]
            if tid in m["covers_track_ids"]
        ]
        course_json = ROOT / "curriculum/digital_rc" / tid / "course.json"
        standalone_1to1 = False
        if course_json.is_file():
            tids = json.loads(course_json.read_text()).get("track_ids") or []
            standalone_1to1 = tids == [tid]

        package_status.append(
            {
                "track_id": tid,
                "content_maturity_state": t["content_maturity"]["state"],
                "standalone_1to1_package": standalone_1to1,
                "package_mappings": covering,
                "covering_package_ids": t["content_maturity"]["facets"]["covering_package_ids"],
            }
        )

    # mismatches / unresolved
    mismatches = []
    # HARDWARE_ENGINEERING multi-cover while EMBEDDED also has standalone
    mismatches.append(
        {
            "kind": "shared_package_also_has_standalone_track_package",
            "package_id": "HARDWARE_ENGINEERING",
            "covers_track_ids": ["HARDWARE_ENGINEERING", "EMBEDDED_PROTOTYPING"],
            "note": "EMBEDDED_PROTOTYPING also has curriculum/digital_rc/EMBEDDED_PROTOTYPING; package_mappings records multi-cover without aliasing.",
        }
    )
    # historical ledger said NETWORKING/CYBER below bar but packages exist under historical IDs
    mismatches.append(
        {
            "kind": "gap_ledger_stale_vs_disk",
            "detail": "WAIKE_FULL_TAXONOMY_GAP_LEDGER.json marked NETWORKING_INFRA/CYBER_SOC BELOW_BAR; disk has COMPUTER_NETWORKING and CYBERSECURITY packages mapping 1:1.",
        }
    )
    mismatches.append(
        {
            "kind": "gap_ledger_package_count_stale",
            "ledger_digital_rc_course_count": 14,
            "disk_digital_rc_dir_count": len(pkgs),
            "note": "Ledger predates EMBEDDED_PROTOTYPING and GUNNCHOS_PRODUCT_LAB package dirs.",
        }
    )

    unresolved_collisions = [
        {
            "raw_id": "GENERAL_IT",
            "reason": "shared_digital_rc_package_covers_two_tracks",
            "covers_track_ids": ["DIGITAL_CONFIDENCE", "IT_SUPPORT_HARDWARE"],
            "resolution": "package_mappings_only_not_alias",
        },
        {
            "raw_id": "general_it",
            "reason": "snake_of_multi_track_package_not_alias",
            "covers_track_ids": ["DIGITAL_CONFIDENCE", "IT_SUPPORT_HARDWARE"],
            "resolution": "left_unresolved_fail_closed",
        },
    ]

    historical_ids = sorted(
        {
            a["alias"]
            for a in aliases
            if a["alias"].startswith("WAIKE_COURSE_")
            or a["alias"] in {"COMPUTER_NETWORKING", "CYBERSECURITY", "cybersecurity"}
        }
    )

    similar_titles_not_aliased = [
        {
            "candidate": "networking",
            "near_track": "NETWORKING_INFRA",
            "reason": "lessons/by_course/networking exists but is not exact snake of track_id or 1:1 historical package id; not invented",
        },
        {
            "candidate": "software_engineering",
            "near_track": "SOFTWARE_BUILDER",
            "reason": "similar title/folder; no explicit track_id evidence",
        },
        {
            "candidate": "data_visualization_bi",
            "near_track": "DATA_VIZ_BI",
            "reason": "similar folder name; not exact snake of DATA_VIZ_BI",
        },
    ]

    this_pr_fixes = [
        "Canonical 18-track registry with deterministic uuid5 stable IDs",
        "Evidence-only historical alias map + fail-closed resolve_track_id",
        "Explicit package_mappings for multi-track and historical package IDs",
        "Deterministic consumer export with registry_hash",
        "Reconciliation reports separating contract work from remaining content gaps",
    ]
    remaining_content_work = [
        "SEVEN_GC_APPRENTICESHIP still has no digital_rc package (program shell only)",
        "DIGITAL_CONFIDENCE and IT_SUPPORT_HARDWARE remain shared under GENERAL_IT (no standalone packages)",
        "Package version fields are null until versioned package manifests exist",
        "Track-level prerequisites arrays are empty pending evidence-backed prerequisite graph",
        "Stale gap ledger should be refreshed in a follow-up content/ops packet",
        "Similar-title lesson folders (networking, software_engineering, …) remain unresolved by design",
    ]

    payload = {
        "schema": "waike.taxonomy.reconciliation.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_commit_sha": git_head_sha(ROOT),
        "registry_hash": compute_registry_hash(reg),
        "validation_errors": errors,
        "exact_counts": {
            "canonical_tracks": len(tracks),
            "historical_aliases": len(aliases),
            "digital_rc_package_dirs": len(pkgs),
            "package_mappings": len(reg["package_mappings"]),
            "unresolved_collisions": len(unresolved_collisions),
            "mismatches": len(mismatches),
            "similar_titles_not_aliased": len(similar_titles_not_aliased),
        },
        "canonical_tracks": [
            {
                "track_id": t["track_id"],
                "stable_uuid": t["stable_uuid"],
                "title": t["title"],
                "academy_id": t["academy_id"],
                "extension_class": t["extension_class"],
                "historical_aliases": t["historical_aliases"],
                "content_maturity": t["content_maturity"],
            }
            for t in tracks
        ],
        "aliases": aliases,
        "package_status": package_status,
        "digital_rc_packages_on_disk": pkgs,
        "package_mappings": reg["package_mappings"],
        "mismatches": mismatches,
        "historical_ids": historical_ids,
        "unresolved_collisions": unresolved_collisions,
        "similar_titles_not_aliased": similar_titles_not_aliased,
        "what_this_pr_fixes": this_pr_fixes,
        "remaining_content_work": remaining_content_work,
    }
    return payload


def _md(payload: dict) -> str:
    c = payload["exact_counts"]
    lines = [
        "# WAIKE Taxonomy Reconciliation",
        "",
        f"Generated (UTC): `{payload['generated_utc']}`",
        f"Source commit: `{payload['source_commit_sha']}`",
        f"Registry hash (sha256): `{payload['registry_hash']}`",
        "",
        "## Exact counts",
        "",
        f"- Canonical tracks: **{c['canonical_tracks']}**",
        f"- Historical aliases: **{c['historical_aliases']}**",
        f"- Digital RC package dirs on disk (`ls curriculum/digital_rc`): **{c['digital_rc_package_dirs']}**",
        f"- Package mappings: **{c['package_mappings']}**",
        f"- Unresolved collisions: **{c['unresolved_collisions']}**",
        f"- Mismatches recorded: **{c['mismatches']}**",
        f"- Similar titles not aliased: **{c['similar_titles_not_aliased']}**",
        "",
        "## Canonical 18 tracks",
        "",
        "| track_id | academy | extension | maturity | aliases |",
        "|---|---|---|---|---|",
    ]
    for t in payload["canonical_tracks"]:
        als = ", ".join(f"`{a}`" for a in t["historical_aliases"])
        lines.append(
            f"| `{t['track_id']}` | `{t['academy_id']}` | `{t['extension_class']}` | "
            f"`{t['content_maturity']['state']}` | {als} |"
        )

    lines += [
        "",
        "## Package mappings (not aliases when multi-track)",
        "",
    ]
    for m in payload["package_mappings"]:
        lines.append(
            f"- `{m['package_id']}` → {m['covers_track_ids']} ({m['relationship']})"
        )

    lines += [
        "",
        "## Digital RC packages on disk",
        "",
        ", ".join(f"`{p}`" for p in payload["digital_rc_packages_on_disk"]),
        "",
        "## Historical IDs retained as aliases",
        "",
        ", ".join(f"`{h}`" for h in payload["historical_ids"]),
        "",
        "## Unresolved collisions (fail-closed)",
        "",
    ]
    for u in payload["unresolved_collisions"]:
        lines.append(
            f"- `{u['raw_id']}`: {u['reason']} → {u['resolution']}"
        )

    lines += ["", "## Mismatches", ""]
    for m in payload["mismatches"]:
        lines.append(f"- `{m['kind']}`: {m.get('note') or m.get('detail') or m}")

    lines += ["", "## Similar titles intentionally NOT aliased", ""]
    for s in payload["similar_titles_not_aliased"]:
        lines.append(f"- `{s['candidate']}` (~`{s['near_track']}`): {s['reason']}")

    lines += ["", "## What this PR fixes", ""]
    for item in payload["what_this_pr_fixes"]:
        lines.append(f"- {item}")

    lines += ["", "## Remaining content work (out of contract scope)", ""]
    for item in payload["remaining_content_work"]:
        lines.append(f"- {item}")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    payload = _build()
    if payload["validation_errors"]:
        print("validation errors:", payload["validation_errors"], file=sys.stderr)
        return 1
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    REPORT_MD.write_text(_md(payload), encoding="utf-8")
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
