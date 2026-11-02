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


def test_catalog_alias_honesty_does_not_invent_true_or_flip_full_18():
    alias = _load(ROOT / "artifacts" / "CATALOG_ALIAS_HONESTY.json")
    residual = _load(ROOT / "artifacts" / "FULL_18_RESIDUAL_HONESTY.json")
    rc = _load(COURSE_RC)

    assert alias["full_18_course_digital_rc"] is False
    assert alias["HUMAN"] is False
    assert alias["RC2"] is False
    assert alias["V1"] is False
    assert alias["instructional_completeness_claimed"] is False
    assert alias["gates"]["FULL_18_FALSE_HONEST"] is True
    assert alias["gates"]["CATALOG_ALIAS_NEQ_INVENTED_TRUE"] is True
    assert alias["gates"]["NO_INVENTED_DIGITAL_RC_TRUE"] is True
    for row in alias["aliases"]:
        assert row["invent_course_digital_rc_true"] is False
        assert row["maps_to_course_digital_rc_key"] in rc["courses"]
    assert sorted(alias["residuals_not_aliased_to_true"]) == sorted(
        residual["course_digital_rc_not_true_ids"]
        if "course_digital_rc_not_true_ids" in residual
        else [r["id"] for r in residual["residuals"]]
    )


def test_full_18_residual_honesty_does_not_invent_true_flags():
    residual_path = ROOT / "artifacts" / "FULL_18_RESIDUAL_HONESTY.json"
    residual = _load(residual_path)
    stamp = _load(STAMP)
    ledger = _load(LEDGER)

    assert residual["full_18_course_digital_rc"] is False
    assert residual["HUMAN"] is False
    assert residual["RC2"] is False
    assert residual["V1"] is False
    assert residual["instructional_completeness_claimed"] is False
    assert residual["gates"]["FULL_18_FALSE_HONEST"] is True
    assert residual["gates"]["NO_INVENTED_DIGITAL_RC_TRUE"] is True
    assert residual["gates"]["HUMAN_CURRICULUM_ACCEPTANCE"] is False

    residual_ids = sorted(row["id"] for row in residual["residuals"])
    assert residual_ids == sorted(stamp["course_digital_rc_not_true_ids"])
    assert "SEVEN_GC_APPRENTICESHIP" in residual_ids
    assert "EMBEDDED_PROTOTYPING" in residual_ids
    assert "GUNNCHOS_PRODUCT_LAB" in residual_ids
    for row in residual["residuals"]:
        assert row["invent_course_digital_rc_true"] is False
    assert set(ledger["dirs_present_not_in_course_digital_rc_keys"]).issubset(set(residual_ids))
    assert set(ledger["catalog_missing_digital_rc_dir"]).issubset(set(residual_ids))


def test_pathway_discovery_honesty_does_not_invent_true_or_flip_full_18():
    from waike_ops.pathways import discover_course_dirs, build_all_pathways

    discovery = _load(ROOT / "artifacts" / "PATHWAY_DISCOVERY_HONESTY.json")
    stamp = _load(STAMP)
    residual = _load(ROOT / "artifacts" / "FULL_18_RESIDUAL_HONESTY.json")

    dirs = discover_course_dirs()
    pathways = build_all_pathways()
    discovered_ids = sorted(p.name for p in dirs)
    pathway_ids = sorted(p["course_id"] for p in pathways)

    assert discovery["full_18_course_digital_rc"] is False
    assert discovery["HUMAN"] is False
    assert discovery["RC2"] is False
    assert discovery["V1"] is False
    assert discovery["instructional_completeness_claimed"] is False
    assert discovery["gates"]["FULL_18_FALSE_HONEST"] is True
    assert discovery["gates"]["DISCOVERY_NEQ_INVENTED_TRUE"] is True
    assert discovery["gates"]["NO_INVENTED_DIGITAL_RC_TRUE"] is True
    assert discovery["discovery"]["digital_rc_dirs_with_course_json"] == len(dirs)
    assert discovered_ids == pathway_ids
    assert len(dirs) == discovery["discovery"]["digital_rc_dirs_with_course_json"]
    # Discovery of on-disk residual packages must not invent COURSE_DIGITAL_RC=true.
    residual_ids = {row["id"] for row in residual["residuals"]}
    true_ids = set(stamp["course_digital_rc_true_ids"])
    for rid in discovery["discovery"]["residuals_must_stay_not_true"]:
        assert rid in residual_ids
        assert rid not in true_ids
    assert "EMBEDDED_PROTOTYPING" in discovered_ids
    assert "GUNNCHOS_PRODUCT_LAB" in discovered_ids
    assert "SEVEN_GC_APPRENTICESHIP" not in discovered_ids
