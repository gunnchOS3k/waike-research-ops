"""Misconception diagnosis + remediation loop with evidence states (no demeaning labels)."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .skill_graph import build_skill_graph

# Evidence states — CERTAINLY_FILLED requires reassessment/transfer evidence
EVIDENCE_STATES = (
    "GAP_IDENTIFIED",
    "REMEDIATION_ASSIGNED",
    "PRACTICE_IN_PROGRESS",
    "REASSESSED",
    "TRANSFER_CHECKED",
    "CERTAINLY_FILLED",  # only after REASSESSED + TRANSFER_CHECKED
)

FORBIDDEN_LABELS = (
    "dumb",
    "slow",
    "hopeless",
    "bad student",
    "low iq",
    "lazy",
    "stupid",
)


def _privacy_safe_profile(learner_ref: str) -> dict[str, Any]:
    return {
        "learner_ref": learner_ref,  # opaque id only
        "strengths": [],
        "focus_skills": [],
        "labels": [],  # must never contain demeaning terms
        "privacy": {
            "no_demeaning_labels": True,
            "store_grades_locally_only": True,
            "pii_forbidden_in_git": True,
        },
    }


def diagnose_misconception(
    *,
    learner_ref: str,
    course_id: str,
    item_id: str,
    observed_wrong_choice: str | None,
    skill_hint: str | None = None,
) -> dict[str, Any]:
    graph = build_skill_graph()
    skill_id = skill_hint or f"skill:{course_id}:w01"
    node_ids = {n["id"] for n in graph["nodes"]}
    if skill_id not in node_ids:
        # fall back to first weekly skill for course
        for n in graph["nodes"]:
            if n.get("course_id") == course_id and n.get("kind") == "weekly_skill":
                skill_id = n["id"]
                break

    profile = _privacy_safe_profile(learner_ref)
    profile["focus_skills"] = [skill_id]

    diagnosis = {
        "schema": "waike.misconception_diagnosis.v1",
        "learner_ref": learner_ref,
        "course_id": course_id,
        "item_id": item_id,
        "skill_id": skill_id,
        "observed_wrong_choice": observed_wrong_choice,
        "hypothesis": f"Gap on {skill_id} — practice the prerequisite edge before new content.",
        "evidence_state": "GAP_IDENTIFIED",
        "student_model": profile,
        "forbidden_labels_checked": list(FORBIDDEN_LABELS),
        "demeaning_label_used": False,
    }
    return diagnosis


def remediation_loop(diagnosis: dict[str, Any], *, reassess_score: float | None = None, transfer_ok: bool | None = None) -> dict[str, Any]:
    """DIAGNOSE → ASSIGN → PRACTICE → REASSESS → TRANSFER. CERTAINLY_FILLED only with both."""
    states = ["GAP_IDENTIFIED"]
    steps = [
        {"step": "DIAGNOSE", "evidence_state": "GAP_IDENTIFIED", "detail": diagnosis.get("hypothesis")},
        {
            "step": "ASSIGN",
            "evidence_state": "REMEDIATION_ASSIGNED",
            "detail": f"Remediation packet for {diagnosis.get('skill_id')}",
        },
        {
            "step": "PRACTICE",
            "evidence_state": "PRACTICE_IN_PROGRESS",
            "detail": "Isomorphic practice items (anti-memorization)",
        },
    ]
    states.extend(["REMEDIATION_ASSIGNED", "PRACTICE_IN_PROGRESS"])

    final = "PRACTICE_IN_PROGRESS"
    if reassess_score is not None:
        steps.append(
            {
                "step": "REASSESS",
                "evidence_state": "REASSESSED",
                "detail": f"reassess_score={reassess_score}",
                "score": reassess_score,
            }
        )
        states.append("REASSESSED")
        final = "REASSESSED"
        if transfer_ok is True and reassess_score >= 0.8:
            steps.append(
                {
                    "step": "TRANSFER",
                    "evidence_state": "TRANSFER_CHECKED",
                    "detail": "Transfer item passed on isomorphic variant",
                }
            )
            states.append("TRANSFER_CHECKED")
            steps.append(
                {
                    "step": "CLOSE",
                    "evidence_state": "CERTAINLY_FILLED",
                    "detail": "Reassessment + transfer evidence present",
                }
            )
            states.append("CERTAINLY_FILLED")
            final = "CERTAINLY_FILLED"
        elif transfer_ok is False or (reassess_score is not None and reassess_score < 0.8):
            steps.append(
                {
                    "step": "HOLD",
                    "evidence_state": "REASSESSED",
                    "detail": "Not CERTAINLY_FILLED — reassessment/transfer incomplete or below bar",
                }
            )

    # Refuse CERTAINLY_FILLED without evidence
    if final == "CERTAINLY_FILLED" and ("REASSESSED" not in states or "TRANSFER_CHECKED" not in states):
        final = "REASSESSED"

    return {
        "schema": "waike.remediation_loop.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "loop": "DIAGNOSE→ASSIGN→PRACTICE→REASSESS→TRANSFER",
        "steps": steps,
        "evidence_states_seen": states,
        "final_evidence_state": final,
        "certainly_filled_requires": ["REASSESSED", "TRANSFER_CHECKED"],
        "student_model": diagnosis.get("student_model"),
    }
