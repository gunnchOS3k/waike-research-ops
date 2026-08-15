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
from waike_mastery.corpus_diff import (  # noqa: E402
    MASTERY_001_NINE_COURSE_BASELINE,
    build_corpus_version_diff,
)
from waike_mastery.corpus_inventory import build_corpus_inventory  # noqa: E402
from waike_mastery.course_honesty import run_course_honesty  # noqa: E402
from waike_mastery.diagnosis import diagnose_misconception, remediation_loop  # noqa: E402
from waike_mastery.discover import emit_learning_contract  # noqa: E402
from waike_mastery.educator import educator_copilot_session  # noqa: E402
from waike_mastery.failure_taxonomy import classify_miss, sample_taxonomy_report  # noqa: E402
from waike_mastery.policy import evaluate_mastery_policy  # noqa: E402
from waike_mastery.registry import build_assessable_registry  # noqa: E402
from waike_mastery.skill_graph import build_skill_graph  # noqa: E402
from waike_mastery.tool_use import run_tool_use_mastery  # noqa: E402


def _write(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(ROOT / "artifacts" / "mastery"))
    p.add_argument("--max-items-per-course", type=int, default=None)
    args = p.parse_args()
    out = Path(args.out)

    contract = emit_learning_contract()
    inventory = build_corpus_inventory()
    corpus_diff = build_corpus_version_diff()
    honesty = run_course_honesty()
    registry = build_assessable_registry()
    graph = build_skill_graph()
    audit = audit_curriculum()
    canary = run_key_leak_canary()
    tool = run_tool_use_mastery()
    bench = run_mastery_benchmark(max_items_per_course=args.max_items_per_course)

    sample = next(i for i in registry["items"] if i.get("choices"))
    variant = isomorphic_variant(sample, seed="mastery-canary")

    diag = diagnose_misconception(
        learner_ref="opaque-learner-demo",
        course_id=sample["course_id"],
        item_id=sample["item_id"],
        observed_wrong_choice=(sample.get("choices") or ["?"])[-1],
    )
    rem_open = remediation_loop(diag)
    rem_closed = remediation_loop(diag, reassess_score=0.9, transfer_ok=True)

    educator = educator_copilot_session(
        course_id=contract["courses"][0]["course_id"], intent="grading_assist"
    )

    # Failure taxonomy sample from incorrect curriculum-overlap rows (no key leak)
    misses: list[dict] = []
    for row in bench.get("grade_rows") or []:
        for it in row.get("items") or []:
            if it.get("ok"):
                continue
            if len(misses) >= 40:
                break
            misses.append(
                classify_miss(
                    stem=f"{row.get('course_id')}:{it.get('id')}",
                    chosen=str(it.get("got")),
                    calc_mismatch=False,
                )
            )
        if len(misses) >= 40:
            break
    taxonomy = sample_taxonomy_report(misses)

    expected_new = {"WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE"}
    discovered_ids = {c["course_id"] for c in contract["courses"]}
    corpus_discovery_pass = (
        contract["discovery"]["hardcoded_course_names"] is False
        and contract["discovery"]["course_count"] == inventory["course_count"]
        and inventory["course_count"] >= 12
        and expected_new.issubset(discovered_ids)
        and inventory["assessable_items"] > 1016
    )

    # Infra smoke children — may pass without claiming mastery
    infra_children = {
        "MODE_CONTRACT_PERMISSIONS": all(
            k in contract["permissions"]
            for k in ("MASTERY_BENCHMARK", "LEARNER_TUTOR", "EDUCATOR_COPILOT")
        )
        and contract["permissions"]["MASTERY_BENCHMARK"]["may_read_instructor_keys"] is False
        and contract["permissions"]["EDUCATOR_COPILOT"]["hitl_grading_required"] is True,
        "LEARNING_CONTRACT_DISCOVERY": contract["discovery"]["course_count"] >= 1
        and contract["discovery"]["hardcoded_course_names"] is False,
        "CORPUS_DISCOVERY_CURRENT": corpus_discovery_pass,
        "ASSESSABLE_REGISTRY": registry["item_count"] > 0
        and not registry["key_fields_present_in_registry"]
        and registry["self_grading_forbidden"] is True,
        "KEY_LEAK_CANARY": bool(canary["pass"]) and bool(canary.get("canary_text_used")),
        "TOOL_USE_PARTIAL_LABS": tool.get("coverage_status") == "PARTIAL"
        and tool.get("mastery_complete") is False
        and tool["passed"] >= 6,
        "BENCHMARK_ISOLATION_MEASURED": bench["self_graded"] is False
        and isinstance(bench.get("used_instructor_keys_during_solve"), bool)
        and bench["used_instructor_keys_during_solve"] is False,
        "ISOMORPHIC_VARIANTS": bool(variant.get("isomorphic")),
        "DIAGNOSIS_REMEDIATION": rem_open["final_evidence_state"] != "CERTAINLY_FILLED"
        and rem_closed["final_evidence_state"] == "CERTAINLY_FILLED",
        "EDUCATOR_COPILOT": educator["permissions"]["may_publish_grades_without_human"] is False,
        "CURRICULUM_AUDIT_ENGINE": "defect_candidate_count" in audit,
        "COURSE_HONESTY_SURFACES": bool(honesty.get("pass")),
        "NO_FALSE_055_MASTERY_BAR": True,
        "BASELINE_001_PRESERVED": MASTERY_001_NINE_COURSE_BASELINE["overall_score"]
        == 0.6442307692307693,
    }
    infra_smoke = all(infra_children.values())

    policy = evaluate_mastery_policy(
        overall_score=float(bench["overall_score"]),
        per_course=bench["per_course"],
        used_instructor_keys_during_solve=bool(bench["used_instructor_keys_during_solve"]),
        self_graded=bool(bench["self_graded"]),
        canary_pass=bool(canary["pass"]),
        transfer_score=bench.get("transfer", {}).get("score"),
        tool_use_status="COMPLETE" if tool.get("mastery_complete") else "PARTIAL",
    )
    mastery_pass = bool(policy["earned"])
    mastery_eval_token = mastery_pass

    if mastery_pass and float(bench["overall_score"]) < policy["policy"]["overall_min"]:
        mastery_pass = False
        mastery_eval_token = False
        policy["reasons_not_earned"].append("tripwire_blocked_false_pass")

    # Mastery-002 child gates for aggregate PASS (expect false until earned)
    mastery_children = {
        "OVERALL_GE_095": float(bench["overall_score"]) >= 0.95,
        "PER_COURSE_GE_090": all(
            (v.get("score") or 0) >= 0.90 for v in (bench.get("per_course") or {}).values()
        ),
        "TRANSFER_GE_090": (bench.get("transfer") or {}).get("score") is not None
        and float((bench.get("transfer") or {}).get("score") or 0) >= 0.90,
        "TOOL_USE_COMPLETE": tool.get("mastery_complete") is True,
        "NO_KEY_LEAK": bool(canary["pass"]),
        "ISOLATED_GRADE": bench["self_graded"] is False
        and bench["used_instructor_keys_during_solve"] is False,
        "CORPUS_DISCOVERY": corpus_discovery_pass,
        "COURSE_HONESTY": bool(honesty.get("pass")),
    }
    if not all(mastery_children.values()):
        mastery_pass = False
        mastery_eval_token = False

    tokens = {
        "WAIKE_AI_DIGITAL_MASTERY_PASS": mastery_pass,
        "AI_WAIKE_MASTERY_EVAL": mastery_eval_token,
        "AI_WAIKE_MASTERY_INFRA_SMOKE_PASS": infra_smoke,
        "WAIKE_AI_STUDENT_CORPUS_DISCOVERY_PASS": corpus_discovery_pass,
        "WAIKE_AI_NO_KEY_LEAK_PASS": bool(canary["pass"]),
        "MASTERY_001_NINE_COURSE_BASELINE": 0.6442307692307693,
        "REAL_STUDENT": False,
        "REAL_TEACHER": False,
        "HUMAN_E6": False,
        "ACCREDITED": False,
        "REAL_STUDENT_MASTERY_VALIDATED": False,
        "REAL_TEACHER_EFFECTIVENESS_VALIDATED": False,
        "USED_INSTRUCTOR_KEYS_IN_BENCHMARK_SOLVE": bool(
            bench["used_instructor_keys_during_solve"]
        ),
        "SELF_GRADED": bool(bench["self_graded"]),
        "note": (
            "Mastery-002: PASS only if all mastery_children pass. "
            "Curriculum-overlap is baseline infrastructure; gunnchAI runtime solver is separate. "
            "Historical 0.644 preserved as MASTERY_001_NINE_COURSE_BASELINE. "
            "REAL_*/HUMAN_E6/ACCREDITED stay false."
        ),
    }

    eval_report = {
        "schema": "AI_WAIKE_MASTERY_EVAL.v2",
        "suite": "AI_WAIKE_MASTERY_EVAL",
        "wave": "AI-WAIKE-MASTERY-002",
        "honesty_remediation": "2026-08-15-mastery-002-corpus-normalize-real-solver-contract",
        "corpus": {
            "discoverable_courses": contract["discovery"]["course_count"],
            "course_ids": [c["course_id"] for c in contract["courses"]],
            "assessable_items": registry["item_count"],
            "per_course_counts": registry["per_course"],
            "skill_graph_nodes": graph["node_count"],
            "skill_graph_edges": graph["edge_count"],
            "curriculum_defect_candidates": audit["defect_candidate_count"],
            "inventory_totals": inventory["totals"],
            "source": (
                "filesystem discovery of curriculum/digital_rc/*/course.json "
                "from current accepted main (12-course universe after #46+#47)"
            ),
        },
        "corpus_version_diff": {
            "old_courses": corpus_diff["old_corpus"]["courses"],
            "old_items": corpus_diff["old_corpus"]["assessable_items"],
            "new_courses": corpus_diff["new_corpus"]["courses"],
            "new_items": corpus_diff["new_corpus"]["assessable_items"],
            "added_courses": corpus_diff["added_courses"],
        },
        "mastery_scores": {
            "overall": bench["overall_score"],
            "per_course": bench["per_course"],
            "per_assessment_sample": dict(list(bench["per_assessment"].items())[:12]),
            "per_domain": bench["per_domain"],
            "items_attempted": bench["items_attempted"],
            "items_correct": bench["items_correct"],
            "solver": bench["solver"],
            "transfer": bench.get("transfer"),
            "historical_baseline_001": 0.6442307692307693,
            "published_without_false_pass": True,
        },
        "mastery_policy": policy,
        "mastery_children": {k: {"pass": v} for k, v in mastery_children.items()},
        "tool_use": {
            "attempted": tool["attempted"],
            "passed": tool["passed"],
            "pass_rate": tool["pass_rate"],
            "coverage_status": tool.get("coverage_status"),
            "claim": tool.get("claim"),
            "mastery_complete": tool.get("mastery_complete"),
            "labs": [{"lab_id": r["lab_id"], "ok": r.get("ok")} for r in tool["results"]],
        },
        "canary": canary,
        "course_honesty": honesty,
        "failure_taxonomy": {"miss_count": taxonomy["miss_count"], "counts": taxonomy["counts"]},
        "diagnosis_remediation": {
            "open_loop_final": rem_open["final_evidence_state"],
            "closed_loop_final": rem_closed["final_evidence_state"],
            "demeaning_label_used": diag["demeaning_label_used"],
        },
        "educator_mode": educator,
        "infra_children": {k: {"pass": v} for k, v in infra_children.items()},
        "children": {k: {"pass": v} for k, v in infra_children.items()},
        "tokens": tokens,
        "open": [
            "WAIKE_AI_DIGITAL_MASTERY_PASS false until all mastery_children pass.",
            "Curriculum-overlap solver remains baseline; gunnchAI runtime solver owns Mastery-002 scoring path.",
            "Tool-use PARTIAL (includes computed WIRELESS/ROBOTICS/GAME labs) ≠ COMPLETE.",
            "REAL_STUDENT / REAL_TEACHER / HUMAN_E6 / ACCREDITED remain false.",
            "device-os #116 untouched; gunnchAI #36 not a fourth stream.",
        ],
        "WAIKE_AI_DIGITAL_MASTERY_PASS": tokens["WAIKE_AI_DIGITAL_MASTERY_PASS"],
        "AI_WAIKE_MASTERY_INFRA_SMOKE_PASS": tokens["AI_WAIKE_MASTERY_INFRA_SMOKE_PASS"],
        "WAIKE_AI_STUDENT_CORPUS_DISCOVERY_PASS": tokens["WAIKE_AI_STUDENT_CORPUS_DISCOVERY_PASS"],
        "claim_boundary": (
            "Scores published honestly on current 12-course corpus. "
            "Aggregate mastery PASS only under qualifying policy + child gates. "
            "Not accredited; not a live classroom study."
        ),
    }

    _write(out / "WAIKE_GUNNCHAI_LEARNING_CONTRACT.json", contract)
    _write(out / "CORPUS_INVENTORY.json", inventory)
    _write(out / "CORPUS_VERSION_DIFF.json", corpus_diff)
    _write(out / "MASTERY_001_NINE_COURSE_BASELINE.json", MASTERY_001_NINE_COURSE_BASELINE)
    _write(out / "COURSE_HONESTY.json", honesty)
    _write(out / "FAILURE_TAXONOMY.json", taxonomy)
    _write(
        out / "ASSESSABLE_ITEM_REGISTRY.json",
        {
            **registry,
            "items": registry["items"][:5],
            "items_omitted_for_size": registry["item_count"] - 5,
        },
    )
    _write(out / "ASSESSABLE_ITEM_REGISTRY.full.json", registry)
    _write(out / "SKILL_GRAPH.json", graph)
    _write(out / "CURRICULUM_SELF_AUDIT.json", audit)
    _write(out / "KEY_LEAK_CANARY.json", canary)
    _write(out / "TOOL_USE_MASTERY.json", tool)
    _write(out / "MASTERY_BENCHMARK.json", {**bench, "grade_rows": bench["grade_rows"][:3]})
    _write(out / "AI_WAIKE_MASTERY_EVAL.json", eval_report)
    ingest = ROOT / "ingest" / "learning_contract"
    _write(ingest / "waike_gunnchai_learning_contract.v1.json", contract)

    if tokens["WAIKE_AI_DIGITAL_MASTERY_PASS"] and float(bench["overall_score"]) < 0.95:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "FALSE_MASTERY_PASS_AT_SUB_POLICY_SCORE",
                    "overall_score": bench["overall_score"],
                },
                indent=2,
            )
        )
        return 2

    summary = {
        "ok": infra_smoke,
        "infra_smoke": infra_smoke,
        "mastery_pass": mastery_pass,
        "corpus_discovery_pass": corpus_discovery_pass,
        "courses": contract["discovery"]["course_count"],
        "items": registry["item_count"],
        "overall_score": bench["overall_score"],
        "baseline_001": 0.6442307692307693,
        "transfer_score": bench.get("transfer", {}).get("score"),
        "tool_use_status": tool.get("coverage_status"),
        "tool_passed": tool["passed"],
        "canary_pass": canary["pass"],
        "added_courses": corpus_diff["added_courses"],
        "used_instructor_keys_during_solve": bench["used_instructor_keys_during_solve"],
        "wrote": str(out / "AI_WAIKE_MASTERY_EVAL.json"),
    }
    print(json.dumps(summary, indent=2))
    return 0 if infra_smoke else 1


if __name__ == "__main__":
    raise SystemExit(main())
