"""Preserve MASTERY_001 nine-course baseline and emit CORPUS_VERSION_DIFF."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .corpus_inventory import build_corpus_inventory

ROOT = Path(__file__).resolve().parents[2]

# Historical #47 nine-course snapshot (do not overwrite as current truth).
MASTERY_001_NINE_COURSE_BASELINE: dict[str, Any] = {
    "schema": "waike.mastery_001_nine_course_baseline.v1",
    "label": "MASTERY_001_NINE_COURSE_BASELINE",
    "source": "waike-research-ops #47 merged artifacts (pre-#46 12-course regen)",
    "courses": 9,
    "assessable_items": 1016,
    "course_ids": [
        "AI_ML_EDGE",
        "CLOUD_DEVOPS",
        "COMPUTER_NETWORKING",
        "CYBERSECURITY",
        "DATA_VIZ_BI",
        "GENERAL_IT",
        "HARDWARE_ENGINEERING",
        "PM_AGILE_LSS",
        "SOFTWARE_BUILDER",
    ],
    "overall_score": 0.6442307692307693,
    "solver": "curriculum_overlap_v1",
    "note": (
        "Historical Mastery-001 score on the nine-course corpus. "
        "Preserved for comparison; not current accepted-main truth after #46."
    ),
}


def _hash_ids_items(course_ids: list[str], item_count: int) -> str:
    blob = json.dumps({"course_ids": sorted(course_ids), "item_count": item_count}, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest()


def build_corpus_version_diff(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    inv = build_corpus_inventory(root)
    old_ids = list(MASTERY_001_NINE_COURSE_BASELINE["course_ids"])
    new_ids = list(inv["course_ids"])
    added = sorted(set(new_ids) - set(old_ids))
    removed = sorted(set(old_ids) - set(new_ids))
    return {
        "schema": "waike.corpus_version_diff.v1",
        "old_corpus": {
            "label": "MASTERY_001_NINE_COURSE_BASELINE",
            "courses": 9,
            "assessable_items": 1016,
            "course_ids": old_ids,
            "overall_score_preserved": 0.6442307692307693,
            "hash": _hash_ids_items(old_ids, 1016),
        },
        "new_corpus": {
            "label": "MASTERY_002_CURRENT_MAIN",
            "courses": inv["course_count"],
            "assessable_items": inv["assessable_items"],
            "course_ids": new_ids,
            "totals": inv["totals"],
            "skill_graph_nodes": inv["skill_graph_nodes"],
            "skill_graph_edges": inv["skill_graph_edges"],
            "hash": inv["corpus_hash_sha256"],
        },
        "added_courses": added,
        "removed_courses": removed,
        "changed_items": {
            "assessable_items_delta": inv["assessable_items"] - 1016,
            "per_course_new_only": {
                cid: inv["per_course_assessable"].get(cid) for cid in added
            },
        },
        "changed_rubrics": {
            "note": "rubric file counts regenerated via filesystem inventory",
            "rubrics_files_total": inv["totals"]["rubrics_files"],
        },
        "expected_new_courses_present": {
            "WIRELESS_6G": "WIRELESS_6G" in new_ids,
            "ROBOTICS_CONTROL": "ROBOTICS_CONTROL" in new_ids,
            "GAME_DEV_INTERACTIVE": "GAME_DEV_INTERACTIVE" in new_ids,
        },
    }
