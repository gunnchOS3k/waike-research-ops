"""Course-specific packaging for batch007 DIGITAL_RC."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch007.labs import LAB_SPECS_007

SYLLABUS_ASSESSMENT_007 = {
    "EMBEDDED_PROTOTYPING": (
        "ForgeSense Subsystem Bench: weekly EP quizzes on MCU/GPIO/I2C/SPI/ADC/ISR/QEMU/DT/sleep, "
        "mid (20 original) on digital-first honesty, final (24 original) on capstone + PHYSICAL_PENDING, "
        "practical over ten runnable labs, subsystem portfolio. Complements HARDWARE_ENGINEERING."
    ),
    "GUNNCHOS_PRODUCT_LAB": (
        "gunnchOS Product Lab Bench: weekly GPL quizzes on charter/compat/checkout/compose/privacy/"
        "guest/semver/CI/pins, mid (20 original), final (24 original), practical over ten labs, "
        "product capstone with no_device_os_pr. Does not merge device-os #103."
    ),
}

SYLLABUS_DURATION_007 = {
    "EMBEDDED_PROTOTYPING": (
        "Ten ForgeSense Subsystem weeks (~6–8 hours/week). QEMU/digital-first; "
        "NO_AI weeks 4 and 9. PHYSICAL_PENDING for solder/OTA."
    ),
    "GUNNCHOS_PRODUCT_LAB": (
        "Ten Product Lab weeks (~6–8 hours/week). Compose/compat/privacy focus; "
        "NO_AI weeks 4 and 9. Accepted-main pins only."
    ),
}

SYLLABUS_CLAIM_007 = {
    "EMBEDDED_PROTOTYPING": (
        "Zephyr/J-STD topic labels PUBLIC_REFERENCE_ONLY. Does not grant certs. "
        "Standalone track — complements HARDWARE_ENGINEERING integration. Instructor keys out of learner packet."
    ),
    "GUNNCHOS_PRODUCT_LAB": (
        "PMI/privacy topic labels PUBLIC_REFERENCE_ONLY. Does not merge device-os #103. "
        "COURSE_DIGITAL_RC only — not REAL_STUDENT_E6 / REAL_TEACHER_E6."
    ),
}

PITFALLS = {
    "EMBEDDED_PROTOTYPING": {i: f"Week {i} EP pitfall: empty JSON, print-PASS, or physical claim without EVT." for i in range(1, 11)},
    "GUNNCHOS_PRODUCT_LAB": {i: f"Week {i} GPL pitfall: fabricated_outcomes, preview SHA in accepted, or device-os PR." for i in range(1, 11)},
}


def _rubrics(course_id: str, prefix: str) -> list[dict[str, Any]]:
    return [
        {"rubric_id": f"{course_id}-lab", "title": f"{prefix} lab", "criteria": [
            {"name": "machine_fields", "weight": 25, "desc": "Lab JSON fields honest"},
            {"name": "no_key_leak", "weight": 25, "desc": "No instructor keys"},
            {"name": "empty_fails", "weight": 25, "desc": "Empty fails"},
            {"name": "print_pass", "weight": 25, "desc": "PASS rejected"},
        ]},
        {"rubric_id": f"{course_id}-assignment", "title": f"{prefix} journal", "criteria": [
            {"name": "ticket_ids", "weight": 40, "desc": "Uses EP/GPL tickets"},
            {"name": "no_pii", "weight": 30, "desc": "No secrets/PII"},
            {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged"},
        ]},
        {"rubric_id": f"{course_id}-quiz", "title": f"{prefix} quiz", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "Original stems"},
            {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
        ]},
        {"rubric_id": f"{course_id}-mid", "title": f"{prefix} mid", "criteria": [
            {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
            {"name": "honesty", "weight": 40, "desc": "Fields-first discipline"},
        ]},
        {"rubric_id": f"{course_id}-final-knowledge", "title": f"{prefix} final", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
            {"name": "capstone_boundary", "weight": 50, "desc": "Capstone/physical/PR boundaries"},
        ]},
        {"rubric_id": f"{course_id}-practical", "title": f"{prefix} practical", "criteria": [
            {"name": "student_json", "weight": 40, "desc": "Reference passes; empty fails"},
            {"name": "negatives", "weight": 30, "desc": "Wrong submissions fail"},
            {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
        ]},
        {"rubric_id": f"{course_id}-project", "title": f"{prefix} project", "criteria": [
            {"name": "capstone_flags", "weight": 40, "desc": "Capstone honesty flags"},
            {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
            {"name": "no_key_leak", "weight": 30, "desc": "no_key_leak true"},
        ]},
        {"rubric_id": f"{course_id}-portfolio", "title": f"{prefix} portfolio", "criteria": [
            {"name": "claim_boundary", "weight": 40, "desc": "PHYSICAL_PENDING / no PR stated"},
            {"name": "machine_artifacts", "weight": 30, "desc": "Lab JSON digests"},
            {"name": "career_map", "weight": 30, "desc": "Aligned roles"},
        ]},
    ]


def rubrics_007(course_id: str) -> list[dict[str, Any]]:
    if course_id == "EMBEDDED_PROTOTYPING":
        return _rubrics(course_id, "ForgeSense")
    if course_id == "GUNNCHOS_PRODUCT_LAB":
        return _rubrics(course_id, "Product Lab")
    raise KeyError(course_id)


def lab_readme_007(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_007[lab_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "",
        "Empty {} fails. PASS raises.", "",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        "", spec["wrong_hint"], "",
    ])


def instructor_week_notes_007(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    return (
        f"# {course_id} — instructor week {n}\n\n"
        f"**Live example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n"
    )


def presentation_007(course_id: str, week: dict[str, Any]) -> str:
    return f"# Week {week['week']}: {week['title']}\n\n{week['worked_example']}\n"


def instructor_packet_007(course_id: str) -> str:
    return f"# Instructor packet — {course_id}\n\nKeys in instructor/answer_keys.json only.\n"


def student_packet_007(course_id: str, hook: str) -> str:
    return f"# Student packet — {course_id}\n\n{hook}\n\nSubmit lab JSON; empty/wrong/print-PASS fail.\n"


def group_project_007(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_007(course_id: str) -> str:
    return f"# Portfolio — {course_id}\n\nLab JSON + claim boundary paragraph.\n"
