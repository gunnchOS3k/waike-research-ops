"""IT_SUPPORT_HARDWARE Refurb Bench labs. Graders recompute from the technician's own inputs."""
from __future__ import annotations

import math
from typing import Any

from waike_course_ready.batch007.labs import LabResult, _check, _require_student, _result

COURSE = "IT_SUPPORT_HARDWARE"
B_ISH = (
    "IT_SUPPORT_HARDWARE Refurb Bench. Planning arithmetic and decision tables on donated-PC fixtures; "
    "no customer data retained, no mains-voltage work inside a PSU. Not student/teacher E6."
)
PSU_HEADROOM = 1.25
PSU_SIZES = [450, 550, 650, 750, 850]


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


def psu_plan(components: dict[str, float]) -> dict[str, Any]:
    total = sum(components.values())
    need = total * PSU_HEADROOM
    choice = next((s for s in PSU_SIZES if s >= need), None)
    return {"total_w": total, "required_w": need, "chosen_psu_w": choice}


def lab_ish_psu_budget(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_psu_budget", COURSE, submission, ["components", "total_w", "required_w", "chosen_psu_w"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_psu_budget", COURSE, checks, B_ISH)
    comps = {k: _num(v) for k, v in (data.get("components") or {}).items()} if isinstance(data.get("components"), dict) else {}
    ok_in = len(comps) >= 4 and all(v is not None and v > 0 for v in comps.values())
    checks.append(_check("components_listed", ok_in, "≥4 parts with positive watts"))
    if ok_in:
        p = psu_plan(comps)  # type: ignore[arg-type]
        checks.append(_check("total_recomputed", _close(data.get("total_w"), p["total_w"], 0.01), f"{p['total_w']} W"))
        checks.append(_check("headroom_applied", _close(data.get("required_w"), p["required_w"], 0.01), "× 1.25"))
        checks.append(_check("smallest_adequate_psu", data.get("chosen_psu_w") == p["chosen_psu_w"], f"{p['chosen_psu_w']} W"))
    return _result("lab_ish_psu_budget", COURSE, checks, B_ISH)


def channels_from_slots(slots: list[str]) -> int:
    return len({str(s)[:1].upper() for s in slots if s})


def lab_ish_memory_bandwidth(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_memory_bandwidth", COURSE, submission, ["mt_s", "slots_used", "channels", "bandwidth_gb_s"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_memory_bandwidth", COURSE, checks, B_ISH)
    mts = _num(data.get("mt_s"))
    slots = data.get("slots_used") if isinstance(data.get("slots_used"), list) else []
    ok_in = mts is not None and mts > 0 and bool(slots)
    checks.append(_check("inputs_valid", ok_in, "transfer rate and populated slots"))
    if ok_in:
        ch = channels_from_slots(slots)
        checks.append(_check("channels_from_slots", data.get("channels") == ch, f"distinct channel letters = {ch}"))
        bw = mts * 8 * ch / 1000  # type: ignore[operator]
        checks.append(_check("bandwidth_recomputed", _close(data.get("bandwidth_gb_s"), bw, 0.05), f"{bw:.1f} GB/s"))
    return _result("lab_ish_memory_bandwidth", COURSE, checks, B_ISH)


def raid_row(level: str, n: int, size_tb: float) -> dict[str, Any] | None:
    if level == "0" and n >= 2:
        return {"usable_tb": n * size_tb, "guaranteed_failures": 0}
    if level == "1" and n >= 2:
        return {"usable_tb": size_tb, "guaranteed_failures": n - 1}
    if level == "5" and n >= 3:
        return {"usable_tb": (n - 1) * size_tb, "guaranteed_failures": 1}
    if level == "6" and n >= 4:
        return {"usable_tb": (n - 2) * size_tb, "guaranteed_failures": 2}
    if level == "10" and n >= 4 and n % 2 == 0:
        return {"usable_tb": n / 2 * size_tb, "guaranteed_failures": 1}
    return None


def lab_ish_raid_capacity(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_raid_capacity", COURSE, submission, ["disks", "size_tb", "levels", "raid_is_backup"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_raid_capacity", COURSE, checks, B_ISH)
    n, size = data.get("disks"), _num(data.get("size_tb"))
    levels = data.get("levels") if isinstance(data.get("levels"), dict) else {}
    ok_in = isinstance(n, int) and n >= 4 and size is not None and size > 0
    checks.append(_check("array_inputs", ok_in, "≥4 disks of positive size"))
    checks.append(_check("five_levels", set(levels) == {"0", "1", "5", "6", "10"}, "RAID 0/1/5/6/10"))
    if ok_in:
        bad = [lv for lv, row in levels.items() if not isinstance(row, dict) or raid_row(lv, n, size) is None
               or not _close(row.get("usable_tb"), raid_row(lv, n, size)["usable_tb"], 0.01)  # type: ignore[index]
               or row.get("guaranteed_failures") != raid_row(lv, n, size)["guaranteed_failures"]]  # type: ignore[index]
        checks.append(_check("levels_recomputed", bool(levels) and not bad, f"wrong={bad}"))
    checks.append(_check("raid_not_backup", data.get("raid_is_backup") is False, "RAID survives disk loss, not deletion or ransomware"))
    return _result("lab_ish_raid_capacity", COURSE, checks, B_ISH)


def mbr_limit(sector_bytes: int) -> int:
    return 2 ** 32 * sector_bytes


def lab_ish_partition_scheme(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_partition_scheme", COURSE, submission, ["disk_bytes", "sector_bytes", "mbr_max_bytes", "scheme", "boot_firmware"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_partition_scheme", COURSE, checks, B_ISH)
    disk, sector = data.get("disk_bytes"), data.get("sector_bytes")
    ok_in = isinstance(disk, int) and disk > 0 and sector in (512, 4096)
    checks.append(_check("inputs_valid", ok_in, "disk bytes and a 512 or 4096-byte sector"))
    if ok_in:
        lim = mbr_limit(sector)
        checks.append(_check("mbr_limit_recomputed", data.get("mbr_max_bytes") == lim, f"2^32 × {sector} = {lim}"))
        needs_gpt = disk > lim
        checks.append(_check("scheme_choice", data.get("scheme") == "GPT" if needs_gpt else data.get("scheme") in ("GPT", "MBR"), "GPT above the MBR limit"))
        if data.get("scheme") == "GPT":
            checks.append(_check("uefi_for_gpt_boot", data.get("boot_firmware") == "UEFI", "booting a GPT system disk needs UEFI"))
    return _result("lab_ish_partition_scheme", COURSE, checks, B_ISH)


FAULT_TABLE = {
    "no_lights_no_fans": ("power_path", "outlet, power cable, PSU switch"),
    "fans_spin_no_display_beeps": ("memory_or_cpu_seating", "reseat RAM one stick at a time"),
    "post_ok_no_boot_device": ("boot_order_or_disk", "firmware boot order and disk detection"),
    "boots_then_stop_error": ("driver_or_os", "last driver or update installed"),
    "random_shutdown_under_load": ("thermal_or_psu_capacity", "temperatures and PSU rating"),
}
FAULT_TICKETS = {
    "ISH-T1": "fans_spin_no_display_beeps",
    "ISH-T2": "no_lights_no_fans",
    "ISH-T3": "random_shutdown_under_load",
    "ISH-T4": "post_ok_no_boot_device",
    "ISH-T5": "boots_then_stop_error",
}


def lab_ish_fault_isolation(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_ish_fault_isolation", COURSE, submission, ["classified", "replaced_parts_before_isolating"], B_ISH)
    if data is None:
        return _result("lab_ish_fault_isolation", COURSE, checks, B_ISH)
    got = data.get("classified") if isinstance(data.get("classified"), dict) else {}
    expected = {t: FAULT_TABLE[s][0] for t, s in FAULT_TICKETS.items()}
    checks.append(_check("tickets_classified", got == expected, f"expected {expected}"))
    checks.append(_check("isolate_before_replace", data.get("replaced_parts_before_isolating") is False, "no shotgun swaps"))
    return _result("lab_ish_fault_isolation", COURSE, checks, B_ISH)


LINK_GBPS = {"HDMI_1_4": 8.16, "HDMI_2_0": 14.4, "DP_1_4": 25.92}


def display_rate_gbps(w: int, h: int, hz: float, bpp: int) -> float:
    return w * h * hz * bpp / 1e9


def lab_ish_display_link(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_display_link", COURSE, submission, ["modes", "rate_is_lower_bound"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_display_link", COURSE, checks, B_ISH)
    modes = data.get("modes") if isinstance(data.get("modes"), list) else []
    checks.append(_check("two_modes", len(modes) >= 2, f"modes={len(modes)}"))
    bad = 0
    for m in modes:
        try:
            rate = display_rate_gbps(int(m["width"]), int(m["height"]), float(m["hz"]), int(m["bpp"]))
            fits = {k: rate <= v for k, v in LINK_GBPS.items()}
        except (KeyError, TypeError, ValueError):
            bad += 1
            continue
        if not _close(m.get("rate_gbps"), rate, 0.01) or m.get("fits") != fits:
            bad += 1
    checks.append(_check("modes_recomputed", bool(modes) and bad == 0, f"wrong={bad}"))
    checks.append(_check("blanking_ignored_stated", data.get("rate_is_lower_bound") is True, "active pixels only → lower bound"))
    return _result("lab_ish_display_link", COURSE, checks, B_ISH)


def ups_runtime_min(battery_wh: float, efficiency: float, load_w: float) -> float:
    return battery_wh * efficiency / load_w * 60


def lab_ish_ups_runtime(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_ups_runtime", COURSE, submission, ["battery_wh", "efficiency", "load_w", "runtime_min", "shutdown_at_min"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_ups_runtime", COURSE, checks, B_ISH)
    wh, eff, load = (_num(data.get(k)) for k in ("battery_wh", "efficiency", "load_w"))
    ok_in = wh is not None and wh > 0 and eff is not None and 0 < eff <= 1 and load is not None and load > 0
    checks.append(_check("inputs_valid", ok_in, "Wh > 0, 0 < efficiency ≤ 1, load > 0"))
    if ok_in:
        rt = ups_runtime_min(wh, eff, load)  # type: ignore[arg-type]
        checks.append(_check("runtime_recomputed", _close(data.get("runtime_min"), rt, 0.1), f"{rt:.1f} min"))
        sd = _num(data.get("shutdown_at_min"))
        checks.append(_check("shutdown_with_margin", sd is not None and 0 < sd <= 0.8 * rt, "start shutdown by 80% of runtime"))
    return _result("lab_ish_ups_runtime", COURSE, checks, B_ISH)


def imaging_minutes(image_gb: float, machines: int, link_gbps: float, efficiency: float) -> dict[str, float]:
    per_stream_s = image_gb * 8 / (link_gbps * efficiency)
    return {"unicast_min": per_stream_s * machines / 60, "multicast_min": per_stream_s / 60}


def lab_ish_imaging_time(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_imaging_time", COURSE, submission,
        ["image_gb", "machines", "link_gbps", "efficiency", "unicast_min", "multicast_min"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_imaging_time", COURSE, checks, B_ISH)
    gb, link, eff = (_num(data.get(k)) for k in ("image_gb", "link_gbps", "efficiency"))
    n = data.get("machines")
    ok_in = gb and link and eff and 0 < eff <= 1 and isinstance(n, int) and n > 0 and gb > 0 and link > 0
    checks.append(_check("inputs_valid", bool(ok_in), "positive size, count, link; 0 < efficiency ≤ 1"))
    if ok_in:
        t = imaging_minutes(gb, n, link, eff)  # type: ignore[arg-type]
        checks.append(_check("unicast_recomputed", _close(data.get("unicast_min"), t["unicast_min"], 0.1), f"{t['unicast_min']:.1f} min"))
        checks.append(_check("multicast_recomputed", _close(data.get("multicast_min"), t["multicast_min"], 0.05), f"{t['multicast_min']:.2f} min"))
    return _result("lab_ish_imaging_time", COURSE, checks, B_ISH)


def sanitize_method(disposition: str, media_ok: bool) -> str:
    if not media_ok:
        return "Destroy"
    return {"reuse_internal": "Clear", "leave_org": "Purge"}.get(disposition, "Destroy")


SANITIZE_DEVICES = [
    {"serial": "RB-1001", "media": "hdd", "disposition": "reuse_internal", "media_ok": True},
    {"serial": "RB-1002", "media": "ssd", "disposition": "leave_org", "media_ok": True},
    {"serial": "RB-1003", "media": "ssd", "disposition": "leave_org", "media_ok": False},
    {"serial": "RB-1004", "media": "hdd", "disposition": "leave_org", "media_ok": True},
]


def lab_ish_sanitize_decision(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_ish_sanitize_decision", COURSE, submission, ["decisions"], B_ISH)
    if data is None:
        return _result("lab_ish_sanitize_decision", COURSE, checks, B_ISH)
    rows = {r.get("serial"): r for r in data.get("decisions") or [] if isinstance(r, dict)}
    checks.append(_check("every_device", set(rows) == {d["serial"] for d in SANITIZE_DEVICES}, "one decision per serial"))
    bad = [d["serial"] for d in SANITIZE_DEVICES
           if d["serial"] in rows and rows[d["serial"]].get("method") != sanitize_method(d["disposition"], d["media_ok"])]
    checks.append(_check("methods_by_disposition", bool(rows) and not bad, f"wrong={bad}"))
    verified = all(r.get("verified") is True and str(r.get("certificate_id") or "").strip() for r in rows.values())
    checks.append(_check("certificates", bool(rows) and verified, "verification + certificate per device"))
    return _result("lab_ish_sanitize_decision", COURSE, checks, B_ISH)


def lab_ish_service_report(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ish_service_report", COURSE, submission, ["labs_passed", "devices", "customer_data_retained"], B_ISH,
    )
    if data is None:
        return _result("lab_ish_service_report", COURSE, checks, B_ISH)
    checks.append(_check("labs_passed", isinstance(data.get("labs_passed"), int) and data["labs_passed"] >= 6, "≥6 prior labs"))
    devs = [d for d in data.get("devices") or [] if isinstance(d, dict)]
    faults = {v[0] for v in FAULT_TABLE.values()}
    good = all(d.get("fault_class") in faults and str(d.get("fix") or "").strip()
               and d.get("sanitization") in ("Clear", "Purge", "Destroy") and d.get("verified") is True for d in devs)
    checks.append(_check("devices_documented", bool(devs) and good, "fault class, fix, sanitization, verification"))
    checks.append(_check("no_customer_data", data.get("customer_data_retained") is False, "nothing kept from donors"))
    return _result("lab_ish_service_report", COURSE, checks, B_ISH)


LAB_ORDER_ISH = [
    "lab_ish_psu_budget", "lab_ish_memory_bandwidth", "lab_ish_raid_capacity", "lab_ish_partition_scheme",
    "lab_ish_fault_isolation", "lab_ish_display_link", "lab_ish_ups_runtime", "lab_ish_imaging_time",
    "lab_ish_sanitize_decision", "lab_ish_service_report",
]
LABS_ISH = {name: globals()[name] for name in LAB_ORDER_ISH}

_PARTS = {"cpu": 125, "gpu": 200, "motherboard": 50, "ram": 10, "ssd": 8, "fans": 12}
_PSU = psu_plan(_PARTS)
_IMG = imaging_minutes(32, 40, 1.0, 0.7)
_MODES = [(3840, 2160, 60, 24), (3840, 2160, 120, 24)]

REFERENCE_ISH: dict[str, dict[str, Any]] = {
    "lab_ish_psu_budget": {"components": _PARTS, **_PSU},
    "lab_ish_memory_bandwidth": {"mt_s": 3200, "slots_used": ["A2", "B2"], "channels": 2, "bandwidth_gb_s": 51.2},
    "lab_ish_raid_capacity": {
        "disks": 4, "size_tb": 4,
        "levels": {lv: raid_row(lv, 4, 4) for lv in ("0", "1", "5", "6", "10")}, "raid_is_backup": False,
    },
    "lab_ish_partition_scheme": {
        "disk_bytes": 4_000_000_000_000, "sector_bytes": 512, "mbr_max_bytes": mbr_limit(512),
        "scheme": "GPT", "boot_firmware": "UEFI",
    },
    "lab_ish_fault_isolation": {
        "classified": {t: FAULT_TABLE[s][0] for t, s in FAULT_TICKETS.items()}, "replaced_parts_before_isolating": False,
    },
    "lab_ish_display_link": {"modes": [
        {"width": w, "height": h, "hz": hz, "bpp": bpp, "rate_gbps": round(display_rate_gbps(w, h, hz, bpp), 3),
         "fits": {k: display_rate_gbps(w, h, hz, bpp) <= v for k, v in LINK_GBPS.items()}}
        for w, h, hz, bpp in _MODES
    ], "rate_is_lower_bound": True},
    "lab_ish_ups_runtime": {
        "battery_wh": 864, "efficiency": 0.85, "load_w": 300,
        "runtime_min": round(ups_runtime_min(864, 0.85, 300), 1), "shutdown_at_min": 110,
    },
    "lab_ish_imaging_time": {
        "image_gb": 32, "machines": 40, "link_gbps": 1.0, "efficiency": 0.7,
        "unicast_min": round(_IMG["unicast_min"], 1), "multicast_min": round(_IMG["multicast_min"], 2),
    },
    "lab_ish_sanitize_decision": {"decisions": [
        {"serial": d["serial"], "method": sanitize_method(d["disposition"], d["media_ok"]),
         "verified": True, "certificate_id": f"SAN-{d['serial']}"}
        for d in SANITIZE_DEVICES
    ]},
    "lab_ish_service_report": {
        "labs_passed": 8,
        "devices": [{"serial": "RB-1002", "fault_class": "memory_or_cpu_seating", "fix": "reseated DIMM in A2",
                     "sanitization": "Purge", "verified": True}],
        "customer_data_retained": False,
    },
}

WRONG_ISH: dict[str, dict[str, Any]] = {
    "lab_ish_psu_budget": {"components": _PARTS, "total_w": 405, "required_w": 405, "chosen_psu_w": 450},
    "lab_ish_memory_bandwidth": {"mt_s": 3200, "slots_used": ["A1", "A2"], "channels": 2, "bandwidth_gb_s": 51.2},
    "lab_ish_raid_capacity": {"disks": 4, "size_tb": 4, "levels": {"5": {"usable_tb": 16, "guaranteed_failures": 2}}, "raid_is_backup": True},
    "lab_ish_partition_scheme": {"disk_bytes": 4_000_000_000_000, "sector_bytes": 512, "mbr_max_bytes": 2_000_000_000_000,
                                 "scheme": "MBR", "boot_firmware": "BIOS"},
    "lab_ish_fault_isolation": {"classified": {"ISH-T1": "power_path"}, "replaced_parts_before_isolating": True},
    "lab_ish_display_link": {"modes": [{"width": 3840, "height": 2160, "hz": 120, "bpp": 24, "rate_gbps": 11.94,
                                        "fits": {"HDMI_1_4": False, "HDMI_2_0": True, "DP_1_4": True}}], "rate_is_lower_bound": False},
    "lab_ish_ups_runtime": {"battery_wh": 864, "efficiency": 0.85, "load_w": 300, "runtime_min": 172.8, "shutdown_at_min": 170},
    "lab_ish_imaging_time": {"image_gb": 32, "machines": 40, "link_gbps": 1.0, "efficiency": 0.7, "unicast_min": 6.1, "multicast_min": 6.1},
    "lab_ish_sanitize_decision": {"decisions": [{"serial": "RB-1002", "method": "Clear", "verified": False}]},
    "lab_ish_service_report": {"labs_passed": 1, "devices": [{"serial": "RB-1002", "fault_class": "it broke"}], "customer_data_retained": True},
}

LAB_SPECS_ISH: dict[str, dict[str, Any]] = {
    "lab_ish_psu_budget": {
        "title": "Power supply budget — sum the parts, add 25% headroom, pick the smallest adequate unit",
        "readme": "List at least four components with watts, total them, multiply by 1.25, and choose the smallest PSU from 450/550/650/750/850 W that covers it.",
        "wrong_hint": "Buying a PSU equal to the raw total leaves no headroom and fails.",
    },
    "lab_ish_memory_bandwidth": {
        "title": "Memory channels — slots decide bandwidth",
        "readme": "From the transfer rate (MT/s) and the populated slots, count channels (distinct slot letters) and compute GB/s = MT/s × 8 × channels / 1000.",
        "wrong_hint": "Two sticks in A1 and A2 share one channel; claiming dual-channel fails.",
    },
    "lab_ish_raid_capacity": {
        "title": "RAID usable capacity and guaranteed failures",
        "readme": "For your array (≥4 disks), give usable TB and guaranteed tolerated failures for RAID 0, 1, 5, 6, 10. raid_is_backup must be false.",
        "wrong_hint": "Counting parity disks as usable space, or calling RAID a backup, fails.",
    },
    "lab_ish_partition_scheme": {
        "title": "MBR or GPT — the 2^32-sector ceiling",
        "readme": "Compute the MBR limit 2^32 × sector size, pick GPT when the disk is larger, and boot GPT system disks with UEFI.",
        "wrong_hint": "Formatting a 4 TB disk as MBR strands the space above 2 TiB.",
    },
    "lab_ish_fault_isolation": {
        "title": "Fault isolation — symptom to subsystem before any part swap",
        "readme": "Classify tickets ISH-T1…T5 with the bench fault table and confirm replaced_parts_before_isolating is false.",
        "wrong_hint": "Replacing the motherboard for a reseat-able RAM fault fails.",
    },
    "lab_ish_display_link": {
        "title": "Display bandwidth — will the cable carry the mode?",
        "readme": "For at least two modes compute width × height × Hz × bpp in Gbit/s and mark fits for HDMI 1.4 (8.16), HDMI 2.0 (14.4), DP 1.4 (25.92). State that ignoring blanking makes this a lower bound.",
        "wrong_hint": "Promising 4K 120 Hz over HDMI 2.0 fails.",
    },
    "lab_ish_ups_runtime": {
        "title": "UPS runtime — watt-hours, inverter efficiency, load",
        "readme": "runtime_min = Wh × efficiency / load × 60. Schedule graceful shutdown no later than 80% of that runtime.",
        "wrong_hint": "Ignoring inverter loss, or shutting down at the last minute, fails.",
    },
    "lab_ish_imaging_time": {
        "title": "Imaging a lab — unicast versus multicast",
        "readme": "Compute minutes to push one image to N machines one at a time (unicast) and as one shared stream (multicast) at the given link efficiency.",
        "wrong_hint": "Using bytes where the link is in bits is off by eight.",
    },
    "lab_ish_sanitize_decision": {
        "title": "Media sanitization — Clear, Purge, or Destroy",
        "readme": "Apply the bench rule (inspired by NIST SP 800-88): failed media → Destroy; leaving the organisation → Purge; internal reuse → Clear. Record verification and a certificate ID.",
        "wrong_hint": "A quick format on a donated SSD is not Purge.",
    },
    "lab_ish_service_report": {
        "title": "Refurb service report",
        "readme": "labs_passed ≥ 6; every device has a fault class from the table, the fix, a sanitization method, and verification; customer_data_retained false.",
        "wrong_hint": "A report without sanitization proof fails.",
    },
}
