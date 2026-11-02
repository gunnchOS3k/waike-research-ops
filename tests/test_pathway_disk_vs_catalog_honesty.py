"""Local pathway disk-vs-catalog honesty — no instructional-completeness claim."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "artifacts" / "PATHWAY_DISK_VS_CATALOG_LEDGER.json"
STAMP = ROOT / "artifacts" / "DIGITAL_RC_HONESTY_STAMP.json"
COURSE_RC = ROOT / "artifacts" / "COURSE_DIGITAL_RC.json"
DIGITAL_RC_DIRS = ROOT / "curriculum" / "digital_rc"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_ledger_matches_on_disk_dirs_and_rc_keys():
    ledger = _load(LEDGER)
    rc = _load(COURSE_RC)
    on_disk = sorted(p.name for p in DIGITAL_RC_DIRS.iterdir() if p.is_dir())
    rc_keys = sorted(rc["courses"].keys())

    assert ledger["counts"]["digital_rc_dirs_on_disk"] == len(on_disk)
    assert ledger["counts"]["course_digital_rc_keys"] == len(rc_keys)
    assert sorted(ledger["digital_rc_dirs_on_disk"]) == on_disk
    assert sorted(ledger["course_digital_rc_keys"]) == rc_keys
    assert ledger["full_18_course_digital_rc"] is False
    assert ledger["instructional_completeness_claimed"] is False
    assert ledger["HUMAN"] is False
    assert ledger["RC2"] is False
    assert ledger["V1"] is False
    assert ledger["gates"]["PATHWAY_COUNT_HONESTY_PASS"] is True
    assert ledger["gates"]["INSTRUCTIONAL_COMPLETENESS_CLAIMED"] is False
    assert ledger["gates"]["HUMAN_CURRICULUM_ACCEPTANCE"] is False


def test_honesty_stamp_lists_known_non_true_ids():
    ledger = _load(LEDGER)
    stamp = _load(STAMP)
    rc = _load(COURSE_RC)

    true_ids = sorted(
        cid
        for cid, row in rc["courses"].items()
        if row.get("COURSE_DIGITAL_RC") is True
    )
    expected_not_true = sorted(
        set(ledger["dirs_present_not_in_course_digital_rc_keys"])
        | set(ledger["catalog_missing_digital_rc_dir"])
    )

    assert stamp["full_18_course_digital_rc"] is False
    assert stamp["instructional_completeness_claimed"] is False
    assert stamp["HUMAN"] is False
    assert stamp["RC2"] is False
    assert stamp["V1"] is False
    assert stamp["HUMAN_E6"] is False
    assert stamp["REAL_STUDENT_E6"] is False
    assert stamp["REAL_TEACHER_E6"] is False
    assert sorted(stamp["course_digital_rc_true_ids"]) == true_ids
    assert stamp["course_digital_rc_true_count"] == len(true_ids)
    assert sorted(stamp["course_digital_rc_not_true_ids"]) == expected_not_true
    assert stamp["course_digital_rc_not_true_ids"], "full_18 false requires named non-true ids"
    assert stamp["catalog_vs_true_gap_count"] == (
        ledger["counts"]["catalog_track_ids"] - ledger["counts"]["course_digital_rc_keys"]
    )
