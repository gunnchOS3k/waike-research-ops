"""Course-specific syllabus, rubrics, lab READMEs, instructor notes — not emit.py clones."""
from __future__ import annotations

from typing import Any

from waike_course_ready.labs import COURSE_LABS, LAB_SPECS
from waike_course_ready.batch002.packaging import (
    SYLLABUS_ASSESSMENT_002, SYLLABUS_CLAIM_002, SYLLABUS_DURATION_002,
    rubrics_002, lab_readme_002, instructor_week_notes_002, presentation_002,
    instructor_packet_002, student_packet_002, group_project_002, portfolio_002,
)
from waike_course_ready.batch003.packaging import (
    SYLLABUS_ASSESSMENT_003, SYLLABUS_CLAIM_003, SYLLABUS_DURATION_003,
    rubrics_003, lab_readme_003, instructor_week_notes_003, presentation_003,
    instructor_packet_003, student_packet_003, group_project_003, portfolio_003,
)

SYLLABUS_ASSESSMENT = {
    **SYLLABUS_ASSESSMENT_003,
    **SYLLABUS_ASSESSMENT_002,
    "GENERAL_IT": (
        "Civic Tech Desk assessment mix: weekly operator quizzes (ticket 4417/4502 numbers, "
        "not vendor stems), a mid-course desk audit (20 original items on accounts/storage/"
        "change windows), a final knowledge set (24 original items on hardware/DNS/services/"
        "after-hours), a practical that requires submitted user/service/backup JSON, and a "
        "two-person after-hours rotation whose recorder notes a stranger can continue. "
        "Reboot-and-hope scores zero on every ticket rubric."
    ),
    "COMPUTER_NETWORKING": (
        "Packet Range assessment mix: weekly protocol quizzes, a mid-course written exam on "
        "encapsulation/CIDR/LPM/TCP numbering (20 original items), a final on STP/SPF/NAT/ACL/"
        "intent files (24 original items), a practical that parses a crafted Ethernet+IPv4 "
        "frame and must drop a real TTL=1 header, and a guest-VLAN redesign presentation. "
        "A trace that omits VLAN, LPM, TTL, or ACL is incomplete."
    ),
    "CYBERSECURITY": (
        "Harbor SOC assessment mix: weekly ops quizzes, a mid-course on upcoming ISC2 CC "
        "2026-09-01 domains in WAIKE words (20 original items), a final on hardening/IR/"
        "toy-parser/forensics (24 original items), a practical over seven fixture labs that "
        "reject empty submissions, and an evidence-locker design checkpoint before the "
        "policy checker. Burst notes that say 'attacker' fail. Scanning hosts you do not "
        "own fails the course, not just the lab."
    ),
}

SYLLABUS_DURATION = {
    **SYLLABUS_DURATION_003,
    **SYLLABUS_DURATION_002,
    "GENERAL_IT": (
        "Ten public-desk weeks (about 6–8 hours/week including Saturday volunteer shadow). "
        "Not a two-hour 'computers' workshop. Dual-boot kiosk time is scheduled; do not "
        "patch both images in the same hour."
    ),
    "COMPUTER_NETWORKING": (
        "Ten Packet Range weeks with one deep data-path practical in week 4 that returns in "
        "the capstone. Budget a quiet table for hex slicing; this is not a GUI click-through."
    ),
    "CYBERSECURITY": (
        "Ten Harbor SOC weeks. Week 8 is the only vulnerability lab and it stays on the "
        "length-prefixed toy parser. Do not schedule 'scan the campus' as homework."
    ),
}

SYLLABUS_CLAIM = {
    **SYLLABUS_CLAIM_003,
    **SYLLABUS_CLAIM_002,
    "GENERAL_IT": (
        "Aligns to Google IT Support themes and CompTIA A+ V15 220-1201/1202 domain names. "
        "Does not grant those credentials. Instructor keys stay out of the learner packet."
    ),
    "COMPUTER_NETWORKING": (
        "Aligns to Cisco CCNA 200-301 v1.1 domain weights and cites CS144's weekly shape. "
        "Does not grant CCNA and does not ship Stanford code or solutions. Instructor keys "
        "stay out of the learner packet."
    ),
    "CYBERSECURITY": (
        "Prefers ISC2 CC outline effective 2026-09-01; dual-maps current CC and Security+ "
        "SY0-701; cites CS161 project-depth pattern only. No item harvests. Instructor keys "
        "stay out of the learner packet."
    ),
}


def rubrics(course_id: str) -> list[dict[str, Any]]:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return rubrics_003(course_id)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return rubrics_002(course_id)
    if course_id == "GENERAL_IT":
        return [
            {"rubric_id": "GENERAL_IT-lab", "title": "Civic desk lab", "criteria": [
                {"name": "kiosk_least_privilege", "weight": 25, "desc": "kiosk not in sudo/root; unique UID/home"},
                {"name": "restore_hash", "weight": 25, "desc": "SHA256 of restored civic tree matches source; no ssn.txt"},
                {"name": "ticket_next_action", "weight": 25, "desc": "reboot_and_hope scores zero; 4417/4418/4419 next-actions match"},
                {"name": "change_window", "weight": 25, "desc": "snapshot before apply; planned time inside 18:00–21:00"},
            ]},
            {"rubric_id": "GENERAL_IT-assignment", "title": "Desk journal", "criteria": [
                {"name": "named_ticket", "weight": 40, "desc": "Uses 4417/4502/CHG-88 numbers, not 'a user had an issue'"},
                {"name": "no_pii", "weight": 30, "desc": "No PAN/password/SSN in the journal"},
                {"name": "next_shift", "weight": 30, "desc": "A Saturday volunteer can continue without asking you"},
            ]},
            {"rubric_id": "GENERAL_IT-quiz", "title": "Operator knowledge", "criteria": [
                {"name": "desk_numbers", "weight": 50, "desc": "1200s, 10.20.30.14, 15% free — not vendor stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys only in instructor/answer_keys.json"},
            ]},
            {"rubric_id": "GENERAL_IT-mid", "title": "Mid-course desk audit", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 items not cloned from weekly quizzes"},
                {"name": "accounts_storage_change", "weight": 40, "desc": "UID clone, free-ratio, window math"},
            ]},
            {"rubric_id": "GENERAL_IT-final-knowledge", "title": "Final operator knowledge", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 items not cloned from weekly quizzes"},
                {"name": "hardware_dns_services", "weight": 50, "desc": "Power-first triage, split horizon, cups restart budget"},
            ]},
            {"rubric_id": "GENERAL_IT-practical", "title": "Submitted desk artifacts", "criteria": [
                {"name": "student_json", "weight": 50, "desc": "Empty submission fails; reference JSON passes"},
                {"name": "negatives", "weight": 30, "desc": "kiosk-with-sudo fails the user lab"},
                {"name": "print_pass", "weight": 20, "desc": "A file containing only PASS is rejected"},
            ]},
            {"rubric_id": "GENERAL_IT-project", "title": "After-hours rotation", "criteria": [
                {"name": "two_roles", "weight": 30, "desc": "Operator and recorder swap at 30 minutes"},
                {"name": "stranger_handoff", "weight": 40, "desc": "Recorder notes do not require the operator's memory"},
                {"name": "scope", "weight": 30, "desc": "No imaging of neighborhood laptops"},
            ]},
            {"rubric_id": "GENERAL_IT-portfolio", "title": "Desk portfolio", "criteria": [
                {"name": "tree_and_hash", "weight": 50, "desc": "Folder tree + restore hash"},
                {"name": "chg88", "weight": 30, "desc": "Change record with window"},
                {"name": "no_faces", "weight": 20, "desc": "Tour video without patron faces"},
            ]},
        ]
    if course_id == "COMPUTER_NETWORKING":
        return [
            {"rubric_id": "COMPUTER_NETWORKING-lab", "title": "Packet Range lab", "criteria": [
                {"name": "datapath_parse", "weight": 30, "desc": "Student reports TTL from bytes 14+8, not a hardcoded 4"},
                {"name": "ttl1_drop", "weight": 25, "desc": "A crafted TTL=1 header decrements to 0 and is not forwarded"},
                {"name": "lpm", "weight": 25, "desc": "/24 beats /16; /32 steals the host"},
                {"name": "acl_order", "weight": 20, "desc": "deny tcp/23 before permit 443 before deny *"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-assignment", "title": "Hex and graph work", "criteria": [
                {"name": "sliced_frame", "weight": 40, "desc": "Paper slice of MAC/ethertype/IHL/TTL/proto/src/dst"},
                {"name": "spf_recompute", "weight": 30, "desc": "Changing B-D to 20 flips A→D to A-C-D"},
                {"name": "no_vendor_gui", "weight": 30, "desc": "No stolen Packet Tracer / exam-sim screenshots"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-quiz", "title": "Protocol knowledge", "criteria": [
                {"name": "range_numbers", "weight": 50, "desc": "10.20.30.0/26, seq/ACK, 5-tuple — original stems"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys only in instructor/answer_keys.json"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-mid", "title": "Mid-course path exam", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 items not weekly clones"},
                {"name": "encap_cidr_tcp", "weight": 40, "desc": "MTU chop, LPM, ACK arithmetic"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-final-knowledge", "title": "Final edge exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 items not weekly clones"},
                {"name": "stp_spf_acl", "weight": 50, "desc": "BPDU guard, SPF cost 4 vs 10, telnet deny"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-practical", "title": "Datapath practical", "criteria": [
                {"name": "student_parse", "weight": 40, "desc": "Empty parse JSON fails"},
                {"name": "ttl_header", "weight": 40, "desc": "TTL=1 uses the parsed header, not (1-1)==0"},
                {"name": "negatives", "weight": 20, "desc": "Wrong network address on /26 fails CIDR lab"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-project", "title": "Guest VLAN redesign", "criteria": [
                {"name": "intent_json", "weight": 40, "desc": "Prefixes, ACL, NAT, four-router costs"},
                {"name": "guest_isolated", "weight": 30, "desc": "Guest cannot reach Roof management"},
                {"name": "eight_minutes", "weight": 30, "desc": "Talk uses this topology, not a campus UPNOW slide clone"},
            ]},
            {"rubric_id": "COMPUTER_NETWORKING-portfolio", "title": "Path portfolio", "criteria": [
                {"name": "trace", "weight": 50, "desc": "One Pier→Roof trace naming VLAN/LPM/TTL/ACL"},
                {"name": "intent", "weight": 30, "desc": "Validator-rejected missing next-hop included as evidence"},
                {"name": "no_ccna_claim", "weight": 20, "desc": "Portfolio does not say 'I am CCNA'"},
            ]},
        ]
    if course_id == "CYBERSECURITY":
        return [
            {"rubric_id": "CYBERSECURITY-lab", "title": "Harbor fixture lab", "criteria": [
                {"name": "burst_note", "weight": 25, "desc": "Incident note contains burst, not attacker; empty note fails"},
                {"name": "bot_rbac", "weight": 25, "desc": "harbor-bot cannot close; bot-close fixture fails"},
                {"name": "toy_parser", "weight": 25, "desc": "Safe parser rejects oversize length; targets=[course_ctf_fixture]"},
                {"name": "ir_order", "weight": 25, "desc": "contain before eradicate; lessons last"},
            ]},
            {"rubric_id": "CYBERSECURITY-assignment", "title": "SOC memo", "criteria": [
                {"name": "named_identities", "weight": 40, "desc": "Naiya/Omar/harbor-bot, not 'a user'"},
                {"name": "no_secrets", "weight": 30, "desc": "No tokens or passwords in the memo"},
                {"name": "authorized_only", "weight": 30, "desc": "No scan of systems Harbor does not own"},
            ]},
            {"rubric_id": "CYBERSECURITY-quiz", "title": "SOC knowledge", "criteria": [
                {"name": "harbor_words", "weight": 50, "desc": "Original WAIKE stems; no ISC2/CompTIA item text"},
                {"name": "key_hidden", "weight": 50, "desc": "Keys only in instructor/answer_keys.json"},
            ]},
            {"rubric_id": "CYBERSECURITY-mid", "title": "Mid-course Harbor exam", "criteria": [
                {"name": "original_stems", "weight": 60, "desc": "20 items not weekly clones"},
                {"name": "cc_2026_domains", "weight": 40, "desc": "Principles/governance/IAM/zones/bursts in WAIKE words"},
            ]},
            {"rubric_id": "CYBERSECURITY-final-knowledge", "title": "Final Harbor exam", "criteria": [
                {"name": "original_stems", "weight": 50, "desc": "24 items not weekly clones"},
                {"name": "harden_ir_parser", "weight": 50, "desc": "Baseline flags, IR clock, length lie, USB timeline"},
            ]},
            {"rubric_id": "CYBERSECURITY-practical", "title": "Seven-lab practical", "criteria": [
                {"name": "empty_fails", "weight": 40, "desc": "Missing student JSON fails each lab"},
                {"name": "no_network", "weight": 30, "desc": "Socket opens during toy parser fail the lab"},
                {"name": "bot_negative", "weight": 30, "desc": "Bot with case.close fails IAM"},
            ]},
            {"rubric_id": "CYBERSECURITY-project", "title": "Evidence locker", "criteria": [
                {"name": "design_first", "weight": 40, "desc": "≤2 page design before the checker"},
                {"name": "pii_reject", "weight": 30, "desc": "password= fields rejected"},
                {"name": "bot_not_closer", "weight": 30, "desc": "harbor-bot cannot close locker cases"},
            ]},
            {"rubric_id": "CYBERSECURITY-portfolio", "title": "SOC portfolio", "criteria": [
                {"name": "seven_json", "weight": 50, "desc": "Seven lab results plus empty-fail evidence"},
                {"name": "cannot_claim", "weight": 30, "desc": "Timeline page lists what the USB fixture cannot prove"},
                {"name": "no_cert_claim", "weight": 20, "desc": "Does not claim ISC2 CC or Security+"},
            ]},
        ]
    raise KeyError(course_id)


def lab_readme(course_id: str, lab_id: str) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return lab_readme_003(course_id, lab_id)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return lab_readme_002(course_id, lab_id)
    spec = LAB_SPECS[lab_id]
    if course_id == "GENERAL_IT":
        how = (
            "From the Civic desk repo root, submit the operator JSON you actually filled in. "
            "Do not ask staff to run the reference store and call it yours."
        )
        empty = "An empty `{}` is a closed ticket with no work — it fails student_artifact."
    elif course_id == "COMPUTER_NETWORKING":
        how = (
            "From the Packet Range repo root, submit the parse/table JSON you computed. "
            "A GUI screenshot is not a validator input."
        )
        empty = "Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails."
    else:
        how = (
            "From the Harbor SOC repo root, submit fixture answers only. "
            "Do not point this lab at a host you do not own."
        )
        empty = "An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network."
    return "\n".join(
        [
            f"# {lab_id} — {spec['title']}",
            "",
            spec["readme"],
            "",
            "## Student artifact",
            f"Keys: `{', '.join(spec['required_keys'])}`.",
            empty,
            "A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.",
            "",
            "## How to run",
            how,
            "```",
            f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
            f"python3 scripts/run_course_labs.py --lab {lab_id} --empty",
            "```",
            "",
            spec["wrong_hint"],
            "",
        ]
    )


def instructor_week_notes(course_id: str, week: dict[str, Any]) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return instructor_week_notes_003(course_id, week)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return instructor_week_notes_002(course_id, week)
    n = week["week"]
    lab = week["lab_id"]
    if course_id == "GENERAL_IT":
        pitfall = {
            1: "Learners will disable the idle timer. Stop them; the timer is a shared-kiosk control.",
            2: "Do not let anyone format the camera card as the first move on a 4.7 GiB vanish.",
            3: "Watch for copied /etc/passwd lines that keep UID 1020.",
            4: "If they skip the restore hash, the .tgz is theater.",
            5: "reboot_and_hope is an automatic zero, even if the kiosk comes back.",
            6: "Do not open the spare SODIMM bag until power and cables are named.",
            7: "Guest Wi-Fi volunteers will gaslight DNS. Draw the horizon.",
            8: "If toy-tracker is active, stop the lesson and rewrite the image.",
            9: "Apply-then-snapshot is a souvenir. Make them reorder the JSON.",
            10: "Recorder notes that say 'ask me' fail the group project on the spot.",
        }[n]
        return (
            f"# Civic Tech Desk — instructor week {n}\n\n"
            f"**Live number:** work {week['worked_example']}\n\n"
            f"**Lab `{lab}`:** collect student JSON; do not run the golden path and call it theirs.\n\n"
            f"**Pitfall:** {pitfall}\n\n"
            "Refuse vendor item banks. Point at `curriculum/alignment/general_it_alignment.json`.\n"
        )
    if course_id == "COMPUTER_NETWORKING":
        pitfall = {
            1: "If they debug TCP checksums with a wrong dest MAC, rewind to sticky notes.",
            2: "Printer at .96 on a /28 is the most common off-by-lot error. Make them bitwise it.",
            3: "MAC-only tables leak VLANs. Force the tuple key on the board.",
            4: "Do not accept (1-1)==0 as a TTL story. Parse the TTL=1 frame.",
            5: "rwnd vs cwnd confusion: label receiver belly vs network belly.",
            6: "The loop postmortem needs a blocked port, not 'STP magic'.",
            7: "When you set B-D=20, wait until someone actually recomputes 10 vs 22.",
            8: "Ask which liar expired: DHCP, DNS TTL, or NAT pool.",
            9: "If permit ip any any is line 1, the ACL is wallpaper — fail it.",
            10: "Intent missing nh fails. Guest reaching Roof management fails.",
        }[n]
        return (
            f"# Packet Range — instructor week {n}\n\n"
            f"**Hex/graph on the board:** {week['worked_example']}\n\n"
            f"**Lab `{lab}`:** student must submit parse/table JSON. Empty fails.\n\n"
            f"**Pitfall:** {pitfall}\n\n"
            "No CS144 code, no CCNA dumps. Alignment JSON only.\n"
        )
    pitfall = {
        1: "If someone wants the bot to have sudo 'just to try,' that is the week's exam.",
        2: "Orphan intern accounts: make Omar print the binding table live.",
        3: "A volunteer trunking kiosk to staff for a label printer is a zone incident.",
        4: "Notes that say attacker fail. Burst is a look.",
        5: "ai_agent_sudo true is an automatic baseline fail.",
        6: "Stolen laptop: revoke before rewriting the matrix.",
        7: "Wipe-before-contain fails the clock. ASAP is not a timestamp.",
        8: "No sockets, no random IPs, no shellcode. Fixture only.",
        9: "Do not let them 'identify ada' from a USB fixture that has no identity.",
        10: "Design checkpoint before the checker. Scanning the WAN fails the capstone.",
    }[n]
    return (
        f"# Harbor SOC — instructor week {n}\n\n"
        f"**Tabletop beat:** {week['worked_example']}\n\n"
        f"**Lab `{lab}`:** fixture + student JSON. Empty note fails no_attacker_word.\n\n"
        f"**Pitfall:** {pitfall}\n\n"
        "No ISC2/CompTIA item text. Upcoming CC 2026-09-01 is a domain map, not a dump.\n"
    )


def presentation(course_id: str, week: dict[str, Any]) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return presentation_003(course_id, week)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return presentation_002(course_id, week)
    n = week["week"]
    if course_id == "GENERAL_IT":
        slide3 = "Put 1200 seconds, 15% free, and CHG window 18:00–21:00 on the board. Sit in silence until someone does the arithmetic."
        notes = "If they ask for A+ dumps, close the slide and open the alignment JSON. Keys never leave the instructor packet."
    elif course_id == "COMPUTER_NETWORKING":
        slide3 = "Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy."
        notes = "Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python."
    else:
        slide3 = "Write the Harbor note on the board: 'burst on ada' vs 'ada is the attacker'. Only the first passes."
        notes = "Week 8 is a toy parser. Anyone opening nmap on the campus /24 fails the course ethic, not just the lab."
    return "\n".join(
        [
            f"# Week {n} presentation — {week['title']}",
            "",
            "## Slide 1 — Cold open",
            week["worked_example"],
            "",
            "## Slide 2 — Teaching beat",
            week["lesson"].split("\n\n")[0],
            "",
            "## Slide 3 — Live work",
            slide3,
            "",
            "## Speaker notes",
            notes,
            "",
        ]
    )


def instructor_packet(course_id: str) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return instructor_packet_003(course_id)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return instructor_packet_002(course_id)
    if course_id == "GENERAL_IT":
        return (
            "# Instructor packet — Civic Tech Desk\n\n"
            "Keys: `instructor/answer_keys.json`. Never copy into learner ingest or slides.\n\n"
            "Collect student lab JSON. Running `run_course_labs.py` with no submission must fail; "
            "that is not their grade.\n\n"
            "Alignment: `curriculum/alignment/general_it_alignment.json` (Google IT Support themes, "
            "A+ V15 220-1201/1202 — not 1101/1102).\n"
        )
    if course_id == "COMPUTER_NETWORKING":
        return (
            "# Instructor packet — Packet Range\n\n"
            "Keys: `instructor/answer_keys.json`. Never copy into learner ingest or slides.\n\n"
            "Week 4 practical: require a student parse of the crafted frame and a TTL=1 drop "
            "from the header, not a tautology.\n\n"
            "Alignment: `curriculum/alignment/networking_alignment.json` (CCNA v1.1 weights, "
            "CS144 structure only).\n"
        )
    return (
        "# Instructor packet — Harbor SOC\n\n"
        "Keys: `instructor/answer_keys.json`. Never copy into learner ingest or slides.\n\n"
        "Burst notes that say attacker fail. Toy parser must not open sockets. "
        "Bot-close fixtures must fail.\n\n"
        "Alignment: `curriculum/alignment/cybersecurity_alignment.json` (CC 2026-09-01 preferred).\n"
    )


def student_packet(course_id: str, hook: str) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return student_packet_003(course_id, hook)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return student_packet_002(course_id, hook)
    if course_id == "GENERAL_IT":
        extra = "You will submit user tables, restore hashes, and change records. You will not receive keys."
    elif course_id == "COMPUTER_NETWORKING":
        extra = "You will submit CIDR answers and a frame parse. You will not receive keys."
    else:
        extra = "You will submit an incident note and parser results. You will not receive keys. You will not scan what you do not own."
    return f"# Student packet — {course_id}\n\n{hook}\n\n{extra}\n"


def group_project(course_id: str, title: str, assignment: str) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return group_project_003(course_id, title, assignment)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return group_project_002(course_id, title, assignment)
    if course_id == "GENERAL_IT":
        extra = "Roles: operator and recorder. Swap at 30 minutes. Notes that require the operator's memory fail."
    elif course_id == "COMPUTER_NETWORKING":
        extra = "Deliver intent JSON + Pier→Roof trace (VLAN, LPM, TTL, ACL) + guest VLAN that cannot reach Roof."
    else:
        extra = "Design checkpoint (≤2 pages) before the evidence-locker checker. No CS161 file-share clone."
    return f"# Group project — {title}\n\n{assignment}\n\n{extra}\n"


def portfolio(course_id: str) -> str:
    if course_id in SYLLABUS_ASSESSMENT_003:
        return portfolio_003(course_id)
    if course_id in SYLLABUS_ASSESSMENT_002:
        return portfolio_002(course_id)
    if course_id == "GENERAL_IT":
        return "# Portfolio — Civic Tech Desk\n\nShip restore hash, CHG-88, and a no-face desk tour. No PII.\n"
    if course_id == "COMPUTER_NETWORKING":
        return "# Portfolio — Packet Range\n\nShip datapath JSON, intent file, and the four-noun trace. Do not claim CCNA.\n"
    return "# Portfolio — Harbor SOC\n\nShip seven lab JSON files, USB timeline with cannot-claim, and a scope paragraph. Do not claim CC/Security+.\n"
