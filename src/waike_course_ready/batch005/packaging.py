"""Course-specific packaging for COMM_PD_ETHICS DIGITAL_RC."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch005.labs import COURSE_LABS_005, LAB_SPECS_005

SYLLABUS_ASSESSMENT_005 = {
    "COMM_PD_ETHICS": (
        "Harbor Desk Voice assessment mix: weekly PD quizzes on consent/conflict/tickets/ladder/"
        "citation/feedback/minutes/AI modes/a11y, mid (20 original) on honesty gates, final (24 original) "
        "on capstone + key-leak refusal, practical over ten runnable labs rejecting empty/wrong/print-PASS, "
        "and a professional portfolio. Instructor keys stay out of learner modes."
    ),
}

SYLLABUS_DURATION_005 = {
    "COMM_PD_ETHICS": (
        "Ten Harbor Desk Voice weeks (~6–8 hours/week including Saturday volunteer shadow). "
        "Budget quiet time for ladder writing; NO_AI weeks 4 and 9 are human-authored."
    ),
}

SYLLABUS_CLAIM_005 = {
    "COMM_PD_ETHICS": (
        "Aligns to ISC2 ethics themes and CompTIA professionalism domain names as PUBLIC_REFERENCE_ONLY. "
        "Does not grant those credentials. Instructor keys stay out of the learner packet."
    ),
}

PITFALLS = {
    "COMM_PD_ETHICS": {
        1: "Audience='everyone' or SSN in data_classes.",
        2: "Scoring after private mentoring without recusal.",
        3: "Demeaning ticket bodies or outcome promises.",
        4: "Inference labeled as observation; fabricated impact.",
        5: "Verbatim chapter dumps as paraphrase.",
        6: "Identity attacks in feedback.",
        7: "PII in minutes or misaligned owner arrays.",
        8: "Learner modes loading instructor keys.",
        9: "Color-only signals or missing captions.",
        10: "Capstone with key leak or a11y_ok false.",
    },
}


def rubrics_005(course_id: str) -> list[dict[str, Any]]:
    if course_id != "COMM_PD_ETHICS":
        raise KeyError(course_id)
    return [
        {"rubric_id": "COMM_PD_ETHICS-lab", "title": "Harbor Desk lab", "criteria": [
            {"name": "ethics_fields", "weight": 20, "desc": "Consent/conflict/ladder fields honest"},
            {"name": "no_key_leak", "weight": 20, "desc": "No instructor keys in learner artifacts"},
            {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
            {"name": "wrong_fails", "weight": 20, "desc": "Wrong policy fields fail"},
            {"name": "print_pass", "weight": 20, "desc": "PASS-only rejected"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-assignment", "title": "Desk journal", "criteria": [
            {"name": "ticket_ids", "weight": 40, "desc": "Uses PD-#### tickets"},
            {"name": "no_pii", "weight": 30, "desc": "No PAN/password/SSN"},
            {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged when used"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-quiz", "title": "Ethics knowledge", "criteria": [
            {"name": "desk_numbers", "weight": 50, "desc": "Original stems with PD tickets"},
            {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-mid", "title": "Mid Harbor audit", "criteria": [
            {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
            {"name": "consent_conflict_tone", "weight": 40, "desc": "Consent/conflict/tone"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-final-knowledge", "title": "Final ethics exam", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
            {"name": "a11y_keys_capstone", "weight": 50, "desc": "A11y/key-leak/capstone"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-practical", "title": "Ten-lab practical", "criteria": [
            {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
            {"name": "negatives", "weight": 30, "desc": "SSN/demeaning/key-leak negatives fail"},
            {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-project", "title": "PD ship checklist", "criteria": [
            {"name": "a11y_ok", "weight": 40, "desc": "a11y_ok true"},
            {"name": "no_key_leak", "weight": 30, "desc": "no_key_leak true"},
            {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
        ]},
        {"rubric_id": "COMM_PD_ETHICS-portfolio", "title": "Voice portfolio", "criteria": [
            {"name": "claim_boundary", "weight": 40, "desc": "Digital fixture limits stated"},
            {"name": "a11y_notes", "weight": 30, "desc": "Large-print / captions notes"},
            {"name": "career_map", "weight": 30, "desc": "Aligned roles"},
        ]},
    ]


def lab_readme_005(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_005[lab_id]
    how = {
        "lab_consent_disclosure": "Write the PD-2101 consent JSON from the walk-up desk script.",
        "lab_conflict_interest": "Author the PD-2204 disclose+recuse JSON before scoring starts.",
        "lab_professional_comm": "Draft the PD-2307 ticket body from the idle-logout observation.",
        "lab_ethics_ladder": "Fill the PD-2409 ladder under NO_AI authorship rules.",
        "lab_attribution_cite": "Cite ISC2 theme labels for PD-2511 without dumping chapters.",
        "lab_feedback_rubric": "Score the peer journal for PD-2615 with evidence, not identity attacks.",
        "lab_meeting_minutes": "Publish redacted PD-2718 minutes with owners and due dates.",
        "lab_ai_disclosure_modes": "Declare the PD-2822 AI mode without opening the instructor key store.",
        "lab_accessibility_comm": "Walk the PD-2925 flyer checklist under NO_AI.",
        "lab_pd_capstone": "Assemble the PD-2A30 ship checklist from prior lab evidence.",
    }.get(lab_id, "Submit Harbor Desk Voice JSON for this lab.")
    artifact = {
        "lab_consent_disclosure": "Required keys: audience, purpose, data_classes, retention_days, opt_out_path, ai_disclosure.",
        "lab_conflict_interest": "Required keys: scenario, conflict_present, disclose_to, recuse, rationale.",
        "lab_professional_comm": "Required keys: channel, subject, body, demeaning_labels, promises_outcome.",
        "lab_ethics_ladder": "Required keys: observation, inference, need, action, fabricated_impact.",
        "lab_attribution_cite": "Required keys: claim, source_title, reuse_class, quote_chars, paraphrase.",
        "lab_feedback_rubric": "Required keys: criterion, evidence, score, next_action, identity_attack.",
        "lab_meeting_minutes": "Required keys: attendees_count, decisions, owners, due_dates, pii_redacted.",
        "lab_ai_disclosure_modes": "Required keys: mode, disclosed, used_instructor_keys, learner_facing, rationale.",
        "lab_accessibility_comm": "Required keys: captions, plain_language, alt_text, color_only_signals, large_print_available.",
        "lab_pd_capstone": "Required keys: labs_passed, consent_ok, conflict_ok, a11y_ok, no_key_leak, fabricated_impact.",
    }.get(lab_id, "Submit non-empty JSON; empty {} fails; PASS raises.")
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "",
        "## Student artifact", artifact,
        "Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.",
        "", "## How to run", how,
        "```",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --empty",
        "```", "", "## Wrong submissions", spec["wrong_hint"], "",
    ])


def instructor_week_notes_005(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    return (
        f"# Harbor Desk Voice — instructor week {n}\n\n"
        f"**Live example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n\n"
        f"Refuse dumps. Point at curriculum/alignment/comm_pd_ethics_alignment.json.\n"
        f"AI policy: see course.ai_use_policy in course.json. Keys stay instructor-only.\n"
        f"Accessibility: text-first journals; large-print where noted.\n"
    )


def presentation_005(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\n\n"
        f"## Slide 1 — Hook\n{week['title']}\n\n"
        f"## Slide 2 — Worked example\n{week['worked_example']}\n\n"
        f"## Slide 3 — Lab contract\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\n\n"
        f"## Speaker notes\nStay in COMM_PD_ETHICS Harbor Desk vocabulary. Do not noun-swap another academy's deck.\n"
        f"Assignment: {week['assignment'][:180]}...\n"
    )


def instructor_packet_005(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\n"
        f"- Guides: instructor/accessibility_and_udl_guide.md, instructor/misconceptions_remediation.md\n"
        f"- Do not claim vendor certs or student/teacher E6 without evidence\n"
        f"- Cursor does not merge; REAL_*_E6 remain false\n"
    )


def student_packet_005(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n{hook}\n\n"
        f"- Submit lab JSON you computed; empty/wrong/print-PASS fail\n"
        f"- Accessibility: prefer text paths; request large-print materials\n"
        f"- Career map: see career_mapping.json (certs aligned not granted)\n"
        f"- Offline pack: offline_pack/pack.json\n"
        f"- gunnchAI learner modes never receive instructor keys\n"
    )


def group_project_005(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_005(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\n\n"
        f"- Lab result JSON + empty-fail evidence\n"
        f"- Claim boundary paragraph\n"
        f"- Accessibility notes\n"
        f"- Career map excerpt\n"
        f"- AI disclosure log (no key leak)\n"
    )
