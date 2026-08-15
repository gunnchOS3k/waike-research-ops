"""Honest mastery qualifying policy — 0.55 smoke bars never earn mastery PASS."""
from __future__ import annotations

from typing import Any

# Smoke / infra bars must NEVER flip WAIKE_AI_DIGITAL_MASTERY_PASS.
FORBIDDEN_MASTERY_SMOKE_BAR = 0.55

# Qualifying policy for aggregate digital mastery (machine-graded corpus).
MASTERY_OVERALL_MIN = 0.95
MASTERY_PER_COURSE_MIN = 0.90
MASTERY_TRANSFER_MIN = 0.90


def evaluate_mastery_policy(
    *,
    overall_score: float,
    per_course: dict[str, dict[str, Any]],
    used_instructor_keys_during_solve: bool,
    self_graded: bool,
    canary_pass: bool,
    transfer_score: float | None,
    tool_use_status: str,
) -> dict[str, Any]:
    """Return whether mastery PASS is earned. Scores are always published separately."""
    course_fails = [
        cid
        for cid, row in per_course.items()
        if float(row.get("score") or 0.0) < MASTERY_PER_COURSE_MIN
    ]
    reasons: list[str] = []
    if overall_score < MASTERY_OVERALL_MIN:
        reasons.append(
            f"overall_score={overall_score:.4f} < policy_min={MASTERY_OVERALL_MIN}"
        )
    if course_fails:
        reasons.append(f"per_course_below_min={course_fails}")
    if used_instructor_keys_during_solve:
        reasons.append("used_instructor_keys_during_solve")
    if self_graded:
        reasons.append("self_graded")
    if not canary_pass:
        reasons.append("key_leak_canary_failed")
    if transfer_score is None or transfer_score < MASTERY_TRANSFER_MIN:
        reasons.append(
            f"transfer_score={transfer_score} < policy_min={MASTERY_TRANSFER_MIN}"
        )
    if tool_use_status != "COMPLETE":
        reasons.append(f"tool_use_status={tool_use_status} (need COMPLETE for mastery)")
    # Explicit anti-pattern: never treat ~0.55 as mastery
    if overall_score < MASTERY_OVERALL_MIN and overall_score >= FORBIDDEN_MASTERY_SMOKE_BAR - 0.001:
        reasons.append(
            f"smoke_bar_{FORBIDDEN_MASTERY_SMOKE_BAR}_is_not_mastery"
        )

    earned = len(reasons) == 0
    return {
        "policy": {
            "overall_min": MASTERY_OVERALL_MIN,
            "per_course_min": MASTERY_PER_COURSE_MIN,
            "transfer_min": MASTERY_TRANSFER_MIN,
            "forbidden_smoke_bar": FORBIDDEN_MASTERY_SMOKE_BAR,
        },
        "earned": earned,
        "reasons_not_earned": reasons,
    }
