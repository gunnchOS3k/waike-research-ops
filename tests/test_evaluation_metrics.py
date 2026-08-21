"""Canonical tests for waike_curriculum.evaluation.metrics (R5-S1)."""

from __future__ import annotations

from waike_curriculum.evaluation.metrics import completion_rate


def test_completion_rate_empty_progress_is_zero():
    # Hand-computed: empty/falsy progress → 0.0 (not derived from completion_rate).
    expected_empty = 0.0
    assert completion_rate(None) == expected_empty
    assert completion_rate([]) == expected_empty
    assert completion_rate({}) == expected_empty
    assert completion_rate("") == expected_empty
    assert completion_rate(0) == expected_empty


def test_completion_rate_nonzero_progress_is_half():
    # Hand-computed stub contract on accepted main: any truthy progress → 0.5.
    expected_partial = 0.5
    assert completion_rate(["module_a"]) == expected_partial
    assert completion_rate({"completed": 1, "total": 4}) == expected_partial
    assert completion_rate(1) == expected_partial
