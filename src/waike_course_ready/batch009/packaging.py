"""Course-specific packaging for batch009 — CYBER_SOC, DIGITAL_CONFIDENCE, IT_SUPPORT_HARDWARE, NETWORKING_INFRA."""
from __future__ import annotations

from typing import Any

from waike_course_ready.batch009.content import BATCH_COURSE_IDS
from waike_course_ready.batch009.labs import LAB_SPECS_009

SOC, DCO, ISH, NIF = "CYBER_SOC", "DIGITAL_CONFIDENCE", "IT_SUPPORT_HARDWARE", "NETWORKING_INFRA"

SYLLABUS_ASSESSMENT_009 = {
    SOC: (
        "Night Shift Desk grading: weekly SOC quizzes on log reading, windowed rules, precision and recall, "
        "indicator hygiene, ATT&CK mapping, DMARC alignment, CVSS v3.1, queue order, and shift metrics; a "
        "20-item midterm on detection arithmetic; a 24-item final on triage judgement and handoff; ten "
        "recomputing desk labs; a written shift handoff reviewed by the incoming analyst."
    ),
    DCO: (
        "Library Lab grading: weekly checks on file paths, storage units, passphrase entropy, link reading, "
        "spreadsheet formulas, typing speed, attachment limits, 3-2-1 backups, colour contrast, and a personal "
        "safety plan; a 20-item midterm on everyday computer arithmetic; a 24-item final on safe operator "
        "habits; ten recomputing practice labs; a portfolio a patron could follow."
    ),
    ISH: (
        "Refurb Bench grading: weekly checks on power budgets, memory channels, RAID, partition schemes, fault "
        "isolation, display bandwidth, UPS runtime, imaging time, and sanitization; a 20-item midterm on bench "
        "arithmetic; a 24-item final on diagnosis and data-handling judgement; ten recomputing bench labs; a "
        "per-device service report with sanitization proof."
    ),
    NIF: (
        "Backbone Room grading: weekly checks on fiber latency, IPv6 text, bandwidth-delay product, BGP path "
        "choice, DNS TTL planning, CDN offload, optical budgets, availability, and 95th-percentile billing; a "
        "20-item midterm on infrastructure arithmetic; a 24-item final on design trade-offs; ten recomputing "
        "change-request labs; a design packet built only from documentation numbers."
    ),
}

SYLLABUS_DURATION_009 = {
    SOC: "Ten desk weeks at 6–8 hours each, one simulated overnight queue per week. Weeks 3 (precision and recall) and 7 (CVSS by hand) are NO_AI.",
    DCO: "Ten library sessions at 4–6 hours each, paced for adults returning to computers. Weeks 2 (storage units) and 6 (typing) are NO_AI.",
    ISH: "Ten bench weeks at 6–8 hours each with a donated machine on the bench. Weeks 3 (RAID table) and 9 (sanitization) are NO_AI.",
    NIF: "Ten change-request weeks at 6–8 hours each, paper first then spreadsheet. Weeks 7 (optical budget) and 9 (transit bill) are NO_AI.",
}

SYLLABUS_CLAIM_009 = {
    SOC: (
        "MITRE ATT&CK, FIRST CVSS v3.1, NIST SP 800-61r2, and RFC 7489 are PUBLIC_REFERENCE_ONLY. Synthetic logs "
        "and documentation IP ranges only; defensive practice, no live targets. Not a SOC certification. "
        "COURSE_DIGITAL_RC only, not REAL_STUDENT_E6 or REAL_TEACHER_E6."
    ),
    DCO: (
        "NIST SP 800-63B, W3C WCAG 2.2, and CISA Secure Our World are PUBLIC_REFERENCE_ONLY. Practice files and "
        "made-up accounts only; no patron data. Not a digital-literacy certificate. COURSE_DIGITAL_RC only, not "
        "REAL_STUDENT_E6 or REAL_TEACHER_E6."
    ),
    ISH: (
        "CompTIA A+ objective labels, NIST SP 800-88r1, and the UEFI specification are PUBLIC_REFERENCE_ONLY; no "
        "exam items. Donor data is never opened. Not A+ certification or a manufacturer warranty authority. "
        "COURSE_DIGITAL_RC only, not REAL_STUDENT_E6 or REAL_TEACHER_E6."
    ),
    NIF: (
        "IETF RFCs 4271, 5952, 7323, and 1034 and Cisco CCNA labels are PUBLIC_REFERENCE_ONLY. Documentation ASNs "
        "and the 2001:db8::/32 prefix only; no production peering claim. COURSE_DIGITAL_RC only, not "
        "REAL_STUDENT_E6 or REAL_TEACHER_E6."
    ),
}

PITFALLS_009 = {
    SOC: {
        1: "Counting failures per source and missing the success that follows them.",
        2: "Sliding the window by event instead of by time, so bursts split across buckets.",
        3: "Quoting accuracy on an imbalanced alert set instead of precision and recall.",
        4: "Pasting a live indicator into chat instead of the defanged form.",
        5: "Mapping a phishing email straight to ransomware without the intermediate techniques.",
        6: "Treating a subdomain sender as misaligned under relaxed DMARC.",
        7: "Rounding the CVSS base score to nearest instead of the specification's Roundup.",
        8: "Sorting the queue by arrival time when a critical alert sits behind low ones.",
        9: "Averaging MTTR across open tickets that have no resolution time.",
        10: "A handoff that lists alerts but not what the incoming analyst should do first.",
    },
    DCO: {
        1: "Resolving .. against the wrong folder, so the path lands in someone else's home.",
        2: "Mixing gigabytes and gibibytes when checking whether a file fits.",
        3: "Calling a long password strong when it is a dictionary word plus digits.",
        4: "Reading the left end of a link instead of the registered domain before the first slash.",
        5: "Typing a total by hand instead of a SUM formula, so edits do not propagate.",
        6: "Reporting gross speed and ignoring the error penalty.",
        7: "Forgetting attachments grow about a third when encoded for email.",
        8: "Two copies on the same laptop counted as two backups.",
        9: "Grey-on-white text that looks fine on one screen but fails 4.5:1.",
        10: "A safety plan that lists apps but not who to call when something goes wrong.",
    },
    ISH: {
        1: "Choosing the supply from the old unit's label instead of the new parts list.",
        2: "Two sticks on the same channel letter; firmware shows single-channel.",
        3: "Calling RAID a backup, or crediting RAID 10 with two guaranteed failures.",
        4: "Converting MBR to GPT before the data is copied off.",
        5: "Replacing the motherboard before reseating memory.",
        6: "Promising 4K 60 Hz over an HDMI 1.4 port because the cable is new.",
        7: "Ignoring inverter efficiency, so runtime is overstated.",
        8: "Forgetting bytes-to-bits, so imaging looks eight times faster.",
        9: "Overwriting an SSD's visible space and calling it Purge.",
        10: "A service report that says fixed it with no fault class or sanitization proof.",
    },
    NIF: {
        1: "Using the vacuum speed of light or the straight-line map distance.",
        2: "Collapsing the second zero run, or using :: for a single zero group.",
        3: "Leaving RTT in milliseconds or the rate in bits when computing BDP bytes.",
        4: "Picking the shortest AS_PATH before comparing local preference.",
        5: "Assuming a DNS change is live when the zone file is saved.",
        6: "Multiplying by the hit ratio instead of the miss ratio.",
        7: "Counting fiber loss only and forgetting connectors and splices.",
        8: "Treating a redundant pair as serial, or adding availabilities.",
        9: "Billing the peak sample or the mean instead of the 95th percentile.",
        10: "A real company's ASN or prefix in the design packet.",
    },
}

_RUBRICS: dict[str, list[tuple[str, str, list[tuple[str, int, str]]]]] = {
    SOC: [
        ("lab", "Desk lab recompute", [("recomputed", 45, "Counts, rates, and scores match the grader's recomputation"), ("defanged", 25, "Indicators appear only in defanged form"), ("rejects_stub", 30, "Empty and PASS-only submissions are refused")]),
        ("assignment", "SOC ticket write-up", [("ticket_ref", 35, "Cites the SOC ticket and the log lines used"), ("verdict", 35, "States escalate, close, or watch with a reason"), ("ai_mode", 30, "AI mode disclosed; NO_AI weeks hand-worked")]),
        ("quiz", "Weekly desk check", [("analyst_fit", 50, "Stems test the week's detection calculation"), ("key_custody", 50, "Answer key stays in the instructor tree")]),
        ("mid", "Midterm: detection arithmetic", [("new_scenarios", 60, "Twenty items on logs not used in weekly quizzes"), ("rates", 40, "Precision, recall, and window counts")]),
        ("final-knowledge", "Final: triage judgement", [("new_scenarios", 50, "Twenty-four items beyond weekly stems"), ("restraint", 50, "Defensive scope and evidence before escalation")]),
        ("practical", "Practical: live queue drill", [("queue_order", 50, "Critical alerts handled before low ones"), ("altered_inputs", 50, "Changed log lines change the result")]),
        ("project", "Shift handoff", [("labs_passed", 30, "Six or more desk labs passed"), ("open_items", 40, "Every open alert has an owner and next action"), ("metrics", 30, "MTTD and MTTR computed from closed tickets only")]),
        ("portfolio", "Analyst portfolio", [("tuned_rule", 40, "One rule tuned with before-and-after precision"), ("cvss_trace", 30, "One CVSS vector scored by hand"), ("roles", 30, "Tier-1 trainee roles; no certification implied")]),
    ],
    DCO: [
        ("lab", "Library practice lab", [("recomputed", 45, "Paths, sizes, and scores match the recomputation"), ("plain_language", 25, "Explains the answer in a sentence a patron understands"), ("rejects_stub", 30, "Empty and PASS-only submissions are refused")]),
        ("assignment", "DCO task sheet", [("task_ref", 35, "Names the DCO task and the practice file"), ("steps", 35, "Lists the clicks or keystrokes in order"), ("ai_mode", 30, "AI mode disclosed; NO_AI weeks done alone")]),
        ("quiz", "Weekly confidence check", [("everyday_fit", 50, "Stems use situations from the library lab"), ("key_custody", 50, "Answer key kept by the instructor")]),
        ("mid", "Midterm: everyday arithmetic", [("new_situations", 60, "Twenty items unlike weekly quiz stems"), ("units", 40, "Bytes, gibibytes, entropy bits, and speeds")]),
        ("final-knowledge", "Final: safe operator habits", [("new_situations", 50, "Twenty-four items beyond weekly stems"), ("safety", 50, "Links, passwords, backups, and asking for help")]),
        ("practical", "Practical: help a patron", [("walkthrough", 50, "Guides a peer through one task without taking the mouse"), ("altered_inputs", 50, "Changed file sizes change the answer")]),
        ("project", "Personal safety plan", [("labs_passed", 30, "Six or more practice labs passed"), ("contacts", 40, "Names who to call and how to reach them"), ("backups", 30, "Shows a 3-2-1 plan with real locations")]),
        ("portfolio", "Operator portfolio", [("before_after", 40, "Typing and task times from week one and week ten"), ("accessibility", 30, "One document checked for contrast"), ("roles", 30, "Entry operator roles; no certificate implied")]),
    ],
    ISH: [
        ("lab", "Bench lab recompute", [("recomputed", 45, "Watts, bandwidths, and capacities match the recomputation"), ("safety", 25, "Electrical and data-handling safety noted"), ("rejects_stub", 30, "Empty and PASS-only submissions are refused")]),
        ("assignment", "ISH work order", [("order_ref", 35, "Names the work order and machine serial"), ("evidence", 35, "Photo or reading supporting the decision"), ("ai_mode", 30, "AI mode disclosed; NO_AI weeks hand-worked")]),
        ("quiz", "Weekly bench check", [("bench_fit", 50, "Stems use the week's machine and numbers"), ("key_custody", 50, "Answer key kept by the bench lead")]),
        ("mid", "Midterm: bench arithmetic", [("new_machines", 60, "Twenty items on machines not used weekly"), ("units", 40, "Watts, GB/s, TB, Gbit/s, and minutes")]),
        ("final-knowledge", "Final: diagnosis and data handling", [("new_machines", 50, "Twenty-four items beyond weekly stems"), ("privacy", 50, "Sanitization and donor-data restraint")]),
        ("practical", "Practical: timed fault drill", [("isolation", 50, "Names the failing stage before replacing parts"), ("altered_inputs", 50, "Changed parts lists change the result")]),
        ("project", "Service report batch", [("labs_passed", 30, "Six or more bench labs passed"), ("per_device", 40, "Fault, fix, and sanitization recorded per machine"), ("no_retention", 30, "customer_data_retained false")]),
        ("portfolio", "Technician portfolio", [("refurbs", 40, "Two refurbished machines documented end to end"), ("certificate", 30, "One sanitization certificate with method and serial"), ("roles", 30, "Entry technician roles; no A+ implied")]),
    ],
    NIF: [
        ("lab", "Change-request lab recompute", [("recomputed", 45, "Delays, windows, and budgets match the recomputation"), ("documentation_numbers", 25, "Only documentation ASNs and prefixes"), ("rejects_stub", 30, "Empty and PASS-only submissions are refused")]),
        ("assignment", "NIF change request", [("request_ref", 35, "Names the change request and its inputs"), ("risk", 35, "States the risk and the rollback"), ("ai_mode", 30, "AI mode disclosed; NO_AI weeks on paper")]),
        ("quiz", "Weekly backbone check", [("infra_fit", 50, "Stems use the week's link or protocol"), ("key_custody", 50, "Answer key kept by the instructor")]),
        ("mid", "Midterm: infrastructure arithmetic", [("new_links", 60, "Twenty items on links not used weekly"), ("units", 40, "ms, bytes, dB, and availability")]),
        ("final-knowledge", "Final: design trade-offs", [("new_links", 50, "Twenty-four items beyond weekly stems"), ("judgement", 50, "Chooses the change that moves the weakest link")]),
        ("practical", "Practical: whiteboard derivation", [("derive", 50, "Derives one packet number from its inputs"), ("altered_inputs", 50, "Changed distances or ratios change the result")]),
        ("project", "Backbone design packet", [("labs_passed", 30, "Six or more change-request labs passed"), ("recomputed", 40, "Latency, availability, and margin recomputed"), ("no_peering_claim", 30, "production_peering_claim false")]),
        ("portfolio", "NOC trainee portfolio", [("runbook", 40, "One cutover runbook with TTL timeline"), ("bill_check", 30, "One transit bill checked against samples"), ("roles", 30, "NOC trainee roles; no CCNA implied")]),
    ],
}

_LAB_RUN = {
    SOC: "Run it at the desk, then swap one log line and confirm the verdict changes:",
    DCO: "Try it, then change one number in your file and check that the answer moves:",
    ISH: "Grade it on the bench, then alter one part's rating and watch the grader disagree:",
    NIF: "Submit the change request, then edit one input and confirm the recomputation follows:",
}

_NOTES = {
    SOC: ("Shift-lead notes", "Desk drill", "replay {lab} against a log with one line changed"),
    DCO: ("Facilitator notes", "Patron practice", "pair learners and have one explain {lab} aloud to the other"),
    ISH: ("Bench-lead notes", "Hands on the case", "have each technician run {lab} against the machine on their bench"),
    NIF: ("NOC mentor notes", "Whiteboard", "ask one trainee to derive {lab} from its inputs before checking"),
}

_SLIDES = {SOC: "Night Shift", DCO: "Library Lab", ISH: "Refurb Bench", NIF: "Backbone Room"}

_PACKETS = {
    SOC: ("Shift-lead packet", "Keys live in instructor/answer_keys.json. In week ten the incoming analyst grades each handoff."),
    DCO: ("Facilitator packet", "Keys live in instructor/answer_keys.json. Keep pace gentle; repeat a session rather than rush."),
    ISH: ("Bench-lead packet", "Keys live in instructor/answer_keys.json. Inspect one sanitization certificate per technician."),
    NIF: ("NOC mentor packet", "Keys live in instructor/answer_keys.json. Reject any packet with real ASNs or prefixes."),
}

_STUDENT = {
    SOC: "Keep a desk notebook: every verdict needs the log lines that support it.",
    DCO: "Keep a practice folder and write one sentence after each session about what felt easier.",
    ISH: "Keep a bench log per machine: serial, fault, fix, and sanitization.",
    NIF: "Keep a change log: inputs, numbers, and the RFC each decision relies on.",
}

_PROJECT = {SOC: "Shift handoff", DCO: "Personal safety plan", ISH: "Refurb service report", NIF: "Backbone design packet"}

_PORTFOLIO = {
    SOC: "One tuned rule with before-and-after precision, one hand-scored CVSS vector, and a reviewed shift handoff.",
    DCO: "Week-one and week-ten typing and task times, one contrast-checked document, and a 3-2-1 backup plan.",
    ISH: "Two refurbished machines documented end to end and one sanitization certificate.",
    NIF: "A DNS cutover runbook, a checked transit bill, and the backbone design packet.",
}


def rubrics_009(course_id: str) -> list[dict[str, Any]]:
    return [
        {"rubric_id": f"{course_id}-{suffix}", "title": title, "criteria": [
            {"name": name, "weight": weight, "desc": desc} for name, weight, desc in criteria
        ]}
        for suffix, title, criteria in _RUBRICS[course_id]
    ]


def lab_readme_009(course_id: str, lab_id: str) -> str:
    spec = LAB_SPECS_009[lab_id]
    return "\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "",
        _LAB_RUN[course_id], "",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        "", f"Common miss: {spec['wrong_hint']}", "",
    ])


def instructor_week_notes_009(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    head, drill, task = _NOTES[course_id]
    return (
        f"# {course_id} — {head}, week {n}\n\n"
        f"**Board work:** {week['worked_example']}\n\n"
        f"**{drill}:** {task.format(lab=week['lab_id'])}.\n\n"
        f"**Watch for:** {PITFALLS_009[course_id][n]}\n"
    )


def presentation_009(course_id: str, week: dict[str, Any]) -> str:
    return f"# {_SLIDES[course_id]} {week['week']}: {week['title']}\n\nOn the board: {week['worked_example']}\n"


def instructor_packet_009(course_id: str) -> str:
    title, body = _PACKETS[course_id]
    return f"# {title} — {course_id}\n\n{body}\n"


def student_packet_009(course_id: str, hook: str) -> str:
    return f"# Learner packet — {course_id}\n\n{hook}\n\n{_STUDENT[course_id]}\n"


def group_project_009(course_id: str, title: str, assignment: str) -> str:
    return f"# {_PROJECT[course_id]} — {course_id}\n\n## {title}\n\n{assignment}\n"


def portfolio_009(course_id: str) -> str:
    return f"# Portfolio — {course_id}\n\n{_PORTFOLIO[course_id]}\n"


# The product packaging dispatch keys on these dicts, so they list only tracks on the product path.
for _table in (SYLLABUS_ASSESSMENT_009, SYLLABUS_DURATION_009, SYLLABUS_CLAIM_009):
    for _cid in [c for c in _table if c not in BATCH_COURSE_IDS]:
        del _table[_cid]
