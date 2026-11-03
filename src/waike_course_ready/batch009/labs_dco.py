"""DIGITAL_CONFIDENCE Library Lab labs. Graders recompute from the learner's own inputs."""
from __future__ import annotations

import math
import posixpath
from typing import Any
from urllib.parse import urlparse

from waike_course_ready.batch007.labs import LabResult, _check, _require_student, _result

COURSE = "DIGITAL_CONFIDENCE"
B_DCO = (
    "DIGITAL_CONFIDENCE Library Lab. Practice files, made-up budgets, and example.* links only; "
    "never real passwords or personal data. Not student/teacher E6."
)
GIB = 2 ** 30


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


def resolve_path(cwd: str, relative: str) -> str:
    return posixpath.normpath(posixpath.join(cwd, relative))


def lab_dco_paths(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_dco_paths", COURSE, submission, ["tasks"], B_DCO)
    if data is None:
        return _result("lab_dco_paths", COURSE, checks, B_DCO)
    tasks = data.get("tasks") if isinstance(data.get("tasks"), list) else []
    checks.append(_check("two_tasks", len(tasks) >= 2, f"tasks={len(tasks)}"))
    bad = [t for t in tasks if not isinstance(t, dict) or not str(t.get("cwd", "")).startswith("/")
           or t.get("absolute") != resolve_path(str(t.get("cwd")), str(t.get("relative", "")))]
    checks.append(_check("paths_resolved", bool(tasks) and not bad, f"wrong={len(bad)}"))
    uses_parent = any(".." in str(t.get("relative", "")) for t in tasks if isinstance(t, dict))
    checks.append(_check("uses_parent_step", uses_parent, "at least one path climbs with .."))
    return _result("lab_dco_paths", COURSE, checks, B_DCO)


def storage_check(drive_gb: float, photo_count: int, photo_mb: float, free_gib: float) -> dict[str, Any]:
    need_bytes = photo_count * photo_mb * 1e6
    return {
        "shown_gib": drive_gb * 1e9 / GIB,
        "photos_gib": need_bytes / GIB,
        "fits": need_bytes <= free_gib * GIB,
    }


def lab_dco_storage_units(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_storage_units", COURSE, submission,
        ["drive_gb", "shown_gib", "photo_count", "photo_mb", "photos_gib", "free_gib", "fits"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_storage_units", COURSE, checks, B_DCO)
    vals = [_num(data.get(k)) for k in ("drive_gb", "photo_count", "photo_mb", "free_gib")]
    ok_in = all(v is not None and v > 0 for v in vals)
    checks.append(_check("inputs_positive", ok_in, "drive, count, size, free > 0"))
    if ok_in:
        truth = storage_check(*vals)  # type: ignore[arg-type]
        checks.append(_check("shown_gib_recomputed", _close(data.get("shown_gib"), truth["shown_gib"], 0.01), f"{truth['shown_gib']:.2f} GiB"))
        checks.append(_check("photos_gib_recomputed", _close(data.get("photos_gib"), truth["photos_gib"], 0.01), f"{truth['photos_gib']:.3f} GiB"))
        checks.append(_check("fit_decision", data.get("fits") is truth["fits"], f"fits={truth['fits']}"))
    return _result("lab_dco_storage_units", COURSE, checks, B_DCO)


def entropy_bits(pool: int, length: int) -> float:
    return length * math.log2(pool)


def lab_dco_entropy(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_entropy", COURSE, submission, ["schemes", "strongest", "reuse_allowed", "forced_rotation_without_cause"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_entropy", COURSE, checks, B_DCO)
    rows = data.get("schemes") if isinstance(data.get("schemes"), list) else []
    checks.append(_check("three_schemes", len(rows) >= 3, f"schemes={len(rows)}"))
    bits: dict[str, float] = {}
    bad = 0
    for r in rows:
        pool, length = (r.get("pool"), r.get("length")) if isinstance(r, dict) else (None, None)
        if not (isinstance(pool, int) and pool >= 2 and isinstance(length, int) and length >= 1):
            bad += 1
            continue
        b = entropy_bits(pool, length)
        bits[str(r.get("name"))] = b
        if not _close(r.get("bits"), b, 0.05):
            bad += 1
    checks.append(_check("bits_recomputed", bool(rows) and bad == 0, f"wrong={bad}"))
    best = max(bits, key=bits.get) if bits else None
    checks.append(_check("strongest_named", data.get("strongest") == best, f"expected {best}"))
    checks.append(_check("no_reuse", data.get("reuse_allowed") is False, "one secret per site"))
    checks.append(_check("no_forced_rotation", data.get("forced_rotation_without_cause") is False,
                         "NIST SP 800-63B: change on evidence of compromise, not on a calendar"))
    return _result("lab_dco_entropy", COURSE, checks, B_DCO)


def registered_domain(url: str) -> tuple[str, str]:
    host = (urlparse(url).hostname or "").lower()
    return host, ".".join(host.split(".")[-2:])


def lab_dco_link_check(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_link_check", COURSE, submission, ["url", "expected_domain", "hostname", "registered_domain", "safe_to_open"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_link_check", COURSE, checks, B_DCO)
    host, reg = registered_domain(str(data.get("url")))
    checks.append(_check("hostname_read", data.get("hostname") == host, host))
    checks.append(_check("registered_domain_read", data.get("registered_domain") == reg, f"read right to left: {reg}"))
    safe = reg == str(data.get("expected_domain") or "").lower()
    checks.append(_check("safety_call", data.get("safe_to_open") is safe, f"safe={safe}"))
    return _result("lab_dco_link_check", COURSE, checks, B_DCO)


def lab_dco_sheet_formulas(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_sheet_formulas", COURSE, submission, ["rows", "total", "average", "largest_item", "share_item", "share_pct"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_sheet_formulas", COURSE, checks, B_DCO)
    rows = data.get("rows") if isinstance(data.get("rows"), dict) else {}
    nums = {k: _num(v) for k, v in rows.items()}
    ok_in = len(nums) >= 4 and all(v is not None and v >= 0 for v in nums.values())
    checks.append(_check("four_rows", ok_in, f"rows={len(nums)}"))
    if ok_in:
        total = sum(nums.values())  # type: ignore[arg-type]
        checks.append(_check("sum_recomputed", _close(data.get("total"), total, 0.005), f"SUM={total}"))
        checks.append(_check("average_recomputed", _close(data.get("average"), total / len(nums), 0.005), "AVERAGE"))
        checks.append(_check("largest_item", data.get("largest_item") == max(nums, key=nums.get), "MAX row"))
        item = data.get("share_item")
        share = 100 * nums[item] / total if item in nums and total else None  # type: ignore[operator]
        checks.append(_check("share_recomputed", share is not None and _close(data.get("share_pct"), share, 0.01), "row / SUM × 100"))
    return _result("lab_dco_sheet_formulas", COURSE, checks, B_DCO)


def typing_scores(chars: int, minutes: float, errors: int) -> dict[str, float]:
    gross = chars / 5 / minutes
    return {"gross_wpm": gross, "net_wpm": gross - errors / minutes, "accuracy_pct": 100 * (chars - errors) / chars}


def lab_dco_typing_wpm(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_typing_wpm", COURSE, submission, ["chars", "minutes", "errors", "gross_wpm", "net_wpm", "accuracy_pct"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_typing_wpm", COURSE, checks, B_DCO)
    c, m, e = data.get("chars"), _num(data.get("minutes")), data.get("errors")
    ok_in = isinstance(c, int) and c > 0 and m is not None and m > 0 and isinstance(e, int) and 0 <= e <= c
    checks.append(_check("inputs_valid", ok_in, "chars > 0, minutes > 0, 0 ≤ errors ≤ chars"))
    if ok_in:
        s = typing_scores(c, m, e)  # type: ignore[arg-type]
        for key, val in s.items():
            checks.append(_check(f"{key}_recomputed", _close(data.get(key), val, 0.05), f"{val:.2f}"))
    return _result("lab_dco_typing_wpm", COURSE, checks, B_DCO)


def base64_size(n: int) -> int:
    return 4 * math.ceil(n / 3)


def lab_dco_attachment_fit(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_attachment_fit", COURSE, submission, ["file_bytes", "limit_bytes", "encoded_bytes", "fits", "plan"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_attachment_fit", COURSE, checks, B_DCO)
    n, lim = data.get("file_bytes"), data.get("limit_bytes")
    ok_in = isinstance(n, int) and n > 0 and isinstance(lim, int) and lim > 0
    checks.append(_check("inputs_valid", ok_in, "integer byte counts"))
    if ok_in:
        enc = base64_size(n)
        fits = enc <= lim
        checks.append(_check("encoded_size_recomputed", data.get("encoded_bytes") == enc, f"4·ceil(n/3) = {enc}"))
        checks.append(_check("fit_decision", data.get("fits") is fits, f"fits={fits}"))
        checks.append(_check("plan_matches", data.get("plan") == ("attach" if fits else "share_link"), "share a link when it will not fit"))
    return _result("lab_dco_attachment_fit", COURSE, checks, B_DCO)


def rule_321(copies: list[dict[str, Any]]) -> dict[str, bool]:
    return {
        "three_copies": len(copies) >= 3,
        "two_media": len({str(c.get("media")) for c in copies}) >= 2,
        "one_offsite": any(c.get("offsite") is True for c in copies),
    }


def lab_dco_backup_321(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_backup_321", COURSE, submission, ["copies", "three_copies", "two_media", "one_offsite", "restore_tested", "plan_ok"], B_DCO,
    )
    if data is None:
        return _result("lab_dco_backup_321", COURSE, checks, B_DCO)
    copies = [c for c in data.get("copies") or [] if isinstance(c, dict)]
    truth = rule_321(copies)
    for key, val in truth.items():
        checks.append(_check(f"{key}_recomputed", data.get(key) is val, f"{key}={val}"))
    ok = all(truth.values()) and data.get("restore_tested") is True
    checks.append(_check("plan_verdict", data.get("plan_ok") is ok, "3-2-1 and a tested restore"))
    return _result("lab_dco_backup_321", COURSE, checks, B_DCO)


def _lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast_ratio(fg: str, bg: str) -> float:
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def lab_dco_contrast(submission: Any = None) -> LabResult:
    data, checks = _require_student("lab_dco_contrast", COURSE, submission, ["pairs"], B_DCO)
    if data is None:
        return _result("lab_dco_contrast", COURSE, checks, B_DCO)
    pairs = data.get("pairs") if isinstance(data.get("pairs"), list) else []
    checks.append(_check("two_pairs", len(pairs) >= 2, f"pairs={len(pairs)}"))
    bad = 0
    for p in pairs:
        try:
            r = contrast_ratio(str(p["fg"]), str(p["bg"]))
        except (KeyError, ValueError, TypeError):
            bad += 1
            continue
        if not (_close(p.get("ratio"), r, 0.01) and p.get("aa_normal") is (r >= 4.5) and p.get("aa_large") is (r >= 3.0)):
            bad += 1
    checks.append(_check("ratios_recomputed", bool(pairs) and bad == 0, f"wrong={bad}"))
    return _result("lab_dco_contrast", COURSE, checks, B_DCO)


def lab_dco_safety_plan(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dco_safety_plan", COURSE, submission,
        ["labs_passed", "password_manager", "mfa_on_email", "backup_copies", "restore_tested", "report_phish_to", "real_passwords_included"],
        B_DCO,
    )
    if data is None:
        return _result("lab_dco_safety_plan", COURSE, checks, B_DCO)
    checks.append(_check("labs_passed", isinstance(data.get("labs_passed"), int) and data["labs_passed"] >= 6, "≥6 prior labs"))
    checks.append(_check("password_manager", data.get("password_manager") is True, "unique secrets need a manager"))
    checks.append(_check("mfa_on_email", data.get("mfa_on_email") is True, "email resets everything else"))
    copies = [c for c in data.get("backup_copies") or [] if isinstance(c, dict)]
    checks.append(_check("backup_321", all(rule_321(copies).values()) and data.get("restore_tested") is True, "3-2-1 + restore test"))
    checks.append(_check("phish_contact", len(str(data.get("report_phish_to") or "").strip()) >= 3, "who to tell"))
    checks.append(_check("no_real_passwords", data.get("real_passwords_included") is False, "plan never holds secrets"))
    return _result("lab_dco_safety_plan", COURSE, checks, B_DCO)


LAB_ORDER_DCO = [
    "lab_dco_paths", "lab_dco_storage_units", "lab_dco_entropy", "lab_dco_link_check", "lab_dco_sheet_formulas",
    "lab_dco_typing_wpm", "lab_dco_attachment_fit", "lab_dco_backup_321", "lab_dco_contrast", "lab_dco_safety_plan",
]
LABS_DCO = {name: globals()[name] for name in LAB_ORDER_DCO}

_PHISH_URL = "https://account.harborbank.example.verify-login.example.net/session"
_COPIES = [
    {"name": "laptop", "media": "ssd", "offsite": False},
    {"name": "usb drive at home", "media": "hdd", "offsite": False},
    {"name": "cloud folder", "media": "cloud", "offsite": True},
]
_STORE = storage_check(500, 1200, 4.2, 4.5)
_BUDGET = {"rent": 650, "food": 240, "bus pass": 55, "phone": 35, "savings": 120}
_TYPE = typing_scores(1250, 5, 15)
_SCHEMES = [("four diceware words", 7776, 4), ("eight random printable", 95, 8), ("twelve lowercase letters", 26, 12)]

REFERENCE_DCO: dict[str, dict[str, Any]] = {
    "lab_dco_paths": {"tasks": [
        {"cwd": "/home/ana/Documents/letters", "relative": "../photos/2026/../summer.jpg",
         "absolute": resolve_path("/home/ana/Documents/letters", "../photos/2026/../summer.jpg")},
        {"cwd": "/home/ana", "relative": "./Downloads/form.pdf", "absolute": resolve_path("/home/ana", "./Downloads/form.pdf")},
    ]},
    "lab_dco_storage_units": {
        "drive_gb": 500, "shown_gib": round(_STORE["shown_gib"], 2), "photo_count": 1200, "photo_mb": 4.2,
        "photos_gib": round(_STORE["photos_gib"], 3), "free_gib": 4.5, "fits": _STORE["fits"],
    },
    "lab_dco_entropy": {
        "schemes": [{"name": n, "pool": p, "length": length, "bits": round(entropy_bits(p, length), 2)} for n, p, length in _SCHEMES],
        "strongest": "twelve lowercase letters", "reuse_allowed": False, "forced_rotation_without_cause": False,
    },
    "lab_dco_link_check": {
        "url": _PHISH_URL, "expected_domain": "harborbank.example",
        "hostname": registered_domain(_PHISH_URL)[0], "registered_domain": registered_domain(_PHISH_URL)[1], "safe_to_open": False,
    },
    "lab_dco_sheet_formulas": {
        "rows": _BUDGET, "total": 1100, "average": 220, "largest_item": "rent",
        "share_item": "food", "share_pct": round(100 * 240 / 1100, 2),
    },
    "lab_dco_typing_wpm": {"chars": 1250, "minutes": 5, "errors": 15, **{k: round(v, 2) for k, v in _TYPE.items()}},
    "lab_dco_attachment_fit": {
        "file_bytes": 19_000_000, "limit_bytes": 25_000_000, "encoded_bytes": base64_size(19_000_000),
        "fits": False, "plan": "share_link",
    },
    "lab_dco_backup_321": {"copies": _COPIES, **rule_321(_COPIES), "restore_tested": True, "plan_ok": True},
    "lab_dco_contrast": {"pairs": [
        {"fg": fg, "bg": "#ffffff", "ratio": round(contrast_ratio(fg, "#ffffff"), 2),
         "aa_normal": contrast_ratio(fg, "#ffffff") >= 4.5, "aa_large": contrast_ratio(fg, "#ffffff") >= 3.0}
        for fg in ("#767676", "#777777")
    ]},
    "lab_dco_safety_plan": {
        "labs_passed": 8, "password_manager": True, "mfa_on_email": True, "backup_copies": _COPIES,
        "restore_tested": True, "report_phish_to": "library IT desk", "real_passwords_included": False,
    },
}

WRONG_DCO: dict[str, dict[str, Any]] = {
    "lab_dco_paths": {"tasks": [{"cwd": "Documents", "relative": "../photos/summer.jpg", "absolute": "/photos/summer.jpg"}]},
    "lab_dco_storage_units": {"drive_gb": 500, "shown_gib": 500, "photo_count": 1200, "photo_mb": 4.2,
                              "photos_gib": 5.04, "free_gib": 4.5, "fits": True},
    "lab_dco_entropy": {"schemes": [{"name": "P@ssw0rd!", "pool": 95, "length": 9, "bits": 100}], "strongest": "P@ssw0rd!",
                        "reuse_allowed": True, "forced_rotation_without_cause": True},
    "lab_dco_link_check": {"url": _PHISH_URL, "expected_domain": "harborbank.example", "hostname": "account.harborbank.example",
                           "registered_domain": "harborbank.example", "safe_to_open": True},
    "lab_dco_sheet_formulas": {"rows": _BUDGET, "total": 1000, "average": 200, "largest_item": "food", "share_item": "food", "share_pct": 24},
    "lab_dco_typing_wpm": {"chars": 1250, "minutes": 5, "errors": 15, "gross_wpm": 250, "net_wpm": 235, "accuracy_pct": 85},
    "lab_dco_attachment_fit": {"file_bytes": 19_000_000, "limit_bytes": 25_000_000, "encoded_bytes": 19_000_000, "fits": True, "plan": "attach"},
    "lab_dco_backup_321": {"copies": _COPIES[:2], "three_copies": True, "two_media": True, "one_offsite": True,
                           "restore_tested": False, "plan_ok": True},
    "lab_dco_contrast": {"pairs": [{"fg": "#777777", "bg": "#ffffff", "ratio": 4.5, "aa_normal": True, "aa_large": True}]},
    "lab_dco_safety_plan": {"labs_passed": 1, "password_manager": False, "mfa_on_email": False, "backup_copies": [],
                            "restore_tested": False, "report_phish_to": "", "real_passwords_included": True},
}

LAB_SPECS_DCO: dict[str, dict[str, Any]] = {
    "lab_dco_paths": {
        "title": "Folders and paths — where does ../ actually land?",
        "readme": "For at least two tasks give cwd (absolute), a relative path, and the absolute path it resolves to. At least one relative path must climb with ..",
        "wrong_hint": "A cwd that is not absolute, or forgetting that .. cancels the folder before it, fails.",
    },
    "lab_dco_storage_units": {
        "title": "Storage units — the 500 GB drive that shows 465 GiB",
        "readme": "Convert the box size to GiB, total the photo folder in GiB (MB = 10^6 bytes), and decide whether it fits in the free GiB.",
        "wrong_hint": "Mixing decimal GB with binary GiB makes the photos look like they fit; they do not.",
    },
    "lab_dco_entropy": {
        "title": "Password strength — bits from pool size and length",
        "readme": "List at least three generation schemes with pool and length, compute bits = length × log2(pool), name the strongest, and set reuse_allowed and forced_rotation_without_cause to false.",
        "wrong_hint": "Scoring a dictionary word with symbol swaps as if it were random fails.",
    },
    "lab_dco_link_check": {
        "title": "Reading a link — hostname, registered domain, decision",
        "readme": "Pull the hostname out of the URL, read the registered domain from the right (last two labels for these example links), and decide safe_to_open against the expected domain.",
        "wrong_hint": "Trusting the familiar word at the left of the hostname fails.",
    },
    "lab_dco_sheet_formulas": {
        "title": "Spreadsheet formulas — SUM, AVERAGE, MAX, share of total",
        "readme": "Enter a budget of at least four rows, then report total, average, the largest item, and one item's share as a percentage.",
        "wrong_hint": "Typing a total by hand that disagrees with the rows fails.",
    },
    "lab_dco_typing_wpm": {
        "title": "Keyboard fluency — gross WPM, net WPM, accuracy",
        "readme": "From characters typed, minutes, and uncorrected errors, compute gross WPM (chars/5/min), net WPM (gross − errors/min), and accuracy.",
        "wrong_hint": "Forgetting the five-characters-per-word convention fails.",
    },
    "lab_dco_attachment_fit": {
        "title": "Attachments — base64 growth against the mail limit",
        "readme": "Compute the encoded size 4·ceil(bytes/3), compare it with the limit, and choose attach or share_link.",
        "wrong_hint": "Comparing the raw file size with the limit fails for files near the edge.",
    },
    "lab_dco_backup_321": {
        "title": "Backups — three copies, two media, one offsite, one tested restore",
        "readme": "List every copy with media type and offsite flag, evaluate each 3-2-1 rule, and set plan_ok only if a restore was tested.",
        "wrong_hint": "Calling two copies on one drive a backup plan fails.",
    },
    "lab_dco_contrast": {
        "title": "Readable screens — WCAG contrast ratio",
        "readme": "For at least two colour pairs compute the WCAG 2.2 contrast ratio and report aa_normal (≥ 4.5) and aa_large (≥ 3.0).",
        "wrong_hint": "Eyeballing #777777 on white as passing AA normal text fails; it is 4.48:1.",
    },
    "lab_dco_safety_plan": {
        "title": "Personal digital safety plan",
        "readme": "labs_passed ≥ 6; password manager and MFA on email; a 3-2-1 backup with a tested restore; a named place to report phishing; no real passwords in the plan.",
        "wrong_hint": "A plan that lists actual passwords fails immediately.",
    },
}
