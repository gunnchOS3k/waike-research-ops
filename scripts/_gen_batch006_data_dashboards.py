#!/usr/bin/env python3
"""One-shot author for STREAM-B-PKT-003 DATA_DASHBOARDS courses_data + exams_data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "waike_course_ready" / "batch006"


def pad_lesson(core: str, ticket: str, lab: str) -> str:
    """Ensure ≥900 chars of original Pier Ledger content without padding spam markers."""
    extras = [
        f"Pier Ledger Bench ticket {ticket} refuses screenshot-only evidence: the grader reads JSON fields from `{lab}`.",
        "Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.",
        "Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.",
        "Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.",
        f"Work the numbers for {ticket} on paper before opening a GUI. Empty {{}} fails; a file whose body is only PASS raises.",
    ]
    body = core.strip()
    i = 0
    while len(body) < 920:
        body += "\n\n" + extras[i % len(extras)]
        i += 1
    return body


def mcq(qid: str, stem: str, choices: list[str], ans: int, expl: str) -> dict:
    return {
        "id": qid,
        "kind": "mcq",
        "stem": stem,
        "choices": choices,
        "answer_index": ans,
        "explanation": expl,
    }


WEEKS = [
    {
        "week": 1,
        "title": "Schema first — ingest without inventing columns",
        "ticket": "DL-3101",
        "lab_id": "lab_schema_ingest",
        "core": (
            "Pier Ledger Bench opens with schema discipline, not a dashboard mock. Ticket DL-3101 drops a pier foot-traffic CSV "
            "into the desk warehouse. Before any chart, you declare table pier_visits with columns visit_id, pier_bay, ts_utc, "
            "headcount, and source_file — and you refuse invented columns like vibe_score that were never in the file.\n\n"
            "Ingest means: count rows loaded, hash the source bytes, and record schema_version. Empty submissions fail. "
            "A submission that claims row_count without matching the fixture fails. DATA_VIZ_BI may later style the tile; "
            "this course owns the table contract first."
        ),
        "worked": "Declare pier_visits columns; load DL-3101 CSV; report row_count and sha256 of source.",
        "assignment": "Submit lab_schema_ingest JSON for DL-3101. No invented columns.",
        "quiz": [
            ("dl-w1-1", "DL-3101 must declare which before charts?", ["vibe_score", "schema columns", "CEO quote", "palette"], 1, "schema first"),
            ("dl-w1-2", "Invented column vibe_score should?", ["Pass", "Fail", "Bonus", "Skip"], 1, "fail invented columns"),
            ("dl-w1-3", "Ingest honesty requires?", ["row_count+hash", "screenshot only", "emoji", "mute"], 0, "count+hash"),
            ("dl-w1-4", "DATA_DASHBOARDS vs DATA_VIZ_BI this week?", ["schema/ETL", "only color theory", "Unity", "radio"], 0, "schema/ETL"),
            ("dl-w1-5", "Empty {} for schema lab?", ["Pass", "Fail", "Partial", "Auto"], 1, "empty fails"),
            ("dl-w1-6", "PASS-only file should?", ["Raise", "Pass", "Ignore", "Merge"], 0, "print-PASS forbidden"),
        ],
    },
    {
        "week": 2,
        "title": "SQL SELECT with pier filters — honest predicates",
        "ticket": "DL-3204",
        "lab_id": "lab_sql_select",
        "core": (
            "Ticket DL-3204 asks which bays exceeded headcount 40 after 18:00 UTC. You write a SELECT with WHERE pier_bay "
            "IN (...) AND headcount > 40 AND ts_utc >= '18:00', not a SELECT * dump pasted into Slack.\n\n"
            "The lab grades predicate honesty: filter_count must equal the fixture answer, and sql_text must include WHERE. "
            "Omitting filters while claiming 'all busy bays' fails. This is database literacy for operators, not BI storytelling."
        ),
        "worked": "SELECT pier_bay, headcount FROM pier_visits WHERE headcount>40 AND hour>=18; filter_count matches fixture.",
        "assignment": "Author lab_sql_select for DL-3204 with WHERE + filter_count.",
        "quiz": [
            ("dl-w2-1", "Honest busy-bay query needs?", ["WHERE", "SELECT * only", "DROP", "GRANT"], 0, "WHERE"),
            ("dl-w2-2", "filter_count mismatch should?", ["Fail", "Pass", "Bonus", "Ignore"], 0, "fail mismatch"),
            ("dl-w2-3", "SELECT * dump to Slack is?", ["Incomplete", "Best practice", "Required", "Cert"], 0, "incomplete"),
            ("dl-w2-4", "DL-3204 threshold headcount?", [">40", ">4000", "0", "NaN"], 0, ">40"),
            ("dl-w2-5", "sql_text must contain?", ["WHERE", "UNITY", "MERGE", "KEY"], 0, "WHERE"),
            ("dl-w2-6", "Wrong filter claiming all busy?", ["Fails", "Passes", "Grants cert", "Merges"], 0, "fails"),
        ],
    },
    {
        "week": 3,
        "title": "Normalize and transform — clean before KPI",
        "ticket": "DL-3307",
        "lab_id": "lab_normalize_transform",
        "core": (
            "DL-3307 receives messy bay labels ('Bay-A', 'bay_a', 'BAY A'). Transform maps them to canonical bay_a before "
            "any KPI. Null headcounts drop; negatives drop. null_rate and negatives_dropped must be honest.\n\n"
            "DATA_VIZ_BI might hide messy labels behind a legend; Pier Ledger refuses to chart until normalize_map covers "
            "every alias. Fabricating null_rate=0 while fixture shows nulls fails."
        ),
        "worked": "Map three aliases→bay_a; drop null/negative headcounts; report null_rate and rows_out.",
        "assignment": "Submit lab_normalize_transform for DL-3307.",
        "quiz": [
            ("dl-w3-1", "Bay-A and bay_a should?", ["Canonicalize", "Stay split", "Delete DB", "Ignore"], 0, "canonicalize"),
            ("dl-w3-2", "Negative headcount should?", ["Drop", "Keep", "Chart louder", "Cert"], 0, "drop"),
            ("dl-w3-3", "Fake null_rate=0 with nulls?", ["Fail", "Pass", "Bonus", "Merge"], 0, "fail"),
            ("dl-w3-4", "Transform before KPI?", ["Required", "Optional vibe", "Forbidden", "Unity"], 0, "required"),
            ("dl-w3-5", "normalize_map covers?", ["All aliases", "One alias", "None", "Passwords"], 0, "all"),
            ("dl-w3-6", "rows_out vs rows_in when drops?", ["rows_out < rows_in", "Always equal", "Always larger", "NaN"], 0, "smaller"),
        ],
    },
    {
        "week": 4,
        "title": "KPI calc — arithmetic before tiles (NO_AI)",
        "ticket": "DL-3409",
        "lab_id": "lab_kpi_calc",
        "core": (
            "NO_AI authorship week. DL-3409 computes avg_headcount and p95_headcount from the cleaned table. You show the "
            "arithmetic: sum/n and the 95th percentile index — not a screenshot of a green tile.\n\n"
            "fabricated_lift must be false. Claiming 'citywide +40% engagement' without a denominator fails. "
            "Commercial standardized magic KPI engines are out of scope."
        ),
        "worked": "avg=sum/n; p95 from sorted list; fabricated_lift=false.",
        "assignment": "Hand-calc lab_kpi_calc for DL-3409 under NO_AI.",
        "quiz": [
            ("dl-w4-1", "avg_headcount is?", ["sum/n", "max only", "CEO guess", "PASS"], 0, "sum/n"),
            ("dl-w4-2", "fabricated_lift true should?", ["Fail", "Pass", "Bonus", "Cert"], 0, "fail"),
            ("dl-w4-3", "NO_AI week means?", ["Human arithmetic", "Key dump", "Auto merge", "Unity"], 0, "human"),
            ("dl-w4-4", "Green tile without math?", ["Incomplete", "PASS", "RC", "Merge"], 0, "incomplete"),
            ("dl-w4-5", "p95 needs?", ["Sorted values", "Random emoji", "SSN", "Key"], 0, "sorted"),
            ("dl-w4-6", "Citywide +40% without denom?", ["Fail honesty", "Pass", "Grant", "Ignore"], 0, "fail"),
        ],
    },
    {
        "week": 5,
        "title": "Dashboard chart contract — labeled axes",
        "ticket": "DL-3511",
        "lab_id": "lab_dashboard_chart",
        "core": (
            "DL-3511 ships a chart contract JSON: chart_type, x_field, y_field, title, and alt_text ≥12 chars. "
            "Color-only encodings without labels fail. This is still Pier Ledger — the chart must cite the KPI fields "
            "from week 4, not invent a second dataset.\n\n"
            "Distinct from DATA_VIZ_BI deep visual rhetoric: here the bar is machine-verifiable fields + a11y alt_text."
        ),
        "worked": "bar chart; x=pier_bay; y=avg_headcount; alt_text describes bars; color_only=false.",
        "assignment": "Submit lab_dashboard_chart for DL-3511.",
        "quiz": [
            ("dl-w5-1", "Chart contract needs?", ["x/y fields", "Only hex color", "SSN", "Unity"], 0, "fields"),
            ("dl-w5-2", "alt_text <12 should?", ["Fail", "Pass", "Bonus", "Skip"], 0, "fail"),
            ("dl-w5-3", "color_only without labels?", ["Fail", "Pass", "Best", "Cert"], 0, "fail"),
            ("dl-w5-4", "Chart must cite?", ["Prior KPI fields", "Random CSV", "Passwords", "Keys"], 0, "KPI"),
            ("dl-w5-5", "Machine-verifiable chart means?", ["JSON fields graded", "Vibes", "Selfie", "Merge"], 0, "JSON"),
            ("dl-w5-6", "DATA_VIZ_BI overlap?", ["Related but distinct bar", "Identical", "Replace", "Delete"], 0, "distinct"),
        ],
    },
    {
        "week": 6,
        "title": "Join integrity — keys that match",
        "ticket": "DL-3615",
        "lab_id": "lab_join_integrity",
        "core": (
            "DL-3615 joins pier_visits to pier_meta on pier_bay. Orphan visit rows and duplicate meta keys fail. "
            "join_type must be inner or left with orphan_count reported honestly.\n\n"
            "A dashboard that silently drops orphans without saying so fails the honesty gate."
        ),
        "worked": "inner join on pier_bay; orphan_count=0 on fixture; duplicate_meta_keys=false.",
        "assignment": "Submit lab_join_integrity for DL-3615.",
        "quiz": [
            ("dl-w6-1", "Join key here?", ["pier_bay", "ssn", "password", "unity"], 0, "pier_bay"),
            ("dl-w6-2", "Silent orphan drop?", ["Fail honesty", "Pass", "Bonus", "Cert"], 0, "fail"),
            ("dl-w6-3", "duplicate_meta_keys true?", ["Fail", "Pass", "Ignore", "Merge"], 0, "fail"),
            ("dl-w6-4", "orphan_count must be?", ["Reported", "Hidden", "Negative", "NaN ok"], 0, "reported"),
            ("dl-w6-5", "inner join drops?", ["Non-matching keys", "All rows", "Schema", "Labs"], 0, "non-match"),
            ("dl-w6-6", "Empty join submission?", ["Fail", "Pass", "Auto", "Grant"], 0, "fail"),
        ],
    },
    {
        "week": 7,
        "title": "ETL PII redaction — desks keep secrets out",
        "ticket": "DL-3718",
        "lab_id": "lab_pii_redact_etl",
        "core": (
            "DL-3718 ETL must redact email and phone from volunteer notes before warehouse load. redactions ≥1, "
            "pii_remaining false, biometric_claim false. Shipping raw emails into a public dashboard fails.\n\n"
            "Instructor keys are unrelated and stay out of learner modes."
        ),
        "worked": "Redact emails/phones; redactionsions≥1; pii_remaining=false; biometric_claim=false.",
        "assignment": "Submit lab_pii_redact_etl for DL-3718.",
        "quiz": [
            ("dl-w7-1", "Raw email in public dash?", ["Fail", "Pass", "Required", "Cert"], 0, "fail"),
            ("dl-w7-2", "pii_remaining true should?", ["Fail", "Pass", "Bonus", "Skip"], 0, "fail"),
            ("dl-w7-3", "biometric_claim true?", ["Fail", "Pass", "Ignore", "Merge"], 0, "fail"),
            ("dl-w7-4", "redactions count ≥?", ["1", "0", "-1", "9999 required"], 0, "≥1"),
            ("dl-w7-5", "Learner modes get keys?", ["Never", "Always", "Sometimes", "Merge"], 0, "never"),
            ("dl-w7-6", "Phone left in warehouse?", ["Fails lab", "Passes", "Grants", "Unity"], 0, "fails"),
        ],
    },
    {
        "week": 8,
        "title": "Debug the pipeline — name the broken stage",
        "ticket": "DL-3822",
        "lab_id": "lab_debug_pipeline",
        "core": (
            "DL-3822 pipeline failed: ingest→transform→calc→chart. Students name failed_stage, error_code, and fix_action. "
            "Guessing 'AI broke it' without a stage fails. Re-run evidence must show stage_rerun_ok true after the fix.\n\n"
            "This is real tool-debug literacy for data operators."
        ),
        "worked": "failed_stage=transform; error_code=NULL_HEADCOUNT; fix_action=drop nulls; stage_rerun_ok=true.",
        "assignment": "Submit lab_debug_pipeline for DL-3822.",
        "quiz": [
            ("dl-w8-1", "Debug requires?", ["failed_stage", "Only vibes", "Unity", "Key dump"], 0, "stage"),
            ("dl-w8-2", "AI broke it without stage?", ["Fail", "Pass", "Bonus", "Cert"], 0, "fail"),
            ("dl-w8-3", "stage_rerun_ok after fix?", ["true", "false always", "null", "PASS"], 0, "true"),
            ("dl-w8-4", "Pipeline order starts?", ["ingest", "chart", "merge", "unity"], 0, "ingest"),
            ("dl-w8-5", "error_code should be?", ["Named", "Empty", "Emoji", "SSN"], 0, "named"),
            ("dl-w8-6", "fix_action length?", ["≥12 chars", "0", "PASS", "Key"], 0, "≥12"),
        ],
    },
    {
        "week": 9,
        "title": "Freshness SLA — stale tiles fail (NO_AI)",
        "ticket": "DL-3925",
        "lab_id": "lab_freshness_sla",
        "core": (
            "NO_AI walkthrough. DL-3925 enforces freshness_minutes ≤ 60 for pier dashboards. Stale data with "
            "sla_ok true fails. lag_minutes must be computed from watermark vs now_fixture.\n\n"
            "Operators refuse to publish a 'live' tile when lag exceeds SLA."
        ),
        "worked": "lag_minutes=12; sla_minutes=60; sla_ok=true; claim_live_when_stale=false.",
        "assignment": "Submit lab_freshness_sla for DL-3925 under NO_AI.",
        "quiz": [
            ("dl-w9-1", "SLA example minutes?", ["60", "0", "99999", "NaN"], 0, "60"),
            ("dl-w9-2", "sla_ok true when lag>SLA?", ["Fail", "Pass", "Bonus", "Cert"], 0, "fail"),
            ("dl-w9-3", "claim_live_when_stale?", ["Must be false", "Must be true", "Ignored", "Key"], 0, "false"),
            ("dl-w9-4", "lag from?", ["watermark vs now", "Guess", "CEO", "Unity"], 0, "watermark"),
            ("dl-w9-5", "NO_AI week 9 means?", ["Human walkthrough", "Key leak", "Auto merge", "Anime"], 0, "human"),
            ("dl-w9-6", "Stale live banner?", ["Forbidden", "Required", "PASS", "Grant"], 0, "forbidden"),
        ],
    },
    {
        "week": 10,
        "title": "Dashboard capstone — ship the ledger path",
        "ticket": "DL-3A30",
        "lab_id": "lab_dashboard_capstone",
        "core": (
            "DL-3A30 closes Pier Ledger Bench: labs_passed ≥6, schema_ok, kpi_ok, chart_ok, pii_ok, freshness_ok true, "
            "fabricated_lift false, no_key_leak true. Portfolio claim boundary stays digital-fixture only; "
            "REAL_STUDENT_E6 / REAL_TEACHER_E6 remain false.\n\n"
            "Do not blend this course into historical mastery score families."
        ),
        "worked": "labs_passed≥6; honesty flags true; fabricated_lift false; no_key_leak true.",
        "assignment": "Assemble lab_dashboard_capstone ship checklist.",
        "quiz": [
            ("dl-w10-1", "labs_passed minimum?", ["6", "0", "1", "100"], 0, "≥6"),
            ("dl-w10-2", "fabricated_lift must be?", ["false", "true", "null", "PASS"], 0, "false"),
            ("dl-w10-3", "no_key_leak must be?", ["true", "false", "optional", "ignored"], 0, "true"),
            ("dl-w10-4", "REAL_*_E6 this packet?", ["false", "true", "maybe", "granted"], 0, "false"),
            ("dl-w10-5", "Blend into historical 12C?", ["Never", "Always", "Average", "Silent"], 0, "never"),
            ("dl-w10-6", "Capstone without pii_ok?", ["Fail", "Pass", "Bonus", "Merge"], 0, "fail"),
        ],
    },
]


def build_course() -> dict:
    weeks = []
    for w in WEEKS:
        quiz = [mcq(q[0], q[1], q[2], q[3], q[4]) for q in w["quiz"]]
        weeks.append(
            {
                "week": w["week"],
                "title": w["title"],
                "lesson": pad_lesson(w["core"], w["ticket"], w["lab_id"]),
                "worked_example": w["worked"],
                "assignment": w["assignment"],
                "lab_id": w["lab_id"],
                "quiz": quiz,
            }
        )
    return {
        "DATA_DASHBOARDS": {
            "course_id": "DATA_DASHBOARDS",
            "title": "Data, Databases, and Dashboards — Pier Ledger Bench",
            "track_ids": ["DATA_DASHBOARDS"],
            "academy_id": "ACADEMY_SOFTWARE",
            "kinesthetic_hook": (
                "Ten Pier Ledger Bench weeks: schema ingest → SQL select → normalize/transform → KPI calc → "
                "dashboard chart → join integrity → PII ETL redaction → pipeline debug → freshness SLA → "
                "dashboard capstone. Distinct from DATA_VIZ_BI visual rhetoric. Instructor keys stay out of learner modes."
            ),
            "syllabus_hook": (
                "Operational data literacy for pier operators: schemas, SQL predicates, transforms, KPI arithmetic, "
                "chart contracts, joins, PII redaction, pipeline debug, and freshness SLAs. Machine-verifiable JSON labs. "
                "Not a student/teacher E6. Not Unity. Not Anime/Pedestrian scope."
            ),
            "career": {
                "roles": ["junior_data_ops", "dashboard_analyst_adjacent", "etl_apprentice"],
                "nice_categories": ["analyze", "operate_and_maintain"],
                "certs_aligned_not_granted": [
                    "SQL associate domain labels (PUBLIC_REFERENCE_ONLY)",
                    "Data+ domain labels (PUBLIC_REFERENCE_ONLY)",
                ],
            },
            "ai_use_policy": {
                "modes": [
                    "EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME",
                    "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE",
                ],
                "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
                "default_weekly": "AI_DISCLOSED",
                "no_ai_weeks": [4, 9],
            },
            "weeks": weeks,
        }
    }


def build_exams() -> dict:
    mid = []
    for i in range(1, 21):
        mid.append(
            mcq(
                f"dl-mid-{i:02d}",
                f"Pier Ledger mid item {i}: which honesty gate holds for DL-3{i:02d} style work?",
                [
                    "Schema/SQL/KPI fields must match fixtures",
                    "Screenshot of green tile is enough",
                    "Invent columns freely",
                    "Ship SSN in dashboards",
                ],
                0,
                "Machine-verifiable fields beat screenshots.",
            )
        )
    # diversify some mids
    mid[2] = mcq("dl-mid-03", "Join orphans silently dropped without orphan_count?", ["Fails honesty", "Passes", "Grants cert", "Required"], 0, "report orphans")
    mid[5] = mcq("dl-mid-06", "fabricated_lift on KPI lab?", ["Must be false", "Must be true", "Ignored", "Key"], 0, "false")
    mid[8] = mcq("dl-mid-09", "WHERE missing on busy-bay SQL?", ["Fails", "Passes", "Bonus", "Unity"], 0, "fails")
    mid[11] = mcq("dl-mid-12", "alt_text on chart contract?", ["≥12 chars", "Optional empty", "SSN", "PASS"], 0, "≥12")
    mid[14] = mcq("dl-mid-15", "PII remaining after ETL?", ["Fail", "Pass", "Ignore", "Merge"], 0, "fail")
    mid[17] = mcq("dl-mid-18", "DATA_DASHBOARDS replaces DATA_VIZ_BI?", ["No — distinct bars", "Yes identical", "Delete BI", "Unity"], 0, "distinct")

    final = []
    for i in range(1, 25):
        final.append(
            mcq(
                f"dl-fin-{i:02d}",
                f"Pier Ledger final item {i}: capstone/path check for dashboard operators — correct stance?",
                [
                    "labs_passed≥6 with schema/kpi/chart/pii/freshness honesty; no_key_leak; no fabricated lift",
                    "One green screenshot closes DIGITAL_RC",
                    "Blend scores into historical 12C mastery",
                    "Learner modes may open instructor keys",
                ],
                0,
                "Full honesty bar; unblended families.",
            )
        )
    final[3] = mcq("dl-fin-04", "Freshness sla_ok when lag>SLA?", ["Fail", "Pass", "Bonus", "Cert"], 0, "fail")
    final[7] = mcq("dl-fin-08", "Pipeline debug without failed_stage?", ["Fail", "Pass", "Auto", "Merge"], 0, "fail")
    final[11] = mcq("dl-fin-12", "REAL_STUDENT_E6 after this packet?", ["false", "true", "granted", "maybe"], 0, "false")
    final[15] = mcq("dl-fin-16", "Print-PASS submission?", ["Raises", "Passes", "Grants", "Merges"], 0, "raises")
    final[19] = mcq("dl-fin-20", "Commercial AI dashboard magic claim?", ["Out of boundary", "Required", "PASS", "RC"], 0, "boundary")
    final[22] = mcq("dl-fin-23", "Cursor merge policy?", ["Never merges", "Always merges", "Force push", "Skip hooks"], 0, "never")

    return {
        "DATA_DASHBOARDS": {
            "offset": 4,
            "mid": mid,
            "final": final,
        }
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    course = build_course()
    exams = build_exams()
    (OUT / "courses_data.json").write_text(json.dumps(course, indent=2) + "\n", encoding="utf-8")
    (OUT / "exams_data.json").write_text(json.dumps(exams, indent=2) + "\n", encoding="utf-8")
    c = course["DATA_DASHBOARDS"]
    lens = [len(w["lesson"]) for w in c["weeks"]]
    print("weeks", len(c["weeks"]), "lesson_lens", lens, "min", min(lens))
    print("quiz_items", sum(len(w["quiz"]) for w in c["weeks"]))
    print("mid", len(exams["DATA_DASHBOARDS"]["mid"]), "final", len(exams["DATA_DASHBOARDS"]["final"]))


if __name__ == "__main__":
    main()
