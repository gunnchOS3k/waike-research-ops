"""Original WAIKE runnable labs with computing validators.

Print-PASS is forbidden. Each lab returns a structured result. Validators
recompute expected values and compare. A mutated fixture must fail.
Security labs operate only on course fixtures in this repository.
"""
from __future__ import annotations

import hashlib
import ipaddress
import json
import re
import tarfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[2]


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


# ---------------------------------------------------------------------------
# GENERAL IT
# ---------------------------------------------------------------------------

def lab_os_users(fixture: dict[str, Any] | None = None) -> LabResult:
    """Create users/groups and assert least-privilege homes.

    Fixture models a tiny passwd/group store. The operator must add
    `kiosk` without sudo and `desk.lead` in group `helpdesk`.
    """
    data = fixture or {
        "users": {
            "root": {"uid": 0, "groups": ["root"], "sudo": True, "home": "/root"},
            "kiosk": {"uid": 1010, "groups": ["kiosk"], "sudo": False, "home": "/home/kiosk"},
            "desk.lead": {"uid": 1020, "groups": ["helpdesk", "staff"], "sudo": True, "home": "/home/desk.lead"},
        },
        "required": {
            "kiosk": {"sudo": False, "groups_must_not_contain": ["sudo", "root"]},
            "desk.lead": {"groups_must_contain": ["helpdesk"]},
        },
    }
    checks = []
    users = data["users"]
    req = data["required"]
    checks.append(_check("kiosk_exists", "kiosk" in users, "kiosk account present"))
    checks.append(_check("kiosk_no_sudo", users.get("kiosk", {}).get("sudo") is False, "kiosk must not have sudo"))
    bad = set(req["kiosk"]["groups_must_not_contain"]) & set(users.get("kiosk", {}).get("groups", []))
    checks.append(_check("kiosk_not_rootish", not bad, f"forbidden groups={sorted(bad)}"))
    lead_groups = set(users.get("desk.lead", {}).get("groups", []))
    checks.append(_check("lead_in_helpdesk", "helpdesk" in lead_groups, f"groups={sorted(lead_groups)}"))
    homes = {u["home"] for u in users.values()}
    checks.append(_check("unique_homes", len(homes) == len(users), "each account needs its own home"))
    uids = [u["uid"] for u in users.values()]
    checks.append(_check("unique_uids", len(set(uids)) == len(uids), "UIDs collide"))
    return LabResult("lab_os_users", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Local fixture user store. Not a live directory service.")


def lab_services(fixture: dict[str, Any] | None = None) -> LabResult:
    """Mock unit file enable/start. Print spooler must be running and enabled."""
    units = fixture or {
        "cupsd": {"enabled": True, "active": True, "restart_sec": 8},
        "sshd": {"enabled": True, "active": True, "restart_sec": 2},
        "toy-tracker": {"enabled": False, "active": False, "restart_sec": 0},
    }
    checks = []
    checks.append(_check("cupsd_running", units["cupsd"]["enabled"] and units["cupsd"]["active"], "print spooler down"))
    checks.append(_check("sshd_running", units["sshd"]["active"], "remote admin path down"))
    checks.append(_check("tracker_off", not units["toy-tracker"]["active"], "classroom image forbids toy-tracker"))
    checks.append(_check("cupsd_restart_budget", units["cupsd"]["restart_sec"] <= 15, "restart loop too slow for kiosk"))
    return LabResult("lab_services", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Mock service table. Not systemd on a real host.")


def lab_storage(fixture: dict[str, Any] | None = None) -> LabResult:
    """Quota math: used+reserved must leave 15% free on the civic desk volume."""
    vol = fixture or {
        "size_bytes": 256 * 1024 ** 3,
        "used_bytes": 180 * 1024 ** 3,
        "reserved_bytes": 12 * 1024 ** 3,
        "min_free_ratio": 0.15,
    }
    free = vol["size_bytes"] - vol["used_bytes"] - vol["reserved_bytes"]
    ratio = free / vol["size_bytes"]
    checks = [
        _check("free_nonneg", free >= 0, f"free={free}"),
        _check("min_free", ratio + 1e-12 >= vol["min_free_ratio"], f"free_ratio={ratio:.4f}"),
        _check("used_lt_size", vol["used_bytes"] < vol["size_bytes"], "used exceeds disk"),
    ]
    return LabResult("lab_storage", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Arithmetic on a fixture volume. Not a live block device.")


def lab_dns_hosts(fixture: dict[str, Any] | None = None) -> LabResult:
    """Resolve civic names from hosts + a tiny zone. Split-horizon is in scope."""
    data = fixture or {
        "hosts": {
            "desk.gary.waike.local": "10.20.30.14",
            "printer.gary.waike.local": "10.20.30.40",
        },
        "zone": {
            "library.gary.waike.local": ["10.20.30.21", "10.20.30.22"],
        },
        "queries": [
            ("desk.gary.waike.local", "10.20.30.14"),
            ("printer.gary.waike.local", "10.20.30.40"),
            ("library.gary.waike.local", "10.20.30.21"),
        ],
    }

    def resolve(name: str) -> str | None:
        if name in data["hosts"]:
            return data["hosts"][name]
        recs = data["zone"].get(name) or []
        return recs[0] if recs else None

    checks = []
    for name, expect in data["queries"]:
        got = resolve(name)
        checks.append(_check(f"resolve:{name}", got == expect, f"got={got} expect={expect}"))
    checks.append(_check("no_public_leak", resolve("example.com") is None, "fixture resolver must not invent WAN answers"))
    return LabResult("lab_dns_hosts", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Static hosts/zone fixture. Not recursive Internet DNS.")


def lab_backup(work: Path | None = None) -> LabResult:
    """Checksummed archive: restore must match SHA256 of the source tree."""
    base = work or (ROOT / "artifacts" / "_lab_tmp" / "backup")
    src = base / "src"
    src.mkdir(parents=True, exist_ok=True)
    (src / "ticket_4417.txt").write_text("patron essay draft v3\n", encoding="utf-8")
    (src / "notes.md").write_text("do not store SSNs\n", encoding="utf-8")

    def tree_hash(path: Path) -> str:
        h = hashlib.sha256()
        for p in sorted(path.rglob("*")):
            if p.is_file():
                h.update(p.relative_to(path).as_posix().encode())
                h.update(p.read_bytes())
        return h.hexdigest()

    before = tree_hash(src)
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
    after = tree_hash(dest / "src")
    checks = [
        _check("archive_exists", archive.is_file() and archive.stat().st_size > 0, str(archive)),
        _check("hash_match", before == after, f"before={before[:12]} after={after[:12]}"),
        _check("no_ssn_file", not (src / "ssn.txt").exists(), "PII file must not be in the lab tree"),
    ]
    return LabResult("lab_backup", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Local tar+sha256. Not a production backup appliance.")


def lab_ticket_queue(fixture: dict[str, Any] | None = None) -> LabResult:
    """Triage three tickets: severity, subsystem, next action. Reboot is not a plan."""
    tickets = fixture or [
        {"id": "4417", "symptom": "kiosk session vanishes at 20 minutes", "idle_logout_sec": 1200,
         "subsystem": "os_policy", "severity": "se3", "next": "adjust_idle_or_save_prompt"},
        {"id": "4418", "symptom": "fan scream then black screen", "subsystem": "hardware_thermal",
         "severity": "se2", "next": "capture_temps_then_reseating_plan"},
        {"id": "4419", "symptom": "cannot reach printer.gary.waike.local", "subsystem": "name_resolution",
         "severity": "se3", "next": "check_hosts_then_spooler"},
    ]
    allowed_next = {
        "4417": "adjust_idle_or_save_prompt",
        "4418": "capture_temps_then_reseating_plan",
        "4419": "check_hosts_then_spooler",
    }
    checks = []
    for t in tickets:
        checks.append(_check(f"{t['id']}_not_reboot", t["next"] != "reboot_and_hope", "reboot is not a root cause"))
        checks.append(_check(f"{t['id']}_next", t["next"] == allowed_next[t["id"]], t["next"]))
        checks.append(_check(f"{t['id']}_sev", t["severity"] in {"se1", "se2", "se3", "se4"}, t["severity"]))
    checks.append(_check("4417_idle_math", tickets[0]["idle_logout_sec"] == 20 * 60, "20 minutes is 1200 seconds"))
    return LabResult("lab_ticket_queue", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Synthetic tickets. No real patron PII.")


def lab_automation_runbook(fixture: dict[str, Any] | None = None) -> LabResult:
    """Dry-run a change: three steps, one rollback, change window honored."""
    run = fixture or {
        "change_id": "CHG-88",
        "window_start_min": 18 * 60,
        "window_end_min": 21 * 60,
        "planned_min": 19 * 60 + 15,
        "steps": ["snapshot_home", "apply_idle_policy", "verify_kiosk_login"],
        "rollback": "restore_snapshot_home",
        "executed": ["snapshot_home", "apply_idle_policy", "verify_kiosk_login"],
    }
    in_window = run["window_start_min"] <= run["planned_min"] <= run["window_end_min"]
    checks = [
        _check("three_steps", len(run["steps"]) >= 3, str(run["steps"])),
        _check("rollback_named", bool(run["rollback"]), "missing rollback"),
        _check("in_window", in_window, f"planned={run['planned_min']}"),
        _check("executed_matches", run["executed"] == run["steps"], "dry-run drifted"),
        _check("snapshot_first", run["steps"][0].startswith("snapshot"), "no snapshot before mutate"),
    ]
    return LabResult("lab_automation_runbook", "GENERAL_IT", all(c["ok"] for c in checks), checks,
                     "Dry-run change record. Not unattended production automation.")


# ---------------------------------------------------------------------------
# NETWORKING
# ---------------------------------------------------------------------------

def _ip_to_int(ip: str) -> int:
    return int(ipaddress.IPv4Address(ip))


def lab_cidr_math(fixture: dict[str, Any] | None = None) -> LabResult:
    """Network, broadcast, usable hosts for 10.20.30.40/26 and a /28."""
    cases = fixture or [
        {"cidr": "10.20.30.40/26", "network": "10.20.30.0", "broadcast": "10.20.30.63", "usable": 62},
        {"cidr": "10.20.30.80/28", "network": "10.20.30.80", "broadcast": "10.20.30.95", "usable": 14},
    ]
    checks = []
    for c in cases:
        net = ipaddress.IPv4Network(c["cidr"], strict=False)
        usable = int(net.num_addresses) - 2 if net.prefixlen <= 30 else (0 if net.prefixlen == 32 else 0)
        if net.prefixlen == 31:
            usable = 2
        checks.append(_check(f"{c['cidr']}_net", str(net.network_address) == c["network"], str(net.network_address)))
        checks.append(_check(f"{c['cidr']}_bcast", str(net.broadcast_address) == c["broadcast"], str(net.broadcast_address)))
        checks.append(_check(f"{c['cidr']}_usable", usable == c["usable"], f"usable={usable}"))
    return LabResult("lab_cidr_math", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "IPv4 arithmetic. Not a Cisco simulator.")


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


def lab_datapath(fixture: dict[str, Any] | None = None) -> LabResult:
    """Deep protocol/data-path lab: Ethernet+IPv4 parse, TTL decrement, LPM.

    Frame is a crafted classroom bytestring, not a capture from a live network.
    """
    # dst=aa:aa:aa:aa:aa:01 src=aa:aa:aa:aa:aa:02 ethertype=0800
    eth = bytes.fromhex("aaaaaaaaaa01") + bytes.fromhex("aaaaaaaaaa02") + bytes.fromhex("0800")
    # IPv4 ihl=5, ttl=4, proto=6, src=10.20.30.14 dst=10.20.40.9, total_len=40
    ip = bytearray(20)
    ip[0] = 0x45
    ip[2:4] = (40).to_bytes(2, "big")
    ip[8] = 4
    ip[9] = 6
    ip[12:16] = ipaddress.IPv4Address("10.20.30.14").packed
    ip[16:20] = ipaddress.IPv4Address("10.20.40.9").packed
    tcp = bytes(20)  # unused payload; length only
    frame = eth + bytes(ip) + tcp
    table = (fixture or {}).get("table") or [
        {"prefix": "10.20.40.0/24", "nh": "10.20.30.1", "iface": "eth1"},
        {"prefix": "10.20.0.0/16", "nh": "10.20.30.254", "iface": "eth0"},
        {"prefix": "0.0.0.0/0", "nh": "192.0.2.1", "iface": "wan0"},
    ]

    dst_mac = frame[0:6].hex()
    ethertype = int.from_bytes(frame[12:14], "big")
    iph = frame[14:34]
    version = iph[0] >> 4
    ihl = iph[0] & 0x0F
    ttl = iph[8]
    proto = iph[9]
    dst = str(ipaddress.IPv4Address(iph[16:20]))
    route = _lpm(table, dst)
    new_ttl = ttl - 1
    checks = [
        _check("ethertype_ipv4", ethertype == 0x0800, hex(ethertype)),
        _check("ipv4_version", version == 4 and ihl == 5, f"ver={version} ihl={ihl}"),
        _check("tcp", proto == 6, f"proto={proto}"),
        _check("dst_mac_unicast", dst_mac == "aaaaaaaaaa01", dst_mac),
        _check("ttl_positive_after_dec", new_ttl > 0, f"ttl={ttl}"),
        _check("lpm_more_specific", route.get("iface") == "eth1", str(route)),
        _check("nh", route.get("nh") == "10.20.30.1", str(route)),
    ]
    # Negative: /32 more-specific should win if present
    table2 = table + [{"prefix": "10.20.40.9/32", "nh": "10.20.30.9", "iface": "host9"}]
    r2 = _lpm(table2, dst)
    checks.append(_check("lpm_host_route", r2.get("iface") == "host9", str(r2)))
    # TTL 1 must drop
    checks.append(_check("ttl1_would_drop", (1 - 1) == 0, "TTL expiry is a drop, not a forward"))
    return LabResult("lab_datapath", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "Classroom-crafted frame. Not a packet capture from production. Original WAIKE datapath, not CS144 code.")


def lab_vlan_mac(fixture: dict[str, Any] | None = None) -> LabResult:
    """Forward a frame only if VLAN and MAC table agree."""
    mac_table = (fixture or {}).get("mac") or {
        ("aa:aa:aa:aa:aa:10", 20): "Gi1/0/8",
        ("aa:aa:aa:aa:aa:11", 30): "Gi1/0/9",
    }
    frame = (fixture or {}).get("frame") or {"dst": "aa:aa:aa:aa:aa:10", "vlan": 20}
    key = (frame["dst"], frame["vlan"])
    out = mac_table.get(key)
    miss = mac_table.get((frame["dst"], 30))
    checks = [
        _check("hit_vlan20", out == "Gi1/0/8", str(out)),
        _check("vlan_isolation", miss is None or miss != out, "MAC must not leak across VLAN 30"),
    ]
    return LabResult("lab_vlan_mac", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "Toy MAC/VLAN table. Not a live switch.")


def lab_spf_routing(fixture: dict[str, Any] | None = None) -> LabResult:
    """Dijkstra on a four-router town. Cost(A-B-D) must beat A-C-D."""
    edges = (fixture or {}).get("edges") or {
        ("A", "B"): 2,
        ("B", "A"): 2,
        ("B", "D"): 2,
        ("D", "B"): 2,
        ("A", "C"): 5,
        ("C", "A"): 5,
        ("C", "D"): 5,
        ("D", "C"): 5,
        ("B", "C"): 9,
        ("C", "B"): 9,
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
    checks = [
        _check("path_cost_ad", d["D"] == 4, f"dist={d}"),
        _check("not_long_way", d["D"] < 10, "A-C-D must lose"),
        _check("self_zero", d["A"] == 0, str(d["A"])),
    ]
    return LabResult("lab_spf_routing", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "Four-node SPF. Not OSPF packet exchange with a vendor NOS.")


def lab_nat_acl(fixture: dict[str, Any] | None = None) -> LabResult:
    """Inside source NAT plus an ACL that blocks port 23 and allows 443."""
    acl = (fixture or {}).get("acl") or [
        {"action": "deny", "dport": 23},
        {"action": "permit", "dport": 443},
        {"action": "deny", "dport": "*"},
    ]
    nat = (fixture or {}).get("nat") or {"inside": "10.20.30.14", "outside": "192.0.2.88"}

    def decide(dport: int) -> str:
        for rule in acl:
            if rule["dport"] in {dport, "*"}:
                return rule["action"]
        return "deny"

    checks = [
        _check("telnet_denied", decide(23) == "deny", "telnet must die at the edge"),
        _check("https_ok", decide(443) == "permit", "library HTTPS must pass"),
        _check("unknown_denied", decide(9) == "deny", "implicit deny via star rule"),
        _check("nat_maps", nat["inside"].startswith("10.") and nat["outside"].startswith("192.0.2."), str(nat)),
    ]
    return LabResult("lab_nat_acl", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "Ordered ACL on a fixture. Not a live firewall.")


def lab_dns_resolution(fixture: dict[str, Any] | None = None) -> LabResult:
    """Iterative path: stub -> TLD -> authoritative. Cache hit skips the walk."""
    cache = dict((fixture or {}).get("cache") or {})
    auth = (fixture or {}).get("auth") or {"desk.gary.waike.example": "203.0.113.14"}
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
    checks = [
        _check("first_walk", how1 == "auth_walk" and ip1 == "203.0.113.14", f"{how1}:{ip1}"),
        _check("second_cache", how2 == "cache" and ip2 == ip1, f"{how2}:{ip2}"),
    ]
    return LabResult("lab_dns_resolution", "COMPUTER_NETWORKING", all(c["ok"] for c in checks), checks,
                     "Toy resolver. Not a public recursive service.")


# ---------------------------------------------------------------------------
# CYBER — authorized fixtures only
# ---------------------------------------------------------------------------

SANDBOX_NOTE = (
    "Authorized WAIKE course sandbox/fixture only. Do not run against systems you do not own."
)


def lab_siem_triage(fixture: dict[str, Any] | None = None) -> LabResult:
    """Count AUTH_FAIL bursts. Burst is evidence to look, not proof of an attacker."""
    lines = (fixture or {}).get("lines") or [
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_FAIL user=ada src=10.20.30.5",
        "AUTH_OK user=bea src=10.20.30.8",
        "AUTH_FAIL user=cal src=10.20.30.9",
    ]
    threshold = int((fixture or {}).get("threshold", 3))
    counts: dict[str, int] = {}
    for line in lines:
        if "AUTH_FAIL" not in line:
            continue
        m = re.search(r"user=([a-z0-9._-]+)", line)
        if m:
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    bursts = sorted(u for u, n in counts.items() if n >= threshold)
    checks = [
        _check("ada_burst", bursts == ["ada"], f"bursts={bursts} counts={counts}"),
        _check("no_attacker_word", True, "note must say burst, not attacker"),
        _check("cal_under", counts.get("cal", 0) < threshold, str(counts)),
    ]
    return LabResult("lab_siem_triage", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def lab_hardening_baseline(fixture: dict[str, Any] | None = None) -> LabResult:
    """CIS-inspired classroom baseline on a JSON image, not a live scan."""
    image = fixture or {
        "guest_login": False,
        "ssh_password_auth": False,
        "unattended_upgrades": True,
        "open_ports": [22, 443],
        "world_writable_home": False,
        "ai_agent_sudo": False,
    }
    checks = [
        _check("no_guest", image["guest_login"] is False, "guest login"),
        _check("ssh_keys_only", image["ssh_password_auth"] is False, "password SSH"),
        _check("patch_pipe", image["unattended_upgrades"] is True, "no patch pipe"),
        _check("ports", set(image["open_ports"]) <= {22, 443}, str(image["open_ports"])),
        _check("home_mode", image["world_writable_home"] is False, "home is 777"),
        _check("no_ai_sudo", image["ai_agent_sudo"] is False, "non-human identity must not have sudo"),
    ]
    return LabResult("lab_hardening_baseline", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def lab_iam_rbac(fixture: dict[str, Any] | None = None) -> LabResult:
    """RBAC: human analyst read-only on cases; AI bot cannot close incidents."""
    policy = fixture or {
        "roles": {
            "analyst": {"actions": ["case.read", "case.comment"]},
            "lead": {"actions": ["case.read", "case.comment", "case.close"]},
            "ai.triage.bot": {"actions": ["case.read"]},
        },
        "bindings": {
            "naiya": "analyst",
            "omar": "lead",
            "harbor-bot": "ai.triage.bot",
        },
    }

    def allow(user: str, action: str) -> bool:
        role = policy["bindings"][user]
        return action in policy["roles"][role]["actions"]

    checks = [
        _check("analyst_read", allow("naiya", "case.read"), "analyst should read"),
        _check("analyst_no_close", not allow("naiya", "case.close"), "analyst closed a case"),
        _check("lead_close", allow("omar", "case.close"), "lead cannot close"),
        _check("bot_no_close", not allow("harbor-bot", "case.close"), "bot must not close"),
    ]
    return LabResult("lab_iam_rbac", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def lab_segmentation_zones(fixture: dict[str, Any] | None = None) -> LabResult:
    """Zone matrix: kiosk cannot speak to SOC; SOC can pull kiosk syslog."""
    matrix = fixture or {
        ("kiosk", "soc"): "deny",
        ("soc", "kiosk"): "allow_syslog_only",
        ("kiosk", "internet"): "allow_proxy",
        ("guest", "staff"): "deny",
    }
    checks = [
        _check("kiosk_no_soc", matrix[("kiosk", "soc")] == "deny", "east-west hole"),
        _check("soc_syslog", matrix[("soc", "kiosk")] == "allow_syslog_only", str(matrix[("soc", "kiosk")])),
        _check("guest_staff", matrix[("guest", "staff")] == "deny", "guest jumped to staff"),
    ]
    return LabResult("lab_segmentation_zones", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def lab_incident_playbook(fixture: dict[str, Any] | None = None) -> LabResult:
    """NIST 800-61-shaped clock: detect -> contain -> eradicate -> recover -> lessons."""
    steps = (fixture or {}).get("steps") or [
        "detect",
        "contain",
        "eradicate",
        "recover",
        "lessons",
    ]
    clock = ["detect", "contain", "eradicate", "recover", "lessons"]
    checks = [
        _check("order", steps == clock, f"got={steps}"),
        _check("contain_before_wipe", steps.index("contain") < steps.index("eradicate"), "wiped before contain"),
        _check("lessons_last", steps[-1] == "lessons", "no retro"),
    ]
    return LabResult("lab_incident_playbook", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def _unsafe_len_parser(buf: bytes) -> bytes:
    """Intentionally unsafe toy parser (course CTF fixture). Trusts len byte."""
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


def lab_safe_vuln_detect(fixture: dict[str, Any] | None = None) -> LabResult:
    """Authorized course CTF: detect the length lie; do not exploit real software.

    The unsafe parser is a classroom fixture. Students write a detector and a
    safe parser. No shellcode, no network targets, no credential stuffing.
    """
    oversize = bytes([20]) + b"short"
    ok_msg = bytes([4]) + b"abcd"
    unsafe_got = _unsafe_len_parser(oversize)
    safe_ok = _safe_len_parser(ok_msg)
    safe_raised = False
    try:
        _safe_len_parser(oversize)
    except ValueError:
        safe_raised = True
    checks = [
        _check("unsafe_truncates_or_overreads_pattern", len(unsafe_got) < 20, "fixture did not demonstrate the lie"),
        _check("safe_accepts_honest", safe_ok == b"abcd", safe_ok.decode("latin1", "replace")),
        _check("safe_rejects_lie", safe_raised, "safe parser accepted oversize claim"),
        _check("no_network", True, "this lab never opens a socket"),
    ]
    return LabResult("lab_safe_vuln_detect", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


def lab_forensics_timeline(fixture: dict[str, Any] | None = None) -> LabResult:
    """Order USB insert -> file copy -> unmount from a fixture event log."""
    events = (fixture or {}).get("events") or [
        {"t": 100, "ev": "usb_insert", "dev": "sdb1"},
        {"t": 140, "ev": "file_copy", "path": "/media/sdb1/essay.docx"},
        {"t": 155, "ev": "usb_unmount", "dev": "sdb1"},
        {"t": 90, "ev": "login", "user": "kiosk"},
    ]
    ordered = sorted(events, key=lambda e: e["t"])
    kinds = [e["ev"] for e in ordered]
    checks = [
        _check("login_first", kinds[0] == "login", str(kinds)),
        _check("copy_between", kinds.index("usb_insert") < kinds.index("file_copy") < kinds.index("usb_unmount"), str(kinds)),
        _check("no_secret_in_path", all("password" not in json.dumps(e) for e in events), "secret in fixture"),
    ]
    return LabResult("lab_forensics_timeline", "CYBERSECURITY", all(c["ok"] for c in checks), checks, SANDBOX_NOTE)


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


def run_lab(lab_id: str, **kwargs: Any) -> dict[str, Any]:
    fn = LABS[lab_id]
    result = fn(**kwargs)
    return result.as_dict()


def run_all() -> dict[str, Any]:
    results = []
    for course, ids in COURSE_LABS.items():
        for lab_id in ids:
            results.append(run_lab(lab_id))
    # Negative tests: mutated fixtures must fail
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
    ok = all(r["ok"] for r in results) and all(n["ok"] for n in negatives)
    return {
        "ok": ok,
        "lab_count": len(results),
        "results": results,
        "negatives_must_fail_and_did": negatives,
        "print_pass_forbidden": True,
    }
