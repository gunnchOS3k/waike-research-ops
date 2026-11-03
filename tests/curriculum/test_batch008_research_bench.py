from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.batch008.content import COURSES_008
from waike_course_ready.batch008.labs import LABS_008, REFERENCE_008, paired_interval, twin_rmse


def _run(lab_id: str, sub: dict) -> bool:
    return LABS_008[lab_id](sub).ok


def test_ntn_delay_recomputed_from_altitude():
    leo = dict(REFERENCE_008["lab_sga_ntn_delay"])
    assert _run("lab_sga_ntn_delay", leo)
    assert not _run("lab_sga_ntn_delay", {**leo, "altitude_km": 35786})


def test_manifest_digest_is_recomputed_not_trusted():
    ref = dict(REFERENCE_008["lab_sga_repro_manifest"])
    assert _run("lab_sga_repro_manifest", ref)
    assert not _run("lab_sga_repro_manifest", {**ref, "config_text": ref["config_text"] + "x"})


def test_paired_interval_matches_hand_calc_and_blocks_zero_crossing_claim():
    lo, hi = paired_interval([0.61, 0.63, 0.60, 0.62, 0.64], [0.66, 0.65, 0.67, 0.64, 0.68])[1:]
    assert round(lo, 4) == 0.0137 and round(hi, 4) == 0.0663
    _, lo0, _ = paired_interval([0.61, 0.63, 0.60, 0.62, 0.64], [0.62, 0.62, 0.61, 0.61, 0.65])
    assert lo0 < 0
    ref = dict(REFERENCE_008["lab_sga_paired_ci"])
    assert _run("lab_sga_paired_ci", ref)
    assert not _run("lab_sga_paired_ci", {**ref, "claims_improvement": False})


def test_twin_never_calibrated_without_measurements():
    assert round(twin_rmse(), 4) == 1.3229
    ref = dict(REFERENCE_008["lab_sga_twin_gap"])
    assert _run("lab_sga_twin_gap", ref)
    assert not _run("lab_sga_twin_gap", {**ref, "calibrated_claim": True})


def test_weeks_map_one_to_one_onto_distinct_labs():
    weeks = COURSES_008["SEVEN_GC_APPRENTICESHIP"]["weeks"]
    assert [w["lab_id"] for w in weeks] == list(LABS_008)
    assert len({w["lesson"] for w in weeks}) == 10
