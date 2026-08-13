"""Emit digital RC packages, learner/teacher ingest, and product catalog projection."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.labs import COURSE_LABS

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
    return [
        {
            "rubric_id": f"{course_id}-lab",
            "title": "Runnable lab",
            "criteria": [
                {"name": "validator_ok", "weight": 40, "desc": "Lab JSON ok=true with named checks"},
                {"name": "evidence", "weight": 30, "desc": "Inputs/outputs attached, no PII"},
                {"name": "explanation", "weight": 30, "desc": "Learner can say what a failing check means"},
            ],
        },
        {
            "rubric_id": f"{course_id}-assignment",
            "title": "Weekly assignment",
            "criteria": [
                {"name": "specific_numbers", "weight": 40, "desc": "Uses course numbers, not generic prose"},
                {"name": "scope", "weight": 30, "desc": "Does not claim certs or unauthorized testing"},
                {"name": "clarity", "weight": 30, "desc": "A stranger can continue the work"},
            ],
        },
        {
            "rubric_id": f"{course_id}-quiz",
            "title": "Knowledge check",
            "criteria": [
                {"name": "original", "weight": 50, "desc": "WAIKE stems, not vendor items"},
                {"name": "keyed", "weight": 50, "desc": "Instructor key exists and is not in learner UI"},
            ],
        },
        {
            "rubric_id": f"{course_id}-mid",
            "title": "Mid-course knowledge",
            "criteria": [{"name": "coverage_weeks_1_5", "weight": 100, "desc": "Items map to weeks 1–5"}],
        },
        {
            "rubric_id": f"{course_id}-final-knowledge",
            "title": "Final knowledge",
            "criteria": [{"name": "coverage_weeks_6_10", "weight": 100, "desc": "Items map to later weeks plus capstone"}],
        },
        {
            "rubric_id": f"{course_id}-practical",
            "title": "Final practical",
            "criteria": [
                {"name": "labs_green", "weight": 60, "desc": "Required labs ok"},
                {"name": "negative_fail", "weight": 20, "desc": "Mutated fixtures fail"},
                {"name": "writeup", "weight": 20, "desc": "Honest claim boundary"},
            ],
        },
        {
            "rubric_id": f"{course_id}-project",
            "title": "Group project",
            "criteria": [
                {"name": "design", "weight": 30, "desc": "Design exists before implementation"},
                {"name": "handoff", "weight": 40, "desc": "Recorder notes let a stranger continue"},
                {"name": "ethics", "weight": 30, "desc": "No PII, no unauthorized targets"},
            ],
        },
        {
            "rubric_id": f"{course_id}-portfolio",
            "title": "Portfolio",
            "criteria": [
                {"name": "artifacts", "weight": 70, "desc": "Required artifacts present"},
                {"name": "no_pii", "weight": 30, "desc": "No faces, secrets, or PANs"},
            ],
        },
    ]


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
        "10 weeks. Operator/support, packet-range, or Harbor SOC hours — not a 2-hour workshop pretending to be a course.",
        "",
        "## Weekly map",
    ]
    for w in c["weeks"]:
        syllabus.append(f"- Week {w['week']:02d}: {w['title']}")
    syllabus += [
        "",
        "## Assessments",
        "- 10 weekly quizzes (6 original items each)",
        "- Mid-course knowledge (20 items, weeks 1–5)",
        "- Final knowledge (24 items)",
        "- Final practical (runnable labs)",
        "- Group project / capstone",
        "",
        "## Claim boundary",
        "Original WAIKE materials. Domain alignment only. No certification granted. Instructor keys are not in the learner packet.",
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
        slides = [
            f"# Week {w['week']} presentation — {w['title']}",
            "",
            "## Slide 1 — Cold open",
            w["worked_example"],
            "",
            "## Slide 2 — Teaching beat",
            w["lesson"].split("\n\n")[0],
            "",
            "## Slide 3 — Numbers on the board",
            "Do the worked example live. Do not skip to the quiz.",
            "",
            "## Speaker notes",
            "If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.",
        ]
        _write(base / "presentation" / f"week_{w['week']:02d}.md", "\n".join(slides))
        _write(
            base / "instructor" / f"week_{w['week']:02d}_notes.md",
            f"# Instructor notes week {w['week']}\n\nPace: live worked example first.\n\nLab `{w['lab_id']}` must be executed, not narrated.\n\nDo not paste vendor exam items.\n",
        )

    for lab_id in labs:
        _write(
            base / "labs" / lab_id / "README.md",
            f"# {lab_id}\n\nRun from repo root:\n\n```\npython3 scripts/run_course_labs.py --lab {lab_id}\n```\n\nValidators compute. Print-PASS is rejected.\n",
        )

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
        f"# Group project — {c['title']}\n\n{c['weeks'][-1]['assignment']}\n\nDesign first. Recorder notes must let a stranger continue.\n",
    )

    rubrics = _rubrics(course_id)
    _dump(base / "rubrics" / "rubrics.json", rubrics)
    for r in rubrics:
        lines = [f"# {r['title']}", ""]
        for crit in r["criteria"]:
            lines.append(f"- **{crit['name']}** ({crit['weight']}%): {crit['desc']}")
        _write(base / "rubrics" / f"{r['rubric_id']}.md", "\n".join(lines))

    _dump(base / "instructor" / "answer_keys.json", answer_keys)
    _write(
        base / "instructor" / "INSTRUCTOR_PACKET.md",
        f"# Instructor packet — {c['title']}\n\nKeys: `instructor/answer_keys.json` (never copy into learner ingest).\n\nRun labs via `scripts/run_course_labs.py`.\n\nAlignment: see `curriculum/alignment/`.\n",
    )
    _write(
        base / "student" / "STUDENT_PACKET.md",
        f"# Student packet — {c['title']}\n\n{c['kinesthetic_hook']}\n\nRead weekly lessons, submit assignments, run labs. You will not receive answer keys in this packet.\n",
    )
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
    _write(base / "portfolio" / "PORTFOLIO.md", f"# Portfolio — {c['title']}\n\nShip lab JSON, the capstone artifact, and a scope paragraph. No PII.\n")
    _dump(base / "career_mapping.json", c["career"])

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
        }[course_id],
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
    _dump(base / "course.json", package)
    return package


def emit_all() -> dict[str, Any]:
    packages = {cid: emit_course(cid) for cid in COURSES}
    return packages


if __name__ == "__main__":
    emit_all()
    print("emitted", sorted(COURSES))
