"""Emit digital RC packages, learner/teacher ingest, and product catalog projection."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.exams import exam_is_restatement
from waike_course_ready.labs import COURSE_LABS
from waike_ops.prereqs import COURSE_PREREQS
from waike_course_ready.packaging import (
    SYLLABUS_ASSESSMENT,
    SYLLABUS_CLAIM,
    SYLLABUS_DURATION,
    group_project,
    instructor_packet,
    instructor_week_notes,
    lab_readme,
    portfolio,
    presentation,
    rubrics as course_rubrics,
    student_packet,
)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "curriculum" / "digital_rc"


def _md_escape(s: str) -> str:
    return s.strip() + "\n"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def _dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def _rubrics(course_id: str) -> list[dict[str, Any]]:
    return course_rubrics(course_id)


def emit_course(course_id: str) -> dict[str, Any]:
    c = COURSES[course_id]
    base = OUT / course_id
    extras = extra_assessment_items(course_id)
    labs = COURSE_LABS[course_id]

    syllabus = [
        f"# {c['title']}",
        "",
        "## Who this is for",
        c["syllabus_hook"],
        "",
        "## Tracks and academy",
        f"- Tracks: {', '.join(c['track_ids'])}",
        f"- Academy: {c['academy_id']}",
        "",
        "## Duration",
        SYLLABUS_DURATION[course_id],
        "",
        "## Weekly map",
    ]
    for w in c["weeks"]:
        syllabus.append(f"- Week {w['week']:02d}: {w['title']}")
    syllabus += [
        "",
        "## Assessments",
        SYLLABUS_ASSESSMENT[course_id],
        "",
        "## Claim boundary",
        SYLLABUS_CLAIM[course_id],
        "",
        f"## Kinesthetic hook",
        c["kinesthetic_hook"],
        "",
    ]
    _write(base / "syllabus.md", "\n".join(syllabus))

    answer_keys: dict[str, Any] = {"schema": "waike.answer_keys.v1", "course_id": course_id, "quizzes": {}, "mid": [], "final": []}
    quiz_count = 0
    quiz_items = 0
    for w in c["weeks"]:
        wk = f"w{w['week']:02d}"
        _write(base / "weeks" / wk / "lesson.md", f"# Week {w['week']}: {w['title']}\n\n{w['lesson']}\n\n## Worked example\n\n{w['worked_example']}\n")
        _write(
            base / "assignments" / f"a{w['week']:02d}.md",
            f"# Assignment A{w['week']:02d} — {w['title']}\n\n{w['assignment']}\n\nLab to run: `{w['lab_id']}`\n",
        )
        quiz_obj = {
            "quiz_id": f"{course_id}-q{w['week']:02d}",
            "week": w["week"],
            "items": [{"id": i["id"], "kind": i["kind"], "stem": i["stem"], "choices": i["choices"]} for i in w["quiz"]],
        }
        _dump(base / "quizzes" / f"q{w['week']:02d}.json", quiz_obj)
        answer_keys["quizzes"][quiz_obj["quiz_id"]] = [
            {"id": i["id"], "answer_index": i["answer_index"], "explanation": i["explanation"]} for i in w["quiz"]
        ]
        quiz_count += 1
        quiz_items += len(w["quiz"])
        _write(base / "presentation" / f"week_{w['week']:02d}.md", presentation(course_id, w))
        _write(base / "instructor" / f"week_{w['week']:02d}_notes.md", instructor_week_notes(course_id, w))

    for lab_id in labs:
        _write(base / "labs" / lab_id / "README.md", lab_readme(course_id, lab_id))

    mid_learner = [{"id": i["id"], "kind": i["kind"], "stem": i["stem"], "choices": i["choices"]} for i in extras["mid"]]
    fin_learner = [{"id": i["id"], "kind": i["kind"], "stem": i["stem"], "choices": i["choices"]} for i in extras["final"]]
    _dump(base / "assessments" / "mid_course.json", {"assessment_id": f"{course_id}-mid", "items": mid_learner})
    _dump(base / "assessments" / "final_knowledge.json", {"assessment_id": f"{course_id}-final", "items": fin_learner})
    answer_keys["mid"] = [{"id": i["id"], "answer_index": i["answer_index"], "explanation": i["explanation"]} for i in extras["mid"]]
    answer_keys["final"] = [{"id": i["id"], "answer_index": i["answer_index"], "explanation": i["explanation"]} for i in extras["final"]]

    practical = {
        "practical_id": f"{course_id}-practical",
        "labs": labs,
        "pass_rule": "all listed labs ok=true AND package negatives fail",
    }
    _dump(base / "assessments" / "final_practical.json", practical)
    _write(
        base / "projects" / "group_project.md",
        group_project(course_id, c["title"], c["weeks"][-1]["assignment"]),
    )

    rubrics = _rubrics(course_id)
    _dump(base / "rubrics" / "rubrics.json", rubrics)
    for r in rubrics:
        lines = [f"# {r['title']}", ""]
        for crit in r["criteria"]:
            lines.append(f"- **{crit['name']}** ({crit['weight']}%): {crit['desc']}")
        _write(base / "rubrics" / f"{r['rubric_id']}.md", "\n".join(lines))

    _dump(base / "instructor" / "answer_keys.json", answer_keys)
    _write(base / "instructor" / "INSTRUCTOR_PACKET.md", instructor_packet(course_id))
    _write(base / "student" / "STUDENT_PACKET.md", student_packet(course_id, c["kinesthetic_hook"]))
    offline = {
        "schema": "waike.offline_pack.v1",
        "course_id": course_id,
        "lesson_ids": [f"{course_id}-w{w['week']:02d}" for w in c["weeks"]],
        "labs": labs,
        "product_pack_hint": "wireless_basics_101 maps as a session-shaped compatibility probe only",
    }
    _dump(base / "offline_pack" / "pack.json", offline)
    _dump(
        base / "portfolio" / "artifacts.json",
        {
            "required": ["lab_result_json", "change_or_intent_or_policy", "scope_paragraph"],
            "no_pii": True,
        },
    )
    _write(base / "portfolio" / "PORTFOLIO.md", portfolio(course_id))
    _dump(base / "career_mapping.json", c["career"])
    if c.get("ai_use_policy"):
        _dump(base / "ai_use_policy.json", c["ai_use_policy"])

    # Full DIGITAL_RC extras (guides / skill graph / misconceptions / gunnchAI contract / a11y / readings)
    if course_id == "DATA_DASHBOARDS":
        _dump(base / "prerequisites.json", {
            "course_id": course_id,
            "required": ["Comfort with tables/CSV", "Willingness to compute KPIs by hand when asked"],
            "recommended": ["DATA_VIZ_BI visual literacy (complementary, not a substitute)"],
        })
        _dump(base / "learning_objectives.json", {
            "course_id": course_id,
            "objectives": [
                "Declare schemas and ingest with row_count + source hash",
                "Write SQL SELECT with honest WHERE filters",
                "Normalize aliases and drop null/negative measures",
                "Compute avg/p95 KPIs without fabricated lift",
                "Author chart contracts with labeled axes and alt_text",
                "Join tables with orphan reporting",
                "Redact PII in ETL before warehouse load",
                "Debug pipeline stages with named error codes",
                "Enforce freshness SLAs without stale-live claims",
                "Close a dashboard capstone with no_key_leak",
            ],
        })
        _dump(base / "readings.json", {
            "course_id": course_id,
            "items": [
                {"week": 1, "title": "Pier Ledger schema card (fixture)", "reuse_class": "ORIGINAL"},
                {"week": 2, "title": "SQL SELECT predicate discipline (fixture)", "reuse_class": "ORIGINAL"},
                {"week": 5, "title": "Chart a11y alt-text checklist (fixture)", "reuse_class": "ORIGINAL"},
                {"week": 7, "title": "ETL PII redaction notes (fixture)", "reuse_class": "ORIGINAL"},
            ],
        })
        _dump(base / "a11y_checklist.json", {
            "course_id": course_id,
            "captions": True,
            "plain_language": True,
            "alt_text_required": True,
            "color_only_signals_forbidden": True,
            "large_print_available": True,
            "keyboard_or_text_path": True,
        })
        _dump(base / "skill_graph.json", {
            "schema": "waike.course_skill_graph.v1",
            "course_id": course_id,
            "nodes": [{"id": f"DATA_DASHBOARDS.w{w:02d}", "week": w} for w in range(1, 11)],
            "edges": [{"from": f"DATA_DASHBOARDS.w{w:02d}", "to": f"DATA_DASHBOARDS.w{w+1:02d}", "relation": "prerequisite"} for w in range(1, 10)],
        })
        _dump(base / "misconceptions.json", {
            "course_id": course_id,
            "items": [
                {"id": "M1", "misconception": "Dashboards can invent columns", "remediation": "Schema first; invented_columns fail"},
                {"id": "M2", "misconception": "SELECT * is enough for busy-bay tickets", "remediation": "Add WHERE + filter_count"},
                {"id": "M3", "misconception": "Green tiles prove KPI math", "remediation": "Show avg/p95 fields"},
                {"id": "M4", "misconception": "Learner tutors may load answer keys", "remediation": "Permission denied; Socratic only"},
            ],
        })
        _dump(base / "remediation.json", {
            "course_id": course_id,
            "loops": [
                {"on": "M1", "practice_lab": "lab_schema_ingest", "reassess": "quiz w01"},
                {"on": "M2", "practice_lab": "lab_sql_select", "reassess": "quiz w02"},
                {"on": "M3", "practice_lab": "lab_kpi_calc", "reassess": "quiz w04"},
                {"on": "M4", "practice_lab": "lab_dashboard_capstone", "reassess": "quiz w10"},
            ],
        })
        _dump(base / "gunnchai_contract.json", {
            "schema": "waike.course_gunnchai_contract.v1",
            "course_id": course_id,
            "discovery": "filesystem_scan curriculum/digital_rc/DATA_DASHBOARDS",
            "learner_modes_may_read_instructor_keys": False,
            "socratic_default": True,
            "educator_hitl_required": True,
            "tools": ["ingest", "transform", "calc", "chart", "debug"],
            "transfer_checks": ["new pier CSV without stem clone"],
        })
        _write(base / "instructor" / "accessibility_and_udl_guide.md",
               "# Accessibility / UDL — DATA_DASHBOARDS\n\n"
               "Text-first journals, chart alt text, large-print packets, no color-only signals.\n"
               "Fabricated disability quotes forbidden.\n")
        _write(base / "instructor" / "misconceptions_remediation.md",
               "# Misconceptions + remediation — DATA_DASHBOARDS\n\n"
               "See misconceptions.json and remediation.json. Reassess after practice lab.\n")
        _write(base / "guides" / "learner_ai_policy.md",
               "# Learner AI policy — DATA_DASHBOARDS\n\n"
               "Default AI_DISCLOSED. Weeks 4 and 9 are NO_AI authorship.\n"
               "Never request instructor keys in learner modes.\n")

    if course_id == "COMM_PD_ETHICS":
        _dump(base / "prerequisites.json", {
            "course_id": course_id,
            "required": ["Digital literacy for ticket journals", "Willingness to recuse on conflict"],
            "recommended": ["GENERAL_IT desk culture exposure"],
        })
        _dump(base / "learning_objectives.json", {
            "course_id": course_id,
            "objectives": [
                "Author consent disclosures with audience/purpose/retention/opt-out",
                "Disclose and recuse on scoring conflicts",
                "Write professional tickets without demeaning labels",
                "Separate observation from inference on the ethics ladder",
                "Cite PUBLIC_REFERENCE_ONLY sources without dumps",
                "Give evidence-based feedback without identity attacks",
                "Publish redacted minutes with owners and due dates",
                "Disclose AI modes without instructor key access in learner paths",
                "Ship accessible professional communication (captions/alt/large-print)",
                "Close a PD capstone with no_key_leak and a11y_ok",
            ],
        })
        _dump(base / "readings.json", {
            "course_id": course_id,
            "items": [
                {"week": 1, "title": "Harbor Desk consent card (fixture)", "reuse_class": "ORIGINAL"},
                {"week": 2, "title": "ISC2 ethics theme names", "reuse_class": "PUBLIC_REFERENCE_ONLY"},
                {"week": 5, "title": "CompTIA professionalism domain labels", "reuse_class": "PUBLIC_REFERENCE_ONLY"},
                {"week": 9, "title": "Plain-language a11y checklist (fixture)", "reuse_class": "ORIGINAL"},
            ],
        })
        _dump(base / "a11y_checklist.json", {
            "course_id": course_id,
            "captions": True,
            "plain_language": True,
            "alt_text_required": True,
            "color_only_signals_forbidden": True,
            "large_print_available": True,
            "keyboard_or_text_path": True,
        })
        _dump(base / "skill_graph.json", {
            "schema": "waike.course_skill_graph.v1",
            "course_id": course_id,
            "nodes": [{"id": f"COMM_PD_ETHICS.w{w:02d}", "week": w} for w in range(1, 11)],
            "edges": [{"from": f"COMM_PD_ETHICS.w{w:02d}", "to": f"COMM_PD_ETHICS.w{w+1:02d}", "relation": "prerequisite"} for w in range(1, 10)],
        })
        _dump(base / "misconceptions.json", {
            "course_id": course_id,
            "items": [
                {"id": "M1", "misconception": "Consent can say audience=everyone", "remediation": "Name concrete audiences"},
                {"id": "M2", "misconception": "Mentoring+scoring is fine if friendly", "remediation": "Disclose and recuse"},
                {"id": "M3", "misconception": "Inference is an observation", "remediation": "Rewrite ladder rungs"},
                {"id": "M4", "misconception": "Learner tutors may load answer keys", "remediation": "Permission denied; Socratic only"},
            ],
        })
        _dump(base / "remediation.json", {
            "course_id": course_id,
            "loops": [
                {"on": "M1", "practice_lab": "lab_consent_disclosure", "reassess": "quiz w01"},
                {"on": "M2", "practice_lab": "lab_conflict_interest", "reassess": "quiz w02"},
                {"on": "M3", "practice_lab": "lab_ethics_ladder", "reassess": "quiz w04"},
                {"on": "M4", "practice_lab": "lab_ai_disclosure_modes", "reassess": "quiz w08"},
            ],
        })
        _dump(base / "gunnchai_contract.json", {
            "schema": "waike.course_gunnchai_contract.v1",
            "course_id": course_id,
            "discovery": "filesystem_scan curriculum/digital_rc/COMM_PD_ETHICS",
            "learner_modes_may_read_instructor_keys": False,
            "socratic_default": True,
            "educator_hitl_required": True,
            "tools": ["curriculum_lookup", "ladder_prompt", "misconception_hint"],
            "transfer_checks": ["new desk scenario without stem clone"],
        })
        _write(base / "instructor" / "accessibility_and_udl_guide.md",
               "# Accessibility / UDL — COMM_PD_ETHICS\n\n"
               "Text-first journals, captions, alt text, large-print packets, no color-only signals.\n"
               "Fabricated disability quotes forbidden.\n")
        _write(base / "instructor" / "misconceptions_remediation.md",
               "# Misconceptions + remediation — COMM_PD_ETHICS\n\n"
               "See misconceptions.json and remediation.json. Reassess after practice lab.\n")
        _write(base / "guides" / "learner_ai_policy.md",
               "# Learner AI policy — COMM_PD_ETHICS\n\n"
               "Default AI_DISCLOSED. Weeks 4 and 9 are NO_AI authorship.\n"
               "Never request instructor keys in learner modes.\n")


    package = {
        "schema": "waike.course_package.v1",
        "course_id": course_id,
        "title": c["title"],
        "track_ids": c["track_ids"],
        "academy_id": c["academy_id"],
        "kinesthetic_hook": c["kinesthetic_hook"],
        "lesson_excerpt": c["weeks"][0]["lesson"][:400],
        "worked_example": c["weeks"][0]["worked_example"],
        "assignment": c["weeks"][0]["assignment"],
        "lab_hint": c["weeks"][0]["lab_id"],
        "syllabus": {"path": "syllabus.md", "weeks": len(c["weeks"])},
        "weeks": [
            {
                "week": w["week"],
                "title": w["title"],
                "lesson": {
                    "lesson_id": f"{course_id}-w{w['week']:02d}",
                    "title": w["title"],
                    "body_md": w["lesson"],
                    "worked_example": w["worked_example"],
                },
                "lab_id": w["lab_id"],
            }
            for w in c["weeks"]
        ],
        "assignments": [f"a{w['week']:02d}.md" for w in c["weeks"]],
        "labs": labs,
        "quizzes": [f"q{w['week']:02d}.json" for w in c["weeks"]],
        "assessments": {
            "mid_course_items": len(extras["mid"]),
            "final_items": len(extras["final"]),
            "practicals": 1,
            "projects": 1,
        },
        "rubrics": [r["rubric_id"] for r in rubrics],
        "answer_keys_ref": "instructor/answer_keys.json",
        "student_materials_ref": "student/STUDENT_PACKET.md",
        "instructor_materials_ref": "instructor/INSTRUCTOR_PACKET.md",
        "presentation_materials_ref": "presentation/",
        "offline_pack_ref": "offline_pack/pack.json",
        "portfolio": {"path": "portfolio/"},
        "career_mapping": c["career"],
        "alignment_ref": {
            "GENERAL_IT": "curriculum/alignment/general_it_alignment.json",
            "COMPUTER_NETWORKING": "curriculum/alignment/networking_alignment.json",
            "CYBERSECURITY": "curriculum/alignment/cybersecurity_alignment.json",
            "SOFTWARE_BUILDER": "curriculum/alignment/software_builder_alignment.json",
            "HARDWARE_ENGINEERING": "curriculum/alignment/hardware_engineering_alignment.json",
            "PM_AGILE_LSS": "curriculum/alignment/pm_agile_lss_alignment.json",
            "AI_ML_EDGE": "curriculum/alignment/ai_ml_edge_alignment.json",
            "DATA_VIZ_BI": "curriculum/alignment/data_viz_bi_alignment.json",
            "CLOUD_DEVOPS": "curriculum/alignment/cloud_devops_alignment.json",
            "WIRELESS_6G": "curriculum/alignment/wireless_6g_alignment.json",
            "ROBOTICS_CONTROL": "curriculum/alignment/robotics_control_alignment.json",
            "GAME_DEV_INTERACTIVE": "curriculum/alignment/game_dev_interactive_alignment.json",
            "COMM_PD_ETHICS": "curriculum/alignment/comm_pd_ethics_alignment.json",
            "DATA_DASHBOARDS": "curriculum/alignment/data_dashboards_alignment.json",
        }[course_id],
        "ai_use_policy": c.get("ai_use_policy"),
        "provenance": {
            "original_waike": True,
            "reuse_class_note": "See sources/benchmark_registry.json",
            "instructor_keys_not_in_learner_ui": True,
        },
        "counts": {
            "syllabus": 1,
            "weeks": len(c["weeks"]),
            "full_lessons": len(c["weeks"]),
            "assignments": len(c["weeks"]),
            "runnable_labs": len(labs),
            "quizzes": quiz_count,
            "quiz_items": quiz_items,
            "mid_course_items": len(extras["mid"]),
            "final_items": len(extras["final"]),
            "mid_course_items_original": sum(
                1
                for i in extras["mid"]
                if i["stem"] not in {q["stem"] for w in c["weeks"] for q in w["quiz"]}
                and not str(i["stem"]).startswith("Mid-course check:")
                and not exam_is_restatement(i["stem"], [q["stem"] for w in c["weeks"] for q in w["quiz"]])
            ),
            "final_items_original": sum(
                1
                for i in extras["final"]
                if i["stem"] not in {q["stem"] for w in c["weeks"] for q in w["quiz"]}
                and not str(i["stem"]).startswith("Capstone check:")
                and not exam_is_restatement(i["stem"], [q["stem"] for w in c["weeks"] for q in w["quiz"]])
            ),
            "practicals": 1,
            "projects": 1,
            "rubrics": len(rubrics),
            "answer_keys": 1 + quiz_count + 2,
            "student_materials": 1,
            "instructor_materials": 1 + len(c["weeks"]),
            "presentation_materials": len(c["weeks"]),
            "offline_pack": 1,
            "portfolio_artifacts": 1,
        },
    }
    if course_id not in COURSE_PREREQS:
        raise KeyError(f"missing authored prerequisites for {course_id}")
    _dump(base / "prerequisites.json", COURSE_PREREQS[course_id])

    _dump(base / "course.json", package)
    return package


def emit_all() -> dict[str, Any]:
    packages = {cid: emit_course(cid) for cid in COURSES}
    return packages


if __name__ == "__main__":
    emit_all()
    print("emitted", sorted(COURSES))
