#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "REQUIREMENTS.md",
    "curriculum/catalog.yaml",
    "results/catalog/course_catalog.md",
    "results/validation/curriculum_validation_report.md",
    "results/validation/depth_validation_report.md",
    "results/validation/no_exam_heavy_report.md",
    "results/portfolio_evidence_index/portfolio_evidence_index.md",
    "curriculum_depth/artifact_depth_standard.md",
]

COURSES = [
    "digital_confidence", "general_it", "hardware_engineering", "software_engineering",
    "networking", "cybersecurity", "cloud_devops", "ai_ml_data", "edge_ai_embedded",
    "wireless_dsp_6g", "robotics_control", "project_management_agile_lss",
    "data_visualization_bi", "communication_ethics_professional_dev",
    "game_development_interactive_media", "gunnchos_device_os_product_lab",
    "ai_ran_digital_twin_research", "reproducible_research",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    for cid in COURSES:
        missing += [
            p for p in [
                f"results/deep_student_packets/{cid}_student_packet.md",
                f"results/deep_instructor_packets/{cid}_instructor_packet.md",
                f"results/deep_course_packets/{cid}_deep_course_packet.md",
                f"assignment_bodies/by_course/{cid}/assignment_01.md",
                f"assignment_bodies/by_course/{cid}/assignment_08.md",
                f"lessons/by_course/{cid}/week_01/lesson_plan.md",
                f"lessons/by_course/{cid}/week_08/lesson_plan.md",
                f"group_projects/by_course/{cid}/project_brief.md",
                f"student_workbooks/by_course/{cid}/workbook.md",
                f"industry_alignment/by_course/{cid}/job_role_map.md",
                f"assessment/by_course/{cid}/mastery_evidence_map.md",
            ]
            if not (ROOT / p).exists()
        ]
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
