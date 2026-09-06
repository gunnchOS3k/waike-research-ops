"""Course-specific packaging for batch008 SEVEN_GC_APPRENTICESHIP."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch008.labs import LAB_SPECS_008

CID = "SEVEN_GC_APPRENTICESHIP"

SYLLABUS_ASSESSMENT_008 = {
    CID: (
        "Gary 7GC Research Desk: weekly SGC quizzes on evidence classes/recon/baseline/design/"
        "sim/analysis/audit/capstone/handoff/robustness, mid (20 original) on digital honesty, "
        "final (24 original) on external gates + claim discipline, practical over ten runnable labs, "
        "reproducible research portfolio. Mentor/hardware/field remain EXTERNAL_*."
    ),
}

SYLLABUS_DURATION_008 = {
    CID: (
        "Formats from programs/seven_gc_apprenticeship.md: Workshop 2h; Bootcamp 2 weeks; "
        "Course 8 digital weeks; Apprenticeship 12 weeks (weeks 1–10 digital + 11–12 external scaffolds). "
        "Budget ~6–8 hours/week. NO_AI weeks 4 and 7."
    ),
}

SYLLABUS_CLAIM_008 = {
    CID: (
        "First-class digital COURSE_DIGITAL_RC for SEVEN_GC_APPRENTICESHIP. RESEARCH_APPRENTICESHIP "
        "classification retained. Does not grant 3GPP/O-RAN membership or invent field/mentor completion. "
        "Instructor keys out of learner packet. Commercial standardized 6G does not exist today."
    ),
}

PITFALLS = {
    CID: {i: f"Week {i} SGC pitfall: unlabeled simulation, mentor fiction, or empty JSON." for i in range(1, 11)},
}


def _rubrics(course_id: str) -> list[dict[str, Any]]:
    return [
        {"rubric_id": f"{course_id}-lab", "title": "Research Desk lab", "criteria": [
            {"name": "machine_fields", "weight": 25, "desc": "Lab JSON fields honest"},
            {"name": "evidence_class", "weight": 25, "desc": "SIMULATED/DIGITAL labeled"},
            {"name": "empty_fails", "weight": 25, "desc": "Empty fails"},
            {"name": "print_pass", "weight": 25, "desc": "PASS rejected"},
        ]},
        {"rubric_id": f"{course_id}-assignment", "title": "Research journal", "criteria": [
            {"name": "ticket_ids", "weight": 40, "desc": "Uses SGC tickets"},
            {"name": "no_pii", "weight": 30, "desc": "No secrets/PII"},
            {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged"},
        ]},
        {"rubric_id": f"{course_id}-quiz", "title": "Knowledge check", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "Original stems"},
            {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
        ]},
        {"rubric_id": f"{course_id}-mid", "title": "Mid audit", "criteria": [
            {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
            {"name": "honesty", "weight": 40, "desc": "Simulated vs measured discipline"},
        ]},
        {"rubric_id": f"{course_id}-final-knowledge", "title": "Final knowledge", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
            {"name": "external_gates", "weight": 50, "desc": "EXTERNAL_* gates named"},
        ]},
        {"rubric_id": f"{course_id}-practical", "title": "Practical labs", "criteria": [
            {"name": "student_json", "weight": 40, "desc": "Reference passes; empty fails"},
            {"name": "negatives", "weight": 30, "desc": "Wrong submissions fail"},
            {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
        ]},
        {"rubric_id": f"{course_id}-project", "title": "Capstone package", "criteria": [
            {"name": "question_quality", "weight": 10, "desc": "Testable question"},
            {"name": "setup_provenance", "weight": 10, "desc": "Env/SHA/fixture"},
            {"name": "method", "weight": 10, "desc": "Method clarity"},
            {"name": "experiment_design", "weight": 10, "desc": "IV/DV/controls"},
            {"name": "evidence_integrity", "weight": 10, "desc": "Hashes/raw preserved"},
            {"name": "analysis", "weight": 10, "desc": "No overclaim"},
            {"name": "claim_discipline", "weight": 10, "desc": "Supports/does-not-support"},
            {"name": "limitations", "weight": 10, "desc": "Limitations explicit"},
            {"name": "communication", "weight": 10, "desc": "Presentation clarity"},
            {"name": "portfolio_quality", "weight": 10, "desc": "README + artifacts"},
        ]},
        {"rubric_id": f"{course_id}-portfolio", "title": "Portfolio", "criteria": [
            {"name": "claim_boundary", "weight": 40, "desc": "EXTERNAL gates + SIMULATED labels"},
            {"name": "machine_artifacts", "weight": 30, "desc": "Lab JSON digests"},
            {"name": "career_map", "weight": 30, "desc": "Aligned roles not granted"},
        ]},
    ]


def rubrics_008(course_id: str) -> list[dict[str, Any]]:
    if course_id != CID:
        raise KeyError(course_id)
    return _rubrics(course_id)


def lab_readme_008(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_008[lab_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "",
        spec["readme"], "",
        f"execution_mode: {spec.get('execution_mode')}",
        f"evidence_class: {spec.get('evidence_class')}",
        "",
        "Empty {} fails. PASS raises. No fabricated mentor/field completion.", "",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        "", spec["wrong_hint"], "",
    ])


def instructor_week_notes_008(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    return (
        f"# {course_id} — instructor week {n}\n\n"
        f"**Live example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; refuse MEASURED_FIELD upgrades.\n\n"
        f"**Hint ladder:** (1) name evidence class (2) point to fixture path (3) Socratic question only.\n\n"
        f"**Misconception:** treating SIMULATED KPI deltas as pier measurements.\n\n"
        f"**External gates:** mentor/hardware/field remain EXTERNAL_* — never auto-complete.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n"
    )


def presentation_008(course_id: str, week: dict[str, Any]) -> str:
    return f"# Week {week['week']}: {week['title']}\n\n{week['worked_example']}\n"


def instructor_packet_008(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        "Keys in instructor/answer_keys.json only.\n\n"
        "Teaching intent: reproducible digital research apprenticeship.\n"
        "Expected evidence: lab JSON with labeled SIMULATED/DIGITAL_REPRODUCTION classes.\n"
        "Remediation: re-run baseline with seed before allowing claim upgrades.\n"
        "Simulated-vs-measured guidance: never mark MEASURED_* without real captures.\n"
        "External human/physical/field gate notes: forms/rubrics/slots allowed; completion forbidden without evidence.\n"
        "gunnchAI may /explain and /quizme for practice; AI never silently grades.\n"
    )


def student_packet_008(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n{hook}\n\n"
        "Formats: Workshop / Bootcamp / 8-week Course / 12-week Apprenticeship.\n"
        "Submit lab JSON; empty/wrong/print-PASS fail.\n"
        "Tutor: `/waike lesson seven_gc_apprenticeship`, `/explain`, `/quizme` (practice only).\n"
        "Do not invent mentor signatures or field measurements.\n"
    )


def group_project_008(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_008(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\n\n"
        "Include: research README, experiment design, reproducibility instructions, logs/results,\n"
        "evidence hashes, limitations, optional screenshot without PII, rubric self-assessment,\n"
        "presentation/poster, optional mentor-review placeholder (EXTERNAL_HUMAN_GATE only).\n"
        "mentor_signed must remain false until real review exists.\n"
    )
