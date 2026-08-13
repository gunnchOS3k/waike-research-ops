"""Emit digital RC packages, learner/teacher ingest, and product catalog projection."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.labs import COURSE_LABS
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
            "mid_course_items_original": sum(
                1
                for i in extras["mid"]
                if i["stem"] not in {q["stem"] for w in c["weeks"] for q in w["quiz"]}
                and not str(i["stem"]).startswith("Mid-course check:")
            ),
            "final_items_original": sum(
                1
                for i in extras["final"]
                if i["stem"] not in {q["stem"] for w in c["weeks"] for q in w["quiz"]}
                and not str(i["stem"]).startswith("Capstone check:")
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
    _dump(base / "course.json", package)
    return package


def emit_all() -> dict[str, Any]:
    packages = {cid: emit_course(cid) for cid in COURSES}
    return packages


if __name__ == "__main__":
    emit_all()
    print("emitted", sorted(COURSES))
