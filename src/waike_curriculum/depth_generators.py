"""Generate full-depth WAIKE educational artifacts."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES, ROOT, load_catalog
from waike_curriculum.depth_content import (
    ASSIGNMENT_TASKS,
    DISCLAIMER,
    FLAGSHIP_COURSES,
    GROUP_PROJECTS,
    TECHNICAL_FLAGSHIP,
    WEEK_PLANS,
    generic_week_plan,
)

LESSON_FILES = [
    "lesson_plan.md",
    "teaching_notes.md",
    "slides_outline.md",
    "demo_plan.md",
    "guided_practice.md",
    "independent_practice.md",
    "7gc_case_connection.md",
    "discussion_prompts.md",
    "exit_ticket.md",
    "gunnchai_tutor_card.md",
]

ASSIGNMENT_SECTIONS = [
    "Purpose",
    "What you are learning",
    "Why this matters",
    "7GC case-study connection",
    "Theory connection",
    "Scenario",
    "Your task",
    "Step-by-step instructions",
    "Deliverables",
    "Acceptance criteria",
    "Stretch goals",
    "Tools you may use",
    "gunnchAI3k allowed help",
    "gunnchAI3k not allowed help",
    "Common mistakes",
    "Reflection questions",
    "Submission format",
    "Portfolio connection",
    "Rubric",
    "Revision instructions",
]

GROUP_PROJECT_FILES = [
    "README.md",
    "project_brief.md",
    "community_context.md",
    "technical_requirements.md",
    "research_question.md",
    "stakeholder_map.md",
    "team_charter.md",
    "roles_and_responsibilities.md",
    "milestone_plan.md",
    "weekly_checkpoints.md",
    "quality_plan.md",
    "ethics_privacy_review.md",
    "risk_register.md",
    "peer_review_form.md",
    "individual_contribution_log.md",
    "public_demo_guide.md",
    "final_report_template.md",
    "presentation_template.md",
    "portfolio_artifact_guide.md",
    "instructor_solution_guide.md",
]

CASE_DEPTH_FILES = [
    "human_story.md",
    "stakeholder_map.md",
    "technical_context.md",
    "constraints.md",
    "learner_tasks.md",
    "discussion_prompts.md",
    "instructor_guidance.md",
    "extension_challenges.md",
    "local_validation_needed.md",
]


def write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n", encoding="utf-8")


def week_plan(course_id: str, course_title: str, week: int) -> dict[str, str]:
    if course_id in WEEK_PLANS and week <= len(WEEK_PLANS[course_id]):
        return WEEK_PLANS[course_id][week - 1]
    return generic_week_plan(course_title, week)


def lesson_plan_md(course: dict[str, Any], week: int, wp: dict[str, str]) -> str:
    title = course["course_title"]
    return f"""# Week {week} lesson plan: {wp['title']}

## Plain-English purpose
Learners understand **{wp['theory']}** and connect it to a real 7GC scenario before building evidence.

## Theory topics
- {wp['theory']}
- Vocabulary introduced in teaching_notes.md

## Learner-friendly analogy
Think of this week like learning a craft: watch, try with help, try alone, then teach back one step.

## Learning outcomes
- Explain the core idea in plain English (mastery level 2–3)
- Apply the idea to case `{wp['case']}` (level 3)
- Produce weekly evidence artifact (level 4–5)

## Instructor warm-up
Ask: "Where have you seen this problem in your community?" Record answers without collecting PII.

## Mini lecture outline (20–30 min)
1. Why this matters for jobs and community
2. Concept introduction with diagram
3. Live demo or walkthrough (see demo_plan.md)
4. Connect to 7GC case-study thread

## Guided practice
See `guided_practice.md` — instructor circulates, uses Socratic questions only.

## Independent practice
See `independent_practice.md` — learners attempt assignment steps without step-by-step hand-holding.

## 7GC case-study connection
Site/case: `{wp['case']}`. {DISCLAIMER}

## Check for understanding
Exit ticket in exit_ticket.md; review 3 learner responses for misconception patterns.

## Homework / continuation
Complete assignment_{week:02d}.md in assignment_bodies.

## Evidence learners produce
Reflection, diagram, or checklist as specified in assignment acceptance criteria.

## Support options
Peer pairs, office hours, gunnchAI3k hints (not full solutions).

## Accessibility / UDL
Offer text + visual paths; caption demos; allow extra time for assignments.

## Common misconceptions
Listed in teaching_notes.md — address before grading.

## Instructor notes
Calibrate rubric with master_rubric.yaml; emphasize revision over penalty.
"""


def teaching_notes_md(wp: dict[str, str]) -> str:
    return f"""# Teaching notes — {wp['title']}

## Key points
- Connect theory to community impact before tools.
- Use {wp['case']} as narrative hook — do not claim field validation.

## Demonstration tips
- Screen share with large fonts; pause for questions.
- Show both success path and one failure path.

## Common misconceptions
- Learners confuse memorizing steps with understanding outcomes.
- Learners may over-trust AI-generated answers — reinforce integrity boundaries.

## Facilitation moves
- Think-pair-share after demo.
- Cold-call explanations in plain English (supportive tone).
"""


def assignment_body(course: dict[str, Any], week: int, wp: dict[str, str]) -> str:
    cid = course["course_id"]
    tasks = ASSIGNMENT_TASKS.get(cid, [f"Apply week {week} concepts to 7GC case study."] * 8)
    task = tasks[week - 1] if week <= len(tasks) else tasks[-1]
    sections = []
    sections.append(f"# Assignment {week:02d}: {wp['title']}\n")
    for name in ASSIGNMENT_SECTIONS:
        if name == "Purpose":
            body = f"Build applied understanding of **{wp['theory']}** for portfolio evidence."
        elif name == "What you are learning":
            body = wp["theory"]
        elif name == "Why this matters":
            body = "Employers and communities need people who can explain and apply technology, not only pass quizzes."
        elif name == "7GC case-study connection":
            body = f"Case thread: `{wp['case']}`. {DISCLAIMER}"
        elif name == "Theory connection":
            body = f"This assignment practices: {wp['theory']}."
        elif name == "Scenario":
            body = "You are a WAIKE learner supporting a 7GC campus partner (fictional/synthetic fixture)."
        elif name == "Your task":
            body = task
        elif name == "Step-by-step instructions":
            body = (
                "1. Read the case brief in `case_studies/7gc/` (15 min).\n"
                "2. Complete guided lab if listed for this week (30–45 min).\n"
                "3. Execute your task and capture evidence (screenshots/diagrams/logs).\n"
                "4. Write a 150-word reflection linking theory to the case.\n"
                "5. Self-check against acceptance criteria below.\n"
                "6. Submit via course folder + portfolio index entry."
            )
        elif name == "Deliverables":
            body = "- Primary artifact (diagram, doc, code, or report)\n- Reflection (150+ words)\n- Reproducibility note (how to verify your work)"
        elif name == "Acceptance criteria":
            body = (
                "- All required sections present\n"
                "- Plain-English explanation included\n"
                "- 7GC connection explicit\n"
                "- No PII in submission\n"
                "- Rubric category ≥ 2 on technical execution and documentation"
            )
        elif name == "Stretch goals":
            body = "Present to peer; open GitHub issue in linked gunnchOS3k repo (documentation only)."
        elif name == "Tools you may use":
            body = "Free tools: browser, text editor, Git, Python/Node as per course; see lab README for alternatives."
        elif name == "gunnchAI3k allowed help":
            body = "Hints, practice questions, debugging guidance, draft structure feedback."
        elif name == "gunnchAI3k not allowed help":
            body = "Submitting AI-written final answers without attribution; fabricated citations; completing graded work wholesale."
        elif name == "Common mistakes":
            body = "Vague reflections; missing evidence files; claiming field validation without proof."
        elif name == "Reflection questions":
            body = "What surprised you? What would you validate with a community partner?"
        elif name == "Submission format":
            body = "Folder or PDF + markdown in portfolio; name files `assignment_XX_<lastname>/`."
        elif name == "Portfolio connection":
            body = "Tag skill in portfolio_evidence_index after course completion."
        elif name == "Rubric":
            body = "Use `rubrics/master_rubric.yaml` categories: conceptual, technical, case application, documentation."
        elif name == "Revision instructions":
            body = "Submit change log with revisions; highest quality evidence may replace earlier draft."
        else:
            body = "See course assessment plan."
        sections.append(f"## {name}\n\n{body}\n")
    return "\n".join(sections)


def lab_package(course: dict[str, Any], week: int, wp: dict[str, str]) -> None:
    cid = course["course_id"]
    base = ROOT / "labs" / "by_course" / cid / f"week_{week:02d}_lab"
    write(base / "README.md", f"# Lab week {week} — {wp['title']}\n\n{cid} guided lab.\n")
    write(
        base / "lab_instructions.md",
        f"""# Lab instructions

## Required tools
- Laptop with browser and text editor (see INSTALL_NOTES if using optional cloud tools)

## Setup
1. Clone or open course materials.
2. Read safety/privacy note: **no real student PII** in logs.

## Steps
1. Follow demo_plan from lesson week_{week:02d}.
2. Execute practice commands or worksheet in guided_practice.md.
3. Record outputs in `expected_outputs/README.md` descriptions.
4. Compare to acceptance criteria in assignment_{week:02d}.md.

## What output means
Shows guided practice competence — **not** production deployment proof.

## What output does not prove
Field validation, certification, or carrier-grade performance.

## Extension
Optional: link issue in related gunnchOS3k repo with `[WAIKE lab]` prefix.

## Troubleshooting
See troubleshooting.md — check paths, permissions, offline fallback worksheet.
""",
    )
    write(base / "troubleshooting.md", "# Troubleshooting\n\n- Re-read step numbers\n- Ask peer then instructor\n- gunnchAI3k: debugging hints only\n")
    write(base / "rubric.md", "# Lab rubric\n\nMaster rubric + technical_execution focus.\n")
    write(base / "solution_notes_for_instructors.md", f"# Instructor solutions — week {week}\n\nAccept multiple valid approaches; grade evidence quality.\n")
    write(base / "starter_files/README.md", "# Starter files\n\nAdd worksheets or templates as course evolves.\n")
    write(base / "expected_outputs/README.md", "# Expected outputs\n\nDescribe screenshots or transcripts learners should capture.\n")


def tutor_card_md(topic: str, week: int) -> str:
    return f"""# gunnchAI3k tutor card — week {week}

topic: {topic}
learner_level: developing
plain_english_explanation: Ask learner to explain the idea as if teaching a family member.
diagnostic_questions:
  - What problem are we solving?
  - What would break if we skipped this step?
socratic_hint_1: What is the smallest test you could run?
socratic_hint_2: What evidence would convince a skeptical peer?
socratic_hint_3: How does the 7GC case change your design?
allowed_support: hints, practice, debugging, draft review
not_allowed_support: full graded solution, fabricated sources
practice_prompt: Give me a practice question at my level (not the answer).
debugging_help: Help me interpret my error message line by line.
reflection_prompt: What did you learn that a textbook would miss?
academic_integrity_boundary: Learner must author final submission and cite AI help.
"""


def deepen_lessons(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    for week in range(1, 9):
        wp = week_plan(cid, course["course_title"], week)
        base = ROOT / "lessons" / "by_course" / cid / f"week_{week:02d}"
        write(base / "lesson_plan.md", lesson_plan_md(course, week, wp))
        write(base / "teaching_notes.md", teaching_notes_md(wp))
        write(base / "slides_outline.md", f"# Slides outline week {week}\n\n1. Title\n2. Why it matters\n3. Concept\n4. Demo\n5. Practice\n6. 7GC case\n7. Assignment\n")
        write(base / "demo_plan.md", f"# Demo plan week {week}\n\nLive walkthrough of {wp['theory']} with one failure example.\n")
        write(base / "guided_practice.md", f"# Guided practice\n\nInstructor-led steps mirroring assignment_{week:02d} sections 1–3.\n")
        write(base / "independent_practice.md", f"# Independent practice\n\nLearners complete assignment steps 4–6 solo.\n")
        write(base / "7gc_case_connection.md", f"# 7GC connection\n\nCase: {wp['case']}\n\n{DISCLAIMER}\n")
        write(base / "discussion_prompts.md", f"# Discussion\n\n- How would this play out at the campus?\n- What ethical guardrails matter?\n")
        write(base / "exit_ticket.md", f"# Exit ticket\n\nIn one sentence: what is the key idea from {wp['title']}?\n")
        write(base / "gunnchai_tutor_card.md", tutor_card_md(wp["title"], week))


def deepen_assignments(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    for week in range(1, 9):
        wp = week_plan(cid, course["course_title"], week)
        write(
            ROOT / "assignment_bodies" / "by_course" / cid / f"assignment_{week:02d}.md",
            assignment_body(course, week, wp),
        )
        write(
            ROOT / "instructor_solution_guides" / "by_course" / cid / f"assignment_{week:02d}_solution_guide.md",
            f"# Solution guide assignment {week:02d}\n\n## Exemplar criteria\n\nMultiple valid solutions.\n\n## Common partial credit\n\nMissing 7GC link — redirect to case brief.\n\n## Not allowed\n\nPosting full copy-paste answers publicly.\n",
        )


def deepen_labs(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    lab_weeks = range(1, 9) if cid in TECHNICAL_FLAGSHIP or cid == "digital_confidence" else range(1, 5)
    for week in lab_weeks:
        wp = week_plan(cid, course["course_title"], week)
        lab_package(course, week, wp)


def deepen_group_project(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    gp = GROUP_PROJECTS.get(cid, {
        "title": f"{course['course_title']} capstone",
        "site": course.get("7gc_sites", ["gary"])[0],
        "community": "Community need — requires local validation.",
        "technical": "Deliver report + demo + reproducibility checklist.",
        "research": "What evidence would mature this from stub to pilot?",
    })
    base = ROOT / "group_projects" / "by_course" / cid
    for fname in GROUP_PROJECT_FILES:
        if fname == "project_brief.md":
            body = f"# {gp['title']}\n\n## Community context\n{gp['community']}\n\n## Technical\n{gp['technical']}\n\n## Research\n{gp['research']}\n\n{DISCLAIMER}\n"
        elif fname == "team_charter.md":
            body = "# Team charter\n\nRoles, norms, meeting schedule, conflict path.\n"
        elif fname == "peer_review_form.md":
            body = "# Peer review\n\nRate contribution 1–4 with evidence comments.\n"
        elif fname == "ethics_privacy_review.md":
            body = "# Ethics review\n\nNo PII; consent for demos; crisis privacy awareness.\n"
        else:
            body = f"# {fname.replace('_', ' ').replace('.md', '').title()}\n\nSee project_brief.md.\n"
        write(base / fname, body)
    write(
        ROOT / "instructor_solution_guides" / "by_course" / cid / "group_project_solution_guide.md",
        "# Group project solution guide\n\nExemplar structure, not single answer.\n",
    )


def deepen_case_studies() -> None:
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        for case in cases:
            base = ROOT / "case_studies" / "7gc" / site / case["case_id"]
            for fname in CASE_DEPTH_FILES:
                if (base / fname).exists() and (base / fname).read_text(encoding="utf-8").count("\n") > 8:
                    continue
                write(
                    base / fname,
                    f"# {fname.replace('_', ' ').title()} — {case['title']}\n\n"
                    f"Site: {site}\n\n{DISCLAIMER}\n\n"
                    "Community partner review needed for deployment claims.\n",
                )
            write(
                base / "local_validation_needed.md",
                "# Local validation needed\n\n- Partner interview\n- Pilot consent\n- Not field validated in repo\n",
            )


def deepen_industry(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    title = course["course_title"]
    base = ROOT / "industry_alignment" / "by_course" / cid
    write(base / "industry_skill_map.md", f"# Skills — {title}\n\nMapped to NICE/SFIA-style verbs — **not accredited**.\n")
    write(base / "job_role_map.md", f"# Job roles\n\nEntry-level roles this course supports (help desk, junior analyst, apprentice).\n")
    write(base / "certification_alignment.md", "# Cert alignment\n\nInformed by CompTIA/Cisco paths — not endorsed.\n")
    write(base / "toolchain_alignment.md", "# Tools\n\nFree-first toolchain; paid alternatives noted with fallbacks.\n")
    write(base / "employer_evidence.md", "# Employer evidence\n\nPortfolio artifacts demonstrate skills — not professional readiness alone.\n")
    write(base / "interview_readiness.md", "# Interview talk track\n\nSTAR stories from group project.\n")
    write(base / "portfolio_language.md", "# Portfolio language\n\nAction verbs + metrics from assignments.\n")


def deepen_assessment(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    base = ROOT / "assessment" / "by_course" / cid
    write(
        base / "mastery_evidence_map.md",
        f"""# Mastery evidence map — {cid}

| Outcome | Assignment | Lab | Group project | Portfolio | Rubric |
|---------|------------|-----|---------------|-----------|--------|
| Explain | assignment_01 | week_01_lab | charter | reflection | conceptual |
| Apply | assignment_04 | week_04_lab | build | demo | technical |
| Team | assignment_05 | — | milestones | peer review | teamwork |
| Ethics | assignment_07 | — | ethics review | report | ethical_reasoning |
""",
    )
    write(base / "continuous_improvement_plan.md", "# Continuous improvement\n\nCollect feedback; calibrate rubrics; update 7GC cases annually.\n")
    write(base / "assessment_plan.md", "# Assessment plan\n\nNot exam-heavy; see curriculum/assessment_model.yaml.\n")
    write(base / "revision_policy.md", "# Revision\n\nAllowed with change log.\n")


def deepen_workbooks(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    base = ROOT / "student_workbooks" / "by_course" / cid
    write(base / "workbook.md", f"# Student workbook — {course['course_title']}\n\nTrack weekly evidence here.\n")
    write(base / "weekly_checklists.md", "# Weekly checklists\n\n- [ ] Lesson\n- [ ] Lab\n- [ ] Assignment\n- [ ] Reflection\n")
    write(base / "reflection_journal.md", "# Reflection journal\n\nPrompts each week.\n")
    write(base / "portfolio_builder.md", "# Portfolio builder\n\nArtifact list for capstone.\n")


def case_study_applications(course: dict[str, Any]) -> None:
    cid = course["course_id"]
    base = ROOT / "case_study_applications" / "by_course" / cid
    write(base / "7gc_case_sequence.md", f"# 7GC sequence\n\nSites: {', '.join(course.get('7gc_sites', []))}\n")
    for site in ["gary", "ghana", "guyana", "gaza", "geelong", "graham_land", "germany"]:
        write(base / f"{site}_case_application.md", f"# {site} application\n\nLink flagship cases to weekly assignments.\n{DISCLAIMER}\n")


def deep_student_packet(course: dict[str, Any]) -> str:
    cid = course["course_id"]
    return f"""# Student packet — {course['course_title']}

## Welcome
You will build real skills through practice, teamwork, and portfolio evidence — not one high-stakes exam.

## Course purpose
Master: explain → apply → document → present → revise.

## What you will build
- 8 weekly artifacts
- Guided labs (see `labs/by_course/{cid}/`)
- Group capstone (see `group_projects/by_course/{cid}/`)
- Portfolio entry in evidence index

## Weekly roadmap
Weeks 1–8 in `lessons/by_course/{cid}/`

## Assignments
`assignment_bodies/by_course/{cid}/assignment_01.md` through `assignment_08.md`

## Group project
`group_projects/by_course/{cid}/project_brief.md`

## Team roles
Project Lead, Technical Lead, Research Lead, Documentation Lead, Quality, Presentation, Community Impact

## How grading works
Labs 25%, group 25%, portfolio 20%, docs 10%, presentation 10%, reflection 5%, quizzes ≤5%

## Revision policy
Revise with change log; mastery goal.

## Portfolio checklist
See `student_workbooks/by_course/{cid}/portfolio_builder.md`

## gunnchAI3k ethics
Hints yes; full solutions no.

## Help
Instructor, peers, office hours.

## Final demo
Week 8 showcase — public-friendly format in `public_demo_guide.md`
"""


def deep_instructor_packet(course: dict[str, Any]) -> str:
    cid = course["course_id"]
    return f"""# Instructor packet — {course['course_title']}

## Overview
Teach from `lessons/by_course/{cid}/week_XX/lesson_plan.md`.

## Weekly plan
8 weeks; each folder has teaching_notes, demo_plan, tutor card.

## Labs
Facilitate `labs/by_course/{cid}/`; use solution_notes_for_instructors.md.

## Group project
Manage milestones in `group_projects/by_course/{cid}/milestone_plan.md`.

## Grading
Use rubrics/master_rubric.yaml; team + individual scores.

## gunnchAI3k policy
Tutor cards per week; no graded wholesale generation.

## Accessibility
UDL options in each lesson_plan.md.

## Showcase
See public_demo_guide.md
"""


def deepen_course(course: dict[str, Any]) -> None:
    deepen_lessons(course)
    deepen_assignments(course)
    deepen_labs(course)
    deepen_group_project(course)
    deepen_industry(course)
    deepen_assessment(course)
    deepen_workbooks(course)
    case_study_applications(course)
    write(ROOT / "results" / "deep_student_packets" / f"{course['course_id']}_student_packet.md", deep_student_packet(course))
    write(ROOT / "results" / "deep_instructor_packets" / f"{course['course_id']}_instructor_packet.md", deep_instructor_packet(course))
    write(
        ROOT / "results" / "deep_course_packets" / f"{course['course_id']}_deep_course_packet.md",
        f"# Deep course packet — {course['course_title']}\n\nLessons, labs, assignments, group project, industry alignment generated.\n",
    )


def deepen_all() -> None:
    deepen_case_studies()
    for course in load_catalog().get("courses", []):
        deepen_course(course)


def portfolio_evidence_index() -> None:
    lines = ["# Portfolio evidence index\n", "| Course | Artifact | Skill | Job role | 7GC | Repo | Evidence path |", "|--------|----------|-------|----------|-----|------|---------------|"]
    for course in load_catalog().get("courses", []):
        cid = course["course_id"]
        lines.append(f"| {cid} | Capstone + week 8 | Applied + teamwork | Entry apprentice | {course.get('7gc_sites',[''])[0]} | gunnchOS3k | assignment_bodies/.../assignment_08.md |")
    write(ROOT / "results" / "portfolio_evidence_index" / "portfolio_evidence_index.md", "\n".join(lines))
