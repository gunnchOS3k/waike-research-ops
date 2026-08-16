"""Runnable labs for STREAM-B-PKT-003 — DATA_DASHBOARDS full DIGITAL_RC package.

Ten Pier Ledger Bench labs. Empty/wrong/print-PASS fail. Machine-verifiable data artifacts.
"""
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
    if not isinstance(submission, dict):
        return None, "submission_not_object"
    if submission == {}:
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


COURSE = "DATA_DASHBOARDS"
B = (
    "DATA_DASHBOARDS Pier Ledger Bench fixture. Not a student/teacher E6. "
    "Distinct from DATA_VIZ_BI. Instructor keys stay out of learner modes. "
    "COURSE_DIGITAL_RC only when full package bar holds."
)


def lab_schema_ingest(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_schema_ingest", COURSE, submission,
        ["table", "columns", "row_count", "source_sha256", "invented_columns"], B,
    )
    if data is None:
        return _result("lab_schema_ingest", COURSE, checks, B)
    cols = data.get("columns") or []
    invented = data.get("invented_columns")
    checks.append(_check("table", str(data.get("table") or "") == "pier_visits", "table=pier_visits"))
    checks.append(_check("columns_list", isinstance(cols, list) and len(cols) >= 4, "≥4 columns"))
    checks.append(_check("required_cols", {"visit_id", "pier_bay", "ts_utc", "headcount"}.issubset(set(cols)), "core cols"))
    checks.append(_check("row_count", int(data.get("row_count") or 0) >= 3, "row_count ≥3"))
    checks.append(_check("sha", len(str(data.get("source_sha256") or "")) >= 16, "source_sha256"))
    checks.append(_check("no_invented", invented is False or invented == [], "no invented columns"))
    return _result("lab_schema_ingest", COURSE, checks, B)


def lab_sql_select(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sql_select", COURSE, submission,
        ["sql_text", "filter_count", "has_where", "threshold"], B,
    )
    if data is None:
        return _result("lab_sql_select", COURSE, checks, B)
    sql = str(data.get("sql_text") or "")
    checks.append(_check("has_where", data.get("has_where") is True and "where" in sql.lower(), "WHERE present"))
    checks.append(_check("threshold", int(data.get("threshold") or 0) == 40, "threshold=40"))
    checks.append(_check("filter_count", int(data.get("filter_count") or -1) >= 1, "filter_count ≥1"))
    checks.append(_check("sql_depth", len(sql) >= 24, "sql_text ≥24"))
    checks.append(_check("no_select_star_only", not (sql.strip().lower() == "select *"), "not SELECT * alone"))
    return _result("lab_sql_select", COURSE, checks, B)


def lab_normalize_transform(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_normalize_transform", COURSE, submission,
        ["normalize_map", "rows_in", "rows_out", "null_rate", "negatives_dropped"], B,
    )
    if data is None:
        return _result("lab_normalize_transform", COURSE, checks, B)
    nmap = data.get("normalize_map") or {}
    rows_in = int(data.get("rows_in") or 0)
    rows_out = int(data.get("rows_out") or 0)
    checks.append(_check("map", isinstance(nmap, dict) and len(nmap) >= 2, "normalize_map ≥2"))
    checks.append(_check("rows_in", rows_in >= 3, "rows_in ≥3"))
    checks.append(_check("rows_out", 0 < rows_out <= rows_in, "rows_out ≤ rows_in"))
    checks.append(_check("null_rate", 0 <= float(data.get("null_rate") or -1) <= 1, "null_rate 0..1"))
    checks.append(_check("negatives_dropped", data.get("negatives_dropped") is True, "negatives_dropped"))
    return _result("lab_normalize_transform", COURSE, checks, B)


def lab_kpi_calc(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_kpi_calc", COURSE, submission,
        ["avg_headcount", "p95_headcount", "n", "fabricated_lift"], B,
    )
    if data is None:
        return _result("lab_kpi_calc", COURSE, checks, B)
    n = int(data.get("n") or 0)
    avg = float(data.get("avg_headcount") or -1)
    p95 = float(data.get("p95_headcount") or -1)
    checks.append(_check("n", n >= 3, "n ≥3"))
    checks.append(_check("avg", avg > 0, "avg_headcount > 0"))
    checks.append(_check("p95", p95 >= avg, "p95 ≥ avg"))
    checks.append(_check("no_fabricated", data.get("fabricated_lift") is False, "fabricated_lift false"))
    return _result("lab_kpi_calc", COURSE, checks, B)


def lab_dashboard_chart(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dashboard_chart", COURSE, submission,
        ["chart_type", "x_field", "y_field", "title", "alt_text", "color_only"], B,
    )
    if data is None:
        return _result("lab_dashboard_chart", COURSE, checks, B)
    checks.append(_check("chart_type", str(data.get("chart_type") or "") in ("bar", "line", "scatter"), "allowed type"))
    checks.append(_check("x_field", bool(str(data.get("x_field") or "").strip()), "x_field"))
    checks.append(_check("y_field", bool(str(data.get("y_field") or "").strip()), "y_field"))
    checks.append(_check("title", len(str(data.get("title") or "")) >= 8, "title ≥8"))
    checks.append(_check("alt_text", len(str(data.get("alt_text") or "")) >= 12, "alt_text ≥12"))
    checks.append(_check("no_color_only", data.get("color_only") is False, "color_only false"))
    return _result("lab_dashboard_chart", COURSE, checks, B)


def lab_join_integrity(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_join_integrity", COURSE, submission,
        ["join_key", "join_type", "orphan_count", "duplicate_meta_keys", "rows_joined"], B,
    )
    if data is None:
        return _result("lab_join_integrity", COURSE, checks, B)
    checks.append(_check("join_key", str(data.get("join_key") or "") == "pier_bay", "join_key=pier_bay"))
    checks.append(_check("join_type", str(data.get("join_type") or "") in ("inner", "left"), "inner|left"))
    orphan = data.get("orphan_count")
    checks.append(_check("orphan_count", isinstance(orphan, int) and orphan == 0, "orphan_count=0 on fixture"))
    checks.append(_check("no_dup_meta", data.get("duplicate_meta_keys") is False, "no duplicate meta"))
    checks.append(_check("rows_joined", int(data.get("rows_joined") or 0) >= 3, "rows_joined ≥3"))
    return _result("lab_join_integrity", COURSE, checks, B)


def lab_pii_redact_etl(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_pii_redact_etl", COURSE, submission,
        ["redactions", "pii_remaining", "biometric_claim", "fields_redacted"], B,
    )
    if data is None:
        return _result("lab_pii_redact_etl", COURSE, checks, B)
    fields = data.get("fields_redacted") or []
    checks.append(_check("redactions", int(data.get("redactions") or 0) >= 1, "redactions ≥1"))
    checks.append(_check("pii_gone", data.get("pii_remaining") is False, "pii_remaining false"))
    checks.append(_check("no_bio", data.get("biometric_claim") is False, "biometric_claim false"))
    checks.append(_check("fields", isinstance(fields, list) and len(fields) >= 1, "fields_redacted"))
    return _result("lab_pii_redact_etl", COURSE, checks, B)


def lab_debug_pipeline(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_debug_pipeline", COURSE, submission,
        ["failed_stage", "error_code", "fix_action", "stage_rerun_ok"], B,
    )
    if data is None:
        return _result("lab_debug_pipeline", COURSE, checks, B)
    stage = str(data.get("failed_stage") or "")
    checks.append(_check("stage", stage in ("ingest", "transform", "calc", "chart"), "known stage"))
    checks.append(_check("error_code", len(str(data.get("error_code") or "")) >= 4, "error_code"))
    checks.append(_check("fix_action", len(str(data.get("fix_action") or "")) >= 12, "fix_action ≥12"))
    checks.append(_check("rerun_ok", data.get("stage_rerun_ok") is True, "stage_rerun_ok"))
    return _result("lab_debug_pipeline", COURSE, checks, B)


def lab_freshness_sla(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_freshness_sla", COURSE, submission,
        ["lag_minutes", "sla_minutes", "sla_ok", "claim_live_when_stale"], B,
    )
    if data is None:
        return _result("lab_freshness_sla", COURSE, checks, B)
    lag = int(data.get("lag_minutes") or 9999)
    sla = int(data.get("sla_minutes") or 0)
    sla_ok = data.get("sla_ok")
    checks.append(_check("sla_minutes", sla == 60, "sla_minutes=60"))
    checks.append(_check("lag", lag >= 0, "lag_minutes ≥0"))
    expected_ok = lag <= sla
    checks.append(_check("sla_ok_honest", sla_ok is expected_ok, "sla_ok matches lag≤sla"))
    checks.append(_check("no_stale_live", data.get("claim_live_when_stale") is False, "no stale live claim"))
    return _result("lab_freshness_sla", COURSE, checks, B)


def lab_dashboard_capstone(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_dashboard_capstone", COURSE, submission,
        ["labs_passed", "schema_ok", "kpi_ok", "chart_ok", "pii_ok", "freshness_ok", "no_key_leak", "fabricated_lift"], B,
    )
    if data is None:
        return _result("lab_dashboard_capstone", COURSE, checks, B)
    checks.append(_check("labs_passed", int(data.get("labs_passed") or 0) >= 6, "labs_passed ≥6"))
    for flag in ("schema_ok", "kpi_ok", "chart_ok", "pii_ok", "freshness_ok", "no_key_leak"):
        checks.append(_check(flag, data.get(flag) is True, f"{flag} true"))
    checks.append(_check("no_fabricated", data.get("fabricated_lift") is False, "fabricated_lift false"))
    return _result("lab_dashboard_capstone", COURSE, checks, B)


LABS_006 = {
    "lab_schema_ingest": lab_schema_ingest,
    "lab_sql_select": lab_sql_select,
    "lab_normalize_transform": lab_normalize_transform,
    "lab_kpi_calc": lab_kpi_calc,
    "lab_dashboard_chart": lab_dashboard_chart,
    "lab_join_integrity": lab_join_integrity,
    "lab_pii_redact_etl": lab_pii_redact_etl,
    "lab_debug_pipeline": lab_debug_pipeline,
    "lab_freshness_sla": lab_freshness_sla,
    "lab_dashboard_capstone": lab_dashboard_capstone,
}

COURSE_LABS_006 = {COURSE: list(LABS_006.keys())}

LAB_SPECS_006 = {
    "lab_schema_ingest": {
        "title": "schema ingest",
        "readme": "DL-3101 Pier Ledger ingest: table pier_visits; columns include visit_id/pier_bay/ts_utc/headcount; row_count≥3; source_sha256; invented_columns false/[]. Distinct from DATA_VIZ_BI — schema before tiles.",
        "required_keys": [],
        "wrong_hint": "Wrong table, invented columns, tiny row_count, or missing sha fail.",
        "course_id": COURSE,
    },
    "lab_sql_select": {
        "title": "SQL select",
        "readme": "DL-3204 SELECT with WHERE; threshold=40; filter_count≥1; sql_text includes WHERE. SELECT * alone fails.",
        "required_keys": [],
        "wrong_hint": "Missing WHERE, wrong threshold, or empty filter_count fail.",
        "course_id": COURSE,
    },
    "lab_normalize_transform": {
        "title": "normalize transform",
        "readme": "DL-3307 normalize_map≥2 aliases; rows_out≤rows_in; null_rate 0..1; negatives_dropped true.",
        "required_keys": [],
        "wrong_hint": "Empty map, rows_out>rows_in, or negatives_dropped false fail.",
        "course_id": COURSE,
    },
    "lab_kpi_calc": {
        "title": "KPI calc",
        "readme": "DL-3409 NO_AI: avg_headcount>0; p95≥avg; n≥3; fabricated_lift false.",
        "required_keys": [],
        "wrong_hint": "fabricated_lift true or non-positive avg fail.",
        "course_id": COURSE,
    },
    "lab_dashboard_chart": {
        "title": "dashboard chart",
        "readme": "DL-3511 chart_type bar|line|scatter; x/y fields; title≥8; alt_text≥12; color_only false.",
        "required_keys": [],
        "wrong_hint": "color_only true, tiny alt_text, or missing axes fail.",
        "course_id": COURSE,
    },
    "lab_join_integrity": {
        "title": "join integrity",
        "readme": "DL-3615 join_key=pier_bay; join_type inner|left; orphan_count=0; duplicate_meta_keys false; rows_joined≥3.",
        "required_keys": [],
        "wrong_hint": "orphans, duplicate meta, or wrong join_key fail.",
        "course_id": COURSE,
    },
    "lab_pii_redact_etl": {
        "title": "PII redact ETL",
        "readme": "DL-3718 redactions≥1; pii_remaining false; biometric_claim false; fields_redacted nonempty.",
        "required_keys": [],
        "wrong_hint": "pii_remaining true or biometric_claim true fail.",
        "course_id": COURSE,
    },
    "lab_debug_pipeline": {
        "title": "debug pipeline",
        "readme": "DL-3822 failed_stage∈{ingest,transform,calc,chart}; error_code; fix_action≥12; stage_rerun_ok true.",
        "required_keys": [],
        "wrong_hint": "Unknown stage, short fix, or stage_rerun_ok false fail.",
        "course_id": COURSE,
    },
    "lab_freshness_sla": {
        "title": "freshness SLA",
        "readme": "DL-3925 NO_AI: sla_minutes=60; sla_ok matches lag≤sla; claim_live_when_stale false.",
        "required_keys": [],
        "wrong_hint": "Dishonest sla_ok or stale live claim fail.",
        "course_id": COURSE,
    },
    "lab_dashboard_capstone": {
        "title": "dashboard capstone",
        "readme": "DL-3A30 labs_passed≥6; schema/kpi/chart/pii/freshness/no_key_leak true; fabricated_lift false. REAL_*_E6 false.",
        "required_keys": [],
        "wrong_hint": "labs_passed<6 or any honesty flag wrong fails.",
        "course_id": COURSE,
    },
}

REFERENCE_006 = {
    "lab_schema_ingest": {
        "table": "pier_visits",
        "columns": ["visit_id", "pier_bay", "ts_utc", "headcount", "source_file"],
        "row_count": 12,
        "source_sha256": "a1b2c3d4e5f6789012345678deadbeef",
        "invented_columns": False,
    },
    "lab_sql_select": {
        "sql_text": "SELECT pier_bay, headcount FROM pier_visits WHERE headcount > 40 AND ts_utc >= '18:00'",
        "filter_count": 3,
        "has_where": True,
        "threshold": 40,
    },
    "lab_normalize_transform": {
        "normalize_map": {"Bay-A": "bay_a", "bay_a": "bay_a", "BAY A": "bay_a"},
        "rows_in": 20,
        "rows_out": 17,
        "null_rate": 0.1,
        "negatives_dropped": True,
    },
    "lab_kpi_calc": {
        "avg_headcount": 28.5,
        "p95_headcount": 44.0,
        "n": 17,
        "fabricated_lift": False,
    },
    "lab_dashboard_chart": {
        "chart_type": "bar",
        "x_field": "pier_bay",
        "y_field": "avg_headcount",
        "title": "Pier bay average headcount",
        "alt_text": "Bar chart of average headcount by pier bay",
        "color_only": False,
    },
    "lab_join_integrity": {
        "join_key": "pier_bay",
        "join_type": "inner",
        "orphan_count": 0,
        "duplicate_meta_keys": False,
        "rows_joined": 17,
    },
    "lab_pii_redact_etl": {
        "redactions": 4,
        "pii_remaining": False,
        "biometric_claim": False,
        "fields_redacted": ["email", "phone"],
    },
    "lab_debug_pipeline": {
        "failed_stage": "transform",
        "error_code": "NULL_HEADCOUNT",
        "fix_action": "drop null headcounts then rerun transform",
        "stage_rerun_ok": True,
    },
    "lab_freshness_sla": {
        "lag_minutes": 12,
        "sla_minutes": 60,
        "sla_ok": True,
        "claim_live_when_stale": False,
    },
    "lab_dashboard_capstone": {
        "labs_passed": 9,
        "schema_ok": True,
        "kpi_ok": True,
        "chart_ok": True,
        "pii_ok": True,
        "freshness_ok": True,
        "no_key_leak": True,
        "fabricated_lift": False,
    },
}

WRONG_006 = {
    "lab_schema_ingest": {
        "table": "vibes", "columns": ["vibe_score"], "row_count": 0,
        "source_sha256": "x", "invented_columns": True,
    },
    "lab_sql_select": {
        "sql_text": "SELECT *", "filter_count": 0, "has_where": False, "threshold": 0,
    },
    "lab_normalize_transform": {
        "normalize_map": {}, "rows_in": 1, "rows_out": 9, "null_rate": 2.0, "negatives_dropped": False,
    },
    "lab_kpi_calc": {
        "avg_headcount": -1, "p95_headcount": -2, "n": 0, "fabricated_lift": True,
    },
    "lab_dashboard_chart": {
        "chart_type": "pie_only_color", "x_field": "", "y_field": "", "title": "x",
        "alt_text": "x", "color_only": True,
    },
    "lab_join_integrity": {
        "join_key": "ssn", "join_type": "cross", "orphan_count": 9,
        "duplicate_meta_keys": True, "rows_joined": 0,
    },
    "lab_pii_redact_etl": {
        "redactions": 0, "pii_remaining": True, "biometric_claim": True, "fields_redacted": [],
    },
    "lab_debug_pipeline": {
        "failed_stage": "ai", "error_code": "x", "fix_action": "idk", "stage_rerun_ok": False,
    },
    "lab_freshness_sla": {
        "lag_minutes": 900, "sla_minutes": 60, "sla_ok": True, "claim_live_when_stale": True,
    },
    "lab_dashboard_capstone": {
        "labs_passed": 1, "schema_ok": False, "kpi_ok": False, "chart_ok": False,
        "pii_ok": False, "freshness_ok": False, "no_key_leak": False, "fabricated_lift": True,
    },
}
