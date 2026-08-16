"""Course-specific packaging for DATA_DASHBOARDS DIGITAL_RC."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch006.labs import LAB_SPECS_006

SYLLABUS_ASSESSMENT_006 = {
    "DATA_DASHBOARDS": (
        "Pier Ledger Bench assessment mix: weekly DL quizzes on schema/SQL/transform/KPI/chart/join/"
        "PII/debug/freshness, mid (20 original) on honesty gates, final (24 original) on capstone + "
        "key-leak refusal, practical over ten runnable labs rejecting empty/wrong/print-PASS, and a "
        "data-ops portfolio. Distinct from DATA_VIZ_BI. Instructor keys stay out of learner modes."
    ),
}

SYLLABUS_DURATION_006 = {
    "DATA_DASHBOARDS": (
        "Ten Pier Ledger Bench weeks (~6–8 hours/week including Saturday data desk shadow). "
        "Budget quiet time for KPI arithmetic; NO_AI weeks 4 and 9 are human-authored."
    ),
}

SYLLABUS_CLAIM_006 = {
    "DATA_DASHBOARDS": (
        "Aligns to SQL associate / Data+ domain names as PUBLIC_REFERENCE_ONLY. "
        "Does not grant those credentials. Distinct from DATA_VIZ_BI visual rhetoric. "
        "Instructor keys stay out of the learner packet."
    ),
}

PITFALLS = {
    "DATA_DASHBOARDS": {
        1: "Invented columns or missing source hash.",
        2: "SELECT * without WHERE / filter_count.",
        3: "Fake null_rate or negatives kept.",
        4: "fabricated_lift or screenshot-only KPI.",
        5: "color_only chart or tiny alt_text.",
        6: "Silent orphans or duplicate meta keys.",
        7: "PII left in warehouse / biometric claim.",
        8: "Debug without naming failed_stage.",
        9: "sla_ok true while lag exceeds SLA.",
        10: "Capstone with key leak or fabricated_lift.",
    },
}


def rubrics_006(course_id: str) -> list[dict[str, Any]]:
    if course_id != "DATA_DASHBOARDS":
        raise KeyError(course_id)
    return [
        {"rubric_id": "DATA_DASHBOARDS-lab", "title": "Pier Ledger lab", "criteria": [
            {"name": "schema_sql_fields", "weight": 20, "desc": "Schema/SQL/KPI fields honest"},
            {"name": "no_key_leak", "weight": 20, "desc": "No instructor keys in learner artifacts"},
            {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
            {"name": "wrong_fails", "weight": 20, "desc": "Wrong data fields fail"},
            {"name": "print_pass", "weight": 20, "desc": "PASS-only rejected"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-assignment", "title": "Ledger journal", "criteria": [
            {"name": "ticket_ids", "weight": 40, "desc": "Uses DL-#### tickets"},
            {"name": "no_pii", "weight": 30, "desc": "No PAN/password/SSN"},
            {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged when used"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-quiz", "title": "Data knowledge", "criteria": [
            {"name": "ledger_numbers", "weight": 50, "desc": "Original stems with DL tickets"},
            {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-mid", "title": "Mid ledger audit", "criteria": [
            {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
            {"name": "schema_sql_kpi", "weight": 40, "desc": "Schema/SQL/KPI honesty"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-final-knowledge", "title": "Final data exam", "criteria": [
            {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
            {"name": "freshness_keys_capstone", "weight": 50, "desc": "Freshness/key-leak/capstone"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-practical", "title": "Ten-lab practical", "criteria": [
            {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
            {"name": "negatives", "weight": 30, "desc": "Invented-col/PII/stale negatives fail"},
            {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-project", "title": "Dashboard ship checklist", "criteria": [
            {"name": "schema_kpi_chart", "weight": 40, "desc": "schema/kpi/chart ok"},
            {"name": "no_key_leak", "weight": 30, "desc": "no_key_leak true"},
            {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
        ]},
        {"rubric_id": "DATA_DASHBOARDS-portfolio", "title": "Ledger portfolio", "criteria": [
            {"name": "claim_boundary", "weight": 40, "desc": "Digital fixture limits stated"},
            {"name": "machine_artifacts", "weight": 30, "desc": "Hashes/SQL/KPI JSON included"},
            {"name": "career_map", "weight": 30, "desc": "Aligned roles"},
        ]},
    ]


def lab_readme_006(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_006[lab_id]
    how = {
        "lab_schema_ingest": "Declare pier_visits schema and ingest DL-3101 CSV with hash.",
        "lab_sql_select": "Write the DL-3204 WHERE query and report filter_count.",
        "lab_normalize_transform": "Map bay aliases and drop null/negative headcounts for DL-3307.",
        "lab_kpi_calc": "Hand-calc avg and p95 for DL-3409 under NO_AI.",
        "lab_dashboard_chart": "Author the DL-3511 chart contract with alt_text.",
        "lab_join_integrity": "Join visits to meta on pier_bay for DL-3615; report orphans.",
        "lab_pii_redact_etl": "Redact email/phone before warehouse load on DL-3718.",
        "lab_debug_pipeline": "Name failed_stage and fix for DL-3822; rerun ok.",
        "lab_freshness_sla": "Compute lag vs 60-minute SLA for DL-3925 under NO_AI.",
        "lab_dashboard_capstone": "Assemble DL-3A30 ship checklist from prior lab evidence.",
    }.get(lab_id, "Submit Pier Ledger Bench JSON for this lab.")
    artifact = {
        "lab_schema_ingest": "Required keys: table, columns, row_count, source_sha256, invented_columns.",
        "lab_sql_select": "Required keys: sql_text, filter_count, has_where, threshold.",
        "lab_normalize_transform": "Required keys: normalize_map, rows_in, rows_out, null_rate, negatives_dropped.",
        "lab_kpi_calc": "Required keys: avg_headcount, p95_headcount, n, fabricated_lift.",
        "lab_dashboard_chart": "Required keys: chart_type, x_field, y_field, title, alt_text, color_only.",
        "lab_join_integrity": "Required keys: join_key, join_type, orphan_count, duplicate_meta_keys, rows_joined.",
        "lab_pii_redact_etl": "Required keys: redactions, pii_remaining, biometric_claim, fields_redacted.",
        "lab_debug_pipeline": "Required keys: failed_stage, error_code, fix_action, stage_rerun_ok.",
        "lab_freshness_sla": "Required keys: lag_minutes, sla_minutes, sla_ok, claim_live_when_stale.",
        "lab_dashboard_capstone": "Required keys: labs_passed, schema_ok, kpi_ok, chart_ok, pii_ok, freshness_ok, no_key_leak, fabricated_lift.",
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


def instructor_week_notes_006(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    return (
        f"# Pier Ledger Bench — instructor week {n}\n\n"
        f"**Live example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n\n"
        f"Refuse dumps. Point at curriculum/alignment/data_dashboards_alignment.json.\n"
        f"AI policy: see course.ai_use_policy in course.json. Keys stay instructor-only.\n"
        f"Keep distinct from DATA_VIZ_BI visual rhetoric.\n"
    )


def presentation_006(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\n\n"
        f"## Slide 1 — Hook\n{week['title']}\n\n"
        f"## Slide 2 — Worked example\n{week['worked_example']}\n\n"
        f"## Slide 3 — Lab contract\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\n\n"
        f"## Speaker notes\nStay in DATA_DASHBOARDS Pier Ledger vocabulary. Do not noun-swap DATA_VIZ_BI decks.\n"
        f"Assignment: {week['assignment'][:180]}...\n"
    )


def instructor_packet_006(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\n"
        f"- Guides: instructor/accessibility_and_udl_guide.md, instructor/misconceptions_remediation.md\n"
        f"- Distinct from DATA_VIZ_BI; do not claim vendor certs or student/teacher E6 without evidence\n"
        f"- Cursor does not merge; REAL_*_E6 remain false\n"
    )


def student_packet_006(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n{hook}\n\n"
        f"- Submit lab JSON you computed; empty/wrong/print-PASS fail\n"
        f"- Accessibility: prefer text paths; request large-print materials\n"
        f"- Career map: see career_mapping.json (certs aligned not granted)\n"
        f"- Offline pack: offline_pack/pack.json\n"
        f"- gunnchAI learner modes never receive instructor keys\n"
    )


def group_project_006(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_006(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\n\n"
        f"- Lab result JSON + empty-fail evidence\n"
        f"- Claim boundary paragraph (distinct from DATA_VIZ_BI)\n"
        f"- Schema/SQL/KPI/chart artifacts\n"
        f"- Career map excerpt\n"
        f"- AI disclosure log (no key leak)\n"
    )
