"""NETWORKING_INFRA Backbone Room labs. Graders recompute from the learner's own inputs.

All ASNs and prefixes are documentation values (RFC 5398, RFC 3849, RFC 5737); no lab claims
a real peering, transit contract, or production route.
"""
from __future__ import annotations

import ipaddress
import math
from typing import Any

from waike_course_ready.batch007.labs import LabResult, _check, _require_student, _result

COURSE = "NETWORKING_INFRA"
B_NIF = (
    "NETWORKING_INFRA Backbone Room. Documentation ASNs and prefixes, planning coefficients, and synthetic "
    "traffic samples only; no production peering or transit claims. Not student/teacher E6."
)
C_KM_S = 299_792.458
FIBER_INDEX = 1.468
FIBER_DB_PER_KM = 0.35
CONNECTOR_DB = 0.5
SPLICE_DB = 0.1
MIN_MARGIN_DB = 3.0
MINUTES_PER_YEAR = 525_600
DOC_ASN = range(64496, 64512)
DOC_V6 = ipaddress.ip_network("2001:db8::/32")
DOC_V4 = [ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")]


def _num(v: Any) -> float | None:
    if isinstance(v, bool):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _close(a: Any, b: float, tol: float) -> bool:
    x = _num(a)
    return x is not None and abs(x - b) <= tol


def latency_budget(route_km: float, packet_bytes: int, link_gbps: float) -> dict[str, float]:
    prop = route_km / (C_KM_S / FIBER_INDEX) * 1000
    ser = packet_bytes * 8 / (link_gbps * 1e9) * 1000
    return {"propagation_ms": prop, "serialization_ms": ser, "one_way_ms": prop + ser}


def lab_nif_latency_budget(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_latency_budget", COURSE, submission,
        ["route_km", "packet_bytes", "link_gbps", "propagation_ms", "serialization_ms", "one_way_ms"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_latency_budget", COURSE, checks, B_NIF)
    km, gbps, pkt = _num(data.get("route_km")), _num(data.get("link_gbps")), data.get("packet_bytes")
    ok_in = km is not None and km > 0 and gbps is not None and gbps > 0 and isinstance(pkt, int) and pkt > 0
    checks.append(_check("inputs_valid", ok_in, "route km, packet bytes, link Gbit/s > 0"))
    if ok_in:
        b = latency_budget(km, pkt, gbps)  # type: ignore[arg-type]
        checks.append(_check("propagation_recomputed", _close(data.get("propagation_ms"), b["propagation_ms"], 0.005), f"{b['propagation_ms']:.3f} ms"))
        checks.append(_check("serialization_recomputed", _close(data.get("serialization_ms"), b["serialization_ms"], 0.0005), f"{b['serialization_ms']:.4f} ms"))
        checks.append(_check("one_way_recomputed", _close(data.get("one_way_ms"), b["one_way_ms"], 0.005), f"{b['one_way_ms']:.3f} ms"))
    return _result("lab_nif_latency_budget", COURSE, checks, B_NIF)


def lab_nif_ipv6_text(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_ipv6_text", COURSE, submission, ["full", "compressed", "site_prefix_len", "subnet_len", "subnet_count"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_ipv6_text", COURSE, checks, B_NIF)
    try:
        addr = ipaddress.IPv6Address(str(data.get("full")))
    except ValueError:
        addr = None
    checks.append(_check("address_parses", addr is not None, "valid IPv6 text"))
    if addr is not None:
        checks.append(_check("rfc5952_form", data.get("compressed") == addr.compressed, f"expected {addr.compressed}"))
    site, sub = data.get("site_prefix_len"), data.get("subnet_len")
    ok_len = isinstance(site, int) and isinstance(sub, int) and 0 < site < sub <= 128
    checks.append(_check("prefix_lengths", ok_len, "site prefix shorter than subnet prefix"))
    if ok_len:
        checks.append(_check("subnet_count_recomputed", data.get("subnet_count") == 2 ** (sub - site), f"2^({sub}-{site})"))
    return _result("lab_nif_ipv6_text", COURSE, checks, B_NIF)


def bdp(rate_mbps: float, rtt_ms: float, window_bytes: int) -> dict[str, float]:
    bdp_bytes = rate_mbps * 1e6 * rtt_ms / 1000 / 8
    return {
        "bdp_bytes": bdp_bytes,
        "max_throughput_mbps": window_bytes * 8 / (rtt_ms / 1000) / 1e6,
        "window_scale_shift": max(0, math.ceil(math.log2(bdp_bytes / 65535))) if bdp_bytes > 65535 else 0,
    }


def lab_nif_bdp_window(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_bdp_window", COURSE, submission,
        ["rate_mbps", "rtt_ms", "window_bytes", "bdp_bytes", "max_throughput_mbps", "window_scale_shift"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_bdp_window", COURSE, checks, B_NIF)
    rate, rtt, win = _num(data.get("rate_mbps")), _num(data.get("rtt_ms")), data.get("window_bytes")
    ok_in = rate is not None and rate > 0 and rtt is not None and rtt > 0 and isinstance(win, int) and win > 0
    checks.append(_check("inputs_valid", ok_in, "rate, RTT, window > 0"))
    if ok_in:
        b = bdp(rate, rtt, win)  # type: ignore[arg-type]
        checks.append(_check("bdp_recomputed", _close(data.get("bdp_bytes"), b["bdp_bytes"], 1), f"{b['bdp_bytes']:.0f} B"))
        checks.append(_check("window_cap_recomputed", _close(data.get("max_throughput_mbps"), b["max_throughput_mbps"], 0.01), f"{b['max_throughput_mbps']:.2f} Mbit/s"))
        checks.append(_check("scale_shift_recomputed", data.get("window_scale_shift") == b["window_scale_shift"], f"RFC 7323 shift {b['window_scale_shift']}"))
    return _result("lab_nif_bdp_window", COURSE, checks, B_NIF)


ORIGIN_RANK = {"IGP": 0, "EGP": 1, "INCOMPLETE": 2}
BGP_ROUTES = [
    {"id": "R1", "local_pref": 100, "as_path": [64500], "origin": "IGP", "med": 0, "router_id": "10.0.0.1"},
    {"id": "R2", "local_pref": 200, "as_path": [64501, 64502, 64503, 64510], "origin": "IGP", "med": 50, "router_id": "10.0.0.2"},
    {"id": "R3", "local_pref": 200, "as_path": [64505, 64506, 64507, 64510], "origin": "EGP", "med": 0, "router_id": "10.0.0.3"},
]


def bgp_best(routes: list[dict[str, Any]]) -> tuple[str, str]:
    steps = [
        ("local_pref", lambda r: -r["local_pref"]),
        ("as_path", lambda r: len(r["as_path"])),
        ("origin", lambda r: ORIGIN_RANK[r["origin"]]),
        ("med", lambda r: r["med"]),
        ("router_id", lambda r: tuple(int(x) for x in r["router_id"].split("."))),
    ]
    cands = list(routes)
    decided = "only_route"
    for name, key in steps:
        best = min(key(r) for r in cands)
        keep = [r for r in cands if key(r) == best]
        if len(keep) < len(cands):
            decided = name
        cands = keep
        if len(cands) == 1:
            break
    return cands[0]["id"], decided


def lab_nif_bgp_path(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_nif_bgp_path", COURSE, submission, ["best_route", "deciding_attribute"], B_NIF)
    if data is None:
        return _result("lab_nif_bgp_path", COURSE, checks, B_NIF)
    best, why = bgp_best(BGP_ROUTES)
    checks.append(_check("best_route_recomputed", data.get("best_route") == best, f"expected {best}"))
    checks.append(_check("tie_breaker_named", data.get("deciding_attribute") == why, f"last elimination by {why}"))
    return _result("lab_nif_bgp_path", COURSE, checks, B_NIF)


def dns_stale(ttl_s: int, cached_at_s: int, changed_at_s: int) -> dict[str, int]:
    until = cached_at_s + ttl_s
    return {"stale_until_s": until, "stale_window_s": max(0, until - changed_at_s), "worst_case_s": ttl_s}


def lab_nif_dns_ttl(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_dns_ttl", COURSE, submission,
        ["ttl_s", "cached_at_s", "changed_at_s", "stale_until_s", "stale_window_s", "worst_case_s", "lower_ttl_by_s"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_dns_ttl", COURSE, checks, B_NIF)
    ttl, c, ch = data.get("ttl_s"), data.get("cached_at_s"), data.get("changed_at_s")
    ok_in = all(isinstance(v, int) and v >= 0 for v in (ttl, c, ch)) and ttl > 0 and c <= ch  # type: ignore[operator]
    checks.append(_check("inputs_valid", ok_in, "integer seconds; cached before the change"))
    if ok_in:
        s = dns_stale(ttl, c, ch)  # type: ignore[arg-type]
        for key, val in s.items():
            checks.append(_check(f"{key}_recomputed", data.get(key) == val, f"{key}={val}"))
        lower = data.get("lower_ttl_by_s")
        checks.append(_check("lower_ttl_one_old_ttl_ahead", isinstance(lower, int) and lower <= ch - ttl, "lower the TTL at least one old TTL before the change"))  # type: ignore[operator]
    return _result("lab_nif_dns_ttl", COURSE, checks, B_NIF)


def cdn_offload(total_rps: float, hit_ratio: float, object_kb: float) -> dict[str, float]:
    origin = total_rps * (1 - hit_ratio)
    return {
        "origin_rps": origin,
        "origin_gbps": origin * object_kb * 1000 * 8 / 1e9,
        "edge_gbps": total_rps * object_kb * 1000 * 8 / 1e9,
    }


def lab_nif_cdn_offload(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_cdn_offload", COURSE, submission, ["total_rps", "object_kb", "scenarios"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_cdn_offload", COURSE, checks, B_NIF)
    rps, kb = _num(data.get("total_rps")), _num(data.get("object_kb"))
    rows = data.get("scenarios") if isinstance(data.get("scenarios"), list) else []
    ok_in = rps is not None and rps > 0 and kb is not None and kb > 0 and len(rows) >= 2
    checks.append(_check("inputs_valid", ok_in, "rate, object size, ≥2 hit-ratio scenarios"))
    if ok_in:
        bad = 0
        for r in rows:
            h = _num(r.get("hit_ratio")) if isinstance(r, dict) else None
            if h is None or not 0 <= h <= 1:
                bad += 1
                continue
            t = cdn_offload(rps, h, kb)  # type: ignore[arg-type]
            if not (_close(r.get("origin_rps"), t["origin_rps"], 0.5) and _close(r.get("origin_gbps"), t["origin_gbps"], 0.005)):
                bad += 1
        checks.append(_check("scenarios_recomputed", bad == 0, f"wrong={bad}"))
    return _result("lab_nif_cdn_offload", COURSE, checks, B_NIF)


def optical_budget(km: float, connectors: int, splices: int, tx_dbm: float, rx_sens_dbm: float) -> dict[str, Any]:
    loss = km * FIBER_DB_PER_KM + connectors * CONNECTOR_DB + splices * SPLICE_DB
    margin = tx_dbm - loss - rx_sens_dbm
    return {"loss_db": loss, "margin_db": margin, "passes": margin >= MIN_MARGIN_DB}


def lab_nif_optical_budget(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_optical_budget", COURSE, submission,
        ["km", "connectors", "splices", "tx_dbm", "rx_sens_dbm", "loss_db", "margin_db", "passes"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_optical_budget", COURSE, checks, B_NIF)
    km, tx, rx = _num(data.get("km")), _num(data.get("tx_dbm")), _num(data.get("rx_sens_dbm"))
    con, spl = data.get("connectors"), data.get("splices")
    ok_in = km is not None and km > 0 and tx is not None and rx is not None and isinstance(con, int) and isinstance(spl, int) and con >= 0 and spl >= 0
    checks.append(_check("inputs_valid", ok_in, "span, counts, powers"))
    if ok_in:
        b = optical_budget(km, con, spl, tx, rx)  # type: ignore[arg-type]
        checks.append(_check("loss_recomputed", _close(data.get("loss_db"), b["loss_db"], 0.01), f"{b['loss_db']:.2f} dB"))
        checks.append(_check("margin_recomputed", _close(data.get("margin_db"), b["margin_db"], 0.01), f"{b['margin_db']:.2f} dB"))
        checks.append(_check("pass_needs_3db_margin", data.get("passes") is b["passes"], "margin ≥ 3 dB"))
    return _result("lab_nif_optical_budget", COURSE, checks, B_NIF)


def availability(parallel_pair: list[float], serial: list[float]) -> dict[str, float]:
    a = 1.0
    for p in parallel_pair:
        a *= 1 - p
    total = 1 - a
    for s in serial:
        total *= s
    return {"availability": total, "downtime_min_per_year": (1 - total) * MINUTES_PER_YEAR}


def lab_nif_availability(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_availability", COURSE, submission, ["parallel_pair", "serial", "availability", "downtime_min_per_year"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_availability", COURSE, checks, B_NIF)
    par = [_num(x) for x in data.get("parallel_pair") or []]
    ser = [_num(x) for x in data.get("serial") or []]
    ok_in = len(par) == 2 and len(ser) >= 1 and all(x is not None and 0 < x < 1 for x in par + ser)
    checks.append(_check("inputs_valid", ok_in, "two redundant parts and ≥1 serial part, each 0 < A < 1"))
    if ok_in:
        r = availability(par, ser)  # type: ignore[arg-type]
        checks.append(_check("availability_recomputed", _close(data.get("availability"), r["availability"], 1e-6), f"{r['availability']:.6f}"))
        checks.append(_check("downtime_recomputed", _close(data.get("downtime_min_per_year"), r["downtime_min_per_year"], 0.5), f"{r['downtime_min_per_year']:.1f} min/yr"))
    return _result("lab_nif_availability", COURSE, checks, B_NIF)


P95_SAMPLES_MBPS = [
    310, 295, 420, 388, 512, 640, 455, 470, 300, 289,
    905, 610, 575, 530, 498, 444, 401, 366, 350, 720,
]


def p95_bill(samples: list[float], usd_per_mbps: float) -> dict[str, float]:
    s = sorted(samples)
    idx = math.ceil(0.95 * len(s)) - 1
    return {"p95_mbps": s[idx], "bill_usd": s[idx] * usd_per_mbps, "free_burst_samples": len(s) - (idx + 1)}


def lab_nif_p95_billing(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_p95_billing", COURSE, submission, ["samples_mbps", "usd_per_mbps", "p95_mbps", "bill_usd", "free_burst_samples"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_p95_billing", COURSE, checks, B_NIF)
    samples = [_num(x) for x in data.get("samples_mbps") or []]
    price = _num(data.get("usd_per_mbps"))
    ok_in = len(samples) >= 20 and all(x is not None and x >= 0 for x in samples) and price is not None and price > 0
    checks.append(_check("inputs_valid", ok_in, "≥20 five-minute samples and a price"))
    if ok_in:
        b = p95_bill(samples, price)  # type: ignore[arg-type]
        checks.append(_check("p95_recomputed", _close(data.get("p95_mbps"), b["p95_mbps"], 1e-6), f"{b['p95_mbps']} Mbit/s"))
        checks.append(_check("bill_recomputed", _close(data.get("bill_usd"), b["bill_usd"], 0.01), f"${b['bill_usd']:.2f}"))
        checks.append(_check("free_burst_count", data.get("free_burst_samples") == b["free_burst_samples"], "top 5% are not billed"))
    return _result("lab_nif_p95_billing", COURSE, checks, B_NIF)


def lab_nif_design_packet(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_nif_design_packet", COURSE, submission,
        ["labs_passed", "asn", "ipv6_prefix", "route_km", "one_way_ms", "parallel_pair", "serial", "availability",
         "availability_target", "meets_target", "optical", "production_peering_claim"], B_NIF,
    )
    if data is None:
        return _result("lab_nif_design_packet", COURSE, checks, B_NIF)
    checks.append(_check("labs_passed", isinstance(data.get("labs_passed"), int) and data["labs_passed"] >= 6, "≥6 prior labs"))
    checks.append(_check("documentation_asn", data.get("asn") in DOC_ASN, "RFC 5398 documentation ASN"))
    try:
        net = ipaddress.ip_network(str(data.get("ipv6_prefix")))
        doc = net.version == 6 and net.subnet_of(DOC_V6)
    except (ValueError, TypeError):
        doc = False
    checks.append(_check("documentation_prefix", doc, "inside 2001:db8::/32 (RFC 3849)"))
    km = _num(data.get("route_km"))
    if km and km > 0:
        lat = latency_budget(km, 1500, 10.0)["propagation_ms"]
        checks.append(_check("latency_recomputed", _close(data.get("one_way_ms"), lat, 0.01), f"{lat:.3f} ms propagation"))
    else:
        checks.append(_check("latency_recomputed", False, "route_km > 0"))
    par = [_num(x) for x in data.get("parallel_pair") or []]
    ser = [_num(x) for x in data.get("serial") or []]
    target = _num(data.get("availability_target"))
    if len(par) == 2 and ser and all(x is not None and 0 < x < 1 for x in par + ser) and target:
        a = availability(par, ser)["availability"]  # type: ignore[arg-type]
        checks.append(_check("availability_recomputed", _close(data.get("availability"), a, 1e-6), f"{a:.6f}"))
        checks.append(_check("target_verdict", data.get("meets_target") is (a >= target), "computed A vs target"))
    else:
        checks.append(_check("availability_recomputed", False, "valid availability inputs"))
    opt = data.get("optical") if isinstance(data.get("optical"), dict) else {}
    try:
        ob = optical_budget(float(opt["km"]), int(opt["connectors"]), int(opt["splices"]), float(opt["tx_dbm"]), float(opt["rx_sens_dbm"]))
        checks.append(_check("optical_margin", ob["passes"] and _close(opt.get("margin_db"), ob["margin_db"], 0.01), "≥3 dB, recomputed"))
    except (KeyError, TypeError, ValueError):
        checks.append(_check("optical_margin", False, "optical inputs"))
    checks.append(_check("no_production_claim", data.get("production_peering_claim") is False, "design exercise only"))
    return _result("lab_nif_design_packet", COURSE, checks, B_NIF)


LAB_ORDER_NIF = [
    "lab_nif_latency_budget", "lab_nif_ipv6_text", "lab_nif_bdp_window", "lab_nif_bgp_path", "lab_nif_dns_ttl",
    "lab_nif_cdn_offload", "lab_nif_optical_budget", "lab_nif_availability", "lab_nif_p95_billing", "lab_nif_design_packet",
]
LABS_NIF = {name: globals()[name] for name in LAB_ORDER_NIF}

_LAT = latency_budget(1145, 1500, 1.0)
_BDP = bdp(1000, 80, 65535)
_BEST = bgp_best(BGP_ROUTES)
_DNS = dns_stale(3600, 3000, 5000)
_CDN = [(h, cdn_offload(12000, h, 150)) for h in (0.92, 0.96)]
_OPT = optical_budget(40, 4, 6, 0.0, -23.0)
_AV = availability([0.999, 0.999], [0.9995, 0.9999])
_P95 = p95_bill(P95_SAMPLES_MBPS, 0.35)
_V6_FULL = "2001:0DB8:0000:0000:0001:0000:0000:0001"

REFERENCE_NIF: dict[str, dict[str, Any]] = {
    "lab_nif_latency_budget": {"route_km": 1145, "packet_bytes": 1500, "link_gbps": 1.0, **{k: round(v, 4) for k, v in _LAT.items()}},
    "lab_nif_ipv6_text": {
        "full": _V6_FULL, "compressed": ipaddress.IPv6Address(_V6_FULL).compressed,
        "site_prefix_len": 48, "subnet_len": 64, "subnet_count": 2 ** 16,
    },
    "lab_nif_bdp_window": {"rate_mbps": 1000, "rtt_ms": 80, "window_bytes": 65535,
                           "bdp_bytes": round(_BDP["bdp_bytes"]), "max_throughput_mbps": round(_BDP["max_throughput_mbps"], 2),
                           "window_scale_shift": _BDP["window_scale_shift"]},
    "lab_nif_bgp_path": {"best_route": _BEST[0], "deciding_attribute": _BEST[1]},
    "lab_nif_dns_ttl": {"ttl_s": 3600, "cached_at_s": 3000, "changed_at_s": 5000, **_DNS, "lower_ttl_by_s": 5000 - 3600},
    "lab_nif_cdn_offload": {"total_rps": 12000, "object_kb": 150, "scenarios": [
        {"hit_ratio": h, "origin_rps": round(t["origin_rps"], 1), "origin_gbps": round(t["origin_gbps"], 3)} for h, t in _CDN
    ]},
    "lab_nif_optical_budget": {"km": 40, "connectors": 4, "splices": 6, "tx_dbm": 0.0, "rx_sens_dbm": -23.0,
                               "loss_db": round(_OPT["loss_db"], 2), "margin_db": round(_OPT["margin_db"], 2), "passes": _OPT["passes"]},
    "lab_nif_availability": {"parallel_pair": [0.999, 0.999], "serial": [0.9995, 0.9999],
                             "availability": round(_AV["availability"], 7), "downtime_min_per_year": round(_AV["downtime_min_per_year"], 1)},
    "lab_nif_p95_billing": {"samples_mbps": P95_SAMPLES_MBPS, "usd_per_mbps": 0.35, **_P95},
    "lab_nif_design_packet": {
        "labs_passed": 8, "asn": 64500, "ipv6_prefix": "2001:db8:4400::/48",
        "route_km": 1145, "one_way_ms": round(_LAT["propagation_ms"], 4),
        "parallel_pair": [0.999, 0.999], "serial": [0.9995, 0.9999], "availability": round(_AV["availability"], 7),
        "availability_target": 0.999, "meets_target": True,
        "optical": {"km": 40, "connectors": 4, "splices": 6, "tx_dbm": 0.0, "rx_sens_dbm": -23.0, "margin_db": round(_OPT["margin_db"], 2)},
        "production_peering_claim": False,
    },
}

WRONG_NIF: dict[str, dict[str, Any]] = {
    "lab_nif_latency_budget": {"route_km": 1145, "packet_bytes": 1500, "link_gbps": 1.0,
                               "propagation_ms": 3.82, "serialization_ms": 0.0015, "one_way_ms": 3.82},
    "lab_nif_ipv6_text": {"full": _V6_FULL, "compressed": "2001:db8:0:0:1::1", "site_prefix_len": 48, "subnet_len": 64, "subnet_count": 16},
    "lab_nif_bdp_window": {"rate_mbps": 1000, "rtt_ms": 80, "window_bytes": 65535, "bdp_bytes": 80_000_000,
                           "max_throughput_mbps": 1000, "window_scale_shift": 0},
    "lab_nif_bgp_path": {"best_route": "R1", "deciding_attribute": "as_path"},
    "lab_nif_dns_ttl": {"ttl_s": 3600, "cached_at_s": 3000, "changed_at_s": 5000, "stale_until_s": 5000,
                        "stale_window_s": 0, "worst_case_s": 0, "lower_ttl_by_s": 4900},
    "lab_nif_cdn_offload": {"total_rps": 12000, "object_kb": 150, "scenarios": [
        {"hit_ratio": 0.92, "origin_rps": 11040, "origin_gbps": 13.2}, {"hit_ratio": 0.96, "origin_rps": 11520, "origin_gbps": 13.8}]},
    "lab_nif_optical_budget": {"km": 40, "connectors": 4, "splices": 6, "tx_dbm": 0.0, "rx_sens_dbm": -23.0,
                               "loss_db": 14.0, "margin_db": 9.0, "passes": True},
    "lab_nif_availability": {"parallel_pair": [0.999, 0.999], "serial": [0.9995, 0.9999], "availability": 0.9984, "downtime_min_per_year": 841},
    "lab_nif_p95_billing": {"samples_mbps": P95_SAMPLES_MBPS, "usd_per_mbps": 0.35, "p95_mbps": 905, "bill_usd": 316.75, "free_burst_samples": 0},
    "lab_nif_design_packet": {
        "labs_passed": 2, "asn": 13335, "ipv6_prefix": "2606:4700::/32", "route_km": 1145, "one_way_ms": 3.8,
        "parallel_pair": [0.999, 0.999], "serial": [0.9995], "availability": 0.99999, "availability_target": 0.99999,
        "meets_target": True, "optical": {}, "production_peering_claim": True,
    },
}

LAB_SPECS_NIF: dict[str, dict[str, Any]] = {
    "lab_nif_latency_budget": {
        "title": "Fiber latency budget — propagation plus serialization",
        "readme": "Light in fiber travels at c / 1.468. Compute propagation ms for the route, serialization ms for one packet on the link, and their one-way sum.",
        "wrong_hint": "Using the vacuum speed of light under-states fiber delay by about a third.",
    },
    "lab_nif_ipv6_text": {
        "title": "IPv6 text form and /48 → /64 subnet count",
        "readme": "Write the RFC 5952 canonical form of the full address (lowercase, no leading zeros, :: replaces the first longest zero run of two or more groups) and count /64 subnets in the site prefix.",
        "wrong_hint": "Compressing the second zero run, or using :: for a single zero group, fails.",
    },
    "lab_nif_bdp_window": {
        "title": "Bandwidth-delay product and the 64 KiB window ceiling",
        "readme": "Compute BDP bytes = rate × RTT / 8, the throughput a fixed window allows (window × 8 / RTT), and the RFC 7323 window-scale shift needed to cover the BDP.",
        "wrong_hint": "Forgetting to convert ms to seconds or bits to bytes fails.",
    },
    "lab_nif_bgp_path": {
        "title": "BGP best path — local preference before path length",
        "readme": "Run the simplified decision order (highest local_pref, shortest AS_PATH, lowest origin, lowest MED, lowest router ID) on R1–R3. Report the winner and the attribute that removed the last competitor.",
        "wrong_hint": "Picking the shortest AS_PATH first ignores local preference.",
    },
    "lab_nif_dns_ttl": {
        "title": "DNS TTL — how long a change stays invisible",
        "readme": "From TTL, the time a resolver cached the record, and the change time, compute when the cache expires, the stale window, the worst case, and the latest time to lower the TTL beforehand.",
        "wrong_hint": "Assuming a change is visible the moment the zone is edited fails.",
    },
    "lab_nif_cdn_offload": {
        "title": "CDN offload — what the origin still sees",
        "readme": "For at least two request hit ratios, compute origin requests per second and origin Gbit/s from the total rate and the average object size.",
        "wrong_hint": "Multiplying by the hit ratio instead of the miss ratio fails.",
    },
    "lab_nif_optical_budget": {
        "title": "Optical link budget — loss, margin, 3 dB rule",
        "readme": "Planning coefficients: 0.35 dB/km, 0.5 dB per connector, 0.1 dB per splice. Margin = tx − loss − receiver sensitivity; the span passes at ≥ 3 dB.",
        "wrong_hint": "Counting only fiber loss and ignoring connectors overstates margin.",
    },
    "lab_nif_availability": {
        "title": "Availability — redundant pair in series with single parts",
        "readme": "A_pair = 1 − (1 − A1)(1 − A2); multiply by each serial part; downtime = (1 − A) × 525,600 minutes per year.",
        "wrong_hint": "Adding availabilities, or treating the pair as serial, fails.",
    },
    "lab_nif_p95_billing": {
        "title": "95th-percentile transit billing",
        "readme": "Sort the five-minute samples, discard the top 5% (index ceil(0.95·n) − 1 is billed), and multiply by the price per Mbit/s.",
        "wrong_hint": "Billing the peak or the mean fails.",
    },
    "lab_nif_design_packet": {
        "title": "Backbone design packet — documentation numbers, recomputed",
        "readme": "labs_passed ≥ 6; a documentation ASN (64496–64511) and an IPv6 prefix inside 2001:db8::/32; propagation, availability, and optical margin all recomputed; production_peering_claim false.",
        "wrong_hint": "Using a real company's ASN or prefix fails.",
    },
}
