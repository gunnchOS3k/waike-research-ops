"""Runnable labs for batch008 — SEVEN_GC_APPRENTICESHIP (7GC AI-RAN Research Bench).

Every lab recomputes its answer from the submitted inputs; a memorized number
with altered inputs fails. All evidence is SYNTHETIC_SIM or CITED — no lab can
be passed by claiming measured field data, a paper submission, or affiliation.
"""
from __future__ import annotations

import hashlib
import math
from typing import Any

from waike_course_ready.batch007.labs import LabResult, _check, _require_student, _result

COURSE = "SEVEN_GC_APPRENTICESHIP"
B_SGA = (
    "SEVEN_GC_APPRENTICESHIP Research Bench. Synthetic simulation and cited specs only; "
    "no measured-field, paper-submission, or affiliation claims. Not student/teacher E6."
)

C_KM_S = 299_792.458
MU_EARTH_KM3_S2 = 398_600.4418
R_EARTH_KM = 6_371.0
EVIDENCE_CLASSES = {"SYNTHETIC_SIM", "CITED_SPEC", "MEASURED"}

BEAM_FIXTURE = {
    "true_beams": [3, 7, 1, 4, 4, 0, 6, 2],
    "ranked_predictions": [
        [3, 2, 5], [6, 7, 1], [1, 0, 2], [5, 6, 4],
        [4, 3, 5], [2, 1, 3], [6, 5, 7], [0, 1, 2],
    ],
}
PAIRED_FIXTURE = {
    "baseline": [0.61, 0.63, 0.60, 0.62, 0.64],
    "model": [0.66, 0.65, 0.67, 0.64, 0.68],
}
T_CRIT_95 = {2: 12.706, 3: 4.303, 4: 3.182, 5: 2.776, 6: 2.571, 7: 2.447, 8: 2.365, 9: 2.306, 10: 2.262}
TWIN_FIXTURE = {
    "twin_rsrp_dbm": [-95.0, -97.0, -99.0, -101.0],
    "reference_sim_rsrp_dbm": [-94.0, -98.0, -100.0, -103.0],
}


def _num(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _close(a: Any, b: float, tol: float) -> bool:
    x = _num(a)
    return x is not None and abs(x - b) <= tol


def lab_sga_claim_ledger(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_claim_ledger", COURSE, submission, ["claims", "affiliation_claim"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_claim_ledger", COURSE, checks, B_SGA)
    claims = data.get("claims") if isinstance(data.get("claims"), list) else []
    checks.append(_check("claims_present", len(claims) >= 3, f"claims={len(claims)}"))
    classes_ok = all(isinstance(c, dict) and c.get("evidence_class") in EVIDENCE_CLASSES for c in claims)
    checks.append(_check("evidence_class_labeled", bool(claims) and classes_ok, "each claim labels its evidence"))
    unbacked = [c for c in claims if isinstance(c, dict) and c.get("evidence_class") == "MEASURED" and not c.get("dataset_ref")]
    checks.append(_check("no_measured_without_dataset", not unbacked, f"measured_without_dataset={len(unbacked)}"))
    cited = [c for c in claims if isinstance(c, dict) and c.get("evidence_class") == "CITED_SPEC"]
    checks.append(_check("cited_specs_named", all(str(c.get("source_id") or "").strip() for c in cited), "CITED_SPEC needs source_id"))
    checks.append(_check("no_affiliation", data.get("affiliation_claim") is False, "affiliation_claim must be false"))
    return _result("lab_sga_claim_ledger", COURSE, checks, B_SGA)


def lab_sga_repro_manifest(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_repro_manifest", COURSE, submission,
        ["config_text", "config_sha256", "seed", "command", "rerun_metric_a", "rerun_metric_b"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_repro_manifest", COURSE, checks, B_SGA)
    digest = hashlib.sha256(str(data.get("config_text")).encode("utf-8")).hexdigest()
    checks.append(_check("config_digest_recomputed", str(data.get("config_sha256")).lower() == digest, "sha256(config_text)"))
    checks.append(_check("seed_pinned", isinstance(data.get("seed"), int), "integer seed"))
    checks.append(_check("command_recorded", len(str(data.get("command") or "")) >= 8, "exact command"))
    a, b = _num(data.get("rerun_metric_a")), _num(data.get("rerun_metric_b"))
    checks.append(_check("rerun_identical", a is not None and a == b, "same seed + config → same metric"))
    return _result("lab_sga_repro_manifest", COURSE, checks, B_SGA)


def lab_sga_ntn_delay(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_ntn_delay", COURSE, submission, ["altitude_km", "one_way_ms", "rtt_ms", "geometry"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_ntn_delay", COURSE, checks, B_SGA)
    alt = _num(data.get("altitude_km"))
    checks.append(_check("altitude_positive", alt is not None and alt > 0, "altitude_km > 0"))
    if alt is not None and alt > 0:
        one_way = alt / C_KM_S * 1000.0
        checks.append(_check("one_way_recomputed", _close(data.get("one_way_ms"), one_way, 0.01), f"expected {one_way:.3f} ms"))
        checks.append(_check("rtt_recomputed", _close(data.get("rtt_ms"), 2 * one_way, 0.02), f"expected {2 * one_way:.3f} ms"))
    checks.append(_check("nadir_stated", data.get("geometry") == "nadir", "slant range is longer than nadir"))
    return _result("lab_sga_ntn_delay", COURSE, checks, B_SGA)


def lab_sga_leo_doppler(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_leo_doppler", COURSE, submission,
        ["altitude_km", "carrier_ghz", "orbital_speed_km_s", "doppler_bound_khz", "bound_is_upper"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_leo_doppler", COURSE, checks, B_SGA)
    alt, fc = _num(data.get("altitude_km")), _num(data.get("carrier_ghz"))
    ok_in = alt is not None and alt > 0 and fc is not None and fc > 0
    checks.append(_check("inputs_positive", ok_in, "altitude and carrier > 0"))
    if ok_in:
        v = math.sqrt(MU_EARTH_KM3_S2 / (R_EARTH_KM + alt))
        bound_khz = v / C_KM_S * fc * 1e6
        checks.append(_check("orbital_speed_recomputed", _close(data.get("orbital_speed_km_s"), v, 0.01), f"expected {v:.3f} km/s"))
        checks.append(_check("doppler_bound_recomputed", _close(data.get("doppler_bound_khz"), bound_khz, 0.5), f"expected {bound_khz:.2f} kHz"))
    checks.append(_check("bound_not_measurement", data.get("bound_is_upper") is True, "v/c·f is an upper bound"))
    return _result("lab_sga_leo_doppler", COURSE, checks, B_SGA)


def _topk(k: int) -> float:
    hits = sum(1 for t, ranked in zip(BEAM_FIXTURE["true_beams"], BEAM_FIXTURE["ranked_predictions"]) if t in ranked[:k])
    return hits / len(BEAM_FIXTURE["true_beams"])


def lab_sga_beam_topk(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_beam_topk", COURSE, submission, ["top1", "top3", "n_samples", "dataset_class"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_beam_topk", COURSE, checks, B_SGA)
    checks.append(_check("n_matches_fixture", data.get("n_samples") == len(BEAM_FIXTURE["true_beams"]), "n=8"))
    checks.append(_check("top1_recomputed", _close(data.get("top1"), _topk(1), 1e-6), f"expected {_topk(1)}"))
    checks.append(_check("top3_recomputed", _close(data.get("top3"), _topk(3), 1e-6), f"expected {_topk(3)}"))
    checks.append(_check("synthetic_labeled", data.get("dataset_class") == "SYNTHETIC_SIM", "fixture is synthetic"))
    return _result("lab_sga_beam_topk", COURSE, checks, B_SGA)


def paired_interval(baseline: list[float], model: list[float]) -> tuple[float, float, float]:
    diffs = [m - b for b, m in zip(baseline, model)]
    n = len(diffs)
    mean = sum(diffs) / n
    sd = math.sqrt(sum((d - mean) ** 2 for d in diffs) / (n - 1))
    half = T_CRIT_95[n] * sd / math.sqrt(n)
    return mean, mean - half, mean + half


def lab_sga_paired_ci(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_paired_ci", COURSE, submission, ["mean_diff", "ci_low", "ci_high", "claims_improvement"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_paired_ci", COURSE, checks, B_SGA)
    mean, lo, hi = paired_interval(PAIRED_FIXTURE["baseline"], PAIRED_FIXTURE["model"])
    checks.append(_check("mean_recomputed", _close(data.get("mean_diff"), mean, 5e-4), f"expected {mean:.4f}"))
    checks.append(_check("ci_low_recomputed", _close(data.get("ci_low"), lo, 5e-4), f"expected {lo:.4f}"))
    checks.append(_check("ci_high_recomputed", _close(data.get("ci_high"), hi, 5e-4), f"expected {hi:.4f}"))
    checks.append(_check("claim_matches_interval", data.get("claims_improvement") is (lo > 0), "claim only if CI excludes 0"))
    return _result("lab_sga_paired_ci", COURSE, checks, B_SGA)


ORAN_LOOPS = {"real_time": (0.0, 10.0), "near_real_time": (10.0, 1000.0), "non_real_time": (1000.0, math.inf)}


def oran_loop_class(latency_ms: float) -> str:
    for name, (lo, hi) in ORAN_LOOPS.items():
        if lo <= latency_ms < hi:
            return name
    return "non_real_time"


def lab_sga_oran_loops(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_oran_loops", COURSE, submission, ["tasks", "a1_policy_target"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_oran_loops", COURSE, checks, B_SGA)
    tasks = data.get("tasks") if isinstance(data.get("tasks"), list) else []
    checks.append(_check("three_tasks", len(tasks) >= 3, f"tasks={len(tasks)}"))
    wrong = [t for t in tasks if not isinstance(t, dict) or _num(t.get("loop_ms")) is None
             or t.get("loop_class") != oran_loop_class(float(t["loop_ms"]))]
    checks.append(_check("loops_classified", bool(tasks) and not wrong, f"misclassified={len(wrong)}"))
    classes = {t.get("loop_class") for t in tasks if isinstance(t, dict)}
    checks.append(_check("covers_all_loops", classes >= set(ORAN_LOOPS), "one task per loop"))
    checks.append(_check("a1_targets_near_rt_ric", data.get("a1_policy_target") == "near_rt_ric", "A1: non-RT RIC → near-RT RIC"))
    return _result("lab_sga_oran_loops", COURSE, checks, B_SGA)


def twin_rmse() -> float:
    pairs = zip(TWIN_FIXTURE["twin_rsrp_dbm"], TWIN_FIXTURE["reference_sim_rsrp_dbm"])
    sq = [(a - b) ** 2 for a, b in pairs]
    return math.sqrt(sum(sq) / len(sq))


def lab_sga_twin_gap(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_twin_gap", COURSE, submission,
        ["rmse_db", "measured_samples", "calibration_status", "calibrated_claim"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_twin_gap", COURSE, checks, B_SGA)
    checks.append(_check("rmse_recomputed", _close(data.get("rmse_db"), twin_rmse(), 0.005), f"expected {twin_rmse():.4f} dB"))
    measured = data.get("measured_samples")
    checks.append(_check("measured_count_integer", isinstance(measured, int) and measured >= 0, "count of field samples"))
    if isinstance(measured, int) and measured == 0:
        checks.append(_check("status_uncalibrated", data.get("calibration_status") == "UNCALIBRATED_NO_MEASUREMENTS", "no field data"))
        checks.append(_check("no_calibrated_claim", data.get("calibrated_claim") is False, "twin vs sim is not calibration"))
    return _result("lab_sga_twin_gap", COURSE, checks, B_SGA)


VALIDITY_KINDS = ("internal", "external", "construct", "conclusion")


def lab_sga_validity(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_validity", COURSE, submission,
        ["threats", "synthetic_data_only", "private_iq_used", "affiliation_claim"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_validity", COURSE, checks, B_SGA)
    threats = data.get("threats") if isinstance(data.get("threats"), dict) else {}
    missing = [k for k in VALIDITY_KINDS if not (isinstance(threats.get(k), list) and threats[k])]
    checks.append(_check("four_validity_kinds", not missing, f"missing={missing}"))
    checks.append(_check("synthetic_only", data.get("synthetic_data_only") is True, "synthetic data only"))
    checks.append(_check("no_private_iq", data.get("private_iq_used") is False, "no private competition IQ"))
    checks.append(_check("no_affiliation", data.get("affiliation_claim") is False, "no affiliation claim"))
    return _result("lab_sga_validity", COURSE, checks, B_SGA)


def lab_sga_research_capstone(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sga_research_capstone", COURSE, submission,
        ["labs_passed", "figures", "submitted_claim", "evidence_class", "no_key_leak"], B_SGA,
    )
    if data is None:
        return _result("lab_sga_research_capstone", COURSE, checks, B_SGA)
    checks.append(_check("labs_passed", isinstance(data.get("labs_passed"), int) and data["labs_passed"] >= 6, "≥6 prior labs"))
    figures = data.get("figures") if isinstance(data.get("figures"), list) else []
    traced = all(isinstance(f, dict) and len(str(f.get("config_sha256") or "")) == 64 and f.get("seed") is not None for f in figures)
    checks.append(_check("figures_traced", bool(figures) and traced, "each figure has config digest + seed"))
    checks.append(_check("not_submitted", data.get("submitted_claim") is False, "no paper-submission claim"))
    checks.append(_check("evidence_synthetic", data.get("evidence_class") == "SYNTHETIC_SIM", "capstone evidence class"))
    checks.append(_check("no_key_leak", data.get("no_key_leak") is True, "instructor keys stay out"))
    return _result("lab_sga_research_capstone", COURSE, checks, B_SGA)


_CONFIG_TEXT = "scenario=leo600_sband\nseed=20261102\nbeams=8\nepochs=5\n"
_CONFIG_SHA = hashlib.sha256(_CONFIG_TEXT.encode("utf-8")).hexdigest()
_MEAN, _LO, _HI = paired_interval(PAIRED_FIXTURE["baseline"], PAIRED_FIXTURE["model"])
_V600 = math.sqrt(MU_EARTH_KM3_S2 / (R_EARTH_KM + 600.0))

LAB_ORDER_008 = [
    "lab_sga_claim_ledger", "lab_sga_repro_manifest", "lab_sga_ntn_delay", "lab_sga_leo_doppler",
    "lab_sga_beam_topk", "lab_sga_paired_ci", "lab_sga_oran_loops", "lab_sga_twin_gap",
    "lab_sga_validity", "lab_sga_research_capstone",
]

LABS_008 = {name: globals()[name] for name in LAB_ORDER_008}

COURSE_LABS_008 = {COURSE: list(LAB_ORDER_008)}

REFERENCE_008: dict[str, dict[str, Any]] = {
    "lab_sga_claim_ledger": {
        "claims": [
            {"text": "Top-3 beam accuracy rises with codebook prior", "evidence_class": "SYNTHETIC_SIM"},
            {"text": "LEO one-way nadir delay at 600 km is about 2 ms", "evidence_class": "CITED_SPEC", "source_id": "3GPP_TR_38_811_NTN"},
            {"text": "Field RSRP matches the twin", "evidence_class": "MEASURED", "dataset_ref": "none-yet", "status": "OPEN"},
        ],
        "affiliation_claim": False,
    },
    "lab_sga_repro_manifest": {
        "config_text": _CONFIG_TEXT, "config_sha256": _CONFIG_SHA, "seed": 20261102,
        "command": "python -m sim.run --config leo600.cfg --seed 20261102",
        "rerun_metric_a": 0.625, "rerun_metric_b": 0.625,
    },
    "lab_sga_ntn_delay": {
        "altitude_km": 600, "one_way_ms": round(600 / C_KM_S * 1000, 4),
        "rtt_ms": round(1200 / C_KM_S * 1000, 4), "geometry": "nadir",
    },
    "lab_sga_leo_doppler": {
        "altitude_km": 600, "carrier_ghz": 2.0, "orbital_speed_km_s": round(_V600, 4),
        "doppler_bound_khz": round(_V600 / C_KM_S * 2.0 * 1e6, 2), "bound_is_upper": True,
    },
    "lab_sga_beam_topk": {"top1": 0.5, "top3": 0.875, "n_samples": 8, "dataset_class": "SYNTHETIC_SIM"},
    "lab_sga_paired_ci": {
        "mean_diff": round(_MEAN, 4), "ci_low": round(_LO, 4), "ci_high": round(_HI, 4), "claims_improvement": True,
    },
    "lab_sga_oran_loops": {
        "tasks": [
            {"task": "HARQ retransmission scheduling", "loop_ms": 1, "loop_class": "real_time"},
            {"task": "xApp beam-pair handover tuning", "loop_ms": 100, "loop_class": "near_real_time"},
            {"task": "rApp energy-saving policy training", "loop_ms": 60000, "loop_class": "non_real_time"},
        ],
        "a1_policy_target": "near_rt_ric",
    },
    "lab_sga_twin_gap": {
        "rmse_db": round(twin_rmse(), 4), "measured_samples": 0,
        "calibration_status": "UNCALIBRATED_NO_MEASUREMENTS", "calibrated_claim": False,
    },
    "lab_sga_validity": {
        "threats": {
            "internal": ["seed sweep covers only 5 seeds"],
            "external": ["single synthetic scenario; no field site"],
            "construct": ["top-k accuracy ignores beam SNR loss"],
            "conclusion": ["n=5 paired runs; wide interval"],
        },
        "synthetic_data_only": True, "private_iq_used": False, "affiliation_claim": False,
    },
    "lab_sga_research_capstone": {
        "labs_passed": 9,
        "figures": [{"name": "topk_vs_codebook", "config_sha256": _CONFIG_SHA, "seed": 20261102}],
        "submitted_claim": False, "evidence_class": "SYNTHETIC_SIM", "no_key_leak": True,
    },
}

WRONG_008: dict[str, dict[str, Any]] = {
    "lab_sga_claim_ledger": {
        "claims": [{"text": "Field trial proves 40% gain", "evidence_class": "MEASURED"}], "affiliation_claim": True,
    },
    "lab_sga_repro_manifest": {
        "config_text": _CONFIG_TEXT, "config_sha256": "0" * 64, "seed": "random",
        "command": "run it", "rerun_metric_a": 0.625, "rerun_metric_b": 0.641,
    },
    "lab_sga_ntn_delay": {"altitude_km": 35786, "one_way_ms": 2.0, "rtt_ms": 4.0, "geometry": "slant"},
    "lab_sga_leo_doppler": {
        "altitude_km": 600, "carrier_ghz": 2.0, "orbital_speed_km_s": 7.9,
        "doppler_bound_khz": 5.0, "bound_is_upper": False,
    },
    "lab_sga_beam_topk": {"top1": 0.875, "top3": 1.0, "n_samples": 8, "dataset_class": "MEASURED"},
    "lab_sga_paired_ci": {"mean_diff": 0.04, "ci_low": 0.039, "ci_high": 0.041, "claims_improvement": False},
    "lab_sga_oran_loops": {
        "tasks": [
            {"task": "HARQ", "loop_ms": 1, "loop_class": "near_real_time"},
            {"task": "xApp", "loop_ms": 100, "loop_class": "non_real_time"},
            {"task": "rApp", "loop_ms": 60000, "loop_class": "real_time"},
        ],
        "a1_policy_target": "du",
    },
    "lab_sga_twin_gap": {
        "rmse_db": 0.0, "measured_samples": 0, "calibration_status": "CALIBRATED", "calibrated_claim": True,
    },
    "lab_sga_validity": {
        "threats": {"internal": ["none"]}, "synthetic_data_only": False,
        "private_iq_used": True, "affiliation_claim": True,
    },
    "lab_sga_research_capstone": {
        "labs_passed": 2, "figures": [{"name": "fig1"}], "submitted_claim": True,
        "evidence_class": "MEASURED", "no_key_leak": False,
    },
}

LAB_SPECS_008: dict[str, dict[str, Any]] = {
    "lab_sga_claim_ledger": {
        "title": "Claim ledger — label every claim's evidence class",
        "readme": "List at least three research claims. Label each SYNTHETIC_SIM, CITED_SPEC (with source_id), or MEASURED (with dataset_ref). affiliation_claim must be false.",
        "wrong_hint": "A MEASURED claim without dataset_ref, or affiliation_claim true, fails.",
    },
    "lab_sga_repro_manifest": {
        "title": "Reproducibility manifest — digest, seed, command, rerun",
        "readme": "Record config_text and its sha256, an integer seed, the exact command, and two reruns of the metric. The grader recomputes the digest.",
        "wrong_hint": "A digest that does not match config_text, a non-integer seed, or reruns that differ fail.",
    },
    "lab_sga_ntn_delay": {
        "title": "NTN propagation delay — nadir one-way and round trip",
        "readme": "For your chosen altitude_km compute one_way_ms = altitude / c and rtt_ms = 2 × one_way. State geometry = nadir.",
        "wrong_hint": "Reusing the LEO 600 km delay for a GEO altitude fails the recompute.",
    },
    "lab_sga_leo_doppler": {
        "title": "LEO Doppler upper bound from orbital speed",
        "readme": "Compute v = sqrt(μ/(R+h)) with μ = 398600.4418 km³/s², R = 6371 km, then the bound f_d ≤ (v/c)·f_c in kHz. bound_is_upper must be true.",
        "wrong_hint": "Escape-speed guesses or treating the bound as a measured shift fail.",
    },
    "lab_sga_beam_topk": {
        "title": "Beam selection top-k accuracy on the 8-sample fixture",
        "readme": "true_beams = [3,7,1,4,4,0,6,2]; ranked = [[3,2,5],[6,7,1],[1,0,2],[5,6,4],[4,3,5],[2,1,3],[6,5,7],[0,1,2]]. Report top1, top3, n_samples, dataset_class.",
        "wrong_hint": "Counting a top-3 hit as top-1, or labeling the fixture MEASURED, fails.",
    },
    "lab_sga_paired_ci": {
        "title": "Paired 95% interval — baseline vs model over five seeds",
        "readme": "baseline = [0.61,0.63,0.60,0.62,0.64], model = [0.66,0.65,0.67,0.64,0.68]. Use the paired t-interval with t(0.975, df=4) = 2.776. Claim improvement only if the interval excludes 0.",
        "wrong_hint": "Using a z-value, unpaired variance, or claiming improvement against the interval fails.",
    },
    "lab_sga_oran_loops": {
        "title": "O-RAN control loops — real-time, near-RT RIC, non-RT RIC",
        "readme": "Classify at least three tasks by loop latency: <10 ms real_time, 10 ms–1 s near_real_time (xApp), ≥1 s non_real_time (rApp). The A1 policy target is near_rt_ric.",
        "wrong_hint": "Putting rApp training in the real-time loop or targeting A1 at the DU fails.",
    },
    "lab_sga_twin_gap": {
        "title": "Digital-twin gap — RMSE vs reference sim is not calibration",
        "readme": "twin = [-95,-97,-99,-101] dBm, reference_sim = [-94,-98,-100,-103] dBm. Compute RMSE. With measured_samples = 0, status is UNCALIBRATED_NO_MEASUREMENTS and calibrated_claim false.",
        "wrong_hint": "Calling a twin-vs-sim comparison calibrated fails.",
    },
    "lab_sga_validity": {
        "title": "Threats to validity and ethics guardrails",
        "readme": "Name at least one internal, external, construct, and conclusion threat. Confirm synthetic_data_only, no private competition IQ, no affiliation claim.",
        "wrong_hint": "Missing a validity kind or using private IQ fails.",
    },
    "lab_sga_research_capstone": {
        "title": "Research capstone packet — traced figures, no submission claim",
        "readme": "labs_passed ≥ 6; every figure carries config_sha256 and seed; submitted_claim false; evidence_class SYNTHETIC_SIM; no_key_leak true.",
        "wrong_hint": "Untraced figures or a paper-submission claim fail.",
    },
}
for _lab_id, _spec in LAB_SPECS_008.items():
    _spec["course_id"] = COURSE
    _spec["required_keys"] = []
