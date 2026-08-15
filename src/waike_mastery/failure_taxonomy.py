"""Failure taxonomy for missed marks — first divergence, not only final wrong answer."""
from __future__ import annotations

from typing import Any

TAXONOMY = [
    "MODEL_KNOWLEDGE_GAP",
    "PREREQUISITE_GAP",
    "CONCEPT_CONFUSION",
    "REASONING_FAILURE",
    "CALCULATION_FAILURE",
    "INSTRUCTION_INTERPRETATION_FAILURE",
    "VOCABULARY_FAILURE",
    "TRANSFER_FAILURE",
    "TOOL_SELECTION_FAILURE",
    "TOOL_EXECUTION_FAILURE",
    "DEBUGGING_FAILURE",
    "CODE_FAILURE",
    "SOURCE_GROUNDING_FAILURE",
    "RUBRIC_FAILURE",
    "PARTIAL_COMPLETION",
    "CARELESS_ERROR",
    "ACCESSIBILITY_BARRIER",
    "AMBIGUOUS_PROMPT",
    "CURRICULUM_DEFECT_CANDIDATE",
    "GRADER_DEFECT_CANDIDATE",
    "POLICY_BLOCKED",
    "RESOURCE_BLOCKED",
    "DIAGNOSIS_UNCERTAIN",
]


def classify_miss(
    *,
    stem: str,
    chosen: str | None,
    expected_hint: str | None = None,
    used_keys: bool = False,
    tool_failed: bool = False,
    calc_mismatch: bool = False,
    blocked_resource: bool = False,
    blocked_runtime: bool = False,
) -> dict[str, Any]:
    if used_keys:
        code = "POLICY_BLOCKED"
    elif blocked_resource:
        code = "RESOURCE_BLOCKED"
    elif blocked_runtime:
        code = "DIAGNOSIS_UNCERTAIN"
    elif tool_failed:
        code = "TOOL_EXECUTION_FAILURE"
    elif calc_mismatch:
        code = "CALCULATION_FAILURE"
    elif chosen is None:
        code = "PARTIAL_COMPLETION"
    elif expected_hint and chosen and expected_hint.lower() in (stem or "").lower():
        code = "INSTRUCTION_INTERPRETATION_FAILURE"
    else:
        code = "MODEL_KNOWLEDGE_GAP"
    assert code in TAXONOMY
    return {
        "failure_code": code,
        "first_divergence": "answer_selection" if chosen is not None else "no_attempt",
        "stem_excerpt": (stem or "")[:160],
        "chosen_excerpt": (chosen or "")[:120],
        "taxonomy_version": "waike.failure_taxonomy.v1",
    }


def sample_taxonomy_report(misses: list[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for m in misses:
        counts[m["failure_code"]] = counts.get(m["failure_code"], 0) + 1
    return {
        "schema": "waike.failure_taxonomy_report.v1",
        "taxonomy": TAXONOMY,
        "miss_count": len(misses),
        "counts": counts,
        "samples": misses[:25],
    }
