"""Runnable labs for batch007 — EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB."""
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
        return {"lab_id": self.lab_id, "course_id": self.course_id, "ok": self.ok,
                "checks": self.checks, "claim_boundary": self.boundary, "boundary": self.boundary}

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

B_EP = "EMBEDDED_PROTOTYPING ForgeSense Subsystem Bench. Not student/teacher E6. PHYSICAL_PENDING for solder/OTA."
B_GPL = "GUNNCHOS_PRODUCT_LAB Product Bench. Not student/teacher E6. Do not merge device-os #103."

def lab_ep_memory_map(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_memory_map", "EMBEDDED_PROTOTYPING", submission,
        ["flash_base", "sram_base", "vector_table_offset", "physical_status"], B_EP,
    )
    if data is None:
        return _result("lab_ep_memory_map", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("flash", str(data.get("flash_base") or "").startswith("0x"), "flash"))
    checks.append(_check("sram", str(data.get("sram_base") or "").startswith("0x"), "sram"))
    checks.append(_check("vto", int(str(data.get("vector_table_offset") or "0"), 0) >= 0, "vto"))
    checks.append(_check("physical", data.get("physical_status") == "PHYSICAL_PENDING", "physical"))
    return _result("lab_ep_memory_map", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_gpio_contract(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_gpio_contract", "EMBEDDED_PROTOTYPING", submission,
        ["pin", "direction", "default_level", "pull"], B_EP,
    )
    if data is None:
        return _result("lab_ep_gpio_contract", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("pin", data.get("pin") == "LED0", "pin"))
    checks.append(_check("dir", data.get("direction") == "out", "dir"))
    checks.append(_check("level", data.get("default_level") in (0, 1, False, True), "level"))
    checks.append(_check("pull", data.get("pull") in ("none", "up", "down"), "pull"))
    return _result("lab_ep_gpio_contract", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_i2c_timing(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_i2c_timing", "EMBEDDED_PROTOTYPING", submission,
        ["bus", "addr", "freq_khz", "nack_recovery"], B_EP,
    )
    if data is None:
        return _result("lab_ep_i2c_timing", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("bus", data.get("bus") == "i2c1", "bus"))
    checks.append(_check("addr", str(data.get("addr") or "").lower() in ("0x3c", "60"), "addr"))
    checks.append(_check("freq", int(data.get("freq_khz") or 0) == 100, "freq"))
    checks.append(_check("nack", data.get("nack_recovery") is True, "nack"))
    return _result("lab_ep_i2c_timing", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_spi_flash(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_spi_flash", "EMBEDDED_PROTOTYPING", submission,
        ["opcode", "addr", "read_len", "crc_ok"], B_EP,
    )
    if data is None:
        return _result("lab_ep_spi_flash", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("op", int(str(data.get("opcode") or "0"), 0) == 0x03, "op"))
    checks.append(_check("len", int(data.get("read_len") or 0) >= 1, "len"))
    checks.append(_check("crc", data.get("crc_ok") is True, "crc"))
    checks.append(_check("addr", str(data.get("addr") or "").startswith("0x"), "addr"))
    return _result("lab_ep_spi_flash", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_adc_scale(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_adc_scale", "EMBEDDED_PROTOTYPING", submission,
        ["raw", "vref_mv", "resolution_bits", "mv"], B_EP,
    )
    if data is None:
        return _result("lab_ep_adc_scale", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("raw", 0 <= int(data.get("raw") or -1) <= 4095, "raw"))
    checks.append(_check("vref", int(data.get("vref_mv") or 0) == 3300, "vref"))
    checks.append(_check("bits", int(data.get("resolution_bits") or 0) == 12, "bits"))
    checks.append(_check("mv", abs(int(data.get("mv") or -1) - 1650) <= 50, "mv"))
    return _result("lab_ep_adc_scale", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_isr_vs_poll(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_isr_vs_poll", "EMBEDDED_PROTOTYPING", submission,
        ["mode", "max_latency_us", "missed_edges"], B_EP,
    )
    if data is None:
        return _result("lab_ep_isr_vs_poll", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("mode", data.get("mode") == "isr", "mode"))
    checks.append(_check("lat", int(data.get("max_latency_us") if data.get("max_latency_us") is not None else 9999) <= 250, "lat"))
    checks.append(_check("miss", data.get("missed_edges") is not None and int(data.get("missed_edges")) == 0, "miss"))
    return _result("lab_ep_isr_vs_poll", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_zephyr_qemu(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_zephyr_qemu", "EMBEDDED_PROTOTYPING", submission,
        ["board", "qemu_ok", "physical_status"], B_EP,
    )
    if data is None:
        return _result("lab_ep_zephyr_qemu", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("board", data.get("board") == "qemu_cortex_m0", "board"))
    checks.append(_check("qemu", data.get("qemu_ok") is True, "qemu"))
    checks.append(_check("physical", data.get("physical_status") == "PHYSICAL_PENDING", "physical"))
    return _result("lab_ep_zephyr_qemu", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_dt_overlay(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_dt_overlay", "EMBEDDED_PROTOTYPING", submission,
        ["overlay_has_i2c1", "overlay_has_led0", "delete_soc"], B_EP,
    )
    if data is None:
        return _result("lab_ep_dt_overlay", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("i2c", data.get("overlay_has_i2c1") is True, "i2c"))
    checks.append(_check("led", data.get("overlay_has_led0") is True, "led"))
    checks.append(_check("soc", data.get("delete_soc") is False, "soc"))
    return _result("lab_ep_dt_overlay", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_sleep_mode(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_sleep_mode", "EMBEDDED_PROTOTYPING", submission,
        ["sleep_mode", "wake_gpio", "wake_latency_ms"], B_EP,
    )
    if data is None:
        return _result("lab_ep_sleep_mode", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("mode", data.get("sleep_mode") in ("SYSTEM_OFF", "SLEEP"), "mode"))
    checks.append(_check("gpio", data.get("wake_gpio") == "BTN0", "gpio"))
    checks.append(_check("lat", int(data.get("wake_latency_ms") or 999) <= 20, "lat"))
    return _result("lab_ep_sleep_mode", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_ep_subsystem_capstone(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ep_subsystem_capstone", "EMBEDDED_PROTOTYPING", submission,
        ["labs_passed", "qemu_ok", "dt_ok", "physical_status", "no_key_leak"], B_EP,
    )
    if data is None:
        return _result("lab_ep_subsystem_capstone", "EMBEDDED_PROTOTYPING", checks, B_EP)
    checks.append(_check("labs", int(data.get("labs_passed") or 0) >= 6, "labs"))
    checks.append(_check("qemu", data.get("qemu_ok") is True, "qemu"))
    checks.append(_check("dt", data.get("dt_ok") is True, "dt"))
    checks.append(_check("physical", data.get("physical_status") == "PHYSICAL_PENDING", "physical"))
    checks.append(_check("keys", data.get("no_key_leak") is True, "keys"))
    return _result("lab_ep_subsystem_capstone", "EMBEDDED_PROTOTYPING", checks, B_EP)

def lab_gpl_product_charter(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_product_charter", "GUNNCHOS_PRODUCT_LAB", submission,
        ["problem", "goal_metric", "in_scope", "out_scope", "fabricated_outcomes"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_product_charter", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("problem", len(str(data.get("problem") or "")) >= 8, "problem"))
    checks.append(_check("goal", len(str(data.get("goal_metric") or "")) >= 8, "goal"))
    checks.append(_check("scope", isinstance(data.get("in_scope"), list) and len(data.get("in_scope") or []) >= 1, "scope"))
    checks.append(_check("out", isinstance(data.get("out_scope"), list), "out"))
    checks.append(_check("fab", data.get("fabricated_outcomes") is False, "fab"))
    return _result("lab_gpl_product_charter", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_compat_matrix(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_compat_matrix", "GUNNCHOS_PRODUCT_LAB", submission,
        ["device_os_sha", "gunnchai_sha", "contract_ok"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_compat_matrix", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("dos", len(str(data.get("device_os_sha") or "")) >= 7, "dos"))
    checks.append(_check("ai", len(str(data.get("gunnchai_sha") or "")) >= 7, "ai"))
    checks.append(_check("ok", data.get("contract_ok") is True, "ok"))
    return _result("lab_gpl_compat_matrix", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_checkout_flow(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_checkout_flow", "GUNNCHOS_PRODUCT_LAB", submission,
        ["states", "orphan_state"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_checkout_flow", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("states", isinstance(data.get("states"), list) and len(data.get("states") or []) >= 4, "states"))
    checks.append(_check("orphan", data.get("orphan_state") is False, "orphan"))
    return _result("lab_gpl_checkout_flow", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_compose_health(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_compose_health", "GUNNCHOS_PRODUCT_LAB", submission,
        ["migrate_ok", "health", "rollback_to", "current_digest"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_compose_health", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("mig", data.get("migrate_ok") is True, "mig"))
    checks.append(_check("health", data.get("health") == "healthy", "health"))
    checks.append(_check("rb", str(data.get("rollback_to") or "") != str(data.get("current_digest") or ""), "rb"))
    checks.append(_check("digest", len(str(data.get("current_digest") or "")) >= 12, "digest"))
    return _result("lab_gpl_compose_health", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_privacy_bom(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_privacy_bom", "GUNNCHOS_PRODUCT_LAB", submission,
        ["fields", "pii_in_bom", "retention_days"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_privacy_bom", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("fields", isinstance(data.get("fields"), list) and len(data.get("fields") or []) >= 2, "fields"))
    checks.append(_check("pii", data.get("pii_in_bom") is False, "pii"))
    checks.append(_check("ret", int(data.get("retention_days") or 0) >= 1, "ret"))
    return _result("lab_gpl_privacy_bom", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_guest_protocol(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_guest_protocol", "GUNNCHOS_PRODUCT_LAB", submission,
        ["ping_ok", "boot_status", "protocol_version"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_guest_protocol", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("ping", data.get("ping_ok") is True, "ping"))
    checks.append(_check("boot", data.get("boot_status") == "ready", "boot"))
    checks.append(_check("ver", str(data.get("protocol_version") or "").startswith("wp"), "ver"))
    return _result("lab_gpl_guest_protocol", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_release_notes(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_release_notes", "GUNNCHOS_PRODUCT_LAB", submission,
        ["semver", "breaking", "changelog_entries"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_release_notes", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("sem", len(str(data.get("semver") or "")) >= 5, "sem"))
    checks.append(_check("brk", data.get("breaking") is False, "brk"))
    checks.append(_check("entries", int(data.get("changelog_entries") or 0) >= 1, "entries"))
    return _result("lab_gpl_release_notes", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_ci_tokens(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_ci_tokens", "GUNNCHOS_PRODUCT_LAB", submission,
        ["tokens_passed", "tokens_total", "fabricated_green"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_ci_tokens", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("pass", int(data.get("tokens_passed") or 0) >= 1, "pass"))
    checks.append(_check("tot", int(data.get("tokens_total") or 0) >= int(data.get("tokens_passed") or 0), "tot"))
    checks.append(_check("fab", data.get("fabricated_green") is False, "fab"))
    return _result("lab_gpl_ci_tokens", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_dep_pin(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_dep_pin", "GUNNCHOS_PRODUCT_LAB", submission,
        ["preview_sha_in_accepted", "pin_file"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_dep_pin", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("prev", data.get("preview_sha_in_accepted") is False, "prev"))
    checks.append(_check("pin", data.get("pin_file") == "CURRENT_ACCEPTED_MAIN.json", "pin"))
    return _result("lab_gpl_dep_pin", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

def lab_gpl_product_capstone(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_gpl_product_capstone", "GUNNCHOS_PRODUCT_LAB", submission,
        ["labs_passed", "compat_ok", "no_device_os_pr", "no_key_leak"], B_GPL,
    )
    if data is None:
        return _result("lab_gpl_product_capstone", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)
    checks.append(_check("labs", int(data.get("labs_passed") or 0) >= 6, "labs"))
    checks.append(_check("compat", data.get("compat_ok") is True, "compat"))
    checks.append(_check("pr", data.get("no_device_os_pr") is True, "pr"))
    checks.append(_check("keys", data.get("no_key_leak") is True, "keys"))
    return _result("lab_gpl_product_capstone", "GUNNCHOS_PRODUCT_LAB", checks, B_GPL)

LABS_007 = {
    "lab_ep_memory_map": lab_ep_memory_map,
    "lab_ep_gpio_contract": lab_ep_gpio_contract,
    "lab_ep_i2c_timing": lab_ep_i2c_timing,
    "lab_ep_spi_flash": lab_ep_spi_flash,
    "lab_ep_adc_scale": lab_ep_adc_scale,
    "lab_ep_isr_vs_poll": lab_ep_isr_vs_poll,
    "lab_ep_zephyr_qemu": lab_ep_zephyr_qemu,
    "lab_ep_dt_overlay": lab_ep_dt_overlay,
    "lab_ep_sleep_mode": lab_ep_sleep_mode,
    "lab_ep_subsystem_capstone": lab_ep_subsystem_capstone,
    "lab_gpl_product_charter": lab_gpl_product_charter,
    "lab_gpl_compat_matrix": lab_gpl_compat_matrix,
    "lab_gpl_checkout_flow": lab_gpl_checkout_flow,
    "lab_gpl_compose_health": lab_gpl_compose_health,
    "lab_gpl_privacy_bom": lab_gpl_privacy_bom,
    "lab_gpl_guest_protocol": lab_gpl_guest_protocol,
    "lab_gpl_release_notes": lab_gpl_release_notes,
    "lab_gpl_ci_tokens": lab_gpl_ci_tokens,
    "lab_gpl_dep_pin": lab_gpl_dep_pin,
    "lab_gpl_product_capstone": lab_gpl_product_capstone
}

COURSE_LABS_007 = {
    "EMBEDDED_PROTOTYPING": ["lab_ep_memory_map", "lab_ep_gpio_contract", "lab_ep_i2c_timing", "lab_ep_spi_flash", "lab_ep_adc_scale", "lab_ep_isr_vs_poll", "lab_ep_zephyr_qemu", "lab_ep_dt_overlay", "lab_ep_sleep_mode", "lab_ep_subsystem_capstone"],
    "GUNNCHOS_PRODUCT_LAB": ["lab_gpl_product_charter", "lab_gpl_compat_matrix", "lab_gpl_checkout_flow", "lab_gpl_compose_health", "lab_gpl_privacy_bom", "lab_gpl_guest_protocol", "lab_gpl_release_notes", "lab_gpl_ci_tokens", "lab_gpl_dep_pin", "lab_gpl_product_capstone"],
}

LAB_SPECS_007 = {
    "lab_ep_memory_map": {
        "title": "ep_memory_map",
        "readme": "lab_ep_memory_map fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_gpio_contract": {
        "title": "ep_gpio_contract",
        "readme": "lab_ep_gpio_contract fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_i2c_timing": {
        "title": "ep_i2c_timing",
        "readme": "lab_ep_i2c_timing fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_spi_flash": {
        "title": "ep_spi_flash",
        "readme": "lab_ep_spi_flash fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_adc_scale": {
        "title": "ep_adc_scale",
        "readme": "lab_ep_adc_scale fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_isr_vs_poll": {
        "title": "ep_isr_vs_poll",
        "readme": "lab_ep_isr_vs_poll fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_zephyr_qemu": {
        "title": "ep_zephyr_qemu",
        "readme": "lab_ep_zephyr_qemu fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_dt_overlay": {
        "title": "ep_dt_overlay",
        "readme": "lab_ep_dt_overlay fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_sleep_mode": {
        "title": "ep_sleep_mode",
        "readme": "lab_ep_sleep_mode fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_ep_subsystem_capstone": {
        "title": "ep_subsystem_capstone",
        "readme": "lab_ep_subsystem_capstone fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "EMBEDDED_PROTOTYPING"
    },
    "lab_gpl_product_charter": {
        "title": "gpl_product_charter",
        "readme": "lab_gpl_product_charter fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_compat_matrix": {
        "title": "gpl_compat_matrix",
        "readme": "lab_gpl_compat_matrix fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_checkout_flow": {
        "title": "gpl_checkout_flow",
        "readme": "lab_gpl_checkout_flow fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_compose_health": {
        "title": "gpl_compose_health",
        "readme": "lab_gpl_compose_health fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_privacy_bom": {
        "title": "gpl_privacy_bom",
        "readme": "lab_gpl_privacy_bom fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_guest_protocol": {
        "title": "gpl_guest_protocol",
        "readme": "lab_gpl_guest_protocol fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_release_notes": {
        "title": "gpl_release_notes",
        "readme": "lab_gpl_release_notes fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_ci_tokens": {
        "title": "gpl_ci_tokens",
        "readme": "lab_gpl_ci_tokens fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_dep_pin": {
        "title": "gpl_dep_pin",
        "readme": "lab_gpl_dep_pin fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    },
    "lab_gpl_product_capstone": {
        "title": "gpl_product_capstone",
        "readme": "lab_gpl_product_capstone fixture JSON.",
        "required_keys": [],
        "wrong_hint": "Wrong/empty/print-PASS fail.",
        "course_id": "GUNNCHOS_PRODUCT_LAB"
    }
}

REFERENCE_007 = {
    "lab_ep_memory_map": {
        "flash_base": "0x00000000",
        "sram_base": "0x20000000",
        "vector_table_offset": "0x100",
        "physical_status": "PHYSICAL_PENDING"
    },
    "lab_ep_gpio_contract": {
        "pin": "LED0",
        "direction": "out",
        "default_level": 0,
        "pull": "none"
    },
    "lab_ep_i2c_timing": {
        "bus": "i2c1",
        "addr": "0x3C",
        "freq_khz": 100,
        "nack_recovery": True
    },
    "lab_ep_spi_flash": {
        "opcode": "0x03",
        "addr": "0x00001000",
        "read_len": 16,
        "crc_ok": True
    },
    "lab_ep_adc_scale": {
        "raw": 2048,
        "vref_mv": 3300,
        "resolution_bits": 12,
        "mv": 1650
    },
    "lab_ep_isr_vs_poll": {
        "mode": "isr",
        "max_latency_us": 200,
        "missed_edges": 0
    },
    "lab_ep_zephyr_qemu": {
        "board": "qemu_cortex_m0",
        "qemu_ok": True,
        "physical_status": "PHYSICAL_PENDING"
    },
    "lab_ep_dt_overlay": {
        "overlay_has_i2c1": True,
        "overlay_has_led0": True,
        "delete_soc": False
    },
    "lab_ep_sleep_mode": {
        "sleep_mode": "SYSTEM_OFF",
        "wake_gpio": "BTN0",
        "wake_latency_ms": 5
    },
    "lab_ep_subsystem_capstone": {
        "labs_passed": 9,
        "qemu_ok": True,
        "dt_ok": True,
        "physical_status": "PHYSICAL_PENDING",
        "no_key_leak": True
    },
    "lab_gpl_product_charter": {
        "problem": "checkout wait",
        "goal_metric": "median_wait_minutes",
        "in_scope": [
            "queue"
        ],
        "out_scope": [
            "new building"
        ],
        "fabricated_outcomes": False
    },
    "lab_gpl_compat_matrix": {
        "device_os_sha": "d5c2d17",
        "gunnchai_sha": "d357846",
        "contract_ok": True
    },
    "lab_gpl_checkout_flow": {
        "states": [
            "requested",
            "approved",
            "checked_out",
            "returned"
        ],
        "orphan_state": False
    },
    "lab_gpl_compose_health": {
        "migrate_ok": True,
        "health": "healthy",
        "rollback_to": "abc111",
        "current_digest": "def222222222"
    },
    "lab_gpl_privacy_bom": {
        "fields": [
            "camera",
            "mic"
        ],
        "pii_in_bom": False,
        "retention_days": 30
    },
    "lab_gpl_guest_protocol": {
        "ping_ok": True,
        "boot_status": "ready",
        "protocol_version": "wp011r"
    },
    "lab_gpl_release_notes": {
        "semver": "1.4.0",
        "breaking": False,
        "changelog_entries": 3
    },
    "lab_gpl_ci_tokens": {
        "tokens_passed": 4,
        "tokens_total": 4,
        "fabricated_green": False
    },
    "lab_gpl_dep_pin": {
        "preview_sha_in_accepted": False,
        "pin_file": "CURRENT_ACCEPTED_MAIN.json"
    },
    "lab_gpl_product_capstone": {
        "labs_passed": 9,
        "compat_ok": True,
        "no_device_os_pr": True,
        "no_key_leak": True
    }
}

WRONG_007 = {
    "lab_ep_memory_map": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_gpio_contract": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_i2c_timing": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_spi_flash": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_adc_scale": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_isr_vs_poll": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_zephyr_qemu": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_dt_overlay": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_sleep_mode": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_ep_subsystem_capstone": {
        "physical_status": "SHIPPED",
        "qemu_ok": False,
        "delete_soc": True
    },
    "lab_gpl_product_charter": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_compat_matrix": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_checkout_flow": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_compose_health": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_privacy_bom": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_guest_protocol": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_release_notes": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_ci_tokens": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_dep_pin": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    },
    "lab_gpl_product_capstone": {
        "fabricated_outcomes": True,
        "contract_ok": False,
        "no_key_leak": False,
        "preview_sha_in_accepted": True
    }
}

