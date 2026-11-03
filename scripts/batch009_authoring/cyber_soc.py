"""CYBER_SOC — Night Shift Desk. Authored week by week; numbers match batch009/labs_soc.py."""

COURSE_ID = "CYBER_SOC"
PREFIX = "soc"
TITLE = "Cybersecurity Foundations and SOC Readiness — Night Shift Desk"
ACADEMY = "ACADEMY_CYBER"
KINESTHETIC = (
    "Ten Night Shift Desk tickets: read the auth log → tune a window rule → measure precision → hash and defang "
    "indicators → map to ATT&CK → check DMARC alignment → score CVSS by hand → order the queue → report MTTD/MTTR → hand off the shift."
)
SYLLABUS_HOOK = (
    "CYBER_SOC COURSE_DIGITAL_RC: analyst-desk numeracy for a junior SOC seat — log parsing, windowed detection, "
    "precision and recall, indicator hygiene, MITRE ATT&CK mapping, email authentication, CVSS v3.1, triage "
    "queues, and shift metrics. Defensive only, synthetic logs, documentation IP ranges. Distinct from the "
    "CYBERSECURITY Harbor SOC governance course. Not student/teacher E6."
)
CAREER = {
    "roles": ["soc_analyst_tier1_trainee", "security_operations_intern", "alert_triage_assistant"],
    "nice_categories": ["protect_and_defend", "analyze"],
    "certs_aligned_not_granted": [
        "MITRE ATT&CK technique vocabulary (PUBLIC_REFERENCE_ONLY)",
        "FIRST CVSS v3.1 scoring (PUBLIC_REFERENCE_ONLY; not a certification)",
        "NIST SP 800-61r2 incident phases (PUBLIC_REFERENCE_ONLY)",
    ],
}
NO_AI_WEEKS = [3, 7]

WEEKS = [
    {
        "title": "Auth log anatomy — failures, sources, and the success that follows",
        "lab_id": "lab_soc_log_parse",
        "worked_example": "203.0.113.45 failed 3×, 198.51.100.7 failed 2×, 192.0.2.10 failed 1×; Accepted password for root from 203.0.113.45 at 01:15:31 → escalate",
        "lesson": (
            "Ticket SOC-2101 lands at 01:20 on the Night Shift Desk: eight lines from the bastion host's sshd log and a "
            "request to say whether anything matters. Read a log line left to right as a sentence. The timestamp says "
            "when, the host and process say where, and the message says what happened to whom from which address. In "
            "this fixture 203.0.113.45 fails three times as root, 198.51.100.7 tries the made-up accounts admin and oracle "
            "twice, and 192.0.2.10 fails once right after the user naiya logged in with her key from the same machine. "
            "Counting failures per source is the start, not the finding. The line that changes the night is the last one: "
            "Accepted password for root from 203.0.113.45, seconds after that address failed. A success that follows a "
            "run of failures from the same source is the pattern analysts escalate, because it can mean a guessed "
            "password. Naiya's typo after a good key login is noise you note and move past. All addresses here come from "
            "documentation ranges, so nobody's real server appears in the course, and you never paste a live customer "
            "log into a chat tool to save time."
        ),
        "assignment": "Submit lab_soc_log_parse JSON for SOC-2101: failed_by_ip, top_source, accepted_after_failures.",
        "quiz": [
            ("Which address in the fixture has the most failed logins?", ["203.0.113.45", "198.51.100.7", "192.0.2.10", "10.0.0.1"], "three failures"),
            ("Why does the root success from 203.0.113.45 need escalation?", ["It follows a run of failures from the same source", "Root logins are always forbidden by law", "It came from a documentation range", "It used a public key"], "success after failures"),
            ("Naiya fails once just after a key login from her own address. How do you treat it?", ["Note it as likely noise and move on", "Lock every account", "Escalate as a breach", "Delete the line"], "context"),
            ("What should never happen with a live customer log during triage?", ["Pasting it into an outside chat tool", "Reading it on the SIEM", "Counting its failures", "Saving it in the case"], "data handling"),
            ("Which part of a log line tells you the remote address?", ["The 'from … port' clause", "The process ID", "The hostname bastion", "The month"], "anatomy"),
            ("Why do the course logs use addresses like 198.51.100.7?", ["They are reserved documentation ranges", "They belong to the course host", "They are random", "They are IPv6"], "RFC 5737"),
        ],
    },
    {
        "title": "Windowed detection — a threshold means nothing without a clock",
        "lab_id": "lab_soc_window_rule",
        "worked_example": "threshold 4 in 60 s → 203.0.113.45 fires at t=70 (events 20, 50, 65, 70); 198.51.100.7 does not; widen to 90 s → it fires at 265",
        "lesson": (
            "SOC-2202 asks you to turn last night's eyeballing into a rule the SIEM can run. 'Four failed logins' is not a "
            "rule until you say within how long. The fixture lists eleven failures with second offsets. With a threshold "
            "of four inside a sixty-second sliding window, 203.0.113.45 fires at second 70: the failures at 20, 50, 65 and "
            "70 all sit within sixty seconds of each other, while the first one at second 0 has already aged out. "
            "198.51.100.7 never fires, because its attempts at 200, 230, 250 and 265 span sixty-five seconds, one heartbeat "
            "too slow. Widen the window to ninety seconds and that address alerts at 265 as well. Neither choice is free. "
            "A wider window catches slow guessing and also pulls in people who mistype their passwords on a cold morning. "
            "Write the threshold and window into the rule's description so the next analyst can reason about a miss, and "
            "replay the rule against stored events before you switch it on. The lab grader replays your parameters, so "
            "it rejects an alert list that would only be true for a different window."
        ),
        "assignment": "Submit lab_soc_window_rule JSON for SOC-2202: threshold, window_s, and the alerts your rule fires.",
        "quiz": [
            ("With 4-in-60 s, when does 203.0.113.45 first alert?", ["At second 70", "At second 50", "At second 0", "Never"], "20,50,65,70"),
            ("Why does 198.51.100.7 stay quiet under 4-in-60 s?", ["Its four attempts span 65 seconds", "It has only two failures", "It is allow-listed", "Its logins succeeded"], "window edge"),
            ("What does widening the window to 90 s trade away?", ["More false positives from ordinary typos", "All detection", "Log retention", "Nothing"], "trade-off"),
            ("What makes 'four failed logins' an actual rule?", ["Stating the time window it counts within", "Writing it in capitals", "Adding a severity", "Sending it by email"], "window"),
            ("Before enabling a new rule, what should you do?", ["Replay it against stored events", "Enable it on every host blind", "Delete old alerts", "Disable logging"], "backtest"),
            ("Where should the threshold and window be documented?", ["In the rule description", "Only in your memory", "In a sticky note", "Nowhere"], "maintainability"),
        ],
    },
    {
        "title": "Detection quality — precision, recall, and the analyst's hour",
        "lab_id": "lab_soc_detection_metrics",
        "worked_example": "TP 18, FP 42, FN 6, TN 934 → precision 18/60 = 0.30, recall 18/24 = 0.75, FPR 42/976 = 0.043 → needs tuning",
        "lesson": (
            "SOC-2303 is a NO_AI week: do the fractions on paper and show each line, because these four numbers decide "
            "whether a rule stays on. A month of the brute-force rule produced 60 alerts. Eighteen were real attacks, "
            "true positives, and forty-two were not, false positives. Six real attacks slipped through without an alert, "
            "false negatives, and 934 quiet events were correctly left alone. Precision asks how often an alert is worth "
            "opening: 18 out of 60, or 0.30. Recall asks how many real attacks the rule caught: 18 out of 24, or 0.75. The "
            "false-positive rate compares wrong alerts with all benign events, 42 out of 976, about 0.043, which sounds tiny "
            "and still costs forty-two investigations. At ten minutes each that is seven analyst-hours spent proving "
            "nothing happened. A precision under one half means most alerts are noise, so the honest call is needs tuning, "
            "not 'the rule works'. Tuning that raises precision often lowers recall, so record both before and after a "
            "change, and never report recall alone because it flatters a noisy rule."
        ),
        "assignment": "Submit lab_soc_detection_metrics JSON for SOC-2303 (NO_AI): precision, recall, false_positive_rate, alerts, needs_tuning.",
        "quiz": [
            ("Sixty alerts, eighteen real. What is precision?", ["0.30", "0.75", "0.043", "0.18"], "18/60"),
            ("Twenty-four real attacks, eighteen alerted. What is recall?", ["0.75", "0.30", "0.25", "0.82"], "18/24"),
            ("Why is a 0.043 false-positive rate still expensive here?", ["It means 42 investigations that find nothing", "It is above 50%", "It hides true positives", "It breaks the SIEM"], "volume"),
            ("Which single metric flatters a noisy rule?", ["Recall reported alone", "Precision", "False-negative count", "Alert volume"], "one-sided"),
            ("What usually happens to recall when you tighten a rule for precision?", ["It tends to fall", "It always rises", "It is unaffected", "It becomes undefined"], "trade-off"),
            ("Precision is 0.30. What is the honest call?", ["The rule needs tuning", "The rule is excellent", "Disable logging", "Raise recall to 1.0 by alerting on everything"], "<0.5"),
        ],
    },
    {
        "title": "Indicator hygiene — hash it, defang it, then compare",
        "lab_id": "lab_soc_ioc_match",
        "worked_example": "sha256('WAIKE-SOC training sample: …') = fc6c0f88…e657; http://update-check.example.net/payload → hxxp://update-check[.]example[.]net/payload; on IOC list → match",
        "lesson": (
            "SOC-2404 arrives with a suspicious attachment name and a link from a user report. Indicators of compromise are "
            "only useful if you can compare them exactly and pass them around safely. For files that means a cryptographic "
            "hash: SHA-256 turns any sequence of bytes into a 64-character fingerprint, and a single changed byte produces an "
            "unrelated digest, so the lab recomputes the hash from the inert sample text instead of trusting a pasted value. "
            "For links it means defanging before the indicator goes into a ticket, chat, or report: write hxxp instead of "
            "http and bracket every dot in the host, so update-check.example.net becomes update-check[.]example[.]net and "
            "nobody's mail client turns it into a clickable trap. Only after both steps do you check the desk's indicator "
            "list. Here the sample hash and the domain are both on it, so the answer is a match and the ticket goes to the "
            "phishing playbook. A miss does not mean safe, it means unknown, and the course's sample is inert text, never "
            "real malware, so nobody downloads or detonates anything on a personal laptop."
        ),
        "assignment": "Submit lab_soc_ioc_match JSON for SOC-2404: sample_text, sha256, url, defanged_url, ioc_match.",
        "quiz": [
            ("Why does the grader recompute the SHA-256 rather than trust the ticket?", ["One changed byte gives an unrelated digest", "Hashes expire", "SHA-256 is reversible", "It is faster"], "exact match"),
            ("How is http://update-check.example.net written after defanging?", ["hxxp://update-check[.]example[.]net", "http://update-check.example.net", "update-check dot example", "https://update-check.example.net"], "defang"),
            ("Why defang a URL before posting it in a ticket?", ["So no client renders it as a clickable link", "To encrypt it", "To shorten it", "Because tickets reject dots"], "safety"),
            ("An indicator is not on the list. What does that mean?", ["Unknown, not proven safe", "Definitely safe", "Definitely malicious", "The list is broken"], "absence"),
            ("What is the course's attachment sample?", ["Inert text standing in for a file", "Live malware", "A real customer invoice", "An exploit kit"], "boundary"),
            ("How long is a SHA-256 hex digest?", ["64 characters", "32 characters", "40 characters", "128 characters"], "256 bits"),
        ],
    },
    {
        "title": "ATT&CK mapping — describe behaviour, not villains",
        "lab_id": "lab_soc_attack_map",
        "worked_example": "B1 brute force → T1110 credential_access; B3 spoofed invoice → T1566 initial_access; B5 .locked files → T1486 impact; actor_attribution_claim false",
        "lesson": (
            "SOC-2505 gives the desk five behaviours seen this week and asks for a shared vocabulary. MITRE ATT&CK is a "
            "public catalogue of attacker techniques, each with an ID and one or more tactics that say what the attacker "
            "was trying to achieve. Many failed SSH logins from one address are T1110, Brute Force, under credential access. "
            "A never-before-seen account logging in at three in the morning with a correct password is T1078, Valid "
            "Accounts, which ATT&CK lists under several tactics because stolen credentials help an intruder get in, stay in, "
            "and blend in. A spoofed invoice attachment is T1566, Phishing, under initial access. PowerShell launched with an "
            "encoded command line is T1059, Command and Scripting Interpreter, under execution, and files renamed with a "
            ".locked suffix beside a ransom note are T1486, Data Encrypted for Impact. Mapping lets the day shift, the "
            "detection engineers, and management talk about the same thing. It does not tell you who did it. Plenty of "
            "groups use the same techniques, so the lab requires actor_attribution_claim to stay false."
        ),
        "assignment": "Submit lab_soc_attack_map JSON for SOC-2505: technique ID and tactic for B1–B5, actor_attribution_claim false.",
        "quiz": [
            ("Many failed SSH logins from one source map to which technique?", ["T1110 Brute Force", "T1566 Phishing", "T1486 Data Encrypted for Impact", "T1059 Command and Scripting Interpreter"], "brute force"),
            ("Why does T1078 Valid Accounts appear under several tactics?", ["Stolen credentials help an intruder enter, persist, and evade", "It is mislabelled", "Tactics are random", "It only applies to admins"], "multi-tactic"),
            ("Files renamed .locked with a ransom note map to?", ["T1486 under impact", "T1110 under credential access", "T1566 under initial access", "T1078 under persistence"], "impact"),
            ("Why must actor_attribution_claim stay false?", ["Many groups share the same techniques", "ATT&CK forbids naming groups", "Attribution is always obvious", "Tactics prove identity"], "technique ≠ actor"),
            ("PowerShell with an encoded command maps to which tactic?", ["Execution", "Impact", "Collection", "Reconnaissance"], "T1059"),
            ("What is the main benefit of ATT&CK mapping on a desk?", ["A shared vocabulary across teams", "Automatic blocking", "Legal proof", "Faster hashing"], "common language"),
        ],
    },
    {
        "title": "Email authentication — passing is not the same as aligned",
        "lab_id": "lab_soc_dmarc_align",
        "worked_example": "A: From mail.harborpay.example, SPF via bounce.harborpay.example, DKIM d=harborpay.example → aligned → DMARC pass; B: From harborpay.example, SPF/DKIM pass for bulk-sender.example → not aligned → DMARC fail",
        "lesson": (
            "SOC-2606 compares two invoices that both claim to come from Harbor Pay. SPF checks whether the sending server "
            "is allowed to send for the envelope's return-path domain. DKIM checks a signature made with a key published by "
            "the domain in the signature's d= tag. Both can pass for a domain that has nothing to do with the address the "
            "reader sees in the From line. DMARC closes that gap with alignment: at least one passing check must belong to "
            "the same organisational domain as the visible From address. Under relaxed alignment, subdomains count, so in "
            "message A the From address mail.harborpay.example, the return path bounce.harborpay.example, and the DKIM "
            "domain harborpay.example all share harborpay.example, and DMARC passes. Message B also shows SPF pass and DKIM "
            "pass, but both checks vouch for bulk-sender.example while the From line says harborpay.example, so DMARC fails. "
            "That is exactly the shape of a convincing spoof, and a user who sees 'SPF pass' in a header viewer will be "
            "fooled unless someone on the desk explains alignment."
        ),
        "assignment": "Submit lab_soc_dmarc_align JSON for SOC-2606: spf_aligned, dkim_aligned, dmarc_pass for messages A and B.",
        "quiz": [
            ("Message B passes SPF and DKIM. Why does DMARC still fail?", ["Neither passing check belongs to the From domain", "DKIM keys expired", "SPF is optional", "The message is too long"], "alignment"),
            ("What does DKIM's d= tag name?", ["The domain whose key signed the message", "The recipient", "The mail server IP", "The DMARC policy"], "signing domain"),
            ("Under relaxed alignment, does mail.harborpay.example align with harborpay.example?", ["Yes, they share the organisational domain", "No, subdomains never align", "Only for SPF", "Only on weekends"], "relaxed"),
            ("SPF authorises a server to send for which domain?", ["The envelope return-path domain", "The visible From domain only", "Any domain", "The recipient's domain"], "envelope"),
            ("For DMARC to pass, how many aligned passing checks are needed?", ["At least one of SPF or DKIM", "Both", "Neither", "Three"], "either"),
            ("Why must the desk explain alignment to users?", ["'SPF pass' alone can make a spoof look trustworthy", "Users configure DNS", "Alignment is a user setting", "It speeds delivery"], "user education"),
        ],
    },
    {
        "title": "CVSS v3.1 by hand — from vector string to severity band",
        "lab_id": "lab_soc_cvss_score",
        "worked_example": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H → ISS 0.9148, impact 5.873, exploitability 3.887 → Roundup 9.8 Critical; AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N → 5.5 Medium",
        "lesson": (
            "SOC-2707 is the second NO_AI week, because a desk that only reads scores off a website cannot defend them in a "
            "patch meeting. The FIRST CVSS v3.1 base score turns eight metrics into a number. Impact starts from the "
            "confidentiality, integrity, and availability weights, 0.56 for High, 0.22 for Low, 0 for None, combined as "
            "ISS = 1 − (1 − C)(1 − I)(1 − A). For an unchanged scope, impact is 6.42 × ISS. Exploitability is 8.22 × attack "
            "vector × attack complexity × privileges required × user interaction, where a network vector weighs 0.85 and "
            "low complexity 0.77. For the familiar AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H vector, ISS is about 0.9148, impact "
            "about 5.873, exploitability about 3.887, and their sum rounds up to 9.8, Critical. Roundup means the next tenth "
            "upward, not the nearest, which is where hand scorers slip. A local, low-privilege flaw that only leaks data, "
            "AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N, lands at 5.5, Medium. The base score describes the flaw, not your network; "
            "asset value enters next week."
        ),
        "assignment": "Submit lab_soc_cvss_score JSON for SOC-2707 (NO_AI): at least two vectors with base_score and severity.",
        "quiz": [
            ("What base score does AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H receive?", ["9.8", "10.0", "8.8", "7.5"], "classic critical"),
            ("How does CVSS v3.1 Roundup treat 5.41?", ["It becomes 5.5", "It becomes 5.4", "It becomes 5.0", "It becomes 6.0"], "next tenth up"),
            ("Which weight does High confidentiality impact use?", ["0.56", "0.22", "0.85", "0.77"], "C:H"),
            ("For unchanged scope, impact equals what?", ["6.42 × ISS", "7.52 × ISS", "8.22 × ISS", "ISS squared"], "scope U"),
            ("A score of 5.5 falls in which band?", ["Medium", "Low", "High", "Critical"], "4.0–6.9"),
            ("What does the base score not include?", ["How valuable the affected asset is to you", "Attack vector", "Privileges required", "Impact on integrity"], "base vs context"),
        ],
    },
    {
        "title": "Triage queue — severity meets asset criticality",
        "lab_id": "lab_soc_triage_queue",
        "worked_example": "priority = severity weight × criticality: A5 12, A1 9, A3 6 (t=2), A6 6 (t=8), A2 4, A4 3; due = received + SLA (critical 15, high 60, medium 240, low 1440)",
        "lesson": (
            "SOC-2808 hands you six open alerts at once and one pair of hands. Severity alone is a poor sort key, because a "
            "critical alert on a lobby kiosk can matter less than a high alert on the domain controller. The desk multiplies "
            "a severity weight, four for critical down to one for low, by the asset's criticality from one to three. A5, "
            "critical on a criticality-three server, scores twelve and goes first. A1, high on criticality three, scores "
            "nine. A3 and A6 both score six, so the earlier arrival, A3 at minute two, goes ahead of A6 at minute eight. A2, "
            "the critical alert on a criticality-one kiosk, scores four, and A4 scores three. Each alert also gets a due "
            "time: the minute it arrived plus the service-level target for its severity, fifteen minutes for critical, an "
            "hour for high, four hours for medium, a day for low. That puts A2's due time at minute 27 even though it sits "
            "fifth in the queue, which is a signal to ask for help rather than quietly breach the target. A queue is a plan "
            "you can explain to the shift lead, not a mood."
        ),
        "assignment": "Submit lab_soc_triage_queue JSON for SOC-2808: ordered_ids and due_min for A1–A6.",
        "quiz": [
            ("Which alert goes first under severity × criticality?", ["A5", "A2", "A1", "A3"], "12"),
            ("Why does A2, a critical alert, rank fifth?", ["It sits on a criticality-one kiosk", "It arrived first", "Critical alerts are ignored", "It is a duplicate"], "asset value"),
            ("A3 and A6 tie at six. What breaks the tie?", ["Earlier arrival", "Alphabetical order", "Random choice", "Higher severity always"], "time"),
            ("When is A2 due if it arrived at minute 12?", ["Minute 27", "Minute 72", "Minute 252", "Minute 12"], "12 + 15"),
            ("A low-priority alert's due time will pass before you reach it. What should you do?", ["Ask the shift lead for help", "Close it silently", "Change its received time", "Ignore the SLA"], "escalate capacity"),
            ("What makes a triage queue defensible?", ["A stated sort rule you can explain", "Gut feeling", "Newest first always", "Loudest requester first"], "explainable"),
        ],
    },
    {
        "title": "Shift metrics — MTTD, MTTR, and the median that resists one bad night",
        "lab_id": "lab_soc_shift_metrics",
        "worked_example": "time to detect = 12, 45, 5, 70 min → MTTD 33, median 28.5; time to resolve from detection = 78, 65, 35, 150 → MTTR 82",
        "lesson": (
            "SOC-2909 asks how the week went, in numbers management will read. Mean time to detect is the average gap "
            "between when something happened and when the desk noticed. The four incidents took 12, 45, 5 and 70 minutes to "
            "detect, so MTTD is 33 minutes. Mean time to resolve, measured here from detection to resolution, averages 78, "
            "65, 35 and 150 minutes to 82. Define the start and end points in the report, because some teams measure "
            "resolution from occurrence and their numbers are not comparable with yours. One slow detection, the seventy-"
            "minute ransomware case, pulls the mean up; the median of the four detection times is 28.5 minutes and tells a "
            "steadier story about a typical night. Report both, and name the outlier instead of hiding it, since that is the "
            "incident the next tuning effort should study. Four incidents are a tiny sample. A dashboard that celebrates a "
            "five-minute drop in MTTD between two such weeks is reporting noise, so the course asks for the numbers and a "
            "sentence about how much they can bear."
        ),
        "assignment": "Submit lab_soc_shift_metrics JSON for SOC-2909: mttd_min, mttr_min, median_ttd_min.",
        "quiz": [
            ("Detection gaps are 12, 45, 5, 70 minutes. What is MTTD?", ["33 minutes", "28.5 minutes", "45 minutes", "132 minutes"], "mean"),
            ("What is the median time to detect for the same four gaps?", ["28.5 minutes", "33 minutes", "25 minutes", "37.5 minutes"], "middle pair"),
            ("Why report the median beside the mean?", ["One slow case can pull the mean up", "The median is always larger", "Means are illegal", "Medians include resolution"], "outliers"),
            ("Why define where MTTR starts?", ["Teams measure from different events, so numbers differ", "MTTR never changes", "It is set by law", "It hides incidents"], "comparability"),
            ("Resolution times 78, 65, 35, 150 minutes give what MTTR?", ["82 minutes", "71.5 minutes", "150 minutes", "65 minutes"], "mean"),
            ("A five-minute MTTD drop across two four-incident weeks shows what?", ["Probably noise in a tiny sample", "A proven improvement", "A broken SIEM", "A need to fire analysts"], "sample size"),
        ],
    },
    {
        "title": "Shift handoff — open incidents, NIST phases, and clean boundaries",
        "lab_id": "lab_soc_shift_handoff",
        "worked_example": "I4 open: T1486, containment_eradication_recovery, next owner day-shift lead; MTTD 33, MTTR 82; real_customer_data false; offensive_tooling false",
        "lesson": (
            "SOC-2A10 closes the night. A handoff is the document the day shift reads with its first coffee, so it must be "
            "complete without you in the room. List every open incident with its ATT&CK technique ID, the NIST SP 800-61 "
            "phase it is in, and a named next owner. The phases are preparation, detection and analysis, containment with "
            "eradication and recovery, and post-incident activity; saying 'containment' tells the reader which actions are "
            "already done and which are waiting. Carry the shift's MTTD and MTTR from last week's calculation rather than "
            "rounding them in your head, and say what changed in the rules you tuned. Two boundaries close every Night "
            "Shift Desk packet. It contains no real customer data, only the course's synthetic logs and documentation "
            "addresses, and it contains no offensive tooling: the desk detects, contains, and documents; it does not build "
            "exploits or scan systems it does not own. Mentors check the packet against six or more passed labs and ask you "
            "to walk one incident from first log line to current phase out loud."
        ),
        "assignment": "Submit lab_soc_shift_handoff JSON for SOC-2A10: labs_passed, open incidents with technique/phase/owner, MTTD/MTTR, boundaries.",
        "quiz": [
            ("What must every open incident in a handoff carry?", ["Technique ID, NIST phase, and a next owner", "Only a title", "The analyst's mood", "A screenshot"], "complete"),
            ("Which of these is a NIST SP 800-61 phase?", ["Containment, eradication, and recovery", "Revenge", "Marketing", "Exploit development"], "phases"),
            ("Why carry MTTD and MTTR from the calculation rather than memory?", ["Rounded guesses drift from the record", "Memory is always right", "The SIEM forbids it", "They never change"], "traceable"),
            ("What does 'no offensive tooling' mean for the desk?", ["It detects and contains; it does not build exploits or scan others", "It may scan any network", "It writes malware for practice", "It ignores attacks"], "defensive"),
            ("Who reads the handoff first?", ["The incoming shift", "The attacker", "Only auditors", "Nobody"], "audience"),
            ("During review a mentor asks for what walk-through?", ["One incident from first log line to current phase", "The entire SIEM config", "Every quiz answer", "A vendor demo"], "oral check"),
        ],
    },
]

MID = [
    ("A log shows 'Failed password for invalid user test from 203.0.113.9'. What does 'invalid user' tell you?", ["The account name does not exist on the host", "The password was correct", "The address is internal", "The login succeeded"], "username spray"),
    ("Your rule counts failures since midnight with no window. What goes wrong at 23:50?", ["A day's scattered typos can add up to an alert", "Nothing", "It never fires", "It only fires on weekends"], "missing window"),
    ("Five failures arrive at seconds 0, 59, 118, 177, 236 against a 4-in-60 s rule. Does it fire?", ["No; no four fall within 60 seconds", "Yes, at 177", "Yes, at 59", "Yes, at 0"], "slow drip"),
    ("A rule has precision 0.9 and recall 0.2. Describe it.", ["Alerts are trustworthy but most attacks are missed", "Noisy but complete", "Perfect", "Useless in every way"], "trade-off"),
    ("Doubling true negatives while holding other counts does what to precision?", ["Leaves it unchanged", "Doubles it", "Halves it", "Sets it to 1"], "TN not in precision"),
    ("Two files have SHA-256 digests that differ in the last character. What do you conclude?", ["They are different files", "They are the same file", "One hash is truncated", "The hash function failed"], "fingerprint"),
    ("Which of these is correctly defanged?", ["hxxps://login[.]example[.]org/reset", "https://login.example.org/reset", "hxxps://login.example.org/reset", "login example org"], "dots and scheme"),
    ("A user forwards a phish to the whole department 'as a warning'. What risk did that create?", ["More people can now click the live link", "None", "It deletes the phish", "It blocks the sender"], "containment"),
    ("Which ATT&CK tactic describes the attacker's goal of staying in after a reboot?", ["Persistence", "Impact", "Reconnaissance", "Exfiltration"], "tactic meaning"),
    ("A colleague says 'this T1566 alert proves a nation-state attack'. Your response?", ["Technique use alone does not identify an actor", "Agree and publish", "Delete the alert", "Change the technique ID"], "attribution"),
    ("Valid-account misuse is hard to detect mainly because…", ["The login itself looks legitimate", "It always fails", "It uses malware", "It is rare"], "T1078"),
    ("A message's From domain is example.org, DKIM d=example.org passes, SPF fails. DMARC result?", ["Pass, through aligned DKIM", "Fail", "Neutral", "Cannot be evaluated"], "one aligned pass"),
    ("Strict alignment would treat mail.harborpay.example vs harborpay.example how?", ["As not aligned", "As aligned", "As a DKIM failure", "As spam"], "strict"),
    ("Why would an attacker register harb0rpay.example?", ["To pass checks for a look-alike domain users misread", "To break DMARC", "To speed delivery", "To get a certificate"], "look-alike"),
    ("A vector changes only AC:L to AC:H. What happens to the base score?", ["It drops, because exploitability falls", "It rises", "No change", "It becomes 10"], "complexity"),
    ("Two flaws both score 7.5. One is on a test VM, one on payroll. Which patch first?", ["Payroll, because asset value differs", "The test VM", "Either, scores are equal", "Neither"], "context"),
    ("An analyst rounds 6.94 to 6.9 when scoring CVSS by hand. What is the correct value?", ["7.0", "6.9", "6.0", "7.5"], "Roundup"),
    ("Severity weight 3, criticality 2 versus weight 2, criticality 3. Which wins?", ["They tie at 6; earlier arrival decides", "The first", "The second", "Neither is queued"], "tie"),
    ("Your queue will breach three SLAs this hour. What is the honest action?", ["Tell the shift lead and request help", "Backdate received times", "Close low alerts unread", "Turn off the SLA timer"], "capacity"),
    ("A single 6-hour detection appears among ten 10-minute ones. Which summary misleads less?", ["The median with the outlier named", "The mean alone", "The maximum alone", "Nothing at all"], "robust"),
]

FINAL = [
    ("An accepted login follows twelve failures from one address at 03:00. First action on the desk?", ["Escalate and check what the account did next", "Ignore it, it succeeded", "Block every address", "Delete the log"], "triage"),
    ("A teammate wants to tune a rule live in production without replay. Your advice?", ["Replay against stored events first", "Go ahead", "Disable the SIEM", "Raise all thresholds to 1000"], "backtest"),
    ("After tuning, precision rose from 0.3 to 0.6 and recall fell from 0.75 to 0.5. How do you report it?", ["Show both before and after and the trade-off", "Report only precision", "Report only recall", "Say nothing changed"], "honest reporting"),
    ("Which metric counts how many real attacks a rule missed?", ["False negatives", "True negatives", "Precision", "Alert volume"], "FN"),
    ("A threat feed lists a domain. Your log has it with a different subdomain. Is that a match?", ["Possibly; record it as a related indicator and investigate", "Exactly the same indicator", "Never relevant", "Proof of breach"], "partial match"),
    ("Where should a live malicious sample never be opened?", ["On a personal or production laptop", "In an approved isolated sandbox", "In a vendor's analysis portal approved by policy", "Nowhere is ever acceptable"], "safe handling"),
    ("Which statement about MITRE ATT&CK is accurate?", ["It catalogues techniques and tactics, not culprits", "It assigns blame", "It is a firewall", "It scores vulnerabilities"], "purpose"),
    ("A ransomware note appears. Which technique ID belongs in the handoff?", ["T1486", "T1110", "T1566", "T1595"], "impact"),
    ("An email shows DMARC fail but the user insists it is from their bank. What do you check first?", ["Which domains SPF and DKIM actually vouched for", "The font", "The subject line length", "The time zone"], "alignment"),
    ("Why do many organisations publish a DMARC reject policy after monitoring?", ["So unaligned mail claiming their domain is refused", "To speed up newsletters", "To disable DKIM", "To hide their MX"], "policy"),
    ("A CVSS vector has S:C. What changes in the calculation?", ["The changed-scope impact formula and PR weights apply", "Nothing", "The score is capped at 5", "Exploitability is ignored"], "scope"),
    ("A vendor scores a flaw 9.8 but your server has the service disabled. What remains true?", ["The base score is 9.8; your exposure is lower", "The base score becomes 0", "The vendor is wrong", "The flaw disappears"], "base vs environment"),
    ("Your queue sorts by newest alert first. What failure follows?", ["Old critical alerts on key assets wait too long", "Nothing", "Alerts merge", "SLAs disappear"], "sort rule"),
    ("Two analysts disagree on queue order. What settles it?", ["The written severity × criticality rule", "Seniority", "Coin toss", "Whoever shouts"], "explainable"),
    ("Your MTTD is 33 minutes; another team reports 8. What do you check before comparing?", ["How each team defines the start and end points", "Who has better coffee", "Nothing", "Their tool vendor"], "definitions"),
    ("Management wants MTTR below 30 minutes by next week. What do you tell them?", ["Which incidents drive the number and what would shorten them", "It is done", "Stop logging incidents", "Close tickets faster without fixing"], "honest metrics"),
    ("A handoff lists 'ransomware stuff, Bob knows'. What is missing?", ["Technique ID, NIST phase, and a named next owner", "Nothing", "A meme", "The analyst's password"], "completeness"),
    ("Which NIST SP 800-61 phase includes writing lessons learned?", ["Post-incident activity", "Preparation", "Detection and analysis", "Containment"], "phase"),
    ("A training packet includes a real customer's email headers. What should happen?", ["Remove them and use synthetic data", "Keep them, they are realistic", "Share them wider", "Encrypt and post publicly"], "data boundary"),
    ("A trainee asks to port-scan a neighbour's network 'for practice'. Your answer?", ["No; only systems you own or are authorised to test", "Yes, on weekends", "Only with a VPN", "Only if it is fast"], "authorisation"),
    ("Why does the course use 203.0.113.0/24 and similar ranges?", ["They are reserved for documentation, so no real host is implicated", "They are faster", "They are private LAN ranges", "They belong to MITRE"], "RFC 5737"),
    ("What is the clearest sign a rule's alerts are mostly noise?", ["Precision well below one half", "High recall", "Low alert volume", "A long rule name"], "precision"),
    ("A detection engineer proposes alerting on every login. What happens to recall and precision?", ["Recall approaches 1; precision collapses", "Both rise", "Both fall to 0", "Neither changes"], "extremes"),
    ("What is the boundary of the Night Shift Desk course?", ["Defensive analysis on synthetic data, not a certification or live SOC duty", "A guaranteed SOC job", "A penetration-testing licence", "Access to production SIEMs"], "claim boundary"),
]
