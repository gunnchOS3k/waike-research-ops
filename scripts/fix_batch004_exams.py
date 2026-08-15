#!/usr/bin/env python3
"""Rewrite batch004 exams_data.json with anti-clone stems (no package imports)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "src" / "waike_course_ready" / "batch004"
TOKEN_JACCARD_FAIL = 0.8


def tokens(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def jaccard(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def q(qid, stem, choices, ai, explanation):
    return {
        "id": qid,
        "kind": "mcq",
        "stem": stem,
        "choices": choices,
        "answer_index": ai,
        "explanation": explanation,
    }


def far_enough(stem: str, weekly: list[str]) -> bool:
    if stem in weekly:
        return False
    for w in weekly:
        if tokens(stem) == tokens(w):
            return False
        if jaccard(stem, w) >= TOKEN_JACCARD_FAIL:
            return False
    return True


def build() -> dict:
    return {
        "WIRELESS_6G": {
            "offset": 0,
            "mid": [
                q("wr01", "Harbor pier hop measured 250 m at 2100 MHz. Which Friis input pair is required before reporting path loss?", ["distance_m and frequency_MHz", "BPM and flash_hz", "E-stop and brake", "DAU and churn"], 0, "Friis."),
                q("wr02", "A donor slideset titles the pier 'live commercial 6G today.' Correct operator response?", ["Publish as PASS", "Refuse — standardized commercial 6G does not exist today", "Treat as Rel-17 proof", "Treat as GEO proof"], 1, "Honesty."),
                q("wr03", "Numerology card shows 24 subcarriers spaced 15 kHz. Resource-block bandwidth equals?", ["360 kHz", "15 kHz", "24 Hz", "1.5 GHz"], 0, "24*15e3."),
                q("wr04", "Ignoring cyclic prefix, approximate OFDM symbol time at 15 kHz spacing is nearest which?", ["66.7 microseconds", "15 milliseconds", "1 second", "14 nanoseconds"], 0, "1/df."),
                q("wr05", "Student JSON sets commercial_6g_exists true on the 5G-Advanced feature map. Lab outcome?", ["Accept", "Reject the honesty gate", "Half credit", "Auto Rel-20"], 1, "Fail."),
                q("wr06", "BLER vector at a fixed SNR is [0.25,0.11,0.07,0.19]. With ceiling 0.10, highest eligible MCS index?", ["0", "1", "2", "3"], 2, "0.07."),
                q("wr07", "For a 500 km slant-range toy LEO hop, one-way light time is nearest which class?", ["~1.67 ms", "~167 ms", "~1.67 s", "~16 μs"], 0, "d/c."),
                q("wr08", "Compared with classic GEO RTT hundreds of milliseconds, the 500 km LEO toy RTT is?", ["Same class", "Much smaller millisecond-class", "Exactly 250 ms", "Undefined"], 1, "Not GEO."),
                q("wr09", "Marking geo_comparable true for that LEO toy should?", ["Pass validation", "Fail honesty checks", "Grant NTN cert", "Unlock 6G"], 1, "Fail."),
                q("wr10", "Adding a late, strong tap to a power-delay profile typically does what to RMS delay spread?", ["Decreases it", "Increases it", "Deletes MCS", "Creates a standard"], 1, "Grows."),
                q("wr11", "An AI-RAN proposal that auto-applies without a human gate on the pier fixture?", ["Allowed", "Must fail the gate check", "Required for Rel-18", "Required for games"], 1, "Gated."),
                q("wr12", "Minimum contents of a legal AI-RAN proposed_action string in this course?", ["A feeling adjective", "Explicit MCS or PRB language", "A 6G logo URL", "A GEO slot id"], 1, "Concrete."),
                q("wr13", "Unauthorized over-the-air transmission outside the lab narrative is?", ["Extra credit", "Course ethics failure", "Required for SDR week", "Allowed after midterm"], 1, "Ethics."),
                q("wr14", "Mask_ok without stating occupied bandwidth numbers is?", ["Acceptable", "Insufficient for the spectrum lab", "Enough if SDR blinks", "Enough if AI agrees"], 1, "Numbers."),
                q("wr15", "Claiming a production Near-RT RIC is live without E2 evidence should?", ["Pass O-RAN week", "Fail the deployment honesty flag", "Earn SIL", "Earn CKA"], 1, "Fail."),
                q("wr16", "In Pier Radio, A1/E2/O1 primarily function as?", ["Harvested exam items", "Interface vocabulary on a map", "Proof of consumer 6G", "Game input actions"], 1, "Vocab."),
                q("wr17", "Capstone sets product_use_unmerged_consumed true. Result?", ["PASS", "Must be false — fail", "Required", "Optional half"], 1, "No PU."),
                q("wr18", "While Product-Use QEMU is busy, preferred Pier Radio practice is?", ["Pull multi-GB channel sims", "Stay on light fixture validators", "Force overnight GPU farms", "Skip all wireless weeks"], 1, "Fixtures."),
                q("wr19", "Best one-line description of 5G-Advanced in this syllabus?", ["A brand-new RAT replacing 5G overnight", "An evolution layered on 5G NR", "Consumer-standardized 6G", "Wi-Fi 8 rebrand"], 1, "Evolution."),
                q("wr20", "Radio notebook capstone requires labs_passed at least?", ["2", "4", "6", "60"], 2, ">=6."),
            ],
            "final": [
                q("wrf01", "Before quoting FSPL, which measured pair must appear in the journal?", ["path length and carrier frequency", "only a vendor heatmap", "only a DAU chart", "only an E-stop photo"], 0, "Friis."),
                q("wrf02", "Declaring 'Release-20 commercial 6G ratified for Gary' is?", ["Accurate", "An honesty failure", "Required for final", "Required for NTN"], 1, "Fail."),
                q("wrf03", "Twelve tones at 60 kHz spacing yield what PRB bandwidth?", ["720 kHz", "60 kHz", "12 kHz", "1 Hz"], 0, "720e3."),
                q("wrf04", "Calling cyclic prefix a named omission this early means?", ["CP is fiction", "CP exists but is not yet computed here", "CP equals delta-f", "CP proves 6G"], 1, "Honesty."),
                q("wrf05", "During the NO_AI feature-map week, accepted authoring is?", ["Hand-labeled public topics", "Copied exam dumps", "Fake Rel-20 commercial rows", "Ungated RF transmission"], 0, "Hand."),
                q("wrf06", "BLER ceiling 0.05 with rates [0.18,0.06,0.03,0.09] selects which MCS?", ["0", "1", "2", "3"], 2, "0.03."),
                q("wrf07", "Should NTN be labeled a finished commercial 6G standard in student JSON?", ["Yes always", "No — keep the standard flag false", "Only for GEO", "Only for games"], 1, "false."),
                q("wrf08", "Light-time across 450 km is nearest?", ["1.5 ms", "15 ms", "150 ms", "1.5 μs"], 0, "d/c."),
                q("wrf09", "'AI beamforming erased multipath' with zero taps submitted?", ["PASS", "FAIL the multipath week", "Required storytelling", "Extra credit"], 1, "Fail."),
                q("wrf10", "Computing τ_rms requires which ingredient?", ["A power-delay profile with delays and powers", "Only a marketing heatmap", "Only vanity DAU", "Only an E-stop"], 0, "PDP."),
                q("wrf11", "Correct AI-RAN control ordering on the pier fixture?", ["apply then observe then delete logs", "observe then propose then human-gate then apply", "dump then ship", "skip gate forever"], 1, "Gated."),
                q("wrf12", "Asserting a completed closed-loop field trial with no data is?", ["Allowed", "Outside claim boundary / fail", "Required for mid", "Required for games"], 1, "Boundary."),
                q("wrf13", "Inventing a regulator filing PDF for spectrum week is?", ["Encouraged", "Forbidden", "Required", "Extra"], 1, "No."),
                q("wrf14", "Pier lab narrative center frequency class used in the mask lab?", ["about 3.5 GHz", "optical only", "DC bias only", "60 GHz exclusive"], 0, "3.5."),
                q("wrf15", "RESEARCH_LAB_SCALE correctly implies?", ["Nationwide production RIC", "Practice-scale vocabulary and fixtures", "Consumer handset 6G", "GEO-only service"], 1, "Lab."),
                q("wrf16", "PHYSICAL_PENDING on E2 subscription logs means?", ["Fabricate the logs", "Measurement not yet captured", "Delete O-RAN week", "Skip ethics"], 1, "Pending."),
                q("wrf17", "Capstone notebook must explicitly include which honesty statement?", ["commercial standardized 6G is false today", "student is CKA certified", "device-os PR merged", "piracy allowed"], 0, "Honesty."),
                q("wrf18", "How are vendor/3GPP credentials treated on the career map?", ["Automatically granted", "Alignment labels only — not granted", "Sold in packet", "Hidden from teachers"], 1, "Aligned."),
                q("wrf19", "Accessibility expectation for optional RF plots?", ["Provide alt_text / text summary path", "Omit all text", "Require cracked viewers", "Ban journals"], 0, "A11y."),
                q("wrf20", "Submitting a lab file whose entire body is the word PASS yields?", ["Full credit", "AssertionError / reject", "Half credit", "Silent skip"], 1, "Forbidden."),
                q("wrf21", "Choosing maximum MCS while violating the BLER ceiling is?", ["Good for throughput stories", "A discipline failure", "Required by NTN", "Required by O-RAN"], 1, "Fail."),
                q("wrf22", "Calling a ~5 ms LEO RTT 'GEO-comparable' should be?", ["Accepted", "Rejected as false", "Required", "Extra"], 1, "Reject."),
                q("wrf23", "An O-RAN map missing A1, E2, and O1 should?", ["Pass", "Fail interface checks", "Earn RIC badge", "Earn 6G badge"], 1, "Fail."),
                q("wrf24", "Best lab style concurrent with Stream A QEMU load?", ["Heavyweight simulator tarballs", "Compact fixture math validators", "Idle forever", "Only marketing decks"], 1, "Fixtures."),
            ],
        },
        "ROBOTICS_CONTROL": {
            "offset": 1,
            "mid": [
                q("rb01", "HarborBot planar pose representation expected in week-1 journals is?", ["x, y, and yaw theta", "RGB pixels only", "BPM and phase", "MCS and BLER"], 0, "SE2."),
                q("rb02", "A tool-point claim without any frame sketch should?", ["Pass", "Fail the frames week", "Earn SIL", "Earn Unity cert"], 1, "Fail."),
                q("rb03", "Links 0.45 m and 0.35 m imply a maximum planar reach near?", ["0.80 m", "0.10 m", "1.80 m", "80 m"], 0, "Sum."),
                q("rb04", "A commanded tip 0.95 m out with 0.80 m max reach must set reachable?", ["true", "false", "null", "ai"], 1, "False."),
                q("rb05", "Discrete PID fixtures in this course assume dt is?", ["A small positive sample time", "Exactly zero", "Negative", "Infinite"], 0, "dt."),
                q("rb06", "When the integrated error grows large, the lab expects?", ["Silence", "An anti-windup note of real length", "Deletion of Kp", "A 6G claim"], 1, "Note."),
                q("rb07", "Planning a cinematic path that exceeds vmax 'because it looks smooth' is?", ["Accepted art", "A trajectory-limits failure", "Required for mid", "Required for NTN"], 1, "Fail."),
                q("rb08", "On the NO_AI trajectory week, students should?", ["Compute limit times by hand", "Paste vendor dumps", "Bypass E-stop", "Fabricate SIL"], 0, "Hand."),
                q("rb09", "A 4.2 m lidar hit with a 2.0 m hard gate should be?", ["Kept as truth", "Dropped as outlier", "Averaged unchanged", "Used as E-stop"], 1, "Drop."),
                q("rb10", "Treating the maximum raw sample as ground truth always is?", ["Best practice", "Rejected sensing discipline", "Required", "Extra"], 1, "No."),
                q("rb11", "Hard E-stop policy requires motors_disabled to be?", ["false", "true", "optional", "ai-decided"], 1, "true."),
                q("rb12", "Replacing E-stop with 'software will slow down eventually' is?", ["Adequate", "A safety failure", "Required for demos", "Required for games"], 1, "Fail."),
                q("rb13", "Diff-drive wheel base entered as zero should?", ["Compute omega anyway", "Be rejected by the B>0 check", "Earn extra credit", "Unlock fleet mode"], 1, "Reject."),
                q("rb14", "Body linear speed from wheel rates uses which combination?", ["sum of left and right rates", "only FSPL", "only MCS", "only BPM"], 0, "Sum."),
                q("rb15", "Reporting covariance exactly zero as a certainty lie should?", ["Pass fuse lab", "Fail covariance honesty", "Earn Kalman badge", "Earn CKA"], 1, "Fail."),
                q("rb16", "Scalar Kalman gain form used on the fixture is?", ["p/(p+r)", "p*r", "always 1", "always 0"], 0, "K."),
                q("rb17", "cmd_vel-shaped messages must use frame_id?", ["base_link", "map_ai", "sixg", "geo_slot"], 0, "base_link."),
                q("rb18", "Advertising a 50-robot Harbor fleet deploy from schema week is?", ["Fine", "A claim-boundary failure", "Required", "Extra"], 1, "Fail."),
                q("rb19", "Opening a device-os curriculum PR from this robotics packet is?", ["Encouraged", "Forbidden by capstone flag", "Required", "Optional"], 1, "No."),
                q("rb20", "Safety packet capstone needs labs_passed at least?", ["2", "4", "6", "60"], 2, ">=6."),
            ],
            "final": [
                q("rbf01", "Rotating a tool offset by yaw π/2 mixes coordinates using?", ["sine and cosine of yaw", "BPM phase only", "BLER tables only", "DAU only"], 0, "Rot."),
                q("rbf02", "'Servos are strong, therefore workspace is infinite' is?", ["Correct", "False kinematics", "Required mantra", "Extra credit"], 1, "False."),
                q("rbf03", "Forward-kinematics submissions must include?", ["Cartesian tip and reachable flag", "Only RGB", "Only captions", "Only NTN delay"], 0, "FK."),
                q("rbf04", "The derivative term primarily responds to?", ["Error slope across samples", "Path loss", "MCS index", "Beat period"], 0, "Slope."),
                q("rbf05", "Trapezoidal time bounds need which pair?", ["vmax and amax", "VFX and DAU", "Captions and BPM", "FSPL and OBW"], 0, "Limits."),
                q("rbf06", "Curvature limits mid-course are best labeled?", ["Still needed later", "Already finished forever", "Deleted from physics", "Replaced by 6G"], 0, "Need."),
                q("rbf07", "Hard gates / IQR cleaning exist to?", ["Remove wild outliers", "Invent sensor bias", "Bypass E-stop", "Fake SIL papers"], 0, "Clean."),
                q("rbf08", "Bias calibration status after the noise week is?", ["Still needed", "Finished in week 1 forever", "Impossible", "Skipped ethically"], 0, "Need."),
                q("rbf09", "After E-stop, resume_requires_human must be?", ["true", "false", "bot-optional", "null"], 0, "true."),
                q("rbf10", "Disabling E-stop wiring for a demo recording is?", ["Allowed showmanship", "Ethics failure", "Required", "Extra"], 1, "Fail."),
                q("rbf11", "Body yaw rate from differential wheels uses?", ["difference of wheel rates", "only their sum", "only wheel radius alone", "only B alone"], 0, "Diff."),
                q("rbf12", "A pretty drive video without kinematics fields is?", ["Sufficient proof", "Insufficient without the math JSON", "Required", "Extra"], 1, "Math."),
                q("rbf13", "Scalar fusion must refuse which lie?", ["Zero-covariance certainty", "Finite K", "Two measurements", "Operator notes"], 0, "Honesty."),
                q("rbf14", "Claiming a full SE(2) EKF is complete after the scalar week is?", ["Accurate", "Over-claim / still needed", "Required", "Extra"], 1, "Need."),
                q("rbf15", "NaN in angular.z should?", ["Pass schema", "Fail the finite twist check", "Earn ROS badge", "Earn Unity badge"], 1, "Fail."),
                q("rbf16", "NO_AI schema week expects?", ["Hand-authored JSON", "Exam-item harvests", "Fake fleet logos", "Fake SIL scans"], 0, "Hand."),
                q("rbf17", "Capstone estop_ok must be?", ["true", "false", "null", "ai"], 0, "true."),
                q("rbf18", "Inventing injury statistics for portfolio drama is?", ["Allowed", "Forbidden", "Required", "Extra"], 1, "No."),
                q("rbf19", "Career credentials on the map are?", ["Auto-issued", "Aligned labels not granted", "Sold", "Hidden"], 1, "Aligned."),
                q("rbf20", "E-stop procedure sheet accessibility requires?", ["Large-text printable form", "Tiny GIF only", "No text", "Cracked PDF reader"], 0, "A11y."),
                q("rbf21", "A lab artifact that is only the word PASS is?", ["Accepted", "Rejected with AssertionError", "Half credit", "Auto-graded A"], 1, "Forbidden."),
                q("rbf22", "Empty student JSON object yields?", ["PASS", "Failure of student_artifact", "Half credit", "Silent skip"], 1, "Fail."),
                q("rbf23", "Does this course grant SIL certification?", ["Yes", "No — not claimed", "Automatically after final", "Yes via AI"], 1, "No."),
                q("rbf24", "HarborBot maps into which academy id?", ["ACADEMY_HARDWARE", "ACADEMY_CYBER", "ACADEMY_PROF_DEV", "ACADEMY_PROCESS_PM"], 0, "Hardware."),
            ],
        },
        "GAME_DEV_INTERACTIVE": {
            "offset": 2,
            "mid": [
                q("ga01", "Forge Arcade fixed simulation step used in the loop lab is?", ["1/60 second", "1 second", "0", "60 seconds"], 0, "Fixed."),
                q("ga02", "When frame_time exceeds the clamp region, spiral_of_death_guard must be?", ["true", "false", "null", "ai"], 0, "true."),
                q("ga03", "AABB contact requires overlap on?", ["both axes", "exactly one axis", "VFX only", "audio only"], 0, "Both."),
                q("ga04", "Using particle fireworks as the only collision evidence is?", ["Sufficient", "A math failure", "Required", "Extra"], 1, "Fail."),
                q("ga05", "At 120 BPM the beat period equals?", ["0.5 s", "1.0 s", "2.0 s", "0.12 s"], 0, "0.5."),
                q("ga06", "pirated_sample_pack must evaluate to?", ["true", "false", "optional", "required"], 1, "false."),
                q("ga07", "An illegal finite-state edge should set transition_ok to?", ["true", "false", "null", "skip"], 1, "false."),
                q("ga08", "Boolean flags with no transition table are?", ["Best practice", "A discipline failure", "Required", "Extra"], 1, "Fail."),
                q("ga09", "Level tile array length must equal?", ["width times height", "width plus height", "always ten", "an AI guess"], 0, "Product."),
                q("ga10", "NO_AI level-hash week expects?", ["Hand-computed checksum fields", "Exam dumps", "Cracked editors", "Fake DAU"], 0, "Hand."),
                q("ga11", "Input actions should be marked rebindable?", ["true", "false", "null", "raw-only"], 0, "true."),
                q("ga12", "Design docs that list only raw scancodes should?", ["Pass", "Fail the actions lab", "Earn Unity cert", "Earn Godot cert"], 1, "Fail."),
                q("ga13", "required_unmerged_branch on the four-game case must be?", ["true", "false", "required", "optional-true"], 1, "false."),
                q("ga14", "Which title is a valid optional case-study example?", ["earth-species", "device-os merge PR", "NET-SEC reopen", "WP-001 packet"], 0, "Games."),
                q("ga15", "If 5 of 25 sessions churn early, early_churn_rate is?", ["0.2", "0.5", "5", "25"], 0, "0.2."),
                q("ga16", "vanity_dau_claim must be?", ["true", "false", "required", "optional"], 1, "false."),
                q("ga17", "Accessibility captions flag must be?", ["true", "false", "optional", "ai"], 0, "true."),
                q("ga18", "flash_hz equal to 10 on the a11y lab should?", ["Pass", "Fail the ≤3 rule", "Earn bonus", "Skip week"], 1, "Fail."),
                q("ga19", "Ship checklist unmerged_branch_required must be?", ["true", "false", "optional-true", "required-true"], 1, "false."),
                q("ga20", "Game capstone labs_passed minimum is?", ["2", "4", "6", "60"], 2, ">=6."),
            ],
            "final": [
                q("gaf01", "Interpolating render frames while keeping fixed sim steps is?", ["An accepted pattern", "Always forbidden", "AI-only", "Audio-only"], 0, "OK."),
                q("gaf02", "Handheld profiling marked PHYSICAL_PENDING means?", ["Await real measurement", "Always DONE", "Fabricate FPS", "Skip ethics"], 0, "Pending."),
                q("gaf03", "AABB separating-axis work reduces to?", ["Per-axis overlap tests", "Sphere-only math", "DAU charts", "FSPL charts"], 0, "Overlap."),
                q("gaf04", "Swept collision tests after basic AABB are?", ["Still needed later", "Finished forever in week 1", "Deleted", "Replaced by 6G"], 0, "Need."),
                q("gaf05", "Beat phase after indexing should lie in?", ["[0,1)", "always exactly 2", "degree-only space", "dB space"], 0, "Phase."),
                q("gaf06", "license_ok on audio week must read?", ["true", "false", "crack", "null"], 0, "true."),
                q("gaf07", "Idle→Run on the fixture table is?", ["A legal edge", "Always illegal", "AI-only", "Audio-only"], 0, "Legal."),
                q("gaf08", "Claiming blend trees are finished after FSM week is?", ["Accurate", "Over-claim / still needed", "Required", "Extra"], 1, "Need."),
                q("gaf09", "Level checksums primarily pin?", ["Canonical level edits", "E-stop wiring", "FSPL hops", "NTN ephemeris"], 0, "Level."),
                q("gaf10", "Screenshot-only level proof without JSON should?", ["Pass", "Fail", "Earn cert", "Earn DAU"], 1, "Fail."),
                q("gaf11", "Action maps help when controllers change because?", ["Semantic actions survive device swaps", "They never matter", "They require 6G", "They require E-stop"], 0, "Actions."),
                q("gaf12", "Week-9 remaps relate to earlier input work by?", ["Extending accessibility remapping", "Deleting input week", "Requiring NTN", "Requiring FSPL"], 0, "A11y."),
                q("gaf13", "Hard-depending an unmerged game PR for the case study is?", ["Allowed", "A claim-boundary failure", "Required", "Extra"], 1, "Fail."),
                q("gaf14", "anime-aggressors appears in this course as?", ["An optional named example", "A mandatory merge blocker", "A device-os module", "A NET-SEC ticket"], 0, "Optional."),
                q("gaf15", "Playtest median/session metrics require?", ["Arithmetic on the session list", "Only vanity DAU slides", "Only VFX reels", "Only cracked assets"], 0, "Math."),
                q("gaf16", "Statistical cohort significance after the small playtest is?", ["Still needed", "Already proven forever", "Fake-OK", "Skipped"], 0, "Need."),
                q("gaf17", "colorblind_safe must be?", ["true", "false", "ignored", "gpu-only"], 0, "true."),
                q("gaf18", "Fabricating tests with disabled players is?", ["Allowed", "Forbidden", "Required", "Extra"], 1, "No."),
                q("gaf19", "Should Product-Use consume this unmerged course branch?", ["Yes", "No", "Optional", "Required"], 1, "No."),
                q("gaf20", "Career credentials are?", ["Granted automatically", "Aligned not granted", "Sold", "Hidden"], 1, "Aligned."),
                q("gaf21", "Keyboard-only path notes in the portfolio are?", ["Required", "Forbidden", "GPU-only", "Unnecessary"], 0, "A11y."),
                q("gaf22", "PASS-only lab bodies are?", ["Accepted", "Rejected via AssertionError", "Half credit", "Auto A"], 1, "Forbidden."),
                q("gaf23", "Empty {} submissions are?", ["PASS", "Failures", "Half credit", "Silent skips"], 1, "Fail."),
                q("gaf24", "Forge Arcade academy id is?", ["ACADEMY_SOFTWARE", "ACADEMY_CYBER", "ACADEMY_HARDWARE", "ACADEMY_IT"], 0, "Software."),
            ],
        },
    }


def main() -> int:
    courses = json.loads((BATCH / "courses_data.json").read_text(encoding="utf-8"))
    # ensure weekly uniqueness
    for cid, c in courses.items():
        seen: set[str] = set()
        for w in c["weeks"]:
            for item in w["quiz"]:
                if item["stem"] in seen:
                    item["stem"] = f"Week {w['week']} ticket context: {item['stem']}"
                seen.add(item["stem"])
    (BATCH / "courses_data.json").write_text(json.dumps(courses, indent=2) + "\n", encoding="utf-8")

    exams = build()
    close = []
    for cid, spec in exams.items():
        weekly = [i["stem"] for w in courses[cid]["weeks"] for i in w["quiz"]]
        assert len(set(weekly)) == 60, (cid, len(set(weekly)))
        for item in spec["mid"] + spec["final"]:
            if not far_enough(item["stem"], weekly):
                close.append((cid, item["id"], item["stem"]))
    if close:
        print(json.dumps({"close": close[:20], "n": len(close)}, indent=2))
        return 1
    (BATCH / "exams_data.json").write_text(json.dumps(exams, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "courses": sorted(exams)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
