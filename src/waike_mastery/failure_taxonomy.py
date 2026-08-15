"""Failure taxonomy for missed marks — first divergence, not only final wrong answer."""
from __future__ import annotations

from typing import Any

TAXONOMY = [
    "PARSER_FAILURE",
    "MODEL_KNOWLEDGE_GAP",
    "PREREQUISITE_GAP",
    "CONCEPT_CONFUSION",
    "REASONING_FAILURE",
    "CALCULATION_FAILURE",
    "INSTRUCTION_INTERPRETATION_FAILURE",
    "TOOL_REQUIRED_NOT_USED",
    "TOOL_SELECTION_FAILURE",
    "TOOL_EXECUTION_FAILURE",
    "SOURCE_GROUNDING_FAILURE",
    "CONTEXT_LIMIT_FAILURE",
    "PROMPT_FORMAT_FAILURE",
    "AMBIGUOUS_ITEM",
    "CURRICULUM_DEFECT_CANDIDATE",
    "GRADER_DEFECT_CANDIDATE",
    "UNKNOWN",
    # legacy retained
    "VOCABULARY_FAILURE",
    "TRANSFER_FAILURE",
    "DEBUGGING_FAILURE",
    "CODE_FAILURE",
    "RUBRIC_FAILURE",
    "PARTIAL_COMPLETION",
    "CARELESS_ERROR",
    "ACCESSIBILITY_BARRIER",
    "AMBIGUOUS_PROMPT",
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
    parser_failed: bool = False,
) -> dict[str, Any]:
    if used_keys:
        code = "POLICY_BLOCKED"
    elif parser_failed or chosen is None:
        code = "PARSER_FAILURE"
    elif blocked_resource:
        code = "RESOURCE_BLOCKED"
    elif blocked_runtime:
        code = "DIAGNOSIS_UNCERTAIN"
    elif tool_failed:
        code = "TOOL_EXECUTION_FAILURE"
    elif calc_mismatch:
        code = "CALCULATION_FAILURE"
    elif expected_hint and chosen and expected_hint.lower() in (stem or "").lower():
        code = "INSTRUCTION_INTERPRETATION_FAILURE"
    else:
        code = "MODEL_KNOWLEDGE_GAP"
    assert code in TAXONOMY
    return {
        "failure_code": code,
        "first_divergence": "parser"
        if code == "PARSER_FAILURE"
        else ("answer_selection" if chosen is not None else "no_attempt"),
        "stem_excerpt": (stem or "")[:160],
        "chosen_excerpt": (chosen or "")[:120],
        "taxonomy_version": "waike.failure_taxonomy.v2",
    }


def sample_taxonomy_report(misses: list[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    by_course: dict[str, dict[str, int]] = {}
    for m in misses:
        counts[m["failure_code"]] = counts.get(m["failure_code"], 0) + 1
        course = (m.get("stem_excerpt") or "").split(":", 1)[0]
        if course:
            by_course.setdefault(course, {})
            by_course[course][m["failure_code"]] = by_course[course].get(m["failure_code"], 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return {
        "schema": "waike.failure_taxonomy_report.v2",
        "taxonomy": TAXONOMY,
        "miss_count": len(misses),
        "counts": counts,
        "by_course": by_course,
        "largest_classes": [{"code": c, "n": n} for c, n in ranked[:8]],
        "samples": misses[:25],
    }
