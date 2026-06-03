#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "REQUIREMENTS.md",
    "curriculum/catalog.yaml",
    "results/catalog/course_catalog.md",
    "results/catalog/course_catalog.json",
    "results/validation/curriculum_validation_report.md",
    "results/e2e/course_repo_map.md",
    "docs/video_walkthrough_script.md",
]

COURSES = [
    "digital_confidence", "general_it", "hardware_engineering", "software_engineering",
    "networking", "cybersecurity", "cloud_devops", "ai_ml_data", "edge_ai_embedded",
    "wireless_dsp_6g", "robotics_control", "project_management_agile_lss",
    "data_visualization_bi", "communication_ethics_professional_dev",
    "game_development_interactive_media", "gunnchos_device_os_product_lab",
    "ai_ran_digital_twin_research", "reproducible_research",
]

CAMPUSES = ["gary", "ghana", "guyana", "gaza", "geelong", "graham_land", "germany"]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    for cid in COURSES:
        for suffix in ["_syllabus.md", "_assignments.md", "_group_project.md",
                       "_instructor_packet.md", "_student_packet.md"]:
            p = f"results/{'syllabi' if suffix == '_syllabus.md' else 'assignment_packs' if 'assign' in suffix else 'group_project_packs' if 'group' in suffix else 'instructor_packets' if 'instructor' in suffix else 'student_packets'}/{cid}{suffix}"
            # fix paths
        missing += [
            p for p in [
                f"results/syllabi/{cid}_syllabus.md",
                f"results/assignment_packs/{cid}_assignments.md",
                f"results/group_project_packs/{cid}_group_project.md",
                f"results/instructor_packets/{cid}_instructor_packet.md",
                f"results/student_packets/{cid}_student_packet.md",
            ]
            if not (ROOT / p).exists()
        ]
    for site in CAMPUSES:
        if not (ROOT / f"results/case_study_packs/{site}_case_studies.md").exists():
            missing.append(f"results/case_study_packs/{site}_case_studies.md")
    for d in ["context.mmd", "sequence_main_demo.mmd", "code_path_main_demo.mmd"]:
        if not (ROOT / "docs/diagrams" / d).exists():
            missing.append("docs/diagrams/" + d)
    if missing:
        print("FAIL", missing[:25], f"... total {len(missing)}" if len(missing) > 25 else "")
        return 1
    print("PASS e2e artifacts waike-research-ops")
    return 0


if __name__ == "__main__":
    sys.exit(main())
