"""Tests for WAIKE mastery learning-contract surfaces."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def contract():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.discover import emit_learning_contract

    return emit_learning_contract(ROOT)


def test_discover_not_hardcoded_nine_names(contract):
    assert contract["discovery"]["hardcoded_course_names"] is False
    assert contract["discovery"]["course_count"] >= 9
    ids = {c["course_id"] for c in contract["courses"]}
    # Must include main corpus; must not hardcode by requiring exactly these forever
    assert "SOFTWARE_BUILDER" in ids
    assert "GENERAL_IT" in ids


def test_permission_separation(contract):
    p = contract["permissions"]
    assert p["MASTERY_BENCHMARK"]["may_read_instructor_keys"] is False
    assert p["MASTERY_BENCHMARK"]["may_self_grade"] is False
    assert p["LEARNER_TUTOR"]["may_read_instructor_keys"] is False
    assert p["EDUCATOR_COPILOT"]["may_read_instructor_keys"] is True
    assert p["EDUCATOR_COPILOT"]["hitl_grading_required"] is True


def test_registry_strips_keys():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.registry import build_assessable_registry

    reg = build_assessable_registry(ROOT)
    assert reg["item_count"] > 500
    assert reg["key_fields_present_in_registry"] == []
    blob = json.dumps(reg["items"][:50])
    assert "answer_index" not in blob


def test_canary_and_tool_use_and_diagnosis():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.canary import run_key_leak_canary
    from waike_mastery.diagnosis import diagnose_misconception, remediation_loop
    from waike_mastery.tool_use import run_tool_use_mastery

    assert run_key_leak_canary(ROOT)["pass"] is True
    tool = run_tool_use_mastery()
    assert tool["passed"] >= 6
    assert tool["pass_rate"] >= 0.8
    d = diagnose_misconception(
        learner_ref="t1",
        course_id="SOFTWARE_BUILDER",
        item_id="SOFTWARE_BUILDER:sw1-1",
        observed_wrong_choice="Deploy latency",
    )
    assert d["demeaning_label_used"] is False
    assert remediation_loop(d)["final_evidence_state"] != "CERTAINLY_FILLED"
    assert remediation_loop(d, reassess_score=0.95, transfer_ok=True)["final_evidence_state"] == "CERTAINLY_FILLED"


def test_benchmark_no_self_grade():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.benchmark import run_mastery_benchmark

    # Keep CI light: cap items per course
    b = run_mastery_benchmark(ROOT, max_items_per_course=12)
    assert b["self_graded"] is False
    assert b["used_instructor_keys_during_solve"] is False
    assert b["items_attempted"] > 0
