#!/usr/bin/env python3
"""Emit WAIKE↔gunnchAI learning contract, registry, skill graph, mastery eval artifacts."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_mastery.audit import audit_curriculum  # noqa: E402
from waike_mastery.benchmark import isomorphic_variant, run_mastery_benchmark  # noqa: E402
from waike_mastery.canary import run_key_leak_canary  # noqa: E402
from waike_mastery.diagnosis import diagnose_misconception, remediation_loop  # noqa: E402
from waike_mastery.discover import emit_learning_contract  # noqa: E402
from waike_mastery.educator import educator_copilot_session  # noqa: E402
from waike_mastery.registry import build_assessable_registry  # noqa: E402
from waike_mastery.skill_graph import build_skill_graph  # noqa: E402
from waike_mastery.tool_use import run_tool_use_mastery  # noqa: E402


def _write(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def build_tokens(children: dict[str, bool]) -> dict[str, bool | str]:
    aggregate = all(children.values())
    return {
        "WAIKE_AI_DIGITAL_MASTERY_PASS": aggregate,
        "AI_WAIKE_MASTERY_EVAL": aggregate,
        "REAL_STUDENT": False,
        "REAL_TEACHER": False,
        "HUMAN_E6": False,
        "ACCREDITED": False,
        "USED_INSTRUCTOR_KEYS_IN_BENCHMARK_SOLVE": False,
        "SELF_GRADED": False,
        "note": "Honesty tokens stay false without cohort/accreditation evidence.",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(ROOT / "artifacts" / "mastery"))
    p.add_argument("--max-items-per-course", type=int, default=None)
    args = p.parse_args()
    out = Path(args.out)

    contract = emit_learning_contract()
    registry = build_assessable_registry()
    graph = build_skill_graph()
    audit = audit_curriculum()
    canary = run_key_leak_canary()
    tool = run_tool_use_mastery()
    bench = run_mastery_benchmark(max_items_per_course=args.max_items_per_course)

    # isomorphic variant smoke
    sample = next(i for i in registry["items"] if i.get("choices"))
    variant = isomorphic_variant(sample, seed="mastery-canary")

    diag = diagnose_misconception(
        learner_ref="opaque-learner-demo",
        course_id=sample["course_id"],
        item_id=sample["item_id"],
        observed_wrong_choice=(sample.get("choices") or ["?"])[-1],
    )
    # Without reassessment → must NOT be CERTAINLY_FILLED
    rem_open = remediation_loop(diag)
    rem_closed = remediation_loop(diag, reassess_score=0.9, transfer_ok=True)

    educator = educator_copilot_session(course_id=contract["courses"][0]["course_id"], intent="grading_assist")

    children = {
        "MODE_CONTRACT_PERMISSIONS": all(
            k in contract["permissions"]
            for k in ("MASTERY_BENCHMARK", "LEARNER_TUTOR", "EDUCATOR_COPILOT")
        )
        and contract["permissions"]["MASTERY_BENCHMARK"]["may_read_instructor_keys"] is False
        and contract["permissions"]["EDUCATOR_COPILOT"]["hitl_grading_required"] is True,
        "LEARNING_CONTRACT_DISCOVERY": contract["discovery"]["course_count"] >= 1
        and contract["discovery"]["hardcoded_course_names"] is False,
        "ASSESSABLE_REGISTRY": registry["item_count"] > 0
        and not registry["key_fields_present_in_registry"]
        and registry["self_grading_forbidden"] is True,
        "KEY_LEAK_CANARY": bool(canary["pass"]),
        "TOOL_USE_LABS": tool["pass_rate"] >= 0.8 and tool["passed"] >= 6,
        "MASTERY_BENCHMARK_ISOLATED": bench["used_instructor_keys_during_solve"] is False
        and bench["self_graded"] is False
        and bench["overall_score"] >= 0.55,
        "ISOMORPHIC_VARIANTS": bool(variant.get("isomorphic")),
        "DIAGNOSIS_REMEDIATION": rem_open["final_evidence_state"] != "CERTAINLY_FILLED"
        and rem_closed["final_evidence_state"] == "CERTAINLY_FILLED",
        "EDUCATOR_COPILOT": educator["permissions"]["may_publish_grades_without_human"] is False,
        "CURRICULUM_AUDIT_ENGINE": "defect_candidate_count" in audit,
    }
    tokens = build_tokens(children)

    eval_report = {
        "schema": "AI_WAIKE_MASTERY_EVAL.v1",
        "suite": "AI_WAIKE_MASTERY_EVAL",
        "corpus": {
            "discoverable_courses": contract["discovery"]["course_count"],
            "course_ids": [c["course_id"] for c in contract["courses"]],
            "assessable_items": registry["item_count"],
            "per_course_counts": registry["per_course"],
            "skill_graph_nodes": graph["node_count"],
            "skill_graph_edges": graph["edge_count"],
            "curriculum_defect_candidates": audit["defect_candidate_count"],
            "source": "origin/main digital_rc (WAIKE #45 nine-course corpus); #46 not required",
        },
        "mastery_scores": {
            "overall": bench["overall_score"],
            "per_course": bench["per_course"],
            "per_assessment_sample": dict(list(bench["per_assessment"].items())[:12]),
            "per_domain": bench["per_domain"],
            "items_attempted": bench["items_attempted"],
            "items_correct": bench["items_correct"],
            "solver": bench["solver"],
        },
        "tool_use": {
            "attempted": tool["attempted"],
            "passed": tool["passed"],
            "pass_rate": tool["pass_rate"],
            "labs": [{"lab_id": r["lab_id"], "ok": r.get("ok")} for r in tool["results"]],
        },
        "canary": canary,
        "diagnosis_remediation": {
            "open_loop_final": rem_open["final_evidence_state"],
            "closed_loop_final": rem_closed["final_evidence_state"],
            "demeaning_label_used": diag["demeaning_label_used"],
        },
        "educator_mode": educator,
        "children": {k: {"pass": v} for k, v in children.items()},
        "tokens": tokens,
        "open": [
            "REAL_STUDENT / REAL_TEACHER / HUMAN_E6 / ACCREDITED remain false without evidence.",
            "MCQ solver is curriculum-overlap digital — not frontier exam proctoring.",
            "Tool-use solvers cover a representative lab set, not every lab id in COURSE_LABS.",
            "device-os Product-Use (#116) is out of scope for this stream.",
            "Do not depend on unmerged WAIKE #46 for Product-Use corpus.",
        ],
        "WAIKE_AI_DIGITAL_MASTERY_PASS": tokens["WAIKE_AI_DIGITAL_MASTERY_PASS"],
        "claim_boundary": (
            "Digital WAIKE↔gunnchAI mastery harness on discoverable student curriculum. "
            "Not accredited instruction; not a live classroom study."
        ),
    }

    _write(out / "WAIKE_GUNNCHAI_LEARNING_CONTRACT.json", contract)
    _write(out / "ASSESSABLE_ITEM_REGISTRY.json", {**registry, "items": registry["items"][:5], "items_omitted_for_size": registry["item_count"] - 5})
    _write(out / "ASSESSABLE_ITEM_REGISTRY.full.json", registry)
    _write(out / "SKILL_GRAPH.json", graph)
    _write(out / "CURRICULUM_SELF_AUDIT.json", audit)
    _write(out / "KEY_LEAK_CANARY.json", canary)
    _write(out / "TOOL_USE_MASTERY.json", tool)
    _write(out / "MASTERY_BENCHMARK.json", {**bench, "grade_rows": bench["grade_rows"][:3]})
    _write(out / "AI_WAIKE_MASTERY_EVAL.json", eval_report)
    # ingest-facing contract copy
    ingest = ROOT / "ingest" / "learning_contract"
    _write(ingest / "waike_gunnchai_learning_contract.v1.json", contract)

    summary = {
        "ok": bool(tokens["WAIKE_AI_DIGITAL_MASTERY_PASS"]),
        "courses": contract["discovery"]["course_count"],
        "items": registry["item_count"],
        "overall_score": bench["overall_score"],
        "tool_use_passed": tool["passed"],
        "canary_pass": canary["pass"],
        "wrote": str(out / "AI_WAIKE_MASTERY_EVAL.json"),
    }
    print(json.dumps(summary, indent=2))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
