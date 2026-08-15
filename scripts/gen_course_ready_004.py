#!/usr/bin/env python3
"""Generate WAIKE-COURSE-READY-004 (WIRELESS_6G, ROBOTICS_CONTROL, GAME_DEV_INTERACTIVE)."""
from __future__ import annotations

import json
import math
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "waike_course_ready" / "batch004"
ALIGN = ROOT / "curriculum" / "alignment"
OUT.mkdir(parents=True, exist_ok=True)
ALIGN.mkdir(parents=True, exist_ok=True)


def q(qid, stem, choices, ai, explanation):
    return {
        "id": qid,
        "kind": "mcq",
        "stem": stem,
        "choices": choices,
        "answer_index": ai,
        "explanation": explanation,
    }


def ensure_lesson(body: str, tag: str = "") -> str:
    """Require substantive authored depth. Never pad with Detail-mark / rotating trailers."""
    del tag  # tag kept for call-site compatibility; must not be injected into body
    body = textwrap.dedent(body).strip()
    low = body.lower()
    for bad in (
        "operator note: record evidence before changing shared systems",
        "evidence discipline week",
        "evidence for this week lives in the submitted lab json",
        "not in a screenshot of a green checkmark",
        "detail mark",
        "operators keep a numbered ticket trail for",
        "whiteboard the worked numbers before opening any gui",
        "if a volunteer asks for a certificate selfie",
        "keep journals free of patron faces, passwords, and fabricated impact statistics",
        "when tools disagree, name the observation first, then the inference",
        "ticket arithmetic checkpoint",
        "restate the worked example in your own symbols",
    ):
        if bad in low:
            raise ValueError(f"padding marker present: {bad}")
    # Import locally to avoid generator import cycles when run as a script.
    sys_path_note = ""  # placate linters; real check uses length only here
    del sys_path_note
    if len(body) < 871:
        raise ValueError(f"lesson too short for #45 post-collapse floor: {len(body)} < 871")
    return body


AI = {
    "modes": [
        "EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME",
        "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE",
    ],
    "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
    "default_weekly": "AI_DISCLOSED",
}


def mk_week(n, title, lesson, worked, assignment, lab_id, quiz):
    assert len(quiz) == 6
    return {
        "week": n,
        "title": title,
        "lesson": ensure_lesson(lesson, tag=f"w{n}-{lab_id}"),
        "worked_example": worked,
        "assignment": assignment,
        "lab_id": lab_id,
        "quiz": quiz,
    }


# ===================== COURSES =====================

WIRELESS = {
    "course_id": "WIRELESS_6G",
    "title": "Wireless / 5G-Advanced / NTN / AI-RAN — Pier Radio Bench",
    "track_ids": ["WIRELESS_6G"],
    "academy_id": "ACADEMY_NETWORKING",
    "kinesthetic_hook": (
        "Run the Gary Pier Radio Bench for ten weeks: FSPL → OFDM → 5G-Advanced → NTN LEO "
        "delay → AI-RAN gated policy. Commercial standardized 6G does NOT exist today."
    ),
    "syllabus_hook": (
        "Honest wireless engineering on fixtures: Friis math, numerology, Release topic labels, "
        "NTN light-time, O-RAN vocabulary, and AI-RAN gates. No commercial-6G brochure claims. "
        "3GPP/IEEE names are PUBLIC_REFERENCE_ONLY."
    ),
    "career": {
        "roles": ["rf_lab_technician", "ran_ops_junior", "wireless_research_apprentice"],
        "nice_categories": ["analyze", "build_and_deploy"],
        "certs_aligned_not_granted": [
            "CompTIA Network+ (wireless domains)",
            "3GPP 5G NR overview (PUBLIC_REFERENCE_ONLY)",
        ],
    },
    "ai_use_policy": {**AI, "no_ai_weeks": [3, 8]},
    "weeks": [
        mk_week(
            1,
            "Pier Radio Bench — free-space path loss without marketing",
            """
            The Pier Radio Bench sits under the Gary pier canopy: a USRP-class SDR, a scratched
            ThinkPad, and a laminated card that says COMMERCIAL_STANDARDIZED_6G=false. Week 1 is
            ticket WR-4101. Beginners want a 6G slide deck. Operators compute free-space path loss
            for a 3.5 GHz pier hop at 120 m using FSPL_dB = 20*log10(d_m) + 20*log10(f_MHz) - 27.55.

            Plug numbers on paper before any GUI: d=120, f=3500. That is the only number the lab
            accepts. Pasting a vendor '6G ready' banner into the journal fails the claim boundary.

            Consensus Ladder for WR-4101: observed = 120 m tape and 3.5 GHz center; inferred = FSPL
            dominates this short clear hop; still need = pier-railing multipath (week 6).

            Failure mode: claiming 'we have 6G coverage' because a slide said so. Operators speak
            `fixtures/wr4101/fspl.json` with d_m, f_mhz, fspl_db. Invented 6G standard IDs fail.

            Resource rule: light math fixtures only while Product-Use QEMU is busy — no multi-GB
            Sionna/DeepMIMO tarballs on this ticket. Accessibility: journals stay text-first; any
            optional plot needs an alt_text field in the portfolio later.
            """,
            "d=120 m, f=3500 MHz → FSPL ≈ 20*log10(120)+20*log10(3500)-27.55 ≈ 84.9 dB.",
            "Journal WR-4101 with d_m, f_mhz, fspl_db, and commercial-6G=false. Submit lab_fspl_budget.",
            "lab_fspl_budget",
            [
                q("wr-w1-1", "WR-4101 uses which FSPL term?", ["20*log10(120)", "6G_TCI", "Rel-20 MCS", "GEO slot"], 0, "Friis."),
                q("wr-w1-2", "COMMERCIAL_STANDARDIZED_6G card reads?", ["true", "false", "pending", "vendor_true"], 1, "false."),
                q("wr-w1-3", "Forbidden claim on WR-4101?", ["Computed FSPL", "6G coverage from a slide", "3.5 GHz", "120 m"], 1, "No marketing."),
                q("wr-w1-4", "Observation for the hop?", ["Railing multipath measured", "d=120 m and f=3.5 GHz", "6G ratified", "SDR serial"], 1, "Measured."),
                q("wr-w1-5", "Heavy sim download on WR-4101?", ["Required", "Forbidden — fixtures only", "GPU required", "Overnight required"], 1, "Resource."),
                q("wr-w1-6", "Lab rejects?", ["Shown FSPL math", "Invented 6G standard ID", "d_m", "f_mhz"], 1, "No fake IDs."),
            ],
        ),
        mk_week(
            2,
            "OFDM numerology intuition — symbols without a fake 6G waveform",
            """
            Ticket WR-4202 ships a toy OFDM numerology card: Δf=30 kHz, N_sc=12 subcarriers per PRB,
            symbol duration ≈ 1/Δf ignoring CP. Pier operators compute PRB bandwidth = 12*30e3 = 360 kHz
            for scheduling math — not a marketing badge.

            One slot with 14 symbols at μ=1 is a teaching fixture, not a claim the pier ships Rel-18.
            The lab asks for n_sc, delta_f_hz, prb_bw_hz, and symbol_duration_s. Empty JSON fails.
            A print('PASS') string raises AssertionError.

            Consensus Ladder: observed = numerology table; inferred = larger Δf shortens symbols;
            still need = measured Doppler on the pier.

            Failure mode: renaming the week '6G waveform lab' and pasting a vendor constellation
            screenshot with no math. Cyclic prefix is a named omission this week — honesty is skill.
            """,
            "PRB BW = 12×30e3 = 360000 Hz; T_sym ≈ 1/30000 ≈ 33.33 μs (no CP).",
            "Compute PRB BW and symbol duration for WR-4202. Submit lab_ofdm_numerology.",
            "lab_ofdm_numerology",
            [
                q("wr-w2-1", "12 sc @ 30 kHz → PRB BW?", ["360 kHz", "30 kHz", "3.6 MHz", "12 Hz"], 0, "12*30e3."),
                q("wr-w2-2", "T_sym without CP @ 30 kHz?", ["30 μs", "≈33.3 μs", "1 ms", "14 μs"], 1, "1/Δf."),
                q("wr-w2-3", "Week 2 grades?", ["Screenshots", "Numerology fields", "6G badges", "Ephemeris"], 1, "Math."),
                q("wr-w2-4", "CP this week?", ["Fully computed", "Named omission", "Ignored forever", "Equals Δf"], 1, "Honesty."),
                q("wr-w2-5", "Larger Δf does what to T_sym?", ["Lengthens", "Shortens", "Deletes PRBs", "Creates 6G"], 1, "1/Δf."),
                q("wr-w2-6", "print('PASS')?", ["Accepted", "Raises AssertionError", "Half credit", "Skip"], 1, "Forbidden."),
            ],
        ),
        mk_week(
            3,
            "5G-Advanced features map — Release labels without exam dumps",
            """
            Ticket WR-4303 is a feature map: RedCap, XR awareness, NTN early hooks, AI/ML study items —
            all PUBLIC_REFERENCE_ONLY. List ≥3 Release-18/19 topic labels and one non-claim: this course
            does not grant 3GPP membership or dump exam items.

            Lab checks features[] length ≥3 with name+release_tag and commercial_6g_exists=false.
            If commercial_6g_exists is true, the lab fails.

            Consensus Ladder: observed = public overview titles; inferred = 5G-Advanced evolves 5G NR;
            still need = measurements mapping to those titles.

            NO_AI week: hand-write the map. Generative fill inventing 'Rel-20 commercial 6G' fails the
            claim boundary even if grammar is perfect. Alignment file only — no harvested stems.
            """,
            "≥3 features with release tags; commercial_6g_exists=false.",
            "Hand-write WR-4303 feature map. NO_AI. Submit lab_5ga_feature_map.",
            "lab_5ga_feature_map",
            [
                q("wr-w3-1", "commercial_6g_exists?", ["true", "false", "null", "Rel-20"], 1, "false."),
                q("wr-w3-2", "RedCap here is?", ["Exam dump", "PUBLIC_REFERENCE_ONLY label", "6G PHY", "Secret"], 1, "Label."),
                q("wr-w3-3", "Week 3 AI?", ["AI dumps", "NO_AI hand map", "AI writes Rel-20", "Skip"], 1, "NO_AI."),
                q("wr-w3-4", "Min features[]?", ["1", "2", "3", "20"], 2, "≥3."),
                q("wr-w3-5", "5G-Advanced is?", ["New RAT replacing 5G", "Evolutionary on 5G NR", "Commercial 6G", "Wi-Fi 8"], 1, "Evolution."),
                q("wr-w3-6", "Invent Rel-20 commercial 6G row?", ["PASS", "Fails claim boundary", "Extra", "Required"], 1, "Fail."),
            ],
        ),
        mk_week(
            4,
            "Link adaptation toy — MCS vs BLER on a fixture",
            """
            Ticket WR-4404 gives BLER for MCS 0..4 at SNR=8 dB: [0.40,0.22,0.09,0.18,0.35]. Pick the
            highest MCS with BLER ≤ 0.1 → MCS 2 at 0.09. Lab checks snr_db, bler_cap, chosen_mcs,
            bler_at_choice.

            Consensus Ladder: observed = table; inferred = higher MCS needs headroom; still need =
            outer-loop CQI mapping (not claimed).

            Failure mode: always max MCS for 'throughput.' Empty {} fails. PASS string raises.
            Operators speak `fixtures/wr4404/bler_table.json` and defend the choice on a whiteboard.
            """,
            "SNR=8 dB, cap 0.1 → chosen_mcs=2 (BLER 0.09).",
            "Select MCS under BLER cap for WR-4404. Submit lab_mcs_bler.",
            "lab_mcs_bler",
            [
                q("wr-w4-1", "At SNR 8 with given BLER table & cap 0.1, MCS?", ["0", "1", "2", "4"], 2, "0.09."),
                q("wr-w4-2", "Pick MCS 4 for throughput?", ["Correct", "Fails BLER discipline", "Required", "6G"], 1, "Cap."),
                q("wr-w4-3", "bler_at_choice for MCS 2?", ["0.40", "0.09", "0.18", "1.0"], 1, "Table."),
                q("wr-w4-4", "Empty {}?", ["PASS", "Fails student_artifact", "Half", "Auto0"], 1, "Empty."),
                q("wr-w4-5", "Outer-loop CQI claimed?", ["Yes", "No — not claimed", "Rel-20", "NTN only"], 1, "Boundary."),
                q("wr-w4-6", "BLER cap?", ["0.5", "0.1", "0.01", "1.0"], 1, "0.1."),
            ],
        ),
        mk_week(
            5,
            "NTN LEO delay honesty — light-time, not sci-fi maps",
            """
            Ticket WR-4505: LEO altitude 550 km, slant ≈700 km. Light-time ≈ d/c; RTT ≈ 2*d/c.
            c=3e8, d=7e5 → one_way≈2.333 ms, RTT≈4.667 ms. Not GEO-class (~250 ms). Lab fails if
            geo_comparable=true or ntn_as_6g_standard=true.

            Consensus Ladder: observed = altitude card; inferred = ms-class RTT for this toy slant;
            still need = feeder/gateway scheduling (out of scope).

            Marketing fail: 'global 6G NTN' heatmap with no delay math. No constellation sim downloads —
            fixture arithmetic only while Stream A runs.
            """,
            "d=700 km → one_way≈2.333 ms, RTT≈4.667 ms; geo_comparable=false.",
            "Compute NTN light-time for WR-4505. Submit lab_ntn_delay.",
            "lab_ntn_delay",
            [
                q("wr-w5-1", "700 km one-way → ms ≈?", ["0.23", "2.33", "23", "250"], 1, "d/c."),
                q("wr-w5-2", "RTT ≈?", ["2.33 ms", "4.67 ms", "250 ms", "1 s"], 1, "2*d/c."),
                q("wr-w5-3", "geo_comparable?", ["true", "false", "null", "6G"], 1, "false."),
                q("wr-w5-4", "ntn_as_6g_standard?", ["true", "false", "Rel-20", "optional"], 1, "false."),
                q("wr-w5-5", "Heatmap without delay math?", ["PASS", "Marketing fail", "Required", "Extra"], 1, "Fail."),
                q("wr-w5-6", "Altitude class?", ["550 km LEO", "GEO 35786 km", "Wi-Fi", "Undersea"], 0, "LEO."),
            ],
        ),
        mk_week(
            6,
            "Channel tap toy — RMS delay spread on pier railing fixture",
            """
            Ticket WR-4606: delays_ns=[0,120,350], powers_db=[0,-3,-10]. Compute discrete PDP RMS delay
            spread with linear powers. Lab checks tau_rms_ns within tolerance and tap_count=3.

            Multipath is a number, not a vibe. Claiming 'AI beamforming solved multipath' without taps
            fails. PHYSICAL sounding stays PHYSICAL_PENDING.

            Consensus Ladder: observed = tap table; inferred = late energy grows τ_rms; still need =
            measured sounding. Empty {} fails. Wrong τ_rms fails. PASS raises.
            """,
            "Three-tap PDP → compute tau_rms_ns; tap_count=3.",
            "Compute RMS delay spread for WR-4606. Submit lab_delay_spread.",
            "lab_delay_spread",
            [
                q("wr-w6-1", "Tap count?", ["1", "2", "3", "64"], 2, "3."),
                q("wr-w6-2", "Powers unit?", ["dB relative", "watts only", "MCS", "RTT"], 0, "dB."),
                q("wr-w6-3", "AI beamforming claim with no taps?", ["PASS", "Fails week", "Required", "Extra"], 1, "Fail."),
                q("wr-w6-4", "Sounding status?", ["DONE", "PHYSICAL_PENDING", "6G auto", "Skip"], 1, "Pending."),
                q("wr-w6-5", "First tap delay?", ["0 ns", "120 ns", "350 ns", "1 ms"], 0, "0."),
                q("wr-w6-6", "Need tau_rms_ns?", ["No", "Yes", "Screenshot only", "AI only"], 1, "Yes."),
            ],
        ),
        mk_week(
            7,
            "AI-RAN control loop — gated policy, not magic autonomy",
            """
            Ticket WR-4707: observe KPI window → propose MCS/PRB action → human gate → apply.
            Submit observe_kpis, proposed_action, human_gate=true, auto_apply_without_gate=false.
            Ungated auto-apply fails.

            AI-RAN is research/systems with gates — not pier-wide 6G autonomy. NO_AI quiz week.
            Consensus Ladder: observed = KPI CSV; inferred = actions need gates; still need =
            closed-loop field trial evidence (not claimed).
            """,
            "human_gate=true; auto_apply_without_gate=false; action names MCS or PRB.",
            "Author WR-4707 policy JSON. Submit lab_airan_policy.",
            "lab_airan_policy",
            [
                q("wr-w7-1", "auto_apply_without_gate?", ["true", "false", "null", "6G"], 1, "false."),
                q("wr-w7-2", "human_gate?", ["false", "true", "optional", "vendor"], 1, "true."),
                q("wr-w7-3", "AI-RAN this week?", ["Magic", "Gated policy on fixtures", "Commercial 6G", "Dump"], 1, "Gated."),
                q("wr-w7-4", "Field trial claimed?", ["Yes", "No — not claimed", "Rel-20", "Pier-wide"], 1, "Boundary."),
                q("wr-w7-5", "Action should name?", ["Feelings", "MCS or PRB", "6G logo", "GEO"], 1, "Concrete."),
                q("wr-w7-6", "Quiz AI mode?", ["AI dumps", "NO_AI", "Skip", "Auto AI"], 1, "NO_AI."),
            ],
        ),
        mk_week(
            8,
            "Spectrum honesty — masks and no unauthorized TX",
            """
            Ticket WR-4808: lab license narrative at 3.5 GHz, OBW 18 MHz. Submit center_ghz, obw_mhz,
            mask_ok, unauthorized_tx=false. Transmitting outside the narrative 'because SDR' fails ethics.

            Consensus Ladder: observed = license card; inferred = OBW fits mask; still need = real
            FCC/ITU filings (not fabricated). NO_AI week. No fake auction wins in journals.
            """,
            "center 3.5 GHz, OBW 18 MHz, mask_ok true, unauthorized_tx false.",
            "Submit lab_spectrum_mask for WR-4808. No unauthorized TX.",
            "lab_spectrum_mask",
            [
                q("wr-w8-1", "unauthorized_tx?", ["true", "false", "maybe", "6G"], 1, "false."),
                q("wr-w8-2", "OBW?", ["18 MHz", "100 MHz", "1 GHz", "30 kHz"], 0, "18."),
                q("wr-w8-3", "TX outside narrative?", ["Extra", "Ethics fail", "Required", "AI-RAN"], 1, "Fail."),
                q("wr-w8-4", "Fabricate FCC filing?", ["OK", "Forbidden", "Required", "Rel-20"], 1, "No."),
                q("wr-w8-5", "Center?", ["2.4", "3.5 GHz", "28 only", "60"], 1, "3.5."),
                q("wr-w8-6", "mask_ok means?", ["Ignore OOB", "Fixture mask check passed", "6G cert", "NTN"], 1, "Fixture."),
            ],
        ),
        mk_week(
            9,
            "O-RAN interface map — vocabulary without fake RIC production",
            """
            Ticket WR-4909 maps A1/E2/O1/O2 to pier roles. Submit interfaces including A1,E2,O1 and
            deployed_full_ric=false. Production Near-RT RIC claims without E2 logs fail.

            Stay RESEARCH_LAB_SCALE. Consensus Ladder: observed = flashcards; inferred = control split
            exists in O-RAN talk; still need = E2 subscription logs (PHYSICAL_PENDING).

            Failure mode: noun-swapping a Cloud/DevOps deck. Empty {} fails. PASS raises.
            """,
            "interfaces include A1,E2,O1; deployed_full_ric=false.",
            "Submit lab_oran_interfaces for WR-4909.",
            "lab_oran_interfaces",
            [
                q("wr-w9-1", "deployed_full_ric?", ["true", "false", "null", "6G"], 1, "false."),
                q("wr-w9-2", "E2 here is?", ["Dump", "Interface vocabulary", "Commercial 6G", "Wi-Fi"], 1, "Vocab."),
                q("wr-w9-3", "RIC claim without logs?", ["PASS", "Fails", "Required", "Extra"], 1, "Fail."),
                q("wr-w9-4", "Scale?", ["NATIONWIDE", "RESEARCH_LAB_SCALE", "GEO", "CONSUMER_6G"], 1, "Lab."),
                q("wr-w9-5", "A1 in map?", ["Yes", "Never", "NTN only", "Games only"], 0, "Yes."),
                q("wr-w9-6", "E2 logs status?", ["DONE", "PHYSICAL_PENDING", "Fake OK", "Never"], 1, "Pending."),
            ],
        ),
        mk_week(
            10,
            "Capstone radio notebook — no Product-Use unmerged dependency",
            """
            Ticket WR-4910 assembles FSPL, numerology, MCS, NTN delay, AI-RAN gate, and spectrum digests
            into one notebook hash. Capstone forbids consuming unmerged Product-Use packages and forbids
            claiming vendor/3GPP certificates.

            Submit notebook_sha256, includes_commercial_6g_false_statement=true,
            product_use_unmerged_consumed=false, labs_passed≥6.

            Career map: RF lab tech / RAN ops junior — certs aligned not granted. Accessibility:
            text-only summary path required; optional plots need alt_text in portfolio JSON.
            """,
            "product_use_unmerged_consumed=false; commercial_6g false statement; labs_passed≥6.",
            "Ship WR-4910 via lab_radio_capstone. Portfolio + career map.",
            "lab_radio_capstone",
            [
                q("wr-w10-1", "product_use_unmerged_consumed?", ["true", "false", "optional", "required"], 1, "false."),
                q("wr-w10-2", "commercial_6g false statement included?", ["false", "true", "null", "Rel-20"], 1, "true."),
                q("wr-w10-3", "labs_passed min?", ["1", "3", "6", "100"], 2, "≥6."),
                q("wr-w10-4", "Grants 3GPP cert?", ["Yes", "No", "After final", "Auto"], 1, "No."),
                q("wr-w10-5", "Depend on unmerged Product-Use?", ["Yes", "No", "If QEMU", "If AI"], 1, "No."),
                q("wr-w10-6", "Career certs?", ["Granted", "Aligned not granted", "Hidden", "Sold"], 1, "Aligned."),
            ],
        ),
    ],
}


ROBOTICS = {
    "course_id": "ROBOTICS_CONTROL",
    "title": "Robotics and Control — HarborBot Bay",
    "track_ids": ["ROBOTICS_CONTROL"],
    "academy_id": "ACADEMY_HARDWARE",
    "kinesthetic_hook": (
        "Ten weeks in HarborBot Bay: frames → 2R kinematics → PID → traj → sensing → E-stop → "
        "diff-drive → estimation → message schemas → safety capstone. Real commands on fixture math."
    ),
    "syllabus_hook": (
        "Control discipline for a civic pier robot cart: transforms, inverse kinematics checks, "
        "PID with anti-windup notes, trajectory limits, noise-aware sensing, and hard E-stop policy. "
        "ROS topic names are alignment vocabulary only — no claiming a full robot fleet deploy."
    ),
    "career": {
        "roles": ["robotics_technician", "controls_junior", "automation_apprentice"],
        "nice_categories": ["build_and_deploy", "analyze"],
        "certs_aligned_not_granted": [
            "FANUC/ABB operator topic labels (PUBLIC_REFERENCE_ONLY)",
            "OSHA machine-guarding awareness labels (not a license)",
        ],
    },
    "ai_use_policy": {**AI, "no_ai_weeks": [4, 9]},
    "weeks": [
        mk_week(
            1,
            "HarborBot frames — SE(2) pose without cinematic hype",
            """
            HarborBot Bay ticket RB-5101: a diff-drive cart on taped pier coordinates. Pose is (x,y,theta)
            in meters/radians. Students compute a planar transform of a tool point and refuse 'AI nabbed
            the box' stories without a frame diagram.

            Lab checks x, y, theta, tool_x, tool_y after a yaw rotation. Empty {} fails. PASS raises.

            Consensus Ladder: observed = tape origin and tool offset; inferred = rotation mixes x/y;
            still need = wheel slip model (later). Accessibility: ASCII frame diagrams required in journals.
            """,
            "theta=π/2, tool offset (0.2,0) → tool maps to pier axes with sin/cos.",
            "Compute RB-5101 pose/tool map. Submit lab_se2_pose.",
            "lab_se2_pose",
            [
                q("rb-w1-1", "Pose fields?", ["x,y,theta", "RGB only", "MCS", "FSPL"], 0, "SE2."),
                q("rb-w1-2", "Units?", ["m and rad", "deg only", "pixels", "dB"], 0, "SI."),
                q("rb-w1-3", "Empty {}?", ["PASS", "Fails", "Half", "Skip"], 1, "Fail."),
                q("rb-w1-4", "AI nabbed-box claim without frames?", ["OK", "Fails week", "Required", "Extra"], 1, "Fail."),
                q("rb-w1-5", "Journal needs?", ["ASCII frame diagram", "Only TikTok", "Only GPU", "6G"], 0, "A11y."),
                q("rb-w1-6", "print PASS?", ["OK", "Raises", "Half", "Auto"], 1, "Forbidden."),
            ],
        ),
        mk_week(
            2,
            "2R kinematics — reachability before torque myths",
            """
            Ticket RB-5202: planar 2R arm with L1=0.35 m, L2=0.30 m. Forward kinematics to a target and
            a reachability flag when hypot(x,y) > L1+L2. Lab checks x,y, reachable.

            Consensus Ladder: observed = link lengths; inferred = workspace is an annulus/disk bound;
            still need = joint limits map. Failure: claiming infinite reach because 'servos are strong.'
            """,
            "L1=0.35, L2=0.30; point beyond 0.65 m → reachable=false.",
            "FK + reachability for RB-5202. Submit lab_fk_2r.",
            "lab_fk_2r",
            [
                q("rb-w2-1", "Max reach L1+L2?", ["0.65 m", "0.05 m", "2 m", "65 m"], 0, "Sum."),
                q("rb-w2-2", "Beyond max reach?", ["reachable true", "reachable false", "Ignore", "6G"], 1, "False."),
                q("rb-w2-3", "Strong servos imply infinite reach?", ["Yes", "No", "Sometimes", "Always"], 1, "No."),
                q("rb-w2-4", "Lab needs FK x,y?", ["No", "Yes", "Screenshot", "Audio"], 1, "Yes."),
                q("rb-w2-5", "L2 length?", ["0.30 m", "3 m", "30 cm only labeled wrong", "0"], 0, "0.30."),
                q("rb-w2-6", "Joint limits this week?", ["Fully mapped", "Still need later", "Deleted", "AI"], 1, "Later."),
            ],
        ),
        mk_week(
            3,
            "PID on a fixture plant — gains with anti-windup note",
            """
            Ticket RB-5303: discrete PID on e=[1.0,0.6,0.2] with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
            Compute u for the last step with simple rectangular integral and backward diff. Include
            anti_windup_note length ≥8 when integral magnitude is large.

            Consensus Ladder: observed = error series; inferred = D term reacts to slope; still need =
            real motor plant ID. Empty fails. Wrong u fails.
            """,
            "Compute u_last from fixture gains; document anti-windup note.",
            "PID step for RB-5303. Submit lab_pid_step.",
            "lab_pid_step",
            [
                q("rb-w3-1", "dt on fixture?", ["0.1", "1.0", "10", "0"], 0, "0.1."),
                q("rb-w3-2", "Kp?", ["1.2", "12", "0", "100"], 0, "1.2."),
                q("rb-w3-3", "Missing anti_windup when needed?", ["OK", "Fails check", "Extra", "Skip"], 1, "Fail."),
                q("rb-w3-4", "Plant ID claimed done?", ["Yes", "No — still need", "Always", "AI"], 1, "Need."),
                q("rb-w3-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("rb-w3-6", "D term uses?", ["Error slope", "FSPL", "MCS", "BLER"], 0, "Slope."),
            ],
        ),
        mk_week(
            4,
            "Trajectory limits — vmax/amax before cinematic paths",
            """
            Ticket RB-5404: move 1.2 m with vmax=0.4 m/s and amax=0.5 m/s². Compute minimum time for a
            trapezoid/triangle profile bound and reject path_ok if commanded speed exceeds vmax.

            NO_AI week. Consensus Ladder: observed = limits card; inferred = time bounded by v/a;
            still need = curvature limits. Failure: spline that ignores vmax 'because it looks smooth.'
            """,
            "Distance 1.2 m, vmax 0.4, amax 0.5 → compute t_min; path_ok respects vmax.",
            "Trajectory limit check RB-5404. Submit lab_traj_limits. NO_AI.",
            "lab_traj_limits",
            [
                q("rb-w4-1", "vmax?", ["0.4 m/s", "4 m/s", "40", "0"], 0, "0.4."),
                q("rb-w4-2", "Ignore vmax for smooth look?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("rb-w4-3", "AI mode?", ["AI dumps", "NO_AI", "Skip", "Auto"], 1, "NO_AI."),
                q("rb-w4-4", "Distance?", ["1.2 m", "12 m", "0.12", "120"], 0, "1.2."),
                q("rb-w4-5", "amax?", ["0.5", "5", "50", "0"], 0, "0.5."),
                q("rb-w4-6", "Curvature limits?", ["Done", "Still need", "Deleted", "6G"], 1, "Later."),
            ],
        ),
        mk_week(
            5,
            "Sensor noise — mean/std and reject wild outliers",
            """
            Ticket RB-5505: lidar range samples [1.01,1.00,0.99,1.02,3.50] m. Compute mean/std after
            dropping values beyond 1.5×IQR or a hard gate >2.0 m. Lab checks cleaned_n, mean, outlier_dropped.

            Consensus Ladder: observed = samples; inferred = 3.50 is outlier for pier aisle; still need =
            calibrated bias. Failure: trusting raw max as truth.
            """,
            "Drop 3.50; cleaned_n=4; mean≈1.005.",
            "Clean RB-5505 samples. Submit lab_sensor_noise.",
            "lab_sensor_noise",
            [
                q("rb-w5-1", "Outlier in fixture?", ["3.50", "1.00", "0.99", "1.02"], 0, "3.50."),
                q("rb-w5-2", "cleaned_n after drop?", ["5", "4", "1", "0"], 1, "4."),
                q("rb-w5-3", "Trust raw max always?", ["Yes", "No", "AI yes", "Required"], 1, "No."),
                q("rb-w5-4", "Bias calibration?", ["Done", "Still need", "Impossible", "Skip"], 1, "Need."),
                q("rb-w5-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("rb-w5-6", "Hard gate example?", [">2.0 m drop", "Drop all", "Keep 3.50", "Ignore"], 0, "Gate."),
            ],
        ),
        mk_week(
            6,
            "E-stop policy — hard interrupt beats soft hope",
            """
            Ticket RB-5606: E-stop must assert motors_disabled=true, brake_engaged=true, and
            resume_requires_human=true. Software 'slow down' without disable fails.

            Consensus Ladder: observed = E-stop wiring card; inferred = safety power path; still need =
            SIL certification (not claimed). Ethics: never bypass E-stop for a demo video.
            """,
            "motors_disabled, brake_engaged, resume_requires_human all true.",
            "E-stop policy JSON for RB-5606. Submit lab_estop_policy.",
            "lab_estop_policy",
            [
                q("rb-w6-1", "motors_disabled?", ["false", "true", "optional", "AI"], 1, "true."),
                q("rb-w6-2", "Soft slowdown only?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("rb-w6-3", "resume_requires_human?", ["false", "true", "null", "bot"], 1, "true."),
                q("rb-w6-4", "Bypass for demo video?", ["OK", "Ethics fail", "Required", "Extra"], 1, "Fail."),
                q("rb-w6-5", "SIL claimed?", ["Yes", "No — not claimed", "Auto", "Always"], 1, "No."),
                q("rb-w6-6", "brake_engaged?", ["true", "false", "maybe", "skip"], 0, "true."),
            ],
        ),
        mk_week(
            7,
            "Diff-drive ICC — wheel speeds to body twist",
            """
            Ticket RB-5707: wheel base B=0.40 m, r=0.05 m, wheel rates ω_l, ω_r. Compute v and ω_body.
            Lab checks v, omega, and rejects if someone sets B=0.

            Consensus Ladder: observed = encoder rates; inferred = ICC geometry; still need = slip
            compensation. Wrong kinematics fail even if the cart 'looks right' on video.
            """,
            "v=(r/2)*(ω_l+ω_r); ω=(r/B)*(ω_r-ω_l).",
            "Diff-drive map RB-5707. Submit lab_diff_drive.",
            "lab_diff_drive",
            [
                q("rb-w7-1", "Wheel base B?", ["0.40 m", "4 m", "40", "0"], 0, "0.40."),
                q("rb-w7-2", "B=0 allowed?", ["Yes", "No — reject", "Required", "AI"], 1, "Reject."),
                q("rb-w7-3", "v formula uses?", ["ω_l+ω_r", "FSPL", "MCS", "BLER"], 0, "Sum."),
                q("rb-w7-4", "Video-only proof?", ["Enough", "Not enough without math", "Required", "Extra"], 1, "Math."),
                q("rb-w7-5", "r?", ["0.05 m", "0.5", "5", "0"], 0, "0.05."),
                q("rb-w7-6", "Slip compensation?", ["Done", "Still need", "Deleted", "6G"], 1, "Later."),
            ],
        ),
        mk_week(
            8,
            "State estimation toy — fuse odom + range with covariance honesty",
            """
            Ticket RB-5808: scalar fuse x_odom and x_range with variances. Compute Kalman-ish gain
            K = p/(p+r) and x_hat. Lab checks K, x_hat, and refuses cov_zero_lie=true.

            Consensus Ladder: observed = two measurements; inferred = lower variance dominates;
            still need = full EKF on SE2. Failure: claiming perfect certainty (P=0).
            """,
            "K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.",
            "Fuse RB-5808. Submit lab_fuse_scalar.",
            "lab_fuse_scalar",
            [
                q("rb-w8-1", "K formula?", ["p/(p+r)", "p*r", "1", "0"], 0, "Kalman."),
                q("rb-w8-2", "P=0 certainty claim?", ["OK", "Fails cov honesty", "Required", "Extra"], 1, "Fail."),
                q("rb-w8-3", "Full EKF claimed?", ["Yes", "No — still need", "Always", "AI"], 1, "Need."),
                q("rb-w8-4", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("rb-w8-5", "Lower variance does?", ["Ignored", "Dominates fuse", "Deletes robot", "6G"], 1, "Dominates."),
                q("rb-w8-6", "print PASS?", ["OK", "Raises", "Half", "Skip"], 1, "Forbidden."),
            ],
        ),
        mk_week(
            9,
            "Message schemas — /cmd_vel shaped fixtures without fleet claims",
            """
            Ticket RB-5909: validate a cmd_vel-shaped JSON with linear.x and angular.z finite, and
            frame_id='base_link'. Claiming a 50-robot Harbor fleet deploy fails.

            NO_AI week. Consensus Ladder: observed = schema card; inferred = units m/s and rad/s;
            still need = DDS/ROS distro pin (not claimed as production).
            """,
            "linear.x + angular.z finite; frame_id base_link; fleet_claim=false.",
            "Schema check RB-5909. Submit lab_cmd_vel_schema. NO_AI.",
            "lab_cmd_vel_schema",
            [
                q("rb-w9-1", "frame_id?", ["base_link", "map_ai", "6G", "geo"], 0, "base_link."),
                q("rb-w9-2", "Fleet deploy claim?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("rb-w9-3", "AI mode?", ["AI dumps", "NO_AI", "Skip", "Auto"], 1, "NO_AI."),
                q("rb-w9-4", "Units?", ["m/s and rad/s", "deg only", "dB", "MCS"], 0, "SI."),
                q("rb-w9-5", "NaN angular.z?", ["OK", "Fails finite check", "Required", "Extra"], 1, "Fail."),
                q("rb-w9-6", "Production DDS pin claimed?", ["Yes", "No — not claimed", "Always", "AI"], 1, "No."),
            ],
        ),
        mk_week(
            10,
            "Capstone safety packet — E-stop + traj + fuse evidence",
            """
            Ticket RB-5910: assemble E-stop policy, traj limits, and fuse result digests. Capstone
            requires estop_ok=true, labs_passed≥6, and no_device_os_pr=true (do not open device-os PRs).

            Career map: robotics technician / controls junior. Accessibility: emergency procedure
            sheet must be printable large-text. Portfolio forbids fabricated injury statistics.
            """,
            "estop_ok true; labs_passed≥6; no_device_os_pr true.",
            "Ship RB-5910 via lab_robot_capstone. Portfolio + career map.",
            "lab_robot_capstone",
            [
                q("rb-w10-1", "estop_ok?", ["false", "true", "null", "ai"], 1, "true."),
                q("rb-w10-2", "labs_passed min?", ["1", "3", "6", "100"], 2, "≥6."),
                q("rb-w10-3", "Open device-os PR from this course?", ["Yes", "No", "Optional", "Required"], 1, "No."),
                q("rb-w10-4", "Fabricate injury stats?", ["OK", "Forbidden", "Required", "Extra"], 1, "No."),
                q("rb-w10-5", "Career certs?", ["Granted", "Aligned not granted", "Hidden", "Sold"], 1, "Aligned."),
                q("rb-w10-6", "E-stop sheet format?", ["Large-text printable", "Tiny GIF only", "Audio only", "None"], 0, "A11y."),
            ],
        ),
    ],
}


GAMES = {
    "course_id": "GAME_DEV_INTERACTIVE",
    "title": "Game Development — Forge Arcade Studio",
    "track_ids": ["GAME_DEV_INTERACTIVE"],
    "academy_id": "ACADEMY_SOFTWARE",
    "kinesthetic_hook": (
        "Ten Forge Arcade weeks: game loop → AABB → audio clock → entities → levels → input → "
        "optional four-game case studies → playtest metrics → a11y → ship checklist. Case studies are "
        "optional; not dependent on unmerged game branches."
    ),
    "syllabus_hook": (
        "Build interactive media with runnable validators: fixed timestep honesty, collision math, "
        "beat clocks, entity state, and accessibility. Optional case studies may reference four titled "
        "games (anime-aggressors, beatlink-party, earth-species, foot-racing) as PUBLIC examples without "
        "requiring those repos to be merged."
    ),
    "career": {
        "roles": ["gameplay_programmer_junior", "technical_artist_apprentice", "qa_playtest_tech"],
        "nice_categories": ["build_and_deploy", "create"],
        "certs_aligned_not_granted": [
            "Unity Certified Associate topic labels (PUBLIC_REFERENCE_ONLY)",
            "Godot fundamentals topic labels (PUBLIC_REFERENCE_ONLY)",
        ],
    },
    "ai_use_policy": {**AI, "no_ai_weeks": [5, 9]},
    "weeks": [
        mk_week(
            1,
            "Game loop — fixed dt honesty on Forge Arcade",
            """
            Ticket GA-6101: fixed timestep dt=1/60 with accumulator pattern. Lab checks dt, steps,
            spiral_of_death_guard=true when frame_time exceeds 0.25 s clamp. Variable rendering may
            interpolate; simulation steps stay fixed.

            Consensus Ladder: observed = clock card; inferred = fixed dt stabilizes physics; still need =
            profiling on target handheld (PHYSICAL_PENDING). Failure: 'just use delta everywhere' without guard.
            """,
            "dt=1/60; clamp frame_time; spiral_of_death_guard true.",
            "Implement GA-6101 loop JSON. Submit lab_game_loop.",
            "lab_game_loop",
            [
                q("ga-w1-1", "dt?", ["1/60", "1", "0", "60"], 0, "Fixed."),
                q("ga-w1-2", "spiral_of_death_guard?", ["false", "true", "null", "ai"], 1, "true."),
                q("ga-w1-3", "Variable dt only forever?", ["Best", "Fails discipline", "Required", "Extra"], 1, "Fail."),
                q("ga-w1-4", "Handheld profiling?", ["DONE", "PHYSICAL_PENDING", "Skip", "Fake OK"], 1, "Pending."),
                q("ga-w1-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w1-6", "print PASS?", ["OK", "Raises", "Half", "Skip"], 1, "Forbidden."),
            ],
        ),
        mk_week(
            2,
            "AABB collision — overlap math before particle fireworks",
            """
            Ticket GA-6202: two AABBs. Compute overlap on x and y; hit if both overlap. Lab checks
            hit, overlap_x, overlap_y. Failure: particle VFX as 'proof' of collision without math.

            Consensus Ladder: observed = rects; inferred = separating-axis for AABB; still need = swept
            tests for tunnels. Empty fails.
            """,
            "hit = overlap_x and overlap_y; report both overlaps.",
            "AABB test GA-6202. Submit lab_aabb_hit.",
            "lab_aabb_hit",
            [
                q("ga-w2-1", "Hit requires?", ["Both axis overlaps", "One axis", "VFX", "Audio"], 0, "Both."),
                q("ga-w2-2", "VFX-only proof?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("ga-w2-3", "Swept tests?", ["Done", "Still need", "Deleted", "6G"], 1, "Later."),
                q("ga-w2-4", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w2-5", "overlap_x needed?", ["No", "Yes", "Screenshot", "AI"], 1, "Yes."),
                q("ga-w2-6", "AABB means?", ["Axis-aligned box", "Sphere only", "Mesh only", "Audio bus"], 0, "Box."),
            ],
        ),
        mk_week(
            3,
            "Audio clock — beat grid without pirated sample packs",
            """
            Ticket GA-6303: BPM=120 → beat period 0.5 s. Map t=1.25 s to beat index and phase.
            license_ok must be true; pirated_sample_pack=false.

            Consensus Ladder: observed = BPM card; inferred = phase in [0,1); still need = device latency
            calibration. Failure: cracked sample libraries in the portfolio.
            """,
            "BPM 120 → period 0.5; t=1.25 → beat 2 with phase 0.5.",
            "Beat map GA-6303. Submit lab_beat_clock. No piracy.",
            "lab_beat_clock",
            [
                q("ga-w3-1", "Period @120 BPM?", ["0.5 s", "1 s", "2 s", "0.12"], 0, "60/BPM."),
                q("ga-w3-2", "pirated_sample_pack?", ["true", "false", "optional", "required"], 1, "false."),
                q("ga-w3-3", "license_ok?", ["false", "true", "null", "crack"], 1, "true."),
                q("ga-w3-4", "t=1.25 beat index?", ["0", "1", "2", "5"], 2, "2."),
                q("ga-w3-5", "Latency calibration?", ["Done", "Still need", "Skip", "Fake"], 1, "Need."),
                q("ga-w3-6", "Cracked packs in portfolio?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
            ],
        ),
        mk_week(
            4,
            "Entity state — finite states with illegal transition reject",
            """
            Ticket GA-6404: states Idle→Run→Jump→Idle. Reject Jump→Run without Idle/land if table forbids.
            Lab checks transition_ok and state_after.

            Consensus Ladder: observed = transition table; inferred = illegal edges must hard-fail;
            still need = animation blend trees. Failure: boolean soup without a table.
            """,
            "Only legal edges pass; illegal Jump→Run fails transition_ok.",
            "State machine GA-6404. Submit lab_entity_fsm.",
            "lab_entity_fsm",
            [
                q("ga-w4-1", "Illegal edge should?", ["Pass", "Fail transition_ok", "Skip", "AI fix"], 1, "Fail."),
                q("ga-w4-2", "Boolean soup without table?", ["OK", "Fails discipline", "Required", "Extra"], 1, "Fail."),
                q("ga-w4-3", "Blend trees claimed done?", ["Yes", "No — still need", "Always", "AI"], 1, "Need."),
                q("ga-w4-4", "Idle→Run legal?", ["Yes on fixture", "Never", "Only AI", "Only audio"], 0, "Yes."),
                q("ga-w4-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w4-6", "print PASS?", ["OK", "Raises", "Half", "Skip"], 1, "Forbidden."),
            ],
        ),
        mk_week(
            5,
            "Level data — JSON tiles with checksum, NO_AI",
            """
            Ticket GA-6505: level JSON with width, height, tiles length = width*height, and sha256 of
            canonical bytes. NO_AI week. Lab checks dims, len match, checksum_ok.

            Consensus Ladder: observed = level file; inferred = checksum pins edits; still need =
            streaming chunks. Failure: editor GUI screenshot as only artifact.
            """,
            "tiles len = width*height; checksum_ok true.",
            "Level pin GA-6505. Submit lab_level_hash. NO_AI.",
            "lab_level_hash",
            [
                q("ga-w5-1", "tiles length rule?", ["width*height", "width+height", "always 10", "AI"], 0, "Product."),
                q("ga-w5-2", "AI mode?", ["AI dumps", "NO_AI", "Skip", "Auto"], 1, "NO_AI."),
                q("ga-w5-3", "Screenshot-only artifact?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("ga-w5-4", "checksum_ok needed?", ["No", "Yes", "Optional", "Never"], 1, "Yes."),
                q("ga-w5-5", "Streaming chunks?", ["Done", "Still need", "Deleted", "6G"], 1, "Later."),
                q("ga-w5-6", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
            ],
        ),
        mk_week(
            6,
            "Input mapping — actions not raw scancodes in design docs",
            """
            Ticket GA-6606: map Jump to Space and South face button; rebindable=true; raw_only=false.
            Lab checks actions include Jump and rebindable.

            Consensus Ladder: observed = input table; inferred = actions survive device swaps;
            still need = accessibility remaps beyond defaults (week 9). Failure: hard-coded scancode-only docs.
            """,
            "Jump action present; rebindable true; raw_only false.",
            "Input map GA-6606. Submit lab_input_actions.",
            "lab_input_actions",
            [
                q("ga-w6-1", "rebindable?", ["false", "true", "null", "ai"], 1, "true."),
                q("ga-w6-2", "raw_only docs?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("ga-w6-3", "Jump action needed?", ["No", "Yes", "Audio only", "GPU"], 1, "Yes."),
                q("ga-w6-4", "Device swap survival?", ["Actions help", "Impossible", "Ignore", "6G"], 0, "Actions."),
                q("ga-w6-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w6-6", "Week 9 link?", ["A11y remaps", "FSPL", "NTN", "E-stop"], 0, "A11y."),
            ],
        ),
        mk_week(
            7,
            "Optional four-game case study — no unmerged branch dependency",
            """
            Ticket GA-6707: optional case study may cite anime-aggressors, beatlink-party, earth-species,
            and foot-racing as named examples. required_unmerged_branch=false always. Students pick one
            lens (combat timing / beat sync / ecology sim / racing physics) and write fixture metrics.

            Lab checks optional_case_study in the four titles OR none, and required_unmerged_branch=false.
            Consuming unmerged Product-Use/game PRs as a hard dependency fails the claim boundary.
            """,
            "required_unmerged_branch=false; optional title from the four or none.",
            "Case study note GA-6707. Submit lab_four_games_case.",
            "lab_four_games_case",
            [
                q("ga-w7-1", "required_unmerged_branch?", ["true", "false", "optional", "required"], 1, "false."),
                q("ga-w7-2", "Four titles include?", ["beatlink-party", "device-os", "6G-core", "qemu-only"], 0, "Games."),
                q("ga-w7-3", "Hard-depend unmerged PR?", ["OK", "Fails boundary", "Required", "Extra"], 1, "Fail."),
                q("ga-w7-4", "Case study mandatory?", ["Always", "Optional", "Forbidden", "AI only"], 1, "Optional."),
                q("ga-w7-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w7-6", "foot-racing is?", ["Optional example title", "Required merge", "device-os", "NTN"], 0, "Optional."),
            ],
        ),
        mk_week(
            8,
            "Playtest metrics — session length and churn without vanity DAU",
            """
            Ticket GA-6808: 40 sessions, 8 churn out before minute 3. Compute early_churn_rate and
            median_session_min from fixture list. Lab checks rate math and refuses vanity_dau_claim=true.

            Consensus Ladder: observed = session table; inferred = early churn is a design smell;
            still need = cohort significance. Failure: fake million-DAU slides.
            """,
            "early_churn_rate=8/40=0.2; vanity_dau_claim false.",
            "Metrics GA-6808. Submit lab_playtest_metrics.",
            "lab_playtest_metrics",
            [
                q("ga-w8-1", "early_churn_rate?", ["0.2", "0.8", "8", "40"], 0, "8/40."),
                q("ga-w8-2", "vanity_dau_claim?", ["true", "false", "required", "optional"], 1, "false."),
                q("ga-w8-3", "Fake million DAU?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("ga-w8-4", "Sessions fixture n?", ["40", "4", "400", "0"], 0, "40."),
                q("ga-w8-5", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
                q("ga-w8-6", "Cohort significance?", ["Done", "Still need", "Skip", "Fake"], 1, "Need."),
            ],
        ),
        mk_week(
            9,
            "Accessibility — captions, remaps, color-safe UI, NO_AI",
            """
            Ticket GA-6909: captions=true, remaps=true, colorblind_safe=true, flash_hz≤3. NO_AI week.
            Lab fails if captions false or flash_hz>3.

            Consensus Ladder: observed = a11y checklist; inferred = defaults are not enough;
            still need = user testing with disabled players (not fabricated). Large-text menus required
            in student packet notes.
            """,
            "captions/remaps/colorblind_safe true; flash_hz≤3.",
            "A11y checklist GA-6909. Submit lab_game_a11y. NO_AI.",
            "lab_game_a11y",
            [
                q("ga-w9-1", "captions?", ["false", "true", "optional", "ai"], 1, "true."),
                q("ga-w9-2", "flash_hz>3?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
                q("ga-w9-3", "AI mode?", ["AI dumps", "NO_AI", "Skip", "Auto"], 1, "NO_AI."),
                q("ga-w9-4", "Fabricate disabled-player tests?", ["OK", "Forbidden", "Required", "Extra"], 1, "No."),
                q("ga-w9-5", "remaps?", ["true", "false", "null", "raw"], 0, "true."),
                q("ga-w9-6", "colorblind_safe?", ["true", "false", "ignore", "gpu"], 0, "true."),
            ],
        ),
        mk_week(
            10,
            "Ship checklist capstone — build repro without unmerged deps",
            """
            Ticket GA-6910: ship checklist with build_repro_hash, a11y_ok=true, labs_passed≥6,
            unmerged_branch_required=false, and four_games_optional_note present.

            Career map: gameplay programmer junior / QA playtest tech. Certs aligned not granted.
            Portfolio must include keyboard-only path notes. No Product-Use package consumption of this
            unmerged course branch.
            """,
            "a11y_ok true; labs_passed≥6; unmerged_branch_required false.",
            "Ship GA-6910 via lab_game_capstone. Portfolio + career map.",
            "lab_game_capstone",
            [
                q("ga-w10-1", "unmerged_branch_required?", ["true", "false", "optional", "required"], 1, "false."),
                q("ga-w10-2", "labs_passed min?", ["1", "3", "6", "100"], 2, "≥6."),
                q("ga-w10-3", "a11y_ok?", ["false", "true", "null", "skip"], 1, "true."),
                q("ga-w10-4", "Consume this unmerged branch in Product-Use?", ["Yes", "No", "Optional", "Required"], 1, "No."),
                q("ga-w10-5", "Career certs?", ["Granted", "Aligned not granted", "Hidden", "Sold"], 1, "Aligned."),
                q("ga-w10-6", "Keyboard-only path notes?", ["Required in portfolio", "Forbidden", "GPU only", "Audio only"], 0, "A11y."),
            ],
        ),
    ],
}


def build_exams():
    """Distinct mid(20)/final(24) banks — not weekly clones."""
    exams = {}

    def bank(cid, mid, final, offset):
        assert len(mid) == 20 and len(final) == 24, (cid, len(mid), len(final))
        exams[cid] = {"mid": mid, "final": final, "offset": offset}

    # WIRELESS mid/final — new numbers/scenarios
    wr_mid = [
        q("wr01", "Pier hop 200 m at 2800 MHz. Which FSPL term appears?", ["20*log10(200)", "6G_MIB", "Rel-21", "GEO"], 0, "Friis."),
        q("wr02", "A poster says commercial 6G live in Gary. Verdict?", ["Accept", "Reject — not standardized today", "Rel-18 proof", "NTN auto"], 1, "Honesty."),
        q("wr03", "15 sc at 15 kHz → PRB BW?", ["225 kHz", "15 kHz", "1.5 MHz", "15 Hz"], 0, "15*15e3."),
        q("wr04", "T_sym approx at 15 kHz without CP?", ["≈66.7 μs", "15 μs", "1 ms", "14 μs"], 0, "1/Δf."),
        q("wr05", "Feature map with commercial_6g_exists=true?", ["PASS", "FAIL", "Extra", "Required"], 1, "Fail."),
        q("wr06", "SNR 10 dB BLER=[0.3,0.12,0.08,0.2] cap 0.1 → best MCS?", ["0", "1", "2", "3"], 2, "0.08."),
        q("wr07", "LEO slant 600 km one-way ms ≈?", ["2.0", "20", "200", "0.2"], 0, "0.002s."),
        q("wr08", "RTT for 600 km slant ≈?", ["4 ms", "400 ms", "40 μs", "1 s"], 0, "2*d/c."),
        q("wr09", "geo_comparable for LEO toy?", ["true", "false", "null", "6G"], 1, "false."),
        q("wr10", "PDP with more late power generally does what to τ_rms?", ["Shrinks", "Grows", "Deletes taps", "Creates 6G"], 1, "Grows."),
        q("wr11", "AI-RAN auto_apply_without_gate=true?", ["PASS", "FAIL", "Required", "Extra"], 1, "Fail."),
        q("wr12", "human_gate on WR policy?", ["Optional", "Required true", "Forbidden", "Vendor only"], 1, "Required."),
        q("wr13", "unauthorized_tx on pier lab?", ["true OK", "Must be false", "Optional", "Rel-20"], 1, "false."),
        q("wr14", "OBW 10 MHz narrative — mask_ok without numbers?", ["OK", "Reject", "Required", "Extra"], 1, "Need numbers."),
        q("wr15", "deployed_full_ric without E2 logs?", ["PASS", "FAIL", "Required", "Extra"], 1, "Fail."),
        q("wr16", "O-RAN A1 in this course is?", ["Exam dump", "Vocabulary/map label", "Commercial 6G", "Game bus"], 1, "Vocab."),
        q("wr17", "Product-Use unmerged consumed in capstone?", ["true OK", "Must be false", "Required", "Optional"], 1, "false."),
        q("wr18", "Heavy DeepMIMO download during Stream A?", ["Required", "Avoid — fixtures only", "GPU mandate", "Overnight"], 1, "Avoid."),
        q("wr19", "5G-Advanced best one-liner?", ["Brand-new RAT", "Evolution on 5G NR", "Consumer 6G", "Wi-Fi 8"], 1, "Evolution."),
        q("wr20", "labs_passed minimum on radio capstone?", ["2", "4", "6", "60"], 2, "≥6."),
    ]
    wr_final = [
        q("wrf01", "FSPL at 90 m / 2400 MHz needs which pair?", ["d_m and f_mhz", "MCS and BLER", "BPM and dt", "E-stop"], 0, "Friis."),
        q("wrf02", "Claim 'Rel-20 commercial 6G ratified'?", ["OK", "Fails honesty", "Required", "Extra"], 1, "Fail."),
        q("wrf03", "12 sc @ 60 kHz PRB BW?", ["720 kHz", "60 kHz", "12 kHz", "1 Hz"], 0, "720e3."),
        q("wrf04", "Named CP omission means?", ["CP never exists", "Not computed yet but acknowledged", "Equals Δf", "6G"], 1, "Honesty."),
        q("wrf05", "NO_AI feature map week allows?", ["Hand-authored labels", "Exam dumps", "Fake Rel-20 6G", "Ungated TX"], 0, "Hand."),
        q("wrf06", "BLER cap 0.05; table [0.2,0.07,0.04,0.09] → MCS?", ["0", "1", "2", "3"], 2, "0.04."),
        q("wrf07", "NTN as 6G standard flag?", ["true", "false", "Rel-21", "GEO"], 1, "false."),
        q("wrf08", "Light-time 450 km one-way ≈?", ["1.5 ms", "15 ms", "150 ms", "1.5 μs"], 0, "d/c."),
        q("wrf09", "AI beamforming solved multipath with zero taps?", ["PASS", "FAIL", "Required", "Extra"], 1, "Fail."),
        q("wrf10", "τ_rms needs?", ["Power-delay profile math", "Only a heatmap", "Only DAU", "Only E-stop"], 0, "PDP."),
        q("wrf11", "AI-RAN loop order?", ["gate→observe→ignore", "observe→propose→gate→apply", "apply→observe", "dump→ship"], 1, "Gated."),
        q("wrf12", "Field trial evidence claimed without data?", ["OK", "Not claimed / fail", "Required", "Extra"], 1, "Boundary."),
        q("wrf13", "Fabricate FCC filing?", ["OK", "Forbidden", "Required", "Extra"], 1, "No."),
        q("wrf14", "Spectrum center for pier narrative class?", ["3.5 GHz class", "60 GHz only", "DC", "Optical only"], 0, "3.5."),
        q("wrf15", "RESEARCH_LAB_SCALE means?", ["Nationwide RIC", "Lab vocabulary/practice scale", "Consumer 6G", "GEO only"], 1, "Lab."),
        q("wrf16", "E2 logs PHYSICAL_PENDING means?", ["Fake them", "Not measured yet", "Delete O-RAN", "Skip ethics"], 1, "Pending."),
        q("wrf17", "Capstone notebook must include?", ["commercial_6g=false statement", "CKA claim", "device-os merge", "piracy"], 0, "Honesty."),
        q("wrf18", "Career certs?", ["Granted", "Aligned not granted", "Sold", "Hidden"], 1, "Aligned."),
        q("wrf19", "Accessibility on radio plots?", ["alt_text fields", "Ignore", "Audio only crack", "No text path"], 0, "A11y."),
        q("wrf20", "print('PASS') as lab body?", ["Accepted", "Raises", "Half", "Skip"], 1, "Forbidden."),
        q("wrf21", "MCS pick ignores BLER?", ["OK", "Fails discipline", "Required", "Extra"], 1, "Fail."),
        q("wrf22", "GEO-comparable LEO RTT claim at ~5 ms?", ["OK", "false / reject", "Required", "Extra"], 1, "Reject."),
        q("wrf23", "O-RAN map without A1/E2/O1?", ["PASS", "FAIL", "Extra", "Required"], 1, "Fail."),
        q("wrf24", "Stream A QEMU active — preferred radio labs?", ["Multi-GB sims", "Fixture math validators", "Force GPU farm", "Skip all"], 1, "Fixtures."),
    ]
    bank("WIRELESS_6G", wr_mid, wr_final, 0)

    rb_mid = [
        q("rb01", "SE(2) pose uses?", ["x,y,theta", "RGB", "BPM", "MCS"], 0, "Pose."),
        q("rb02", "Tool map without frame diagram?", ["OK", "Fails week", "Required", "Extra"], 1, "Fail."),
        q("rb03", "L1=0.4 L2=0.4 max reach?", ["0.8 m", "0.4", "0.16", "8"], 0, "Sum."),
        q("rb04", "Point at 0.9 m with max 0.8?", ["reachable true", "reachable false", "Ignore", "AI"], 1, "False."),
        q("rb05", "PID dt fixture class?", ["Small positive dt", "Zero dt", "Negative", "Infinite"], 0, "dt."),
        q("rb06", "Anti-windup note when integral huge?", ["Optional always", "Required by lab", "Forbidden", "AI only"], 1, "Required."),
        q("rb07", "Ignore vmax for smooth look?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("rb08", "NO_AI traj week allows?", ["Hand calc limits", "Exam dumps", "Bypass E-stop", "Fake SIL"], 0, "Hand."),
        q("rb09", "Lidar 4.2 m with hard gate 2.0?", ["Keep", "Drop outlier", "Average in", "Ignore gate"], 1, "Drop."),
        q("rb10", "Trust raw max always?", ["Yes", "No", "AI yes", "Required"], 1, "No."),
        q("rb11", "E-stop motors_disabled?", ["false", "true", "optional", "ai"], 1, "true."),
        q("rb12", "Soft slowdown instead of E-stop?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("rb13", "Diff-drive B=0?", ["OK", "Reject", "Required", "Extra"], 1, "Reject."),
        q("rb14", "v uses ω_l+ω_r?", ["Yes", "No", "Only FSPL", "Only MCS"], 0, "Yes."),
        q("rb15", "P=0 certainty lie?", ["OK", "Fails cov honesty", "Required", "Extra"], 1, "Fail."),
        q("rb16", "K = p/(p+r)?", ["Yes", "No", "K=p*r", "K=0"], 0, "Yes."),
        q("rb17", "cmd_vel frame_id?", ["base_link", "map_ai", "6G", "geo"], 0, "base_link."),
        q("rb18", "50-robot fleet claim?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("rb19", "Capstone open device-os PR?", ["Yes", "No", "Optional", "Required"], 1, "No."),
        q("rb20", "labs_passed min?", ["2", "4", "6", "60"], 2, "≥6."),
    ]
    rb_final = [
        q("rbf01", "Yaw π/2 rotates tool offset how?", ["sin/cos mix of x/y", "Deletes pose", "Uses BPM", "Uses BLER"], 0, "Rot."),
        q("rbf02", "Infinite reach because strong servos?", ["OK", "False", "Required", "Extra"], 1, "False."),
        q("rbf03", "FK outputs?", ["x,y (+reachable)", "Only RGB", "Only audio", "Only DAU"], 0, "FK."),
        q("rbf04", "D term reacts to?", ["Error slope", "FSPL", "MCS", "BPM"], 0, "Slope."),
        q("rbf05", "Trapezoid bound needs?", ["vmax and amax", "Only VFX", "Only captions", "Only NTN"], 0, "Limits."),
        q("rbf06", "Curvature limits status mid-course?", ["Still need", "Done always", "Deleted", "6G"], 0, "Need."),
        q("rbf07", "IQR/hard-gate purpose?", ["Drop wild outliers", "Invent bias", "Bypass E-stop", "Fake SIL"], 0, "Clean."),
        q("rbf08", "Bias calibration?", ["Still need", "Done in week1", "Impossible", "Skip forever"], 0, "Need."),
        q("rbf09", "resume_requires_human?", ["true", "false", "bot", "null"], 0, "true."),
        q("rbf10", "Bypass E-stop for demo?", ["OK", "Ethics fail", "Required", "Extra"], 1, "Fail."),
        q("rbf11", "ω_body uses ω_r-ω_l?", ["Yes", "No", "Only sum", "Only r"], 0, "Yes."),
        q("rbf12", "Video without kinematics math?", ["Enough", "Not enough", "Required", "Extra"], 1, "Math."),
        q("rbf13", "Scalar fuse refuses?", ["Zero-cov lie", "Finite K", "Two measurements", "Notes"], 0, "Honesty."),
        q("rbf14", "Full EKF claimed early?", ["OK", "Not claimed / still need", "Required", "Extra"], 1, "Need."),
        q("rbf15", "NaN in angular.z?", ["OK", "Fails finite", "Required", "Extra"], 1, "Fail."),
        q("rbf16", "NO_AI schema week?", ["Hand JSON", "Exam dumps", "Fleet fake", "SIL fake"], 0, "Hand."),
        q("rbf17", "estop_ok on capstone?", ["true", "false", "null", "ai"], 0, "true."),
        q("rbf18", "Fabricate injury stats?", ["OK", "Forbidden", "Required", "Extra"], 1, "No."),
        q("rbf19", "Career certs?", ["Granted", "Aligned not granted", "Sold", "Hidden"], 1, "Aligned."),
        q("rbf20", "E-stop sheet a11y?", ["Large-text printable", "Tiny GIF only", "None", "Crack"], 0, "A11y."),
        q("rbf21", "print PASS?", ["OK", "Raises", "Half", "Skip"], 1, "Forbidden."),
        q("rbf22", "Empty student JSON?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
        q("rbf23", "SIL certification claimed?", ["Yes course grants", "Not claimed", "Auto", "Always"], 1, "No."),
        q("rbf24", "HarborBot academy?", ["ACADEMY_HARDWARE", "ACADEMY_CYBER", "ACADEMY_PROF_DEV", "ACADEMY_PROCESS_PM"], 0, "Hardware."),
    ]
    bank("ROBOTICS_CONTROL", rb_mid, rb_final, 1)

    ga_mid = [
        q("ga01", "Fixed dt class value?", ["1/60", "1", "0", "60"], 0, "Fixed."),
        q("ga02", "Spiral-of-death guard?", ["true", "false", "null", "ai"], 0, "true."),
        q("ga03", "AABB hit needs?", ["Both overlaps", "One overlap", "VFX", "DAU"], 0, "Both."),
        q("ga04", "VFX-only collision proof?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("ga05", "120 BPM period?", ["0.5 s", "1 s", "2 s", "0.12"], 0, "0.5."),
        q("ga06", "Pirated sample pack?", ["true OK", "Must false", "Required", "Extra"], 1, "false."),
        q("ga07", "Illegal FSM edge?", ["Pass", "Fail transition_ok", "Skip", "AI"], 1, "Fail."),
        q("ga08", "Boolean soup without table?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("ga09", "tiles len rule?", ["width*height", "width+height", "10", "AI"], 0, "Product."),
        q("ga10", "NO_AI level week?", ["Hand hash", "Exam dumps", "Crack editor", "Fake DAU"], 0, "Hand."),
        q("ga11", "rebindable input?", ["true", "false", "null", "raw"], 0, "true."),
        q("ga12", "raw_only design docs?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("ga13", "required_unmerged_branch?", ["true", "false", "required", "optional"], 1, "false."),
        q("ga14", "Optional titles include?", ["earth-species", "device-os merge", "NET-SEC reopen", "WP-001"], 0, "Games."),
        q("ga15", "early churn 5/25?", ["0.2", "0.5", "5", "25"], 0, "0.2."),
        q("ga16", "vanity_dau_claim?", ["true", "false", "required", "optional"], 1, "false."),
        q("ga17", "captions on a11y lab?", ["true", "false", "optional", "ai"], 0, "true."),
        q("ga18", "flash_hz 10?", ["OK", "Fails ≤3 rule", "Required", "Extra"], 1, "Fail."),
        q("ga19", "Ship unmerged_branch_required?", ["true", "false", "optional", "required"], 1, "false."),
        q("ga20", "labs_passed min?", ["2", "4", "6", "60"], 2, "≥6."),
    ]
    ga_final = [
        q("gaf01", "Interpolate render vs fixed sim?", ["OK pattern", "Forbidden always", "Only AI", "Only audio"], 0, "OK."),
        q("gaf02", "PHYSICAL handheld profiling?", ["PENDING until measured", "Always DONE", "Fake OK", "Skip ethics"], 0, "Pending."),
        q("gaf03", "Separating axis for AABB?", ["Overlap tests", "Only spheres", "Only DAU", "Only FSPL"], 0, "Overlap."),
        q("gaf04", "Swept tests status?", ["Still need", "Done week1", "Deleted", "6G"], 0, "Need."),
        q("gaf05", "Beat phase range?", ["[0,1)", "Always 2", "Degrees only", "dB"], 0, "Phase."),
        q("gaf06", "license_ok?", ["true", "false", "crack", "null"], 0, "true."),
        q("gaf07", "Idle→Run on fixture?", ["Legal", "Illegal always", "AI only", "Audio only"], 0, "Legal."),
        q("gaf08", "Blend trees claimed early?", ["OK", "Still need / not claimed", "Required", "Extra"], 1, "Need."),
        q("gaf09", "checksum pins?", ["Level edits", "E-stop", "FSPL", "NTN"], 0, "Level."),
        q("gaf10", "Screenshot-only level proof?", ["OK", "Fails", "Required", "Extra"], 1, "Fail."),
        q("gaf11", "Actions survive device swap?", ["Yes intent", "Never", "Ignore", "6G"], 0, "Yes."),
        q("gaf12", "Week 9 remaps relation?", ["A11y extends remaps", "Deletes input", "Requires 6G", "Requires E-stop"], 0, "A11y."),
        q("gaf13", "Hard-depend unmerged game PR?", ["OK", "Fails boundary", "Required", "Extra"], 1, "Fail."),
        q("gaf14", "anime-aggressors role?", ["Optional case title", "Mandatory merge", "device-os", "NET-SEC"], 0, "Optional."),
        q("gaf15", "Playtest median needs?", ["Session list math", "Only vanity DAU", "Only VFX", "Only cracks"], 0, "Math."),
        q("gaf16", "Cohort significance?", ["Still need", "Done always", "Fake OK", "Skip"], 0, "Need."),
        q("gaf17", "colorblind_safe?", ["true", "false", "ignore", "gpu"], 0, "true."),
        q("gaf18", "Fabricate disabled-player tests?", ["OK", "Forbidden", "Required", "Extra"], 1, "No."),
        q("gaf19", "Product-Use consume this unmerged course?", ["Yes", "No", "Optional", "Required"], 1, "No."),
        q("gaf20", "Career certs?", ["Granted", "Aligned not granted", "Sold", "Hidden"], 1, "Aligned."),
        q("gaf21", "Keyboard-only path notes?", ["Required", "Forbidden", "GPU only", "None"], 0, "A11y."),
        q("gaf22", "print PASS?", ["OK", "Raises", "Half", "Skip"], 1, "Forbidden."),
        q("gaf23", "Empty {}?", ["PASS", "Fails", "Half", "Auto"], 1, "Fail."),
        q("gaf24", "Forge Arcade academy?", ["ACADEMY_SOFTWARE", "ACADEMY_CYBER", "ACADEMY_HARDWARE", "ACADEMY_IT"], 0, "Software."),
    ]
    bank("GAME_DEV_INTERACTIVE", ga_mid, ga_final, 2)
    return exams


def write_labs_py() -> str:
    return '''"""Runnable labs for WAIKE-COURSE-READY-004."""
from __future__ import annotations

import hashlib
import json
import math
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
        return {
            "lab_id": self.lab_id,
            "course_id": self.course_id,
            "ok": self.ok,
            "checks": self.checks,
            "claim_boundary": self.boundary,
            "boundary": self.boundary,
        }


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
    if not isinstance(submission, dict):
        return None, "submission_not_object"
    if submission == {}:
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


def _rms_delay(delays_ns: list[float], powers_db: list[float]) -> float:
    p = [10 ** (x / 10.0) for x in powers_db]
    s = sum(p)
    m1 = sum(d * pi for d, pi in zip(delays_ns, p)) / s
    m2 = sum((d ** 2) * pi for d, pi in zip(delays_ns, p)) / s
    return math.sqrt(max(0.0, m2 - m1 * m1))


# ---- WIRELESS ----

def lab_fspl_budget(submission: Any = None) -> LabResult:
    b = "Friis fixture only. Not a live spectrum survey; commercial 6G does not exist."
    data, checks = _require_student("lab_fspl_budget", "WIRELESS_6G", submission, ["d_m", "f_mhz", "fspl_db", "commercial_6g_exists"], b)
    if data is None:
        return _result("lab_fspl_budget", "WIRELESS_6G", checks, b)
    d, f = float(data["d_m"]), float(data["f_mhz"])
    exp = 20 * math.log10(d) + 20 * math.log10(f) - 27.55
    checks.append(_check("fspl", abs(float(data["fspl_db"]) - exp) < 0.05, f"expected {exp:.3f}"))
    checks.append(_check("no_commercial_6g", data.get("commercial_6g_exists") is False, "must be false"))
    return _result("lab_fspl_budget", "WIRELESS_6G", checks, b)


def lab_ofdm_numerology(submission: Any = None) -> LabResult:
    b = "Numerology arithmetic fixture. Not a vendor waveform lab."
    data, checks = _require_student("lab_ofdm_numerology", "WIRELESS_6G", submission, ["n_sc", "delta_f_hz", "prb_bw_hz", "symbol_duration_s"], b)
    if data is None:
        return _result("lab_ofdm_numerology", "WIRELESS_6G", checks, b)
    n, df = int(data["n_sc"]), float(data["delta_f_hz"])
    checks.append(_check("prb", abs(float(data["prb_bw_hz"]) - n * df) < 1e-6, "prb=n*df"))
    checks.append(_check("tsym", abs(float(data["symbol_duration_s"]) - (1.0 / df)) < 1e-9, "T=1/df"))
    return _result("lab_ofdm_numerology", "WIRELESS_6G", checks, b)


def lab_5ga_feature_map(submission: Any = None) -> LabResult:
    b = "PUBLIC_REFERENCE_ONLY labels. No exam dumps; commercial 6G false."
    data, checks = _require_student("lab_5ga_feature_map", "WIRELESS_6G", submission, ["features", "commercial_6g_exists"], b)
    if data is None:
        return _result("lab_5ga_feature_map", "WIRELESS_6G", checks, b)
    feats = data["features"]
    checks.append(_check("count", isinstance(feats, list) and len(feats) >= 3, "need ≥3 features"))
    ok_items = all(isinstance(x, dict) and "name" in x and "release_tag" in x for x in (feats or []))
    checks.append(_check("shape", ok_items, "name+release_tag"))
    checks.append(_check("no_6g", data.get("commercial_6g_exists") is False, "commercial_6g_exists false"))
    return _result("lab_5ga_feature_map", "WIRELESS_6G", checks, b)


def lab_mcs_bler(submission: Any = None) -> LabResult:
    b = "BLER table fixture. Not an over-the-air campaign."
    data, checks = _require_student("lab_mcs_bler", "WIRELESS_6G", submission, ["snr_db", "bler_table", "bler_cap", "chosen_mcs", "bler_at_choice"], b)
    if data is None:
        return _result("lab_mcs_bler", "WIRELESS_6G", checks, b)
    table = [float(x) for x in data["bler_table"]]
    cap = float(data["bler_cap"])
    eligible = [i for i, bl in enumerate(table) if bl <= cap + 1e-12]
    exp = max(eligible) if eligible else -1
    checks.append(_check("mcs", int(data["chosen_mcs"]) == exp, f"expected {exp}"))
    checks.append(_check("bler", abs(float(data["bler_at_choice"]) - table[exp]) < 1e-9, "bler_at_choice"))
    return _result("lab_mcs_bler", "WIRELESS_6G", checks, b)


def lab_ntn_delay(submission: Any = None) -> LabResult:
    b = "Light-time fixture. NTN is not a commercial 6G standard claim."
    data, checks = _require_student("lab_ntn_delay", "WIRELESS_6G", submission, ["distance_m", "one_way_ms", "rtt_ms", "geo_comparable", "ntn_as_6g_standard"], b)
    if data is None:
        return _result("lab_ntn_delay", "WIRELESS_6G", checks, b)
    d = float(data["distance_m"])
    one = (d / 3e8) * 1000.0
    rtt = 2 * one
    checks.append(_check("one_way", abs(float(data["one_way_ms"]) - one) < 0.02, f"expected {one:.3f}"))
    checks.append(_check("rtt", abs(float(data["rtt_ms"]) - rtt) < 0.02, f"expected {rtt:.3f}"))
    checks.append(_check("not_geo", data.get("geo_comparable") is False, "geo_comparable false"))
    checks.append(_check("not_6g_std", data.get("ntn_as_6g_standard") is False, "ntn_as_6g_standard false"))
    return _result("lab_ntn_delay", "WIRELESS_6G", checks, b)


def lab_delay_spread(submission: Any = None) -> LabResult:
    b = "Discrete PDP RMS fixture. Not a channel sounder campaign."
    data, checks = _require_student("lab_delay_spread", "WIRELESS_6G", submission, ["delays_ns", "powers_db", "tau_rms_ns", "tap_count"], b)
    if data is None:
        return _result("lab_delay_spread", "WIRELESS_6G", checks, b)
    delays = [float(x) for x in data["delays_ns"]]
    powers = [float(x) for x in data["powers_db"]]
    exp = _rms_delay(delays, powers)
    checks.append(_check("taps", int(data["tap_count"]) == len(delays) == len(powers), "tap_count"))
    checks.append(_check("tau", abs(float(data["tau_rms_ns"]) - exp) < 0.05, f"expected {exp:.4f}"))
    return _result("lab_delay_spread", "WIRELESS_6G", checks, b)


def lab_airan_policy(submission: Any = None) -> LabResult:
    b = "Gated AI-RAN policy fixture. Not ungated autonomy / not commercial 6G."
    data, checks = _require_student("lab_airan_policy", "WIRELESS_6G", submission, ["observe_kpis", "proposed_action", "human_gate", "auto_apply_without_gate"], b)
    if data is None:
        return _result("lab_airan_policy", "WIRELESS_6G", checks, b)
    act = str(data["proposed_action"]).upper()
    checks.append(_check("action", ("MCS" in act) or ("PRB" in act), "action must name MCS or PRB"))
    checks.append(_check("gate", data.get("human_gate") is True, "human_gate true"))
    checks.append(_check("no_ungated", data.get("auto_apply_without_gate") is False, "no ungated apply"))
    checks.append(_check("kpis", isinstance(data["observe_kpis"], list) and len(data["observe_kpis"]) >= 1, "kpis"))
    return _result("lab_airan_policy", "WIRELESS_6G", checks, b)


def lab_spectrum_mask(submission: Any = None) -> LabResult:
    b = "Lab-license narrative fixture. No unauthorized TX."
    data, checks = _require_student("lab_spectrum_mask", "WIRELESS_6G", submission, ["center_ghz", "obw_mhz", "mask_ok", "unauthorized_tx"], b)
    if data is None:
        return _result("lab_spectrum_mask", "WIRELESS_6G", checks, b)
    checks.append(_check("center", abs(float(data["center_ghz"]) - 3.5) < 1e-6, "3.5 GHz"))
    checks.append(_check("obw", abs(float(data["obw_mhz"]) - 18.0) < 1e-6, "18 MHz"))
    checks.append(_check("mask", data.get("mask_ok") is True, "mask_ok"))
    checks.append(_check("auth", data.get("unauthorized_tx") is False, "unauthorized_tx false"))
    return _result("lab_spectrum_mask", "WIRELESS_6G", checks, b)


def lab_oran_interfaces(submission: Any = None) -> LabResult:
    b = "O-RAN vocabulary map. RESEARCH_LAB_SCALE — not a production RIC claim."
    data, checks = _require_student("lab_oran_interfaces", "WIRELESS_6G", submission, ["interfaces", "deployed_full_ric"], b)
    if data is None:
        return _result("lab_oran_interfaces", "WIRELESS_6G", checks, b)
    ifaces = {str(x).upper() for x in data["interfaces"]}
    checks.append(_check("a1", "A1" in ifaces, "A1"))
    checks.append(_check("e2", "E2" in ifaces, "E2"))
    checks.append(_check("o1", "O1" in ifaces, "O1"))
    checks.append(_check("no_fake_ric", data.get("deployed_full_ric") is False, "deployed_full_ric false"))
    return _result("lab_oran_interfaces", "WIRELESS_6G", checks, b)


def lab_radio_capstone(submission: Any = None) -> LabResult:
    b = "Capstone notebook. No Product-Use unmerged consumption; commercial 6G false."
    keys = ["notebook_sha256", "includes_commercial_6g_false_statement", "product_use_unmerged_consumed", "labs_passed"]
    data, checks = _require_student("lab_radio_capstone", "WIRELESS_6G", submission, keys, b)
    if data is None:
        return _result("lab_radio_capstone", "WIRELESS_6G", checks, b)
    checks.append(_check("sha", str(data["notebook_sha256"]).startswith("sha256:") and len(str(data["notebook_sha256"])) >= 15, "sha256"))
    checks.append(_check("stmt", data.get("includes_commercial_6g_false_statement") is True, "6g false stmt"))
    checks.append(_check("no_pu", data.get("product_use_unmerged_consumed") is False, "no unmerged PU"))
    checks.append(_check("labs", int(data["labs_passed"]) >= 6, "labs≥6"))
    return _result("lab_radio_capstone", "WIRELESS_6G", checks, b)


# ---- ROBOTICS ----

def lab_se2_pose(submission: Any = None) -> LabResult:
    b = "Planar pose fixture. Not a cinematic autonomy demo."
    data, checks = _require_student("lab_se2_pose", "ROBOTICS_CONTROL", submission, ["x", "y", "theta", "tool_offset_x", "tool_offset_y", "tool_x", "tool_y"], b)
    if data is None:
        return _result("lab_se2_pose", "ROBOTICS_CONTROL", checks, b)
    x, y, th = float(data["x"]), float(data["y"]), float(data["theta"])
    ox, oy = float(data["tool_offset_x"]), float(data["tool_offset_y"])
    tx = x + ox * math.cos(th) - oy * math.sin(th)
    ty = y + ox * math.sin(th) + oy * math.cos(th)
    checks.append(_check("tool_x", abs(float(data["tool_x"]) - tx) < 1e-6, f"expected {tx}"))
    checks.append(_check("tool_y", abs(float(data["tool_y"]) - ty) < 1e-6, f"expected {ty}"))
    return _result("lab_se2_pose", "ROBOTICS_CONTROL", checks, b)


def lab_fk_2r(submission: Any = None) -> LabResult:
    b = "2R FK + reachability fixture."
    data, checks = _require_student("lab_fk_2r", "ROBOTICS_CONTROL", submission, ["L1", "L2", "q1", "q2", "x", "y", "reachable"], b)
    if data is None:
        return _result("lab_fk_2r", "ROBOTICS_CONTROL", checks, b)
    L1, L2 = float(data["L1"]), float(data["L2"])
    q1, q2 = float(data["q1"]), float(data["q2"])
    x = L1 * math.cos(q1) + L2 * math.cos(q1 + q2)
    y = L1 * math.sin(q1) + L2 * math.sin(q1 + q2)
    reach = math.hypot(x, y) <= (L1 + L2) + 1e-9
    checks.append(_check("x", abs(float(data["x"]) - x) < 1e-6, f"expected {x}"))
    checks.append(_check("y", abs(float(data["y"]) - y) < 1e-6, f"expected {y}"))
    checks.append(_check("reachable", bool(data["reachable"]) == reach, f"expected {reach}"))
    return _result("lab_fk_2r", "ROBOTICS_CONTROL", checks, b)


def lab_pid_step(submission: Any = None) -> LabResult:
    b = "Discrete PID fixture with anti-windup note discipline."
    keys = ["errors", "Kp", "Ki", "Kd", "dt", "u", "anti_windup_note"]
    data, checks = _require_student("lab_pid_step", "ROBOTICS_CONTROL", submission, keys, b)
    if data is None:
        return _result("lab_pid_step", "ROBOTICS_CONTROL", checks, b)
    e = [float(v) for v in data["errors"]]
    Kp, Ki, Kd, dt = map(float, (data["Kp"], data["Ki"], data["Kd"], data["dt"]))
    integ = sum(e) * dt
    de = (e[-1] - e[-2]) / dt if len(e) >= 2 else 0.0
    u = Kp * e[-1] + Ki * integ + Kd * de
    checks.append(_check("u", abs(float(data["u"]) - u) < 1e-6, f"expected {u}"))
    note = str(data.get("anti_windup_note") or "")
    checks.append(_check("anti", len(note) >= 8, "anti_windup_note"))
    return _result("lab_pid_step", "ROBOTICS_CONTROL", checks, b)


def lab_traj_limits(submission: Any = None) -> LabResult:
    b = "Trapezoid/triangle time bound fixture. vmax/amax honesty."
    data, checks = _require_student("lab_traj_limits", "ROBOTICS_CONTROL", submission, ["distance", "vmax", "amax", "t_min", "path_ok", "cmd_speed"], b)
    if data is None:
        return _result("lab_traj_limits", "ROBOTICS_CONTROL", checks, b)
    d, vmax, amax = float(data["distance"]), float(data["vmax"]), float(data["amax"])
    t_acc = vmax / amax
    d_acc = 0.5 * amax * t_acc * t_acc
    if 2 * d_acc >= d:
        t_min = 2 * math.sqrt(d / amax)
    else:
        t_min = 2 * t_acc + (d - 2 * d_acc) / vmax
    checks.append(_check("t_min", abs(float(data["t_min"]) - t_min) < 1e-6, f"expected {t_min}"))
    ok = float(data["cmd_speed"]) <= vmax + 1e-12
    checks.append(_check("path", bool(data["path_ok"]) == ok, "path_ok vs vmax"))
    return _result("lab_traj_limits", "ROBOTICS_CONTROL", checks, b)


def lab_sensor_noise(submission: Any = None) -> LabResult:
    b = "Outlier gate on lidar fixture samples."
    data, checks = _require_student("lab_sensor_noise", "ROBOTICS_CONTROL", submission, ["samples", "hard_gate", "cleaned", "cleaned_n", "mean", "outlier_dropped"], b)
    if data is None:
        return _result("lab_sensor_noise", "ROBOTICS_CONTROL", checks, b)
    gate = float(data["hard_gate"])
    cleaned = [float(x) for x in data["samples"] if float(x) <= gate]
    mean = sum(cleaned) / len(cleaned) if cleaned else 0.0
    checks.append(_check("n", int(data["cleaned_n"]) == len(cleaned) == len(data["cleaned"]), "cleaned_n"))
    checks.append(_check("mean", abs(float(data["mean"]) - mean) < 1e-6, f"expected {mean}"))
    checks.append(_check("dropped", bool(data["outlier_dropped"]) == (len(cleaned) < len(data["samples"])), "outlier_dropped"))
    return _result("lab_sensor_noise", "ROBOTICS_CONTROL", checks, b)


def lab_estop_policy(submission: Any = None) -> LabResult:
    b = "Hard E-stop policy. Soft hope is not safety."
    data, checks = _require_student("lab_estop_policy", "ROBOTICS_CONTROL", submission, ["motors_disabled", "brake_engaged", "resume_requires_human"], b)
    if data is None:
        return _result("lab_estop_policy", "ROBOTICS_CONTROL", checks, b)
    checks.append(_check("motors", data.get("motors_disabled") is True, "motors_disabled"))
    checks.append(_check("brake", data.get("brake_engaged") is True, "brake_engaged"))
    checks.append(_check("human", data.get("resume_requires_human") is True, "resume_requires_human"))
    return _result("lab_estop_policy", "ROBOTICS_CONTROL", checks, b)


def lab_diff_drive(submission: Any = None) -> LabResult:
    b = "Diff-drive ICC fixture."
    data, checks = _require_student("lab_diff_drive", "ROBOTICS_CONTROL", submission, ["B", "r", "omega_l", "omega_r", "v", "omega"], b)
    if data is None:
        return _result("lab_diff_drive", "ROBOTICS_CONTROL", checks, b)
    B, r = float(data["B"]), float(data["r"])
    checks.append(_check("B", B > 0, "B>0"))
    if B <= 0:
        return _result("lab_diff_drive", "ROBOTICS_CONTROL", checks, b)
    wl, wr = float(data["omega_l"]), float(data["omega_r"])
    v = (r / 2.0) * (wl + wr)
    w = (r / B) * (wr - wl)
    checks.append(_check("v", abs(float(data["v"]) - v) < 1e-9, f"expected {v}"))
    checks.append(_check("omega", abs(float(data["omega"]) - w) < 1e-9, f"expected {w}"))
    return _result("lab_diff_drive", "ROBOTICS_CONTROL", checks, b)


def lab_fuse_scalar(submission: Any = None) -> LabResult:
    b = "Scalar fuse fixture with covariance honesty."
    keys = ["x_odom", "p", "x_range", "r", "K", "x_hat", "cov_zero_lie"]
    data, checks = _require_student("lab_fuse_scalar", "ROBOTICS_CONTROL", submission, keys, b)
    if data is None:
        return _result("lab_fuse_scalar", "ROBOTICS_CONTROL", checks, b)
    p, r = float(data["p"]), float(data["r"])
    K = p / (p + r)
    x_hat = float(data["x_odom"]) + K * (float(data["x_range"]) - float(data["x_odom"]))
    checks.append(_check("K", abs(float(data["K"]) - K) < 1e-9, f"expected {K}"))
    checks.append(_check("x_hat", abs(float(data["x_hat"]) - x_hat) < 1e-9, f"expected {x_hat}"))
    checks.append(_check("cov", data.get("cov_zero_lie") is False, "cov_zero_lie false"))
    return _result("lab_fuse_scalar", "ROBOTICS_CONTROL", checks, b)


def lab_cmd_vel_schema(submission: Any = None) -> LabResult:
    b = "cmd_vel-shaped schema fixture. No fleet deploy claim."
    data, checks = _require_student("lab_cmd_vel_schema", "ROBOTICS_CONTROL", submission, ["linear_x", "angular_z", "frame_id", "fleet_claim"], b)
    if data is None:
        return _result("lab_cmd_vel_schema", "ROBOTICS_CONTROL", checks, b)
    lx, az = float(data["linear_x"]), float(data["angular_z"])
    checks.append(_check("finite", math.isfinite(lx) and math.isfinite(az), "finite twist"))
    checks.append(_check("frame", data.get("frame_id") == "base_link", "base_link"))
    checks.append(_check("fleet", data.get("fleet_claim") is False, "fleet_claim false"))
    return _result("lab_cmd_vel_schema", "ROBOTICS_CONTROL", checks, b)


def lab_robot_capstone(submission: Any = None) -> LabResult:
    b = "Robotics capstone. Do not open device-os PRs from this packet."
    keys = ["estop_ok", "labs_passed", "no_device_os_pr", "packet_sha256"]
    data, checks = _require_student("lab_robot_capstone", "ROBOTICS_CONTROL", submission, keys, b)
    if data is None:
        return _result("lab_robot_capstone", "ROBOTICS_CONTROL", checks, b)
    checks.append(_check("estop", data.get("estop_ok") is True, "estop_ok"))
    checks.append(_check("labs", int(data["labs_passed"]) >= 6, "labs≥6"))
    checks.append(_check("no_dos", data.get("no_device_os_pr") is True, "no_device_os_pr"))
    checks.append(_check("sha", str(data["packet_sha256"]).startswith("sha256:"), "sha"))
    return _result("lab_robot_capstone", "ROBOTICS_CONTROL", checks, b)


# ---- GAMES ----

def lab_game_loop(submission: Any = None) -> LabResult:
    b = "Fixed-timestep loop fixture."
    data, checks = _require_student("lab_game_loop", "GAME_DEV_INTERACTIVE", submission, ["dt", "steps", "frame_time", "spiral_of_death_guard"], b)
    if data is None:
        return _result("lab_game_loop", "GAME_DEV_INTERACTIVE", checks, b)
    checks.append(_check("dt", abs(float(data["dt"]) - (1.0 / 60.0)) < 1e-9, "dt=1/60"))
    checks.append(_check("steps", int(data["steps"]) >= 1, "steps"))
    need_guard = float(data["frame_time"]) > 0.25
    checks.append(_check("guard", (not need_guard) or data.get("spiral_of_death_guard") is True, "guard when frame_time>0.25"))
    checks.append(_check("guard_flag", data.get("spiral_of_death_guard") is True, "guard true on reference"))
    return _result("lab_game_loop", "GAME_DEV_INTERACTIVE", checks, b)


def lab_aabb_hit(submission: Any = None) -> LabResult:
    b = "AABB overlap fixture."
    keys = ["a", "b", "overlap_x", "overlap_y", "hit"]
    data, checks = _require_student("lab_aabb_hit", "GAME_DEV_INTERACTIVE", submission, keys, b)
    if data is None:
        return _result("lab_aabb_hit", "GAME_DEV_INTERACTIVE", checks, b)
    aa, bb = data["a"], data["b"]
    ox = min(float(aa["x2"]), float(bb["x2"])) - max(float(aa["x1"]), float(bb["x1"]))
    oy = min(float(aa["y2"]), float(bb["y2"])) - max(float(aa["y1"]), float(bb["y1"]))
    hit = ox > 0 and oy > 0
    checks.append(_check("ox", abs(float(data["overlap_x"]) - ox) < 1e-9, f"expected {ox}"))
    checks.append(_check("oy", abs(float(data["overlap_y"]) - oy) < 1e-9, f"expected {oy}"))
    checks.append(_check("hit", bool(data["hit"]) == hit, f"expected {hit}"))
    return _result("lab_aabb_hit", "GAME_DEV_INTERACTIVE", checks, b)


def lab_beat_clock(submission: Any = None) -> LabResult:
    b = "Beat grid fixture. No pirated sample packs."
    keys = ["bpm", "t", "beat_index", "phase", "license_ok", "pirated_sample_pack"]
    data, checks = _require_student("lab_beat_clock", "GAME_DEV_INTERACTIVE", submission, keys, b)
    if data is None:
        return _result("lab_beat_clock", "GAME_DEV_INTERACTIVE", checks, b)
    period = 60.0 / float(data["bpm"])
    t = float(data["t"])
    idx = int(math.floor(t / period))
    phase = (t / period) - idx
    checks.append(_check("idx", int(data["beat_index"]) == idx, f"expected {idx}"))
    checks.append(_check("phase", abs(float(data["phase"]) - phase) < 1e-9, f"expected {phase}"))
    checks.append(_check("license", data.get("license_ok") is True, "license_ok"))
    checks.append(_check("piracy", data.get("pirated_sample_pack") is False, "no piracy"))
    return _result("lab_beat_clock", "GAME_DEV_INTERACTIVE", checks, b)


def lab_entity_fsm(submission: Any = None) -> LabResult:
    b = "Entity FSM fixture with illegal edge rejection."
    legal = {("Idle", "Run"), ("Run", "Jump"), ("Jump", "Idle"), ("Run", "Idle"), ("Idle", "Idle")}
    data, checks = _require_student("lab_entity_fsm", "GAME_DEV_INTERACTIVE", submission, ["from_state", "to_state", "transition_ok", "state_after"], b)
    if data is None:
        return _result("lab_entity_fsm", "GAME_DEV_INTERACTIVE", checks, b)
    edge = (str(data["from_state"]), str(data["to_state"]))
    ok = edge in legal
    checks.append(_check("ok", bool(data["transition_ok"]) == ok, f"expected {ok}"))
    exp_after = data["to_state"] if ok else data["from_state"]
    checks.append(_check("after", data.get("state_after") == exp_after, f"expected {exp_after}"))
    return _result("lab_entity_fsm", "GAME_DEV_INTERACTIVE", checks, b)


def lab_level_hash(submission: Any = None) -> LabResult:
    b = "Level JSON pin with checksum."
    data, checks = _require_student("lab_level_hash", "GAME_DEV_INTERACTIVE", submission, ["width", "height", "tiles", "checksum", "checksum_ok"], b)
    if data is None:
        return _result("lab_level_hash", "GAME_DEV_INTERACTIVE", checks, b)
    w, h = int(data["width"]), int(data["height"])
    tiles = data["tiles"]
    checks.append(_check("len", isinstance(tiles, list) and len(tiles) == w * h, "tiles len"))
    canon = json.dumps({"width": w, "height": h, "tiles": tiles}, separators=(",", ":"))
    digest = "sha256:" + hashlib.sha256(canon.encode()).hexdigest()[:16]
    checks.append(_check("sum", data.get("checksum") == digest and data.get("checksum_ok") is True, f"expected {digest}"))
    return _result("lab_level_hash", "GAME_DEV_INTERACTIVE", checks, b)


def lab_input_actions(submission: Any = None) -> LabResult:
    b = "Action-map fixture. Not scancode-only docs."
    data, checks = _require_student("lab_input_actions", "GAME_DEV_INTERACTIVE", submission, ["actions", "rebindable", "raw_only"], b)
    if data is None:
        return _result("lab_input_actions", "GAME_DEV_INTERACTIVE", checks, b)
    acts = set(data["actions"])
    checks.append(_check("jump", "Jump" in acts, "Jump"))
    checks.append(_check("rebind", data.get("rebindable") is True, "rebindable"))
    checks.append(_check("raw", data.get("raw_only") is False, "raw_only false"))
    return _result("lab_input_actions", "GAME_DEV_INTERACTIVE", checks, b)


def lab_four_games_case(submission: Any = None) -> LabResult:
    b = "Optional four-game case study. No unmerged branch hard dependency."
    allowed = {"anime-aggressors", "beatlink-party", "earth-species", "foot-racing", "none"}
    data, checks = _require_student("lab_four_games_case", "GAME_DEV_INTERACTIVE", submission, ["optional_case_study", "required_unmerged_branch", "lens"], b)
    if data is None:
        return _result("lab_four_games_case", "GAME_DEV_INTERACTIVE", checks, b)
    checks.append(_check("title", data.get("optional_case_study") in allowed, "optional title"))
    checks.append(_check("unmerged", data.get("required_unmerged_branch") is False, "no unmerged req"))
    checks.append(_check("lens", len(str(data.get("lens") or "")) >= 4, "lens"))
    return _result("lab_four_games_case", "GAME_DEV_INTERACTIVE", checks, b)


def lab_playtest_metrics(submission: Any = None) -> LabResult:
    b = "Playtest churn math. No vanity DAU claims."
    data, checks = _require_student("lab_playtest_metrics", "GAME_DEV_INTERACTIVE", submission, ["sessions", "early_churn", "early_churn_rate", "vanity_dau_claim"], b)
    if data is None:
        return _result("lab_playtest_metrics", "GAME_DEV_INTERACTIVE", checks, b)
    n = int(data["sessions"])
    c = int(data["early_churn"])
    checks.append(_check("rate", abs(float(data["early_churn_rate"]) - (c / n)) < 1e-9, "rate"))
    checks.append(_check("vanity", data.get("vanity_dau_claim") is False, "no vanity"))
    return _result("lab_playtest_metrics", "GAME_DEV_INTERACTIVE", checks, b)


def lab_game_a11y(submission: Any = None) -> LabResult:
    b = "Accessibility checklist fixture."
    data, checks = _require_student("lab_game_a11y", "GAME_DEV_INTERACTIVE", submission, ["captions", "remaps", "colorblind_safe", "flash_hz"], b)
    if data is None:
        return _result("lab_game_a11y", "GAME_DEV_INTERACTIVE", checks, b)
    checks.append(_check("captions", data.get("captions") is True, "captions"))
    checks.append(_check("remaps", data.get("remaps") is True, "remaps"))
    checks.append(_check("cb", data.get("colorblind_safe") is True, "colorblind_safe"))
    checks.append(_check("flash", float(data["flash_hz"]) <= 3.0, "flash_hz≤3"))
    return _result("lab_game_a11y", "GAME_DEV_INTERACTIVE", checks, b)


def lab_game_capstone(submission: Any = None) -> LabResult:
    b = "Game capstone. No unmerged hard deps; a11y required."
    keys = ["build_repro_hash", "a11y_ok", "labs_passed", "unmerged_branch_required", "four_games_optional_note"]
    data, checks = _require_student("lab_game_capstone", "GAME_DEV_INTERACTIVE", submission, keys, b)
    if data is None:
        return _result("lab_game_capstone", "GAME_DEV_INTERACTIVE", checks, b)
    checks.append(_check("hash", str(data["build_repro_hash"]).startswith("sha256:"), "hash"))
    checks.append(_check("a11y", data.get("a11y_ok") is True, "a11y_ok"))
    checks.append(_check("labs", int(data["labs_passed"]) >= 6, "labs≥6"))
    checks.append(_check("unmerged", data.get("unmerged_branch_required") is False, "unmerged false"))
    checks.append(_check("note", len(str(data["four_games_optional_note"])) >= 8, "note"))
    return _result("lab_game_capstone", "GAME_DEV_INTERACTIVE", checks, b)


LABS_004 = {
    "lab_fspl_budget": lab_fspl_budget,
    "lab_ofdm_numerology": lab_ofdm_numerology,
    "lab_5ga_feature_map": lab_5ga_feature_map,
    "lab_mcs_bler": lab_mcs_bler,
    "lab_ntn_delay": lab_ntn_delay,
    "lab_delay_spread": lab_delay_spread,
    "lab_airan_policy": lab_airan_policy,
    "lab_spectrum_mask": lab_spectrum_mask,
    "lab_oran_interfaces": lab_oran_interfaces,
    "lab_radio_capstone": lab_radio_capstone,
    "lab_se2_pose": lab_se2_pose,
    "lab_fk_2r": lab_fk_2r,
    "lab_pid_step": lab_pid_step,
    "lab_traj_limits": lab_traj_limits,
    "lab_sensor_noise": lab_sensor_noise,
    "lab_estop_policy": lab_estop_policy,
    "lab_diff_drive": lab_diff_drive,
    "lab_fuse_scalar": lab_fuse_scalar,
    "lab_cmd_vel_schema": lab_cmd_vel_schema,
    "lab_robot_capstone": lab_robot_capstone,
    "lab_game_loop": lab_game_loop,
    "lab_aabb_hit": lab_aabb_hit,
    "lab_beat_clock": lab_beat_clock,
    "lab_entity_fsm": lab_entity_fsm,
    "lab_level_hash": lab_level_hash,
    "lab_input_actions": lab_input_actions,
    "lab_four_games_case": lab_four_games_case,
    "lab_playtest_metrics": lab_playtest_metrics,
    "lab_game_a11y": lab_game_a11y,
    "lab_game_capstone": lab_game_capstone,
}

COURSE_LABS_004 = {
    "WIRELESS_6G": [
        "lab_fspl_budget", "lab_ofdm_numerology", "lab_5ga_feature_map", "lab_mcs_bler", "lab_ntn_delay",
        "lab_delay_spread", "lab_airan_policy", "lab_spectrum_mask", "lab_oran_interfaces", "lab_radio_capstone",
    ],
    "ROBOTICS_CONTROL": [
        "lab_se2_pose", "lab_fk_2r", "lab_pid_step", "lab_traj_limits", "lab_sensor_noise",
        "lab_estop_policy", "lab_diff_drive", "lab_fuse_scalar", "lab_cmd_vel_schema", "lab_robot_capstone",
    ],
    "GAME_DEV_INTERACTIVE": [
        "lab_game_loop", "lab_aabb_hit", "lab_beat_clock", "lab_entity_fsm", "lab_level_hash",
        "lab_input_actions", "lab_four_games_case", "lab_playtest_metrics", "lab_game_a11y", "lab_game_capstone",
    ],
}

LAB_SPECS_004 = {
    lid: {
        "title": lid.replace("lab_", "").replace("_", " "),
        "readme": f"Runnable validator for {lid}. Empty/wrong/print-PASS fail.",
        "required_keys": [],
        "wrong_hint": "Wrong numeric or policy fields must fail.",
    }
    for lid in LABS_004
}

REFERENCE_004: dict[str, dict[str, Any]] = {}
WRONG_004: dict[str, dict[str, Any]] = {}


def _fill_refs() -> None:
    import math as _m
    d, f = 120.0, 3500.0
    REFERENCE_004["lab_fspl_budget"] = {
        "d_m": d, "f_mhz": f,
        "fspl_db": 20 * _m.log10(d) + 20 * _m.log10(f) - 27.55,
        "commercial_6g_exists": False,
    }
    WRONG_004["lab_fspl_budget"] = {"d_m": d, "f_mhz": f, "fspl_db": 1.0, "commercial_6g_exists": True}

    REFERENCE_004["lab_ofdm_numerology"] = {"n_sc": 12, "delta_f_hz": 30000.0, "prb_bw_hz": 360000.0, "symbol_duration_s": 1 / 30000.0}
    WRONG_004["lab_ofdm_numerology"] = {"n_sc": 12, "delta_f_hz": 30000.0, "prb_bw_hz": 1.0, "symbol_duration_s": 1.0}

    REFERENCE_004["lab_5ga_feature_map"] = {
        "features": [
            {"name": "RedCap", "release_tag": "Rel-18"},
            {"name": "NTN", "release_tag": "Rel-17/18"},
            {"name": "AI-ML study", "release_tag": "Rel-18 study"},
        ],
        "commercial_6g_exists": False,
    }
    WRONG_004["lab_5ga_feature_map"] = {"features": [{"name": "x", "release_tag": "y"}], "commercial_6g_exists": True}

    table = [0.40, 0.22, 0.09, 0.18, 0.35]
    REFERENCE_004["lab_mcs_bler"] = {"snr_db": 8, "bler_table": table, "bler_cap": 0.1, "chosen_mcs": 2, "bler_at_choice": 0.09}
    WRONG_004["lab_mcs_bler"] = {"snr_db": 8, "bler_table": table, "bler_cap": 0.1, "chosen_mcs": 4, "bler_at_choice": 0.35}

    dist = 700000.0
    one = dist / 3e8 * 1000
    REFERENCE_004["lab_ntn_delay"] = {"distance_m": dist, "one_way_ms": one, "rtt_ms": 2 * one, "geo_comparable": False, "ntn_as_6g_standard": False}
    WRONG_004["lab_ntn_delay"] = {"distance_m": dist, "one_way_ms": 1.0, "rtt_ms": 1.0, "geo_comparable": True, "ntn_as_6g_standard": True}

    delays, powers = [0.0, 120.0, 350.0], [0.0, -3.0, -10.0]
    REFERENCE_004["lab_delay_spread"] = {"delays_ns": delays, "powers_db": powers, "tau_rms_ns": _rms_delay(delays, powers), "tap_count": 3}
    WRONG_004["lab_delay_spread"] = {"delays_ns": delays, "powers_db": powers, "tau_rms_ns": 0.0, "tap_count": 1}

    REFERENCE_004["lab_airan_policy"] = {"observe_kpis": ["bler"], "proposed_action": "MCS down", "human_gate": True, "auto_apply_without_gate": False}
    WRONG_004["lab_airan_policy"] = {"observe_kpis": [], "proposed_action": "feelings", "human_gate": False, "auto_apply_without_gate": True}

    REFERENCE_004["lab_spectrum_mask"] = {"center_ghz": 3.5, "obw_mhz": 18.0, "mask_ok": True, "unauthorized_tx": False}
    WRONG_004["lab_spectrum_mask"] = {"center_ghz": 3.5, "obw_mhz": 18.0, "mask_ok": False, "unauthorized_tx": True}

    REFERENCE_004["lab_oran_interfaces"] = {"interfaces": ["A1", "E2", "O1"], "deployed_full_ric": False}
    WRONG_004["lab_oran_interfaces"] = {"interfaces": ["X"], "deployed_full_ric": True}

    REFERENCE_004["lab_radio_capstone"] = {"notebook_sha256": "sha256:wr4910deadbeef", "includes_commercial_6g_false_statement": True, "product_use_unmerged_consumed": False, "labs_passed": 8}
    WRONG_004["lab_radio_capstone"] = {"notebook_sha256": "x", "includes_commercial_6g_false_statement": False, "product_use_unmerged_consumed": True, "labs_passed": 1}

    th = _m.pi / 2
    REFERENCE_004["lab_se2_pose"] = {"x": 0.0, "y": 0.0, "theta": th, "tool_offset_x": 0.2, "tool_offset_y": 0.0, "tool_x": 0.2 * _m.cos(th), "tool_y": 0.2 * _m.sin(th)}
    WRONG_004["lab_se2_pose"] = {"x": 0.0, "y": 0.0, "theta": th, "tool_offset_x": 0.2, "tool_offset_y": 0.0, "tool_x": 0.0, "tool_y": 0.0}

    L1, L2, q1, q2 = 0.35, 0.30, 0.4, 0.5
    x = L1 * _m.cos(q1) + L2 * _m.cos(q1 + q2)
    y = L1 * _m.sin(q1) + L2 * _m.sin(q1 + q2)
    REFERENCE_004["lab_fk_2r"] = {"L1": L1, "L2": L2, "q1": q1, "q2": q2, "x": x, "y": y, "reachable": True}
    WRONG_004["lab_fk_2r"] = {"L1": L1, "L2": L2, "q1": q1, "q2": q2, "x": 0, "y": 0, "reachable": False}

    errs = [1.0, 0.6, 0.2]
    Kp, Ki, Kd, dt = 1.2, 0.4, 0.1, 0.1
    integ = sum(errs) * dt
    de = (errs[-1] - errs[-2]) / dt
    u = Kp * errs[-1] + Ki * integ + Kd * de
    REFERENCE_004["lab_pid_step"] = {"errors": errs, "Kp": Kp, "Ki": Ki, "Kd": Kd, "dt": dt, "u": u, "anti_windup_note": "clamp integral on saturation"}
    WRONG_004["lab_pid_step"] = {"errors": errs, "Kp": Kp, "Ki": Ki, "Kd": Kd, "dt": dt, "u": 0.0, "anti_windup_note": ""}

    d, vmax, amax = 1.2, 0.4, 0.5
    t_acc = vmax / amax
    d_acc = 0.5 * amax * t_acc * t_acc
    t_min = 2 * t_acc + (d - 2 * d_acc) / vmax
    REFERENCE_004["lab_traj_limits"] = {"distance": d, "vmax": vmax, "amax": amax, "t_min": t_min, "path_ok": True, "cmd_speed": 0.35}
    WRONG_004["lab_traj_limits"] = {"distance": d, "vmax": vmax, "amax": amax, "t_min": 0.01, "path_ok": True, "cmd_speed": 0.9}

    samples = [1.01, 1.00, 0.99, 1.02, 3.50]
    cleaned = [s for s in samples if s <= 2.0]
    REFERENCE_004["lab_sensor_noise"] = {"samples": samples, "hard_gate": 2.0, "cleaned": cleaned, "cleaned_n": len(cleaned), "mean": sum(cleaned) / len(cleaned), "outlier_dropped": True}
    WRONG_004["lab_sensor_noise"] = {"samples": samples, "hard_gate": 2.0, "cleaned": samples, "cleaned_n": 5, "mean": 0.0, "outlier_dropped": False}

    REFERENCE_004["lab_estop_policy"] = {"motors_disabled": True, "brake_engaged": True, "resume_requires_human": True}
    WRONG_004["lab_estop_policy"] = {"motors_disabled": False, "brake_engaged": False, "resume_requires_human": False}

    B, r, wl, wr = 0.40, 0.05, 2.0, 4.0
    REFERENCE_004["lab_diff_drive"] = {"B": B, "r": r, "omega_l": wl, "omega_r": wr, "v": (r / 2) * (wl + wr), "omega": (r / B) * (wr - wl)}
    WRONG_004["lab_diff_drive"] = {"B": 0.0, "r": r, "omega_l": wl, "omega_r": wr, "v": 0, "omega": 0}

    p, rv, xo, xr = 0.04, 0.01, 1.0, 1.2
    K = p / (p + rv)
    REFERENCE_004["lab_fuse_scalar"] = {"x_odom": xo, "p": p, "x_range": xr, "r": rv, "K": K, "x_hat": xo + K * (xr - xo), "cov_zero_lie": False}
    WRONG_004["lab_fuse_scalar"] = {"x_odom": xo, "p": p, "x_range": xr, "r": rv, "K": 0, "x_hat": 0, "cov_zero_lie": True}

    REFERENCE_004["lab_cmd_vel_schema"] = {"linear_x": 0.2, "angular_z": 0.1, "frame_id": "base_link", "fleet_claim": False}
    WRONG_004["lab_cmd_vel_schema"] = {"linear_x": float("nan"), "angular_z": 0.1, "frame_id": "map_ai", "fleet_claim": True}

    REFERENCE_004["lab_robot_capstone"] = {"estop_ok": True, "labs_passed": 8, "no_device_os_pr": True, "packet_sha256": "sha256:rb5910cafe"}
    WRONG_004["lab_robot_capstone"] = {"estop_ok": False, "labs_passed": 1, "no_device_os_pr": False, "packet_sha256": "x"}

    REFERENCE_004["lab_game_loop"] = {"dt": 1 / 60, "steps": 3, "frame_time": 0.3, "spiral_of_death_guard": True}
    WRONG_004["lab_game_loop"] = {"dt": 1.0, "steps": 0, "frame_time": 0.3, "spiral_of_death_guard": False}

    a = {"x1": 0, "y1": 0, "x2": 2, "y2": 2}
    bb = {"x1": 1, "y1": 1, "x2": 3, "y2": 3}
    REFERENCE_004["lab_aabb_hit"] = {"a": a, "b": bb, "overlap_x": 1.0, "overlap_y": 1.0, "hit": True}
    WRONG_004["lab_aabb_hit"] = {"a": a, "b": bb, "overlap_x": 0.0, "overlap_y": 0.0, "hit": False}

    REFERENCE_004["lab_beat_clock"] = {"bpm": 120, "t": 1.25, "beat_index": 2, "phase": 0.5, "license_ok": True, "pirated_sample_pack": False}
    WRONG_004["lab_beat_clock"] = {"bpm": 120, "t": 1.25, "beat_index": 0, "phase": 0.0, "license_ok": False, "pirated_sample_pack": True}

    REFERENCE_004["lab_entity_fsm"] = {"from_state": "Idle", "to_state": "Run", "transition_ok": True, "state_after": "Run"}
    WRONG_004["lab_entity_fsm"] = {"from_state": "Jump", "to_state": "Run", "transition_ok": True, "state_after": "Run"}

    tiles = [0, 1, 0, 1]
    canon = json.dumps({"width": 2, "height": 2, "tiles": tiles}, separators=(",", ":"))
    digest = "sha256:" + hashlib.sha256(canon.encode()).hexdigest()[:16]
    REFERENCE_004["lab_level_hash"] = {"width": 2, "height": 2, "tiles": tiles, "checksum": digest, "checksum_ok": True}
    WRONG_004["lab_level_hash"] = {"width": 2, "height": 2, "tiles": tiles, "checksum": "sha256:dead", "checksum_ok": True}

    REFERENCE_004["lab_input_actions"] = {"actions": ["Jump", "Move"], "rebindable": True, "raw_only": False}
    WRONG_004["lab_input_actions"] = {"actions": ["Move"], "rebindable": False, "raw_only": True}

    REFERENCE_004["lab_four_games_case"] = {"optional_case_study": "beatlink-party", "required_unmerged_branch": False, "lens": "beat sync"}
    WRONG_004["lab_four_games_case"] = {"optional_case_study": "not-a-game", "required_unmerged_branch": True, "lens": "x"}

    REFERENCE_004["lab_playtest_metrics"] = {"sessions": 40, "early_churn": 8, "early_churn_rate": 0.2, "vanity_dau_claim": False}
    WRONG_004["lab_playtest_metrics"] = {"sessions": 40, "early_churn": 8, "early_churn_rate": 0.9, "vanity_dau_claim": True}

    REFERENCE_004["lab_game_a11y"] = {"captions": True, "remaps": True, "colorblind_safe": True, "flash_hz": 2.0}
    WRONG_004["lab_game_a11y"] = {"captions": False, "remaps": False, "colorblind_safe": False, "flash_hz": 10.0}

    REFERENCE_004["lab_game_capstone"] = {
        "build_repro_hash": "sha256:ga6910beef", "a11y_ok": True, "labs_passed": 8,
        "unmerged_branch_required": False, "four_games_optional_note": "optional case only",
    }
    WRONG_004["lab_game_capstone"] = {
        "build_repro_hash": "x", "a11y_ok": False, "labs_passed": 1,
        "unmerged_branch_required": True, "four_games_optional_note": "x",
    }


_fill_refs()
'''


def write_packaging_py() -> str:
    return '''"""Course-specific packaging for COURSE-READY-004."""
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
    return "\\n".join([
        f"# {lab_id} — {spec['title']}", "", spec["readme"], "", "## Student artifact", empty,
        "A file whose entire body is PASS is rejected by _fail_if_print_pass.", "", "## How to run", how,
        "```", f"python3 scripts/run_course_labs.py --lab {lab_id} --submission path/to/student.json",
        f"python3 scripts/run_course_labs.py --lab {lab_id} --empty", "```", "", spec["wrong_hint"], "",
    ])


def instructor_week_notes_004(course_id: str, week: dict[str, Any]) -> str:
    n = week["week"]
    titles = {"WIRELESS_6G": "Pier Radio", "ROBOTICS_CONTROL": "HarborBot", "GAME_DEV_INTERACTIVE": "Forge Arcade"}
    return (
        f"# {titles[course_id]} — instructor week {n}\\n\\n"
        f"**Live number/example:** {week['worked_example']}\\n\\n"
        f"**Lab `{week['lab_id']}`:** collect student JSON; do not run the golden path and call it theirs.\\n\\n"
        f"**Pitfall:** {PITFALLS[course_id][n]}\\n\\n"
        f"Refuse dumps. Point at curriculum/alignment/{course_id.lower()}_alignment.json.\\n"
        f"AI policy: see course.ai_use_policy in course.json.\\n"
        f"Accessibility: text-first journals; large-print where noted.\\n"
    )


def presentation_004(course_id: str, week: dict[str, Any]) -> str:
    return (
        f"# Week {week['week']}: {week['title']}\\n\\n"
        f"## Slide 1 — Hook\\n{week['title']}\\n\\n"
        f"## Slide 2 — Worked example\\n{week['worked_example']}\\n\\n"
        f"## Slide 3 — Lab contract\\n`{week['lab_id']}` rejects empty/wrong/print-PASS.\\n\\n"
        f"## Speaker notes\\nStay in {course_id} vocabulary. Do not noun-swap another academy's deck.\\n"
        f"Assignment: {week['assignment'][:180]}...\\n"
    )


def instructor_packet_004(course_id: str) -> str:
    return (
        f"# Instructor packet — {course_id}\\n\\n"
        f"- Keys: `instructor/answer_keys.json` (not in learner ingest)\\n"
        f"- Labs: run `python3 scripts/run_course_labs.py` — empty/wrong must fail\\n"
        f"- See instructor/accessibility_and_udl_guide.md\\n"
        f"- Do not claim vendor certs, commercial 6G, or physical completion without evidence\\n"
        f"- Cursor does not merge; REAL_*_E6 remain false\\n"
    )


def student_packet_004(course_id: str, hook: str) -> str:
    return (
        f"# Student packet — {course_id}\\n\\n"
        f"{hook}\\n\\n"
        f"- Submit lab JSON you computed; empty/wrong/print-PASS fail\\n"
        f"- Accessibility: prefer text paths; request large-print materials\\n"
        f"- Career map: see career_mapping.json (certs aligned not granted)\\n"
        f"- Offline pack: offline_pack/pack.json\\n"
    )


def group_project_004(course_id: str, title: str, assignment: str) -> str:
    return f"# Group project — {course_id}\\n\\n## {title}\\n\\n{assignment}\\n"


def portfolio_004(course_id: str) -> str:
    return (
        f"# Portfolio — {course_id}\\n\\n"
        f"- Lab result JSON + empty-fail evidence\\n"
        f"- Claim boundary paragraph\\n"
        f"- Accessibility notes\\n"
        f"- Career map excerpt\\n"
    )
'''


def write_alignment(course_id: str, track_id: str, benchmarks: list[dict]) -> None:
    path = ALIGN / f"{course_id.lower()}_alignment.json"
    path.write_text(json.dumps({
        "schema": "waike.alignment.v1",
        "course_id": course_id,
        "track_ids": [track_id],
        "date_checked": "2026-08-15",
        "benchmarks": benchmarks,
        "claim_boundary": "PUBLIC_REFERENCE_ONLY / RESTRICTED outlines. No exam dumps. Certs not granted.",
    }, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    courses = {
        "WIRELESS_6G": WIRELESS,
        "ROBOTICS_CONTROL": ROBOTICS,
        "GAME_DEV_INTERACTIVE": GAMES,
    }
    for cid, c in courses.items():
        assert len(c["weeks"]) == 10
        for w in c["weeks"]:
            assert len(w["lesson"]) >= 900, (cid, w["week"], len(w["lesson"]))
            assert len(w["quiz"]) == 6

    (OUT / "courses_data.json").write_text(json.dumps(courses, indent=2) + "\n", encoding="utf-8")
    (OUT / "exams_data.json").write_text(json.dumps(build_exams(), indent=2) + "\n", encoding="utf-8")
    (OUT / "labs.py").write_text(write_labs_py(), encoding="utf-8")
    (OUT / "packaging.py").write_text(write_packaging_py().replace("\\\\n", "\\n"), encoding="utf-8")
    (OUT / "__init__.py").write_text(
        '"""WAIKE-COURSE-READY-004 batch packages (WIRELESS_6G, ROBOTICS_CONTROL, GAME_DEV_INTERACTIVE)."""\\n',
        encoding="utf-8",
    )
    (OUT / "content.py").write_text(
        '''"""Original WAIKE bodies for COURSE-READY-004 batch."""
from __future__ import annotations

import json
from pathlib import Path

BATCH_COURSE_IDS = ("WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE")

_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
WIRELESS_6G = _DATA["WIRELESS_6G"]
ROBOTICS_CONTROL = _DATA["ROBOTICS_CONTROL"]
GAME_DEV_INTERACTIVE = _DATA["GAME_DEV_INTERACTIVE"]
COURSES_004 = {
    "WIRELESS_6G": WIRELESS_6G,
    "ROBOTICS_CONTROL": ROBOTICS_CONTROL,
    "GAME_DEV_INTERACTIVE": GAME_DEV_INTERACTIVE,
}
''',
        encoding="utf-8",
    )
    (OUT / "exams.py").write_text(
        '''"""Mid/final banks for COURSE-READY-004."""
from __future__ import annotations

import json
from pathlib import Path

_EX = json.loads((Path(__file__).with_name("exams_data.json")).read_text(encoding="utf-8"))


def extra_assessment_items_004(course_id: str):
    from waike_course_ready.exams import rebalance_mcq

    spec = _EX[course_id]
    mid = rebalance_mcq(spec["mid"], spec["offset"])
    final = rebalance_mcq(spec["final"], spec["offset"] + 1)
    if len(mid) != 20 or len(final) != 24:
        raise ValueError(f"{course_id} exam sizes mid={len(mid)} final={len(final)}")
    return {"mid": mid, "final": final}
''',
        encoding="utf-8",
    )

    write_alignment("WIRELESS_6G", "WIRELESS_6G", [
        {"source_id": "3GPP_5G_ADVANCED_OVERVIEW", "reuse_class": "PUBLIC_REFERENCE_ONLY",
         "coverage": [{"domain": "nr_evolution", "waike_weeks": [2, 3, 4]}, {"domain": "ntn", "waike_weeks": [5]}, {"domain": "ai_ran_study", "waike_weeks": [7, 9]}]},
        {"source_id": "ORAN_ALLIANCE_VOCAB", "reuse_class": "PUBLIC_REFERENCE_ONLY",
         "coverage": [{"domain": "interfaces", "waike_weeks": [9]}]},
    ])
    write_alignment("ROBOTICS_CONTROL", "ROBOTICS_CONTROL", [
        {"source_id": "INDUSTRIAL_ROBOT_OPERATOR_TOPICS", "reuse_class": "PUBLIC_REFERENCE_ONLY",
         "coverage": [{"domain": "kinematics", "waike_weeks": [1, 2]}, {"domain": "control", "waike_weeks": [3, 4]}, {"domain": "safety", "waike_weeks": [6, 10]}]},
    ])
    write_alignment("GAME_DEV_INTERACTIVE", "GAME_DEV_INTERACTIVE", [
        {"source_id": "UNITY_ASSOCIATE_TOPICS", "reuse_class": "PUBLIC_REFERENCE_ONLY",
         "coverage": [{"domain": "gameplay", "waike_weeks": [1, 2, 4]}, {"domain": "audio", "waike_weeks": [3]}, {"domain": "a11y", "waike_weeks": [9]}]},
        {"source_id": "GODOT_FUNDAMENTALS_TOPICS", "reuse_class": "PUBLIC_REFERENCE_ONLY",
         "coverage": [{"domain": "scenes_input", "waike_weeks": [5, 6]}]},
    ])

    # Fix __init__ newline
    (OUT / "__init__.py").write_text(
        '"""WAIKE-COURSE-READY-004 batch packages (WIRELESS_6G, ROBOTICS_CONTROL, GAME_DEV_INTERACTIVE)."""\n',
        encoding="utf-8",
    )

    print(json.dumps({
        "wrote": str(OUT),
        "courses": sorted(courses),
        "lesson_mins": {cid: min(len(w["lesson"]) for w in c["weeks"]) for cid, c in courses.items()},
        "quiz_items": {cid: sum(len(w["quiz"]) for w in c["weeks"]) for cid, c in courses.items()},
    }, indent=2))


if __name__ == "__main__":
    main()
