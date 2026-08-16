"""STREAM-B-PKT-003: DATA_DASHBOARDS full DIGITAL_RC labs must execute."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.batch006.labs import (  # noqa: E402
    REFERENCE_006,
    WRONG_006,
    lab_schema_ingest,
    lab_kpi_calc,
    lab_dashboard_chart,
    lab_pii_redact_etl,
    lab_dashboard_capstone,
)
from waike_course_ready.labs import COURSE_LABS, run_lab  # noqa: E402
from waike_course_ready.content import COURSES  # noqa: E402


def test_data_dashboards_in_product_path():
    assert "DATA_DASHBOARDS" in COURSES
    assert len(COURSES["DATA_DASHBOARDS"]["weeks"]) == 10


def test_data_dashboards_labs_registered():
    assert "DATA_DASHBOARDS" in COURSE_LABS
    assert len(COURSE_LABS["DATA_DASHBOARDS"]) == 10


def test_reference_submissions_pass():
    for lab_id, sub in REFERENCE_006.items():
        r = run_lab(lab_id, submission=sub)
        assert r["ok"], (lab_id, r)


def test_empty_and_wrong_fail():
    for lab_id in REFERENCE_006:
        empty = run_lab(lab_id, submission={})
        assert not empty["ok"], lab_id
        wrong = run_lab(lab_id, submission=WRONG_006[lab_id])
        assert not wrong["ok"], lab_id


def test_print_pass_forbidden():
    try:
        lab_schema_ingest("PASS")
        assert False, "expected AssertionError"
    except AssertionError:
        pass


def test_direct_handlers():
    assert lab_kpi_calc(REFERENCE_006["lab_kpi_calc"]).ok
    assert lab_dashboard_chart(REFERENCE_006["lab_dashboard_chart"]).ok
    assert lab_pii_redact_etl(REFERENCE_006["lab_pii_redact_etl"]).ok
    assert lab_dashboard_capstone(REFERENCE_006["lab_dashboard_capstone"]).ok
