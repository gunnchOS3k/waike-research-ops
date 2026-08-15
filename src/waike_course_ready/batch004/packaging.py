"""Course-specific packaging for COURSE-READY-004."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch004.labs import COURSE_LABS_004, LAB_SPECS_004

SYLLABUS_ASSESSMENT_004 = {
    "WIRELESS_6G": (
        "Pier Radio assessment mix: weekly WR quizzes on FSPL/OFDM/BLER/NTN/AI-RAN gates, "
        "mid (20 original) on honesty+math, final (24 original) on spectrum/O-RAN/capstone, "
        "practical over ten runnable labs rejecting empty/wrong/print-PASS, and a radio notebook "
        "portfolio. Commercial standardized 6G does NOT exist today."
    ),
    "ROBOTICS_CONTROL": (
        "HarborBot assessment mix: weekly RB quizzes on frames/FK/PID/traj/E-stop, mid (20) and "
        "final (24) original banks, practical over ten labs, and a safety packet portfolio. "
        "No device-os PRs; no fabricated injury stats."
    ),
    "GAME_DEV_INTERACTIVE": (
        "Forge Arcade assessment mix: weekly GA quizzes on loop/AABB/audio/FSM/a11y, mid (20) and "
        "final (24) original, practical over ten labs, optional four-game case study without unmerged "
        "branch dependencies, and an a11y ship checklist portfolio."
    ),
}

SYLLABUS_DURATION_004 = {
    "WIRELESS_6G": (
        "Ten Pier Radio weeks (~8–10 hours/week). Fixture math only while Stream A QEMU is active — "
        "no multi-GB sim downloads. RESEARCH_ONLY foresight labeled; not a 6G brochure."
    ),
    "ROBOTICS_CONTROL": (
        "Ten HarborBot weeks with E-stop drills. Budget quiet time for kinematics whiteboarding; "
        "demo videos without math score zero."
    ),
    "GAME_DEV_INTERACTIVE": (
        "Ten Forge Arcade weeks. Optional four-game case studies are optional; builds must not hard-"
        "depend on unmerged branches. A11y week is NO_AI."
    ),
}

SYLLABUS_CLAIM_004 = {
    "WIRELESS_6G": (
        "Aligns to 3GPP 5G-Advanced / NTN / O-RAN topic labels as PUBLIC_REFERENCE_ONLY. Does not "
        "grant those memberships or claim commercial standardized 6G. Instructor keys stay out of "
        "the learner packet."
    ),
    "ROBOTICS_CONTROL": (
        "Aligns to industrial robotics operator and machine-guarding awareness labels as "
        "PUBLIC_REFERENCE_ONLY. Does not grant OSHA licenses or vendor certs. Instructor keys stay "
        "out of the learner packet."
    ),
    "GAME_DEV_INTERACTIVE": (
        "Aligns to Unity/Godot fundamentals topic labels as PUBLIC_REFERENCE_ONLY. Does not grant "
        "those credentials. Instructor keys stay out of the learner packet."
    ),
}

PITFALLS = {
    "WIRELESS_6G": {
        1: "Learners paste 6G marketing. Stop them; FSPL only.",
        2: "Constellation screenshots without numerology math.",
        3: "Inventing Rel-20 commercial 6G rows.",
        4: "Max MCS ignoring BLER.",
        5: "GEO delay claimed for LEO toy.",
        6: "AI beamforming stories without taps.",
        7: "Ungated auto-apply AI-RAN.",
        8: "Unauthorized TX 'because SDR'.",
        9: "Fake production RIC.",
        10: "Consuming unmerged Product-Use packages.",
    },
    "ROBOTICS_CONTROL": {
        1: "No frame diagram.",
        2: "Infinite reach myths.",
        3: "Missing anti-windup notes.",
        4: "Ignoring vmax.",
        5: "Trusting raw lidar max.",
        6: "Soft slowdown as E-stop.",
        7: "B=0 kinematics.",
        8: "Zero-covariance lies.",
        9: "Fleet deploy claims.",
        10: "Opening device-os PRs.",
    },
    "GAME_DEV_INTERACTIVE": {
        1: "Variable dt without clamp.",
        2: "VFX as collision proof.",
        3: "Pirated sample packs.",
        4: "Illegal FSM edges accepted.",
        5: "Screenshot-only levels.",
        6: "Scancode-only docs.",
        7: "Hard-depending unmerged game PRs.",
        8: "Vanity DAU slides.",
        9: "flash_hz>3 or no captions.",
        10: "Shipping without a11y_ok.",
    },
}


def rubrics_004(course_id: str) -> list[dict[str, Any]]:
    if course_id == "WIRELESS_6G":
        return [
            {"rubric_id": "WIRELESS_6G-lab", "title": "Pier Radio lab", "criteria": [
                {"name": "fspl_or_bler", "weight": 20, "desc": "FSPL/BLER/NTN math matches fixture"},
                {"name": "honesty_flags", "weight": 20, "desc": "commercial_6g/NTN-standard flags honest"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong arithmetic fails"},
                {"name": "print_pass", "weight": 20, "desc": "PASS-only rejected"},
            ]},
            {"rubric_id": "WIRELESS_6G-assignment", "title": "Radio journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses WR-#### tickets"},
                {"name": "no_6g_brochure", "weight": 30, "desc": "No commercial 6G claim"},
                {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged when used"},
            ]},
            {"rubric_id": "WIRELESS_6G-quiz", "title": "Radio knowledge", "criteria": [
                {"name": "fixture_numbers", "weight": 50, "desc": "Original stems with Pier numbers"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "WIRELESS_6G-mid", "title": "Mid Pier audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
                {"name": "fspl_ofdm_ntn", "weight": 40, "desc": "FSPL/OFDM/BLER/NTN"},
            ]},
            {"rubric_id": "WIRELESS_6G-final-knowledge", "title": "Final radio exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone items"},
                {"name": "airan_oran_honesty", "weight": 50, "desc": "AI-RAN/O-RAN/6G honesty"},
            ]},
            {"rubric_id": "WIRELESS_6G-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "6G-true/ungated negatives fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "WIRELESS_6G-project", "title": "Radio notebook", "criteria": [
                {"name": "digest", "weight": 40, "desc": "Notebook sha256 present"},
                {"name": "no_pu_unmerged", "weight": 30, "desc": "No Product-Use unmerged consume"},
                {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
            ]},
            {"rubric_id": "WIRELESS_6G-portfolio", "title": "Radio portfolio", "criteria": [
                {"name": "alt_text", "weight": 40, "desc": "Text path / plot alt_text"},
                {"name": "claim_boundary", "weight": 30, "desc": "No commercial 6G / cert claim"},
                {"name": "career_map", "weight": 30, "desc": "Aligned roles present"},
            ]},
        ]
    if course_id == "ROBOTICS_CONTROL":
        return [
            {"rubric_id": "ROBOTICS_CONTROL-lab", "title": "HarborBot lab", "criteria": [
                {"name": "kin_pid", "weight": 20, "desc": "FK/PID/traj/fuse math"},
                {"name": "estop", "weight": 20, "desc": "E-stop hard policy"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong fields fail"},
                {"name": "print_pass", "weight": 20, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-assignment", "title": "Bay journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses RB-####"},
                {"name": "frames", "weight": 30, "desc": "ASCII frame diagrams"},
                {"name": "no_bypass", "weight": 30, "desc": "No E-stop bypass"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-quiz", "title": "Controls knowledge", "criteria": [
                {"name": "bay_numbers", "weight": 50, "desc": "Original stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-mid", "title": "Mid HarborBot audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone"},
                {"name": "fk_pid_estop", "weight": 40, "desc": "FK/PID/E-stop"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-final-knowledge", "title": "Final controls exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
                {"name": "fuse_schema_safety", "weight": 50, "desc": "Fuse/schema/safety"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "Soft-E-stop/B=0 fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-project", "title": "Safety packet", "criteria": [
                {"name": "estop_ok", "weight": 40, "desc": "estop_ok true"},
                {"name": "no_device_os", "weight": 30, "desc": "no_device_os_pr"},
                {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
            ]},
            {"rubric_id": "ROBOTICS_CONTROL-portfolio", "title": "Bay portfolio", "criteria": [
                {"name": "large_text_estop", "weight": 40, "desc": "Printable E-stop sheet"},
                {"name": "no_fake_injury", "weight": 30, "desc": "No fabricated stats"},
                {"name": "career_map", "weight": 30, "desc": "Aligned roles"},
            ]},
        ]
    if course_id == "GAME_DEV_INTERACTIVE":
        return [
            {"rubric_id": "GAME_DEV_INTERACTIVE-lab", "title": "Arcade lab", "criteria": [
                {"name": "loop_collide", "weight": 20, "desc": "Loop/AABB/FSM math"},
                {"name": "a11y_license", "weight": 20, "desc": "A11y + license honesty"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong fields fail"},
                {"name": "print_pass", "weight": 20, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-assignment", "title": "Arcade journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses GA-####"},
                {"name": "no_piracy", "weight": 30, "desc": "No cracked packs"},
                {"name": "optional_case", "weight": 30, "desc": "Case study optional / no unmerged hard dep"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-quiz", "title": "Game knowledge", "criteria": [
                {"name": "arcade_numbers", "weight": 50, "desc": "Original stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-mid", "title": "Mid Arcade audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone"},
                {"name": "loop_audio_fsm", "weight": 40, "desc": "Loop/audio/FSM"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-final-knowledge", "title": "Final arcade exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone"},
                {"name": "a11y_metrics_ship", "weight": 50, "desc": "A11y/metrics/ship"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "Piracy/flash negatives fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-project", "title": "Ship checklist", "criteria": [
                {"name": "a11y_ok", "weight": 40, "desc": "a11y_ok true"},
                {"name": "no_unmerged", "weight": 30, "desc": "unmerged_branch_required false"},
                {"name": "six_labs", "weight": 30, "desc": "labs_passed≥6"},
            ]},
            {"rubric_id": "GAME_DEV_INTERACTIVE-portfolio", "title": "Arcade portfolio", "criteria": [
                {"name": "keyboard_path", "weight": 40, "desc": "Keyboard-only notes"},
                {"name": "no_vanity_dau", "weight": 30, "desc": "No fake DAU"},
                {"name": "career_map", "weight": 30, "desc": "Aligned roles"},
            ]},
        ]
    raise KeyError(course_id)


def lab_readme_004(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_004[lab_id]
    hooks = {
        "WIRELESS_6G": ("From the Pier Radio Bench folder, submit computed JSON.", "Empty {} fails. PASS raises. No commercial 6G."),
        "ROBOTICS_CONTROL": ("From HarborBot Bay, submit kinematics/safety JSON.", "Soft E-stop and B=0 fail."),
        "GAME_DEV_INTERACTIVE": ("From Forge Arcade, submit loop/collision/a11y JSON.", "Piracy and flash_hz>3 fail."),
    }
    how, empty = hooks[course_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "", "## Student artifact", empty,
        "A file whose entire body is PASS is rejected by _fail_if_print_pass.", "", "## How to run", how,
        "```", f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --empty", "```", "", spec["wrong_hint"], "",
    ])


def instructor_week_notes_004(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    titles = {"WIRELESS_6G": "Pier Radio", "ROBOTICS_CONTROL": "HarborBot", "GAME_DEV_INTERACTIVE": "Forge Arcade"}
    return (
        f"# {titles[course_id]} — instructor week {n}\n\n"
        f"**Live number/example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n\n"
        f"Refuse dumps. Point at curriculum/alignment/{course_id.lower()}_alignment.json.\n"
        f"AI policy: see course.ai_use_policy in course.json.\n"
        f"Accessibility: text-first journals; large-print where noted.\n"
    )


def presentation_004(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\n\n"
        f"## Slide 1 — Hook\n{week['title']}\n\n"
        f"## Slide 2 — Worked example\n{week['worked_example']}\n\n"
        f"## Slide 3 — Lab contract\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\n\n"
        f"## Speaker notes\nStay in {course_id} vocabulary. Do not noun-swap another academy's deck.\n"
        f"Assignment: {week['assignment'][:180]}...\n"
    )


def instructor_packet_004(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\n"
        f"- See instructor/accessibility_and_udl_guide.md\n"
        f"- Do not claim vendor certs, commercial 6G, or physical completion without evidence\n"
        f"- Cursor does not merge; REAL_*_E6 remain false\n"
    )


def student_packet_004(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n"
        f"{hook}\n\n"
        f"- Submit lab JSON you computed; empty/wrong/print-PASS fail\n"
        f"- Accessibility: prefer text paths; request large-print materials\n"
        f"- Career map: see career_mapping.json (certs aligned not granted)\n"
        f"- Offline pack: offline_pack/pack.json\n"
    )


def group_project_004(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_004(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\n\n"
        f"- Lab result JSON + empty-fail evidence\n"
        f"- Claim boundary paragraph\n"
        f"- Accessibility notes\n"
        f"- Career map excerpt\n"
    )
