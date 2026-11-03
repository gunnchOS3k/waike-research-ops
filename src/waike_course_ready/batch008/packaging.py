"""Course-specific packaging for batch008 — SEVEN_GC_APPRENTICESHIP."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch008.labs import LAB_SPECS_008

_C = "SEVEN_GC_APPRENTICESHIP"

SYLLABUS_ASSESSMENT_008 = {
    _C: (
        "Research Bench grading: weekly SGA quizzes on claim ledgers, manifests, NTN delay, LEO Doppler, "
        "top-k beams, paired intervals, O-RAN loop placement, twin calibration, and validity threats; "
        "a 20-item midterm on evidence classes and link physics; a 24-item final on loop placement, "
        "calibration honesty, ethics, and capstone tracing; ten recomputing labs; a traced research packet."
    ),
}

SYLLABUS_DURATION_008 = {
    _C: (
        "Ten Research Bench weeks at roughly 7–9 hours each, including one reproducible rerun per week. "
        "Weeks 4 (Doppler by hand) and 9 (validity self-review) are NO_AI. Synthetic and cited evidence only."
    ),
}

SYLLABUS_CLAIM_008 = {
    _C: (
        "3GPP TR 38.811 / TR 38.901 and O-RAN Alliance specifications are PUBLIC_REFERENCE_ONLY topic labels. "
        "No private competition IQ, no affiliation claims, no paper submission, and twin outputs stay "
        "UNCALIBRATED_NO_MEASUREMENTS. COURSE_DIGITAL_RC only, not REAL_STUDENT_E6 or REAL_TEACHER_E6."
    ),
}

PITFALLS_008 = {
    1: "A MEASURED row with no dataset_ref gets quietly dropped instead of marked OPEN.",
    2: "A digest pasted from an earlier config; the grader recomputes sha256 from config_text.",
    3: "The LEO 2.0 ms answer copied onto a GEO altitude.",
    4: "Reporting the (v/c)·f bound as a measured Doppler shift.",
    5: "Quoting top-3 as if it were top-1 accuracy.",
    6: "Using z = 1.96 for five pairs, or claiming improvement when the interval crosses zero.",
    7: "Placing model training inside the real-time loop.",
    8: "Setting calibrated_claim true because twin and reference sim agree.",
    9: "Listing only internal threats; external, construct, and conclusion rows left blank.",
    10: "A figure without config digest and seed, or submitted_claim flipped to true.",
}


def rubrics_008(course_id: str) -> list[dict[str, Any]]:
    if course_id != _C:
        raise KeyError(course_id)
    return [
        {"rubric_id": f"{_C}-lab", "title": "Research Bench recompute lab", "criteria": [
            {"name": "recomputed_values", "weight": 40, "desc": "Submitted numbers match the grader's recomputation from inputs"},
            {"name": "evidence_class", "weight": 30, "desc": "SYNTHETIC_SIM / CITED_SPEC labels present and correct"},
            {"name": "rejects_stub", "weight": 30, "desc": "Empty and PASS-only submissions are refused"},
        ]},
        {"rubric_id": f"{_C}-assignment", "title": "SGA ticket write-up", "criteria": [
            {"name": "ticket_trace", "weight": 35, "desc": "Cites the SGA ticket and the manifest digest"},
            {"name": "claim_scope", "weight": 35, "desc": "States the scenario the claim covers and no further"},
            {"name": "ai_mode", "weight": 30, "desc": "AI mode disclosed; NO_AI weeks hand-worked"},
        ]},
        {"rubric_id": f"{_C}-quiz", "title": "Weekly method check", "criteria": [
            {"name": "concept_fit", "weight": 50, "desc": "Stems probe the week's calculation or method"},
            {"name": "key_privacy", "weight": 50, "desc": "Answer key lives only in the instructor tree"},
        ]},
        {"rubric_id": f"{_C}-mid", "title": "Midterm: evidence and link physics", "criteria": [
            {"name": "fresh_items", "weight": 60, "desc": "Twenty items that are not weekly restatements"},
            {"name": "numeric_reasoning", "weight": 40, "desc": "Delay, Doppler, and interval arithmetic"},
        ]},
        {"rubric_id": f"{_C}-final-knowledge", "title": "Final: placement, calibration, ethics", "criteria": [
            {"name": "fresh_items", "weight": 50, "desc": "Twenty-four items beyond weekly stems"},
            {"name": "boundary_judgement", "weight": 50, "desc": "Calibration, affiliation, and submission boundaries"},
        ]},
        {"rubric_id": f"{_C}-practical", "title": "Practical: rerun a figure", "criteria": [
            {"name": "manifest_rerun", "weight": 50, "desc": "Figure regenerates from digest and seed"},
            {"name": "wrong_inputs_fail", "weight": 50, "desc": "Altered inputs change the recomputed result"},
        ]},
        {"rubric_id": f"{_C}-project", "title": "Traced research packet", "criteria": [
            {"name": "labs_passed", "weight": 30, "desc": "Six or more Research Bench labs passed"},
            {"name": "figure_trace", "weight": 40, "desc": "Every figure carries config_sha256 and seed"},
            {"name": "no_submission", "weight": 30, "desc": "submitted_claim false; owner decides submission"},
        ]},
        {"rubric_id": f"{_C}-portfolio", "title": "Apprentice portfolio", "criteria": [
            {"name": "ledger_update", "weight": 40, "desc": "Week-one ledger revised with term results"},
            {"name": "twin_gap", "weight": 30, "desc": "Calibration gap stated with the measurements needed"},
            {"name": "roles", "weight": 30, "desc": "Research-assistant roles, credentials not implied"},
        ]},
    ]


def lab_readme_008(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_008[lab_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "",
        "The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.", "",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        "", f"Common miss: {spec['wrong_hint']}", "",
    ])


def instructor_week_notes_008(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    return (
        f"# {course_id} — mentor notes, week {n}\n\n"
        f"**Board work:** {week['worked_example']}\n\n"
        f"**Rerun check:** ask one apprentice to regenerate `{week['lab_id']}` from their manifest.\n\n"
        f"**Watch for:** {PITFALLS_008[n]}\n"
    )


def presentation_008(course_id: str, week: dict[str, Any]) -> str:
    return f"# Research Bench {week['week']}: {week['title']}\n\nNumbers on the board: {week['worked_example']}\n"


def instructor_packet_008(course_id: str) -> str:
    return (
        f"# Mentor packet — {course_id}\n\n"
        "Answer keys sit in instructor/answer_keys.json. Rerun one figure per apprentice in week ten.\n"
    )


def student_packet_008(course_id: str, hook: str) -> str:
    return (
        f"# Apprentice packet — {course_id}\n\n{hook}\n\n"
        "Keep a claim ledger from week one and a manifest for every run.\n"
    )


def group_project_008(course_id: str, title: str, assignment: str) -> str:
    return f"# Cross-campus research packet — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_008(course_id: str) -> str:
    return (
        f"# Apprentice portfolio — {course_id}\n\n"
        "Revised claim ledger, manifests with digests, and a plain statement of the twin calibration gap.\n"
    )
