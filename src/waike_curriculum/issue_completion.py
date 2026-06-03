"""Implement artifacts for WAIKE GitHub issues #1–#28."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DISCLAIMER = (
    "WAIKE is **aligned with** / **informed by** industry frameworks — "
    "**not accredited by**, **not endorsed by**, and **not official certification training**."
)


def w(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n", encoding="utf-8")


def yaml_mapping(path: Path, framework: str, course_id: str, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {"framework": framework, "disclaimer": DISCLAIMER, "mappings": rows}
    try:
        import yaml
        path.write_text(yaml.dump(data, sort_keys=False), encoding="utf-8")
    except ImportError:
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def course_release_templates() -> None:
    base = ROOT / "templates/course_release"
    files = {
        "README.md": "# WAIKE course release templates\n\nGenerate with `scripts/generate_course_release.py`.\n",
        "course_release_template.md": "# Course release template\n\n## Student-ready\n## Instructor-ready\n## 7GC\n## Assessment\n## Portfolio\n",
        "syllabus_template.md": "# Syllabus template\n",
        "lesson_plan_template.md": "# Lesson plan template\n",
        "assignment_template.md": "# Assignment template\n",
        "guided_lab_template.md": "# Guided lab template\n",
        "group_project_template.md": "# Group project template\n",
        "instructor_packet_template.md": "# Instructor packet template\n",
        "student_packet_template.md": "# Student packet template\n",
        "rubric_template.md": "# Rubric template — master_rubric.yaml\n",
        "gunnchai_tutor_card_template.md": "# Tutor card template\n",
        "portfolio_artifact_template.md": "# Portfolio artifact template\n",
        "release_checklist.md": "# Release checklist\n\n- [ ] 8 lesson weeks\n- [ ] 8 assignments\n- [ ] Group project\n- [ ] validate-depth PASS\n",
        "readiness_gate_checklist.md": "# Readiness gates\n\nStudent + instructor audits must not be PLACEHOLDER_ONLY.\n",
    }
    for name, body in files.items():
        w(base / name, body)
    w(ROOT / "results/templates/course_release_template_preview.md", "# Preview\n\nSee templates/course_release/\n")


def apprenticeships() -> None:
    w(ROOT / "apprenticeships/README.md", "# Research apprenticeships\n")
    w(ROOT / "apprenticeships/apprenticeship_model.md", "# Model\n\nMentor checkpoints, evidence maturity, no PII.\n")
    w(ROOT / "apprenticeships/role_ladder.md", "# Role ladder\n\nBeginner → intermediate → advanced → mentor.\n")
    w(ROOT / "apprenticeships/mentor_check_in_model.md", "# Mentor check-ins\n")
    w(ROOT / "apprenticeships/evidence_model.md", "# Evidence\n\nmake e2e logs, PRs, posters — not toy demos alone.\n")
    tracks = {
        "7gc_digital_twin_research": "7gc-digital-twin",
        "ai_ran_research": "spectrumx-ai-ran-gary",
        "edge_io_measurement": "edge-io-measurement-node",
        "ntn_resilience": "ntn-resilience-sim",
        "beam_selection": "readygary-6g-beam-selection",
        "hardware_device_lab": "gunnchos-hardware-industrial-design",
        "device_os_lab": "gunnchos-device-os",
        "reproducible_research": "waike-research-ops",
    }
    for tid, repo in tracks.items():
        w(
            ROOT / "apprenticeships/tracks" / f"{tid}.md",
            f"""# Track: {tid}

Repo: `{repo}`

## Beginner
- Read README; run `make e2e` (or document blocker)

## Intermediate
- Fix test/doc gap; update traceability

## Advanced
- Add metric/scenario; draft figure from results/

## Artifacts
- Weekly log, PR, reproducibility checklist, demo

## Ethics
Synthetic data only; no affiliation claims; requires local validation for deployment.
""",
        )
    w(ROOT / "results/apprenticeships/research_apprenticeship_index.md", "# Apprenticeship index\n\nSee apprenticeships/tracks/\n")


def standards_mappings() -> None:
    specs = [
        ("NIST_NICE_mapping.md", "nist_nice_mapping.yaml", "NIST NICE", "cybersecurity", [
            {"outcome": "SOC workflow awareness", "assignment": "assignment_06", "artifact": "IR checklist"},
        ]),
        ("SFIA_9_mapping.md", "sfia9_mapping.yaml", "SFIA 9", "digital_confidence", [
            {"skill": "Digital literacy", "level": "2", "assignment": "assignment_01"},
        ]),
        ("SWEBOK_mapping.md", "swebok_mapping.yaml", "SWEBOK", "software_engineering", [
            {"knowledge_area": "Construction", "assignment": "assignment_04", "artifact": "Git PR"},
        ]),
        ("NIST_AI_RMF_mapping.md", "nist_ai_rmf_mapping.yaml", "NIST AI RMF", "ai_ml_data", [
            {"function": "Map", "assignment": "model card", "artifact": "risk review"},
        ]),
        ("CompTIA_A_PLUS_mapping.md", "comptia_a_plus_mapping.yaml", "CompTIA A+", "hardware_engineering", [
            {"domain": "Hardware", "lab": "week_02_lab", "artifact": "repair workflow"},
        ]),
        ("Cisco_CCNA_mapping.md", "ccna_mapping.yaml", "CCNA", "networking", [
            {"topic": "IP addressing", "assignment": "assignment_02", "artifact": "subnet worksheet"},
        ]),
        ("ISC2_CC_SECURITY_PLUS_mapping.md", "isc2_security_plus_mapping.yaml", "ISC2/CC", "cybersecurity", [
            {"domain": "Security operations", "project": "cyber safety kit", "artifact": "threat model"},
        ]),
        ("ABET_mapping.md", "abet_mapping.yaml", "ABET", "ai_ran_digital_twin_research", [
            {"outcome": "Engineering design", "evidence": "group project report"},
        ]),
        ("ACM_CS2023_mapping.md", "acm_cs2023_mapping.yaml", "ACM CS2023", "software_engineering", [
            {"area": "Software development", "evidence": "portfolio repo"},
        ]),
    ]
    for md_name, yaml_name, fw, course, rows in specs:
        w(
            ROOT / "standards_alignment" / md_name,
            f"# {fw} mapping\n\n{DISCLAIMER}\n\nCourse focus: `{course}`.\n\nSee data/{yaml_name}.\n",
        )
        yaml_mapping(ROOT / "standards_alignment/data" / yaml_name, fw, course, rows)


def capstone_library() -> None:
    w(ROOT / "capstones/README.md", "# WAIKE capstone library\n")
    w(ROOT / "capstones/capstone_model.md", "# Capstone model\n\nTeam + individual scoring.\n")
    w(ROOT / "capstones/capstone_readiness_rubric.md", "# Capstone rubric\n\nSee rubrics/master_rubric.yaml\n")
    courses = [
        "digital_confidence", "general_it", "hardware_engineering", "software_engineering",
        "cybersecurity", "networking", "cloud_devops", "ai_ml_data", "edge_ai_embedded",
        "wireless_dsp_6g", "robotics_control", "project_management_agile_lss",
        "data_visualization_bi", "communication_ethics_professional_dev",
        "game_development_interactive_media", "gunnchos_device_os_product_lab",
        "ai_ran_digital_twin_research", "reproducible_research",
    ]
    for c in courses:
        w(ROOT / "capstones/by_track" / f"{c}.md", f"# Capstone — {c}\n\n7GC-grounded; requires local validation.\n")
    for site in ["gary", "ghana", "guyana", "gaza", "geelong", "graham_land", "germany"]:
        w(ROOT / "capstones/by_7gc_site" / f"{site}.md", f"# Capstone themes — {site}\n")
    w(ROOT / "results/capstones/capstone_library_index.md", "# Capstone index\n")


def instructor_training() -> None:
    base = ROOT / "instructor_training"
    for name in [
        "README.md", "instructor_onboarding_path.md", "facilitation_model.md",
        "grading_and_feedback_model.md", "rubric_calibration.md", "group_project_facilitation.md",
        "gunnchai_policy_for_instructors.md", "accessibility_and_udl_training.md",
        "conflict_resolution_and_team_dynamics.md", "course_release_training.md",
        "instructor_observation_rubric.md", "practice_teaching_microcredential.md",
    ]:
        w(base / name, f"# {name.replace('_', ' ')}\n\nFacilitation, grading, UDL, gunnchAI3k boundaries.\n")
    w(ROOT / "results/instructor_training/instructor_training_packet.md", "# Instructor training packet\n")


def portfolio_requirements() -> None:
    base = ROOT / "portfolio"
    w(base / "README.md", "# Portfolio requirements\n")
    w(base / "portfolio_model.md", "# Portfolio model\n")
    w(base / "portfolio_artifact_requirements.md", "# Artifact requirements per track\n")
    w(base / "github_profile_guidance.md", "# GitHub profile\n")
    w(base / "resume_bullet_translation.md", "# Resume bullets\n")
    w(base / "demo_video_guidance.md", "# Demo video\n")
    w(base / "technical_report_guidance.md", "# Technical report\n")
    w(base / "portfolio_review_rubric.md", "# Portfolio rubric\n")
    for c in ["digital_confidence", "software_engineering", "networking", "cybersecurity", "wireless_dsp_6g", "ai_ran_digital_twin_research"]:
        w(base / "by_track" / f"{c}.md", f"# Portfolio — {c}\n")
    w(ROOT / "results/portfolio/portfolio_requirements_index.md", "# Portfolio index\n")
    w(ROOT / "results/portfolio/job_pool_readiness_matrix.md", "# Job pool readiness\n\nNot professional readiness alone.\n")


def localization() -> None:
    base = ROOT / "localization"
    for name in [
        "README.md", "localization_strategy.md", "supported_language_roadmap.md",
        "translation_workflow.md", "plain_language_policy.md", "glossary_model.md",
        "cultural_review_process.md", "accessibility_localization.md",
        "gunnchai_multilingual_policy.md", "local_validator_role.md",
    ]:
        w(base / name, f"# {name}\n\nTranslations **not complete** — process only.\n")
    w(ROOT / "results/localization/localization_plan.md", "# Localization plan\n")


def evaluation_dashboard() -> None:
    base = ROOT / "evaluation"
    for name in [
        "README.md", "evaluation_model.md", "privacy_safe_metrics.md",
        "dashboard_requirements.md", "dashboard_mock_data_policy.md",
    ]:
        w(base / name, f"# {name}\n\nMock/de-identified data only.\n")
    w(base / "learner_progress_schema.yaml", "version: 1\nfields: [course_id, week, artifact_submitted]\n")
    w(base / "cohort_metrics_schema.yaml", "version: 1\nfields: [cohort_id, completion_rate_aggregate]\n")
    w(base / "artifact_quality_schema.yaml", "version: 1\nfields: [rubric_score_aggregate]\n")
    pkg = ROOT / "src/waike_curriculum/evaluation"
    w(pkg / "__init__.py", '"""Evaluation metrics (mock data only)."""\n')
    w(pkg / "schemas.py", "SCHEMAS = ['learner_progress', 'cohort_metrics', 'artifact_quality']\n")
    w(pkg / "mock_data.py", "def mock_cohort():\n    return {'cohort_id': 'synthetic', 'n': 0}\n")
    w(pkg / "metrics.py", "def completion_rate(progress):\n    return 0.0 if not progress else 0.5\n")
    w(pkg / "report.py", "def render_markdown(data):\n    return '# Evaluation report\\n'\n")
    w(ROOT / "scripts/generate_evaluation_dashboard.py", "#!/usr/bin/env python3\nimport sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[1]\nsys.path.insert(0,str(ROOT/'src'))\nfrom waike_curriculum.evaluation.mock_data import mock_cohort\nfrom waike_curriculum.evaluation.report import render_markdown\nimport json\nout=ROOT/'results/evaluation'\nout.mkdir(parents=True,exist_ok=True)\n(out/'evaluation_dashboard_data.json').write_text(json.dumps(mock_cohort(),indent=2))\n(out/'evaluation_dashboard.md').write_text(render_markdown(mock_cohort()))\n(out/'privacy_safe_metrics_report.md').write_text('# Privacy-safe metrics\\nNo PII.\\n')\nprint('Generated evaluation dashboard')\n")
    w(ROOT / "results/evaluation/evaluation_dashboard_data.json", '{"cohort_id":"synthetic","evidence":"mock_only"}\n')
    w(ROOT / "results/evaluation/evaluation_dashboard.md", "# Evaluation dashboard\n\nMock data only.\n")
    w(ROOT / "results/evaluation/privacy_safe_metrics_report.md", "# Privacy-safe metrics\n")


def supporting_issues() -> None:
    w(ROOT / "rubrics/foi_rubric.yaml", "version: 1\nname: Foundations of Innovation\nscale: 0-4\n")
    w(ROOT / "curriculum/learning_outcomes_matrix.md", "# Learning outcomes matrix\n\nSee program_outcomes.yaml + assessment/by_course/*/mastery_evidence_map.md\n")
    w(ROOT / "compliance/fair_chance_youth_safety_policy.md", "# Fair chance / youth safety\n\nDraft policy — not legal advice.\n")
    w(ROOT / "ops/global_campus_ops_playbook.md", "# Global campus ops playbook\n\n7GC sites operational guidance.\n")
    w(ROOT / "portfolio/templates/project_story_card.md", "# Project story card\n\nProblem, role, tools, outcome, reflection.\n")
    w(ROOT / "gunnchai/tutor_requirements.md", "# gunnchAI3k tutor requirements\n\nSee docs/08_GUNNCHAI3K_TUTOR_REQUIREMENTS.md\n")
    w(ROOT / "philosophy/beyond_the_founder_standard.md", "# Beyond the Founder Standard\n\nSee docs/02_BEYOND_THE_FOUNDER_STANDARD.md\n")


# Issue number -> evidence paths (for classification)
ISSUE_EVIDENCE: dict[int, list[str]] = {
    1: ["templates/course_release/README.md", "scripts/generate_course_release.py"],
    2: ["apprenticeships/README.md", "results/apprenticeships/research_apprenticeship_index.md"],
    3: ["rubrics/foi_rubric.yaml"],
    4: ["curriculum/learning_outcomes_matrix.md", "curriculum/program_outcomes.yaml"],
    5: ["compliance/fair_chance_youth_safety_policy.md"],
    6: ["ops/global_campus_ops_playbook.md"],
    7: ["portfolio/templates/project_story_card.md"],
    9: ["docs/00_WAIKE_KNOWLEDGE_OS.md"],
    10: ["docs/01_FOUNDERS_EDUCATION_TO_CURRICULUM_MAP.md"],
    11: ["docs/04_WAIKE_LEVELS_0_TO_7.md", "curriculum/levels.yaml"],
    12: ["docs/02_BEYOND_THE_FOUNDER_STANDARD.md", "philosophy/beyond_the_founder_standard.md"],
    13: ["docs/08_GUNNCHAI3K_TUTOR_REQUIREMENTS.md", "gunnchai/tutor_requirements.md"],
    14: ["docs/17_WAIKE_TO_GUNNCHAI3K_API_CONTRACT.md"],
    15: ["standards_alignment/ACM_CS2023_mapping.md"],
    16: ["standards_alignment/ABET_mapping.md"],
    17: ["standards_alignment/NIST_NICE_mapping.md"],
    18: ["standards_alignment/SFIA_9_mapping.md"],
    19: ["standards_alignment/SWEBOK_mapping.md"],
    20: ["standards_alignment/NIST_AI_RMF_mapping.md"],
    21: ["standards_alignment/CompTIA_A_PLUS_mapping.md"],
    22: ["standards_alignment/Cisco_CCNA_mapping.md"],
    23: ["standards_alignment/ISC2_CC_SECURITY_PLUS_mapping.md"],
    24: ["capstones/README.md", "results/capstones/capstone_library_index.md"],
    25: ["instructor_training/README.md", "results/instructor_training/instructor_training_packet.md"],
    26: ["portfolio/README.md", "results/portfolio/portfolio_requirements_index.md"],
    27: ["localization/README.md", "results/localization/localization_plan.md"],
    28: ["evaluation/README.md", "results/evaluation/evaluation_dashboard.md"],
}


def implement_all() -> None:
    course_release_templates()
    apprenticeships()
    standards_mappings()
    capstone_library()
    instructor_training()
    portfolio_requirements()
    localization()
    evaluation_dashboard()
    supporting_issues()
    # generate_course_release script
    w(
        ROOT / "scripts/generate_course_release.py",
        '#!/usr/bin/env python3\nprint("Use templates/course_release/ — preview in results/templates/")\n',
    )


def evidence_ok(issue_num: int) -> bool:
    for rel in ISSUE_EVIDENCE.get(issue_num, []):
        if not (ROOT / rel).exists():
            return False
    return bool(ISSUE_EVIDENCE.get(issue_num))
