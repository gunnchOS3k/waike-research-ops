#!/usr/bin/env python3
"""Generate batch008 course data: SEVEN_GC_APPRENTICESHIP (7GC AI-RAN Research Bench).

Lessons, quizzes, and exams are authored here, one week at a time; nothing is
padded to reach the depth floor. Numbers in lessons match the graders in
batch008/labs.py, which recompute them from submitted inputs.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "src" / "waike_course_ready" / "batch008"
COURSE_ID = "SEVEN_GC_APPRENTICESHIP"


def _q(qid: str, stem: str, choices: list[str], explain: str) -> dict:
    return {"id": qid, "kind": "mcq", "stem": stem, "choices": choices, "answer_index": 0, "explanation": explain}


WEEKS = [
    {
        "week": 1,
        "title": "Research question and claim ledger",
        "lab_id": "lab_sga_claim_ledger",
        "worked_example": "claim A: SYNTHETIC_SIM; claim B: CITED_SPEC source_id=3GPP_TR_38_811_NTN; claim C: MEASURED dataset_ref=none-yet status=OPEN",
        "lesson": (
            "Research Bench ticket SGA-1101 opens the apprenticeship with a question small enough to answer: "
            "does a codebook prior raise top-3 beam accuracy on a synthetic LEO scenario? Before any code runs, "
            "write a claim ledger. Every sentence you might later put in a poster gets one row and one evidence class. "
            "SYNTHETIC_SIM means your own simulator produced it, so the claim is only as strong as the model's assumptions. "
            "CITED_SPEC means a standards document states it, and the row must name the source_id, for example the 3GPP "
            "NTN study TR 38.811. MEASURED means field or bench data exist and the row points at a dataset_ref you can hand "
            "to a reviewer. A MEASURED row with no dataset is not a weak claim; it is an open question, and the ledger should "
            "say OPEN rather than quietly drop it. The 7GC campuses share one more rule: no row may imply that a university, "
            "operator, or vendor endorses the work, so affiliation_claim stays false. Mentors read the ledger before the "
            "results, because a tidy chart built on an unlabeled claim is the most common way an apprenticeship poster goes wrong."
        ),
        "assignment": "Submit lab_sga_claim_ledger JSON for SGA-1101 with at least three labeled claims and affiliation_claim false.",
        "quiz": [
            ("A ledger row says MEASURED but has no dataset_ref. What should it become?", ["An OPEN question until data exist", "A SYNTHETIC_SIM result", "A CITED_SPEC claim", "A removed row with no trace"], "unbacked measurement is open"),
            ("Which evidence class requires a source_id?", ["CITED_SPEC", "SYNTHETIC_SIM", "MEASURED", "OPEN"], "cited claims name the spec"),
            ("Why is affiliation_claim fixed to false on the Research Bench?", ["No institution has endorsed the apprentice work", "Affiliations slow the simulator", "3GPP forbids naming universities", "It is optional metadata"], "no implied endorsement"),
            ("A simulator output supports a claim. How strong is that claim?", ["As strong as the simulator's assumptions", "Equal to a field trial", "Stronger than any spec", "Independent of configuration"], "sim inherits model assumptions"),
            ("When should the claim ledger be written?", ["Before any results are generated", "After the poster is printed", "Only if a reviewer asks", "After choosing the best seed"], "ledger first"),
            ("Which document anchors NTN delay statements in this course?", ["3GPP TR 38.811", "IEEE 802.11ax", "RFC 9293", "ISO 9001"], "TR 38.811 is the NTN study"),
        ],
    },
    {
        "week": 2,
        "title": "Reproducible runs — config digest, seed, and rerun",
        "lab_id": "lab_sga_repro_manifest",
        "worked_example": "config_text='scenario=leo600_sband\\nseed=20261102\\nbeams=8\\nepochs=5\\n' → sha256 recorded; rerun_metric_a == rerun_metric_b == 0.625",
        "lesson": (
            "SGA-1202 turns the week-one question into something another apprentice can rerun on a different campus. "
            "A run manifest has four parts. The config text is the exact file the simulator read, byte for byte, and its "
            "SHA-256 digest proves which file that was; changing a single newline changes the digest, so the grader recomputes "
            "it rather than trusting a pasted hash. The seed must be an integer you chose and wrote down, not the word random, "
            "because an unpinned generator makes every comparison later in the course meaningless. The command line is "
            "recorded verbatim, including flags, so nobody has to guess which entry point produced a figure. Finally, run the "
            "same seed and config twice and report both metrics. If they differ, something nondeterministic is leaking in: "
            "thread scheduling, an unseeded library, or a timestamp in the config. Track that down before moving on. Gary, "
            "Geelong, and Nubuke cohorts swap manifests in week ten, and a figure whose manifest does not reproduce is removed "
            "from the shared packet rather than footnoted."
        ),
        "assignment": "Submit lab_sga_repro_manifest JSON for SGA-1202: config_text, its sha256, integer seed, exact command, and two identical reruns.",
        "quiz": [
            ("Why does the grader recompute the config digest?", ["A pasted hash may not match the file actually used", "Hashing is faster than reading", "Digests replace the seed", "SHA-256 is only for passwords"], "verify, don't trust"),
            ("Two reruns with the same seed and config disagree. What does that signal?", ["Hidden nondeterminism to fix before comparing", "The model is improving", "Normal sampling noise to average away", "The digest is wrong"], "nondeterminism leak"),
            ("Which seed value fails the manifest check?", ["\"random\"", "20261102", "7", "0"], "seed must be an integer"),
            ("What happens to a week-ten figure whose manifest does not reproduce?", ["It is removed from the shared packet", "It gets a footnote", "It is kept if it looks good", "It is rerun with a new seed until it matches"], "non-reproducible figures removed"),
            ("Changing one newline in config_text does what to the SHA-256?", ["Changes the digest completely", "Leaves it unchanged", "Changes only the last hex digit", "Makes it invalid"], "avalanche property"),
            ("Why record the command line verbatim?", ["So nobody guesses which entry point or flags made a figure", "To make the manifest longer", "Because shells require it", "To hide the config"], "exact provenance"),
        ],
    },
    {
        "week": 3,
        "title": "NTN propagation delay — nadir one-way and round trip",
        "lab_id": "lab_sga_ntn_delay",
        "worked_example": "h=600 km: one_way = 600 / 299792.458 km/s = 2.0014 ms; rtt = 4.0028 ms. GEO h=35786 km: one_way ≈ 119.37 ms",
        "lesson": (
            "SGA-1303 is the first physics week. A non-terrestrial network puts the base station, or a relay for it, on a "
            "satellite, and the first consequence is time. Light covers 299,792.458 km per second, so a low-Earth-orbit "
            "satellite directly overhead at 600 km is about 2.0014 ms away one way and 4.0028 ms round trip. A geostationary "
            "satellite at 35,786 km is about 119.37 ms one way, which is why GEO links feel sluggish for interactive traffic even "
            "with ample bandwidth. These are nadir numbers: the satellite straight above the user. At low elevation the slant "
            "range can be several times the altitude, so the real delay is longer, and the lab asks you to state geometry = nadir "
            "so nobody mistakes a lower bound for a link budget. The 3GPP NTN study, TR 38.811, discusses why terrestrial timing "
            "assumptions such as HARQ round trips and timing advance must be stretched for these distances. The grader "
            "recomputes your delay from the altitude you submit, so copying the LEO answer onto a GEO altitude fails, which is "
            "exactly the mistake this week is designed to catch."
        ),
        "assignment": "Submit lab_sga_ntn_delay JSON for SGA-1303: altitude_km, one_way_ms, rtt_ms, and geometry = nadir.",
        "quiz": [
            ("What is the nadir one-way delay to a satellite at 600 km?", ["About 2.0 ms", "About 20 ms", "About 0.2 ms", "About 119 ms"], "600/299792.458 s"),
            ("Roughly how long is a one-way GEO nadir delay?", ["About 119 ms", "About 2 ms", "About 12 ms", "About 1.2 s"], "35786 km / c"),
            ("Why must the lab state geometry = nadir?", ["Slant range at low elevation is longer, so nadir is a lower bound", "Nadir delay is always the worst case", "3GPP only defines nadir", "Geometry changes the speed of light"], "nadir is the minimum"),
            ("Which terrestrial timing assumptions does NTN stretch?", ["HARQ round trips and timing advance", "Ethernet MTU size", "DNS TTL values", "Battery charge cycles"], "TR 38.811 timing"),
            ("Round-trip delay equals what?", ["Twice the one-way delay", "The one-way delay squared", "Half the one-way delay", "One-way plus 1 ms"], "rtt = 2 × one-way"),
            ("A student submits the 600 km delay with altitude_km = 35786. What happens?", ["The recompute fails", "It passes because delay is constant", "It passes with a warning", "The grader rounds it"], "recompute from inputs"),
        ],
    },
    {
        "week": 4,
        "title": "LEO Doppler — orbital speed and the upper bound",
        "lab_id": "lab_sga_leo_doppler",
        "worked_example": "v = sqrt(398600.4418 / (6371 + 600)) = 7.5617 km/s; f_d ≤ (v/c)·f_c = 50.45 kHz at 2 GHz",
        "lesson": (
            "SGA-1404 is a NO_AI week: work the numbers by hand and show each line. A satellite in a circular orbit moves at "
            "v = sqrt(μ / r), where μ for Earth is 398,600.4418 km³/s² and r is Earth's mean radius of 6,371 km plus the altitude. "
            "At 600 km that gives r = 6,971 km and v ≈ 7.5617 km/s, roughly 27,000 km/h. The carrier seen by a ground user shifts by "
            "the component of that velocity along the line of sight, so the shift can never exceed (v / c) · f_c. At a 2 GHz S-band "
            "carrier the bound is about 50.45 kHz, which is more than three times the 15 kHz subcarrier spacing of a common NR "
            "numerology, so uncompensated Doppler would smear subcarriers into each other. The true maximum seen from the ground "
            "is somewhat lower because Earth's curvature and the user's own rotation change the geometry, and it falls to zero "
            "as the satellite passes overhead. That is why the lab names this an upper bound and sets bound_is_upper = true. "
            "A bound is a design margin, not a measurement, and the claim ledger from week one should file it as SYNTHETIC_SIM or CITED_SPEC."
        ),
        "assignment": "Submit lab_sga_leo_doppler JSON for SGA-1404 (NO_AI): altitude_km, carrier_ghz, orbital_speed_km_s, doppler_bound_khz, bound_is_upper.",
        "quiz": [
            ("Circular orbital speed at 600 km altitude is closest to which value?", ["7.56 km/s", "11.2 km/s", "3.07 km/s", "0.46 km/s"], "sqrt(μ/r)"),
            ("Why is (v/c)·f_c called an upper bound?", ["Only the line-of-sight component shifts the carrier", "It includes atmospheric gain", "It is the measured shift", "It ignores the carrier"], "projection ≤ full speed"),
            ("At 2 GHz, how does the LEO Doppler bound compare with 15 kHz subcarrier spacing?", ["It is more than three times larger", "It is about equal", "It is negligible", "It is exactly 15 kHz"], "50 kHz vs 15 kHz"),
            ("What happens to Doppler as the satellite passes directly overhead?", ["It falls through zero", "It peaks", "It doubles", "It stays constant"], "radial velocity zero at zenith"),
            ("Which constant does the orbital speed formula use?", ["μ = 398,600.4418 km³/s²", "c = 299,792.458 km/s", "g = 9.81 m/s²", "h = 6.626e-34 J·s"], "Earth GM"),
            ("How should the claim ledger file a Doppler bound?", ["As SYNTHETIC_SIM or CITED_SPEC, not MEASURED", "As MEASURED", "As an affiliation claim", "It does not belong in the ledger"], "bound is not measurement"),
        ],
    },
    {
        "week": 5,
        "title": "Beam selection — top-1 and top-k accuracy",
        "lab_id": "lab_sga_beam_topk",
        "worked_example": "8 samples; top-1 hits at samples 1,3,5,7 → 0.5; top-3 misses only sample 6 → 0.875",
        "lesson": (
            "SGA-1505 moves from link physics to the learning problem behind the AI-RAN papers. A millimetre-wave or NTN cell "
            "sweeps a codebook of narrow beams, and exhaustive sweeping costs time and overhead. A beam-selection model looks "
            "at side information, such as position or a coarse channel estimate, and ranks the beams it thinks are best, so "
            "the radio only measures the top few. The honest metric is top-k accuracy: the fraction of samples whose true best "
            "beam appears in the model's first k guesses. On the eight-sample fixture in the lab readme, four samples rank the "
            "true beam first, giving top-1 = 0.5, and seven of eight contain it within three guesses, giving top-3 = 0.875. "
            "Read those numbers together: top-3 tells you a three-beam refinement sweep would usually succeed, while top-1 says "
            "the model alone is right only half the time. Top-k also hides how much signal is lost when the second-best beam is "
            "chosen, which week nine records as a construct-validity threat. The fixture is synthetic, so dataset_class must say so."
        ),
        "assignment": "Submit lab_sga_beam_topk JSON for SGA-1505 from the eight-sample fixture: top1, top3, n_samples, dataset_class.",
        "quiz": [
            ("What does top-3 accuracy measure?", ["Share of samples whose true beam is within the first three guesses", "Accuracy of the third-ranked beam only", "Average of three seeds", "SNR of the top three beams"], "membership in first k"),
            ("On the fixture, why is top-3 higher than top-1?", ["Three samples rank the true beam second or third", "The fixture has three classes", "Top-3 uses a different model", "Rounding"], "hits at ranks 2–3"),
            ("Why do beam-selection models exist at all?", ["Exhaustive codebook sweeps cost time and overhead", "Beams cannot be measured", "Codebooks are secret", "They replace the antenna"], "reduce sweep cost"),
            ("What does top-k accuracy fail to show?", ["How much SNR is lost when a non-best beam is chosen", "Whether the true beam was ranked", "The number of samples", "The codebook size"], "construct gap"),
            ("A top-1 of 0.5 and top-3 of 0.875 suggests which deployment?", ["Model ranks, radio refines over three beams", "Model alone picks the beam", "Exhaustive sweep is unnecessary at k=1", "Discard the model"], "rank then refine"),
            ("Which dataset_class must the fixture carry?", ["SYNTHETIC_SIM", "MEASURED", "CITED_SPEC", "PRIVATE_IQ"], "fixture is synthetic"),
        ],
    },
    {
        "week": 6,
        "title": "Baseline vs model — paired interval over seeds",
        "lab_id": "lab_sga_paired_ci",
        "worked_example": "diffs = [0.05,0.02,0.07,0.02,0.04]; mean 0.04; sd 0.0212; 95% CI = 0.04 ± 2.776·0.0212/√5 = [0.0137, 0.0663]",
        "lesson": (
            "SGA-1606 asks whether the model actually beats the baseline or merely got a lucky seed. Run both on the same five "
            "seeds and subtract run by run; pairing removes the shared difficulty of each seed, which is usually the largest "
            "source of spread. The fixture differences are 0.05, 0.02, 0.07, 0.02 and 0.04, with mean 0.04 and sample standard "
            "deviation about 0.0212. With only five pairs you need Student's t, not the normal 1.96: t at 0.975 with four degrees "
            "of freedom is 2.776, so the half-width is 2.776 × 0.0212 / √5 ≈ 0.0263 and the 95 percent interval runs from about "
            "0.0137 to 0.0663. It excludes zero, so the poster may say the model improved top-3 accuracy on this synthetic "
            "scenario, and should print the interval beside the claim. Had the interval crossed zero, the honest sentence would be "
            "that five seeds cannot distinguish the two. Notice what the interval does not license: it says nothing about another "
            "scenario, a real cell, or a different codebook. That limitation goes into next week's external-validity row, not into a caveat nobody reads."
        ),
        "assignment": "Submit lab_sga_paired_ci JSON for SGA-1606: mean_diff, ci_low, ci_high, and claims_improvement consistent with the interval.",
        "quiz": [
            ("Why subtract baseline from model run by run on the same seed?", ["Pairing cancels the shared difficulty of each seed", "It doubles the sample size", "It removes the need for a baseline", "Seeds must be discarded"], "paired design"),
            ("With five paired runs, which critical value builds the 95% interval?", ["t = 2.776 with 4 degrees of freedom", "z = 1.96", "t = 1.645", "z = 2.58"], "small-sample t"),
            ("The interval is [0.0137, 0.0663]. What may the poster claim?", ["Improvement on this synthetic scenario, with the interval printed", "Improvement in all deployments", "No difference", "A 6.6% guaranteed gain"], "scoped claim"),
            ("If the interval had crossed zero, what is the honest sentence?", ["Five seeds cannot distinguish the two methods", "The model is worse", "The model is better but noisy", "Rerun until it excludes zero"], "inconclusive"),
            ("Which source of spread does pairing usually remove?", ["Per-seed scenario difficulty", "Model capacity", "Codebook size", "Carrier frequency"], "seed difficulty"),
            ("Where does 'says nothing about a real cell' belong?", ["The external-validity row", "The seed list", "The config digest", "The title"], "external validity"),
        ],
    },
    {
        "week": 7,
        "title": "O-RAN control loops — where an AI model may act",
        "lab_id": "lab_sga_oran_loops",
        "worked_example": "HARQ 1 ms → real_time (DU); handover tuning 100 ms → near_real_time (xApp); energy policy 60 s → non_real_time (rApp); A1 → near_rt_ric",
        "lesson": (
            "SGA-1707 places the week-five model inside a real architecture. O-RAN splits radio control into loops by how fast "
            "they must react. Decisions under about 10 ms, such as HARQ retransmission and per-slot scheduling, stay in the "
            "distributed unit and its real-time software. Decisions between roughly 10 ms and one second run as xApps on the "
            "near-real-time RAN Intelligent Controller, which is where a beam-pair or handover tuning model would live. Anything "
            "slower than a second, including training, long-horizon energy policy, and analytics, runs as an rApp on the "
            "non-real-time RIC inside service management and orchestration. The non-real-time RIC guides the near-real-time RIC "
            "through the A1 interface with declarative policies, while E2 connects the near-real-time RIC to the base-station "
            "nodes it controls. The lab gives you three tasks; classify each by its loop latency, cover all three loops, and "
            "name the A1 target. Placing model training in the real-time loop is a design error, not an optimisation, and "
            "the grader treats it that way. O-RAN Alliance specifications are cited here for topic labels only."
        ),
        "assignment": "Submit lab_sga_oran_loops JSON for SGA-1707: at least three tasks with loop_ms and loop_class, plus a1_policy_target.",
        "quiz": [
            ("A model that tunes handover every 100 ms belongs where?", ["An xApp on the near-real-time RIC", "An rApp on the non-real-time RIC", "The DU real-time loop", "The core network billing system"], "10 ms–1 s"),
            ("Which interface carries declarative policy from non-RT RIC to near-RT RIC?", ["A1", "E2", "F1", "Xn"], "A1 policy"),
            ("Where does model training on a day of KPIs run?", ["An rApp in the non-real-time RIC", "An xApp", "The DU scheduler", "The UE modem"], ">1 s loop"),
            ("Which interface connects the near-RT RIC to the nodes it controls?", ["E2", "A1", "O1 only", "N2"], "E2 control"),
            ("HARQ retransmission timing sits in which loop?", ["Real-time, under about 10 ms", "Near-real-time", "Non-real-time", "Offline"], "sub-10 ms"),
            ("How does the grader treat training in the real-time loop?", ["As a design error", "As an optimisation", "As optional", "As extra credit"], "wrong loop"),
        ],
    },
    {
        "week": 8,
        "title": "Digital-twin gap — comparison is not calibration",
        "lab_id": "lab_sga_twin_gap",
        "worked_example": "twin − reference = [-1, 1, 1, 2] dB → RMSE = sqrt(7/4) = 1.3229 dB; measured_samples=0 → UNCALIBRATED_NO_MEASUREMENTS",
        "lesson": (
            "SGA-1808 confronts the gap the 7GC papers keep honest. A digital twin predicts received power across a site; the "
            "lab's twin gives -95, -97, -99 and -101 dBm at four points, and a separate reference simulator gives -94, -98, -100 "
            "and -103 dBm. The errors are -1, 1, 1 and 2 dB, their squares sum to 7, and the root-mean-square error is sqrt(7/4), "
            "about 1.32 dB. That number is useful: it says two models of the same site agree to roughly a decibel. It is not "
            "calibration. Calibration compares the twin with measurements from the real site, and in this course the count of "
            "field samples is zero. With zero measured samples the status must read UNCALIBRATED_NO_MEASUREMENTS and calibrated_claim "
            "must be false, however good the agreement looks. Two simulators can share the same wrong assumption, such as an "
            "optimistic clutter model, and agree perfectly while both miss reality. Paper I in the research spine records exactly "
            "this open gap. The apprentice's job is to state it clearly enough that the next cohort with radio access knows which measurements to collect."
        ),
        "assignment": "Submit lab_sga_twin_gap JSON for SGA-1808: rmse_db, measured_samples, calibration_status, calibrated_claim.",
        "quiz": [
            ("Twin vs reference errors are -1, 1, 1, 2 dB. What is the RMSE?", ["About 1.32 dB", "0.75 dB", "1.75 dB", "5 dB"], "sqrt(7/4)"),
            ("With zero field samples, what status must the twin carry?", ["UNCALIBRATED_NO_MEASUREMENTS", "CALIBRATED", "PARTIALLY_CALIBRATED", "VERIFIED"], "no measurements"),
            ("Why can two simulators agree and both be wrong?", ["They can share the same incorrect assumption", "Simulators never disagree", "RMSE hides agreement", "Seeds force agreement"], "shared bias"),
            ("What does calibration compare the twin against?", ["Measurements from the real site", "A second simulator", "The previous run", "The codebook"], "field data"),
            ("What is the most useful honest output of this week?", ["A clear list of which measurements the next cohort should collect", "A calibrated flag", "A lower RMSE", "A press release"], "state the gap"),
            ("A 1.3 dB twin-vs-sim RMSE justifies which statement?", ["The two models agree to about a decibel", "The twin is calibrated", "The site is measured", "The twin is deployed"], "agreement only"),
        ],
    },
    {
        "week": 9,
        "title": "Threats to validity and research ethics",
        "lab_id": "lab_sga_validity",
        "worked_example": "internal: 5 seeds; external: one synthetic scenario; construct: top-k ignores SNR loss; conclusion: n=5, wide CI",
        "lesson": (
            "SGA-1909 is the second NO_AI week, because the point is your own judgement about your own work. Sort what could "
            "make the results wrong into four kinds. Internal validity asks whether the comparison itself is fair: five seeds, "
            "a tuned model against an untuned baseline, or a data leak between training and test positions. External validity "
            "asks whether the result travels: one synthetic LEO scenario says little about a dense Gary street canyon or a Geelong "
            "port. Construct validity asks whether the metric measures what you care about: top-k accuracy ignores how many "
            "decibels are lost when the second-best beam is used. Conclusion validity asks whether the statistics support the "
            "sentence: five paired runs give a wide interval, and testing many metrics invites a lucky one. Then restate the "
            "guardrails every 7GC research program shares. Use synthetic data only. Never use private competition IQ captures, "
            "even if a teammate offers them. Make no claim that a university, operator, or agency endorses the work. A reviewer "
            "who sees honest threats listed early trusts the remaining claims more, not less."
        ),
        "assignment": "Submit lab_sga_validity JSON for SGA-1909 (NO_AI): threats for all four validity kinds plus the three guardrail flags.",
        "quiz": [
            ("A data leak between training and test positions threatens which validity?", ["Internal", "External", "Construct", "Conclusion"], "unfair comparison"),
            ("One synthetic LEO scenario cannot speak for a street canyon. Which validity?", ["External", "Internal", "Construct", "Conclusion"], "generalisation"),
            ("Top-k ignores decibels lost on the second-best beam. Which validity?", ["Construct", "External", "Internal", "Conclusion"], "metric fit"),
            ("Testing many metrics and reporting the best one threatens which validity?", ["Conclusion", "Construct", "External", "Internal"], "multiple comparisons"),
            ("A teammate offers private competition IQ captures. What do you do?", ["Decline; synthetic data only", "Use them quietly", "Use them with a footnote", "Use them if anonymised"], "guardrail"),
            ("How do honest threats listed early affect reviewer trust?", ["They raise trust in the remaining claims", "They sink the paper", "They are ignored", "They replace results"], "credibility"),
        ],
    },
    {
        "week": 10,
        "title": "Research capstone — traced figures, no submission claim",
        "lab_id": "lab_sga_research_capstone",
        "worked_example": "labs_passed=9; figure topk_vs_codebook carries config_sha256 and seed 20261102; submitted_claim=false; evidence_class=SYNTHETIC_SIM",
        "lesson": (
            "SGA-1A10 assembles the packet that cohorts on different campuses exchange. It contains the week-one claim ledger, "
            "updated with what the term actually showed, and at least one figure. Every figure carries the config digest and seed "
            "from its manifest, so a reader in Nubuke can regenerate the Gary figure without emailing anyone. The packet names "
            "its evidence class, which for this course is SYNTHETIC_SIM end to end, and repeats the week-eight gap in plain words. "
            "It also states what it is not: submitted_claim stays false, because drafting a figure for the research spine is not "
            "the same as submitting a paper, and only the program owner decides when a manuscript goes out. Mentors review the "
            "packet against six or more passed labs, check that no instructor answer key leaked into the learner folder, and "
            "rerun one figure from its manifest in front of the apprentice. A packet that survives that rerun is a real research "
            "artifact at apprentice scale. It is not a publication, a credential, or evidence of deployment, and the closing slide says so."
        ),
        "assignment": "Submit lab_sga_research_capstone JSON for SGA-1A10: labs_passed, traced figures, submitted_claim false, evidence_class, no_key_leak.",
        "quiz": [
            ("What must every capstone figure carry?", ["Its config digest and seed", "A university logo", "A screenshot of the terminal", "The mentor's signature only"], "traceable figure"),
            ("Why is submitted_claim false in the capstone?", ["Drafting a figure is not submitting a paper", "Papers are forbidden", "The simulator cannot export", "Mentors submit automatically"], "owner decides submission"),
            ("What do mentors rerun during review?", ["One figure from its manifest", "Every seed ever tried", "The quiz", "Nothing"], "live reproduction"),
            ("What evidence class does the capstone carry end to end?", ["SYNTHETIC_SIM", "MEASURED", "CITED_SPEC only", "PRIVATE_IQ"], "course is synthetic"),
            ("Which leak does review explicitly check for?", ["Instructor answer keys in the learner folder", "Config digests", "Seeds", "Figure titles"], "no key leak"),
            ("A packet survives the rerun. What is it?", ["An apprentice-scale research artifact, not a publication", "A peer-reviewed paper", "A deployment certificate", "A field trial"], "scoped outcome"),
        ],
    },
]

MID = [
    ("An apprentice reports 'GEO delay is fine for gaming' with no delay figure. Which week-one ledger fix applies?", ["Add a row with its evidence class or mark it OPEN", "Delete the sentence silently", "Label it MEASURED", "Add an affiliation"], "ledger every claim"),
    ("A cited 3GPP delay value appears without a source_id. What is wrong?", ["CITED_SPEC rows must name the source", "Nothing; specs are obvious", "It must be MEASURED instead", "It needs a seed"], "name the spec"),
    ("Your config file has a trailing timestamp line. What reproducibility risk does that create?", ["Every run changes the digest and possibly the output", "None", "It speeds reruns", "It pins the seed"], "nondeterministic config"),
    ("A teammate's figure has a seed but no config digest. Can another campus regenerate it?", ["Not reliably; the config used is unknown", "Yes, the seed is enough", "Yes, if the figure looks right", "Only on Linux"], "seed and digest both"),
    ("A satellite sits at 1,200 km nadir. Approximately what is its one-way delay?", ["About 4.0 ms", "About 2.0 ms", "About 40 ms", "About 0.4 ms"], "1200/c"),
    ("Why do GEO links feel sluggish even with high bandwidth?", ["Round trip near 240 ms dominates interaction", "GEO satellites are slower", "Bandwidth is shared", "Doppler is large"], "latency, not throughput"),
    ("At low elevation, how does slant range compare with altitude?", ["It can be several times larger", "It is always equal", "It is always smaller", "It is undefined"], "slant > nadir"),
    ("Doubling the carrier from 2 GHz to 4 GHz does what to the LEO Doppler bound?", ["Doubles it", "Halves it", "Leaves it unchanged", "Squares it"], "linear in f_c"),
    ("Raising a LEO orbit from 600 km to 1,200 km does what to circular orbital speed?", ["Lowers it slightly", "Raises it sharply", "Leaves it unchanged", "Doubles it"], "v ∝ 1/sqrt(r)"),
    ("Why would uncompensated 50 kHz Doppler harm a 15 kHz-spaced OFDM signal?", ["Subcarriers shift into their neighbours", "Power doubles", "The cyclic prefix grows", "Nothing happens"], "inter-carrier interference"),
    ("Which of these is a design margin rather than a measurement?", ["The (v/c)·f_c Doppler bound", "A logged field RSRP", "A bench spectrum capture", "A drive-test trace"], "bound vs data"),
    ("A model's top-1 is 0.40 and top-5 is 0.95 on a 64-beam codebook. What deployment fits?", ["Rank with the model, sweep five beams", "Trust top-1 alone", "Sweep all 64 beams", "Drop the codebook"], "rank and refine"),
    ("A test set of 8 samples gives top-1 = 0.5. What caution applies?", ["Eight samples give a very coarse estimate", "The model is perfect", "The result is measured", "Top-1 cannot be computed"], "tiny n"),
    ("Why might top-k reward a model that is useless in the field?", ["It ignores how much SNR the chosen beam loses", "It counts too many samples", "It requires labels", "It uses seeds"], "metric gap"),
    ("Which side information might a beam-selection model use?", ["User position or a coarse channel estimate", "The user's name", "Billing records", "Ambient temperature only"], "inputs"),
    ("An apprentice uses a different random seed for baseline and model each run. What is lost?", ["The pairing that cancels per-seed difficulty", "Nothing", "The codebook", "The digest"], "unpaired design"),
    ("Five paired differences have sd 0.03. Using t = 2.776, what is the 95% half-width?", ["About 0.037", "About 0.026", "About 0.083", "About 0.013"], "2.776·0.03/√5"),
    ("Replacing t = 2.776 with z = 1.96 for n = 5 has what effect?", ["The interval becomes too narrow", "The interval becomes too wide", "No effect", "The mean changes"], "overconfident"),
    ("Which statement is supported by a CI of [0.0137, 0.0663] on one synthetic scenario?", ["The model beat the baseline on that scenario", "The model wins on every scenario", "The gain is exactly 4%", "The model is calibrated"], "scoped claim"),
    ("An apprentice reruns seeds until the interval excludes zero. What validity does that break?", ["Conclusion validity", "Construct validity", "External validity", "None"], "p-hacking"),
]

FINAL = [
    ("A beam-tuning model must react every 50 ms. Which component hosts it?", ["Near-real-time RIC xApp", "Non-real-time RIC rApp", "DU real-time scheduler", "Core network UPF"], "10 ms–1 s"),
    ("An energy-saving policy updated hourly from KPIs runs where?", ["Non-real-time RIC rApp", "Near-real-time RIC xApp", "DU", "UE"], ">1 s"),
    ("Which interface would an rApp's guidance travel over to reach an xApp?", ["A1", "E2", "F1-U", "Uu"], "A1 policy"),
    ("A proposal trains a neural network inside the per-slot scheduler loop. How should a reviewer respond?", ["Reject the placement; training belongs in the non-RT loop", "Approve it as faster", "Move it to the UE", "Ignore loop timing"], "loop placement"),
    ("O-RAN documents are used in this course how?", ["For topic labels and architecture vocabulary only", "As exam answer sources", "As a certification", "As measured data"], "PUBLIC_REFERENCE_ONLY"),
    ("Twin and reference sim disagree by RMSE 0.4 dB. What may the poster claim?", ["Two models agree closely; calibration remains open", "The twin is calibrated", "The twin matches the field", "Measurements are unnecessary"], "agreement ≠ calibration"),
    ("Which single change would allow calibrated_claim to become true?", ["Comparing the twin with real site measurements", "Lowering RMSE against the sim", "Adding more seeds", "Renaming the status"], "field data"),
    ("A twin uses an optimistic clutter model shared with the reference simulator. What risk follows?", ["Both agree while both miss reality", "RMSE increases", "Doppler doubles", "Seeds diverge"], "shared bias"),
    ("Errors of 0, 0, 0 and 4 dB give what RMSE?", ["2 dB", "1 dB", "4 dB", "0 dB"], "sqrt(16/4)"),
    ("Why does the research spine keep Paper I's calibration gap visible?", ["So the next cohort knows which measurements to collect", "To lower expectations", "Because it is required by 3GPP", "To delay publication"], "actionable gap"),
    ("Two training positions also appear in the test set. Which validity threat is this?", ["Internal (data leak)", "External", "Construct", "None"], "leak"),
    ("Results from a LEO S-band scenario are presented as valid for urban mmWave. Which threat?", ["External validity", "Internal validity", "Construct validity", "Reproducibility"], "transfer"),
    ("An apprentice optimises top-1 accuracy while the operator cares about throughput. Which threat?", ["Construct validity", "Conclusion validity", "Internal validity", "External validity"], "metric mismatch"),
    ("Which guardrail forbids using captured signals from a private competition?", ["No private competition IQ", "Synthetic data only applies to figures", "No affiliation claims", "Seeds must be pinned"], "IQ guardrail"),
    ("A slide says 'in partnership with a national lab' with no agreement in place. Which rule is broken?", ["No affiliation claims", "Reproducibility", "Construct validity", "Paired design"], "affiliation"),
    ("Which capstone element lets another campus regenerate a figure without contacting you?", ["Config digest and seed on the figure", "A high-resolution PNG", "The mentor's email", "A video walkthrough"], "manifest"),
    ("Why is a capstone packet not a publication?", ["It has not been submitted or peer reviewed", "It lacks figures", "It uses Python", "It has a seed"], "scope"),
    ("Who decides when a manuscript from the research spine is submitted?", ["The program owner", "Any apprentice", "The simulator", "The mentor alone, silently"], "owner decision"),
    ("During review a mentor's rerun of one figure gives a different curve. What follows?", ["The figure is removed until its manifest reproduces", "Keep the prettier curve", "Average the two", "Change the seed quietly"], "reproduce or remove"),
    ("Which artifact must never appear in the learner packet?", ["Instructor answer keys", "Config digests", "Claim ledger", "Validity threats"], "key hygiene"),
    ("A 7GC cohort in Geelong wants to reuse Gary's beam figure in a port scenario. What should the ledger say?", ["The figure is SYNTHETIC_SIM for its own scenario; port transfer is untested", "It is MEASURED for ports", "It applies everywhere", "It needs no ledger row"], "scoped reuse"),
    ("Delay at 600 km nadir is 2.0 ms; a user at 20° elevation sees a longer delay. Why?", ["Slant range is longer than altitude", "Light slows at low elevation", "The satellite moves away faster", "Doppler adds delay"], "geometry"),
    ("Which pair of results would justify 'the model reduces sweep cost on this scenario'?", ["High top-3 accuracy and a paired CI excluding zero", "One lucky seed", "A calibrated twin alone", "An affiliation"], "evidence pairing"),
    ("What is the apprenticeship's final claim boundary?", ["Synthetic, reproducible, apprentice-scale research — not deployment or credential", "Field-validated 6G deployment", "Peer-reviewed publication", "Vendor certification"], "boundary"),
]


def _weeks() -> list[dict]:
    out = []
    for spec in WEEKS:
        n = spec["week"]
        out.append({
            "week": n,
            "title": spec["title"],
            "lesson": spec["lesson"],
            "worked_example": spec["worked_example"],
            "assignment": spec["assignment"],
            "lab_id": spec["lab_id"],
            "quiz": [_q(f"sga-w{n}-{i}", stem, choices, why) for i, (stem, choices, why) in enumerate(spec["quiz"], start=1)],
        })
    return out


def course() -> dict:
    return {
        "course_id": COURSE_ID,
        "title": "7GC AI-RAN Research Apprenticeship — Research Bench",
        "track_ids": [COURSE_ID],
        "academy_id": "ACADEMY_SOFTWARE",
        "kinesthetic_hook": (
            "Ten Research Bench weeks: claim ledger → reproducible manifest → NTN delay → LEO Doppler → beam top-k → "
            "paired interval → O-RAN loops → twin gap → validity threats → traced capstone. Synthetic and cited evidence only."
        ),
        "syllabus_hook": (
            "SEVEN_GC_APPRENTICESHIP COURSE_DIGITAL_RC: research-method apprenticeship over the 7GC AI-RAN spine — claim "
            "ledgers, reproducibility, NTN timing and Doppler, beam-selection metrics, paired statistics, O-RAN control-loop "
            "placement, digital-twin calibration honesty, and validity threats. Advanced overlay on ACADEMY_SOFTWARE; "
            "complements WIRELESS_6G and AI_ML_EDGE without replacing them. Not student/teacher E6; no paper submission."
        ),
        "career": {
            "roles": ["research_apprentice", "ran_ml_research_assistant", "reproducibility_reviewer_junior"],
            "nice_categories": ["analyze", "investigate"],
            "certs_aligned_not_granted": [
                "3GPP TR 38.811 / TR 38.901 topic labels (PUBLIC_REFERENCE_ONLY)",
                "O-RAN architecture vocabulary (PUBLIC_REFERENCE_ONLY; not an O-RAN certification)",
            ],
        },
        "ai_use_policy": {
            "modes": ["EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME", "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE"],
            "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
            "default_weekly": "AI_DISCLOSED",
            "no_ai_weeks": [4, 9],
        },
        "weeks": _weeks(),
    }


def exams() -> dict:
    mid = [_q(f"sga-mid-{i:02d}", s, c, w) for i, (s, c, w) in enumerate(MID, start=1)]
    final = [_q(f"sga-fin-{i:02d}", s, c, w) for i, (s, c, w) in enumerate(FINAL, start=1)]
    if len(mid) != 20 or len(final) != 24:
        raise SystemExit(f"exam sizes mid={len(mid)} final={len(final)}")
    return {"offset": 7, "mid": mid, "final": final}


def _write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    BATCH.mkdir(parents=True, exist_ok=True)
    _write_json(BATCH / "courses_data.json", {COURSE_ID: course()})
    _write_json(BATCH / "exams_data.json", {COURSE_ID: exams()})
    print("Wrote batch008 course + exam data under", BATCH)


if __name__ == "__main__":
    main()
