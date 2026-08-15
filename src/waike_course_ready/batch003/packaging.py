"""Course-specific packaging for COURSE-READY-003."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch003.labs import COURSE_LABS_003, LAB_SPECS_003

SYLLABUS_ASSESSMENT_003 = {
    "AI_ML_EDGE": (
        "EdgeForge assessment mix: weekly quizzes on EF ticket numbers and fixture math, "
        "a mid-course (20 original items on splits/metrics/windows/deploy), a final "
        "(24 original on quantization/RAG/responsibility), a practical over ten runnable "
        "labs that reject empty/wrong/print-PASS, and a redacted-RAG portfolio. "
        "print('PASS') is not a metric."
    ),
    "DATA_VIZ_BI": (
        "Civic Metrics Studio assessment mix: weekly quizzes on CM tickets, mid (20 original) "
        "on clean/SQL/stats/encode, final (24 original) on KPI/repro/license honesty, "
        "practical over ten artifact labs, and a hashed dashboard portfolio. "
        "No pirated BI binaries; no gallery workbooks claimed as yours."
    ),
    "CLOUD_DEVOPS": (
        "ForgeCloud assessment mix: weekly quizzes on FC tickets, mid (20 original) on "
        "perms/git/containers/CI/IAM, final (24 original) on SLO/rollback/k8s/incident, "
        "practical over ten labs, and an incident-runbook portfolio. No force-push main; "
        "no fake CKA/AWS cert claims."
    ),
}

SYLLABUS_DURATION_003 = {
    "AI_ML_EDGE": (
        "Ten EdgeForge weeks (~8–10 hours/week including metric homework). Not a two-hour "
        "AI buzzword tour. Coral flash stays PHYSICAL_PENDING until digital budgets PASS."
    ),
    "DATA_VIZ_BI": (
        "Ten Civic Metrics weeks. Stats weeks are calculator OK / generative-fill NO_AI. "
        "Dashboard first screen stays at three tiles."
    ),
    "CLOUD_DEVOPS": (
        "Ten ForgeCloud weeks with bastion permissions before YAML. Budget quiet time for "
        "pipeline red builds; do not ungated-deploy on pull_request."
    ),
}

SYLLABUS_CLAIM_003 = {
    "AI_ML_EDGE": (
        "Aligns to Google Professional ML Engineer and AWS MLA domain labels as "
        "PUBLIC_REFERENCE_ONLY / RESTRICTED outlines. Does not grant those credentials. "
        "Instructor keys stay out of the learner packet."
    ),
    "DATA_VIZ_BI": (
        "Aligns to Microsoft PL-300 and Tableau Desktop Specialist topic labels as "
        "PUBLIC_REFERENCE_ONLY. No vendor binaries redistributed. Instructor keys stay "
        "out of the learner packet."
    ),
    "CLOUD_DEVOPS": (
        "Aligns to AWS Cloud Practitioner and CKA topic labels as PUBLIC_REFERENCE_ONLY. "
        "Does not grant those credentials. Instructor keys stay out of the learner packet."
    ),
}

PITFALLS = {
    "AI_ML_EDGE": {
        1: "Learners will shuffle occupancy. Stop them; time-order only.",
        2: "people_count as a feature when it defines the label is leakage.",
        3: "Cluster-as-hacker stories without evidence fail the week.",
        4: "AUC worship without an FPR-capped operating point.",
        5: "Reporting only train_acc.",
        6: "Windows that peek at t+1.",
        7: "Downloading giant weights instead of the tiny net.",
        8: "Scoring with a digest mismatch.",
        9: "Claiming PHYSICAL_DONE without digital PASS.",
        10: "Showing raw emails from RAG chunks.",
    },
    "DATA_VIZ_BI": {
        1: "Charting before cleaning negatives/nulls.",
        2: "Missing ON → cartesian.",
        3: "Leaving zone_address on every ticket row.",
        4: "Generative fill under NO_AI stats week.",
        5: "Pie of ticket_ids as a KPI.",
        6: "Stock-photo fourth tile.",
        7: "Cracked BI installers.",
        8: "groupby without input hash.",
        9: "Adjective storms without numbers.",
        10: "PNG-only portfolio.",
    },
    "CLOUD_DEVOPS": {
        1: "Leaving deploy keys 0666.",
        2: "Force-push to main.",
        3: "USER root + :latest.",
        4: "Ungated PR deploy.",
        5: "Public subnet for secrets.",
        6: "iam:CreateUser on deploy role / plaintext tokens.",
        7: "Blame without availability numbers.",
        8: "rollback_to == current.",
        9: "replicas=20 without requests + CKA claims.",
        10: "heroics=true undocumented fixes.",
    },
}


def rubrics_003(course_id: str) -> list[dict[str, Any]]:
    if course_id == "AI_ML_EDGE":
        return [
            {"rubric_id": "AI_ML_EDGE-lab", "title": "EdgeForge lab", "criteria": [
                {"name": "split_or_metrics", "weight": 20, "desc": "Split/metrics/window math matches fixture"},
                {"name": "digest_or_budget", "weight": 20, "desc": "Digest pin or int8 budget honest"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails student_artifact"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong arithmetic fails"},
                {"name": "print_pass", "weight": 20, "desc": "PASS-only rejected"},
            ]},
            {"rubric_id": "AI_ML_EDGE-assignment", "title": "Edge journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses EF-#### tickets"},
                {"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged when used"},
                {"name": "no_biometrics", "weight": 30, "desc": "No face/ID claims"},
            ]},
            {"rubric_id": "AI_ML_EDGE-quiz", "title": "Edge knowledge", "criteria": [
                {"name": "fixture_numbers", "weight": 50, "desc": "Original stems with EdgeForge numbers"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys only in instructor/answer_keys.json"},
            ]},
            {"rubric_id": "AI_ML_EDGE-mid", "title": "Mid EdgeForge audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 items not weekly clones / Jaccard<0.80"},
                {"name": "split_metrics_deploy", "weight": 40, "desc": "Splits, metrics, windows, deploy"},
            ]},
            {"rubric_id": "AI_ML_EDGE-final-knowledge", "title": "Final edge exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 items not weekly clones"},
                {"name": "quant_rag_responsibility", "weight": 50, "desc": "Quantization, RAG, harm notes"},
            ]},
            {"rubric_id": "AI_ML_EDGE-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "Leakage/digest negatives fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS string rejected"},
            ]},
            {"rubric_id": "AI_ML_EDGE-project", "title": "Redacted RAG portfolio", "criteria": [
                {"name": "path_complete", "weight": 40, "desc": "split→metrics→score→budget→RAG"},
                {"name": "redaction", "weight": 30, "desc": "Contact strings redacted"},
                {"name": "no_fabricated_impact", "weight": 30, "desc": "Fixture counts only"},
            ]},
            {"rubric_id": "AI_ML_EDGE-portfolio", "title": "Edge portfolio", "criteria": [
                {"name": "lab_json", "weight": 40, "desc": "Lab results + empty-fail evidence"},
                {"name": "digest_budget", "weight": 30, "desc": "Model digest + quant budget"},
                {"name": "no_cert_claim", "weight": 30, "desc": "No MLA/Google ML cert claim"},
            ]},
        ]
    if course_id == "DATA_VIZ_BI":
        return [
            {"rubric_id": "DATA_VIZ_BI-lab", "title": "Studio lab", "criteria": [
                {"name": "clean_sql_stats", "weight": 20, "desc": "Null/join/stat math correct"},
                {"name": "encode_kpi", "weight": 20, "desc": "Encoding + KPI formula"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong fields fail"},
                {"name": "print_pass", "weight": 20, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-assignment", "title": "Metrics journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses CM-#### tickets"},
                {"name": "license_honesty", "weight": 30, "desc": "No piracy claims"},
                {"name": "no_pii", "weight": 30, "desc": "No patron PII"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-quiz", "title": "BI knowledge", "criteria": [
                {"name": "studio_numbers", "weight": 50, "desc": "Original stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-mid", "title": "Mid Studio audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
                {"name": "clean_join_stats", "weight": 40, "desc": "Clean/SQL/stats/encode"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-final-knowledge", "title": "Final BI exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone items"},
                {"name": "kpi_repro", "weight": 50, "desc": "KPI + repro + license"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "Cartesian/piracy negatives fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-project", "title": "Hashed dashboard", "criteria": [
                {"name": "three_tiles", "weight": 40, "desc": "First screen contract"},
                {"name": "hashes", "weight": 30, "desc": "csv_sha256 present"},
                {"name": "no_cert_claim", "weight": 30, "desc": "No PL-300/Tableau claim"},
            ]},
            {"rubric_id": "DATA_VIZ_BI-portfolio", "title": "Studio portfolio", "criteria": [
                {"name": "quality_gates", "weight": 40, "desc": "null/negatives/freshness"},
                {"name": "story", "weight": 30, "desc": "Numbered board sentence"},
                {"name": "no_gallery_theft", "weight": 30, "desc": "No vendor gallery as yours"},
            ]},
        ]
    if course_id == "CLOUD_DEVOPS":
        return [
            {"rubric_id": "CLOUD_DEVOPS-lab", "title": "ForgeCloud lab", "criteria": [
                {"name": "perms_git_ci", "weight": 20, "desc": "0600 / no force-push / gated CI"},
                {"name": "slo_rollback", "weight": 20, "desc": "Budget + digest rollback"},
                {"name": "empty_fails", "weight": 20, "desc": "Empty JSON fails"},
                {"name": "wrong_fails", "weight": 20, "desc": "Wrong policy fails"},
                {"name": "print_pass", "weight": 20, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-assignment", "title": "Platform journal", "criteria": [
                {"name": "ticket_ids", "weight": 40, "desc": "Uses FC-#### tickets"},
                {"name": "no_force_push", "weight": 30, "desc": "Main protected"},
                {"name": "no_secrets", "weight": 30, "desc": "No plaintext tokens"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-quiz", "title": "Cloud knowledge", "criteria": [
                {"name": "forge_numbers", "weight": 50, "desc": "Original stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-mid", "title": "Mid ForgeCloud audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 non-clone items"},
                {"name": "linux_git_ci_iam", "weight": 40, "desc": "Perms/git/CI/IAM"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-final-knowledge", "title": "Final cloud exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 non-clone items"},
                {"name": "slo_k8s_incident", "weight": 50, "desc": "SLO/rollback/probes/incident"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-practical", "title": "Ten-lab practical", "criteria": [
                {"name": "student_json", "weight": 40, "desc": "Empty fails; reference passes"},
                {"name": "negatives", "weight": 30, "desc": "World-writable/heroics fail"},
                {"name": "print_pass", "weight": 30, "desc": "PASS rejected"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-project", "title": "Incident runbook", "criteria": [
                {"name": "runbook_id", "weight": 40, "desc": "RB-FC-rollback path"},
                {"name": "timeline", "weight": 30, "desc": "detect/contain/recover"},
                {"name": "no_cert_claim", "weight": 30, "desc": "No CKA/AWS claim"},
            ]},
            {"rubric_id": "CLOUD_DEVOPS-portfolio", "title": "ForgeCloud portfolio", "criteria": [
                {"name": "artifacts", "weight": 40, "desc": "Perms/CI/SLO/rollback/probes JSON"},
                {"name": "secrets_hygiene", "weight": 30, "desc": "Vault path, no plaintext"},
                {"name": "claim_boundary", "weight": 30, "desc": "Alignment labels only"},
            ]},
        ]
    raise KeyError(course_id)


def lab_readme_003(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_003[lab_id]
    hooks = {
        "AI_ML_EDGE": ("From the EdgeForge repo root, submit computed JSON.", "Empty {} fails. PASS string raises."),
        "DATA_VIZ_BI": ("From the Civic Metrics Studio folder, submit fixture JSON.", "Wrong rates/joins fail. No piracy."),
        "CLOUD_DEVOPS": ("From the ForgeCloud folder, submit policy/math JSON.", "World-writable keys and heroics fail."),
    }
    how, empty = hooks[course_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "", "## Student artifact", empty,
        "A file whose entire body is PASS is rejected by _fail_if_print_pass.", "", "## How to run", how,
        "```", f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --empty", "```", "", spec["wrong_hint"], "",
    ])


def instructor_week_notes_003(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    titles = {"AI_ML_EDGE": "EdgeForge", "DATA_VIZ_BI": "Civic Metrics Studio", "CLOUD_DEVOPS": "ForgeCloud"}
    return (
        f"# {titles[course_id]} — instructor week {n}\n\n"
        f"**Live number/example:** {week['worked_example']}\n\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\n\n"
        f"Refuse dumps. Point at curriculum/alignment/{course_id.lower()}_alignment.json.\n"
        f"AI policy: see course.ai_use_policy in course.json.\n"
    )


def presentation_003(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\n\n"
        f"## Slide 1 — Hook\n{week['title']}\n\n"
        f"## Slide 2 — Worked example\n{week['worked_example']}\n\n"
        f"## Slide 3 — Lab contract\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\n\n"
        f"## Speaker notes\nStay in {course_id} vocabulary. Do not noun-swap another academy's deck.\n"
        f"Assignment: {week['assignment'][:180]}...\n"
    )


def instructor_packet_003(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\n\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\n"
        f"- AI policy modes: EXPLAIN/HINT/QUESTION_ME/DEBUG_WITH_ME/REVIEW_MY_WORK/COMPARE_APPROACHES/PRACTICE\n"
        f"- Assessment modes: AI_ALLOWED / AI_RESTRICTED / AI_DISCLOSED / NO_AI\n"
        f"- Do not claim vendor certs or physical completion without evidence\n"
        f"- Public pages ≠ free to copy\n"
    )


def student_packet_003(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\n\n{hook}\n\n"
        "You submit lab JSON you computed. You will not receive answer keys. "
        "Empty submissions fail. A file containing only PASS is rejected.\n"
    )


def group_project_003(course_id: str, title: str, assignment: str) -> str:
    extras = {
        "AI_ML_EDGE": "Deliver metrics JSON + digest-pinned score + redacted RAG note. No biometric claims.",
        "DATA_VIZ_BI": "Deliver cleaned hash + three-tile dashboard + numbered board sentence. No gallery theft.",
        "CLOUD_DEVOPS": "Deliver perms/CI/SLO/rollback/probes + RB-FC-rollback timeline. No heroics, no cert claims.",
    }
    return f"# Group project — {title}\n\n{assignment}\n\n{extras[course_id]}\n"


def portfolio_003(course_id: str) -> str:
    texts = {
        "AI_ML_EDGE": "# Portfolio — EdgeForge\n\nShip split/metrics/score/budget/RAG JSON. PHYSICAL_PENDING stays labeled. No MLA claim.\n",
        "DATA_VIZ_BI": "# Portfolio — Civic Metrics Studio\n\nShip csv_sha256, quality gates, KPI story. No PL-300/Tableau claim.\n",
        "CLOUD_DEVOPS": "# Portfolio — ForgeCloud\n\nShip perms/CI/SLO/rollback/probes/incident JSON. No CKA/AWS claim.\n",
    }
    return texts[course_id]
