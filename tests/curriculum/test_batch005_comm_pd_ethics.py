"""STREAM-B-PKT-001: COMM_PD_ETHICS executable labs must execute."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.batch005.labs import (  # noqa: E402
    REFERENCE_005,
    WRONG_005,
    lab_consent_disclosure,
    lab_conflict_interest,
    lab_ethics_ladder,
    lab_professional_comm,
)
from waike_course_ready.labs import COURSE_LABS, run_lab  # noqa: E402


def test_comm_pd_ethics_labs_registered():
    assert "COMM_PD_ETHICS" in COURSE_LABS
    assert len(COURSE_LABS["COMM_PD_ETHICS"]) == 4


def test_reference_submissions_pass():
    for lab_id, sub in REFERENCE_005.items():
        r = run_lab(lab_id, submission=sub)
        assert r["ok"], (lab_id, r)


def test_empty_and_wrong_fail():
    for lab_id in REFERENCE_005:
        empty = run_lab(lab_id, submission={})
        assert not empty["ok"], lab_id
        wrong = run_lab(lab_id, submission=WRONG_005[lab_id])
        assert not wrong["ok"], lab_id


def test_print_pass_forbidden():
    try:
        lab_consent_disclosure("PASS")
        assert False, "expected AssertionError"
    except AssertionError:
        pass


def test_direct_handlers():
    assert lab_conflict_interest(REFERENCE_005["lab_conflict_interest"]).ok
    assert lab_professional_comm(REFERENCE_005["lab_professional_comm"]).ok
    assert lab_ethics_ladder(REFERENCE_005["lab_ethics_ladder"]).ok
