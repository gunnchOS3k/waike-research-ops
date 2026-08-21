"""Canonical tests for batch002 exam size validation (R5-S1)."""

from __future__ import annotations

from unittest import mock

import pytest

from waike_course_ready.batch002 import exams as batch002_exams
from waike_course_ready.content import COURSES_002, extra_assessment_items


def test_batch002_valid_exams_have_required_bank_sizes():
    # Real catalog path (no mock): mid=20, final=24 after rebalance.
    for course_id in COURSES_002:
        extras = extra_assessment_items(course_id)
        assert len(extras["mid"]) == 20, course_id
        assert len(extras["final"]) == 24, course_id
        assert all("stem" in item and "choices" in item for item in extras["mid"] + extras["final"])


def test_batch002_rejects_undersized_rebalanced_banks():
    """Validation raise must fire when rebalance yields wrong lengths.

    Uses a stub rebalance only for the negative path; valid path is covered above
    without mocks.
    """

    def _short_bank(items, offset):  # noqa: ARG001 — production signature
        return list(items)[:3]

    with mock.patch("waike_course_ready.exams.rebalance_mcq", side_effect=_short_bank):
        with pytest.raises(ValueError, match="exam sizes"):
            batch002_exams.extra_assessment_items_002("SOFTWARE_BUILDER")
