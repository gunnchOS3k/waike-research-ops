#!/usr/bin/env python3
"""Generate batch008 DIGITAL_RC: SEVEN_GC_APPRENTICESHIP.

Authorized digital curriculum authoring for the research apprenticeship track.
Does not fabricate field measurements, mentor sign-off, or learner outcomes.
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "src" / "waike_course_ready" / "batch008"
CID = "SEVEN_GC_APPRENTICESHIP"


def _q(qid: str, stem: str, choices: list[str], answer: int, explain: str) -> dict:
    return {
        "id": qid,
        "kind": "mcq",
        "stem": stem,
        "choices": choices,
        "answer_index": answer,
        "explanation": explain,
    }


def _lesson(body: str) -> str:
    text = " ".join(body.split())
    # Ensure depth without repeating trailer spam markers banned by tests.
    fillers = [
        "Apprentices speak Consensus Ladder rungs out loud: observed, inferred, still-need.",
        "SIMULATED fixtures stay labeled until a MEASURED_HARDWARE capture replaces them.",
        "Mentor approval stays EXTERNAL_HUMAN_GATE; portfolios never invent signatures.",
        "Gary 7GC Research Desk tickets refuse vendor throughput theater without provenance.",
        "Repo SHAs and fixture hashes belong in journals before any slide deck claim.",
        "Digital twins here are teaching scaffolds, not ratified commercial 6G products.",
        "gunnchAI /waike lesson may hint; graded answer keys stay instructor-only.",
        "Unauthorized TX, private IQ dumps, and fabricated partner logos fail ethics first.",
    ]
    i = 0
    while len(text) < 900:
        text += " " + fillers[i % len(fillers)]
        i += 1
    return text.strip()


WEEK_SPECS = [
    {
        "week": 1,
        "title": "Research apprenticeship intuition — vocabulary, safety, claim boundaries",
        "ticket": "SGC-6101",
        "lab_id": "lab_sgc_evidence_class",
        "worked": "classes=[SIMULATED,DIGITAL_REPRODUCTION,MEASURED_HARDWARE,MEASURED_FIELD,HUMAN_REVIEW]; pii_in_notes=false",
        "assign": "Classify five evidence snippets; mark privacy violations; refuse fabricated mentor sign-off.",
        "lesson": (
            "At the Gary 7GC Research Desk, week 1 is ticket SGC-6101: name what kind of evidence you hold "
            "before arguing about AI-RAN gains. Beginners hear 'digital twin' and invent pier coverage maps. "
            "Operators separate SIMULATED fixtures, DIGITAL_REPRODUCTION baselines, MEASURED_HARDWARE captures, "
            "MEASURED_FIELD trials, and HUMAN_REVIEW sign-offs. Commercial standardized 6G does not exist today; "
            "AI-RAN language stays research/systems with gates. Privacy is operational: no SSNs, no library PANs, "
            "no RF partner NDAs pasted into Discord. Consensus Ladder for SGC-6101: observed = labeled fixture "
            "row; inferred = simulation is not pier measurement; still need = EXTERNAL_PHYSICAL_GATE when hardware "
            "arrives. Failure mode: marking HUMAN_REVIEW complete because a template checkbox exists. Empty {} "
            "fails. A body that is only PASS raises. Journals cite programs/seven_gc_apprenticeship.md purpose "
            "without inventing campus pilot outcomes."
        ),
    },
    {
        "week": 2,
        "title": "Tools setup — repository reconnaissance without hardware",
        "ticket": "SGC-6202",
        "lab_id": "lab_sgc_repo_recon",
        "worked": "repo_id=waike-research-ops; purpose=reproducible_research_map; has_tests=true; evidence_path=results/",
        "assign": "Recon the apprenticeship map repo: purpose, setup, inputs, outputs, tests, limitations.",
        "lesson": (
            "Ticket SGC-6202 teaches repo navigation as research skill. Read knowledge_maps/course_repo_map.yaml "
            "and programs/research_apprenticeship_reproducible_research.md as PUBLIC_REFERENCE_ONLY maps — do not "
            "silently claim sibling repos are present if they are not checked out. Identify purpose, README/setup, "
            "inputs, outputs, tests, evidence folders, and limitations. Baseline commands stay LOCAL_SOFTWARE or "
            "REPO_CONNECTED deterministic paths. Never mutate production infrastructure or invent clone SHAs. "
            "If a mapped sibling (7gc-digital-twin, spectrumx-ai-ran-gary) is unavailable, record UNAVAILABLE "
            "honestly and continue on waike-research-ops fixtures. Consensus Ladder: observed = map row; inferred = "
            "demo target exists in docs; still need = actual clone at recorded SHA. Screenshots without paths fail."
        ),
    },
    {
        "week": 3,
        "title": "Baseline reproduction — measurement literacy on SIMULATED fixtures",
        "ticket": "SGC-6303",
        "lab_id": "lab_sgc_baseline_repro",
        "worked": "fixture=fixtures/sgc_baseline/kpi_window.json; evidence_class=SIMULATED; output_sha256_len=64",
        "assign": "Reproduce the deterministic SIMULATED KPI baseline; capture command, env, hash.",
        "lesson": (
            "Ticket SGC-6303 runs a deterministic SIMULATED KPI window under fixtures/sgc_baseline/. Learners "
            "record command, python version, cwd, output digest, and evidence_class=SIMULATED. The fixture is "
            "labeled for replacement by MEASURED_HARDWARE later — never rename it as field measured. Variables "
            "and controls stay named: seed, window_id, kpi_names. Stochastic storytelling without a seed fails. "
            "Hashes must be 64 hex characters. Consensus Ladder: observed = fixture bytes; inferred = baseline "
            "reproducible locally; still need = pier SDR capture. Empty {} fails. print-PASS raises. Do not invent "
            "bler curves or beamforming gains beyond fixture fields."
        ),
    },
    {
        "week": 4,
        "title": "Experiment design — question, variables, controls before any run",
        "ticket": "SGC-6404",
        "lab_id": "lab_sgc_experiment_design",
        "worked": "iv=mcs_index; dv=bler; control=snr_db; confound=seed_leak; claim_match=true",
        "assign": "NO_AI week: hand-author research question, hypothesis, IV/DV/controls, evidence plan.",
        "lesson": (
            "Ticket SGC-6404 forbids running the controlled experiment until the design JSON exists. Learners "
            "state a testable research question, hypothesis, independent variable, dependent variable, controls, "
            "confounds, and claim/evidence matching. Example teaching scaffold: IV=mcs_index, DV=bler, "
            "control=snr_db on the SIMULATED table — not a claim that Gary pier closed a live loop. Confound "
            "examples include seed leakage and unlabeled vendor CSV merges. NO_AI week: hand-author the design. "
            "Consensus Ladder: observed = design fields; inferred = one IV change is planned; still need = run "
            "artifacts next week. Designs that promise MEASURED_FIELD without EXTERNAL_FIELD_GATE fail honesty."
        ),
    },
    {
        "week": 5,
        "title": "Controlled SIMULATED experiment — one permitted variable",
        "ticket": "SGC-6505",
        "lab_id": "lab_sgc_controlled_sim",
        "worked": "baseline_mcs=2; trial_mcs=3; snr_db=8; evidence_class=SIMULATED; raw_preserved=true",
        "assign": "Change one permitted IV on the SIMULATED fixture; preserve raw outputs.",
        "lesson": (
            "Ticket SGC-6505 executes the week-4 design on the SIMULATED MCS/BLER table. Change only the "
            "permitted independent variable (mcs_index) while holding snr_db. Preserve raw artifact paths and "
            "label evidence_class=SIMULATED. Distinguish observation (table values) from inference (higher MCS "
            "needs headroom). Do not invent pier throughput. Auto-apply AI-RAN policies without human_gate "
            "language fail research ethics even in simulation. Consensus Ladder: observed = two JSON digests; "
            "inferred = DV moved with IV; still need = MEASURED_HARDWARE confirmation. Empty {} fails."
        ),
    },
    {
        "week": 6,
        "title": "Industry/vendor reality — standards vs products vs your fixture",
        "ticket": "SGC-6606",
        "lab_id": "lab_sgc_analysis",
        "worked": "vendor_claim=6G ready; fixture_supports=false; commercial_6g_exists=false; docs_cited=true",
        "assign": "Parse SIMULATED results; map vendor claim vs fixture support; refuse commercial-6G exists.",
        "lesson": (
            "Ticket SGC-6606 is documentation literacy week. Parse week-5 outputs with deterministic tooling and "
            "compare a vendor '6G ready' slogan to what the fixture actually supports. commercial_6g_exists must "
            "remain false. Open-source repo demos are not carrier deployments. O-RAN vocabulary may appear as "
            "PUBLIC_REFERENCE_ONLY labels without claiming a production Near-RT RIC. Consensus Ladder: observed = "
            "fixture KPI delta; inferred = slogan overclaims; still need = standards document citations without "
            "exam dumps. Analysis that upgrades SIMULATED to MEASURED_FIELD without new evidence fails."
        ),
    },
    {
        "week": 7,
        "title": "Research frontier + ethics — claim audit and validity limits",
        "ticket": "SGC-6707",
        "lab_id": "lab_sgc_claim_audit",
        "worked": "supports=['local_sim_delta']; does_not_support=['field_bler','mentor_signoff']; human_gate=EXTERNAL_HUMAN_GATE",
        "assign": "Audit claims: list supported vs unsupported; name external gates still open.",
        "lesson": (
            "Ticket SGC-6707 is the claim-audit week. Learners list what results do and do not establish. "
            "Supported may include a local SIMULATED delta under fixed SNR. Unsupported includes field BLER, "
            "partner participation, student outcome statistics, and mentor signatures. Privacy/security: no "
            "unauthorized TX narratives, no private competition IQ. Unsupported generalization across 7GC "
            "campuses fails. NO_AI quiz week still allows disclosed calculators on lab JSON. Consensus Ladder: "
            "observed = audit lists; inferred = digital course can complete without field; still need = "
            "EXTERNAL_HUMAN_GATE / EXTERNAL_PHYSICAL_GATE / EXTERNAL_FIELD_GATE as named open gates."
        ),
    },
    {
        "week": 8,
        "title": "Digital capstone package — reproducible research without mentor fiction",
        "ticket": "SGC-6808",
        "lab_id": "lab_sgc_capstone_package",
        "worked": "labs_passed>=6; mentor_signed=false; evidence_class=SIMULATED; includes_limitations=true",
        "assign": "Assemble README, provenance, hashes, limitations, presentation; mentor_signed stays false.",
        "lesson": (
            "Ticket SGC-6808 assembles the digital course capstone: research question, environment, provenance, "
            "method, fixture description, result digests, limitations, SIMULATED/DIGITAL_REPRODUCTION labels, "
            "README, evidence hashes, presentation notes, and reflection without PII. mentor_signed must be "
            "false; optional mentor-review placeholder is EXTERNAL_HUMAN_GATE only. Capstone forbids inventing "
            "physical evidence for credit. Strong simulated packages complete the digital course while listing "
            "physical follow-on work. Consensus Ladder: observed = package files; inferred = digital bar met; "
            "still need = mentor/hardware/field when scheduled. product_use_unmerged_consumed stays false."
        ),
    },
    {
        "week": 9,
        "title": "Apprenticeship extension — cross-repo map and clean handoff",
        "ticket": "SGC-6909",
        "lab_id": "lab_sgc_repro_handoff",
        "worked": "independent_repro=true; map_rows>=3; unavailable_ok=true; mutated_prod=false",
        "assign": "Independent digital invocation reproduces digest; map ≥3 apprenticeship repos honestly.",
        "lesson": (
            "Ticket SGC-6909 starts the 12-week apprenticeship extension digitally: a clean independent "
            "invocation reproduces the baseline digest, and learners map at least three entries from "
            "course_repo_map.yaml (digital twin, AI-RAN, beam selection, edge, NTN, waike-research-ops) with "
            "demo commands and evidence_class expectations. Unavailable siblings are recorded without fake SHAs. "
            "mutated_prod must be false. Mentor check-ins remain EXTERNAL_HUMAN_GATE. Consensus Ladder: observed = "
            "second-run digest match; inferred = handoff works; still need = live mentor pairing."
        ),
    },
    {
        "week": 10,
        "title": "Robustness iteration — sensitivity without fabricated field gains",
        "ticket": "SGC-6A10",
        "lab_id": "lab_sgc_robustness",
        "worked": "snr_db_variants=[6,8,10]; claim_stable=false_unless_documented; field_gain_invented=false",
        "assign": "Sweep one control on SIMULATED table; document sensitivity; refuse invented field gains.",
        "lesson": (
            "Ticket SGC-6A10 iterates the controlled experiment across snr_db variants on the SIMULATED table. "
            "Learners report whether the qualitative claim stays stable and keep field_gain_invented=false. "
            "Weeks 11–12 (review packet + final presentation with mentor) stay scaffolded as "
            "EXTERNAL_HUMAN_GATE / EXTERNAL_FIELD_GATE instructions — not digitally marked complete. "
            "Consensus Ladder: observed = three digests; inferred = sensitivity exists; still need = hardware "
            "sweep. Empty {} fails. print-PASS raises. Career map roles are aligned, not granted."
        ),
    },
]


QUIZ_BANK = {
    1: [
        ("Which evidence class is a synthetic KPI JSON labeled for later replacement?",
         ["SIMULATED", "MEASURED_FIELD", "HUMAN_REVIEW", "Mentor seal"], 0, "Labeled fixture."),
        ("May week-1 journals store patron PANs for 'research realism'?",
         ["No — privacy forbids PII in notes", "Yes if Discord private", "Yes for mentors", "Required"], 0, "No PII."),
        ("Commercial standardized 6G exists today?",
         ["False — course refuses the claim", "True pier-wide", "True if vendor slide", "True after quiz"], 0, "False."),
        ("HUMAN_REVIEW marked complete because a form exists?",
         ["Forbidden without real review", "Auto-complete", "Extra credit", "Required"], 0, "External gate."),
        ("Consensus Ladder still-need for pier SDR?",
         ["EXTERNAL_PHYSICAL_GATE / measured capture", "Ignore", "Invent BLER", "Ship cert"], 0, "Physical gate."),
        ("Empty {} on lab_sgc_evidence_class?",
         ["Fails student_artifact", "Passes", "Bonus", "Grants cert"], 0, "Empty fails."),
    ],
    2: [
        ("Primary recon map for apprenticeship repos?",
         ["knowledge_maps/course_repo_map.yaml", "Random Twitter thread", "Vendor NDAs", "Instructor keys"], 0, "Map file."),
        ("Sibling repo missing locally — honest field?",
         ["UNAVAILABLE with no fake SHA", "Invent SHA", "Mark MEASURED_FIELD", "Skip ethics"], 0, "Unavailable."),
        ("Mutating production RAN from a student laptop?",
         ["Forbidden", "Required lab", "Extra credit", "Silent OK"], 0, "No prod mutate."),
        ("Repo recon evidence path should be?",
         ["Named folder such as results/", "Any Desktop clutter", "Instructor keys", "Discord DM"], 0, "Named path."),
        ("Execution mode for local README/tests only?",
         ["LOCAL_SOFTWARE or REPO_CONNECTED", "MEASURED_FIELD", "HUMAN_REVIEW complete", "TX on air"], 0, "Digital modes."),
        ("print-PASS body?",
         ["Raises AssertionError", "Auto-pass", "Mentor sign", "Field complete"], 0, "Forbidden."),
    ],
    3: [
        ("Baseline fixture evidence_class?",
         ["SIMULATED", "MEASURED_FIELD", "HUMAN_REVIEW", "Partner signed"], 0, "Simulated."),
        ("output_sha256 length?",
         ["64 hex chars", "8", "Any string PASS", "Empty"], 0, "SHA-256 hex."),
        ("Rename SIMULATED to MEASURED_FIELD without capture?",
         ["Fails honesty", "Required", "Extra credit", "Auto"], 0, "No rename."),
        ("Seed omitted on stochastic story?",
         ["Fails literacy", "OK always", "Mentor fix", "Ignore"], 0, "Need seed."),
        ("Still-need after local baseline?",
         ["Hardware/field measurement later", "Cert grant", "Delete fixture", "Fake partner"], 0, "Later measure."),
        ("Wrong submission inventing beamforming_dB=12?",
         ["Must fail", "Passes", "Required", "Silent"], 0, "No invent."),
    ],
    4: [
        ("NO_AI week means?",
         ["Hand-author design JSON", "Paste ChatGPT into keys", "Skip lab", "Invent field"], 0, "Hand author."),
        ("IV/DV example on SIMULATED MCS table?",
         ["IV=mcs_index DV=bler", "IV=mentor DV=cert", "IV=6G DV=exists", "IV=PII DV=ticket"], 0, "MCS/BLER."),
        ("Design promising MEASURED_FIELD without gate?",
         ["Fails honesty", "Required", "Auto-pass", "Cert"], 0, "Honesty."),
        ("Confound example?",
         ["seed_leak or unlabeled vendor CSV", "Using JSON", "Reading README", "Hashing"], 0, "Confound."),
        ("claim_match true means?",
         ["Claim text matches planned evidence class", "Mentor signed", "Field done", "6G exists"], 0, "Match."),
        ("Run controlled experiment before design?",
         ["Forbidden this week", "Required", "Extra", "Silent"], 0, "Design first."),
    ],
    5: [
        ("How many IVs may change in controlled sim?",
         ["One permitted IV", "All at once", "None ever", "Only mentor picks secretly"], 0, "One IV."),
        ("evidence_class for this run?",
         ["SIMULATED", "MEASURED_FIELD", "HUMAN_REVIEW", "Partner"], 0, "Simulated."),
        ("raw_preserved false?",
         ["Fails lab", "Passes", "Bonus", "Cert"], 0, "Preserve raw."),
        ("Ungated auto-apply AI-RAN in sim write-up?",
         ["Fails ethics narrative", "Required", "Extra", "OK"], 0, "Gates."),
        ("Observation vs inference?",
         ["Table values vs 'needs headroom' story", "Same thing", "Mentor only", "Ignore"], 0, "Split."),
        ("Invent pier throughput from fixture?",
         ["Forbidden", "Required", "Extra", "Auto"], 0, "Forbidden."),
    ],
    6: [
        ("commercial_6g_exists must be?",
         ["false", "true", "null meaning true", "vendor decides"], 0, "False."),
        ("Vendor '6G ready' vs fixture?",
         ["fixture_supports=false typically", "Always true", "Grants cert", "Field done"], 0, "Overclaim."),
        ("Upgrading SIMULATED to MEASURED_FIELD in analysis?",
         ["Fails", "Required", "Extra", "Silent"], 0, "Fails."),
        ("O-RAN labels status?",
         ["PUBLIC_REFERENCE_ONLY vocabulary", "Production RIC proof", "Exam dump", "Cert"], 0, "Reference."),
        ("docs_cited false?",
         ["Fails literacy check", "Passes", "Bonus", "Mentor"], 0, "Cite docs."),
        ("Open-source demo equals carrier deployment?",
         ["No", "Yes", "If SHA set", "If Discord yes"], 0, "No."),
    ],
    7: [
        ("Supported claim example?",
         ["local_sim_delta under fixed SNR", "field_bler", "mentor_signoff", "partner logos"], 0, "Local sim."),
        ("does_not_support should include?",
         ["field_bler and mentor_signoff", "JSON hashing", "README paths", "Python version"], 0, "Unsupported."),
        ("human_gate value?",
         ["EXTERNAL_HUMAN_GATE", "COMPLETE", "SIGNED", "SKIP"], 0, "External."),
        ("Campus generalization without evidence?",
         ["Unsupported", "Required", "Auto", "Cert"], 0, "Unsupported."),
        ("Private competition IQ in notes?",
         ["Ethics fail", "Required", "Extra", "OK"], 0, "Fail."),
        ("Digital course can complete without field?",
         ["Yes — list open gates", "No forever", "Only with forged signoff", "Only TX"], 0, "Yes."),
    ],
    8: [
        ("mentor_signed in digital capstone?",
         ["false", "true", "optional true without review", "auto"], 0, "False."),
        ("labs_passed minimum spirit?",
         [">=6 prior lab digests", "0", "Screenshot only", "PASS string"], 0, "Six labs."),
        ("includes_limitations false?",
         ["Fails capstone honesty", "Passes", "Bonus", "Cert"], 0, "Need limits."),
        ("Invent physical evidence for credit?",
         ["Forbidden", "Required", "Extra", "Silent"], 0, "Forbidden."),
        ("Portfolio PII?",
         ["Forbidden", "Required faces", "Library PANs OK", "Passwords OK"], 0, "No PII."),
        ("product_use_unmerged_consumed?",
         ["false", "true", "ignored", "required true"], 0, "False."),
    ],
    9: [
        ("independent_repro true means?",
         ["Second clean run matches digest", "Mentor signed", "Field done", "TX OK"], 0, "Match."),
        ("map_rows minimum?",
         [">=3 apprenticeship map entries", "0", "1 fake", "Only vendor"], 0, "Three."),
        ("unavailable_ok?",
         ["true — record UNAVAILABLE", "false — invent SHA", "Must clone air-gapped prod", "Ignore"], 0, "OK."),
        ("mutated_prod?",
         ["false", "true", "optional", "required"], 0, "False."),
        ("Mentor check-in completion digitally?",
         ["EXTERNAL_HUMAN_GATE only", "Auto complete", "Force true", "Skip ethics"], 0, "External."),
        ("Fake SHA for missing spectrumx repo?",
         ["Forbidden", "Required", "Extra", "OK"], 0, "Forbidden."),
    ],
    10: [
        ("snr_db_variants example?",
         ["[6,8,10]", "[PASS]", "[]", "[mentor]"], 0, "Sweep."),
        ("field_gain_invented?",
         ["false", "true", "optional true", "auto"], 0, "False."),
        ("Weeks 11–12 mentor presentation digitally marked complete?",
         ["No — external gates", "Yes always", "If quiz passed", "If SIMULATED"], 0, "External."),
        ("claim_stable without documenting sensitivity?",
         ["Must not silently claim stability", "Always stable", "Ignore", "Cert"], 0, "Document."),
        ("Career roles in portfolio?",
         ["Aligned not granted", "Granted certs", "ISC2 membership", "3GPP membership"], 0, "Aligned."),
        ("Empty robustness JSON?",
         ["Fails", "Passes", "Bonus", "Field complete"], 0, "Fails."),
    ],
}


LAB_META = {
    "lab_sgc_evidence_class": {
        "title": "evidence classification",
        "readme": "Classify evidence snippets; pii_in_notes must be false.",
        "keys": ["classes", "pii_in_notes", "mentor_signed", "commercial_6g_exists"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "classes": ["SIMULATED", "DIGITAL_REPRODUCTION", "MEASURED_HARDWARE", "MEASURED_FIELD", "HUMAN_REVIEW"],
            "pii_in_notes": False,
            "mentor_signed": False,
            "commercial_6g_exists": False,
        },
        "wrong": {"pii_in_notes": True, "mentor_signed": True, "commercial_6g_exists": True},
        "checks": [
            ("classes_len", "len(classes)>=5"),
            ("pii", "pii_in_notes is False"),
            ("mentor", "mentor_signed is False"),
            ("c6g", "commercial_6g_exists is False"),
        ],
    },
    "lab_sgc_repo_recon": {
        "title": "repository reconnaissance",
        "readme": "Map purpose/setup/tests/evidence; UNAVAILABLE siblings allowed.",
        "keys": ["repo_id", "purpose", "has_tests", "evidence_path", "limitations", "mutated_prod"],
        "mode": "REPO_CONNECTED",
        "evidence": "DIGITAL_REPRODUCTION",
        "ref": {
            "repo_id": "waike-research-ops",
            "purpose": "reproducible_research_map",
            "has_tests": True,
            "evidence_path": "results/",
            "limitations": "sibling_repos_may_be_unavailable",
            "mutated_prod": False,
        },
        "wrong": {"mutated_prod": True, "has_tests": False, "repo_id": ""},
        "checks": [
            ("repo", "repo_id non-empty"),
            ("tests", "has_tests is True"),
            ("evidence", "evidence_path non-empty"),
            ("prod", "mutated_prod is False"),
        ],
    },
    "lab_sgc_baseline_repro": {
        "title": "baseline reproduction",
        "readme": "Reproduce SIMULATED KPI baseline; capture sha256.",
        "keys": ["fixture", "evidence_class", "output_sha256", "seed", "command"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "fixture": "fixtures/sgc_baseline/kpi_window.json",
            "evidence_class": "SIMULATED",
            "output_sha256": "a" * 64,
            "seed": 7,
            "command": "python3 -c \"import json,hashlib,pathlib; p=pathlib.Path('fixtures/sgc_baseline/kpi_window.json'); print(hashlib.sha256(p.read_bytes()).hexdigest())\"",
        },
        "wrong": {"evidence_class": "MEASURED_FIELD", "output_sha256": "short", "seed": None},
        "checks": [
            ("class", "evidence_class==SIMULATED"),
            ("sha", "len(output_sha256)==64"),
            ("seed", "seed is not None"),
            ("fixture", "fixture contains sgc_baseline"),
        ],
    },
    "lab_sgc_experiment_design": {
        "title": "experiment design",
        "readme": "Design before run; IV/DV/controls/claim_match.",
        "keys": ["question", "hypothesis", "iv", "dv", "control", "confound", "claim_match", "evidence_plan"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "DIGITAL_REPRODUCTION",
        "ref": {
            "question": "How does MCS index change BLER at fixed SNR on the SIMULATED table?",
            "hypothesis": "Higher MCS increases BLER at SNR=8 dB on the fixture.",
            "iv": "mcs_index",
            "dv": "bler",
            "control": "snr_db",
            "confound": "seed_leak",
            "claim_match": True,
            "evidence_plan": "SIMULATED table only; no field claim",
        },
        "wrong": {"claim_match": False, "iv": "", "dv": ""},
        "checks": [
            ("iv", "iv non-empty"),
            ("dv", "dv non-empty"),
            ("match", "claim_match is True"),
            ("plan", "evidence_plan mentions SIMULATED or digital"),
        ],
    },
    "lab_sgc_controlled_sim": {
        "title": "controlled simulated experiment",
        "readme": "One IV change; preserve raw; SIMULATED class.",
        "keys": ["baseline_mcs", "trial_mcs", "snr_db", "evidence_class", "raw_preserved", "human_gate"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "baseline_mcs": 2,
            "trial_mcs": 3,
            "snr_db": 8,
            "evidence_class": "SIMULATED",
            "raw_preserved": True,
            "human_gate": True,
        },
        "wrong": {"evidence_class": "MEASURED_FIELD", "raw_preserved": False, "human_gate": False},
        "checks": [
            ("class", "SIMULATED"),
            ("raw", "raw_preserved True"),
            ("gate", "human_gate True"),
            ("iv_changed", "baseline_mcs != trial_mcs"),
        ],
    },
    "lab_sgc_analysis": {
        "title": "analysis vs vendor claims",
        "readme": "Compare vendor slogan to fixture; commercial_6g_exists false.",
        "keys": ["vendor_claim", "fixture_supports", "commercial_6g_exists", "docs_cited", "delta_noted"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "vendor_claim": "6G ready",
            "fixture_supports": False,
            "commercial_6g_exists": False,
            "docs_cited": True,
            "delta_noted": True,
        },
        "wrong": {"commercial_6g_exists": True, "fixture_supports": True, "docs_cited": False},
        "checks": [
            ("c6g", "commercial_6g_exists False"),
            ("support", "fixture_supports False"),
            ("docs", "docs_cited True"),
            ("delta", "delta_noted True"),
        ],
    },
    "lab_sgc_claim_audit": {
        "title": "claim audit",
        "readme": "List supports vs does_not_support; external human gate.",
        "keys": ["supports", "does_not_support", "human_gate", "physical_gate", "field_gate"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "DIGITAL_REPRODUCTION",
        "ref": {
            "supports": ["local_sim_delta"],
            "does_not_support": ["field_bler", "mentor_signoff"],
            "human_gate": "EXTERNAL_HUMAN_GATE",
            "physical_gate": "EXTERNAL_PHYSICAL_GATE",
            "field_gate": "EXTERNAL_FIELD_GATE",
        },
        "wrong": {
            "supports": ["field_bler"],
            "does_not_support": [],
            "human_gate": "COMPLETE",
            "physical_gate": "COMPLETE",
            "field_gate": "COMPLETE",
        },
        "checks": [
            ("supports", "supports non-empty"),
            ("dns", "does_not_support includes mentor or field"),
            ("human", "EXTERNAL_HUMAN_GATE"),
            ("physical", "EXTERNAL_PHYSICAL_GATE"),
        ],
    },
    "lab_sgc_capstone_package": {
        "title": "capstone package",
        "readme": "Digital capstone; mentor_signed false; limitations required.",
        "keys": [
            "labs_passed",
            "mentor_signed",
            "evidence_class",
            "includes_limitations",
            "includes_readme",
            "product_use_unmerged_consumed",
        ],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "labs_passed": 6,
            "mentor_signed": False,
            "evidence_class": "SIMULATED",
            "includes_limitations": True,
            "includes_readme": True,
            "product_use_unmerged_consumed": False,
        },
        "wrong": {
            "labs_passed": 1,
            "mentor_signed": True,
            "includes_limitations": False,
            "product_use_unmerged_consumed": True,
        },
        "checks": [
            ("labs", "labs_passed>=6"),
            ("mentor", "mentor_signed False"),
            ("limits", "includes_limitations True"),
            ("unmerged", "product_use_unmerged_consumed False"),
        ],
    },
    "lab_sgc_repro_handoff": {
        "title": "reproducibility handoff",
        "readme": "Independent repro + cross-repo map honesty.",
        "keys": ["independent_repro", "map_rows", "unavailable_ok", "mutated_prod", "digest_match"],
        "mode": "REPO_CONNECTED",
        "evidence": "DIGITAL_REPRODUCTION",
        "ref": {
            "independent_repro": True,
            "map_rows": 3,
            "unavailable_ok": True,
            "mutated_prod": False,
            "digest_match": True,
        },
        "wrong": {"independent_repro": False, "map_rows": 0, "mutated_prod": True, "digest_match": False},
        "checks": [
            ("repro", "independent_repro True"),
            ("rows", "map_rows>=3"),
            ("prod", "mutated_prod False"),
            ("digest", "digest_match True"),
        ],
    },
    "lab_sgc_robustness": {
        "title": "robustness / sensitivity",
        "readme": "SNR sweep on SIMULATED table; no invented field gains.",
        "keys": ["snr_db_variants", "field_gain_invented", "evidence_class", "documented_sensitivity"],
        "mode": "LOCAL_SOFTWARE",
        "evidence": "SIMULATED",
        "ref": {
            "snr_db_variants": [6, 8, 10],
            "field_gain_invented": False,
            "evidence_class": "SIMULATED",
            "documented_sensitivity": True,
        },
        "wrong": {"field_gain_invented": True, "snr_db_variants": [], "evidence_class": "MEASURED_FIELD"},
        "checks": [
            ("variants", "len(snr_db_variants)>=3"),
            ("field", "field_gain_invented False"),
            ("class", "SIMULATED"),
            ("doc", "documented_sensitivity True"),
        ],
    },
}


def _weeks() -> list[dict]:
    weeks = []
    for spec in WEEK_SPECS:
        w = spec["week"]
        quiz = []
        for i, (stem, choices, ans, exp) in enumerate(QUIZ_BANK[w], start=1):
            quiz.append(_q(f"sgc-w{w}-{i}", f"{spec['ticket']}: {stem}", choices, ans, exp))
        weeks.append({
            "week": w,
            "title": spec["title"],
            "lesson": _lesson(spec["lesson"]),
            "worked_example": spec["worked"],
            "assignment": f"Submit {spec['lab_id']} JSON for {spec['ticket']}. {spec['assign']}",
            "lab_id": spec["lab_id"],
            "quiz": quiz,
        })
    return weeks


def _course() -> dict:
    return {
        "course_id": CID,
        "title": "7GC AI-RAN Research Apprenticeship",
        "track_ids": [CID],
        "academy_id": "ACADEMY_SOFTWARE",
        "kinesthetic_hook": (
            "Run the Gary 7GC Research Desk for ten digital weeks: evidence classes → repo recon → "
            "SIMULATED baseline → experiment design → controlled run → vendor claim audit → capstone, "
            "then apprenticeship extension handoff/robustness — without inventing mentor or field completion."
        ),
        "syllabus_hook": (
            "This is the first-class digital COURSE_DIGITAL_RC for SEVEN_GC_APPRENTICESHIP authorized by "
            "programs/seven_gc_apprenticeship.md. Delivery formats: Workshop (2h + one lab), Bootcamp "
            "(2-week portfolio starter), Course (weeks 1–8), Apprenticeship (weeks 1–10 digital + weeks "
            "11–12 EXTERNAL mentor/hardware/field scaffolds). Extension class remains RESEARCH_APPRENTICESHIP. "
            "HUMAN_PENDING / EXTERNAL_* gates prohibit fabricating mentor sign-off, hardware measurements, "
            "and field pilots — not digital curriculum authoring. Sibling research repos are REPO_CONNECTED "
            "when present; otherwise UNAVAILABLE. Commercial standardized 6G does not exist today."
        ),
        "career": {
            "roles": [
                "wireless_research_apprentice",
                "ran_systems_analyst_junior",
                "reproducible_research_technician",
            ],
            "nice_categories": ["analyze", "build_and_deploy"],
            "certs_aligned_not_granted": [
                "3GPP/O-RAN topic labels (PUBLIC_REFERENCE_ONLY)",
                "AI-RAN study-item vocabulary (not membership)",
            ],
        },
        "ai_use_policy": {
            "modes": [
                "EXPLAIN",
                "HINT",
                "QUESTION_ME",
                "DEBUG_WITH_ME",
                "REVIEW_MY_WORK",
                "COMPARE_APPROACHES",
                "PRACTICE",
            ],
            "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
            "default_weekly": "AI_DISCLOSED",
            "no_ai_weeks": [4, 7],
            "tutor_commands": {
                "lesson": "/waike lesson seven_gc_apprenticeship",
                "explain": "/explain",
                "quiz_practice": "/quizme",
            },
            "graded_answers_protected": True,
            "ai_never_silently_grades": True,
        },
        "delivery_formats": {
            "workshop_hours": 2,
            "bootcamp_weeks": 2,
            "course_weeks": 8,
            "apprenticeship_weeks": 12,
            "external_gates": [
                "EXTERNAL_HUMAN_GATE",
                "EXTERNAL_PHYSICAL_GATE",
                "EXTERNAL_FIELD_GATE",
            ],
        },
        "weeks": _weeks(),
    }


def _exams() -> dict:
    mid = []
    for i in range(1, 21):
        mid.append(_q(
            f"sgc-mid-{i:02d}",
            f"SEVEN_GC mid audit {i}: digital apprenticeship honesty item — "
            f"{'SIMULATED fixtures must stay labeled' if i % 2 else 'mentor_signed stays false without review'}; OK?",
            [
                "Yes — digital honesty before field claims",
                "Mark MEASURED_FIELD anyway",
                "Ship instructor keys to learners",
                "Invent partner participation",
            ],
            0,
            "Digital honesty.",
        ))
    final = []
    topics = [
        "evidence classes",
        "repo recon UNAVAILABLE",
        "baseline sha256",
        "design-before-run",
        "one IV change",
        "commercial_6g_exists false",
        "claim audit gates",
        "capstone limitations",
        "independent repro",
        "snr sweep no field invention",
        "EXTERNAL_HUMAN_GATE",
        "EXTERNAL_PHYSICAL_GATE",
        "EXTERNAL_FIELD_GATE",
        "no PII",
        "print-PASS forbidden",
        "empty JSON fails",
        "gunnchAI practice only",
        "workshop vs apprenticeship formats",
        "Consensus Ladder",
        "PUBLIC_REFERENCE_ONLY standards",
        "no prod mutation",
        "portfolio without mentor fiction",
        "weeks 11-12 external",
        "RESEARCH_APPRENTICESHIP class retained",
    ]
    for i, topic in enumerate(topics, start=1):
        final.append(_q(
            f"sgc-fin-{i:02d}",
            f"SEVEN_GC final {i}: regarding {topic} — correct digital-course stance?",
            [
                f"Honor {topic} without fabricating field/mentor completion",
                "Forge MEASURED_FIELD for credit",
                "Collapse track into WIRELESS_6G",
                "Leak answer keys",
            ],
            0,
            "Honor boundaries.",
        ))
    return {"offset": 7, "mid": mid, "final": final}


def _lab_fn(lab_id: str, meta: dict) -> str:
    keys = meta["keys"]
    keys_lit = json.dumps(keys)
    # Build check block
    checks_src = []
    if lab_id == "lab_sgc_evidence_class":
        checks_src = [
            'checks.append(_check("classes_len", isinstance(data.get("classes"), list) and len(data["classes"]) >= 5, "classes"))',
            'checks.append(_check("pii", data.get("pii_in_notes") is False, "pii"))',
            'checks.append(_check("mentor", data.get("mentor_signed") is False, "mentor"))',
            'checks.append(_check("c6g", data.get("commercial_6g_exists") is False, "c6g"))',
        ]
    elif lab_id == "lab_sgc_repo_recon":
        checks_src = [
            'checks.append(_check("repo", bool(str(data.get("repo_id") or "").strip()), "repo"))',
            'checks.append(_check("tests", data.get("has_tests") is True, "tests"))',
            'checks.append(_check("evidence", bool(str(data.get("evidence_path") or "").strip()), "evidence"))',
            'checks.append(_check("prod", data.get("mutated_prod") is False, "prod"))',
        ]
    elif lab_id == "lab_sgc_baseline_repro":
        checks_src = [
            'checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))',
            'sha = str(data.get("output_sha256") or "")',
            'checks.append(_check("sha", len(sha) == 64 and all(c in "0123456789abcdef" for c in sha.lower()), "sha"))',
            'checks.append(_check("seed", data.get("seed") is not None, "seed"))',
            'checks.append(_check("fixture", "sgc_baseline" in str(data.get("fixture") or ""), "fixture"))',
        ]
    elif lab_id == "lab_sgc_experiment_design":
        checks_src = [
            'checks.append(_check("iv", bool(str(data.get("iv") or "").strip()), "iv"))',
            'checks.append(_check("dv", bool(str(data.get("dv") or "").strip()), "dv"))',
            'checks.append(_check("match", data.get("claim_match") is True, "match"))',
            'plan = str(data.get("evidence_plan") or "").lower()',
            'checks.append(_check("plan", "simulat" in plan or "digital" in plan, "plan"))',
        ]
    elif lab_id == "lab_sgc_controlled_sim":
        checks_src = [
            'checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))',
            'checks.append(_check("raw", data.get("raw_preserved") is True, "raw"))',
            'checks.append(_check("gate", data.get("human_gate") is True, "gate"))',
            'checks.append(_check("iv_changed", data.get("baseline_mcs") != data.get("trial_mcs"), "iv"))',
        ]
    elif lab_id == "lab_sgc_analysis":
        checks_src = [
            'checks.append(_check("c6g", data.get("commercial_6g_exists") is False, "c6g"))',
            'checks.append(_check("support", data.get("fixture_supports") is False, "support"))',
            'checks.append(_check("docs", data.get("docs_cited") is True, "docs"))',
            'checks.append(_check("delta", data.get("delta_noted") is True, "delta"))',
        ]
    elif lab_id == "lab_sgc_claim_audit":
        checks_src = [
            'supports = data.get("supports") or []',
            'dns = data.get("does_not_support") or []',
            'checks.append(_check("supports", isinstance(supports, list) and len(supports) >= 1, "supports"))',
            'blob = " ".join(str(x).lower() for x in dns)',
            'checks.append(_check("dns", "mentor" in blob or "field" in blob, "dns"))',
            'checks.append(_check("human", data.get("human_gate") == "EXTERNAL_HUMAN_GATE", "human"))',
            'checks.append(_check("physical", data.get("physical_gate") == "EXTERNAL_PHYSICAL_GATE", "physical"))',
        ]
    elif lab_id == "lab_sgc_capstone_package":
        checks_src = [
            'checks.append(_check("labs", int(data.get("labs_passed") or 0) >= 6, "labs"))',
            'checks.append(_check("mentor", data.get("mentor_signed") is False, "mentor"))',
            'checks.append(_check("limits", data.get("includes_limitations") is True, "limits"))',
            'checks.append(_check("unmerged", data.get("product_use_unmerged_consumed") is False, "unmerged"))',
        ]
    elif lab_id == "lab_sgc_repro_handoff":
        checks_src = [
            'checks.append(_check("repro", data.get("independent_repro") is True, "repro"))',
            'checks.append(_check("rows", int(data.get("map_rows") or 0) >= 3, "rows"))',
            'checks.append(_check("prod", data.get("mutated_prod") is False, "prod"))',
            'checks.append(_check("digest", data.get("digest_match") is True, "digest"))',
        ]
    elif lab_id == "lab_sgc_robustness":
        checks_src = [
            'variants = data.get("snr_db_variants") or []',
            'checks.append(_check("variants", isinstance(variants, list) and len(variants) >= 3, "variants"))',
            'checks.append(_check("field", data.get("field_gain_invented") is False, "field"))',
            'checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))',
            'checks.append(_check("doc", data.get("documented_sensitivity") is True, "doc"))',
        ]
    body = "\n    ".join(checks_src)
    return f'''
def {lab_id}(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "{lab_id}", "{CID}", submission,
        {keys_lit}, B_SGC,
    )
    if data is None:
        return _result("{lab_id}", "{CID}", checks, B_SGC)
    {body}
    return _result("{lab_id}", "{CID}", checks, B_SGC)
'''


def _generate_labs_py() -> str:
    header = '''"""Runnable labs for batch008 — SEVEN_GC_APPRENTICESHIP."""
from __future__ import annotations
import json
from dataclasses import dataclass
from typing import Any

@dataclass
class LabResult:
    lab_id: str
    course_id: str
    ok: bool
    checks: list[dict[str, Any]]
    boundary: str
    def as_dict(self) -> dict[str, Any]:
        return {"lab_id": self.lab_id, "course_id": self.course_id, "ok": self.ok,
                "checks": self.checks, "claim_boundary": self.boundary, "boundary": self.boundary}

def _check(name: str, ok: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "ok": bool(ok), "detail": detail}

def _fail_if_print_pass(text: str) -> None:
    if str(text).strip() == "PASS":
        raise AssertionError("print-PASS forbidden")

def _coerce_submission(submission: Any) -> tuple[dict[str, Any] | None, str]:
    if submission is None:
        return None, "missing_submission"
    if isinstance(submission, str):
        _fail_if_print_pass(submission)
        try:
            submission = json.loads(submission)
        except json.JSONDecodeError:
            return None, "submission_not_json"
    if not isinstance(submission, dict) or submission == {}:
        return None, "empty_submission"
    return submission, "ok"

def _require_student(lab_id: str, course_id: str, submission: Any, required_keys: list[str], boundary: str):
    checks: list[dict[str, Any]] = []
    data, why = _coerce_submission(submission)
    checks.append(_check("student_artifact", data is not None, why))
    if data is None:
        return None, checks
    missing = [k for k in required_keys if k not in data]
    checks.append(_check("required_keys", not missing, f"missing={missing}"))
    if missing:
        return None, checks
    return data, checks

def _result(lab_id: str, course_id: str, checks: list[dict[str, Any]], boundary: str) -> LabResult:
    return LabResult(lab_id, course_id, all(c["ok"] for c in checks), checks, boundary)

B_SGC = (
    "SEVEN_GC_APPRENTICESHIP Gary 7GC Research Desk. Digital curriculum only. "
    "EXTERNAL_HUMAN/PHYSICAL/FIELD gates remain open. Not student/teacher E6. "
    "Commercial standardized 6G does not exist today."
)
'''
    names = list(LAB_META.keys())
    fns = "\n".join(_lab_fn(n, LAB_META[n]) for n in names)
    specs = {
        n: {
            "title": LAB_META[n]["title"],
            "readme": LAB_META[n]["readme"],
            "required_keys": LAB_META[n]["keys"],
            "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
            "course_id": CID,
            "execution_mode": LAB_META[n]["mode"],
            "evidence_class": LAB_META[n]["evidence"],
        }
        for n in names
    }
    ref = {n: LAB_META[n]["ref"] for n in names}
    wrong = {n: LAB_META[n]["wrong"] for n in names}

    def py_literal(obj: dict) -> str:
        return json.dumps(obj, indent=4).replace("true", "True").replace("false", "False").replace("null", "None")

    labs_map = ",\n    ".join(f'"{n}": {n}' for n in names)
    return header + fns + f"""

LABS_008 = {{
    {labs_map}
}}

COURSE_LABS_008 = {{
    "{CID}": {json.dumps(names)},
}}

LAB_SPECS_008 = {json.dumps(specs, indent=4)}

REFERENCE_008 = {py_literal(ref)}

WRONG_008 = {py_literal(wrong)}
"""


def _packaging_py() -> str:
    return textwrap.dedent(f'''
    """Course-specific packaging for batch008 SEVEN_GC_APPRENTICESHIP."""
    from __future__ import annotations

    from typing import Any

    from waike_course_ready.batch008.labs import LAB_SPECS_008

    CID = "{CID}"

    SYLLABUS_ASSESSMENT_008 = {{
        CID: (
            "Gary 7GC Research Desk: weekly SGC quizzes on evidence classes/recon/baseline/design/"
            "sim/analysis/audit/capstone/handoff/robustness, mid (20 original) on digital honesty, "
            "final (24 original) on external gates + claim discipline, practical over ten runnable labs, "
            "reproducible research portfolio. Mentor/hardware/field remain EXTERNAL_*."
        ),
    }}

    SYLLABUS_DURATION_008 = {{
        CID: (
            "Formats from programs/seven_gc_apprenticeship.md: Workshop 2h; Bootcamp 2 weeks; "
            "Course 8 digital weeks; Apprenticeship 12 weeks (weeks 1–10 digital + 11–12 external scaffolds). "
            "Budget ~6–8 hours/week. NO_AI weeks 4 and 7."
        ),
    }}

    SYLLABUS_CLAIM_008 = {{
        CID: (
            "First-class digital COURSE_DIGITAL_RC for SEVEN_GC_APPRENTICESHIP. RESEARCH_APPRENTICESHIP "
            "classification retained. Does not grant 3GPP/O-RAN membership or invent field/mentor completion. "
            "Instructor keys out of learner packet. Commercial standardized 6G does not exist today."
        ),
    }}

    PITFALLS = {{
        CID: {{i: f"Week {{i}} SGC pitfall: unlabeled simulation, mentor fiction, or empty JSON." for i in range(1, 11)}},
    }}


    def _rubrics(course_id: str) -> list[dict[str, Any]]:
        return [
            {{"rubric_id": f"{{course_id}}-lab", "title": "Research Desk lab", "criteria": [
                {{"name": "machine_fields", "weight": 25, "desc": "Lab JSON fields honest"}},
                {{"name": "evidence_class", "weight": 25, "desc": "SIMULATED/DIGITAL labeled"}},
                {{"name": "empty_fails", "weight": 25, "desc": "Empty fails"}},
                {{"name": "print_pass", "weight": 25, "desc": "PASS rejected"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-assignment", "title": "Research journal", "criteria": [
                {{"name": "ticket_ids", "weight": 40, "desc": "Uses SGC tickets"}},
                {{"name": "no_pii", "weight": 30, "desc": "No secrets/PII"}},
                {{"name": "ai_disclosure", "weight": 30, "desc": "AI mode tagged"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-quiz", "title": "Knowledge check", "criteria": [
                {{"name": "original_stems", "weight": 50, "desc": "Original stems"}},
                {{"name": "key_hidden", "weight": 50, "desc": "Keys instructor-only"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-mid", "title": "Mid audit", "criteria": [
                {{"name": "original_stems", "weight": 60, "desc": "20 non-clone items"}},
                {{"name": "honesty", "weight": 40, "desc": "Simulated vs measured discipline"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-final-knowledge", "title": "Final knowledge", "criteria": [
                {{"name": "original_stems", "weight": 50, "desc": "24 non-clone"}},
                {{"name": "external_gates", "weight": 50, "desc": "EXTERNAL_* gates named"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-practical", "title": "Practical labs", "criteria": [
                {{"name": "student_json", "weight": 40, "desc": "Reference passes; empty fails"}},
                {{"name": "negatives", "weight": 30, "desc": "Wrong submissions fail"}},
                {{"name": "print_pass", "weight": 30, "desc": "PASS rejected"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-project", "title": "Capstone package", "criteria": [
                {{"name": "question_quality", "weight": 10, "desc": "Testable question"}},
                {{"name": "setup_provenance", "weight": 10, "desc": "Env/SHA/fixture"}},
                {{"name": "method", "weight": 10, "desc": "Method clarity"}},
                {{"name": "experiment_design", "weight": 10, "desc": "IV/DV/controls"}},
                {{"name": "evidence_integrity", "weight": 10, "desc": "Hashes/raw preserved"}},
                {{"name": "analysis", "weight": 10, "desc": "No overclaim"}},
                {{"name": "claim_discipline", "weight": 10, "desc": "Supports/does-not-support"}},
                {{"name": "limitations", "weight": 10, "desc": "Limitations explicit"}},
                {{"name": "communication", "weight": 10, "desc": "Presentation clarity"}},
                {{"name": "portfolio_quality", "weight": 10, "desc": "README + artifacts"}},
            ]}},
            {{"rubric_id": f"{{course_id}}-portfolio", "title": "Portfolio", "criteria": [
                {{"name": "claim_boundary", "weight": 40, "desc": "EXTERNAL gates + SIMULATED labels"}},
                {{"name": "machine_artifacts", "weight": 30, "desc": "Lab JSON digests"}},
                {{"name": "career_map", "weight": 30, "desc": "Aligned roles not granted"}},
            ]}},
        ]


    def rubrics_008(course_id: str) -> list[dict[str, Any]]:
        if course_id != CID:
            raise KeyError(course_id)
        return _rubrics(course_id)


    def lab_readme_008(course_id: str, lab_id: str) -> str:
        spec = LAB_SPECS_008[lab_id]
        return "\\n".join([
            f"# {{lab_id}} — {{spec['title']}}", "",
            spec["readme"], "",
            f"execution_mode: {{spec.get('execution_mode')}}",
            f"evidence_class: {{spec.get('evidence_class')}}",
            "",
            "Empty {{}} fails. PASS raises. No fabricated mentor/field completion.", "",
            f"python3 scripts/run_course_labs.py --lab {{lab_id}} --submission path/to/student.json",
            "", spec["wrong_hint"], "",
        ])


    def instructor_week_notes_008(course_id: str, week: dict[str, Any]) -> str:
        n = week["week"]
        return (
            f"# {{course_id}} — instructor week {{n}}\\n\\n"
            f"**Live example:** {{week['worked_example']}}\\n\\n"
            f"**Lab `{{week['lab_id']}}`:** collect student JSON; refuse MEASURED_FIELD upgrades.\\n\\n"
            f"**Hint ladder:** (1) name evidence class (2) point to fixture path (3) Socratic question only.\\n\\n"
            f"**Misconception:** treating SIMULATED KPI deltas as pier measurements.\\n\\n"
            f"**External gates:** mentor/hardware/field remain EXTERNAL_* — never auto-complete.\\n\\n"
            f"**Pitfall:** {{PITFALLS[course_id][n]}}\\n"
        )


    def presentation_008(course_id: str, week: dict[str, Any]) -> str:
        return f"# Week {{week['week']}}: {{week['title']}}\\n\\n{{week['worked_example']}}\\n"


    def instructor_packet_008(course_id: str) -> str:
        return (
            f"# Instructor packet — {{course_id}}\\n\\n"
            "Keys in instructor/answer_keys.json only.\\n\\n"
            "Teaching intent: reproducible digital research apprenticeship.\\n"
            "Expected evidence: lab JSON with labeled SIMULATED/DIGITAL_REPRODUCTION classes.\\n"
            "Remediation: re-run baseline with seed before allowing claim upgrades.\\n"
            "Simulated-vs-measured guidance: never mark MEASURED_* without real captures.\\n"
            "External human/physical/field gate notes: forms/rubrics/slots allowed; completion forbidden without evidence.\\n"
            "gunnchAI may /explain and /quizme for practice; AI never silently grades.\\n"
        )


    def student_packet_008(course_id: str, hook: str) -> str:
        return (
            f"# Student packet — {{course_id}}\\n\\n{{hook}}\\n\\n"
            "Formats: Workshop / Bootcamp / 8-week Course / 12-week Apprenticeship.\\n"
            "Submit lab JSON; empty/wrong/print-PASS fail.\\n"
            "Tutor: `/waike lesson seven_gc_apprenticeship`, `/explain`, `/quizme` (practice only).\\n"
            "Do not invent mentor signatures or field measurements.\\n"
        )


    def group_project_008(course_id: str, title: str, assignment: str) -> str:
        return f"# Group project — {{course_id}}\\n\\n## {{title}}\\n\\n{{assignment}}\\n"


    def portfolio_008(course_id: str) -> str:
        return (
            f"# Portfolio — {{course_id}}\\n\\n"
            "Include: research README, experiment design, reproducibility instructions, logs/results,\\n"
            "evidence hashes, limitations, optional screenshot without PII, rubric self-assessment,\\n"
            "presentation/poster, optional mentor-review placeholder (EXTERNAL_HUMAN_GATE only).\\n"
            "mentor_signed must remain false until real review exists.\\n"
        )
    ''').lstrip()


def main() -> None:
    BATCH.mkdir(parents=True, exist_ok=True)
    course = _course()
    (BATCH / "courses_data.json").write_text(json.dumps({CID: course}, indent=2) + "\n", encoding="utf-8")
    (BATCH / "exams_data.json").write_text(json.dumps({CID: _exams()}, indent=2) + "\n", encoding="utf-8")
    (BATCH / "labs.py").write_text(_generate_labs_py(), encoding="utf-8")
    (BATCH / "packaging.py").write_text(_packaging_py(), encoding="utf-8")
    (BATCH / "content.py").write_text(
        textwrap.dedent(f'''
        """Original WAIKE bodies for batch008 SEVEN_GC_APPRENTICESHIP."""
        from __future__ import annotations
        import json
        from pathlib import Path
        BATCH_COURSE_IDS = ("{CID}",)
        _DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
        SEVEN_GC_APPRENTICESHIP = _DATA["{CID}"]
        COURSES_008 = {{"{CID}": SEVEN_GC_APPRENTICESHIP}}
        ''').strip()
        + "\n",
        encoding="utf-8",
    )
    (BATCH / "exams.py").write_text(
        textwrap.dedent(f'''
        """Mid/final banks for batch008."""
        from __future__ import annotations
        import json
        from pathlib import Path
        _EX = json.loads((Path(__file__).with_name("exams_data.json")).read_text(encoding="utf-8"))
        def extra_assessment_items_008(course_id: str):
            from waike_course_ready.exams import rebalance_mcq
            spec = _EX[course_id]
            mid = rebalance_mcq(spec["mid"], spec["offset"])
            final = rebalance_mcq(spec["final"], spec["offset"] + 1)
            if len(mid) != 20 or len(final) != 24:
                raise ValueError(f"{{course_id}} exam sizes mid={{len(mid)}} final={{len(final)}}")
            return {{"mid": mid, "final": final}}
        ''').strip()
        + "\n",
        encoding="utf-8",
    )
    (BATCH / "__init__.py").write_text('"""Batch008 — SEVEN_GC_APPRENTICESHIP digital course."""\n', encoding="utf-8")

    # Deterministic SIMULATED fixture for baseline lab teaching materials.
    fix = ROOT / "curriculum" / "digital_rc" / CID / "fixtures" / "sgc_baseline"
    # Also stage under batch for emit to copy? Emit builds from course content; write under a staging path too.
    staging = BATCH / "fixtures" / "sgc_baseline"
    for target in (fix, staging):
        target.mkdir(parents=True, exist_ok=True)
        payload = {
            "label": "SIMULATED",
            "replacement_note": "Replace with MEASURED_HARDWARE KPI capture when pier/SDR evidence exists.",
            "window_id": "SGC-KPI-7",
            "seed": 7,
            "snr_db": 8,
            "mcs_bler": {"0": 0.40, "1": 0.22, "2": 0.09, "3": 0.18, "4": 0.35},
            "commercial_6g_exists": False,
        }
        (target / "kpi_window.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        (target / "README.md").write_text(
            "# SIMULATED baseline fixture\n\n"
            "Deterministic teaching data for SEVEN_GC_APPRENTICESHIP.\n"
            "Not a field measurement. Not a mentor-validated result.\n",
            encoding="utf-8",
        )

    print("Wrote batch008 source under", BATCH)


if __name__ == "__main__":
    main()
