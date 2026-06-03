from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES, ROOT, load_assessment_model, load_catalog

ETHOS = (
    "WAIKE uses the 7GC campuses as case-study environments because technology education "
    "should not be abstract. Learners study real communities, real constraints, real risks, "
    "and real opportunities."
)
ASSESSMENT = load_assessment_model()
BREAKDOWN = ASSESSMENT.get("default_breakdown", {})


def write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n", encoding="utf-8")


def course_ethos(course_title: str) -> str:
    return f"{ETHOS}\n\nIn **{course_title}**, learners connect theory to 7GC case studies and portfolio artifacts.\n"


def syllabus_md(course: dict[str, Any]) -> str:
    cid = course["course_id"]
    title = course["course_title"]
    sites = ", ".join(course.get("7gc_sites", []))
    b = BREAKDOWN
    return f"""# {title}

## Purpose
Plain-English: build real understanding and portfolio-ready skill — not exam cramming.

## Who it is for
Beginners through advanced learners per track level `{course.get('level', 'all')}`.

## Prerequisites
See `learning_outcomes.yaml` — prior courses listed in catalog.

## Learning path
theory → case study → lab → group project → portfolio artifact

## 7GC connection
Case-study threads: {sites}. **Requires local validation** for deployment claims.

## Assessment (not exam-heavy)
| Component | Weight |
|-----------|--------|
| Applied labs | {int(b.get('applied_labs', 0.25)*100)}% |
| Group case-study project | {int(b.get('group_case_study_project', 0.25)*100)}% |
| Portfolio artifact | {int(b.get('individual_portfolio_artifact', 0.2)*100)}% |
| Documentation / reproducibility | {int(b.get('documentation_reproducibility', 0.1)*100)}% |
| Communication / presentation | {int(b.get('communication_presentation', 0.1)*100)}% |
| Reflection / peer review | {int(b.get('reflection_peer_review_revision', 0.05)*100)}% |
| Knowledge checks (max 10%) | {int(b.get('knowledge_checks_quizzes', 0.05)*100)}% |

## Revision policy
Revisions allowed with change log after instructor feedback.

## Repo alignment
See `knowledge_maps/course_repo_map.yaml` and catalog `repo_alignment` in generated packets.

## 7GC ethos
{course_ethos(title)}
"""


def learning_outcomes_yaml(course: dict[str, Any]) -> str:
    try:
        import yaml
        data = {
            "course_id": course["course_id"],
            "outcomes": [
                {"id": "explain", "level": 3, "text": "Explain core concepts for 7GC context."},
                {"id": "apply", "level": 4, "text": "Apply skills in labs and group project."},
                {"id": "portfolio", "level": 5, "text": "Deliver portfolio artifact with reproducibility."},
            ],
        }
        return yaml.dump(data, sort_keys=False)
    except ImportError:
        return json.dumps({"course_id": course["course_id"]}, indent=2)


def weekly_schedule_md(course: dict[str, Any]) -> str:
    return """# Weekly schedule (8-week)

| Week | Focus |
|------|--------|
| 1 | Why this matters + mental model |
| 2 | Core theory + guided lab |
| 3 | Case study + small artifact |
| 4 | Implementation checkpoint |
| 5 | Group project design review |
| 6 | Build and test |
| 7 | Documentation, ethics, reproducibility |
| 8 | Demo, portfolio, reflection, revision plan |
"""


def assignment_yaml(course_id: str, week: int, title: str) -> str:
    try:
        import yaml
        data = {
            "assignment_id": f"{course_id}_w{week:02d}",
            "assignment_title": title,
            "course_id": course_id,
            "week": week,
            "estimated_time_hours": 3,
            "difficulty_level": "developing",
            "deliverables": ["reflection", "diagram_or_code"],
            "rubric": "rubrics/master_rubric.yaml",
            "gunnchAI3k_allowed_help": ["hints", "practice", "debugging", "draft_review"],
            "gunnchAI3k_not_allowed_help": ["complete graded submission", "fabricated sources"],
            "revision_policy": "allowed_with_changelog",
            "portfolio_connection": True,
            "7gc_case_study_connection": "site from course map — synthetic teaching fixture",
        }
        return yaml.dump(data, sort_keys=False)
    except ImportError:
        return json.dumps({"assignment_id": f"{course_id}_w{week:02d}"}, indent=2)


def group_project_yaml(course: dict[str, Any]) -> str:
    site = course.get("7gc_sites", ["gary"])[0]
    try:
        import yaml
        data = {
            "project_title": f"{course['course_title']} — 7GC group project",
            "course_id": course["course_id"],
            "7gc_site": site,
            "community_problem": "Source-backed assumption — requires local validation",
            "technical_problem": "Defined in group_project_brief.md",
            "team_roles": [
                "Project Lead", "Technical Lead", "Research Lead", "Documentation Lead",
                "Quality Lead", "Presentation Lead", "Community Impact Lead",
            ],
            "peer_review": True,
            "portfolio_artifacts": ["report", "demo", "reproducibility_checklist"],
            "risk_ethics_privacy_review": True,
        }
        return yaml.dump(data, sort_keys=False)
    except ImportError:
        return "{}\n"


def case_study_files(site: str, case: dict[str, str]) -> dict[str, str]:
    cid = case["case_id"]
    title = case["title"]
    disclaimer = (
        "**Evidence note:** synthetic teaching fixture / source-backed assumption. "
        "**Requires local validation** — not field-validated deployment."
    )
    return {
        "README.md": f"# {title}\n\nSite: {site}\n\n{disclaimer}\n",
        "case_brief.md": f"# Case brief — {title}\n\n## Human story\nTeaching narrative for {site}.\n\n## Technical problem\nTBD with community partner review.\n\n{disclaimer}\n",
        "learner_context.md": "# Learner context\n",
        "instructor_context.md": "# Instructor context\n",
        "data_packet.md": "# Data packet\nSynthetic fixture only.\n",
        "ethical_considerations.md": "# Ethics\nPrivacy, consent, no PII in repos.\n",
        "assignment_variants.md": "# Assignment variants\n",
        "group_project_prompt.md": f"# Group project prompt — {title}\n",
        "rubric.md": "# Rubric\nSee rubrics/master_rubric.yaml\n",
        "reflection_questions.md": "# Reflection\nWhat changed for the community if this worked?\n",
        "solution_guidance_for_instructors.md": "# Instructor guidance\nNot a single correct answer.\n",
    }


def seed_course(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    base = ROOT / "syllabi" / cid
    files = {
        "README.md": f"# {course['course_title']}\n\nSee syllabus.md and generated results packets.\n",
        "syllabus.md": syllabus_md(course),
        "learning_outcomes.yaml": learning_outcomes_yaml(course),
        "weekly_schedule.md": weekly_schedule_md(course),
        "assignment_sequence.md": "# Assignment sequence\n\nWeeks 1–8 assignments in assignments/by_course/\n",
        "group_project_brief.md": f"# Group project\n\n7GC site focus from catalog.\n",
        "rubric.md": "# Rubric\n\n`rubrics/master_rubric.yaml`\n",
        "portfolio_artifact_requirements.md": "# Portfolio artifact\n\nGitHub repo, report, or demo with reproducibility checklist.\n",
        "instructor_notes.md": "# Instructor notes\n",
        "student_packet.md": "# Student packet\n\nSee results/student_packets after export.\n",
        "gunnchai_tutor_cards.md": "# gunnchAI3k tutor cards\n\nAllowed: hints, practice. Not allowed: complete graded work.\n",
        "7gc_case_study_map.md": f"# 7GC map\n\nSites: {', '.join(course.get('7gc_sites', []))}\n",
    }
    for name, body in files.items():
        write(base / name, body)

    abase = ROOT / "assignments" / "by_course" / cid
    for week, title in [
        (1, "Mental model reflection"),
        (2, "Guided lab artifact"),
        (3, "Case study analysis"),
        (4, "Implementation checkpoint"),
        (5, "Group charter draft"),
        (6, "Build log"),
        (7, "Reproducibility checklist"),
        (8, "Portfolio submission"),
    ]:
        write(abase / f"week_{week:02d}.yaml", assignment_yaml(cid, week, title))

    write(ROOT / "group_projects" / "by_course" / f"{cid}.yaml", group_project_yaml(course))
    write(ROOT / "gunnchai_tutor_cards" / "by_course" / f"{cid}.md", files["gunnchai_tutor_cards.md"])


def seed_case_studies() -> None:
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        for case in cases:
            base = ROOT / "case_studies" / "7gc" / site / case["case_id"]
            for fname, body in case_study_files(site, case).items():
                write(base / fname, body)


def generate_results_syllabus(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    src = ROOT / "syllabi" / cid / "syllabus.md"
    dst = ROOT / "results" / "syllabi" / f"{cid}_syllabus.md"
    if src.exists():
        write(dst, src.read_text(encoding="utf-8"))


def generate_results_packets(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    title = course["course_title"]
    inst = f"""# Instructor packet — {title}

## Overview
Facilitate theory → case study → lab → group project → portfolio.

## Grading
Not exam-heavy; see assessment_model.yaml.

## gunnchAI3k
Hints and practice only — not graded completion.

## Accessibility
See instructor/accessibility_and_udl_guide.md
"""
    stud = f"""# Student packet — {title}

## Welcome
You will build real artifacts, not cram for one exam.

## Grading
Labs 25%, group project 25%, portfolio 20%, docs 10%, presentation 10%, reflection 5%, quizzes max 5%.

## Help
Use gunnchAI3k ethically; revise work with change logs.

## Demo
Week 8 portfolio demo required.
"""
    write(ROOT / "results" / "instructor_packets" / f"{cid}_instructor_packet.md", inst)
    write(ROOT / "results" / "student_packets" / f"{cid}_student_packet.md", stud)
    assign_body = f"# Assignments — {title}\n\n"
    abase = ROOT / "assignments" / "by_course" / cid
    if abase.exists():
        for p in sorted(abase.glob("*.yaml")):
            assign_body += f"- {p.name}\n"
    write(ROOT / "results" / "assignment_packs" / f"{cid}_assignments.md", assign_body)
    write(ROOT / "results" / "group_project_packs" / f"{cid}_group_project.md", f"# Group project — {title}\n\nSee group_projects/by_course/{cid}.yaml\n")


def generate_all() -> None:
    catalog = load_catalog()
    for course in catalog.get("courses", []):
        seed_course(course)
        generate_results_syllabus(course)
        generate_results_packets(course)
    seed_case_studies()
    for site in FLAGSHIP_CASE_STUDIES:
        cases = FLAGSHIP_CASE_STUDIES[site]
        body = f"# Case studies — {site}\n\n" + "\n".join(f"- {c['title']} (`{c['case_id']}`)" for c in cases)
        write(ROOT / "results" / "case_study_packs" / f"{site}_case_studies.md", body)


def export_catalog() -> None:
    catalog = load_catalog()
    courses = catalog.get("courses", [])
    md = "# WAIKE Course Catalog\n\n"
    for c in courses:
        md += f"- **{c['course_id']}**: {c['course_title']}\n"
    write(ROOT / "results" / "catalog" / "course_catalog.md", md)
    write(ROOT / "results" / "catalog" / "course_catalog.json", json.dumps(catalog, indent=2))
    write(ROOT / "results" / "catalog" / "program_outcomes_matrix.md", "# Program outcomes\n\nSee curriculum/program_outcomes.yaml\n")
