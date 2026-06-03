"""Course-specific depth content for flagship WAIKE tracks."""

from __future__ import annotations

FLAGSHIP_COURSES = {
    "digital_confidence",
    "software_engineering",
    "networking",
    "cybersecurity",
    "wireless_dsp_6g",
    "ai_ran_digital_twin_research",
}

TECHNICAL_FLAGSHIP = {
    "software_engineering",
    "networking",
    "cybersecurity",
    "wireless_dsp_6g",
    "ai_ran_digital_twin_research",
}

DISCLAIMER = (
    "**Evidence:** synthetic teaching fixture / source-backed assumption. "
    "**Requires local validation** — not field-validated deployment."
)

# Week titles and focus per flagship course (8 weeks)
WEEK_PLANS: dict[str, list[dict[str, str]]] = {
    "digital_confidence": [
        {"title": "Why digital confidence matters", "theory": "Devices, users, community needs", "case": "gary/family_digital_navigation_night"},
        {"title": "Files, folders, and organization", "theory": "File management", "case": "germany/older_adult_digital_confidence"},
        {"title": "Email and safe communication", "theory": "Email, phishing awareness", "case": "gary/homework_portfolio_access_lab"},
        {"title": "Web safety and passwords", "theory": "Passwords, MFA, browser safety", "case": "germany/privacy_security_equity_lab"},
        {"title": "Documents and forms", "theory": "Docs, PDFs, online forms", "case": "guyana/e_government_assistance_desk"},
        {"title": "Video meetings and collaboration", "theory": "Zoom/Meet basics", "case": "geelong/inclusive_smart_city_lab"},
        {"title": "Asking for help and troubleshooting", "theory": "Support pathways", "case": "gary/small_business_digital_starter_kit"},
        {"title": "Portfolio guide and community demo", "theory": "Presentation, revision", "case": "gary/family_digital_navigation_night"},
    ],
    "software_engineering": [
        {"title": "How software helps communities", "theory": "Programs vs apps", "case": "gary/homework_portfolio_access_lab"},
        {"title": "HTML/CSS structure", "theory": "Web foundations", "case": "geelong/youth_creative_tech_studio"},
        {"title": "JavaScript or Python basics", "theory": "Variables, logic", "case": "gaza/crisis_learning_archive"},
        {"title": "Git and GitHub workflow", "theory": "Version control", "case": "gary/homework_portfolio_access_lab"},
        {"title": "Debugging and testing", "theory": "Errors, unit tests", "case": "geelong/youth_creative_tech_studio"},
        {"title": "APIs and simple architecture", "theory": "Client/server", "case": "gaza/blackout_resilient_content_plan"},
        {"title": "Documentation and deployment", "theory": "README, static deploy", "case": "gary/small_business_digital_starter_kit"},
        {"title": "Group app demo and portfolio", "theory": "Demo, reflection", "case": "geelong/youth_creative_tech_studio"},
    ],
    "networking": [
        {"title": "Networks in daily life", "theory": "OSI overview", "case": "gary/public_wifi_quality_map"},
        {"title": "IP addressing and subnets", "theory": "IPv4, CIDR", "case": "ghana/solar_powered_learning_hub"},
        {"title": "DNS, DHCP, and naming", "theory": "Name resolution", "case": "guyana/hinterland_ict_hub_support"},
        {"title": "Wi-Fi and latency basics", "theory": "802.11, latency", "case": "gary/public_wifi_quality_map"},
        {"title": "Routing and paths", "theory": "Traceroute, paths", "case": "ghana/power_backhaul_failure_drill"},
        {"title": "Measurement and Edge-IO", "theory": "Packet loss, jitter", "case": "graham_land/polar_ntn_simulation"},
        {"title": "Troubleshooting playbook", "theory": "Layered debug", "case": "ghana/power_backhaul_failure_drill"},
        {"title": "Connectivity improvement plan", "theory": "Capstone presentation", "case": "gary/public_wifi_quality_map"},
    ],
    "cybersecurity": [
        {"title": "Security mindset and CIA triad", "theory": "Confidentiality, integrity, availability", "case": "ghana/mobile_money_cybersecurity_workshop"},
        {"title": "Authentication and passwords", "theory": "MFA, credential hygiene", "case": "germany/privacy_security_equity_lab"},
        {"title": "Phishing and social engineering", "theory": "Recognition, reporting", "case": "gary/small_business_digital_starter_kit"},
        {"title": "Endpoint and device security", "theory": "Updates, hardening", "case": "ghana/mobile_money_cybersecurity_workshop"},
        {"title": "Logging and SOC basics", "theory": "SIEM concepts", "case": "germany/privacy_security_equity_lab"},
        {"title": "Threat modeling", "theory": "STRIDE-lite", "case": "ghana/mobile_money_cybersecurity_workshop"},
        {"title": "Incident response checklist", "theory": "IR phases", "case": "gary/small_business_digital_starter_kit"},
        {"title": "Cyber safety kit demo", "theory": "Portfolio capstone", "case": "ghana/mobile_money_cybersecurity_workshop"},
    ],
    "wireless_dsp_6g": [
        {"title": "Signals and frequency", "theory": "Spectrum, bandwidth", "case": "ghana/solar_powered_learning_hub"},
        {"title": "Sampling and digital signals", "theory": "Nyquist intuition", "case": "graham_land/offline_scientific_workflow"},
        {"title": "Noise, SNR, and reliability", "theory": "Link budget basics", "case": "gary/public_wifi_quality_map"},
        {"title": "Wi-Fi and propagation", "theory": "Path loss", "case": "ghana/power_backhaul_failure_drill"},
        {"title": "Latency and URLLC concepts", "theory": "6G/URLLC-aligned (not certified)", "case": "graham_land/polar_ntn_simulation"},
        {"title": "NTN and fallback", "theory": "Satellite windows", "case": "graham_land/satellite_outage_mode"},
        {"title": "Measurement plan", "theory": "Edge-IO, synthetic metrics", "case": "gary/public_wifi_quality_map"},
        {"title": "Resilience plan capstone", "theory": "Beam/NTN research connection", "case": "graham_land/priority_aware_data_sync"},
    ],
    "ai_ran_digital_twin_research": [
        {"title": "Digital twin purpose", "theory": "Twin vs map", "case": "gary/homework_portfolio_access_lab"},
        {"title": "7GC site profiles", "theory": "Metrics, maturity", "case": "7gc-digital-twin repo"},
        {"title": "AI-RAN policy intuition", "theory": "Traffic classes", "case": "spectrumx-ai-ran-gary"},
        {"title": "Fairness, energy, latency", "theory": "Tradeoffs", "case": "ghana/power_backhaul_failure_drill"},
        {"title": "Edge-IO telemetry", "theory": "Measurement ethics", "case": "edge-io-measurement-node"},
        {"title": "Reproducibility", "theory": "make e2e, logs", "case": "waike-research-ops"},
        {"title": "Research poster structure", "theory": "Evidence maturity", "case": "guyana/flood_resilience_connectivity_plan"},
        {"title": "Twin extension capstone", "theory": "PR + report", "case": "gary + ghana scenes"},
    ],
}

GROUP_PROJECTS: dict[str, dict[str, str]] = {
    "digital_confidence": {
        "title": "Community Digital Navigation Guide",
        "site": "gary",
        "community": "Families need plain-language help using school portals, Wi-Fi, and safe accounts.",
        "technical": "Produce a multi-page guide with screenshots, safety callouts, and service flows.",
        "research": "How does digital confidence reduce support load for schools and small businesses?",
    },
    "software_engineering": {
        "title": "7GC Web App for Community Need",
        "site": "geelong",
        "community": "Youth creative-tech studio needs a simple portfolio or resource finder.",
        "technical": "HTML/CSS/JS or Python app with GitHub repo, README, and deploy instructions.",
        "research": "What offline or low-bandwidth fallback is needed?",
    },
    "networking": {
        "title": "Campus Connectivity Improvement Plan",
        "site": "ghana",
        "community": "Solar learning hub suffers power/backhaul failures affecting lessons.",
        "technical": "Network diagram, latency budget, measurement plan using Edge-IO concepts.",
        "research": "Which metrics prove improvement without claiming carrier certification?",
    },
    "cybersecurity": {
        "title": "7GC Cyber Safety and IR Kit",
        "site": "ghana",
        "community": "Mobile money users face phishing and account takeover risks.",
        "technical": "Threat model, phishing module, IR checklist, dashboard mockup.",
        "research": "How do privacy constraints change logging for SOC-style workflows?",
    },
    "wireless_dsp_6g": {
        "title": "Wireless Measurement and Resilience Plan",
        "site": "graham_land",
        "community": "Polar site needs NTN fallback and priority sync understanding.",
        "technical": "Signal/latency explanation, measurement plan, presentation — 6G-aligned, not certified.",
        "research": "Connect plan to ReadyGary beam selection research repo as extension.",
    },
    "ai_ran_digital_twin_research": {
        "title": "Extend 7GC Digital Twin with Measurable Use Case",
        "site": "gary",
        "community": "Urban digital equality scenario needs evidence-backed twin metrics.",
        "technical": "Site profile, metrics table, generated report, diagram, draft PR to 7gc-digital-twin.",
        "research": "Evidence maturity plan — what is stub vs measured?",
    },
}

ASSIGNMENT_TASKS: dict[str, list[str]] = {
    "digital_confidence": [
        "Write a one-page reflection on what digital confidence means in your community.",
        "Create a labeled folder structure and screenshot tour for a practice device.",
        "Draft a safe-email checklist and identify three phishing red flags in sample messages.",
        "Set up a password manager plan (theory) and document MFA steps for one account.",
        "Complete a practice form and export a PDF how-to with screenshots.",
        "Run a practice video meeting checklist and document accessibility settings used.",
        "Create a troubleshooting flowchart for three common learner problems.",
        "Assemble the digital navigation guide sections for your 7GC site capstone.",
    ],
    "software_engineering": [
        "Sketch user stories for a 7GC micro-app and post as GitHub issue.",
        "Build a static HTML page with semantic structure and accessibility notes.",
        "Implement three small functions with tests in Python or JavaScript.",
        "Initialize a Git repo, branch, commit, and open a practice pull request.",
        "Fix a provided buggy script; document root cause in reflection.",
        "Call a public API (or mock JSON) and render results in your page.",
        "Write README, LICENSE note, and reproducibility checklist for your repo.",
        "Integrate team app features and record a 3-minute demo script.",
    ],
    "networking": [
        "Draw OSI layer map for home/school network — label devices.",
        "Calculate subnet for a classroom lab; show your work.",
        "Trace DNS resolution with dig/nslookup transcript (or offline diagram).",
        "Measure Wi-Fi RSSI/latency three times; table results (synthetic ok).",
        "Interpret traceroute output and explain one bottleneck hypothesis.",
        "Draft Edge-IO measurement consent paragraph and metric list.",
        "Write troubleshooting steps for 'cannot reach lesson server'.",
        "Draft connectivity improvement plan sections for capstone.",
    ],
    "cybersecurity": [
        "Explain CIA triad with 7GC examples in plain English.",
        "Document password/MFA policy for a fictional small business.",
        "Analyze three phishing samples; classify and recommend actions.",
        "Hardening checklist for student laptop — justify each item.",
        "Design log fields for a mini-SOC table (no real PII).",
        "Create STRIDE-lite threat model diagram for mobile money case.",
        "Draft incident response checklist with roles and comms plan.",
        "Assemble cyber safety kit deliverables for capstone.",
    ],
    "wireless_dsp_6g": [
        "Explain frequency vs bandwidth with a water-pipe analogy and diagram.",
        "Describe sampling with a classroom audio example — what aliasing means.",
        "Compute simple SNR exercise from provided numbers.",
        "Map Wi-Fi failure modes for a learning hub scenario.",
        "Write latency budget table for interactive lesson (targets, not certified URLLC).",
        "Document NTN fallback storyboard for Graham Land case.",
        "Draft measurement plan linking to edge-io-measurement-node concepts.",
        "Finalize resilience plan and presentation outline.",
    ],
    "ai_ran_digital_twin_research": [
        "Read 7gc-digital-twin README; summarize site profile fields.",
        "Run make e2e in 7gc-digital-twin (or document blocker); capture log excerpt.",
        "Map AI-RAN traffic classes to a campus story — table format.",
        "Tradeoff essay: fairness vs energy vs latency (500 words max).",
        "Draft Edge-IO telemetry packet schema — privacy filtered fields only.",
        "Reproducibility checklist for your twin extension branch.",
        "Outline research poster sections with evidence maturity labels.",
        "Submit capstone: metrics table + report + diagram + PR draft description.",
    ],
}


def generic_week_plan(course_title: str, week: int) -> dict[str, str]:
    return {
        "title": f"Week {week}: Core practice — {course_title}",
        "theory": f"Theory block week {week}",
        "case": "7gc/cross_site/synthetic_fixture",
    }
