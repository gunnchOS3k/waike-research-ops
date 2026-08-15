"""Tests for WAIKE mastery learning-contract surfaces (honest demotions)."""
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
    assert contract["discovery"]["method"] == "filesystem_scan"
    assert contract["discovery"]["course_count"] >= 9
    ids = {c["course_id"] for c in contract["courses"]}
    assert "SOFTWARE_BUILDER" in ids
    assert "GENERAL_IT" in ids
    # Ready for #46 merge: discovery is dynamic; do not hardcode nine forever.
    assert isinstance(contract["courses"], list)


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


def test_canary_feeds_and_refuses():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.canary import CANARY_TOKEN, run_key_leak_canary

    c = run_key_leak_canary(ROOT)
    assert c["canary_text_used"] is True
    assert c["feed_into_solver_discovery_attempted"] is True
    assert c["solver_discovery_refused"] is True
    assert c["leaked_to_solver_context"] is False
    assert c["pass"] is True
    assert CANARY_TOKEN in c["canary_token"]


def test_tool_use_is_partial_not_complete():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.tool_use import run_tool_use_mastery

    tool = run_tool_use_mastery()
    assert tool["passed"] >= 6
    assert tool["coverage_status"] == "PARTIAL"
    assert tool["mastery_complete"] is False


def test_benchmark_measures_key_use_and_policy_blocks_055():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.benchmark import run_mastery_benchmark
    from waike_mastery.policy import evaluate_mastery_policy

    b = run_mastery_benchmark(ROOT, max_items_per_course=12)
    assert b["self_graded"] is False
    assert "used_instructor_keys_during_solve" in b
    assert isinstance(b["used_instructor_keys_during_solve"], bool)
    assert "key_use_measurement" in b
    # ~curriculum-overlap scores must not earn mastery under policy
    policy = evaluate_mastery_policy(
        overall_score=0.64,
        per_course=b["per_course"],
        used_instructor_keys_during_solve=b["used_instructor_keys_during_solve"],
        self_graded=False,
        canary_pass=True,
        transfer_score=0.64,
        tool_use_status="PARTIAL",
    )
    assert policy["earned"] is False
    assert any("0.55" in r or "smoke" in r or "overall" in r for r in policy["reasons_not_earned"])


def test_diagnosis_loop():
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from waike_mastery.diagnosis import diagnose_misconception, remediation_loop

    d = diagnose_misconception(
        learner_ref="t1",
        course_id="SOFTWARE_BUILDER",
        item_id="SOFTWARE_BUILDER:sw1-1",
        observed_wrong_choice="Deploy latency",
    )
    assert d["demeaning_label_used"] is False
    assert remediation_loop(d)["final_evidence_state"] != "CERTAINLY_FILLED"
    assert (
        remediation_loop(d, reassess_score=0.95, transfer_ok=True)["final_evidence_state"]
        == "CERTAINLY_FILLED"
    )
