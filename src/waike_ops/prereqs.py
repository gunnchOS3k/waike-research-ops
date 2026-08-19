"""Authored digital-RC prerequisites. Counts follow COURSES on disk, not slogans."""
from __future__ import annotations

COURSE_PREREQS: dict[str, dict[str, list[str] | str]] = {
    "GENERAL_IT": {
        "course_id": "GENERAL_IT",
        "required": [
            "Willingness to keep patron PII, passwords, and SSNs out of ticket notes"
        ],
        "recommended": [],
    },
    "COMPUTER_NETWORKING": {
        "course_id": "COMPUTER_NETWORKING",
        "required": [
            "Can follow a numbered ticket journal without storing credentials"
        ],
        "recommended": ["GENERAL_IT Civic Tech Desk operator habits"],
    },
    "CYBERSECURITY": {
        "course_id": "CYBERSECURITY",
        "required": [
            "Authorized-fixture-only rule: do not scan or exploit systems you do not own",
            "Ticket-journal discipline without PII",
        ],
        "recommended": ["COMPUTER_NETWORKING name-resolution and port literacy"],
    },
    "SOFTWARE_BUILDER": {
        "course_id": "SOFTWARE_BUILDER",
        "required": [
            "Can edit a text file and run a local command",
            "Will not commit secrets or paste PASS as a lab artifact",
        ],
        "recommended": ["GENERAL_IT folder and ticket habits"],
    },
    "HARDWARE_ENGINEERING": {
        "course_id": "HARDWARE_ENGINEERING",
        "required": [
            "Can submit lab JSON and treat Device Lab benches as digital-first unless EVT is in scope"
        ],
        "recommended": ["GENERAL_IT power/storage triage order"],
    },
    "PM_AGILE_LSS": {
        "course_id": "PM_AGILE_LSS",
        "required": [
            "Willingness to charter fixture wait problems — do not invent community outcome numbers"
        ],
        "recommended": ["GENERAL_IT desk operations vocabulary"],
    },
    "AI_ML_EDGE": {
        "course_id": "AI_ML_EDGE",
        "required": [
            "Comfort reading CSV/tables",
            "Will not treat classroom models as production autonomy",
        ],
        "recommended": ["SOFTWARE_BUILDER local command fluency"],
    },
    "DATA_VIZ_BI": {
        "course_id": "DATA_VIZ_BI",
        "required": [
            "Comfort with tables/CSV",
            "Will not decorate charts in place of labeled encodings",
        ],
        "recommended": ["GENERAL_IT operator literacy"],
    },
    "CLOUD_DEVOPS": {
        "course_id": "CLOUD_DEVOPS",
        "required": [
            "Willingness to learn Linux permissions in week 1 from zero if needed",
            "No plaintext tokens in submitted artifacts",
        ],
        "recommended": ["SOFTWARE_BUILDER git/CI vocabulary"],
    },
    "WIRELESS_6G": {
        "course_id": "WIRELESS_6G",
        "required": [
            "Algebra for FSPL (distance, frequency, dB)",
            "Accept that commercial standardized 6G does not exist today",
        ],
        "recommended": ["COMPUTER_NETWORKING local naming and delay honesty"],
    },
    "ROBOTICS_CONTROL": {
        "course_id": "ROBOTICS_CONTROL",
        "required": [
            "Treat e-stop / safe-state as non-negotiable in every lab",
            "Digital-first: physical robot motion is out of scope unless EVT is scheduled",
        ],
        "recommended": ["HARDWARE_ENGINEERING GPIO/I2C vocabulary"],
    },
    "GAME_DEV_INTERACTIVE": {
        "course_id": "GAME_DEV_INTERACTIVE",
        "required": [
            "Can name a game loop, input event, and finite state without claiming a shipped title"
        ],
        "recommended": ["SOFTWARE_BUILDER git and automated-test habits"],
    },
    "COMM_PD_ETHICS": {
        "course_id": "COMM_PD_ETHICS",
        "required": [
            "Digital literacy for ticket journals",
            "Willingness to recuse on conflict",
        ],
        "recommended": ["GENERAL_IT desk culture exposure"],
    },
    "DATA_DASHBOARDS": {
        "course_id": "DATA_DASHBOARDS",
        "required": [
            "Comfort with tables/CSV",
            "Willingness to compute KPIs by hand when asked",
        ],
        "recommended": ["DATA_VIZ_BI visual literacy (complementary, not a substitute)"],
    },
    "EMBEDDED_PROTOTYPING": {
        "course_id": "EMBEDDED_PROTOTYPING",
        "required": [
            "Treat Zephyr/QEMU as digital-first; PHYSICAL_PENDING for solder/OTA without EVT",
            "Submit lab JSON — empty/wrong/print-PASS fail",
        ],
        "recommended": ["HARDWARE_ENGINEERING SPICE/GPIO vocabulary"],
    },
    "GUNNCHOS_PRODUCT_LAB": {
        "course_id": "GUNNCHOS_PRODUCT_LAB",
        "required": [
            "Accepted-main SHA pins only — no preview SHA in accepted-main claims",
            "Do not open or merge device-os #103 from student labs",
        ],
        "recommended": ["SOFTWARE_BUILDER compose/deploy vocabulary", "GENERAL_IT ticket discipline"],
    },
}
