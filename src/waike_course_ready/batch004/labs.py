"""Runnable labs for WAIKE-COURSE-READY-004."""
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
