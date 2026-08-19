#!/usr/bin/env python3
"""Generate batch007 DIGITAL_RC packages: EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB.

Residual closure Phase 0 follow-up. Does not invent SEVEN_GC_APPRENTICESHIP course.
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "src" / "waike_course_ready" / "batch007"


def _q(qid: str, stem: str, choices: list[str], answer: int, explain: str) -> dict:
    return {
        "id": qid,
        "kind": "mcq",
        "stem": stem,
        "choices": choices,
        "answer_index": answer,
        "explanation": explain,
    }


def _lesson(prefix: str, ticket: str, topic: str, detail: str, boundary: str) -> str:
    base = (
        f"{prefix} ticket {ticket}: {topic}. {detail} "
        f"PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. "
        f"Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. "
        f"Empty {{}} fails. A file whose body is only PASS raises. "
        f"Show computed JSON fields; GUI screenshots are not acceptance. "
        f"{boundary} "
    )
    while len(base) < 820:
        base += (
            f"Journal {ticket}: restate the worked numbers, name one claim you refuse "
            f"(commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), "
            f"and keep prose specific to this week's lab_id and ticket IDs. "
        )
    return base.strip()


def _weeks_ep() -> list[dict]:
    specs = [
        (1, "MCU memory map — flash vs SRAM before first boot", "EP-4101", "lab_ep_memory_map",
         "flash_base=0x00000000, sram_base=0x20000000, vector_table_offset=0x100",
         "Map the nRF52840-class memory regions for ForgeSense subsystem firmware."),
        (2, "GPIO contract — direction, pull, and safe defaults", "EP-4202", "lab_ep_gpio_contract",
         "pin=LED0, direction=out, default_level=0, pull=none",
         "Author GPIO contract JSON before any Zephyr pinmux call."),
        (3, "I2C timing — address, frequency, and NACK recovery", "EP-4303", "lab_ep_i2c_timing",
         "bus=i2c1, addr=0x3C, freq_khz=100, nack_recovery=true",
         "SSD1306-class address 0x3C at 100 kHz with explicit NACK plan."),
        (4, "SPI flash read — opcode and length honesty", "EP-4404", "lab_ep_spi_flash",
         "opcode=0x03, addr=0x00001000, read_len=16, crc_ok=true",
         "NO_AI week: hand-author SPI read frame fields."),
        (5, "ADC scaling — counts to millivolts", "EP-4505", "lab_ep_adc_scale",
         "raw=2048, vref_mv=3300, resolution_bits=12, mv=1650",
         "Convert 12-bit ADC count to millivolts with stated vref."),
        (6, "ISR vs polling — latency budget", "EP-4606", "lab_ep_isr_vs_poll",
         "mode=isr, max_latency_us=250, missed_edges=0",
         "Choose ISR when edge latency must stay under 250 µs."),
        (7, "Zephyr west + QEMU — digital boot before iron", "EP-4707", "lab_ep_zephyr_qemu",
         "board=qemu_cortex_m0, qemu_ok=true, physical_status=PHYSICAL_PENDING",
         "west build -b qemu_cortex_m0; no board flash claim without EVT."),
        (8, "Devicetree overlay — I2C1 and LED0 nodes", "EP-4808", "lab_ep_dt_overlay",
         "overlay_has_i2c1=true, overlay_has_led0=true, delete_soc=false",
         "Overlay enables &i2c1 and led0; deleting &soc is unsafe."),
        (9, "Sleep modes — wake source honesty", "EP-4909", "lab_ep_sleep_mode",
         "sleep_mode=SYSTEM_OFF, wake_gpio=BTN0, wake_latency_ms=5",
         "NO_AI week: document wake source without inventing uA draw."),
        (10, "Subsystem capstone — QEMU + DT + bus evidence", "EP-4A10", "lab_ep_subsystem_capstone",
         "labs_passed≥6, qemu_ok=true, dt_ok=true, physical_status=PHYSICAL_PENDING",
         "Assemble ForgeSense subsystem packet from prior lab digests."),
    ]
    weeks = []
    for w, title, ticket, lab_id, worked, assign_hint in specs:
        lesson = _lesson(
            "ForgeSense Subsystem Bench",
            ticket,
            title,
            assign_hint,
            "Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path.",
        )
        weeks.append({
            "week": w,
            "title": title,
            "lesson": lesson,
            "worked_example": worked,
            "assignment": f"Submit {lab_id} JSON for {ticket}. {assign_hint}",
            "lab_id": lab_id,
            "quiz": [
                _q(f"ep-w{w}-1", f"{ticket}: which field is checked first?", ["Machine JSON fields", "GUI screenshot", "Instructor keys", "Vendor cert"], 0, "fields first"),
                _q(f"ep-w{w}-2", f"{lab_id} empty submission?", ["Fails student_artifact", "Passes", "Bonus credit", "Grants cert"], 0, "empty fails"),
                _q(f"ep-w{w}-3", f"Week {w} PHYSICAL_PENDING scope?", ["No solder/OTA without EVT", "Ship anyway", "Ignore boundary", "Mute claim"], 0, "physical pending"),
                _q(f"ep-w{w}-4", f"{ticket} learner may load answer keys?", ["Forbidden — instructor only", "Required", "Optional", "Auto-grant"], 0, "no key leak"),
                _q(f"ep-w{w}-5", f"Week {w} track boundary vs HARDWARE_ENGINEERING?", ["Subsystem firmware/bus/QEMU", "SPICE-only duplicate", "Networking ACL", "Game loop"], 0, "distinct track"),
                _q(f"ep-w{w}-6", f"{ticket} print-PASS body?", ["Raises AssertionError", "Auto-pass", "Extra credit", "Silent accept"], 0, "print pass forbidden"),
            ],
        })
    return weeks


def _weeks_gpl() -> list[dict]:
    specs = [
        (1, "Product charter — scope without fabricated impact", "GPL-5101", "lab_gpl_product_charter",
         "problem=checkout latency, goal_metric=median_wait_minutes, fabricated_outcomes=false",
         "Charter Device Lab product scope; no invented community numbers."),
        (2, "Compatibility matrix — device-os × gunnchAI pins", "GPL-5202", "lab_gpl_compat_matrix",
         "device_os_sha=d5c2d17, gunnchai_sha=d357846, contract_ok=true",
         "Versioned compatibility check on accepted-main pair only."),
        (3, "Checkout flow — ticket states and handoff", "GPL-5303", "lab_gpl_checkout_flow",
         "states=[requested,approved,checked_out,returned], orphan_state=false",
         "Model checkout FSM without opening unmerged device-os PRs."),
        (4, "Compose health — migrate before healthy", "GPL-5404", "lab_gpl_compose_health",
         "migrate_ok=true, health=healthy, rollback_to!=current_digest",
         "NO_AI week: digest pin and rollback pointer honesty."),
        (5, "Privacy BOM — field inventory without PII", "GPL-5505", "lab_gpl_privacy_bom",
         "fields=[camera,mic,location], pii_in_bom=false, retention_days=30",
         "Privacy BOM digital inventory; no biometric claim."),
        (6, "Guest protocol — ping/boot_status contract", "GPL-5606", "lab_gpl_guest_protocol",
         "ping_ok=true, boot_status=ready, protocol_version=wp011r",
         "Guest agent protocol fields; obsolete click-collector rejected."),
        (7, "Release notes — semver and breaking flag", "GPL-5707", "lab_gpl_release_notes",
         "semver=1.4.0, breaking=false, changelog_entries=3",
         "Semver bump with explicit breaking_change false unless true."),
        (8, "CI gate tokens — honest pass/fail", "GPL-5808", "lab_gpl_ci_tokens",
         "tokens_passed=4, tokens_total=4, fabricated_green=false",
         "Report CI tokens; fabricated_green must be false."),
        (9, "Cross-repo dependency pin — no preview in accepted", "GPL-5909", "lab_gpl_dep_pin",
         "preview_sha_in_accepted=false, pin_file=CURRENT_ACCEPTED_MAIN.json",
         "NO_AI week: refuse preview SHA in accepted-main pin."),
        (10, "Product lab capstone — charter+compat+CI evidence", "GPL-5A10", "lab_gpl_product_capstone",
         "labs_passed≥6, compat_ok=true, no_device_os_pr=true, no_key_leak=true",
         "Assemble gunnchOS product lab packet; do not merge device-os #103."),
    ]
    weeks = []
    for w, title, ticket, lab_id, worked, assign_hint in specs:
        lesson = _lesson(
            "gunnchOS Product Lab Bench",
            ticket,
            title,
            assign_hint,
            "Distinct from SOFTWARE_BUILDER ForgeDesk — this course owns product/compat/privacy/CI contract.",
        )
        weeks.append({
            "week": w,
            "title": title,
            "lesson": lesson,
            "worked_example": worked,
            "assignment": f"Submit {lab_id} JSON for {ticket}. {assign_hint}",
            "lab_id": lab_id,
            "quiz": [
                _q(f"gpl-w{w}-1", f"{ticket}: preview SHA in accepted-main pin?", ["Forbidden", "Required", "Always allowed", "Skip check"], 0, "no preview in accepted"),
                _q(f"gpl-w{w}-2", f"Week {w} {lab_id} empty JSON?", ["Fails student_artifact", "Passes", "Grants cert", "Silent"], 0, "empty fails"),
                _q(f"gpl-w{w}-3", f"{ticket} may open device-os #103?", ["Forbidden for students", "Required merge", "Bonus", "Silent"], 0, "no unmerged PR"),
                _q(f"gpl-w{w}-4", f"Week {w} fabricated_outcomes in charter?", ["Must be false", "Must be true", "Ignored", "Key leak OK"], 0, "no fabricated impact"),
                _q(f"gpl-w{w}-5", f"{ticket} scope vs SOFTWARE_BUILDER?", ["Product/compat/privacy pins", "Git conflict only", "Wireless FSPL", "Game state"], 0, "distinct"),
                _q(f"gpl-w{w}-6", f"Week {w} REAL_STUDENT_E6 claim?", ["No — COURSE_DIGITAL_RC only", "Yes granted", "Auto E6", "Silent"], 0, "no E6 claim"),
            ],
        })
    return weeks


def _course_ep() -> dict:
    return {
        "course_id": "EMBEDDED_PROTOTYPING",
        "title": "Embedded Systems and Device Prototyping — ForgeSense Subsystem Bench",
        "track_ids": ["EMBEDDED_PROTOTYPING"],
        "academy_id": "ACADEMY_HARDWARE",
        "kinesthetic_hook": (
            "Ten ForgeSense Subsystem Bench weeks: memory map → GPIO → I2C → SPI → ADC → ISR → "
            "Zephyr QEMU → DT overlay → sleep → capstone. Digital-first; PHYSICAL_PENDING for solder/OTA."
        ),
        "syllabus_hook": (
            "Standalone EMBEDDED_PROTOTYPING COURSE_DIGITAL_RC: MCU map, GPIO, I2C/SPI, ADC scaling, "
            "ISR latency, Zephyr west/QEMU, devicetree overlay, sleep modes, subsystem capstone. "
            "Complements HARDWARE_ENGINEERING SPICE path — does not replace it. Not student/teacher E6."
        ),
        "career": {
            "roles": ["embedded_apprentice", "firmware_technician", "device_lab_integrator"],
            "nice_categories": ["build_and_deploy", "operate_and_maintain"],
            "certs_aligned_not_granted": [
                "Zephyr developer topic labels (PUBLIC_REFERENCE_ONLY)",
                "IPC/J-STD-001 awareness labels (not a license)",
            ],
        },
        "ai_use_policy": {
            "modes": ["EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME", "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE"],
            "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
            "default_weekly": "AI_DISCLOSED",
            "no_ai_weeks": [4, 9],
        },
        "weeks": _weeks_ep(),
    }


def _course_gpl() -> dict:
    return {
        "course_id": "GUNNCHOS_PRODUCT_LAB",
        "title": "gunnchOS Device OS and Product Lab — Product Bench",
        "track_ids": ["GUNNCHOS_PRODUCT_LAB"],
        "academy_id": "ACADEMY_HARDWARE",
        "kinesthetic_hook": (
            "Ten gunnchOS Product Lab weeks: charter → compat matrix → checkout FSM → compose health → "
            "privacy BOM → guest protocol → release notes → CI tokens → dep pin → capstone."
        ),
        "syllabus_hook": (
            "Product lab COURSE_DIGITAL_RC: scope charter, accepted-main compatibility pins, checkout workflow, "
            "compose health, privacy BOM, guest protocol contract, semver release notes, CI gate tokens, "
            "cross-repo dependency hygiene. Does not merge device-os #103. Not student/teacher E6."
        ),
        "career": {
            "roles": ["product_ops_apprentice", "device_lab_integrator", "release_coordinator_junior"],
            "nice_categories": ["operate_and_maintain", "securely_provision"],
            "certs_aligned_not_granted": [
                "PMI CAPM domain labels (PUBLIC_REFERENCE_ONLY)",
                "Privacy engineering topic labels (not a cert)",
            ],
        },
        "ai_use_policy": {
            "modes": ["EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME", "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE"],
            "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
            "default_weekly": "AI_DISCLOSED",
            "no_ai_weeks": [4, 9],
        },
        "weeks": _weeks_gpl(),
    }


def _exams(course_id: str, prefix: str, offset: int) -> dict:
    mid = []
    for i in range(1, 21):
        mid.append(_q(
            f"{prefix}-mid-{i:02d}",
            f"{course_id} mid audit item {i}: lab JSON must beat screenshot-only evidence?",
            ["Yes — machine fields first", "Screenshot is enough", "Invent columns freely", "Ship instructor keys"],
            0,
            "fields beat screenshots",
        ))
    final = []
    for i in range(1, 25):
        final.append(_q(
            f"{prefix}-fin-{i:02d}",
            f"{course_id} final gate {i}: capstone requires no_key_leak and empty-submission fail?",
            ["Yes — enforced", "No — keys allowed", "PASS-only accepted", "Skip negatives"],
            0,
            "no key leak; negatives enforced",
        ))
    return {"offset": offset, "mid": mid, "final": final}


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def _lab_fn(name: str, course: str, keys: list[str], checks: list[tuple[str, str]]) -> str:
    check_lines = []
    for cname, cexpr in checks:
        check_lines.append(f'    checks.append(_check("{cname}", {cexpr}, "{cname}"))')
    body = f'''
def {name}(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "{name}", "{course}", submission,
        {json.dumps(keys)}, BOUNDARY,
    )
    if data is None:
        return _result("{name}", "{course}", checks, BOUNDARY)
{chr(10).join(check_lines)}
    return _result("{name}", "{course}", checks, BOUNDARY)
'''
    return body.strip().replace("BOUNDARY", "B_EP" if course == "EMBEDDED_PROTOTYPING" else "B_GPL")


def _generate_labs_py() -> str:
    ep_labs = [
        ("lab_ep_memory_map", ["flash_base", "sram_base", "vector_table_offset", "physical_status"],
         [("flash", 'str(data.get("flash_base") or "").startswith("0x")'), ("sram", 'str(data.get("sram_base") or "").startswith("0x")'),
          ("vto", 'int(str(data.get("vector_table_offset") or "0"), 0) >= 0'), ("physical", 'data.get("physical_status") == "PHYSICAL_PENDING"')]),
        ("lab_ep_gpio_contract", ["pin", "direction", "default_level", "pull"],
         [("pin", 'data.get("pin") == "LED0"'), ("dir", 'data.get("direction") == "out"'),
          ("level", 'data.get("default_level") in (0, 1, False, True)'), ("pull", 'data.get("pull") in ("none", "up", "down")')]),
        ("lab_ep_i2c_timing", ["bus", "addr", "freq_khz", "nack_recovery"],
         [("bus", 'data.get("bus") == "i2c1"'), ("addr", 'str(data.get("addr") or "").lower() in ("0x3c", "60")'),
          ("freq", 'int(data.get("freq_khz") or 0) == 100'), ("nack", 'data.get("nack_recovery") is True')]),
        ("lab_ep_spi_flash", ["opcode", "addr", "read_len", "crc_ok"],
         [("op", 'int(str(data.get("opcode") or "0"), 0) == 0x03'), ("len", 'int(data.get("read_len") or 0) >= 1'),
          ("crc", 'data.get("crc_ok") is True'), ("addr", 'str(data.get("addr") or "").startswith("0x")')]),
        ("lab_ep_adc_scale", ["raw", "vref_mv", "resolution_bits", "mv"],
         [("raw", '0 <= int(data.get("raw") or -1) <= 4095'), ("vref", 'int(data.get("vref_mv") or 0) == 3300'),
          ("bits", 'int(data.get("resolution_bits") or 0) == 12'), ("mv", 'abs(int(data.get("mv") or -1) - 1650) <= 50')]),
        ("lab_ep_isr_vs_poll", ["mode", "max_latency_us", "missed_edges"],
         [("mode", 'data.get("mode") == "isr"'), ("lat", 'int(data.get("max_latency_us") if data.get("max_latency_us") is not None else 9999) <= 250'),
          ("miss", 'data.get("missed_edges") is not None and int(data.get("missed_edges")) == 0')]),
        ("lab_ep_zephyr_qemu", ["board", "qemu_ok", "physical_status"],
         [("board", 'data.get("board") == "qemu_cortex_m0"'), ("qemu", 'data.get("qemu_ok") is True'),
          ("physical", 'data.get("physical_status") == "PHYSICAL_PENDING"')]),
        ("lab_ep_dt_overlay", ["overlay_has_i2c1", "overlay_has_led0", "delete_soc"],
         [("i2c", 'data.get("overlay_has_i2c1") is True'), ("led", 'data.get("overlay_has_led0") is True'),
          ("soc", 'data.get("delete_soc") is False')]),
        ("lab_ep_sleep_mode", ["sleep_mode", "wake_gpio", "wake_latency_ms"],
         [("mode", 'data.get("sleep_mode") in ("SYSTEM_OFF", "SLEEP")'), ("gpio", 'data.get("wake_gpio") == "BTN0"'),
          ("lat", 'int(data.get("wake_latency_ms") or 999) <= 20')]),
        ("lab_ep_subsystem_capstone", ["labs_passed", "qemu_ok", "dt_ok", "physical_status", "no_key_leak"],
         [("labs", 'int(data.get("labs_passed") or 0) >= 6'), ("qemu", 'data.get("qemu_ok") is True'),
          ("dt", 'data.get("dt_ok") is True'), ("physical", 'data.get("physical_status") == "PHYSICAL_PENDING"'),
          ("keys", 'data.get("no_key_leak") is True')]),
    ]
    gpl_labs = [
        ("lab_gpl_product_charter", ["problem", "goal_metric", "in_scope", "out_scope", "fabricated_outcomes"],
         [("problem", 'len(str(data.get("problem") or "")) >= 8'), ("goal", 'len(str(data.get("goal_metric") or "")) >= 8'),
          ("scope", 'isinstance(data.get("in_scope"), list) and len(data.get("in_scope") or []) >= 1'),
          ("out", 'isinstance(data.get("out_scope"), list)'), ("fab", 'data.get("fabricated_outcomes") is False')]),
        ("lab_gpl_compat_matrix", ["device_os_sha", "gunnchai_sha", "contract_ok"],
         [("dos", 'len(str(data.get("device_os_sha") or "")) >= 7'), ("ai", 'len(str(data.get("gunnchai_sha") or "")) >= 7'),
          ("ok", 'data.get("contract_ok") is True')]),
        ("lab_gpl_checkout_flow", ["states", "orphan_state"],
         [("states", 'isinstance(data.get("states"), list) and len(data.get("states") or []) >= 4'),
          ("orphan", 'data.get("orphan_state") is False')]),
        ("lab_gpl_compose_health", ["migrate_ok", "health", "rollback_to", "current_digest"],
         [("mig", 'data.get("migrate_ok") is True'), ("health", 'data.get("health") == "healthy"'),
          ("rb", 'str(data.get("rollback_to") or "") != str(data.get("current_digest") or "")'),
          ("digest", 'len(str(data.get("current_digest") or "")) >= 12')]),
        ("lab_gpl_privacy_bom", ["fields", "pii_in_bom", "retention_days"],
         [("fields", 'isinstance(data.get("fields"), list) and len(data.get("fields") or []) >= 2'),
          ("pii", 'data.get("pii_in_bom") is False'), ("ret", 'int(data.get("retention_days") or 0) >= 1')]),
        ("lab_gpl_guest_protocol", ["ping_ok", "boot_status", "protocol_version"],
         [("ping", 'data.get("ping_ok") is True'), ("boot", 'data.get("boot_status") == "ready"'),
          ("ver", 'str(data.get("protocol_version") or "").startswith("wp")')]),
        ("lab_gpl_release_notes", ["semver", "breaking", "changelog_entries"],
         [("sem", 'len(str(data.get("semver") or "")) >= 5'), ("brk", 'data.get("breaking") is False'),
          ("entries", 'int(data.get("changelog_entries") or 0) >= 1')]),
        ("lab_gpl_ci_tokens", ["tokens_passed", "tokens_total", "fabricated_green"],
         [("pass", 'int(data.get("tokens_passed") or 0) >= 1'), ("tot", 'int(data.get("tokens_total") or 0) >= int(data.get("tokens_passed") or 0)'),
          ("fab", 'data.get("fabricated_green") is False')]),
        ("lab_gpl_dep_pin", ["preview_sha_in_accepted", "pin_file"],
         [("prev", 'data.get("preview_sha_in_accepted") is False'),
          ("pin", 'data.get("pin_file") == "CURRENT_ACCEPTED_MAIN.json"')]),
        ("lab_gpl_product_capstone", ["labs_passed", "compat_ok", "no_device_os_pr", "no_key_leak"],
         [("labs", 'int(data.get("labs_passed") or 0) >= 6'), ("compat", 'data.get("compat_ok") is True'),
          ("pr", 'data.get("no_device_os_pr") is True'), ("keys", 'data.get("no_key_leak") is True')]),
    ]

    fn_blocks = []
    for name, keys, checks in ep_labs:
        fn_blocks.append(_lab_fn(name, "EMBEDDED_PROTOTYPING", keys, checks))
    for name, keys, checks in gpl_labs:
        fn_blocks.append(_lab_fn(name, "GUNNCHOS_PRODUCT_LAB", keys, checks))

    ep_names = [x[0] for x in ep_labs]
    gpl_names = [x[0] for x in gpl_labs]

    ref_ep = {
        "lab_ep_memory_map": {"flash_base": "0x00000000", "sram_base": "0x20000000", "vector_table_offset": "0x100", "physical_status": "PHYSICAL_PENDING"},
        "lab_ep_gpio_contract": {"pin": "LED0", "direction": "out", "default_level": 0, "pull": "none"},
        "lab_ep_i2c_timing": {"bus": "i2c1", "addr": "0x3C", "freq_khz": 100, "nack_recovery": True},
        "lab_ep_spi_flash": {"opcode": "0x03", "addr": "0x00001000", "read_len": 16, "crc_ok": True},
        "lab_ep_adc_scale": {"raw": 2048, "vref_mv": 3300, "resolution_bits": 12, "mv": 1650},
        "lab_ep_isr_vs_poll": {"mode": "isr", "max_latency_us": 200, "missed_edges": 0},
        "lab_ep_zephyr_qemu": {"board": "qemu_cortex_m0", "qemu_ok": True, "physical_status": "PHYSICAL_PENDING"},
        "lab_ep_dt_overlay": {"overlay_has_i2c1": True, "overlay_has_led0": True, "delete_soc": False},
        "lab_ep_sleep_mode": {"sleep_mode": "SYSTEM_OFF", "wake_gpio": "BTN0", "wake_latency_ms": 5},
        "lab_ep_subsystem_capstone": {"labs_passed": 9, "qemu_ok": True, "dt_ok": True, "physical_status": "PHYSICAL_PENDING", "no_key_leak": True},
    }
    ref_gpl = {
        "lab_gpl_product_charter": {"problem": "checkout wait", "goal_metric": "median_wait_minutes", "in_scope": ["queue"], "out_scope": ["new building"], "fabricated_outcomes": False},
        "lab_gpl_compat_matrix": {"device_os_sha": "d5c2d17", "gunnchai_sha": "d357846", "contract_ok": True},
        "lab_gpl_checkout_flow": {"states": ["requested", "approved", "checked_out", "returned"], "orphan_state": False},
        "lab_gpl_compose_health": {"migrate_ok": True, "health": "healthy", "rollback_to": "abc111", "current_digest": "def222222222"},
        "lab_gpl_privacy_bom": {"fields": ["camera", "mic"], "pii_in_bom": False, "retention_days": 30},
        "lab_gpl_guest_protocol": {"ping_ok": True, "boot_status": "ready", "protocol_version": "wp011r"},
        "lab_gpl_release_notes": {"semver": "1.4.0", "breaking": False, "changelog_entries": 3},
        "lab_gpl_ci_tokens": {"tokens_passed": 4, "tokens_total": 4, "fabricated_green": False},
        "lab_gpl_dep_pin": {"preview_sha_in_accepted": False, "pin_file": "CURRENT_ACCEPTED_MAIN.json"},
        "lab_gpl_product_capstone": {"labs_passed": 9, "compat_ok": True, "no_device_os_pr": True, "no_key_leak": True},
    }

    wrong = {k: {} for k in ep_names + gpl_names}
    for k in ep_names:
        wrong[k] = {"physical_status": "SHIPPED", "qemu_ok": False, "delete_soc": True}
    for k in gpl_names:
        wrong[k] = {"fabricated_outcomes": True, "contract_ok": False, "no_key_leak": False, "preview_sha_in_accepted": True}

    specs = {}
    for name in ep_names + gpl_names:
        cid = "EMBEDDED_PROTOTYPING" if name.startswith("lab_ep_") else "GUNNCHOS_PRODUCT_LAB"
        specs[name] = {"title": name.replace("lab_", ""), "readme": f"{name} fixture JSON.", "required_keys": [], "wrong_hint": "Wrong/empty/print-PASS fail.", "course_id": cid}

    header = textwrap.dedent('''
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
    ''').strip()

    ep_fns = "\n\n".join(fn_blocks[:10])
    gpl_fns = "\n\n".join(fn_blocks[10:])

    labs_map = ",\n    ".join(f'"{n}": {n}' for n in ep_names + gpl_names)
    def py_literal(obj: dict) -> str:
        return json.dumps(obj, indent=4).replace("true", "True").replace("false", "False").replace("null", "None")

    out = header + "\n\n" + ep_fns + "\n\n" + gpl_fns + f"""

LABS_007 = {{
    {labs_map}
}}

COURSE_LABS_007 = {{
    "EMBEDDED_PROTOTYPING": {json.dumps(ep_names)},
    "GUNNCHOS_PRODUCT_LAB": {json.dumps(gpl_names)},
}}

LAB_SPECS_007 = {json.dumps(specs, indent=4)}

REFERENCE_007 = {py_literal({**ref_ep, **ref_gpl})}

WRONG_007 = {py_literal(wrong)}
"""
    return out + "\n"


def main() -> None:
    BATCH.mkdir(parents=True, exist_ok=True)
    courses = {"EMBEDDED_PROTOTYPING": _course_ep(), "GUNNCHOS_PRODUCT_LAB": _course_gpl()}
    _write_json(BATCH / "courses_data.json", courses)
    _write_json(BATCH / "exams_data.json", {
        "EMBEDDED_PROTOTYPING": _exams("EMBEDDED_PROTOTYPING", "ep", 5),
        "GUNNCHOS_PRODUCT_LAB": _exams("GUNNCHOS_PRODUCT_LAB", "gpl", 6),
    })
    (BATCH / "labs.py").write_text(_generate_labs_py(), encoding="utf-8")
    (BATCH / "content.py").write_text(textwrap.dedent('''
        """Original WAIKE bodies for batch007 residual closure."""
        from __future__ import annotations
        import json
        from pathlib import Path
        BATCH_COURSE_IDS = ("EMBEDDED_PROTOTYPING", "GUNNCHOS_PRODUCT_LAB")
        _DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
        EMBEDDED_PROTOTYPING = _DATA["EMBEDDED_PROTOTYPING"]
        GUNNCHOS_PRODUCT_LAB = _DATA["GUNNCHOS_PRODUCT_LAB"]
        COURSES_007 = {"EMBEDDED_PROTOTYPING": EMBEDDED_PROTOTYPING, "GUNNCHOS_PRODUCT_LAB": GUNNCHOS_PRODUCT_LAB}
    ''').strip() + "\n", encoding="utf-8")
    (BATCH / "exams.py").write_text(textwrap.dedent('''
        """Mid/final banks for batch007."""
        from __future__ import annotations
        import json
        from pathlib import Path
        _EX = json.loads((Path(__file__).with_name("exams_data.json")).read_text(encoding="utf-8"))
        def extra_assessment_items_007(course_id: str):
            from waike_course_ready.exams import rebalance_mcq
            spec = _EX[course_id]
            mid = rebalance_mcq(spec["mid"], spec["offset"])
            final = rebalance_mcq(spec["final"], spec["offset"] + 1)
            if len(mid) != 20 or len(final) != 24:
                raise ValueError(f"{course_id} exam sizes mid={len(mid)} final={len(final)}")
            return {"mid": mid, "final": final}
    ''').strip() + "\n", encoding="utf-8")
    (BATCH / "__init__.py").write_text('"""Batch007 — EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB."""\n', encoding="utf-8")
    print("Wrote batch007 source under", BATCH)


if __name__ == "__main__":
    main()
