"""Runnable labs for batch009 — NETWORKING_INFRA + CYBER_SOC closure (defensive only)."""
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


B_NET = "NETWORKING_INFRA Packet Range. Safe/local fixtures only — no unauthorized capture."
B_CYB = (
    "CYBER_SOC Harbor defensive education only. No exploit kits, no offensive malware, "
    "no unauthorized scanning. Sandboxed fixtures only."
)


def lab_wifi_fundamentals(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_wifi_fundamentals",
        "COMPUTER_NETWORKING",
        submission,
        ["ssid", "band_ghz", "channel", "auth", "guest_isolated"],
        B_NET,
    )
    if data is None:
        return _result("lab_wifi_fundamentals", "COMPUTER_NETWORKING", checks, B_NET)
    checks.append(_check("ssid", bool(str(data.get("ssid") or "").strip()), "ssid"))
    checks.append(_check("band", float(data.get("band_ghz") or 0) in (2.4, 5.0, 6.0), "band"))
    checks.append(_check("channel", int(data.get("channel") or 0) > 0, "channel"))
    checks.append(_check("auth", str(data.get("auth") or "").upper() in ("WPA3", "WPA2", "OPEN_LAB_ONLY"), "auth"))
    checks.append(_check("guest", data.get("guest_isolated") is True, "guest"))
    return _result("lab_wifi_fundamentals", "COMPUTER_NETWORKING", checks, B_NET)


def lab_transport_ports(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_transport_ports",
        "COMPUTER_NETWORKING",
        submission,
        ["map", "handshake", "refuse_telnet"],
        B_NET,
    )
    if data is None:
        return _result("lab_transport_ports", "COMPUTER_NETWORKING", checks, B_NET)
    m = data.get("map") or {}
    checks.append(_check("https", str(m.get("https") or "") in ("443", "tcp/443"), "https"))
    checks.append(_check("dns", str(m.get("dns") or "") in ("53", "udp/53", "tcp/53"), "dns"))
    hs = data.get("handshake") or []
    checks.append(_check("hs", list(hs) == ["SYN", "SYN-ACK", "ACK"], "hs"))
    checks.append(_check("no_telnet", data.get("refuse_telnet") is True, "telnet"))
    return _result("lab_transport_ports", "COMPUTER_NETWORKING", checks, B_NET)


def lab_packet_capture_fixture(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_packet_capture_fixture",
        "COMPUTER_NETWORKING",
        submission,
        ["frames", "ethertype", "dst_ip", "authorized_fixture"],
        B_NET,
    )
    if data is None:
        return _result("lab_packet_capture_fixture", "COMPUTER_NETWORKING", checks, B_NET)
    checks.append(_check("frames", int(data.get("frames") or 0) >= 1, "frames"))
    checks.append(_check("etype", str(data.get("ethertype") or "").lower() in ("0x0800", "0800", "ipv4"), "etype"))
    checks.append(_check("dst", str(data.get("dst_ip") or "").startswith("10."), "dst"))
    checks.append(_check("auth", data.get("authorized_fixture") is True, "auth"))
    return _result("lab_packet_capture_fixture", "COMPUTER_NETWORKING", checks, B_NET)


def lab_ops_runbook(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ops_runbook",
        "COMPUTER_NETWORKING",
        submission,
        ["symptom", "checks", "escalate_if", "fabricated_outage"],
        B_NET,
    )
    if data is None:
        return _result("lab_ops_runbook", "COMPUTER_NETWORKING", checks, B_NET)
    steps = data.get("checks") or []
    checks.append(_check("symptom", len(str(data.get("symptom") or "")) >= 8, "symptom"))
    checks.append(_check("checks", isinstance(steps, list) and len(steps) >= 3, "checks"))
    checks.append(_check("escalate", len(str(data.get("escalate_if") or "")) >= 8, "escalate"))
    checks.append(_check("honest", data.get("fabricated_outage") is False, "honest"))
    return _result("lab_ops_runbook", "COMPUTER_NETWORKING", checks, B_NET)


def lab_phishing_defense(submission: Any = None) -> LabResult:
    """Defensive phishing recognition on fixture mail only — no phishing kits."""
    data, checks = _require_student(
        "lab_phishing_defense",
        "CYBERSECURITY",
        submission,
        ["indicators", "action", "report_path", "no_credential_harvest"],
        B_CYB,
    )
    if data is None:
        return _result("lab_phishing_defense", "CYBERSECURITY", checks, B_CYB)
    inds = data.get("indicators") or []
    checks.append(_check("indicators", isinstance(inds, list) and len(inds) >= 2, "indicators"))
    checks.append(
        _check(
            "action",
            str(data.get("action") or "") in ("report_and_delete", "quarantine", "report_only"),
            "action",
        )
    )
    checks.append(_check("report", len(str(data.get("report_path") or "")) >= 4, "report"))
    checks.append(_check("no_harvest", data.get("no_credential_harvest") is True, "no_harvest"))
    return _result("lab_phishing_defense", "CYBERSECURITY", checks, B_CYB)


def lab_threat_model(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_threat_model",
        "CYBERSECURITY",
        submission,
        ["asset", "threats", "controls", "offensive_scope"],
        B_CYB,
    )
    if data is None:
        return _result("lab_threat_model", "CYBERSECURITY", checks, B_CYB)
    threats = data.get("threats") or []
    controls = data.get("controls") or []
    checks.append(_check("asset", len(str(data.get("asset") or "")) >= 4, "asset"))
    checks.append(_check("threats", isinstance(threats, list) and len(threats) >= 3, "threats"))
    checks.append(_check("controls", isinstance(controls, list) and len(controls) >= 2, "controls"))
    checks.append(_check("scope", data.get("offensive_scope") == "none", "scope"))
    return _result("lab_threat_model", "CYBERSECURITY", checks, B_CYB)


def lab_secure_config_audit(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_secure_config_audit",
        "CYBERSECURITY",
        submission,
        ["findings", "severity_max", "remediation", "live_scan"],
        B_CYB,
    )
    if data is None:
        return _result("lab_secure_config_audit", "CYBERSECURITY", checks, B_CYB)
    findings = data.get("findings") or []
    checks.append(_check("findings", isinstance(findings, list) and len(findings) >= 2, "findings"))
    checks.append(
        _check(
            "sev",
            str(data.get("severity_max") or "").lower() in ("low", "medium", "high", "critical"),
            "sev",
        )
    )
    checks.append(_check("remediation", len(str(data.get("remediation") or "")) >= 8, "remediation"))
    checks.append(_check("no_live", data.get("live_scan") is False, "fixture_only"))
    return _result("lab_secure_config_audit", "CYBERSECURITY", checks, B_CYB)


LABS_009 = {
    "lab_wifi_fundamentals": lab_wifi_fundamentals,
    "lab_transport_ports": lab_transport_ports,
    "lab_packet_capture_fixture": lab_packet_capture_fixture,
    "lab_ops_runbook": lab_ops_runbook,
    "lab_phishing_defense": lab_phishing_defense,
    "lab_threat_model": lab_threat_model,
    "lab_secure_config_audit": lab_secure_config_audit,
}

# Full lists (dict.update replaces keys) — include legacy + new labs.
COURSE_LABS_009 = {
    "COMPUTER_NETWORKING": [
        "lab_cidr_math",
        "lab_datapath",
        "lab_vlan_mac",
        "lab_spf_routing",
        "lab_nat_acl",
        "lab_dns_resolution",
        "lab_wifi_fundamentals",
        "lab_transport_ports",
        "lab_packet_capture_fixture",
        "lab_ops_runbook",
    ],
    "CYBERSECURITY": [
        "lab_siem_triage",
        "lab_hardening_baseline",
        "lab_iam_rbac",
        "lab_segmentation_zones",
        "lab_incident_playbook",
        "lab_safe_vuln_detect",
        "lab_forensics_timeline",
        "lab_phishing_defense",
        "lab_threat_model",
        "lab_secure_config_audit",
    ],
    "NETWORKING_INFRA": [
        "lab_cidr_math",
        "lab_datapath",
        "lab_vlan_mac",
        "lab_spf_routing",
        "lab_nat_acl",
        "lab_dns_resolution",
        "lab_wifi_fundamentals",
        "lab_transport_ports",
        "lab_packet_capture_fixture",
        "lab_ops_runbook",
    ],
    "CYBER_SOC": [
        "lab_siem_triage",
        "lab_hardening_baseline",
        "lab_iam_rbac",
        "lab_segmentation_zones",
        "lab_incident_playbook",
        "lab_safe_vuln_detect",
        "lab_forensics_timeline",
        "lab_phishing_defense",
        "lab_threat_model",
        "lab_secure_config_audit",
    ],
}

REFERENCE_009 = {
    "lab_wifi_fundamentals": {
        "ssid": "PacketRange-Guest",
        "band_ghz": 5.0,
        "channel": 36,
        "auth": "WPA3",
        "guest_isolated": True,
    },
    "lab_transport_ports": {
        "map": {"https": "443", "dns": "53", "ssh": "22"},
        "handshake": ["SYN", "SYN-ACK", "ACK"],
        "refuse_telnet": True,
    },
    "lab_packet_capture_fixture": {
        "frames": 3,
        "ethertype": "0x0800",
        "dst_ip": "10.20.40.9",
        "authorized_fixture": True,
    },
    "lab_ops_runbook": {
        "symptom": "Yard cannot reach Roof /24",
        "checks": ["L2 VLAN", "LPM route", "ACL order"],
        "escalate_if": "route present but TTL expire loop",
        "fabricated_outage": False,
    },
    "lab_phishing_defense": {
        "indicators": ["mismatched_from_domain", "urgent_credential_request"],
        "action": "report_and_delete",
        "report_path": "harbor-soc/phishing-report",
        "no_credential_harvest": True,
    },
    "lab_threat_model": {
        "asset": "Harbor SIEM fixture",
        "threats": ["spoofed_syslog", "orphaned_bot_token", "kiosk_to_soc_path"],
        "controls": ["zone_deny", "bot_read_only"],
        "offensive_scope": "none",
    },
    "lab_secure_config_audit": {
        "findings": ["ssh_password_auth_true", "guest_login_true"],
        "severity_max": "high",
        "remediation": "set ssh_password_auth false; guest_login false",
        "live_scan": False,
    },
}

WRONG_009 = {
    "lab_wifi_fundamentals": {
        "ssid": "",
        "band_ghz": 1.0,
        "channel": 0,
        "auth": "NONE",
        "guest_isolated": False,
    },
    "lab_transport_ports": {
        "map": {"https": "80"},
        "handshake": ["SYN"],
        "refuse_telnet": False,
    },
    "lab_packet_capture_fixture": {
        "frames": 0,
        "ethertype": "0x86dd",
        "dst_ip": "8.8.8.8",
        "authorized_fixture": False,
    },
    "lab_ops_runbook": {
        "symptom": "down",
        "checks": ["ping"],
        "escalate_if": "x",
        "fabricated_outage": True,
    },
    "lab_phishing_defense": {
        "indicators": ["x"],
        "action": "harvest_creds",
        "report_path": "",
        "no_credential_harvest": False,
    },
    "lab_threat_model": {
        "asset": "x",
        "threats": ["a"],
        "controls": ["b"],
        "offensive_scope": "exploit",
    },
    "lab_secure_config_audit": {
        "findings": ["x"],
        "severity_max": "unknown",
        "remediation": "fix",
        "live_scan": True,
    },
}

LAB_SPECS_009 = {
    "lab_wifi_fundamentals": {
        "course_id": "COMPUTER_NETWORKING",
        "classification": "DIGITAL",
        "title": "Wi-Fi fundamentals on Packet Range fixture",
        "readme": "Map SSID/band/channel/auth for the authorized Packet Range guest SSID. No live campus survey claims.",
        "required_keys": ["ssid", "band_ghz", "channel", "auth", "guest_isolated"],
        "wrong_hint": "Wrong auth or guest_isolated=false fails isolation check.",
    },
    "lab_transport_ports": {
        "course_id": "COMPUTER_NETWORKING",
        "classification": "DIGITAL",
        "title": "Transport ports and handshake vocabulary",
        "readme": "Map https/dns/ssh ports and list SYN/SYN-ACK/ACK. Refuse telnet as default admin path.",
        "required_keys": ["map", "handshake", "refuse_telnet"],
        "wrong_hint": "Mapping https to 80 or allowing telnet fails.",
    },
    "lab_packet_capture_fixture": {
        "course_id": "COMPUTER_NETWORKING",
        "classification": "SIMULATED",
        "title": "Authorized packet-capture fixture summary",
        "readme": "Summarize fixture frames only. authorized_fixture must be true. No offensive payload crafting.",
        "required_keys": ["frames", "ethertype", "dst_ip", "authorized_fixture"],
        "wrong_hint": "authorized_fixture=false fails.",
    },
    "lab_ops_runbook": {
        "course_id": "COMPUTER_NETWORKING",
        "classification": "DIGITAL",
        "title": "Network ops runbook — Yard to Roof path",
        "readme": "Document symptom, ordered checks, escalate_if. fabricated_outage must be false.",
        "required_keys": ["symptom", "checks", "escalate_if", "fabricated_outage"],
        "wrong_hint": "fabricated_outage=true fails honesty gate.",
    },
    "lab_phishing_defense": {
        "course_id": "CYBERSECURITY",
        "classification": "DIGITAL",
        "title": "Phishing defense triage (defensive only)",
        "readme": "Identify indicators and report_and_delete. Do not craft lures or harvest credentials.",
        "required_keys": ["indicators", "action", "report_path", "no_credential_harvest"],
        "wrong_hint": "no_credential_harvest=false fails.",
    },
    "lab_threat_model": {
        "course_id": "CYBERSECURITY",
        "classification": "DIGITAL",
        "title": "Defensive threat model for Harbor SIEM fixture",
        "readme": "List assets, threats, controls. offensive_scope must be none.",
        "required_keys": ["asset", "threats", "controls", "offensive_scope"],
        "wrong_hint": "offensive_scope other than none fails.",
    },
    "lab_secure_config_audit": {
        "course_id": "CYBERSECURITY",
        "classification": "DIGITAL",
        "title": "Secure configuration audit on fixture",
        "readme": "Audit fixture findings only. live_scan must be false.",
        "required_keys": ["findings", "severity_max", "remediation", "live_scan"],
        "wrong_hint": "live_scan=true fails sandbox rule.",
    },
}
