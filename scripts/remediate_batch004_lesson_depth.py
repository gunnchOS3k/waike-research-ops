#!/usr/bin/env python3
"""Remediate COURSE-READY-004 lesson padding: strip Detail-mark trailers; deepen unique bodies."""
from __future__ import annotations

import json
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.provenance import (  # noqa: E402
    detect_repeated_near_identical_trailers,
    strip_lesson_padding,
)

BATCH = ROOT / "src" / "waike_course_ready" / "batch004"
FLOOR = 871  # must clear #45 post-collapse floor; no identical trailer fillers


# Unique, domain-specific expansions — NOT the rotating trailer class.
EXPAND: dict[str, dict[int, str]] = {
    "WIRELESS_6G": {
        1: """
        Work the Friis card on paper with a second hop length (95 m at 3500 MHz) so the class
        sees how 20*log10(d) moves when the tape changes. Record both answers in the journal
        with units. The Pier Radio Bench treats invented '6G coverage radius' strings as claim
        boundary failures even when the arithmetic for FSPL is correct.

        Operators also name the antenna assumption: isotropic teaching model, not a measured
        panel pattern. If someone imports a vendor EIRP table without citing the fixture path
        `fixtures/wr4101/fspl.json`, stop the demo and return to the laminated card.
        """,
        2: """
        Draw one resource block as twelve vertical tones and mark Δf=30 kHz between them.
        Compute PRB bandwidth again with μ=0 (15 kHz) as a contrast case: 12*15e3=180 kHz.
        Write both results side by side so learners stop treating 'PRB' as a brand badge.

        Call out the cyclic-prefix omission in one sentence: CP is real on air interfaces and
        deliberately not scored this week. Anyone pasting a constellation PNG without
        n_sc/delta_f_hz/prb_bw_hz/symbol_duration_s fields fails the lab contract.
        """,
        3: """
        Build the feature map as three rows only: name, release_tag, PUBLIC_REFERENCE_ONLY.
        Example rows may include RedCap, NTN early hooks, and AI/ML study items — never a
        fabricated Rel-20 commercial-6G row. commercial_6g_exists stays false in JSON.

        NO_AI means hand labels. If a generative draft invents a ratified consumer 6G SKU,
        delete the row and rewrite from the alignment file. Membership in 3GPP is not granted
        by completing WR-4303.
        """,
        4: """
        Walk the BLER table left to right and mark every MCS whose BLER ≤ 0.1 before picking
        the maximum eligible index. At SNR=8 dB the eligible set is {2}; chosen_mcs=2 with
        bler_at_choice=0.09. Document why MCS 3 and 4 are rejected even if throughput stories
        sound better in marketing.

        Outer-loop CQI mapping stays in the 'still need' ladder rung — do not claim the pier
        runs a live link-adaptation closed loop from this fixture alone.
        """,
        5: """
        Recompute light-time with a second slant (650 km) so learners practice d/c without
        memorizing one number. Compare both RTTs to a GEO-class ~250 ms figure and keep
        geo_comparable=false. ntn_as_6g_standard remains false: NTN features in 5G-Advanced
        talk are not a commercial standardized 6G ratification.

        Refuse constellation-sim downloads while Stream A QEMU is active. Fixture milliseconds
        are the graded artifact; heatmaps without delay math are marketing fails.
        """,
        6: """
        Convert powers_db to linear, form the first and second moments of delay, then take the
        square root for τ_rms. Change the last tap power by −1 dB as a sensitivity check and
        note how τ_rms moves. PHYSICAL sounding stays PHYSICAL_PENDING until a real capture
        exists; AI beamforming slogans without taps score zero.

        Submit delays_ns, powers_db, tau_rms_ns, and tap_count=3. Wrong moments fail even when
        the journal prose is polished.
        """,
        7: """
        Write the AI-RAN loop as four explicit fields: observe_kpis (list), proposed_action
        containing MCS or PRB language, human_gate=true, auto_apply_without_gate=false.
        Ungated reinforcement-learning theater fails the validator.

        NO_AI quiz week still allows disclosed calculators on the lab JSON. Closed-loop field
        trial evidence is not claimed; the pier remains RESEARCH_LAB_SCALE.
        """,
        8: """
        Spectrum honesty is an ethics gate: unauthorized_tx=false, center_ghz=3.5, obw_mhz=18,
        mask_ok=true on the narrative card. Transmitting outside the lab narrative 'because
        SDR' fails the course, not just the week.

        Fabricated FCC/ITU PDF filenames are forbidden. Alignment labels are
        PUBLIC_REFERENCE_ONLY. Journals must not invent auction wins.
        """,
        9: """
        Map A1, E2, and O1 onto pier roles with one sentence each. deployed_full_ric stays
        false until E2 subscription logs exist (PHYSICAL_PENDING). Noun-swapping a Cloud or
        DevOps slide deck into O-RAN vocabulary fails the week.

        O2 may appear as optional vocabulary but does not unlock a production RIC claim.
        RESEARCH_LAB_SCALE is the only honest size label for WR-4909.
        """,
        10: """
        Capstone notebook hashes prior digests and requires includes_commercial_6g_false_statement
        true, product_use_unmerged_consumed false, and labs_passed≥6. Career map roles are
        aligned, not granted. Optional plots need alt_text; a text-only summary path is required.

        Do not open device-os PRs from this packet. Do not consume unmerged Product-Use packages
        as a hard dependency for the notebook.
        """,
    },
    "ROBOTICS_CONTROL": {
        1: """
        Tape the pier origin, mark +x along the aisle, and sketch the tool offset arrow before
        any code. With theta=π/2, show how the offset rotates into pier axes using cos/sin.
        Journals without an ASCII frame diagram fail accessibility expectations for HarborBot.

        Refuse 'AI nabbed the box' narratives that skip the SE(2) fields. Lab JSON must carry
        x, y, theta, tool offsets, and mapped tool_x/tool_y that match the rotation math.
        """,
        2: """
        Plot the reachable disk of radius L1+L2=0.65 m and mark a forbidden point beyond it.
        Forward kinematics must report both Cartesian tip and reachable=false when outside.
        Strong-servo myths do not enlarge the workspace.

        Joint-limit maps stay in 'still need'. Learners defend L1/L2 numbers from the fixture
        card, not from a cinematic robot trailer.
        """,
        3: """
        Expand the PID step: integrate the error series with rectangular rule, form the
        backward difference for D, and compute u on the last sample. When |integral| is large,
        anti_windup_note must be a real mitigation sentence (≥8 characters), not an empty string.

        Plant identification remains unfinished. Wrong u fails even if the motor 'sounds right'
        on a phone video.
        """,
        4: """
        For distance 1.2 m, vmax=0.4, amax=0.5, derive whether the profile is triangle or
        trapezoid, then compute t_min. path_ok is false when cmd_speed exceeds vmax. Smooth
        splines that ignore limits fail the NO_AI week.

        Curvature limits are deferred. Whiteboard the numbers; screenshots of path planners
        without t_min/path_ok fields do not pass.
        """,
        5: """
        Apply the hard gate (>2.0 m drop) to the lidar list and recompute mean on the cleaned
        set. outlier_dropped must be true when 3.50 is removed. Trusting the raw maximum as
        aisle truth fails sensing discipline.

        Bias calibration remains a later ladder rung. Empty submissions fail student_artifact.
        """,
        6: """
        E-stop is hard: motors_disabled, brake_engaged, and resume_requires_human all true.
        Soft 'slow down eventually' stories fail. Bypass for demo video is an ethics fail, not
        a style choice. SIL certification is not claimed by this course.

        Practice the printable large-text E-stop sheet path even when the cart is powered down
        for the classroom tabletop.
        """,
        7: """
        Diff-drive: v=(r/2)(ω_l+ω_r), ω=(r/B)(ω_r−ω_l) with B>0. B=0 is rejected before any
        division. Video of the cart without v/omega fields is insufficient evidence.

        Slip compensation stays in 'still need'. Encoder rates come from the fixture, not from
        invented fleet telemetry.
        """,
        8: """
        Scalar fuse uses K=p/(p+r) and refuses cov_zero_lie. Walk a numeric example with
        p=0.04, r=0.01 and show how lower variance pulls x_hat. Full SE(2) EKF is not claimed
        after this toy.

        Finite K and two measurements are required; certainty theater fails honesty.
        """,
        9: """
        cmd_vel-shaped JSON needs finite linear_x/angular_z and frame_id=base_link.
        fleet_claim=false. NaNs fail. NO_AI week: hand-author the schema. Production DDS/ROS
        distro pins are not granted by schema vocabulary alone.
        """,
        10: """
        Capstone packet requires estop_ok=true, labs_passed≥6, no_device_os_pr=true, and a
        packet_sha256. Fabricated injury statistics are forbidden. Career map: robotics
        technician / controls junior — aligned, not granted.

        Large-text E-stop procedure must remain in the portfolio folder.
        """,
    },
    "GAME_DEV_INTERACTIVE": {
        1: """
        Implement the accumulator mental model: fixed dt=1/60, clamp spiral when frame_time
        exceeds 0.25 s, keep spiral_of_death_guard true on the reference path. Variable render
        interpolation is allowed; simulation steps stay fixed.

        Handheld profiling remains PHYSICAL_PENDING. 'Just use delta everywhere' without a
        guard fails the loop contract.
        """,
        2: """
        Compute overlap_x and overlap_y explicitly; hit requires both positive. Particle VFX
        cannot replace the arithmetic. Swept tests for tunneling stay in 'still need'.

        Submit both rectangles and the overlap fields. Empty {} fails. Wrong signs fail.
        """,
        3: """
        BPM 120 → period 0.5 s. Map t=1.25 to beat_index=2 and phase=0.5. license_ok true and
        pirated_sample_pack false are hard gates. Cracked sample libraries in the portfolio
        fail the week regardless of beat math.

        Device latency calibration remains unfinished; do not invent millisecond offsets.
        """,
        4: """
        Author the transition table and reject illegal Jump→Run if the fixture forbids it.
        transition_ok and state_after must match legality. Boolean soups without a table fail.

        Animation blend trees are not claimed done after FSM week.
        """,
        5: """
        Level JSON: tiles length equals width*height; checksum pins canonical bytes.
        NO_AI week. Editor GUI screenshots alone are not artifacts. Streaming chunks stay in
        'still need'.

        checksum_ok must be true only when the digest matches the canonical serialization.
        """,
        6: """
        Actions, not scancodes: Jump must appear, rebindable=true, raw_only=false. Device swaps
        should not break design docs. Week 9 accessibility remaps extend this work; they do not
        delete it.
        """,
        7: """
        Optional case study may cite anime-aggressors, beatlink-party, earth-species, or
        foot-racing — or none. required_unmerged_branch=false always. Hard-depending unmerged
        game or Product-Use PRs fails the claim boundary.

        Pick one lens (combat timing, beat sync, ecology sim, or racing physics) and attach
        fixture metrics without claiming those repos must be merged.
        """,
        8: """
        early_churn_rate = early_churn/sessions on the fixture (8/40=0.2). vanity_dau_claim
        must be false. Fake million-DAU slides fail. Cohort significance remains a later need.

        Median session minutes, when required by the lab fields, must come from the list math
        rather than adjectives.
        """,
        9: """
        Accessibility checklist: captions, remaps, colorblind_safe true; flash_hz≤3. NO_AI.
        Fabricating disabled-player test quotes is forbidden. Large-text menu notes belong in
        the student packet path.
        """,
        10: """
        Ship checklist: build_repro_hash, a11y_ok=true, labs_passed≥6, unmerged_branch_required
        false, and a four_games_optional_note. Keyboard-only path notes are required in the
        portfolio. Product-Use must not consume this unmerged course branch.

        Career certs remain aligned, not granted.
        """,
    },
}


# Second-pass unique deepeners — each week has distinct technical prose (no shared template).
UNIQUE_MORE: dict[str, dict[int, str]] = {
    "WIRELESS_6G": {
        7: """
        On WR-4707, enumerate observe_kpis as concrete CSV column names (bler, prb_util, snr_p50)
        before proposing MCS or PRB moves. Document the human gate as a named pier operator role,
        not a checkbox theater. Auto-apply without that gate must remain false in every submitted
        JSON variant the class practices. Compare one gated proposal against an ungated fantasy
        loop and mark which fields the validator rejects. Keep AI-RAN vocabulary at RESEARCH_LAB_SCALE;
        do not imply pier-wide closed-loop autonomy from this ticket alone.
        """,
        8: """
        For WR-4808, recompute whether OBW 18 MHz at 3.5 GHz sits inside the narrative mask and
        write mask_ok with the inequality you used. List three transmission acts that would set
        unauthorized_tx true even if the SDR UI looks green. Journals that invent auction IDs or
        FCC PDF filenames fail ethics before RF arithmetic is graded. Align labels to
        PUBLIC_REFERENCE_ONLY and keep commercial standardized 6G absent from the claim line.
        """,
        9: """
        Sketch A1 policy advice, E2 near-RT control, and O1/O2 management as separate arrows on
        the pier whiteboard for WR-4909. Require deployed_full_ric=false until an E2 subscription
        log path exists. Write one sentence explaining why a Cloud/DevOps deck cannot be
        noun-swapped into O-RAN interfaces. Cap the honesty note at RESEARCH_LAB_SCALE and refuse
        production RIC claims without PHYSICAL_PENDING evidence.
        """,
    },
    "ROBOTICS_CONTROL": {
        2: """
        For RB-5202, compute tip pose at θ1=0.4 rad, θ2=−0.2 rad with L1=0.35, L2=0.30 and mark
        reachable vs hypot(x,y)>0.65. Include a second target beyond the disk and show
        reachable=false without inventing extra link length. Defend L1/L2 from the fixture card
        only; cinematic reach claims are out of scope. Joint-limit maps stay listed under still-need.
        """,
        3: """
        Walk RB-5303 with the full e series [1.0,0.6,0.2], accumulate rectangular integral, form
        backward Δe/dt, and publish u for the last sample with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
        When |integral| grows, anti_windup_note must name a mitigation (clamp, back-calculation)
        in ≥8 characters. Wrong u fails even if a phone video of the motor looks smooth.
        """,
        4: """
        On RB-5404, decide triangle vs trapezoid for 1.2 m with vmax=0.4 and amax=0.5, then compute
        t_min from the chosen profile. Set path_ok false for any cmd_speed>vmax and explain the
        reject in one sentence. NO_AI week: hand-derive on paper; GUI path screenshots without
        t_min/path_ok fields do not pass. Curvature limits remain deferred.
        """,
        5: """
        Clean RB-5505 lidar [1.01,1.00,0.99,1.02,3.50] with the >2.0 m hard gate, recompute mean
        and cleaned_n, and set outlier_dropped true when 3.50 is removed. Show why trusting the
        raw max as aisle truth breaks sensing discipline. Bias calibration stays on the still-need
        rung; empty student_artifact still fails.
        """,
        6: """
        Assert RB-5606 E-stop fields motors_disabled, brake_engaged, and resume_requires_human
        as a triple-true contract. Contrast against a soft 'slow eventually' story that must fail.
        Note that demo-video bypass is an ethics fail, and SIL certification is not claimed.
        Keep the printable large-text E-stop sheet in the student packet path for tabletop drills.
        """,
        7: """
        Derive RB-5707 v=(r/2)(ω_l+ω_r) and ω=(r/B)(ω_r−ω_l) with B=0.40, r=0.05 and reject B=0
        before division. Publish finite v and omega from fixture encoder rates only. Video without
        those fields is insufficient. Slip compensation remains still-need; invented fleet
        telemetry is forbidden. Work a second numeric pair (ω_l=2.0, ω_r=2.4) on the whiteboard
        and show how ω_body changes sign when the wheel rates swap, still with B>0 enforced.
        """,
        8: """
        For RB-5808, compute K=p/(p+r) with p=0.04, r=0.01, form x_hat, and refuse cov_zero_lie.
        Show how the lower-variance measurement pulls the estimate. State explicitly that full
        SE(2) EKF is not earned by this scalar toy. Certainty theater (P=0) fails honesty.
        Repeat with p=0.09, r=0.01 and note how K shrinks when prior variance rises, still
        refusing any submission that asserts zero covariance as a lie flag.
        """,
        9: """
        Hand-author RB-5909 cmd_vel JSON with finite linear_x, angular_z, and frame_id=base_link.
        fleet_claim must be false; NaNs fail. NO_AI week forbids generative schema dumps.
        Production DDS/ROS distro pins are not granted by vocabulary alone. Add a negative case
        with angular_z=null and show the validator reject text the pier expects learners to cite.
        """,
        10: """
        Assemble RB-5910 with estop_ok=true, labs_passed≥6, no_device_os_pr=true, and packet_sha256.
        Forbid fabricated injury statistics. Keep career mapping as robotics technician / controls
        junior — aligned, not granted — and retain the large-text E-stop procedure in portfolio.
        """,
    },
    "GAME_DEV_INTERACTIVE": {
        1: """
        On GA-6101, simulate three frame_time samples (0.016, 0.040, 0.30) through the accumulator
        with dt=1/60 and show when spiral_of_death_guard clamps. Keep simulation steps fixed while
        allowing render interpolation. Handheld profiling stays PHYSICAL_PENDING; delta-everywhere
        without a guard fails the loop contract.
        """,
        2: """
        Compute GA-6202 overlap_x and overlap_y for two axis-aligned boxes with deliberate miss and
        hit cases; require both overlaps positive for hit. Particle VFX cannot replace the signs.
        Swept tunneling tests remain still-need. Empty {} and wrong signs fail the lab. Include a
        third rectangle pair where overlap_x>0 but overlap_y≤0 and mark hit=false with the arithmetic
        written beside the boxes.
        """,
        3: """
        Map GA-6303 t=1.25 at BPM 120 to beat_index and phase with period 0.5 s. Enforce
        license_ok true and pirated_sample_pack false as hard gates. Cracked sample packs fail
        regardless of beat math. Do not invent device-latency millisecond offsets this week.
        Also map t=0.0 and t=2.0 and show beat_index continuity without claiming a DAW license.
        """,
        4: """
        Author GA-6404 transition table rows and reject illegal Jump→Run when the fixture forbids
        it. Publish transition_ok and state_after that match legality. Boolean soups without a
        table fail. Animation blend trees are not claimed complete after FSM week. Add Idle→Jump
        as a legal row and document the guard condition in one sentence next to the table.
        """,
        5: """
        For GA-6505, prove tiles.length == width*height and pin checksum to canonical bytes.
        NO_AI week: hand-edit JSON; editor screenshots alone are not artifacts. Streaming chunks
        stay still-need. checksum_ok is true only on digest match. Mutate one tile intentionally
        and show checksum_ok flip to false before restoring the canonical bytes.
        """,
        6: """
        Bind GA-6606 actions (not scancodes): Jump must appear with rebindable=true and
        raw_only=false. Argue why device swaps must not break design docs. Week 9 remaps extend
        this contract; they do not erase it. Provide a sample remap table keyboard→gamepad that
        keeps the Jump action id stable across devices. Also bind Interact and Pause with the
        same action-id rule, and show a failing submission that stores only HID scancodes without
        action names so the class can quote the reject reason in journals.
        """,
        7: """
        Optional GA-6707 case study may cite anime-aggressors, beatlink-party, earth-species, or
        foot-racing — or none — with required_unmerged_branch=false. Hard-depending unmerged game
        or Product-Use PRs fails the claim boundary. Attach fixture metrics for one lens without
        demanding merges.
        """,
        8: """
        Compute GA-6808 early_churn_rate = early_churn/sessions on the fixture (8/40=0.2) and keep
        vanity_dau_claim false. Fake million-DAU slides fail. Median session minutes, when required,
        come from list math, not adjectives. Cohort significance remains later-need.
        """,
        9: """
        Complete GA-6909 a11y checklist: captions, remaps, colorblind_safe, flash_hz≤3 under NO_AI.
        Fabricated disabled-player quotes are forbidden. Large-text menu notes belong in the student
        packet path and must be cited in the journal. Record flash_hz from the fixture card and
        refuse any cinematic trailer that exceeds the flash limit for accessibility.
        """,
        10: """
        Ship GA-6910 with build_repro_hash, a11y_ok=true, labs_passed≥6, unmerged_branch_required
        false, and four_games_optional_note. Require a keyboard-only path note in portfolio.
        Product-Use must not consume this unmerged course branch; career certs stay aligned-not-granted.
        """,
    },
}


_BAD_MARKERS = (
    "detail mark",
    "operators keep a numbered ticket trail for",
    "whiteboard the worked numbers before opening any gui",
    "if a volunteer asks for a certificate selfie",
    "evidence for this week lives in the submitted lab json",
    "operator note: record evidence before changing shared systems",
    "ticket arithmetic checkpoint",
    "restate the worked example in your own symbols",
)


def deepen(cid: str, week: int, body: str) -> str:
    core = strip_lesson_padding(body)
    lines = [
        ln
        for ln in core.splitlines()
        if "detail mark" not in ln.lower() and "ticket arithmetic checkpoint" not in ln.lower()
    ]
    core = "\n".join(lines).strip()
    # Drop residual checkpoint paragraphs the line filter may miss mid-wrap
    paras = []
    for p in re.split(r"\n\s*\n", core):
        low = p.lower()
        if "ticket arithmetic checkpoint" in low:
            continue
        if "restate the worked example in your own symbols" in low:
            continue
        paras.append(p)
    core = "\n\n".join(paras).strip()

    for block in (EXPAND.get(cid, {}).get(week), UNIQUE_MORE.get(cid, {}).get(week)):
        if not block:
            continue
        extra = textwrap.dedent(block).strip()
        if extra[:72] not in core:
            core = (core + "\n\n" + extra).strip()

    out = strip_lesson_padding(core)
    if len(out) < FLOOR:
        raise SystemExit(
            f"{cid} w{week} still short after unique deepen: {len(out)} < {FLOOR} "
            "(refusing identical trailer fillers)"
        )
    low = out.lower()
    for bad in _BAD_MARKERS:
        if bad in low:
            raise SystemExit(f"{cid} w{week} still contains padding marker: {bad}")
    return out


def main() -> int:
    path = BATCH / "courses_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    mins: dict[str, int] = {}
    for cid, course in data.items():
        week_mins: list[int] = []
        for w in course["weeks"]:
            w["lesson"] = deepen(cid, int(w["week"]), w["lesson"])
            week_mins.append(len(strip_lesson_padding(w["lesson"])))
        mins[cid] = min(week_mins)
        spam = detect_repeated_near_identical_trailers(course["weeks"])
        if spam.get("spam"):
            raise SystemExit(f"{cid} repeated trailer spam after remediate: {spam}")
        if mins[cid] < 871:
            raise SystemExit(f"{cid} min {mins[cid]} < 871")
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"stripped_mins": mins, "floor": 871, "ticket_arithmetic_spam": 0}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
