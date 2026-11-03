"""CYBER_SOC Night Shift Desk labs. Graders recompute from fixtures or submitted inputs.

Defensive analysis only: no lab asks for exploit code, live targets, or real customer data.
"""
from __future__ import annotations

import hashlib
import math
import re
from datetime import datetime
from typing import Any

from waike_course_ready.batch007.labs import LabResult, _check, _require_student, _result

COURSE = "CYBER_SOC"
B_SOC = (
    "CYBER_SOC Night Shift Desk. Synthetic logs, documentation IP ranges, and public framework IDs only; "
    "no exploit development, no live targets, no real customer data. Not student/teacher E6."
)

AUTH_LOG = [
    "Nov 03 01:12:04 bastion sshd[4121]: Failed password for root from 203.0.113.45 port 52211 ssh2",
    "Nov 03 01:12:06 bastion sshd[4121]: Failed password for root from 203.0.113.45 port 52213 ssh2",
    "Nov 03 01:12:09 bastion sshd[4125]: Failed password for invalid user admin from 198.51.100.7 port 40022 ssh2",
    "Nov 03 01:12:11 bastion sshd[4121]: Failed password for root from 203.0.113.45 port 52219 ssh2",
    "Nov 03 01:13:40 bastion sshd[4130]: Accepted publickey for naiya from 192.0.2.10 port 61000 ssh2",
    "Nov 03 01:14:02 bastion sshd[4133]: Failed password for naiya from 192.0.2.10 port 61004 ssh2",
    "Nov 03 01:15:30 bastion sshd[4140]: Failed password for invalid user oracle from 198.51.100.7 port 40100 ssh2",
    "Nov 03 01:15:31 bastion sshd[4141]: Accepted password for root from 203.0.113.45 port 52290 ssh2",
]
_LOG_RE = re.compile(r"sshd\[\d+\]: (Failed|Accepted) \S+ for (?:invalid user )?(\S+) from (\S+) port")


def parse_auth_log(lines: list[str]) -> dict[str, Any]:
    failed: dict[str, int] = {}
    accepted_after: list[str] = []
    for line in lines:
        m = _LOG_RE.search(line)
        if not m:
            continue
        outcome, _user, ip = m.groups()
        if outcome == "Failed":
            failed[ip] = failed.get(ip, 0) + 1
        elif failed.get(ip) and ip not in accepted_after:
            accepted_after.append(ip)
    top = max(failed, key=lambda k: (failed[k], k)) if failed else None
    return {"failed_by_ip": failed, "top_source": top, "accepted_after_failures": accepted_after}


def lab_soc_log_parse(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_log_parse", COURSE, submission, ["failed_by_ip", "top_source", "accepted_after_failures"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_log_parse", COURSE, checks, B_SOC)
    truth = parse_auth_log(AUTH_LOG)
    checks.append(_check("failed_counts_recomputed", data.get("failed_by_ip") == truth["failed_by_ip"], str(truth["failed_by_ip"])))
    checks.append(_check("top_source", data.get("top_source") == truth["top_source"], str(truth["top_source"])))
    checks.append(_check(
        "success_after_failures_flagged",
        sorted(data.get("accepted_after_failures") or []) == sorted(truth["accepted_after_failures"]),
        "an accepted login from an address that just failed is the line to escalate",
    ))
    return _result("lab_soc_log_parse", COURSE, checks, B_SOC)


FAIL_EVENTS = [
    ("203.0.113.45", 0), ("203.0.113.45", 20), ("198.51.100.7", 30), ("203.0.113.45", 50),
    ("203.0.113.45", 65), ("198.51.100.7", 200), ("203.0.113.45", 70), ("198.51.100.7", 230),
    ("198.51.100.7", 250), ("198.51.100.7", 265), ("192.0.2.10", 300),
]


def window_alerts(threshold: int, window_s: int, events: list[tuple[str, int]] = FAIL_EVENTS) -> dict[str, int]:
    """First time each source reaches `threshold` failures within `window_s` seconds (inclusive)."""
    seen: dict[str, list[int]] = {}
    fired: dict[str, int] = {}
    for ip, t in sorted(events, key=lambda e: e[1]):
        if ip in fired:
            continue
        times = [x for x in seen.get(ip, []) if t - x <= window_s] + [t]
        seen[ip] = times
        if len(times) >= threshold:
            fired[ip] = t
    return fired


def lab_soc_window_rule(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_window_rule", COURSE, submission, ["threshold", "window_s", "alerts"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_window_rule", COURSE, checks, B_SOC)
    th, win = data.get("threshold"), data.get("window_s")
    ok_in = isinstance(th, int) and th >= 2 and isinstance(win, int) and win > 0
    checks.append(_check("rule_parameters", ok_in, "integer threshold ≥ 2 and window > 0"))
    if ok_in:
        truth = window_alerts(th, win)
        checks.append(_check("alerts_recomputed", data.get("alerts") == truth, f"expected {truth}"))
    return _result("lab_soc_window_rule", COURSE, checks, B_SOC)


DETECTION_COUNTS = {"tp": 18, "fp": 42, "fn": 6, "tn": 934}


def detection_metrics(c: dict[str, int] = DETECTION_COUNTS) -> dict[str, float]:
    return {
        "precision": c["tp"] / (c["tp"] + c["fp"]),
        "recall": c["tp"] / (c["tp"] + c["fn"]),
        "false_positive_rate": c["fp"] / (c["fp"] + c["tn"]),
        "alerts": c["tp"] + c["fp"],
    }


def _close(a: Any, b: float, tol: float) -> bool:
    try:
        return abs(float(a) - b) <= tol
    except (TypeError, ValueError):
        return False


def lab_soc_detection_metrics(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_detection_metrics", COURSE, submission,
        ["precision", "recall", "false_positive_rate", "alerts", "needs_tuning"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_detection_metrics", COURSE, checks, B_SOC)
    m = detection_metrics()
    for key in ("precision", "recall", "false_positive_rate"):
        checks.append(_check(f"{key}_recomputed", _close(data.get(key), m[key], 5e-4), f"expected {m[key]:.4f}"))
    checks.append(_check("alert_volume", data.get("alerts") == m["alerts"], f"expected {m['alerts']}"))
    checks.append(_check("tuning_call_matches_precision", data.get("needs_tuning") is (m["precision"] < 0.5), "precision < 0.5 → tune"))
    return _result("lab_soc_detection_metrics", COURSE, checks, B_SOC)


IOC_SAMPLE_TEXT = "WAIKE-SOC training sample: invoice_2026-11.pdf.exe (inert text, not malware)"
IOC_SHA256 = {hashlib.sha256(IOC_SAMPLE_TEXT.encode("utf-8")).hexdigest()}
IOC_DOMAINS = {"update-check.example.net"}


def defang(url: str) -> str:
    scheme, sep, rest = url.partition("://")
    if not sep:
        return url.replace(".", "[.]")
    host, slash, path = rest.partition("/")
    scheme = {"http": "hxxp", "https": "hxxps"}.get(scheme.lower(), scheme)
    return f"{scheme}://{host.replace('.', '[.]')}{slash}{path}"


def lab_soc_ioc_match(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_ioc_match", COURSE, submission, ["sample_text", "sha256", "url", "defanged_url", "ioc_match"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_ioc_match", COURSE, checks, B_SOC)
    digest = hashlib.sha256(str(data.get("sample_text")).encode("utf-8")).hexdigest()
    checks.append(_check("sha256_recomputed", str(data.get("sha256")).lower() == digest, "sha256(sample_text)"))
    url = str(data.get("url") or "")
    checks.append(_check("defang_recomputed", data.get("defanged_url") == defang(url), defang(url)))
    host = url.partition("://")[2].partition("/")[0].lower()
    hit = digest in IOC_SHA256 or host in IOC_DOMAINS
    checks.append(_check("ioc_match_recomputed", data.get("ioc_match") is hit, f"expected {hit}"))
    return _result("lab_soc_ioc_match", COURSE, checks, B_SOC)


ATTACK_BEHAVIORS = {
    "B1": ("many failed SSH logins from one address", "T1110", {"credential_access"}),
    "B2": ("night login with a valid account that was never used before", "T1078",
           {"initial_access", "persistence", "privilege_escalation", "defense_evasion"}),
    "B3": ("user opened a spoofed invoice attachment", "T1566", {"initial_access"}),
    "B4": ("PowerShell started with an encoded command line", "T1059", {"execution"}),
    "B5": ("files renamed .locked and a ransom note dropped", "T1486", {"impact"}),
}


def lab_soc_attack_map(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_attack_map", COURSE, submission, ["mappings", "actor_attribution_claim"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_attack_map", COURSE, checks, B_SOC)
    rows = data.get("mappings") if isinstance(data.get("mappings"), list) else []
    by_id = {r.get("behavior_id"): r for r in rows if isinstance(r, dict)}
    checks.append(_check("all_behaviors_mapped", set(by_id) == set(ATTACK_BEHAVIORS), f"mapped={sorted(by_id)}"))
    wrong = [
        bid for bid, (_, tech, tactics) in ATTACK_BEHAVIORS.items()
        if bid in by_id and (by_id[bid].get("technique_id") != tech or by_id[bid].get("tactic") not in tactics)
    ]
    checks.append(_check("techniques_and_tactics", bool(by_id) and not wrong, f"wrong={wrong}"))
    checks.append(_check("no_actor_attribution", data.get("actor_attribution_claim") is False, "techniques are not actors"))
    return _result("lab_soc_attack_map", COURSE, checks, B_SOC)


DMARC_MESSAGES = {
    "A": {"from_domain": "mail.harborpay.example", "return_path_domain": "bounce.harborpay.example",
          "spf_pass": True, "dkim_domain": "harborpay.example", "dkim_pass": True},
    "B": {"from_domain": "harborpay.example", "return_path_domain": "mailer.bulk-sender.example",
          "spf_pass": True, "dkim_domain": "bulk-sender.example", "dkim_pass": True},
}


def org_domain(host: str) -> str:
    return ".".join(host.lower().strip(".").split(".")[-2:])


def dmarc_relaxed(msg: dict[str, Any]) -> dict[str, bool]:
    org = org_domain(msg["from_domain"])
    spf_aligned = bool(msg["spf_pass"]) and org_domain(msg["return_path_domain"]) == org
    dkim_aligned = bool(msg["dkim_pass"]) and org_domain(msg["dkim_domain"]) == org
    return {"spf_aligned": spf_aligned, "dkim_aligned": dkim_aligned, "dmarc_pass": spf_aligned or dkim_aligned}


def lab_soc_dmarc_align(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_soc_dmarc_align", COURSE, submission, ["results"], B_SOC)
    if data is None:
        return _result("lab_soc_dmarc_align", COURSE, checks, B_SOC)
    res = data.get("results") if isinstance(data.get("results"), dict) else {}
    for mid, msg in DMARC_MESSAGES.items():
        truth = dmarc_relaxed(msg)
        checks.append(_check(f"message_{mid}_alignment", res.get(mid) == truth, f"expected {truth}"))
    return _result("lab_soc_dmarc_align", COURSE, checks, B_SOC)


_AV = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}
_AC = {"L": 0.77, "H": 0.44}
_PR_U = {"N": 0.85, "L": 0.62, "H": 0.27}
_PR_C = {"N": 0.85, "L": 0.68, "H": 0.5}
_UI = {"N": 0.85, "R": 0.62}
_CIA = {"H": 0.56, "L": 0.22, "N": 0.0}


def cvss_roundup(x: float) -> float:
    i = round(x * 100000)
    if i % 10000 == 0:
        return i / 100000.0
    return (math.floor(i / 10000) + 1) / 10.0


def cvss31_base(vector: str) -> float:
    parts = dict(p.split(":", 1) for p in vector.removeprefix("CVSS:3.1/").split("/"))
    changed = parts["S"] == "C"
    iss = 1 - (1 - _CIA[parts["C"]]) * (1 - _CIA[parts["I"]]) * (1 - _CIA[parts["A"]])
    impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15 if changed else 6.42 * iss
    pr = (_PR_C if changed else _PR_U)[parts["PR"]]
    expl = 8.22 * _AV[parts["AV"]] * _AC[parts["AC"]] * pr * _UI[parts["UI"]]
    if impact <= 0:
        return 0.0
    return cvss_roundup(min((1.08 if changed else 1.0) * (impact + expl), 10.0))


def cvss_severity(score: float) -> str:
    if score == 0:
        return "None"
    if score < 4.0:
        return "Low"
    if score < 7.0:
        return "Medium"
    if score < 9.0:
        return "High"
    return "Critical"


def lab_soc_cvss_score(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_soc_cvss_score", COURSE, submission, ["vectors"], B_SOC)
    if data is None:
        return _result("lab_soc_cvss_score", COURSE, checks, B_SOC)
    rows = data.get("vectors") if isinstance(data.get("vectors"), list) else []
    checks.append(_check("two_vectors", len(rows) >= 2, f"vectors={len(rows)}"))
    bad = []
    for r in rows:
        try:
            score = cvss31_base(str(r.get("vector")))
        except (KeyError, ValueError, AttributeError):
            bad.append(r)
            continue
        if not _close(r.get("base_score"), score, 1e-9) or r.get("severity") != cvss_severity(score):
            bad.append(r)
    checks.append(_check("scores_recomputed", bool(rows) and not bad, f"wrong={len(bad)}"))
    return _result("lab_soc_cvss_score", COURSE, checks, B_SOC)


SEV_WEIGHT = {"critical": 4, "high": 3, "medium": 2, "low": 1}
SLA_MIN = {"critical": 15, "high": 60, "medium": 240, "low": 1440}
TRIAGE_ALERTS = [
    {"id": "A1", "severity": "high", "asset_criticality": 3, "received_min": 5},
    {"id": "A2", "severity": "critical", "asset_criticality": 1, "received_min": 12},
    {"id": "A3", "severity": "medium", "asset_criticality": 3, "received_min": 2},
    {"id": "A4", "severity": "low", "asset_criticality": 3, "received_min": 1},
    {"id": "A5", "severity": "critical", "asset_criticality": 3, "received_min": 20},
    {"id": "A6", "severity": "high", "asset_criticality": 2, "received_min": 8},
]


def triage_order(alerts: list[dict[str, Any]] = TRIAGE_ALERTS) -> tuple[list[str], dict[str, int]]:
    ranked = sorted(alerts, key=lambda a: (-SEV_WEIGHT[a["severity"]] * a["asset_criticality"], a["received_min"]))
    due = {a["id"]: a["received_min"] + SLA_MIN[a["severity"]] for a in alerts}
    return [a["id"] for a in ranked], due


def lab_soc_triage_queue(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_soc_triage_queue", COURSE, submission, ["ordered_ids", "due_min"], B_SOC)
    if data is None:
        return _result("lab_soc_triage_queue", COURSE, checks, B_SOC)
    order, due = triage_order()
    checks.append(_check("queue_order_recomputed", data.get("ordered_ids") == order, f"expected {order}"))
    checks.append(_check("sla_due_recomputed", data.get("due_min") == due, "received + SLA by severity"))
    return _result("lab_soc_triage_queue", COURSE, checks, B_SOC)


SHIFT_INCIDENTS = [
    {"id": "I1", "occurred": "2026-11-03T01:00", "detected": "2026-11-03T01:12", "resolved": "2026-11-03T02:30"},
    {"id": "I2", "occurred": "2026-11-03T02:10", "detected": "2026-11-03T02:55", "resolved": "2026-11-03T04:00"},
    {"id": "I3", "occurred": "2026-11-03T03:00", "detected": "2026-11-03T03:05", "resolved": "2026-11-03T03:40"},
    {"id": "I4", "occurred": "2026-11-03T04:20", "detected": "2026-11-03T05:30", "resolved": "2026-11-03T08:00"},
]


def _minutes(a: str, b: str) -> float:
    return (datetime.fromisoformat(b) - datetime.fromisoformat(a)).total_seconds() / 60.0


def shift_metrics(incidents: list[dict[str, str]] = SHIFT_INCIDENTS) -> dict[str, float]:
    ttd = sorted(_minutes(i["occurred"], i["detected"]) for i in incidents)
    ttr = [_minutes(i["detected"], i["resolved"]) for i in incidents]
    n = len(ttd)
    median = ttd[n // 2] if n % 2 else (ttd[n // 2 - 1] + ttd[n // 2]) / 2
    return {"mttd_min": sum(ttd) / n, "mttr_min": sum(ttr) / n, "median_ttd_min": median}


def lab_soc_shift_metrics(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_shift_metrics", COURSE, submission, ["mttd_min", "mttr_min", "median_ttd_min"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_shift_metrics", COURSE, checks, B_SOC)
    m = shift_metrics()
    for key, val in m.items():
        checks.append(_check(f"{key}_recomputed", _close(data.get(key), val, 0.01), f"expected {val}"))
    return _result("lab_soc_shift_metrics", COURSE, checks, B_SOC)


NIST_IR_PHASES = {"preparation", "detection_analysis", "containment_eradication_recovery", "post_incident"}
_TECH_RE = re.compile(r"^T\d{4}(\.\d{3})?$")


def lab_soc_shift_handoff(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_soc_shift_handoff", COURSE, submission,
        ["labs_passed", "open_incidents", "mttd_min", "mttr_min", "real_customer_data", "offensive_tooling"], B_SOC,
    )
    if data is None:
        return _result("lab_soc_shift_handoff", COURSE, checks, B_SOC)
    checks.append(_check("labs_passed", isinstance(data.get("labs_passed"), int) and data["labs_passed"] >= 6, "≥6 prior labs"))
    rows = data.get("open_incidents") if isinstance(data.get("open_incidents"), list) else []
    good = all(
        isinstance(r, dict) and _TECH_RE.match(str(r.get("technique_id") or "")) and r.get("nist_phase") in NIST_IR_PHASES
        and str(r.get("next_owner") or "").strip()
        for r in rows
    )
    checks.append(_check("incidents_handed_off", bool(rows) and good, "technique ID, NIST phase, next owner"))
    m = shift_metrics()
    checks.append(_check("metrics_match_shift", _close(data.get("mttd_min"), m["mttd_min"], 0.01)
                         and _close(data.get("mttr_min"), m["mttr_min"], 0.01), "MTTD/MTTR from the shift log"))
    checks.append(_check("no_customer_data", data.get("real_customer_data") is False, "synthetic only"))
    checks.append(_check("no_offensive_tooling", data.get("offensive_tooling") is False, "defensive desk"))
    return _result("lab_soc_shift_handoff", COURSE, checks, B_SOC)


LAB_ORDER_SOC = [
    "lab_soc_log_parse", "lab_soc_window_rule", "lab_soc_detection_metrics", "lab_soc_ioc_match",
    "lab_soc_attack_map", "lab_soc_dmarc_align", "lab_soc_cvss_score", "lab_soc_triage_queue",
    "lab_soc_shift_metrics", "lab_soc_shift_handoff",
]
LABS_SOC = {name: globals()[name] for name in LAB_ORDER_SOC}

_PARSED = parse_auth_log(AUTH_LOG)
_DET = detection_metrics()
_ORDER, _DUE = triage_order()
_SHIFT = shift_metrics()
_CVSS_REF = ["CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N"]

REFERENCE_SOC: dict[str, dict[str, Any]] = {
    "lab_soc_log_parse": dict(_PARSED),
    "lab_soc_window_rule": {"threshold": 4, "window_s": 60, "alerts": window_alerts(4, 60)},
    "lab_soc_detection_metrics": {
        "precision": round(_DET["precision"], 4), "recall": round(_DET["recall"], 4),
        "false_positive_rate": round(_DET["false_positive_rate"], 4), "alerts": _DET["alerts"], "needs_tuning": True,
    },
    "lab_soc_ioc_match": {
        "sample_text": IOC_SAMPLE_TEXT, "sha256": next(iter(IOC_SHA256)),
        "url": "http://update-check.example.net/payload", "defanged_url": defang("http://update-check.example.net/payload"),
        "ioc_match": True,
    },
    "lab_soc_attack_map": {
        "mappings": [
            {"behavior_id": bid, "technique_id": tech, "tactic": sorted(tactics)[0]}
            for bid, (_, tech, tactics) in ATTACK_BEHAVIORS.items()
        ],
        "actor_attribution_claim": False,
    },
    "lab_soc_dmarc_align": {"results": {mid: dmarc_relaxed(m) for mid, m in DMARC_MESSAGES.items()}},
    "lab_soc_cvss_score": {"vectors": [
        {"vector": v, "base_score": cvss31_base(v), "severity": cvss_severity(cvss31_base(v))} for v in _CVSS_REF
    ]},
    "lab_soc_triage_queue": {"ordered_ids": _ORDER, "due_min": _DUE},
    "lab_soc_shift_metrics": {k: round(v, 2) for k, v in _SHIFT.items()},
    "lab_soc_shift_handoff": {
        "labs_passed": 9,
        "open_incidents": [{"id": "I4", "technique_id": "T1486", "nist_phase": "containment_eradication_recovery", "next_owner": "day-shift lead"}],
        "mttd_min": _SHIFT["mttd_min"], "mttr_min": _SHIFT["mttr_min"],
        "real_customer_data": False, "offensive_tooling": False,
    },
}

WRONG_SOC: dict[str, dict[str, Any]] = {
    "lab_soc_log_parse": {"failed_by_ip": {"203.0.113.45": 4}, "top_source": "198.51.100.7", "accepted_after_failures": []},
    "lab_soc_window_rule": {"threshold": 4, "window_s": 60, "alerts": {"203.0.113.45": 70, "198.51.100.7": 265}},
    "lab_soc_detection_metrics": {"precision": 0.75, "recall": 0.3, "false_positive_rate": 0.042, "alerts": 24, "needs_tuning": False},
    "lab_soc_ioc_match": {"sample_text": IOC_SAMPLE_TEXT, "sha256": "0" * 64, "url": "http://update-check.example.net/payload",
                          "defanged_url": "http://update-check.example.net/payload", "ioc_match": False},
    "lab_soc_attack_map": {"mappings": [{"behavior_id": "B1", "technique_id": "T1566", "tactic": "impact"}], "actor_attribution_claim": True},
    "lab_soc_dmarc_align": {"results": {"A": {"spf_aligned": True, "dkim_aligned": True, "dmarc_pass": True},
                                        "B": {"spf_aligned": True, "dkim_aligned": True, "dmarc_pass": True}}},
    "lab_soc_cvss_score": {"vectors": [{"vector": _CVSS_REF[0], "base_score": 10.0, "severity": "Critical"},
                                       {"vector": _CVSS_REF[1], "base_score": 7.8, "severity": "High"}]},
    "lab_soc_triage_queue": {"ordered_ids": ["A2", "A5", "A1", "A6", "A3", "A4"], "due_min": {}},
    "lab_soc_shift_metrics": {"mttd_min": 28.5, "mttr_min": 98.0, "median_ttd_min": 33.0},
    "lab_soc_shift_handoff": {"labs_passed": 2, "open_incidents": [{"id": "I4", "technique_id": "ransomware", "nist_phase": "panic"}],
                              "mttd_min": 0, "mttr_min": 0, "real_customer_data": True, "offensive_tooling": True},
}

LAB_SPECS_SOC: dict[str, dict[str, Any]] = {
    "lab_soc_log_parse": {
        "title": "Auth log anatomy — failures per source and the success that follows",
        "readme": "Parse the eight-line sshd fixture. Report failed_by_ip counts, the top_source, and accepted_after_failures (addresses that logged in after failing).",
        "wrong_hint": "Counting the Accepted line as a failure, or missing the root success from 203.0.113.45, fails.",
    },
    "lab_soc_window_rule": {
        "title": "Brute-force rule — threshold inside a sliding window",
        "readme": "Choose an integer threshold and window_s. Report alerts as {source: first_alert_second} for FAIL_EVENTS. The grader replays the window with your parameters.",
        "wrong_hint": "Counting all failures ever, instead of those inside the window, flags 198.51.100.7 at 60 s.",
    },
    "lab_soc_detection_metrics": {
        "title": "Detection quality — precision, recall, false-positive rate",
        "readme": "Counts: TP 18, FP 42, FN 6, TN 934. Report precision, recall, false_positive_rate, alert volume, and needs_tuning (true when precision < 0.5).",
        "wrong_hint": "Swapping precision and recall, or calling a 30%-precise rule healthy, fails.",
    },
    "lab_soc_ioc_match": {
        "title": "Indicator handling — hash, defang, match",
        "readme": "Hash sample_text with SHA-256, defang the URL (hxxp, [.] in the host), and report whether either indicator is on the desk's IOC list.",
        "wrong_hint": "A pasted hash or a clickable URL in the ticket fails.",
    },
    "lab_soc_attack_map": {
        "title": "ATT&CK mapping — behaviours to technique IDs and tactics",
        "readme": "Map behaviours B1–B5 to their MITRE ATT&CK technique ID and one valid tactic. actor_attribution_claim must be false.",
        "wrong_hint": "Naming a threat group from technique overlap alone fails.",
    },
    "lab_soc_dmarc_align": {
        "title": "Email authentication — SPF/DKIM pass versus DMARC alignment",
        "readme": "For messages A and B report spf_aligned, dkim_aligned, and dmarc_pass using relaxed alignment on the organisational domain.",
        "wrong_hint": "Treating 'SPF pass' as 'DMARC pass' for message B fails.",
    },
    "lab_soc_cvss_score": {
        "title": "CVSS v3.1 base score from a vector string",
        "readme": "Score at least two CVSS:3.1 vectors with the FIRST v3.1 equations and Roundup, and name each severity band.",
        "wrong_hint": "Rounding to nearest instead of Roundup, or guessing 10.0, fails.",
    },
    "lab_soc_triage_queue": {
        "title": "Triage queue — severity × asset criticality, then SLA due times",
        "readme": "Order A1–A6 by severity weight × asset criticality (ties: earliest received) and give each alert's due minute (received + SLA).",
        "wrong_hint": "Sorting by severity alone puts the kiosk's critical alert first and fails.",
    },
    "lab_soc_shift_metrics": {
        "title": "Shift metrics — MTTD, MTTR, and the median that resists one bad night",
        "readme": "From I1–I4 compute mean time to detect, mean time to resolve (from detection), and median time to detect, in minutes.",
        "wrong_hint": "Measuring resolution from occurrence, or swapping mean and median, fails.",
    },
    "lab_soc_shift_handoff": {
        "title": "Shift handoff — open incidents, phases, metrics, boundaries",
        "readme": "labs_passed ≥ 6; each open incident has an ATT&CK technique ID, a NIST SP 800-61 phase, and a next owner; MTTD/MTTR match the shift; no customer data, no offensive tooling.",
        "wrong_hint": "Free-text technique names, invented phases, or offensive tooling fail.",
    },
}
