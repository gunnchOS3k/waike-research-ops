"""Original WAIKE runnable labs with computing validators.

Print-PASS is forbidden. Empty and wrong student artifacts fail.
Golden fixtures do not auto-pass with no learner work.
Security labs operate only on course fixtures in this repository.
"""
from __future__ import annotations

import hashlib
import ipaddress
import json
import re
import socket
import tarfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[2]

SANDBOX_NOTE = (
    "Authorized WAIKE course sandbox/fixture only. Do not run against systems you do not own."
)


@dataclass
class LabResult:
    lab_id: str
    course_id: str
    ok: bool
    checks: list[dict[str, Any]]
    claim_boundary: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "lab_id": self.lab_id,
            "course_id": self.course_id,
            "ok": self.ok,
            "checks": self.checks,
            "claim_boundary": self.claim_boundary,
        }


def _check(name: str, ok: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "ok": bool(ok), "detail": detail}


def _fail_if_print_pass(text: str) -> None:
    if re.fullmatch(r"\s*PASS\s*", text or ""):
        raise AssertionError("print-PASS is not a validator")


def _coerce_submission(submission: Any) -> tuple[dict[str, Any] | None, str]:
    """Return (dict or None, raw text). Raises on print-PASS."""
    if submission is None:
        return None, ""
    if isinstance(submission, (bytes, bytearray)):
        submission = submission.decode("utf-8")
    if isinstance(submission, str):
        _fail_if_print_pass(submission)
        raw = submission
        try:
            obj = json.loads(submission)
        except json.JSONDecodeError:
            return None, raw
        if isinstance(obj, dict):
            return obj, raw
        return None, raw
    if isinstance(submission, dict):
        raw = json.dumps(submission, sort_keys=True)
        _fail_if_print_pass(raw)
        return submission, raw
    return None, str(submission)


def _require_student(lab_id: str, course_id: str, submission: Any, required_keys: list[str], boundary: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    data, raw = _coerce_submission(submission)
    checks: list[dict[str, Any]] = []
    if data is None or data == {}:
        checks.append(_check("student_artifact", False, "empty or missing student JSON — golden path is not a grade"))
        return None, checks
    checks.append(_check("student_artifact", True, "student JSON present"))
    missing = [k for k in required_keys if k not in data]
    if missing:
        checks.append(_check("required_keys", False, f"missing={missing}"))
        return None, checks
    checks.append(_check("required_keys", True, ",".join(required_keys)))
    return data, checks


def _result(lab_id: str, course_id: str, checks: list[dict[str, Any]], boundary: str) -> LabResult:
    return LabResult(lab_id, course_id, all(c["ok"] for c in checks), checks, boundary)


# ---------------------------------------------------------------------------
# Crafted datapath frame (classroom bytes, not a live capture)
# ---------------------------------------------------------------------------

def _craft_frame(ttl: int) -> bytes:
    eth = bytes.fromhex("aaaaaaaaaa01") + bytes.fromhex("aaaaaaaaaa02") + bytes.fromhex("0800")
    ip = bytearray(20)
    ip[0] = 0x45
    ip[2:4] = (40).to_bytes(2, "big")
    ip[8] = int(ttl)
    ip[9] = 6
    ip[12:16] = ipaddress.IPv4Address("10.20.30.14").packed
    ip[16:20] = ipaddress.IPv4Address("10.20.40.9").packed
    return eth + bytes(ip) + bytes(20)


def _parse_ipv4_frame(frame: bytes) -> dict[str, Any]:
    dst_mac = frame[0:6].hex()
    ethertype = int.from_bytes(frame[12:14], "big")
    iph = frame[14:34]
    return {
        "dst_mac": dst_mac,
        "ethertype": ethertype,
        "version": iph[0] >> 4,
        "ihl": iph[0] & 0x0F,
        "ttl": iph[8],
        "proto": iph[9],
        "dst": str(ipaddress.IPv4Address(iph[16:20])),
        "header": bytes(iph),
    }


def _ip_to_int(ip: str) -> int:
    return int(ipaddress.IPv4Address(ip))


def _lpm(table: list[dict[str, Any]], dest: str) -> dict[str, Any]:
    dest_i = _ip_to_int(dest)
    best = None
    best_len = -1
    for row in table:
        net = ipaddress.IPv4Network(row["prefix"], strict=False)
        if dest_i & int(net.netmask) == int(net.network_address) and net.prefixlen >= best_len:
            best_len = net.prefixlen
            best = row
    return best or {"drop": True, "reason": "no_route"}


def _tree_hash(path: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(path.rglob("*")):
        if p.is_file():
            h.update(p.relative_to(path).as_posix().encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def _backup_tree(work: Path | None = None) -> tuple[Path, str]:
    base = work or (ROOT / "artifacts" / "_lab_tmp" / "backup")
    src = base / "src"
    src.mkdir(parents=True, exist_ok=True)
    (src / "ticket_4417.txt").write_text("patron essay draft v3\n", encoding="utf-8")
    (src / "notes.md").write_text("do not store SSNs\n", encoding="utf-8")
    before = _tree_hash(src)
    archive = base / "desk.tgz"
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(src, arcname="src")
    dest = base / "restore"
    if dest.exists():
        for p in dest.rglob("*"):
            if p.is_file():
                p.unlink()
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive, "r:gz") as tar:
        try:
            tar.extractall(dest, filter="data")
        except TypeError:
            tar.extractall(dest)
    after = _tree_hash(dest / "src")
    return archive, after if after == before else ""


# ---------------------------------------------------------------------------
# GENERAL IT
# ---------------------------------------------------------------------------

def lab_os_users(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data = fixture
    pre: list[dict[str, Any]] = []
    if data is None:
        data, pre = _require_student("lab_os_users", "GENERAL_IT", submission, ["users"], "")
        if data is None:
            return _result("lab_os_users", "GENERAL_IT", pre, "Local fixture user store. Not a live directory service.")
    users = data.get("users") or {}
    req = data.get("required") or {
        "kiosk": {"sudo": False, "groups_must_not_contain": ["sudo", "root"]},
        "desk.lead": {"groups_must_contain": ["helpdesk"]},
    }
    checks = list(pre)
    checks.append(_check("kiosk_exists", "kiosk" in users, "kiosk account present"))
    checks.append(_check("kiosk_no_sudo", users.get("kiosk", {}).get("sudo") is False, "kiosk must not have sudo"))
    bad = set(req["kiosk"]["groups_must_not_contain"]) & set(users.get("kiosk", {}).get("groups", []))
    checks.append(_check("kiosk_not_rootish", not bad, f"forbidden groups={sorted(bad)}"))
    lead_groups = set(users.get("desk.lead", {}).get("groups", []))
    checks.append(_check("lead_in_helpdesk", "helpdesk" in lead_groups, f"groups={sorted(lead_groups)}"))
    homes = {u.get("home") for u in users.values() if isinstance(u, dict)}
    checks.append(_check("unique_homes", len(homes) == len(users) and None not in homes, "each account needs its own home"))
    uids = [u.get("uid") for u in users.values() if isinstance(u, dict)]
    checks.append(_check("unique_uids", len(set(uids)) == len(uids) and None not in uids, "UIDs collide"))
    return _result("lab_os_users", "GENERAL_IT", checks, "Local fixture user store. Not a live directory service.")


def lab_services(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    units = fixture
    pre: list[dict[str, Any]] = []
    if units is None:
        data, pre = _require_student("lab_services", "GENERAL_IT", submission, ["units"], "")
        if data is None:
            return _result("lab_services", "GENERAL_IT", pre, "Mock service table. Not systemd on a real host.")
        units = data["units"]
    checks = list(pre)
    cupsd = units.get("cupsd") or {}
    sshd = units.get("sshd") or {}
    tracker = units.get("toy-tracker") or {}
    checks.append(_check("cupsd_running", cupsd.get("enabled") and cupsd.get("active"), "print spooler down"))
    checks.append(_check("sshd_running", sshd.get("active"), "remote admin path down"))
    checks.append(_check("tracker_off", not tracker.get("active"), "classroom image forbids toy-tracker"))
    checks.append(_check("cupsd_restart_budget", int(cupsd.get("restart_sec") or 99) <= 15, "restart loop too slow for kiosk"))
    return _result("lab_services", "GENERAL_IT", checks, "Mock service table. Not systemd on a real host.")


def lab_storage(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    vol = fixture
    pre: list[dict[str, Any]] = []
    if vol is None:
        data, pre = _require_student("lab_storage", "GENERAL_IT", submission, ["size_bytes", "used_bytes", "reserved_bytes", "free_ratio"], "")
        if data is None:
            return _result("lab_storage", "GENERAL_IT", pre, "Arithmetic on a fixture volume. Not a live block device.")
        vol = data
    checks = list(pre)
    size = int(vol["size_bytes"])
    used = int(vol["used_bytes"])
    reserved = int(vol["reserved_bytes"])
    free = size - used - reserved
    ratio = free / size if size else 0.0
    student_ratio = float(vol.get("free_ratio", -1))
    min_free = float(vol.get("min_free_ratio", 0.15))
    checks.append(_check("free_nonneg", free >= 0, f"free={free}"))
    checks.append(_check("min_free", ratio + 1e-12 >= min_free, f"free_ratio={ratio:.4f}"))
    checks.append(_check("used_lt_size", used < size, "used exceeds disk"))
    checks.append(_check("student_ratio", abs(student_ratio - ratio) < 1e-6, f"student={student_ratio} computed={ratio:.6f}"))
    return _result("lab_storage", "GENERAL_IT", checks, "Arithmetic on a fixture volume. Not a live block device.")


def lab_dns_hosts(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data = fixture
    pre: list[dict[str, Any]] = []
    if data is None:
        data, pre = _require_student("lab_dns_hosts", "GENERAL_IT", submission, ["answers"], "")
        if data is None:
            return _result("lab_dns_hosts", "GENERAL_IT", pre, "Static hosts/zone fixture. Not recursive Internet DNS.")
    checks = list(pre)
    oracle = {
        "desk.gary.waike.local": "10.20.30.14",
        "printer.gary.waike.local": "10.20.30.40",
        "library.gary.waike.local": "10.20.30.21",
        "example.com": None,
    }
    answers = data.get("answers") or {}
    for name, expect in oracle.items():
        got = answers.get(name, "__missing__")
        if expect is None:
            checks.append(_check(f"resolve:{name}", got in (None, "", "nxdomain"), f"got={got}"))
        else:
            checks.append(_check(f"resolve:{name}", got == expect, f"got={got} expect={expect}"))
    return _result("lab_dns_hosts", "GENERAL_IT", checks, "Static hosts/zone fixture. Not recursive Internet DNS.")


def lab_backup(work: Path | None = None, submission: Any = None) -> LabResult:
    archive, expected_hash = _backup_tree(work)
    data, pre = _require_student("lab_backup", "GENERAL_IT", submission, ["restored_hash", "includes_ssn"], "")
    if data is None:
        return _result("lab_backup", "GENERAL_IT", pre, "Local tar+sha256. Not a production backup appliance.")
    checks = list(pre)
    checks.append(_check("archive_exists", archive.is_file() and archive.stat().st_size > 0, str(archive)))
    checks.append(_check("hash_match", bool(expected_hash) and data.get("restored_hash") == expected_hash,
                         f"student={str(data.get('restored_hash'))[:12]} expect={expected_hash[:12]}"))
    checks.append(_check("no_ssn_file", data.get("includes_ssn") is False, "PII file must not be in the lab tree"))
    return _result("lab_backup", "GENERAL_IT", checks, "Local tar+sha256. Not a production backup appliance.")


def lab_ticket_queue(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    tickets = fixture
    pre: list[dict[str, Any]] = []
    if tickets is None:
        data, pre = _require_student("lab_ticket_queue", "GENERAL_IT", submission, ["tickets"], "")
        if data is None:
            return _result("lab_ticket_queue", "GENERAL_IT", pre, "Synthetic tickets. No real patron PII.")
        tickets = data["tickets"]
    allowed_next = {
        "4417": "adjust_idle_or_save_prompt",
        "4418": "capture_temps_then_reseating_plan",
        "4419": "check_hosts_then_spooler",
    }
    checks = list(pre)
    by_id = {t.get("id"): t for t in tickets if isinstance(t, dict)}
    for tid, nxt in allowed_next.items():
        t = by_id.get(tid) or {}
        checks.append(_check(f"{tid}_not_reboot", t.get("next") != "reboot_and_hope", "reboot is not a root cause"))
        checks.append(_check(f"{tid}_next", t.get("next") == nxt, str(t.get("next"))))
        checks.append(_check(f"{tid}_sev", t.get("severity") in {"se1", "se2", "se3", "se4"}, str(t.get("severity"))))
    idle = (by_id.get("4417") or {}).get("idle_logout_sec")
    checks.append(_check("4417_idle_math", idle == 20 * 60, "20 minutes is 1200 seconds"))
    return _result("lab_ticket_queue", "GENERAL_IT", checks, "Synthetic tickets. No real patron PII.")


def lab_automation_runbook(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    run = fixture
    pre: list[dict[str, Any]] = []
    if run is None:
        data, pre = _require_student("lab_automation_runbook", "GENERAL_IT", submission,
                                    ["change_id", "planned_min", "steps", "rollback", "executed"], "")
        if data is None:
            return _result("lab_automation_runbook", "GENERAL_IT", pre, "Dry-run change record. Not unattended production automation.")
        run = data
    window_start = int(run.get("window_start_min", 18 * 60))
    window_end = int(run.get("window_end_min", 21 * 60))
    planned = int(run.get("planned_min", -1))
    steps = list(run.get("steps") or [])
    in_window = window_start <= planned <= window_end
    checks = list(pre)
    checks.append(_check("three_steps", len(steps) >= 3, str(steps)))
    checks.append(_check("rollback_named", bool(run.get("rollback")), "missing rollback"))
    checks.append(_check("in_window", in_window, f"planned={planned}"))
    checks.append(_check("executed_matches", list(run.get("executed") or []) == steps, "dry-run drifted"))
    checks.append(_check("snapshot_first", bool(steps) and str(steps[0]).startswith("snapshot"), "no snapshot before mutate"))
    return _result("lab_automation_runbook", "GENERAL_IT", checks, "Dry-run change record. Not unattended production automation.")


# ---------------------------------------------------------------------------
# NETWORKING
# ---------------------------------------------------------------------------

def lab_cidr_math(fixture: Any = None, submission: Any = None) -> LabResult:
    cases = fixture
    pre: list[dict[str, Any]] = []
    if cases is None:
        data, pre = _require_student("lab_cidr_math", "COMPUTER_NETWORKING", submission, ["cases"], "")
        if data is None:
            return _result("lab_cidr_math", "COMPUTER_NETWORKING", pre, "IPv4 arithmetic. Not a Cisco simulator.")
        cases = data["cases"]
    checks = list(pre)
    for c in cases:
        net = ipaddress.IPv4Network(c["cidr"], strict=False)
        usable = int(net.num_addresses) - 2 if net.prefixlen <= 30 else 0
        if net.prefixlen == 31:
            usable = 2
        checks.append(_check(f"{c['cidr']}_net", str(net.network_address) == c.get("network"), str(net.network_address)))
        checks.append(_check(f"{c['cidr']}_bcast", str(net.broadcast_address) == c.get("broadcast"), str(net.broadcast_address)))
        checks.append(_check(f"{c['cidr']}_usable", usable == c.get("usable"), f"usable={usable}"))
    return _result("lab_cidr_math", "COMPUTER_NETWORKING", checks, "IPv4 arithmetic. Not a Cisco simulator.")


def lab_datapath(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    """Deep protocol/data-path lab: parse crafted Ethernet+IPv4, LPM, real TTL=1 drop."""
    data, pre = _require_student(
        "lab_datapath", "COMPUTER_NETWORKING", submission,
        ["dst_mac", "ethertype", "ttl", "proto", "dst_ip", "lpm_iface", "ttl1_forwarded", "ttl1_after_decrement"],
        "",
    )
    frame = _craft_frame(ttl=4)
    parsed = _parse_ipv4_frame(frame)
    table = (fixture or {}).get("table") if fixture else None
    table = table or [
        {"prefix": "10.20.40.0/24", "nh": "10.20.30.1", "iface": "eth1"},
        {"prefix": "10.20.0.0/16", "nh": "10.20.30.254", "iface": "eth0"},
        {"prefix": "0.0.0.0/0", "nh": "192.0.2.1", "iface": "wan0"},
    ]
    route = _lpm(table, parsed["dst"])
    ttl1_frame = _craft_frame(ttl=1)
    ttl1 = _parse_ipv4_frame(ttl1_frame)
    ttl1_after = int(ttl1["ttl"]) - 1  # decrement the parsed header byte, not a tautology
    checks = list(pre)
    if data is None:
        checks.append(_check("ttl1_from_parsed_header", False, "no student parse of TTL=1 frame"))
        return _result("lab_datapath", "COMPUTER_NETWORKING", checks,
                       "Classroom-crafted frame. Not a packet capture from production. Original WAIKE datapath, not CS144 code.")
    checks += [
        _check("ethertype_ipv4", parsed["ethertype"] == 0x0800 and data.get("ethertype") in (0x0800, 2048, "0x0800"), hex(parsed["ethertype"])),
        _check("ipv4_version", parsed["version"] == 4 and parsed["ihl"] == 5, f"ver={parsed['version']} ihl={parsed['ihl']}"),
        _check("tcp", parsed["proto"] == 6 and int(data.get("proto", -1)) == 6, f"proto={parsed['proto']}"),
        _check("dst_mac_unicast", parsed["dst_mac"] == "aaaaaaaaaa01" and str(data.get("dst_mac", "")).replace(":", "") == "aaaaaaaaaa01", parsed["dst_mac"]),
        _check("student_ttl", int(data.get("ttl", -1)) == parsed["ttl"], f"student={data.get('ttl')} header={parsed['ttl']}"),
        _check("student_dst", str(data.get("dst_ip")) == parsed["dst"], f"student={data.get('dst_ip')}"),
        _check("ttl_positive_after_dec", parsed["ttl"] - 1 > 0, f"ttl={parsed['ttl']}"),
        _check("lpm_more_specific", route.get("iface") == "eth1" and data.get("lpm_iface") == "eth1", str(route)),
        _check("nh", route.get("nh") == "10.20.30.1", str(route)),
    ]
    table2 = table + [{"prefix": "10.20.40.9/32", "nh": "10.20.30.9", "iface": "host9"}]
    r2 = _lpm(table2, parsed["dst"])
    checks.append(_check("lpm_host_route", r2.get("iface") == "host9", str(r2)))
    checks.append(_check("ttl1_parsed_from_header", ttl1["ttl"] == 1, f"header_ttl={ttl1['ttl']}"))
    checks.append(_check("ttl1_decrement", ttl1_after == 0, f"parsed_ttl={ttl1['ttl']} after={ttl1_after}"))
    checks.append(_check(
        "ttl1_drop",
        ttl1_after == 0 and data.get("ttl1_forwarded") is False and int(data.get("ttl1_after_decrement", -1)) == 0,
        f"student_forwarded={data.get('ttl1_forwarded')} student_after={data.get('ttl1_after_decrement')} header_after={ttl1_after}",
    ))
    return _result("lab_datapath", "COMPUTER_NETWORKING", checks,
                   "Classroom-crafted frame. Not a packet capture from production. Original WAIKE datapath, not CS144 code.")


def lab_vlan_mac(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_vlan_mac", "COMPUTER_NETWORKING", submission, ["out_port", "vlan30_leak"], "")
    if data is None:
        return _result("lab_vlan_mac", "COMPUTER_NETWORKING", pre, "Toy MAC/VLAN table. Not a live switch.")
    mac_table = {
        ("aa:aa:aa:aa:aa:10", 20): "Gi1/0/8",
        ("aa:aa:aa:aa:aa:11", 30): "Gi1/0/9",
    }
    out = mac_table.get(("aa:aa:aa:aa:aa:10", 20))
    miss = mac_table.get(("aa:aa:aa:aa:aa:10", 30))
    checks = list(pre) + [
        _check("hit_vlan20", out == "Gi1/0/8" and data.get("out_port") == "Gi1/0/8", str(out)),
        _check("vlan_isolation", miss is None and data.get("vlan30_leak") in (None, "", "none", False), "MAC must not leak across VLAN 30"),
    ]
    return _result("lab_vlan_mac", "COMPUTER_NETWORKING", checks, "Toy MAC/VLAN table. Not a live switch.")


def lab_spf_routing(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_spf_routing", "COMPUTER_NETWORKING", submission, ["cost_a_to_d", "path"], "")
    if data is None:
        return _result("lab_spf_routing", "COMPUTER_NETWORKING", pre, "Four-node SPF. Not OSPF packet exchange with a vendor NOS.")
    edges = {
        ("A", "B"): 2, ("B", "A"): 2, ("B", "D"): 2, ("D", "B"): 2,
        ("A", "C"): 5, ("C", "A"): 5, ("C", "D"): 5, ("D", "C"): 5,
        ("B", "C"): 9, ("C", "B"): 9,
    }
    nodes = sorted({n for e in edges for n in e})

    def dijkstra(src: str) -> dict[str, float]:
        dist = {n: float("inf") for n in nodes}
        dist[src] = 0.0
        remaining = set(nodes)
        while remaining:
            u = min(remaining, key=lambda x: dist[x])
            remaining.remove(u)
            for v in nodes:
                w = edges.get((u, v))
                if w is None:
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist

    d = dijkstra("A")
    checks = list(pre) + [
        _check("path_cost_ad", d["D"] == 4 and int(data.get("cost_a_to_d", -1)) == 4, f"dist={d}"),
        _check("not_long_way", d["D"] < 10, "A-C-D must lose"),
        _check("self_zero", d["A"] == 0, str(d["A"])),
        _check("path_abd", str(data.get("path")).replace(" ", "").upper() in {"A-B-D", "ABD", "A→B→D"}, str(data.get("path"))),
    ]
    return _result("lab_spf_routing", "COMPUTER_NETWORKING", checks, "Four-node SPF. Not OSPF packet exchange with a vendor NOS.")


def lab_nat_acl(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_nat_acl", "COMPUTER_NETWORKING", submission, ["telnet", "https", "discard", "nat_inside"], "")
    if data is None:
        return _result("lab_nat_acl", "COMPUTER_NETWORKING", pre, "Ordered ACL on a fixture. Not a live firewall.")
    acl = [
        {"action": "deny", "dport": 23},
        {"action": "permit", "dport": 443},
        {"action": "deny", "dport": "*"},
    ]

    def decide(dport: int) -> str:
        for rule in acl:
            if rule["dport"] in {dport, "*"}:
                return rule["action"]
        return "deny"

    checks = list(pre) + [
        _check("telnet_denied", decide(23) == "deny" and data.get("telnet") == "deny", "telnet must die at the edge"),
        _check("https_ok", decide(443) == "permit" and data.get("https") == "permit", "library HTTPS must pass"),
        _check("unknown_denied", decide(9) == "deny" and data.get("discard") == "deny", "implicit deny via star rule"),
        _check("nat_maps", str(data.get("nat_inside", "")).startswith("10."), str(data.get("nat_inside"))),
    ]
    return _result("lab_nat_acl", "COMPUTER_NETWORKING", checks, "Ordered ACL on a fixture. Not a live firewall.")


def lab_dns_resolution(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_dns_resolution", "COMPUTER_NETWORKING", submission, ["first_how", "second_how", "ip"], "")
    if data is None:
        return _result("lab_dns_resolution", "COMPUTER_NETWORKING", pre, "Toy resolver. Not a public recursive service.")
    cache: dict[str, str] = {}
    auth = {"desk.gary.waike.example": "203.0.113.14"}
    name = "desk.gary.waike.example"

    def resolve(n: str) -> tuple[str, str]:
        if n in cache:
            return cache[n], "cache"
        if n in auth:
            cache[n] = auth[n]
            return auth[n], "auth_walk"
        return "", "nxdomain"

    ip1, how1 = resolve(name)
    ip2, how2 = resolve(name)
    checks = list(pre) + [
        _check("first_walk", how1 == "auth_walk" and ip1 == "203.0.113.14" and data.get("first_how") == "auth_walk", f"{how1}:{ip1}"),
        _check("second_cache", how2 == "cache" and ip2 == ip1 and data.get("second_how") == "cache", f"{how2}:{ip2}"),
        _check("ip", data.get("ip") == "203.0.113.14", str(data.get("ip"))),
    ]
    return _result("lab_dns_resolution", "COMPUTER_NETWORKING", checks, "Toy resolver. Not a public recursive service.")


# ---------------------------------------------------------------------------
# CYBER — authorized fixtures only
# ---------------------------------------------------------------------------

def lab_siem_triage(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_siem_triage", "CYBERSECURITY", submission, ["bursts", "note"], SANDBOX_NOTE)
    lines = (fixture or {}).get("lines") if fixture else None
    lines = lines or [
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_OK user=bea src=10.20.30.8",
        "AUTH_FAIL user=cal src=10.20.30.9",
    ]
    threshold = int((fixture or {}).get("threshold", 3)) if fixture else 3
    counts: dict[str, int] = {}
    for line in lines:
        if "AUTH_FAIL" not in line:
            continue
        m = re.search(r"user=([a-z0-9._-]+)", line)
        if m:
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    bursts = sorted(u for u, n in counts.items() if n >= threshold)
    checks = list(pre)
    if data is None:
        checks.append(_check("no_attacker_word", False, "no incident note to inspect"))
        return _result("lab_siem_triage", "CYBERSECURITY", checks, SANDBOX_NOTE)
    note = str(data.get("note") or "")
    note_l = note.lower()
    student_bursts = data.get("bursts") or []
    if isinstance(student_bursts, str):
        student_bursts = [student_bursts]
    checks.append(_check("ada_burst", bursts == ["ada"] and list(student_bursts) == ["ada"], f"bursts={bursts} counts={counts}"))
    checks.append(_check(
        "no_attacker_word",
        "burst" in note_l and "attacker" not in note_l,
        f"note must contain burst and must not say attacker; note={note[:80]!r}",
    ))
    checks.append(_check("cal_under", counts.get("cal", 0) < threshold, str(counts)))
    return _result("lab_siem_triage", "CYBERSECURITY", checks, SANDBOX_NOTE)


def lab_hardening_baseline(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    image = fixture
    pre: list[dict[str, Any]] = []
    if image is None:
        data, pre = _require_student(
            "lab_hardening_baseline", "CYBERSECURITY", submission,
            ["guest_login", "ssh_password_auth", "unattended_upgrades", "open_ports", "world_writable_home", "ai_agent_sudo"],
            SANDBOX_NOTE,
        )
        if data is None:
            return _result("lab_hardening_baseline", "CYBERSECURITY", pre, SANDBOX_NOTE)
        image = data
    checks = list(pre) + [
        _check("no_guest", image.get("guest_login") is False, "guest login"),
        _check("ssh_keys_only", image.get("ssh_password_auth") is False, "password SSH"),
        _check("patch_pipe", image.get("unattended_upgrades") is True, "no patch pipe"),
        _check("ports", set(image.get("open_ports") or []) <= {22, 443}, str(image.get("open_ports"))),
        _check("home_mode", image.get("world_writable_home") is False, "home is 777"),
        _check("no_ai_sudo", image.get("ai_agent_sudo") is False, "non-human identity must not have sudo"),
    ]
    return _result("lab_hardening_baseline", "CYBERSECURITY", checks, SANDBOX_NOTE)


def lab_iam_rbac(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    policy = fixture
    pre: list[dict[str, Any]] = []
    if policy is None:
        data, pre = _require_student("lab_iam_rbac", "CYBERSECURITY", submission, ["roles", "bindings"], SANDBOX_NOTE)
        if data is None:
            return _result("lab_iam_rbac", "CYBERSECURITY", pre, SANDBOX_NOTE)
        policy = data

    def allow(user: str, action: str) -> bool:
        try:
            role = policy["bindings"][user]
            return action in policy["roles"][role]["actions"]
        except (KeyError, TypeError):
            return False

    checks = list(pre) + [
        _check("analyst_read", allow("naiya", "case.read"), "analyst should read"),
        _check("analyst_no_close", not allow("naiya", "case.close"), "analyst closed a case"),
        _check("lead_close", allow("omar", "case.close"), "lead cannot close"),
        _check("bot_no_close", not allow("harbor-bot", "case.close"), "bot must not close"),
    ]
    return _result("lab_iam_rbac", "CYBERSECURITY", checks, SANDBOX_NOTE)


def lab_segmentation_zones(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student(
        "lab_segmentation_zones", "CYBERSECURITY", submission,
        ["kiosk_to_soc", "soc_to_kiosk", "guest_to_staff"],
        SANDBOX_NOTE,
    )
    if data is None:
        return _result("lab_segmentation_zones", "CYBERSECURITY", pre, SANDBOX_NOTE)
    checks = list(pre) + [
        _check("kiosk_no_soc", data.get("kiosk_to_soc") == "deny", "east-west hole"),
        _check("soc_syslog", data.get("soc_to_kiosk") == "allow_syslog_only", str(data.get("soc_to_kiosk"))),
        _check("guest_staff", data.get("guest_to_staff") == "deny", "guest jumped to staff"),
    ]
    return _result("lab_segmentation_zones", "CYBERSECURITY", checks, SANDBOX_NOTE)


def lab_incident_playbook(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_incident_playbook", "CYBERSECURITY", submission, ["steps"], SANDBOX_NOTE)
    if data is None:
        return _result("lab_incident_playbook", "CYBERSECURITY", pre, SANDBOX_NOTE)
    steps = list(data.get("steps") or [])
    clock = ["detect", "contain", "eradicate", "recover", "lessons"]
    checks = list(pre)
    checks.append(_check("order", steps == clock, f"got={steps}"))
    if "contain" in steps and "eradicate" in steps:
        checks.append(_check("contain_before_wipe", steps.index("contain") < steps.index("eradicate"), "wiped before contain"))
    else:
        checks.append(_check("contain_before_wipe", False, "missing steps"))
    checks.append(_check("lessons_last", bool(steps) and steps[-1] == "lessons", "no retro"))
    return _result("lab_incident_playbook", "CYBERSECURITY", checks, SANDBOX_NOTE)


def _unsafe_len_parser(buf: bytes) -> bytes:
    if not buf:
        return b""
    claimed = buf[0]
    return buf[1:1 + claimed]


def _safe_len_parser(buf: bytes) -> bytes:
    if not buf:
        return b""
    claimed = buf[0]
    available = len(buf) - 1
    if claimed > available:
        raise ValueError("oversize length byte")
    return buf[1:1 + claimed]


def lab_safe_vuln_detect(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    """Authorized course CTF: detect the length lie; do not exploit real software."""
    data, pre = _require_student(
        "lab_safe_vuln_detect", "CYBERSECURITY", submission,
        ["targets", "safe_rejects_lie", "honest_payload"],
        SANDBOX_NOTE,
    )
    opened: list[Any] = []
    real_socket = socket.socket

    def _guard(*a: Any, **k: Any) -> Any:
        opened.append((a, k))
        raise OSError("course lab must not open sockets")

    socket.socket = _guard  # type: ignore[misc, assignment]
    try:
        oversize = bytes([20]) + b"short"
        ok_msg = bytes([4]) + b"abcd"
        unsafe_got = _unsafe_len_parser(oversize)
        safe_ok = _safe_len_parser(ok_msg)
        safe_raised = False
        try:
            _safe_len_parser(oversize)
        except ValueError:
            safe_raised = True
    finally:
        socket.socket = real_socket  # type: ignore[misc]

    checks = list(pre)
    if data is None:
        checks.append(_check("no_network", False, "no student targets declared"))
        return _result("lab_safe_vuln_detect", "CYBERSECURITY", checks, SANDBOX_NOTE)
    targets = data.get("targets")
    if isinstance(targets, str):
        targets = [targets]
    checks += [
        _check("unsafe_truncates_or_overreads_pattern", len(unsafe_got) < 20, "fixture did not demonstrate the lie"),
        _check("safe_accepts_honest", safe_ok == b"abcd" and data.get("honest_payload") == "abcd", str(data.get("honest_payload"))),
        _check("safe_rejects_lie", safe_raised and data.get("safe_rejects_lie") is True, "safe parser accepted oversize claim"),
        _check(
            "no_network",
            len(opened) == 0 and list(targets or []) == ["course_ctf_fixture"],
            f"opened={len(opened)} targets={targets}",
        ),
    ]
    return _result("lab_safe_vuln_detect", "CYBERSECURITY", checks, SANDBOX_NOTE)


def lab_forensics_timeline(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    data, pre = _require_student("lab_forensics_timeline", "CYBERSECURITY", submission, ["first_event", "cannot_claim_identity"], SANDBOX_NOTE)
    events = [
        {"t": 100, "ev": "usb_insert", "dev": "sdb1"},
        {"t": 140, "ev": "file_copy", "path": "/media/sdb1/essay.docx"},
        {"t": 155, "ev": "usb_unmount", "dev": "sdb1"},
        {"t": 90, "ev": "login", "user": "kiosk"},
    ]
    ordered = sorted(events, key=lambda e: e["t"])
    kinds = [e["ev"] for e in ordered]
    checks = list(pre)
    if data is None:
        return _result("lab_forensics_timeline", "CYBERSECURITY", checks, SANDBOX_NOTE)
    checks += [
        _check("login_first", kinds[0] == "login" and data.get("first_event") == "login", str(kinds)),
        _check("copy_between", kinds.index("usb_insert") < kinds.index("file_copy") < kinds.index("usb_unmount"), str(kinds)),
        _check("no_secret_in_path", all("password" not in json.dumps(e) for e in events), "secret in fixture"),
        _check("cannot_claim", data.get("cannot_claim_identity") is True, "fixture does not identify the human"),
    ]
    return _result("lab_forensics_timeline", "CYBERSECURITY", checks, SANDBOX_NOTE)


LABS: dict[str, Callable[..., LabResult]] = {
    "lab_os_users": lab_os_users,
    "lab_services": lab_services,
    "lab_storage": lab_storage,
    "lab_dns_hosts": lab_dns_hosts,
    "lab_backup": lab_backup,
    "lab_ticket_queue": lab_ticket_queue,
    "lab_automation_runbook": lab_automation_runbook,
    "lab_cidr_math": lab_cidr_math,
    "lab_datapath": lab_datapath,
    "lab_vlan_mac": lab_vlan_mac,
    "lab_spf_routing": lab_spf_routing,
    "lab_nat_acl": lab_nat_acl,
    "lab_dns_resolution": lab_dns_resolution,
    "lab_siem_triage": lab_siem_triage,
    "lab_hardening_baseline": lab_hardening_baseline,
    "lab_iam_rbac": lab_iam_rbac,
    "lab_segmentation_zones": lab_segmentation_zones,
    "lab_incident_playbook": lab_incident_playbook,
    "lab_safe_vuln_detect": lab_safe_vuln_detect,
    "lab_forensics_timeline": lab_forensics_timeline,
}

COURSE_LABS = {
    "GENERAL_IT": [
        "lab_os_users",
        "lab_services",
        "lab_storage",
        "lab_dns_hosts",
        "lab_backup",
        "lab_ticket_queue",
        "lab_automation_runbook",
    ],
    "COMPUTER_NETWORKING": [
        "lab_cidr_math",
        "lab_datapath",
        "lab_vlan_mac",
        "lab_spf_routing",
        "lab_nat_acl",
        "lab_dns_resolution",
    ],
    "CYBERSECURITY": [
        "lab_siem_triage",
        "lab_hardening_baseline",
        "lab_iam_rbac",
        "lab_segmentation_zones",
        "lab_incident_playbook",
        "lab_safe_vuln_detect",
        "lab_forensics_timeline",
    ],
}


def _ref_users() -> dict[str, Any]:
    return {
        "users": {
            "root": {"uid": 0, "groups": ["root"], "sudo": True, "home": "/root"},
            "kiosk": {"uid": 1010, "groups": ["kiosk"], "sudo": False, "home": "/home/kiosk"},
            "desk.lead": {"uid": 1020, "groups": ["helpdesk", "staff"], "sudo": True, "home": "/home/desk.lead"},
        }
    }


REFERENCE: dict[str, dict[str, Any]] = {
    "lab_os_users": _ref_users(),
    "lab_services": {"units": {
        "cupsd": {"enabled": True, "active": True, "restart_sec": 8},
        "sshd": {"enabled": True, "active": True, "restart_sec": 2},
        "toy-tracker": {"enabled": False, "active": False, "restart_sec": 0},
    }},
    "lab_storage": {
        "size_bytes": 256 * 1024 ** 3,
        "used_bytes": 180 * 1024 ** 3,
        "reserved_bytes": 12 * 1024 ** 3,
        "min_free_ratio": 0.15,
        "free_ratio": (256 * 1024 ** 3 - 180 * 1024 ** 3 - 12 * 1024 ** 3) / (256 * 1024 ** 3),
    },
    "lab_dns_hosts": {"answers": {
        "desk.gary.waike.local": "10.20.30.14",
        "printer.gary.waike.local": "10.20.30.40",
        "library.gary.waike.local": "10.20.30.21",
        "example.com": "nxdomain",
    }},
    "lab_backup": {"restored_hash": "PENDING", "includes_ssn": False},
    "lab_ticket_queue": {"tickets": [
        {"id": "4417", "idle_logout_sec": 1200, "severity": "se3", "next": "adjust_idle_or_save_prompt"},
        {"id": "4418", "severity": "se2", "next": "capture_temps_then_reseating_plan"},
        {"id": "4419", "severity": "se3", "next": "check_hosts_then_spooler"},
    ]},
    "lab_automation_runbook": {
        "change_id": "CHG-88",
        "window_start_min": 18 * 60,
        "window_end_min": 21 * 60,
        "planned_min": 19 * 60 + 15,
        "steps": ["snapshot_home", "apply_idle_policy", "verify_kiosk_login"],
        "rollback": "restore_snapshot_home",
        "executed": ["snapshot_home", "apply_idle_policy", "verify_kiosk_login"],
    },
    "lab_cidr_math": {"cases": [
        {"cidr": "10.20.30.40/26", "network": "10.20.30.0", "broadcast": "10.20.30.63", "usable": 62},
        {"cidr": "10.20.30.80/28", "network": "10.20.30.80", "broadcast": "10.20.30.95", "usable": 14},
    ]},
    "lab_datapath": {
        "dst_mac": "aaaaaaaaaa01",
        "ethertype": 0x0800,
        "ttl": 4,
        "proto": 6,
        "dst_ip": "10.20.40.9",
        "lpm_iface": "eth1",
        "ttl1_forwarded": False,
        "ttl1_after_decrement": 0,
    },
    "lab_vlan_mac": {"out_port": "Gi1/0/8", "vlan30_leak": False},
    "lab_spf_routing": {"cost_a_to_d": 4, "path": "A-B-D"},
    "lab_nat_acl": {"telnet": "deny", "https": "permit", "discard": "deny", "nat_inside": "10.20.30.14"},
    "lab_dns_resolution": {"first_how": "auth_walk", "second_how": "cache", "ip": "203.0.113.14"},
    "lab_siem_triage": {"bursts": ["ada"], "note": "burst on ada — look, do not convict"},
    "lab_hardening_baseline": {
        "guest_login": False,
        "ssh_password_auth": False,
        "unattended_upgrades": True,
        "open_ports": [22, 443],
        "world_writable_home": False,
        "ai_agent_sudo": False,
    },
    "lab_iam_rbac": {
        "roles": {
            "analyst": {"actions": ["case.read", "case.comment"]},
            "lead": {"actions": ["case.read", "case.comment", "case.close"]},
            "ai.triage.bot": {"actions": ["case.read"]},
        },
        "bindings": {"naiya": "analyst", "omar": "lead", "harbor-bot": "ai.triage.bot"},
    },
    "lab_segmentation_zones": {"kiosk_to_soc": "deny", "soc_to_kiosk": "allow_syslog_only", "guest_to_staff": "deny"},
    "lab_incident_playbook": {"steps": ["detect", "contain", "eradicate", "recover", "lessons"]},
    "lab_safe_vuln_detect": {"targets": ["course_ctf_fixture"], "safe_rejects_lie": True, "honest_payload": "abcd"},
    "lab_forensics_timeline": {"first_event": "login", "cannot_claim_identity": True},
}

WRONG: dict[str, dict[str, Any]] = {
    "lab_os_users": {"users": {"kiosk": {"uid": 1010, "groups": ["sudo"], "sudo": True, "home": "/home/kiosk"}}},
    "lab_services": {"units": {
        "cupsd": {"enabled": False, "active": False, "restart_sec": 90},
        "sshd": {"enabled": True, "active": True, "restart_sec": 2},
        "toy-tracker": {"enabled": True, "active": True, "restart_sec": 1},
    }},
    "lab_storage": {
        "size_bytes": 256 * 1024 ** 3,
        "used_bytes": 240 * 1024 ** 3,
        "reserved_bytes": 12 * 1024 ** 3,
        "min_free_ratio": 0.15,
        "free_ratio": 0.50,
    },
    "lab_dns_hosts": {"answers": {"desk.gary.waike.local": "1.1.1.1", "printer.gary.waike.local": "10.20.30.40",
                                  "library.gary.waike.local": "10.20.30.21", "example.com": "8.8.8.8"}},
    "lab_backup": {"restored_hash": "0" * 64, "includes_ssn": True},
    "lab_ticket_queue": {"tickets": [
        {"id": "4417", "idle_logout_sec": 20, "severity": "se3", "next": "reboot_and_hope"},
        {"id": "4418", "severity": "se2", "next": "reboot_and_hope"},
        {"id": "4419", "severity": "se3", "next": "reboot_and_hope"},
    ]},
    "lab_automation_runbook": {
        "change_id": "CHG-88",
        "planned_min": 10 * 60,
        "steps": ["apply_idle_policy", "verify_kiosk_login"],
        "rollback": "",
        "executed": ["verify_kiosk_login"],
    },
    "lab_cidr_math": {"cases": [
        {"cidr": "10.20.30.40/26", "network": "10.20.30.40", "broadcast": "10.20.30.63", "usable": 62},
        {"cidr": "10.20.30.80/28", "network": "10.20.30.80", "broadcast": "10.20.30.95", "usable": 14},
    ]},
    "lab_datapath": {
        "dst_mac": "ffffffffffff",
        "ethertype": 0x0806,
        "ttl": 64,
        "proto": 1,
        "dst_ip": "8.8.8.8",
        "lpm_iface": "wan0",
        "ttl1_forwarded": True,
        "ttl1_after_decrement": 1,
    },
    "lab_vlan_mac": {"out_port": "Gi1/0/9", "vlan30_leak": "Gi1/0/8"},
    "lab_spf_routing": {"cost_a_to_d": 10, "path": "A-C-D"},
    "lab_nat_acl": {"telnet": "permit", "https": "deny", "discard": "permit", "nat_inside": "192.0.2.1"},
    "lab_dns_resolution": {"first_how": "cache", "second_how": "auth_walk", "ip": "0.0.0.0"},
    "lab_siem_triage": {"bursts": ["cal"], "note": "ada is the attacker, close the case"},
    "lab_hardening_baseline": {
        "guest_login": True,
        "ssh_password_auth": True,
        "unattended_upgrades": False,
        "open_ports": [22, 80, 3389],
        "world_writable_home": True,
        "ai_agent_sudo": True,
    },
    "lab_iam_rbac": {
        "roles": {
            "analyst": {"actions": ["case.read"]},
            "lead": {"actions": ["case.close"]},
            "ai.triage.bot": {"actions": ["case.read", "case.close"]},
        },
        "bindings": {"naiya": "analyst", "omar": "lead", "harbor-bot": "ai.triage.bot"},
    },
    "lab_segmentation_zones": {"kiosk_to_soc": "allow", "soc_to_kiosk": "allow", "guest_to_staff": "allow"},
    "lab_incident_playbook": {"steps": ["eradicate", "detect", "contain", "recover", "lessons"]},
    "lab_safe_vuln_detect": {"targets": ["10.0.0.1"], "safe_rejects_lie": False, "honest_payload": "shellcode"},
    "lab_forensics_timeline": {"first_event": "usb_insert", "cannot_claim_identity": False},
}


LAB_SPECS: dict[str, dict[str, Any]] = {
    "lab_os_users": {
        "title": "Civic kiosk accounts",
        "readme": "Build a three-account desk store. `kiosk` must not be in sudo/root. `desk.lead` must sit in helpdesk. Unique UID and home. Submitting nothing, or cloning UID 1020 onto sat.am, fails.",
        "required_keys": ["users"],
        "wrong_hint": "A kiosk with sudo=true is an automatic fail (same as the package negative).",
    },
    "lab_services": {
        "title": "Spooler and tracker",
        "readme": "cupsd must be enabled+active with restart_sec ≤ 15. toy-tracker must be dead. This is the Civic image, not a generic 'enable a service' worksheet.",
        "required_keys": ["units"],
        "wrong_hint": "Leaving toy-tracker active fails the classroom image.",
    },
    "lab_storage": {
        "title": "Civic volume free ratio",
        "readme": "Compute free = size - used - reserved on the 256 GiB civic volume. Policy is 15% free. You must submit the ratio you computed; a guessed 0.50 fails.",
        "required_keys": ["size_bytes", "used_bytes", "reserved_bytes", "free_ratio"],
        "wrong_hint": "210+12 on 256 GiB is under 15% — do not mark pass.",
    },
    "lab_dns_hosts": {
        "title": "Split-horizon civic names",
        "readme": "Answer desk/printer/library from the staff horizon. example.com must be nxdomain in this fixture resolver.",
        "required_keys": ["answers"],
        "wrong_hint": "Inventing 8.8.8.8 for example.com fails no_public_leak.",
    },
    "lab_backup": {
        "title": "Checksummed civic archive",
        "readme": "Hash the restored civic tree (ticket_4417.txt + notes.md). Submit SHA256. includes_ssn must be false. An empty hash or 64 zeros fails.",
        "required_keys": ["restored_hash", "includes_ssn"],
        "wrong_hint": "A hash that does not match the restored tree fails even if the tar exists.",
    },
    "lab_ticket_queue": {
        "title": "Tickets 4417/4418/4419",
        "readme": "reboot_and_hope is never a next-action. 4417 idle math is 1200 seconds.",
        "required_keys": ["tickets"],
        "wrong_hint": "Three reboots score three zeros.",
    },
    "lab_automation_runbook": {
        "title": "CHG-88 dry-run",
        "readme": "Snapshot first. Planned minute inside 18:00–21:00. executed must equal steps.",
        "required_keys": ["change_id", "planned_min", "steps", "rollback", "executed"],
        "wrong_hint": "Apply-then-snapshot, or a 10:00 plan, fails.",
    },
    "lab_cidr_math": {
        "title": "Pier /26 and /28",
        "readme": "10.20.30.40/26 network is 10.20.30.0, not .40. Usable 62 and 14. This is bitwise work, not a GUI.",
        "required_keys": ["cases"],
        "wrong_hint": "Using the host address as the network on /26 is the package negative.",
    },
    "lab_datapath": {
        "title": "Crafted Ethernet+IPv4 path",
        "readme": "Parse dest MAC, ethertype, TTL at IP[8], proto, dest IP. LPM must pick the /24 (eth1). Craft a TTL=1 copy of the same header, decrement that byte, and refuse to forward when the result is 0. `(1-1)==0` without parsing is not accepted.",
        "required_keys": ["dst_mac", "ethertype", "ttl", "proto", "dst_ip", "lpm_iface", "ttl1_forwarded", "ttl1_after_decrement"],
        "wrong_hint": "ttl1_forwarded true, or after_decrement 1, fails the drop check.",
    },
    "lab_vlan_mac": {
        "title": "VLAN-aware MAC table",
        "readme": "aa:aa:aa:aa:aa:10 in VLAN 20 exits Gi1/0/8. The same MAC in VLAN 30 is a miss.",
        "required_keys": ["out_port", "vlan30_leak"],
        "wrong_hint": "Leaking the VLAN 20 port into VLAN 30 fails isolation.",
    },
    "lab_spf_routing": {
        "title": "Four-router town SPF",
        "readme": "A-B-D costs 4. A-C-D costs 10. Submit cost_a_to_d=4 and path A-B-D.",
        "required_keys": ["cost_a_to_d", "path"],
        "wrong_hint": "Reporting 10 / A-C-D fails not_long_way.",
    },
    "lab_nat_acl": {
        "title": "Edge ACL and inside NAT",
        "readme": "deny 23, permit 443, deny *. Inside is 10.20.30.14. Order matters.",
        "required_keys": ["telnet", "https", "discard", "nat_inside"],
        "wrong_hint": "permit telnet fails the edge story.",
    },
    "lab_dns_resolution": {
        "title": "Stub then cache",
        "readme": "First lookup walks auth (203.0.113.14). Second is cache.",
        "required_keys": ["first_how", "second_how", "ip"],
        "wrong_hint": "Calling the first hit a cache miss-order fails.",
    },
    "lab_siem_triage": {
        "title": "Harbor AUTH_FAIL bursts",
        "readme": "Count failures. ada ≥ 3 is a burst. Your note must contain the word burst and must not contain attacker. Empty notes fail.",
        "required_keys": ["bursts", "note"],
        "wrong_hint": "A note that says 'ada is the attacker' fails no_attacker_word.",
    },
    "lab_hardening_baseline": {
        "title": "Harbor image baseline",
        "readme": "No guest, no password SSH, unattended upgrades on, ports ⊆ {22,443}, home not 777, ai_agent_sudo false.",
        "required_keys": ["guest_login", "ssh_password_auth", "unattended_upgrades", "open_ports", "world_writable_home", "ai_agent_sudo"],
        "wrong_hint": "ai_agent_sudo true is an automatic baseline fail.",
    },
    "lab_iam_rbac": {
        "title": "Naiya / Omar / harbor-bot",
        "readme": "Analyst reads. Lead closes. Bot cannot close. Submitting a bot with case.close is the package negative.",
        "required_keys": ["roles", "bindings"],
        "wrong_hint": "harbor-bot with case.close fails bot_no_close.",
    },
    "lab_segmentation_zones": {
        "title": "Kiosk / SOC / guest matrix",
        "readme": "kiosk→soc deny. soc→kiosk allow_syslog_only. guest→staff deny.",
        "required_keys": ["kiosk_to_soc", "soc_to_kiosk", "guest_to_staff"],
        "wrong_hint": "Allowing kiosk to SOC is an east-west hole.",
    },
    "lab_incident_playbook": {
        "title": "800-61-shaped clock",
        "readme": "detect → contain → eradicate → recover → lessons. Wipe-before-contain fails.",
        "required_keys": ["steps"],
        "wrong_hint": "Putting eradicate first fails contain_before_wipe.",
    },
    "lab_safe_vuln_detect": {
        "title": "Toy length-prefixed parser",
        "readme": "targets must be exactly [course_ctf_fixture]. Opening a socket during the lab fails no_network. The safe parser must reject an oversize length byte. No shellcode, no campus nmap.",
        "required_keys": ["targets", "safe_rejects_lie", "honest_payload"],
        "wrong_hint": "targets=['10.0.0.1'] fails no_network even if you did not connect.",
    },
    "lab_forensics_timeline": {
        "title": "USB fixture timeline",
        "readme": "Sort by t. First event is login. You cannot claim a named human from this fixture.",
        "required_keys": ["first_event", "cannot_claim_identity"],
        "wrong_hint": "Claiming ada from the USB stick fails cannot_claim.",
    },
}


def reference_submission(lab_id: str) -> dict[str, Any]:
    sub = dict(REFERENCE[lab_id])
    if lab_id == "lab_backup":
        _, digest = _backup_tree()
        sub = {"restored_hash": digest, "includes_ssn": False}
    return sub


def run_lab(lab_id: str, **kwargs: Any) -> dict[str, Any]:
    fn = LABS[lab_id]
    result = fn(**kwargs)
    return result.as_dict()


def _ttl1_from_parsed_header(datapath_result: dict[str, Any]) -> bool:
    names = {c["name"]: c["ok"] for c in datapath_result.get("checks", [])}
    return bool(names.get("ttl1_parsed_from_header") and names.get("ttl1_decrement") and names.get("ttl1_drop"))


def run_all() -> dict[str, Any]:
    results = []
    empty_rows = []
    wrong_rows = []
    for _course, ids in COURSE_LABS.items():
        for lab_id in ids:
            results.append(run_lab(lab_id, submission=reference_submission(lab_id)))
            empty = run_lab(lab_id, submission={})
            empty_rows.append({"lab_id": lab_id, "failed_as_required": (not empty["ok"])})
            wrong = run_lab(lab_id, submission=WRONG[lab_id])
            wrong_rows.append({"lab_id": lab_id, "failed_as_required": (not wrong["ok"])})

    no_sub = run_lab("lab_os_users")
    print_pass_raises = False
    try:
        _fail_if_print_pass("PASS")
    except AssertionError:
        print_pass_raises = True
    try:
        run_lab("lab_siem_triage", submission="PASS")
        print_pass_on_submit = False
    except AssertionError:
        print_pass_on_submit = True

    negatives = []
    bad_users = lab_os_users({
        "users": {"kiosk": {"uid": 1010, "groups": ["sudo"], "sudo": True, "home": "/home/kiosk"}},
        "required": {"kiosk": {"sudo": False, "groups_must_not_contain": ["sudo", "root"]},
                     "desk.lead": {"groups_must_contain": ["helpdesk"]}},
    })
    negatives.append({"lab_id": "lab_os_users_negative", "ok": (not bad_users.ok)})
    bad_lpm = lab_cidr_math([
        {"cidr": "10.20.30.40/26", "network": "10.20.30.40", "broadcast": "10.20.30.63", "usable": 62},
        {"cidr": "10.20.30.80/28", "network": "10.20.30.80", "broadcast": "10.20.30.95", "usable": 14},
    ])
    negatives.append({"lab_id": "lab_cidr_math_negative", "ok": (not bad_lpm.ok)})
    bad_bot = lab_iam_rbac({
        "roles": {"ai.triage.bot": {"actions": ["case.read", "case.close"]}, "analyst": {"actions": ["case.read"]},
                  "lead": {"actions": ["case.close"]}},
        "bindings": {"naiya": "analyst", "omar": "lead", "harbor-bot": "ai.triage.bot"},
    })
    negatives.append({"lab_id": "lab_iam_rbac_negative", "ok": (not bad_bot.ok)})

    datapath = next(r for r in results if r["lab_id"] == "lab_datapath")
    empty_ok = all(r["failed_as_required"] for r in empty_rows)
    wrong_ok = all(r["failed_as_required"] for r in wrong_rows)
    refs_ok = all(r["ok"] for r in results)
    neg_ok = all(n["ok"] for n in negatives)
    ttl_ok = _ttl1_from_parsed_header(datapath)
    ok = refs_ok and empty_ok and wrong_ok and neg_ok and print_pass_raises and print_pass_on_submit and (not no_sub["ok"]) and ttl_ok
    return {
        "ok": ok,
        "lab_count": len(results),
        "results": results,
        "negatives_must_fail_and_did": negatives,
        "empty_submission_fails": empty_ok,
        "wrong_submission_fails": wrong_ok,
        "no_submission_fails": (not no_sub["ok"]),
        "print_pass_raises": print_pass_raises and print_pass_on_submit,
        "ttl1_from_parsed_header": ttl_ok,
        "empty_rows": empty_rows,
        "wrong_rows": wrong_rows,
        "print_pass_forbidden": True,
    }
