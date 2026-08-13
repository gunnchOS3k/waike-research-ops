
"""Course-specific packaging for COURSE-READY-002."""
from __future__ import annotations
from typing import Any
from waike_course_ready.batch002.labs import COURSE_LABS_002, LAB_SPECS_002

SYLLABUS_ASSESSMENT_002 = {
  "SOFTWARE_BUILDER": (
    "ForgeDesk assessment mix: weekly builder quizzes on ticket 8801-class numbers, "
    "a mid-course audit (20 original items on conflict/REST/migrate/authz/CI), a final "
    "(24 original items on deploy/security/SLO/capstone path), a practical over ten "
    "runnable labs that reject empty/wrong/print-PASS, and an issue-to-deploy group "
    "project. Silent 200 on forbidden writes scores zero."
  ),
  "HARDWARE_ENGINEERING": (
    "ForgeSense assessment mix: weekly circuit/embedded quizzes, mid (20 original) on "
    "dividers/Thevenin/RC/logic/power/bus, final (24 original) on Zephyr/DT/PCB/diagnosis, "
    "practical over ten digital labs, and a digitally validated subsystem project. "
    "Soldering remains PHYSICAL_PENDING. Fabricated yield claims fail."
  ),
  "PM_AGILE_LSS": (
    "Process Studio assessment mix: weekly PM/LSS quizzes, mid (20 original) on "
    "charter/RACI/WBS/sprint/risk/SIPOC, final (24 original) on Pareto/SPC/DMAIC/change/"
    "PMP-2026-context judgment, practical over ten artifact labs, and an end-to-end "
    "improvement simulation. Not a PMI ATP. No fabricated community outcomes."
  ),
}

SYLLABUS_DURATION_002 = {
  "SOFTWARE_BUILDER": (
    "Ten ForgeDesk weeks (~8–10 hours/week including CI red-build time). Not a two-hour "
    "HTML workshop. Device Lab compose is scheduled; do not deploy ungated on pull_request."
  ),
  "HARDWARE_ENGINEERING": (
    "Ten Hardware+Embedded weeks with sim/QEMU before any iron. Budget quiet time for "
    "network math and DT overlays; PHYSICAL_PENDING blocks soldering until digital PASS."
  ),
  "PM_AGILE_LSS": (
    "Ten Process/PM weeks on one Device Lab wait problem. Chart math weeks are calculator "
    "OK / generative-fill NO_AI. Sponsor demos use fixture counts only."
  ),
}

SYLLABUS_CLAIM_002 = {
  "SOFTWARE_BUILDER": (
    "Aligns to CS50/CS50 Web topic shape and GitHub Actions docs as PUBLIC_REFERENCE_ONLY. "
    "Secure-dev themes are labels. Does not grant vendor certs. Instructor keys stay out "
    "of the learner packet."
  ),
  "HARDWARE_ENGINEERING": (
    "Aligns to MIT OCW 6.002 rigor citations, Zephyr/KiCad/datasheet references. Integrates "
    "EMBEDDED_PROTOTYPING. Does not redistribute OCW problem sets or claim physical completion "
    "without evidence. Instructor keys stay out of the learner packet."
  ),
  "PM_AGILE_LSS": (
    "Aligns to ASQ CSSGB BoK themes, PMI CAPM ECO, and PMI PMP 2026 ECO (People/Process/"
    "Business Environment; AI/sustainability/value in context). WAIKE is NOT a PMI ATP and "
    "grants no PMI/ASQ credential. Instructor keys stay out of the learner packet."
  ),
}

def rubrics_002(course_id: str) -> list[dict[str, Any]]:
    if course_id == "SOFTWARE_BUILDER":
        return [
            {"rubric_id": "SOFTWARE_BUILDER-lab", "title": "ForgeDesk lab", "criteria": [
                {"name": "conflict_tokens", "weight": 20, "desc": "require_role and HOURS both survive"},
                {"name": "status_map", "weight": 20, "desc": "201/400/403/404 map matches role/body"},
                {"name": "ci_gate", "weight": 20, "desc": "PR workflow lint→test→upload; no ungated deploy"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails student_artifact"},
                {"name": "print_pass", "weight": 20, "desc": "PASS-only submission rejected"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-assignment", "title": "Builder journal", "criteria": [
                {"name": "ticket_numbers", "weight": 40, "desc": "Uses 8801-class tickets not 'a bug'"},
                {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged when used"},
                {"name": "no_secrets", "weight": 30, "desc": "No passwords/tokens in journal"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-quiz", "title": "Builder knowledge", "criteria": [
                {"name": "forge_numbers", "weight": 50, "desc": "Original stems; status/digest/SLO math"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys only in instructor/answer_keys.json"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-mid", "title": "Mid ForgeDesk audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 items not weekly clones / Jaccard<0.80"},
                {"name": "conflict_rest_ci", "weight": 40, "desc": "Conflict, REST, migrate, authz, CI"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-final-knowledge", "title": "Final builder exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 items not weekly clones"},
                {"name": "deploy_sec_slo", "weight": 50, "desc": "Deploy, review, availability, capstone path"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "Bot-close and bad migrate fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS string rejected"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-project", "title": "Issue to deploy", "criteria": [
                {"name": "path_complete", "weight": 40, "desc": "issue→PR→CI→migrate→deploy→SLO"},
                {"name": "device_lab_target", "weight": 30, "desc": "Local compose digest pin"},
                {"name": "no_fabricated_impact", "weight": 30, "desc": "Fixture counts only"},
            ]},
            {"rubric_id": "SOFTWARE_BUILDER-portfolio", "title": "Builder portfolio", "criteria": [
                {"name": "lab_json", "weight": 40, "desc": "Lab results + empty-fail evidence"},
                {"name": "security_findings", "weight": 30, "desc": "IDOR finding with evidence"},
                {"name": "no_cert_claim", "weight": 30, "desc": "Does not claim vendor certs"},
            ]},
        ]
    if course_id == "HARDWARE_ENGINEERING":
        return [
            {"rubric_id": "HARDWARE_ENGINEERING-lab", "title": "ForgeSense lab", "criteria": [
                {"name": "network_math", "weight": 20, "desc": "I/Vout/Vth/Rth/tau computed not guessed"},
                {"name": "mpn_budget", "weight": 20, "desc": "Real MPNs with positive margin"},
                {"name": "qemu_west", "weight": 20, "desc": "qemu_cortex_m0 + PHYSICAL_PENDING"},
                {"name": "erc_drc", "weight": 20, "desc": "Zero ERC/DRC; power connected"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty/wrong/print-PASS fail"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-assignment", "title": "Bench journal", "criteria": [
                {"name": "numbers", "weight": 40, "desc": "Uses fixture net values not adjectives"},
                {"name": "physical_pending", "weight": 30, "desc": "Does not claim solder done"},
                {"name": "ai_disclosure", "weight": 30, "desc": "Numeric AI_RESTRICTED honored"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-quiz", "title": "Circuit/embedded knowledge", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "WAIKE stems; no OCW item harvest"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-mid", "title": "Mid network/embedded exam", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
                {"name": "divider_rc_bus", "weight": 40, "desc": "Divider/RC/logic/power/bus"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-final-knowledge", "title": "Final subsystem exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone items"},
                {"name": "zephyr_pcb_fail", "weight": 50, "desc": "QEMU/DT/PCB/diagnosis"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-practical", "title": "Digital hardware practical", "criteria": [
                {"name": "computed_nets", "weight": 40, "desc": "SPICE/Thevenin from values"},
                {"name": "negatives", "weight": 30, "desc": "Fake MPN / DONE physical fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-project", "title": "Digitally validated subsystem", "criteria": [
                {"name": "artifact_chain", "weight": 40, "desc": "Power+bus+DT+QEMU+diagnosis linked"},
                {"name": "no_fake_yield", "weight": 30, "desc": "No fabricated field yields"},
                {"name": "embedded_integration", "weight": 30, "desc": "Shows EMBEDDED_PROTOTYPING outcomes"},
            ]},
            {"rubric_id": "HARDWARE_ENGINEERING-portfolio", "title": "Hardware portfolio", "criteria": [
                {"name": "bom_budget", "weight": 40, "desc": "BOM + power budget MPNs"},
                {"name": "qemu_log", "weight": 30, "desc": "Sanitized QEMU evidence"},
                {"name": "no_ocw_copy", "weight": 30, "desc": "No OCW problem-set paste"},
            ]},
        ]
    if course_id == "PM_AGILE_LSS":
        return [
            {"rubric_id": "PM_AGILE_LSS-lab", "title": "Process Studio lab", "criteria": [
                {"name": "charter_metric", "weight": 20, "desc": "Baseline metric; fabricated_outcomes false"},
                {"name": "one_A", "weight": 20, "desc": "Exactly one Accountable per task"},
                {"name": "critical_path", "weight": 20, "desc": "CP days recomputed from preds"},
                {"name": "spc_math", "weight": 20, "desc": "mean/UCL/LCL/ooc match fixture"},
                {"name": "ai_disclose", "weight": 20, "desc": "AI critique sets ai_disclosed true"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-assignment", "title": "PM memo", "criteria": [
                {"name": "named_artifacts", "weight": 40, "desc": "References lab artifact ids"},
                {"name": "no_fake_community", "weight": 30, "desc": "No invented city outcomes"},
                {"name": "not_atp", "weight": 30, "desc": "Does not claim PMI ATP/credential"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-quiz", "title": "PM/LSS knowledge", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "WAIKE stems; no ECO task paste"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-mid", "title": "Mid process/PM exam", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
                {"name": "charter_raci_wbs", "weight": 40, "desc": "Charter/RACI/WBS/sprint/risk"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-final-knowledge", "title": "Final process/PM exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone items"},
                {"name": "dmaic_pmp2026", "weight": 50, "desc": "DMAIC/SPC/change/PMP-2026 context"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-practical", "title": "Artifact practical", "criteria": [
                {"name": "empty_fails", "weight": 40, "desc": "Empty submissions fail"},
                {"name": "math_labs", "weight": 30, "desc": "Pareto/SPC/CP compute"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-project", "title": "E2E improvement simulation", "criteria": [
                {"name": "chain", "weight": 40, "desc": "charter→DMAIC→change→status→AI critique"},
                {"name": "real_artifacts", "weight": 30, "desc": "Uses prior lab outputs"},
                {"name": "claim_boundary", "weight": 30, "desc": "Not ATP; no fake certs/outcomes"},
            ]},
            {"rubric_id": "PM_AGILE_LSS-portfolio", "title": "PM portfolio", "criteria": [
                {"name": "registers", "weight": 40, "desc": "RACI/risk/sprint artifacts"},
                {"name": "charts", "weight": 30, "desc": "Pareto + control chart"},
                {"name": "no_cert_claim", "weight": 30, "desc": "No CAPM/PMP/CSSGB claim"},
            ]},
        ]
    raise KeyError(course_id)

PITFALLS = {
  "SOFTWARE_BUILDER": {
    1: "Learners will take-theirs without reading. Stop them; both tokens must survive.",
    2: "200-with-null is a lie. Force 404.",
    3: "Watch for DELETE FROM checkouts 'cleanup'.",
    4: "Red CSS without OVERDUE text fails.",
    5: "forge-bot with close is the week's exam.",
    6: "PNG badges are not JUnit.",
    7: "Ungated deploy on PR fails the gate.",
    8: "rollback_to==current is theater.",
    9: "Empty findings on IDOR fixture fail.",
    10: "Fabricated city savings fail the capstone.",
  },
  "HARDWARE_ENGINEERING": {
    1: "Screenshot of a GUI is not I/Vout math.",
    2: "Forgetting loading when Rin≈Rth.",
    3: "Sampling reset too early.",
    4: "Swapping NAND for NOR casually.",
    5: "Fake MPNs.",
    6: "Bit-bang before checking pullups/rail.",
    7: "Claiming physical DONE.",
    8: "Deleting soc in DT.",
    9: "Nonzero ERC waived casually.",
    10: "Invented yield percentages.",
  },
  "PM_AGILE_LSS": {
    1: "Goals without baselines.",
    2: "Two Accountables.",
    3: "Critical path by vibes.",
    4: "Overcommit sprint.",
    5: "score≠prob*impact.",
    6: "Outputs without measures.",
    7: "Stopping Pareto under 80%.",
    8: "AI-filled control limits under NO_AI.",
    9: "Fake community outcomes in DMAIC.",
    10: "ai_disclosed false.",
  },
}

def lab_readme_002(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_002[lab_id]
    hooks = {
      "SOFTWARE_BUILDER": ("From the ForgeDesk repo root, submit the JSON you computed.", "Empty {} fails. PASS string raises."),
      "HARDWARE_ENGINEERING": ("From the ForgeSense digital bench, submit computed values — not a GUI screenshot.", "Wrong arithmetic fails. PHYSICAL_PENDING stays pending."),
      "PM_AGILE_LSS": ("From the Process Studio folder, submit artifact JSON with fixture counts only.", "Fabricated outcomes fail. AI critique requires ai_disclosed true."),
    }
    how, empty = hooks[course_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "", "## Student artifact", empty,
        "A file whose entire body is PASS is rejected by _fail_if_print_pass.", "", "## How to run", how,
        "```", f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --empty", "```", "", spec["wrong_hint"], "",
    ])

def instructor_week_notes_002(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    titles = {"SOFTWARE_BUILDER": "ForgeDesk", "HARDWARE_ENGINEERING": "ForgeSense", "PM_AGILE_LSS": "Process Studio"}
    return (
        f"# {titles[course_id]} — instructor week {n}\n\n"
        f"**Live number/example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n\n"
        f"Refuse dumps. Point at curriculum/alignment/{course_id.lower()}_alignment.json.\n"
        f"AI policy: see course.ai_use_policy in course.json.\n"
    )

def presentation_002(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\n\n"
        f"## Slide 1 — Hook\n{week['title']}\n\n"
        f"## Slide 2 — Worked example\n{week['worked_example']}\n\n"
        f"## Slide 3 — Lab contract\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\n\n"
        f"## Speaker notes\nStay in {course_id} vocabulary. Do not noun-swap another academy's deck.\n"
        f"Assignment: {week['assignment'][:180]}...\n"
    )

def instructor_packet_002(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\n"
        f"- AI policy modes: EXPLAIN/HINT/QUESTION_ME/DEBUG_WITH_ME/REVIEW_MY_WORK/COMPARE_APPROACHES/PRACTICE\n"
        f"- Assessment modes: AI_ALLOWED / AI_RESTRICTED / AI_DISCLOSED / NO_AI\n"
        f"- Do not claim PMI ATP, vendor certs, or physical completion without evidence\n"
        f"- Public pages ≠ free to copy\n"
    )

def student_packet_002(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n"
        f"{hook}\n\n"
        f"Submit lab JSON you computed. Empty submissions fail. Do not paste PASS.\n"
        f"Disclose AI modes when used. Some assessments are NO_AI or AI_RESTRICTED.\n"
        f"Portfolio uses fixture evidence only — no fabricated community outcomes.\n"
    )

def group_project_002(course_id: str, title: str, assignment: str) -> str:
    if course_id == "SOFTWARE_BUILDER":
        body = "Ship issue→PR→CI→migrate→compose digest deploy→SLO note using ForgeDesk fixtures."
    elif course_id == "HARDWARE_ENGINEERING":
        body = "Digitally validate ForgeSense subsystem (budget+bus+DT+QEMU+diagnosis). PHYSICAL_PENDING for solder."
    else:
        body = "Run end-to-end improvement simulation with charter→DMAIC→change→status→AI critique artifacts."
    return f"# Group project — {title}\n\n{body}\n\nSeed assignment cue:\n{assignment}\n"

def portfolio_002(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\n\n"
        f"Include lab result JSON, one failing empty-submission proof, and the capstone packet.\n"
        f"Do not claim certs. Do not invent community outcomes.\n"
    )
