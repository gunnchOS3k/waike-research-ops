"""Runnable labs for WAIKE-COURSE-READY-002 with computing validators."""
from __future__ import annotations

import hashlib
import json
import math
import re
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
    if not isinstance(submission, dict):
        return None, "submission_not_object"
    if submission == {}:
        return None, "empty_submission"
    return submission, "ok"


def _require_student(lab_id: str, course_id: str, submission: Any, required_keys: list[str], boundary: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
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


# ----- SOFTWARE -----

def lab_git_conflict(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Resolve conflict keeping require_role and HOURS; empty fails."
    data, checks = _require_student("lab_git_conflict", "SOFTWARE_BUILDER", submission, ["parents", "survivor_tokens", "resolved_text"], boundary)
    if data is None:
        return _result("lab_git_conflict", "SOFTWARE_BUILDER", checks, boundary)
    parents = data.get("parents") or []
    tokens = set(data.get("survivor_tokens") or [])
    text = str(data.get("resolved_text") or "")
    checks.append(_check("two_parents", len(parents) >= 2, f"parents={len(parents)}"))
    checks.append(_check("keep_require_role", "require_role" in tokens and "require_role" in text, "missing require_role"))
    checks.append(_check("keep_hours", "HOURS" in tokens and "HOURS" in text, "missing HOURS"))
    checks.append(_check("single_entrypoint", text.count("def open_hours") == 1, "need exactly one open_hours"))
    return _result("lab_git_conflict", "SOFTWARE_BUILDER", checks, boundary)


def lab_rest_api(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Status codes from method/role/body; empty fails."
    data, checks = _require_student("lab_rest_api", "SOFTWARE_BUILDER", submission, ["cases", "store_len_after_idempotent_put"], boundary)
    if data is None:
        return _result("lab_rest_api", "SOFTWARE_BUILDER", checks, boundary)
    expected = {
        ("POST", "/api/v1/checkouts", "reader", True): 403,
        ("POST", "/api/v1/checkouts", "desk", False): 400,
        ("POST", "/api/v1/checkouts", "desk", True): 201,
        ("GET", "/api/v1/checkouts/missing", "desk", False): 404,
    }
    got = {}
    for c in data.get("cases") or []:
        key = (c.get("method"), c.get("path"), c.get("role"), bool(c.get("has_device_id")))
        got[key] = c.get("status")
    ok_map = all(got.get(k) == v for k, v in expected.items())
    checks.append(_check("status_map", ok_map, f"got={got}"))
    checks.append(_check("idempotent_store", int(data.get("store_len_after_idempotent_put") or -1) == 1, "store len"))
    return _result("lab_rest_api", "SOFTWARE_BUILDER", checks, boundary)


def lab_db_migration(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Forward adds nullable returned_at; version 3; no DELETE checkouts."
    data, checks = _require_student("lab_db_migration", "SOFTWARE_BUILDER", submission, ["forward_sql", "down_sql", "schema_version"], boundary)
    if data is None:
        return _result("lab_db_migration", "SOFTWARE_BUILDER", checks, boundary)
    fwd = str(data.get("forward_sql") or "").upper()
    down = str(data.get("down_sql") or "").upper()
    checks.append(_check("version", int(data.get("schema_version") or 0) == 3, "version"))
    checks.append(_check("adds_returned_at", "RETURNED_AT" in fwd and "TIMESTAMP" in fwd, "forward"))
    checks.append(_check("nullable", "NOT NULL" not in fwd.split("RETURNED_AT", 1)[-1][:40], "nullable"))
    checks.append(_check("no_delete_history", "DELETE FROM CHECKOUTS" not in fwd and "DELETE FROM CHECKOUTS" not in down, "delete"))
    checks.append(_check("down_drops_column", "RETURNED_AT" in down and "DROP" in down, "down"))
    checks.append(_check("no_password", "PASSWORD" not in fwd and "PASSWORD" not in down, "secrets"))
    return _result("lab_db_migration", "SOFTWARE_BUILDER", checks, boundary)


def lab_frontend_ui(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Accessible board tree with OVERDUE text and named filter button."
    data, checks = _require_student("lab_frontend_ui", "SOFTWARE_BUILDER", submission, ["tree"], boundary)
    if data is None:
        return _result("lab_frontend_ui", "SOFTWARE_BUILDER", checks, boundary)
    blob = json.dumps(data.get("tree") or {}).lower()
    checks.append(_check("filter_button", "filter overdue" in blob, "filter name"))
    checks.append(_check("overdue_text", "overdue" in blob, "overdue marker"))
    checks.append(_check("alert_role", "role" in blob and "alert" in blob, "alert"))
    checks.append(_check("not_color_only", "class\":\"red\"" not in blob or "overdue" in blob, "color+text"))
    return _result("lab_frontend_ui", "SOFTWARE_BUILDER", checks, boundary)


def lab_authz(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "desk create/close/read; reader read; forge-bot annotate only."
    data, checks = _require_student("lab_authz", "SOFTWARE_BUILDER", submission, ["roles"], boundary)
    if data is None:
        return _result("lab_authz", "SOFTWARE_BUILDER", checks, boundary)
    roles = data.get("roles") or {}
    def acts(r):
        return set((roles.get(r) or {}).get("actions") or [])
    checks.append(_check("desk_can_create", "checkout.create" in acts("desk"), "desk create"))
    checks.append(_check("desk_can_close", "checkout.close" in acts("desk"), "desk close"))
    checks.append(_check("reader_read_only", acts("reader") == {"checkout.read"}, f"reader={acts('reader')}"))
    checks.append(_check("bot_no_close", "checkout.close" not in acts("forge-bot"), "bot close"))
    checks.append(_check("bot_annotate", "checkout.annotate" in acts("forge-bot"), "bot annotate"))
    return _result("lab_authz", "SOFTWARE_BUILDER", checks, boundary)


def lab_automated_testing(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "JUnit-like report total>=8 failed==0 named test present."
    data, checks = _require_student("lab_automated_testing", "SOFTWARE_BUILDER", submission, ["total", "failed", "tests"], boundary)
    if data is None:
        return _result("lab_automated_testing", "SOFTWARE_BUILDER", checks, boundary)
    tests = data.get("tests") or []
    names = {t.get("name"): t for t in tests}
    total = data.get("total"); failed = data.get("failed")
    checks.append(_check("total", total is not None and int(total) >= 8, "total"))
    checks.append(_check("failed_zero", failed is not None and int(failed) == 0, "failed"))
    t = names.get("test_reader_post_forbidden") or {}
    checks.append(_check("named_test", bool(t) and t.get("passed") is True, "named"))
    return _result("lab_automated_testing", "SOFTWARE_BUILDER", checks, boundary)


def lab_github_actions_ci(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "PR workflow lint→test→upload; no ungated deploy."
    data, checks = _require_student("lab_github_actions_ci", "SOFTWARE_BUILDER", submission, ["on", "jobs"], boundary)
    if data is None:
        return _result("lab_github_actions_ci", "SOFTWARE_BUILDER", checks, boundary)
    on = data.get("on") or []
    jobs = data.get("jobs") or []
    names = [j.get("name") for j in jobs]
    checks.append(_check("pull_request", "pull_request" in on, "trigger"))
    checks.append(_check("has_test", "test" in names, "test job"))
    checks.append(_check("has_lint", "lint" in names, "lint job"))
    checks.append(_check("has_upload", "upload-report" in names, "upload"))
    if "lint" in names and "test" in names:
        checks.append(_check("order", names.index("lint") < names.index("test"), "order"))
    deploy = [j for j in jobs if j.get("name") == "deploy"]
    checks.append(_check("no_ungated_deploy", not deploy or all(j.get("environment") for j in deploy), "deploy gate"))
    echo_pass = any("PASS" == str(j.get("run") or "").strip() for j in jobs)
    checks.append(_check("no_echo_pass", not echo_pass, "echo pass"))
    return _result("lab_github_actions_ci", "SOFTWARE_BUILDER", checks, boundary)


def lab_deploy_rollback(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Digest pin, distinct rollback, migrate ok, healthy."
    data, checks = _require_student("lab_deploy_rollback", "SOFTWARE_BUILDER", submission, ["current", "rollback_to", "migrate", "health"], boundary)
    if data is None:
        return _result("lab_deploy_rollback", "SOFTWARE_BUILDER", checks, boundary)
    cur = str(data.get("current") or "")
    rb = str(data.get("rollback_to") or "")
    checks.append(_check("digest_shape", cur.startswith("sha256:") and rb.startswith("sha256:"), "digest"))
    checks.append(_check("rollback_distinct", cur != rb and bool(rb), "distinct"))
    checks.append(_check("migrate_ok", data.get("migrate") == "ok", "migrate"))
    checks.append(_check("healthy", data.get("health") == "healthy", "health"))
    return _result("lab_deploy_rollback", "SOFTWARE_BUILDER", checks, boundary)


def lab_security_review(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Findings list with high IDOR evidence."
    data, checks = _require_student("lab_security_review", "SOFTWARE_BUILDER", submission, ["findings"], boundary)
    if data is None:
        return _result("lab_security_review", "SOFTWARE_BUILDER", checks, boundary)
    findings = data.get("findings") or []
    sev = {str(f.get("severity") or "").lower() for f in findings}
    has_idor = any("idor" in str(f.get("id") or "").lower() or "idor" in str(f.get("evidence") or "").lower() for f in findings)
    checks.append(_check("nonempty", len(findings) >= 1, "count"))
    checks.append(_check("needs_high", bool(sev & {"high", "critical"}), f"sev={sev}"))
    checks.append(_check("idor_present", has_idor, "idor"))
    checks.append(_check("schema", all(f.get("id") and f.get("severity") and f.get("evidence") for f in findings), "schema"))
    return _result("lab_security_review", "SOFTWARE_BUILDER", checks, boundary)


def lab_observability(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Availability and budget from fixture counts only."
    data, checks = _require_student("lab_observability", "SOFTWARE_BUILDER", submission, ["failed", "total", "availability", "budget_ok"], boundary)
    if data is None:
        return _result("lab_observability", "SOFTWARE_BUILDER", checks, boundary)
    failed = int(data.get("failed") or -1)
    total = int(data.get("total") or 0)
    avail = float(data.get("availability") or -1)
    expect = 1.0 - (failed / total) if total else -1
    checks.append(_check("counts", failed == 50 and total == 10000, "fixture counts"))
    checks.append(_check("availability_math", abs(avail - expect) < 1e-9, f"got={avail} expect={expect}"))
    checks.append(_check("budget_ok", data.get("budget_ok") is True and avail >= 0.995, "budget"))
    return _result("lab_observability", "SOFTWARE_BUILDER", checks, boundary)


# ----- HARDWARE -----

def _series_req(r1: float, r2: float, vin: float) -> tuple[float, float]:
    i = vin / (r1 + r2)
    return i, i * r2


def lab_spice_network(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Series divider: compute I and Vout from R1,R2,Vin — not print PASS."
    data, checks = _require_student("lab_spice_network", "HARDWARE_ENGINEERING", submission, ["R1", "R2", "Vin", "I", "Vout"], boundary)
    if data is None:
        return _result("lab_spice_network", "HARDWARE_ENGINEERING", checks, boundary)
    r1, r2, vin = float(data["R1"]), float(data["R2"]), float(data["Vin"])
    i_e, v_e = _series_req(r1, r2, vin)
    checks.append(_check("current", abs(float(data["I"]) - i_e) < 1e-9, f"I={data['I']} expect={i_e}"))
    checks.append(_check("vout", abs(float(data["Vout"]) - v_e) < 1e-9, f"V={data['Vout']} expect={v_e}"))
    checks.append(_check("positive_r", r1 > 0 and r2 > 0, "R"))
    return _result("lab_spice_network", "HARDWARE_ENGINEERING", checks, boundary)


def lab_thevenin(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Thevenin of divider seen from load node: Vth=Vin*R2/(R1+R2), Rth=R1||R2."
    data, checks = _require_student("lab_thevenin", "HARDWARE_ENGINEERING", submission, ["Vin", "R1", "R2", "Vth", "Rth"], boundary)
    if data is None:
        return _result("lab_thevenin", "HARDWARE_ENGINEERING", checks, boundary)
    vin, r1, r2 = float(data["Vin"]), float(data["R1"]), float(data["R2"])
    vth = vin * r2 / (r1 + r2)
    rth = (r1 * r2) / (r1 + r2)
    checks.append(_check("vth", abs(float(data["Vth"]) - vth) < 1e-9, "vth"))
    checks.append(_check("rth", abs(float(data["Rth"]) - rth) < 1e-9, "rth"))
    return _result("lab_thevenin", "HARDWARE_ENGINEERING", checks, boundary)


def lab_rc_transient(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "tau=R*C; V(t)=V0*(1-exp(-t/tau)) for charging."
    data, checks = _require_student("lab_rc_transient", "HARDWARE_ENGINEERING", submission, ["R", "C", "V0", "t", "tau", "Vt"], boundary)
    if data is None:
        return _result("lab_rc_transient", "HARDWARE_ENGINEERING", checks, boundary)
    R, C, V0, t = float(data["R"]), float(data["C"]), float(data["V0"]), float(data["t"])
    tau = R * C
    vt = V0 * (1 - math.exp(-t / tau))
    checks.append(_check("tau", abs(float(data["tau"]) - tau) < 1e-12, "tau"))
    checks.append(_check("vt", abs(float(data["Vt"]) - vt) < 1e-9, "Vt"))
    return _result("lab_rc_transient", "HARDWARE_ENGINEERING", checks, boundary)


def lab_logic_gate(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "2-input NAND truth table must match."
    data, checks = _require_student("lab_logic_gate", "HARDWARE_ENGINEERING", submission, ["gate", "rows"], boundary)
    if data is None:
        return _result("lab_logic_gate", "HARDWARE_ENGINEERING", checks, boundary)
    expect = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 0}
    got = {(int(r["a"]), int(r["b"])): int(r["y"]) for r in (data.get("rows") or [])}
    checks.append(_check("nand", data.get("gate") == "NAND", "gate"))
    checks.append(_check("truth", got == expect, f"got={got}"))
    return _result("lab_logic_gate", "HARDWARE_ENGINEERING", checks, boundary)


def lab_power_budget(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Sum currents for real MPNs; margin vs regulator."
    data, checks = _require_student("lab_power_budget", "HARDWARE_ENGINEERING", submission, ["rails", "regulator_mA", "total_mA", "margin_mA"], boundary)
    if data is None:
        return _result("lab_power_budget", "HARDWARE_ENGINEERING", checks, boundary)
    rails = data.get("rails") or []
    total = sum(float(r["Iq_mA"]) for r in rails)
    reg = float(data["regulator_mA"])
    margin = reg - total
    mpns = {r.get("mpn") for r in rails}
    checks.append(_check("real_mpns", {"nRF52840", "AMS1117-3.3", "SSD1306"}.issubset(mpns), f"mpns={mpns}"))
    checks.append(_check("total", abs(float(data["total_mA"]) - total) < 1e-9, "total"))
    checks.append(_check("margin", abs(float(data["margin_mA"]) - margin) < 1e-9 and margin > 0, "margin"))
    return _result("lab_power_budget", "HARDWARE_ENGINEERING", checks, boundary)


def lab_bus_protocol(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Parse I2C write frame: addr, reg, data."
    data, checks = _require_student("lab_bus_protocol", "HARDWARE_ENGINEERING", submission, ["bus", "addr", "reg", "data", "frame_hex"], boundary)
    if data is None:
        return _result("lab_bus_protocol", "HARDWARE_ENGINEERING", checks, boundary)
    raw = bytes.fromhex(str(data["frame_hex"]).replace(" ", ""))
    checks.append(_check("bus", data.get("bus") == "I2C", "bus"))
    checks.append(_check("len", len(raw) >= 3, "len"))
    if len(raw) >= 3:
        checks.append(_check("addr", int(data["addr"]) == raw[0], "addr"))
        checks.append(_check("reg", int(data["reg"]) == raw[1], "reg"))
        checks.append(_check("data", int(data["data"]) == raw[2], "data"))
    return _result("lab_bus_protocol", "HARDWARE_ENGINEERING", checks, boundary)


def lab_zephyr_qemu(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "west build model for qemu_cortex_m0; PHYSICAL_PENDING for flash."
    data, checks = _require_student("lab_zephyr_qemu", "HARDWARE_ENGINEERING", submission, ["board", "west_cmd", "physical_status", "qemu_ok"], boundary)
    if data is None:
        return _result("lab_zephyr_qemu", "HARDWARE_ENGINEERING", checks, boundary)
    checks.append(_check("board", data.get("board") == "qemu_cortex_m0", "board"))
    cmd = str(data.get("west_cmd") or "")
    checks.append(_check("west", "west build" in cmd and "qemu_cortex_m0" in cmd, "west"))
    checks.append(_check("physical_pending", data.get("physical_status") == "PHYSICAL_PENDING", "physical"))
    checks.append(_check("qemu_ok", data.get("qemu_ok") is True, "qemu"))
    return _result("lab_zephyr_qemu", "HARDWARE_ENGINEERING", checks, boundary)


def lab_devicetree(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "DT overlay enables I2C1 and LED0 gpio."
    data, checks = _require_student("lab_devicetree", "HARDWARE_ENGINEERING", submission, ["overlay", "i2c1_status", "led0_gpios"], boundary)
    if data is None:
        return _result("lab_devicetree", "HARDWARE_ENGINEERING", checks, boundary)
    ov = str(data.get("overlay") or "")
    checks.append(_check("i2c_okay", data.get("i2c1_status") == "okay" and "&i2c1" in ov, "i2c"))
    checks.append(_check("led", bool(data.get("led0_gpios")) and "led0" in ov.lower(), "led"))
    checks.append(_check("no_board_delete", "/delete-node/" not in ov or "soc" not in ov, "safety"))
    return _result("lab_devicetree", "HARDWARE_ENGINEERING", checks, boundary)


def lab_pcb_erc_drc(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "ERC/DRC report: no unconnected power; clearance ok."
    data, checks = _require_student("lab_pcb_erc_drc", "HARDWARE_ENGINEERING", submission, ["erc_errors", "drc_errors", "unconnected_power", "bom_lines"], boundary)
    if data is None:
        return _result("lab_pcb_erc_drc", "HARDWARE_ENGINEERING", checks, boundary)
    erc = data.get("erc_errors"); drc = data.get("drc_errors")
    checks.append(_check("erc_clean", erc is not None and int(erc) == 0, "erc"))
    checks.append(_check("drc_clean", drc is not None and int(drc) == 0, "drc"))
    checks.append(_check("power", data.get("unconnected_power") is False, "power"))
    bom = data.get("bom_lines") or []
    checks.append(_check("bom", len(bom) >= 3 and all("mpn" in x for x in bom), "bom"))
    return _result("lab_pcb_erc_drc", "HARDWARE_ENGINEERING", checks, boundary)


def lab_failure_diagnosis(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Digitally diagnose: 3V3 rail sag + I2C NACK → regulator or bus pullup."
    data, checks = _require_student("lab_failure_diagnosis", "HARDWARE_ENGINEERING", submission, ["symptoms", "root_cause", "next_probe", "physical_status"], boundary)
    if data is None:
        return _result("lab_failure_diagnosis", "HARDWARE_ENGINEERING", checks, boundary)
    sym = set(data.get("symptoms") or [])
    checks.append(_check("symptoms", {"rail_sag_3v3", "i2c_nack"}.issubset(sym), f"sym={sym}"))
    checks.append(_check("cause", data.get("root_cause") in {"weak_regulator", "missing_pullups", "shared_rail_overload"}, "cause"))
    checks.append(_check("probe", "measure" in str(data.get("next_probe") or "").lower(), "probe"))
    checks.append(_check("physical", data.get("physical_status") == "PHYSICAL_PENDING", "physical"))
    return _result("lab_failure_diagnosis", "HARDWARE_ENGINEERING", checks, boundary)


# ----- PM / LSS -----

def lab_charter(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Charter with problem, goal metric, in/out scope — no fabricated community outcomes."
    data, checks = _require_student("lab_charter", "PM_AGILE_LSS", submission, ["problem", "goal_metric", "in_scope", "out_scope", "fabricated_outcomes"], boundary)
    if data is None:
        return _result("lab_charter", "PM_AGILE_LSS", checks, boundary)
    checks.append(_check("problem", len(str(data.get("problem") or "")) >= 20, "problem"))
    checks.append(_check("metric", "baseline" in str(data.get("goal_metric") or "").lower() or "%" in str(data.get("goal_metric")), "metric"))
    checks.append(_check("scope", len(data.get("in_scope") or []) >= 2 and len(data.get("out_scope") or []) >= 1, "scope"))
    checks.append(_check("no_fabrications", data.get("fabricated_outcomes") is False, "fabrications"))
    return _result("lab_charter", "PM_AGILE_LSS", checks, boundary)


def lab_raci(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Each task has exactly one A."
    data, checks = _require_student("lab_raci", "PM_AGILE_LSS", submission, ["matrix"], boundary)
    if data is None:
        return _result("lab_raci", "PM_AGILE_LSS", checks, boundary)
    ok = True
    for row in data.get("matrix") or []:
        roles = row.get("roles") or {}
        a_count = sum(1 for v in roles.values() if v == "A")
        if a_count != 1:
            ok = False
    checks.append(_check("one_accountable", ok and len(data.get("matrix") or []) >= 3, "A count"))
    return _result("lab_raci", "PM_AGILE_LSS", checks, boundary)


def lab_wbs_schedule(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "WBS tasks with durations; critical path length computed."
    data, checks = _require_student("lab_wbs_schedule", "PM_AGILE_LSS", submission, ["tasks", "critical_path_days"], boundary)
    if data is None:
        return _result("lab_wbs_schedule", "PM_AGILE_LSS", checks, boundary)
    tasks = {t["id"]: t for t in (data.get("tasks") or [])}
    # Simple longest path on deps
    memo: dict[str, float] = {}
    def dur(tid: str) -> float:
        if tid in memo:
            return memo[tid]
        t = tasks[tid]
        preds = t.get("preds") or []
        memo[tid] = float(t["days"]) + (max((dur(p) for p in preds), default=0.0))
        return memo[tid]
    expect = max((dur(t) for t in tasks), default=0.0)
    checks.append(_check("tasks", len(tasks) >= 4, "tasks"))
    checks.append(_check("cp", abs(float(data["critical_path_days"]) - expect) < 1e-9, f"cp={data['critical_path_days']} expect={expect}"))
    return _result("lab_wbs_schedule", "PM_AGILE_LSS", checks, boundary)


def lab_sprint_board(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Sprint: committed points <= capacity; Done has ACs."
    data, checks = _require_student("lab_sprint_board", "PM_AGILE_LSS", submission, ["capacity", "committed", "done_items"], boundary)
    if data is None:
        return _result("lab_sprint_board", "PM_AGILE_LSS", checks, boundary)
    cap = int(data["capacity"])
    com = int(data["committed"])
    done = data.get("done_items") or []
    checks.append(_check("cap", com <= cap and cap > 0, "capacity"))
    checks.append(_check("acs", all(i.get("acceptance") for i in done) and len(done) >= 1, "ACs"))
    return _result("lab_sprint_board", "PM_AGILE_LSS", checks, boundary)


def lab_risk_register(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Risk score=prob*impact; top risk has response."
    data, checks = _require_student("lab_risk_register", "PM_AGILE_LSS", submission, ["risks"], boundary)
    if data is None:
        return _result("lab_risk_register", "PM_AGILE_LSS", checks, boundary)
    risks = data.get("risks") or []
    ok_scores = all(abs(float(r["score"]) - float(r["prob"]) * float(r["impact"])) < 1e-9 for r in risks)
    top = max(risks, key=lambda r: float(r["score"])) if risks else None
    checks.append(_check("scores", ok_scores and len(risks) >= 3, "scores"))
    checks.append(_check("response", bool(top and top.get("response")), "response"))
    return _result("lab_risk_register", "PM_AGILE_LSS", checks, boundary)


def lab_sipoc_process(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "SIPOC with >=3 process steps and measurable output."
    data, checks = _require_student("lab_sipoc_process", "PM_AGILE_LSS", submission, ["suppliers", "inputs", "process", "outputs", "customers"], boundary)
    if data is None:
        return _result("lab_sipoc_process", "PM_AGILE_LSS", checks, boundary)
    checks.append(_check("process_steps", len(data.get("process") or []) >= 3, "steps"))
    checks.append(_check("measurable_output", any("%" in str(o) or "count" in str(o).lower() or "time" in str(o).lower() for o in (data.get("outputs") or [])), "output"))
    checks.append(_check("filled", all(len(data.get(k) or []) >= 1 for k in ["suppliers", "inputs", "customers"]), "filled"))
    return _result("lab_sipoc_process", "PM_AGILE_LSS", checks, boundary)


def lab_pareto_rootcause(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Pareto cumulative %; top causes explain >=80%."
    data, checks = _require_student("lab_pareto_rootcause", "PM_AGILE_LSS", submission, ["causes", "cum_pct_top", "root_cause"], boundary)
    if data is None:
        return _result("lab_pareto_rootcause", "PM_AGILE_LSS", checks, boundary)
    causes = sorted(data.get("causes") or [], key=lambda c: -float(c["count"]))
    total = sum(float(c["count"]) for c in causes) or 1.0
    cum = 0.0
    k = 0
    while k < len(causes) and cum < 0.80:
        cum += float(causes[k]["count"]) / total
        k += 1
    checks.append(_check("cum", abs(float(data["cum_pct_top"]) - cum) < 1e-6, f"cum={data['cum_pct_top']} expect={cum}"))
    checks.append(_check("ge80", cum >= 0.80, "80"))
    checks.append(_check("root", len(str(data.get("root_cause") or "")) >= 10, "root"))
    return _result("lab_pareto_rootcause", "PM_AGILE_LSS", checks, boundary)


def lab_control_chart(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Mean/UCL/LCL for individuals; flag points outside."
    data, checks = _require_student("lab_control_chart", "PM_AGILE_LSS", submission, ["points", "mean", "ucl", "lcl", "out_of_control"], boundary)
    if data is None:
        return _result("lab_control_chart", "PM_AGILE_LSS", checks, boundary)
    pts = [float(x) for x in (data.get("points") or [])]
    mean = sum(pts) / len(pts)
    # Use mr-based sigma approx: sigma ~= average moving range / 1.128
    mrs = [abs(pts[i] - pts[i - 1]) for i in range(1, len(pts))]
    sigma = (sum(mrs) / len(mrs) / 1.128) if mrs else 0.0
    ucl, lcl = mean + 3 * sigma, mean - 3 * sigma
    ooc = [i for i, v in enumerate(pts) if v > ucl or v < lcl]
    checks.append(_check("mean", abs(float(data["mean"]) - mean) < 1e-6, "mean"))
    checks.append(_check("ucl", abs(float(data["ucl"]) - ucl) < 1e-4, "ucl"))
    checks.append(_check("lcl", abs(float(data["lcl"]) - lcl) < 1e-4, "lcl"))
    checks.append(_check("ooc", list(data.get("out_of_control") or []) == ooc, f"ooc={ooc}"))
    return _result("lab_control_chart", "PM_AGILE_LSS", checks, boundary)


def lab_dmaic_case(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "DMAIC phases present with artifacts; no fake community stats."
    data, checks = _require_student("lab_dmaic_case", "PM_AGILE_LSS", submission, ["define", "measure", "analyze", "improve", "control", "fabricated_outcomes"], boundary)
    if data is None:
        return _result("lab_dmaic_case", "PM_AGILE_LSS", checks, boundary)
    for phase in ["define", "measure", "analyze", "improve", "control"]:
        checks.append(_check(phase, len(str(data.get(phase) or "")) >= 15, phase))
    checks.append(_check("no_fake", data.get("fabricated_outcomes") is False, "fake"))
    return _result("lab_dmaic_case", "PM_AGILE_LSS", checks, boundary)


def lab_change_status_ai(fixture: dict[str, Any] | None = None, submission: Any = None) -> LabResult:
    boundary = "Change control + status report + AI plan critique (disclose)."
    data, checks = _require_student("lab_change_status_ai", "PM_AGILE_LSS", submission, ["change_request", "status_report", "ai_plan_critique", "ai_disclosed"], boundary)
    if data is None:
        return _result("lab_change_status_ai", "PM_AGILE_LSS", checks, boundary)
    cr = data.get("change_request") or {}
    checks.append(_check("cr", cr.get("id") and cr.get("impact") and cr.get("decision") in {"approve", "reject", "defer"}, "cr"))
    checks.append(_check("status", len(str(data.get("status_report") or "")) >= 40, "status"))
    critique = str(data.get("ai_plan_critique") or "")
    checks.append(_check("critique", "risk" in critique.lower() or "assumption" in critique.lower(), "critique"))
    checks.append(_check("disclosed", data.get("ai_disclosed") is True, "disclose"))
    return _result("lab_change_status_ai", "PM_AGILE_LSS", checks, boundary)


LABS_002 = {
    "lab_git_conflict": lab_git_conflict,
    "lab_rest_api": lab_rest_api,
    "lab_db_migration": lab_db_migration,
    "lab_frontend_ui": lab_frontend_ui,
    "lab_authz": lab_authz,
    "lab_automated_testing": lab_automated_testing,
    "lab_github_actions_ci": lab_github_actions_ci,
    "lab_deploy_rollback": lab_deploy_rollback,
    "lab_security_review": lab_security_review,
    "lab_observability": lab_observability,
    "lab_spice_network": lab_spice_network,
    "lab_thevenin": lab_thevenin,
    "lab_rc_transient": lab_rc_transient,
    "lab_logic_gate": lab_logic_gate,
    "lab_power_budget": lab_power_budget,
    "lab_bus_protocol": lab_bus_protocol,
    "lab_zephyr_qemu": lab_zephyr_qemu,
    "lab_devicetree": lab_devicetree,
    "lab_pcb_erc_drc": lab_pcb_erc_drc,
    "lab_failure_diagnosis": lab_failure_diagnosis,
    "lab_charter": lab_charter,
    "lab_raci": lab_raci,
    "lab_wbs_schedule": lab_wbs_schedule,
    "lab_sprint_board": lab_sprint_board,
    "lab_risk_register": lab_risk_register,
    "lab_sipoc_process": lab_sipoc_process,
    "lab_pareto_rootcause": lab_pareto_rootcause,
    "lab_control_chart": lab_control_chart,
    "lab_dmaic_case": lab_dmaic_case,
    "lab_change_status_ai": lab_change_status_ai,
}

COURSE_LABS_002 = {
    "SOFTWARE_BUILDER": [
        "lab_git_conflict", "lab_rest_api", "lab_db_migration", "lab_frontend_ui", "lab_authz",
        "lab_automated_testing", "lab_github_actions_ci", "lab_deploy_rollback", "lab_security_review", "lab_observability",
    ],
    "HARDWARE_ENGINEERING": [
        "lab_spice_network", "lab_thevenin", "lab_rc_transient", "lab_logic_gate", "lab_power_budget",
        "lab_bus_protocol", "lab_zephyr_qemu", "lab_devicetree", "lab_pcb_erc_drc", "lab_failure_diagnosis",
    ],
    "PM_AGILE_LSS": [
        "lab_charter", "lab_raci", "lab_wbs_schedule", "lab_sprint_board", "lab_risk_register",
        "lab_sipoc_process", "lab_pareto_rootcause", "lab_control_chart", "lab_dmaic_case", "lab_change_status_ai",
    ],
}

LAB_SPECS_002 = {lid: {"title": lid.replace("lab_", "").replace("_", " "), "readme": f"Runnable validator for {lid}. Empty/wrong/print-PASS fail.", "required_keys": [], "wrong_hint": "Wrong numeric or policy fields must fail."} for lid in LABS_002}

REFERENCE_002: dict[str, dict[str, Any]] = {
    "lab_git_conflict": {"parents": ["aaa", "bbb"], "survivor_tokens": ["require_role", "HOURS"], "resolved_text": "def open_hours():\n    require_role('desk')\n    HOURS={'mon':[9,17]}\n    return HOURS\n"},
    "lab_rest_api": {"cases": [
        {"method": "POST", "path": "/api/v1/checkouts", "role": "reader", "has_device_id": True, "status": 403},
        {"method": "POST", "path": "/api/v1/checkouts", "role": "desk", "has_device_id": False, "status": 400},
        {"method": "POST", "path": "/api/v1/checkouts", "role": "desk", "has_device_id": True, "status": 201},
        {"method": "GET", "path": "/api/v1/checkouts/missing", "role": "desk", "has_device_id": False, "status": 404},
    ], "store_len_after_idempotent_put": 1},
    "lab_db_migration": {"forward_sql": "ALTER TABLE checkouts ADD COLUMN returned_at TIMESTAMP NULL;", "down_sql": "ALTER TABLE checkouts DROP COLUMN returned_at;", "schema_version": 3},
    "lab_frontend_ui": {"tree": {"children": [{"type": "button", "name": "Filter overdue"}, {"type": "table", "rows": [{"text": "ring-7 OVERDUE"}]}, {"type": "div", "role": "alert", "text": "error"}]}},
    "lab_authz": {"roles": {"desk": {"actions": ["checkout.create", "checkout.close", "checkout.read"]}, "reader": {"actions": ["checkout.read"]}, "forge-bot": {"actions": ["checkout.annotate"]}}},
    "lab_automated_testing": {"total": 10, "failed": 0, "skipped": 1, "tests": [{"name": "test_reader_post_forbidden", "passed": True}]},
    "lab_github_actions_ci": {"on": ["pull_request"], "jobs": [{"name": "lint", "run": "ruff"}, {"name": "test", "run": "pytest"}, {"name": "upload-report", "run": "upload"}]},
    "lab_deploy_rollback": {"current": "sha256:aaa", "rollback_to": "sha256:bbb", "migrate": "ok", "health": "healthy"},
    "lab_security_review": {"findings": [{"id": "FORGE-IDOR-1", "severity": "high", "evidence": "GET /checkouts/{id} lacks owner check IDOR"}]},
    "lab_observability": {"failed": 50, "total": 10000, "availability": 0.995, "budget_ok": True},
    "lab_spice_network": {"R1": 1000.0, "R2": 3000.0, "Vin": 12.0, "I": 0.003, "Vout": 9.0},
    "lab_thevenin": {"Vin": 12.0, "R1": 1000.0, "R2": 3000.0, "Vth": 9.0, "Rth": 750.0},
    "lab_rc_transient": {"R": 1000.0, "C": 1e-6, "V0": 5.0, "t": 0.001, "tau": 0.001, "Vt": 5.0 * (1 - __import__('math').exp(-1.0))},
    "lab_logic_gate": {"gate": "NAND", "rows": [{"a": 0, "b": 0, "y": 1}, {"a": 0, "b": 1, "y": 1}, {"a": 1, "b": 0, "y": 1}, {"a": 1, "b": 1, "y": 0}]},
    "lab_power_budget": {"rails": [{"mpn": "nRF52840", "Iq_mA": 5.4}, {"mpn": "AMS1117-3.3", "Iq_mA": 5.0}, {"mpn": "SSD1306", "Iq_mA": 10.0}], "regulator_mA": 50.0, "total_mA": 20.4, "margin_mA": 29.6},
    "lab_bus_protocol": {"bus": "I2C", "frame_hex": "3c00af", "addr": 0x3C, "reg": 0x00, "data": 0xAF},
    "lab_zephyr_qemu": {"board": "qemu_cortex_m0", "west_cmd": "west build -b qemu_cortex_m0 app", "physical_status": "PHYSICAL_PENDING", "qemu_ok": True},
    "lab_devicetree": {"overlay": "&i2c1 { status = \"okay\"; }; / { leds { led0: led_0 { gpios = <&gpio0 13 0>; }; }; };", "i2c1_status": "okay", "led0_gpios": "gpio0.13"},
    "lab_pcb_erc_drc": {"erc_errors": 0, "drc_errors": 0, "unconnected_power": False, "bom_lines": [{"mpn": "nRF52840"}, {"mpn": "AMS1117-3.3"}, {"mpn": "SSD1306"}]},
    "lab_failure_diagnosis": {"symptoms": ["rail_sag_3v3", "i2c_nack"], "root_cause": "shared_rail_overload", "next_probe": "measure 3V3 under OLED load", "physical_status": "PHYSICAL_PENDING"},
    "lab_charter": {"problem": "Device Lab checkout wait exceeds 15 minutes at noon peak.", "goal_metric": "Reduce median wait from baseline 15m to 8m", "in_scope": ["queue board", "staffing slots"], "out_scope": ["new building"], "fabricated_outcomes": False},
    "lab_raci": {"matrix": [
        {"task": "charter", "roles": {"PM": "A", "Sponsor": "C", "Lead": "R"}},
        {"task": "measure", "roles": {"PM": "C", "Analyst": "A", "Lead": "R"}},
        {"task": "control", "roles": {"PM": "A", "Analyst": "R", "Sponsor": "I"}},
    ]},
    "lab_wbs_schedule": {"tasks": [
        {"id": "A", "days": 2, "preds": []},
        {"id": "B", "days": 3, "preds": ["A"]},
        {"id": "C", "days": 2, "preds": ["A"]},
        {"id": "D", "days": 4, "preds": ["B", "C"]},
    ], "critical_path_days": 9.0},
    "lab_sprint_board": {"capacity": 20, "committed": 18, "done_items": [{"id": "S1", "acceptance": "Wait metric dashboard live"}]},
    "lab_risk_register": {"risks": [
        {"id": "R1", "prob": 3, "impact": 5, "score": 15, "response": "cross-train"},
        {"id": "R2", "prob": 2, "impact": 4, "score": 8, "response": "buffer"},
        {"id": "R3", "prob": 1, "impact": 3, "score": 3, "response": "accept"},
    ]},
    "lab_sipoc_process": {"suppliers": ["desk"], "inputs": ["ticket"], "process": ["intake", "triage", "resolve"], "outputs": ["resolved count/day"], "customers": ["patrons"]},
    "lab_pareto_rootcause": {"causes": [{"name": "missing cable", "count": 40}, {"name": "no staff", "count": 30}, {"name": "bad label", "count": 20}, {"name": "other", "count": 10}], "cum_pct_top": 0.9, "root_cause": "cable kit not staged at intake"},
    "lab_control_chart": {"points": [10, 11, 10, 12, 10, 25, 11], "mean": 0, "ucl": 0, "lcl": 0, "out_of_control": []},
    "lab_dmaic_case": {"define": "Problem: noon wait baseline 15m", "measure": "Sample n=60 waits from fixture log", "analyze": "Pareto shows cable kit gaps", "improve": "Stage kits; change staffing slot", "control": "Weekly control chart on wait", "fabricated_outcomes": False},
    "lab_change_status_ai": {"change_request": {"id": "CR-12", "impact": "schedule +2d", "decision": "approve"}, "status_report": "SPI 0.96; top risk R1 mitigated; next: control chart review", "ai_plan_critique": "AI plan understated staffing risk and ignored assumption of cable inventory", "ai_disclosed": True},
}

# Fix control chart reference dynamically
def _fix_cc():
    pts = REFERENCE_002["lab_control_chart"]["points"]
    mean = sum(pts) / len(pts)
    mrs = [abs(pts[i] - pts[i - 1]) for i in range(1, len(pts))]
    sigma = (sum(mrs) / len(mrs) / 1.128)
    ucl, lcl = mean + 3 * sigma, mean - 3 * sigma
    ooc = [i for i, v in enumerate(pts) if v > ucl or v < lcl]
    REFERENCE_002["lab_control_chart"].update({"mean": mean, "ucl": ucl, "lcl": lcl, "out_of_control": ooc})
_fix_cc()

# Fix pareto cum to match algorithm
def _fix_pareto():
    causes = sorted(REFERENCE_002["lab_pareto_rootcause"]["causes"], key=lambda c: -float(c["count"]))
    total = sum(float(c["count"]) for c in causes)
    cum = 0.0
    k = 0
    while k < len(causes) and cum < 0.80:
        cum += float(causes[k]["count"]) / total
        k += 1
    REFERENCE_002["lab_pareto_rootcause"]["cum_pct_top"] = cum
_fix_pareto()

WRONG_002 = {
    "lab_git_conflict": {"parents": ["a"], "survivor_tokens": ["HOURS"], "resolved_text": "def open_hours():\n    HOURS={}\n"},
    "lab_rest_api": {"cases": [], "store_len_after_idempotent_put": 2},
    "lab_db_migration": {"forward_sql": "DELETE FROM checkouts; ALTER TABLE checkouts ADD COLUMN returned_at TIMESTAMP NOT NULL;", "down_sql": "DROP DATABASE", "schema_version": 2},
    "lab_frontend_ui": {"tree": {"children": [{"type": "div", "class": "red"}]}},
    "lab_authz": {"roles": {"desk": {"actions": ["checkout.read"]}, "reader": {"actions": ["checkout.read"]}, "forge-bot": {"actions": ["checkout.close"]}}},
    "lab_automated_testing": {"total": 3, "failed": 2, "tests": []},
    "lab_github_actions_ci": {"on": ["push"], "jobs": [{"name": "deploy", "run": "PASS"}]},
    "lab_deploy_rollback": {"current": "sha256:aaa", "rollback_to": "sha256:aaa", "migrate": "skipped", "health": "starting"},
    "lab_security_review": {"findings": []},
    "lab_observability": {"failed": 50, "total": 10000, "availability": 0.5, "budget_ok": False},
    "lab_spice_network": {"R1": 1000.0, "R2": 3000.0, "Vin": 12.0, "I": 1.0, "Vout": 1.0},
    "lab_thevenin": {"Vin": 12.0, "R1": 1000.0, "R2": 3000.0, "Vth": 1.0, "Rth": 1.0},
    "lab_rc_transient": {"R": 1000.0, "C": 1e-6, "V0": 5.0, "t": 0.001, "tau": 1.0, "Vt": 0.0},
    "lab_logic_gate": {"gate": "NAND", "rows": [{"a": 1, "b": 1, "y": 1}]},
    "lab_power_budget": {"rails": [{"mpn": "fake", "Iq_mA": 100}], "regulator_mA": 50.0, "total_mA": 10, "margin_mA": 5},
    "lab_bus_protocol": {"bus": "I2C", "frame_hex": "3c00af", "addr": 1, "reg": 2, "data": 3},
    "lab_zephyr_qemu": {"board": "pi", "west_cmd": "make", "physical_status": "DONE", "qemu_ok": False},
    "lab_devicetree": {"overlay": "/delete-node/ &soc;", "i2c1_status": "disabled", "led0_gpios": ""},
    "lab_pcb_erc_drc": {"erc_errors": 3, "drc_errors": 2, "unconnected_power": True, "bom_lines": []},
    "lab_failure_diagnosis": {"symptoms": ["ok"], "root_cause": "ghost", "next_probe": "ignore", "physical_status": "DONE"},
    "lab_charter": {"problem": "bad", "goal_metric": "better", "in_scope": [], "out_scope": [], "fabricated_outcomes": True},
    "lab_raci": {"matrix": [{"task": "x", "roles": {"PM": "R", "Lead": "R"}}]},
    "lab_wbs_schedule": {"tasks": [{"id": "A", "days": 1, "preds": []}], "critical_path_days": 99},
    "lab_sprint_board": {"capacity": 10, "committed": 50, "done_items": [{"id": "S1"}]},
    "lab_risk_register": {"risks": [{"id": "R1", "prob": 2, "impact": 2, "score": 9, "response": ""}]},
    "lab_sipoc_process": {"suppliers": [], "inputs": [], "process": ["a"], "outputs": ["vibes"], "customers": []},
    "lab_pareto_rootcause": {"causes": [{"name": "a", "count": 1}], "cum_pct_top": 0.1, "root_cause": "x"},
    "lab_control_chart": {"points": [1, 2, 3], "mean": 0, "ucl": 0, "lcl": 0, "out_of_control": [9]},
    "lab_dmaic_case": {"define": "x", "measure": "x", "analyze": "x", "improve": "x", "control": "x", "fabricated_outcomes": True},
    "lab_change_status_ai": {"change_request": {"id": "CR", "impact": "", "decision": "maybe"}, "status_report": "ok", "ai_plan_critique": "fine", "ai_disclosed": False},
}
