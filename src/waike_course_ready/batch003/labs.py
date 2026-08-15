"""Runnable labs for WAIKE-COURSE-READY-003 with computing validators."""
from __future__ import annotations

import json
import math
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


# ---- AI_ML_EDGE ----

def lab_data_split(submission: Any = None) -> LabResult:
    boundary = "Fixture split math only. Not a live campus dataset export."
    data, checks = _require_student("lab_data_split", "AI_ML_EDGE", submission, ["n", "holdout", "train_n", "val_n", "shuffle"], boundary)
    if data is None:
        return _result("lab_data_split", "AI_ML_EDGE", checks, boundary)
    n, holdout = int(data["n"]), float(data["holdout"])
    train_n, val_n = int(data["train_n"]), int(data["val_n"])
    exp_val = int(round(n * holdout))
    exp_train = n - exp_val
    checks.append(_check("split_math", train_n == exp_train and val_n == exp_val, f"expected train={exp_train} val={exp_val}"))
    checks.append(_check("no_shuffle", data.get("shuffle") is False, "shuffle must be false for time-ordered holdout"))
    return _result("lab_data_split", "AI_ML_EDGE", checks, boundary)


def lab_supervised_metrics(submission: Any = None) -> LabResult:
    boundary = "Confusion arithmetic on fixture counts. Not a vendor exam item."
    data, checks = _require_student(
        "lab_supervised_metrics", "AI_ML_EDGE", submission,
        ["tp", "fp", "fn", "precision", "recall", "f1"], boundary,
    )
    if data is None:
        return _result("lab_supervised_metrics", "AI_ML_EDGE", checks, boundary)
    tp, fp, fn = float(data["tp"]), float(data["fp"]), float(data["fn"])
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * p * r / (p + r)) if (p + r) else 0.0
    checks.append(_check("precision", abs(float(data["precision"]) - p) < 1e-3, f"expected {p:.3f}"))
    checks.append(_check("recall", abs(float(data["recall"]) - r) < 1e-3, f"expected {r:.3f}"))
    checks.append(_check("f1", abs(float(data["f1"]) - f1) < 1e-3, f"expected {f1:.3f}"))
    return _result("lab_supervised_metrics", "AI_ML_EDGE", checks, boundary)


def lab_cluster_assign(submission: Any = None) -> LabResult:
    boundary = "Manhattan assignment on fixture vectors. Not staff accusation."
    data, checks = _require_student(
        "lab_cluster_assign", "AI_ML_EDGE", submission,
        ["point", "centroid_a", "centroid_b", "assignment", "dist_a", "dist_b"], boundary,
    )
    if data is None:
        return _result("lab_cluster_assign", "AI_ML_EDGE", checks, boundary)

    def man(a, b):
        return sum(abs(float(x) - float(y)) for x, y in zip(a, b, strict=True))

    p, a, b = data["point"], data["centroid_a"], data["centroid_b"]
    da, db = man(p, a), man(p, b)
    exp = "B" if db < da else "A"
    checks.append(_check("dist_a", abs(float(data["dist_a"]) - da) < 1e-6, f"expected {da}"))
    checks.append(_check("dist_b", abs(float(data["dist_b"]) - db) < 1e-6, f"expected {db}"))
    checks.append(_check("assignment", data["assignment"] == exp, f"expected {exp}"))
    return _result("lab_cluster_assign", "AI_ML_EDGE", checks, boundary)


def lab_eval_thresholds(submission: Any = None) -> LabResult:
    boundary = "TPR/FPR arithmetic on fixture confusion at a threshold."
    data, checks = _require_student(
        "lab_eval_thresholds", "AI_ML_EDGE", submission,
        ["tp", "fp", "fn", "tn", "tpr", "fpr", "fpr_cap_ok"], boundary,
    )
    if data is None:
        return _result("lab_eval_thresholds", "AI_ML_EDGE", checks, boundary)
    tp, fp, fn, tn = map(float, (data["tp"], data["fp"], data["fn"], data["tn"]))
    tpr = tp / (tp + fn) if (tp + fn) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    checks.append(_check("tpr", abs(float(data["tpr"]) - tpr) < 1e-3, f"expected {tpr:.3f}"))
    checks.append(_check("fpr", abs(float(data["fpr"]) - fpr) < 1e-3, f"expected {fpr:.3f}"))
    checks.append(_check("fpr_cap", bool(data["fpr_cap_ok"]) == (fpr <= 0.20 + 1e-9), "fpr_cap_ok must match FPR≤0.20"))
    return _result("lab_eval_thresholds", "AI_ML_EDGE", checks, boundary)


def lab_overfit_gap(submission: Any = None) -> LabResult:
    boundary = "Gap honesty on fixture accuracies. Not a bigger-model sales pitch."
    data, checks = _require_student(
        "lab_overfit_gap", "AI_ML_EDGE", submission,
        ["train_acc", "val_acc", "gap", "mitigation_note"], boundary,
    )
    if data is None:
        return _result("lab_overfit_gap", "AI_ML_EDGE", checks, boundary)
    gap = float(data["train_acc"]) - float(data["val_acc"])
    checks.append(_check("gap", abs(float(data["gap"]) - gap) < 1e-6, f"expected {gap}"))
    note = str(data.get("mitigation_note") or "")
    if gap >= 0.25:
        checks.append(_check("mitigation", len(note) >= 8, "gap≥0.25 requires mitigation_note"))
    else:
        checks.append(_check("mitigation", True, "gap below threshold"))
    return _result("lab_overfit_gap", "AI_ML_EDGE", checks, boundary)


def lab_feature_windows(submission: Any = None) -> LabResult:
    boundary = "Causal trailing mean on fixture series. No future frames."
    data, checks = _require_student(
        "lab_feature_windows", "AI_ML_EDGE", submission,
        ["series", "window", "index", "mean", "uses_future"], boundary,
    )
    if data is None:
        return _result("lab_feature_windows", "AI_ML_EDGE", checks, boundary)
    series = [float(x) for x in data["series"]]
    w, idx = int(data["window"]), int(data["index"])
    start = idx - w + 1
    ok_range = start >= 0 and idx < len(series)
    exp = sum(series[start : idx + 1]) / w if ok_range else None
    checks.append(_check("range", ok_range, "window must fit causally"))
    checks.append(_check("mean", ok_range and abs(float(data["mean"]) - exp) < 1e-6, f"expected {exp}"))
    checks.append(_check("no_future", data.get("uses_future") is False, "uses_future must be false"))
    return _result("lab_feature_windows", "AI_ML_EDGE", checks, boundary)


def lab_tiny_mlp_forward(submission: Any = None) -> LabResult:
    boundary = "Tiny 2×2×1 forward pass on published weights. Not ImageNet."
    data, checks = _require_student(
        "lab_tiny_mlp_forward", "AI_ML_EDGE", submission,
        ["x", "y_hat"], boundary,
    )
    if data is None:
        return _result("lab_tiny_mlp_forward", "AI_ML_EDGE", checks, boundary)
    # Fixed published weights
    W1 = [[0.5, -0.2], [0.1, 0.4]]
    b1 = [0.0, 0.1]
    W2 = [0.7, -0.3]
    b2 = 0.2
    x = [float(v) for v in data["x"]]
    h = []
    for i in range(2):
        z = W1[i][0] * x[0] + W1[i][1] * x[1] + b1[i]
        h.append(max(0.0, z))
    z2 = W2[0] * h[0] + W2[1] * h[1] + b2
    y = 1.0 / (1.0 + math.exp(-z2))
    checks.append(_check("y_hat", abs(float(data["y_hat"]) - y) < 1e-3, f"expected {y:.4f}"))
    return _result("lab_tiny_mlp_forward", "AI_ML_EDGE", checks, boundary)


def lab_score_model(submission: Any = None) -> LabResult:
    boundary = "Digest-pinned scoring on fixture vectors. Refuse digest mismatch."
    data, checks = _require_student(
        "lab_score_model", "AI_ML_EDGE", submission,
        ["scores", "threshold", "labels", "model_digest", "digest_ok"], boundary,
    )
    if data is None:
        return _result("lab_score_model", "AI_ML_EDGE", checks, boundary)
    expected_digest = "sha256:ef2803aa"
    th = float(data["threshold"])
    labels = [1 if float(s) >= th else 0 for s in data["scores"]]
    checks.append(_check("labels", list(data["labels"]) == labels, f"expected {labels}"))
    checks.append(_check("digest", data["model_digest"] == expected_digest and bool(data["digest_ok"]) is True, "digest must match sha256:ef2803aa"))
    return _result("lab_score_model", "AI_ML_EDGE", checks, boundary)


def lab_quantize_budget(submission: Any = None) -> LabResult:
    boundary = "Size/latency budget math. PHYSICAL_PENDING for device flash."
    data, checks = _require_student(
        "lab_quantize_budget", "AI_ML_EDGE", submission,
        ["params", "fp32_bytes", "int8_bytes", "ratio", "latency_ms", "sla_ms", "budget_ok", "physical_status"], boundary,
    )
    if data is None:
        return _result("lab_quantize_budget", "AI_ML_EDGE", checks, boundary)
    params = int(data["params"])
    checks.append(_check("fp32", int(data["fp32_bytes"]) == params * 4, "fp32_bytes=params*4"))
    checks.append(_check("int8", int(data["int8_bytes"]) == params, "int8_bytes=params"))
    ratio = float(data["int8_bytes"]) / float(data["fp32_bytes"])
    checks.append(_check("ratio", abs(float(data["ratio"]) - ratio) < 1e-6, f"expected {ratio}"))
    ok = float(data["latency_ms"]) <= float(data["sla_ms"])
    checks.append(_check("budget", bool(data["budget_ok"]) == ok, "budget_ok must match SLA"))
    checks.append(_check("physical", data.get("physical_status") == "PHYSICAL_PENDING", "flash remains PHYSICAL_PENDING"))
    return _result("lab_quantize_budget", "AI_ML_EDGE", checks, boundary)


def lab_rag_redact(submission: Any = None) -> LabResult:
    boundary = "Fixture RAG retrieve+redact. No biometric identification claims."
    data, checks = _require_student(
        "lab_rag_redact", "AI_ML_EDGE", submission,
        ["hits", "redactions", "biometric_claim"], boundary,
    )
    if data is None:
        return _result("lab_rag_redact", "AI_ML_EDGE", checks, boundary)
    checks.append(_check("hits", list(data["hits"]) == ["R12", "R19"], "expected hits R12,R19"))
    checks.append(_check("redactions", int(data["redactions"]) >= 2, "redact ≥2 contact strings"))
    checks.append(_check("biometric", data.get("biometric_claim") is False, "biometric_claim must be false"))
    return _result("lab_rag_redact", "AI_ML_EDGE", checks, boundary)


# ---- DATA_VIZ_BI ----

def lab_clean_nulls(submission: Any = None) -> LabResult:
    boundary = "Null-rate and drop policy on fixture waits. Not a live mayor feed."
    data, checks = _require_student(
        "lab_clean_nulls", "DATA_VIZ_BI", submission,
        ["rows", "nulls", "null_rate", "negatives_dropped"], boundary,
    )
    if data is None:
        return _result("lab_clean_nulls", "DATA_VIZ_BI", checks, boundary)
    rate = float(data["nulls"]) / float(data["rows"])
    checks.append(_check("null_rate", abs(float(data["null_rate"]) - rate) < 1e-9, f"expected {rate}"))
    checks.append(_check("negatives", data.get("negatives_dropped") is True, "negatives must be dropped"))
    return _result("lab_clean_nulls", "DATA_VIZ_BI", checks, boundary)


def lab_sql_join_counts(submission: Any = None) -> LabResult:
    boundary = "Join cardinality on fixture tables. Cartesian trap must be named."
    data, checks = _require_student(
        "lab_sql_join_counts", "DATA_VIZ_BI", submission,
        ["tickets", "zones", "matched", "joined_rows", "cartesian_trap_rows"], boundary,
    )
    if data is None:
        return _result("lab_sql_join_counts", "DATA_VIZ_BI", checks, boundary)
    checks.append(_check("joined", int(data["joined_rows"]) == int(data["matched"]), "joined_rows=matched"))
    cart = int(data["tickets"]) * int(data["zones"])
    checks.append(_check("cartesian", int(data["cartesian_trap_rows"]) == cart, f"expected {cart}"))
    return _result("lab_sql_join_counts", "DATA_VIZ_BI", checks, boundary)


def lab_schema_nf(submission: Any = None) -> LabResult:
    boundary = "Normalize repeating zone_address out of tickets."
    data, checks = _require_student("lab_schema_nf", "DATA_VIZ_BI", submission, ["tables"], boundary)
    if data is None:
        return _result("lab_schema_nf", "DATA_VIZ_BI", checks, boundary)
    tables = {t["name"]: t for t in data["tables"]}
    checks.append(_check("has_zone_dim", "zone_dim" in tables, "need zone_dim"))
    checks.append(_check("has_tickets", "tickets" in tables, "need tickets"))
    tcols = set(tables.get("tickets", {}).get("columns") or [])
    checks.append(_check("no_address_on_tickets", "zone_address" not in tcols and "zone_id" in tcols, "tickets keep zone_id only"))
    zcols = set(tables.get("zone_dim", {}).get("columns") or [])
    checks.append(_check("address_on_dim", "zone_address" in zcols or "address" in zcols, "address lives on zone_dim"))
    return _result("lab_schema_nf", "DATA_VIZ_BI", checks, boundary)


def lab_stats_summary(submission: Any = None) -> LabResult:
    boundary = "Mean/median/IQR on fixture waits. NO_AI generative fill forbidden."
    data, checks = _require_student(
        "lab_stats_summary", "DATA_VIZ_BI", submission,
        ["values", "mean", "median", "iqr"], boundary,
    )
    if data is None:
        return _result("lab_stats_summary", "DATA_VIZ_BI", checks, boundary)
    vals = sorted(float(v) for v in data["values"])
    n = len(vals)
    mean = sum(vals) / n
    mid = n // 2
    median = vals[mid] if n % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    q1 = vals[n // 4]
    q3 = vals[(3 * n) // 4]
    iqr = q3 - q1
    checks.append(_check("mean", abs(float(data["mean"]) - mean) < 1e-6, f"expected {mean}"))
    checks.append(_check("median", abs(float(data["median"]) - median) < 1e-6, f"expected {median}"))
    checks.append(_check("iqr", abs(float(data["iqr"]) - iqr) < 1e-6, f"expected {iqr}"))
    return _result("lab_stats_summary", "DATA_VIZ_BI", checks, boundary)


def lab_chart_encode(submission: Any = None) -> LabResult:
    boundary = "Encoding validity for civic wait charts."
    data, checks = _require_student(
        "lab_chart_encode", "DATA_VIZ_BI", submission,
        ["mark", "x", "y", "invalid_rejected"], boundary,
    )
    if data is None:
        return _result("lab_chart_encode", "DATA_VIZ_BI", checks, boundary)
    ok = data.get("mark") == "bar" and data.get("x") == "zone" and data.get("y") == "median_wait"
    checks.append(_check("encoding", ok, "expect bar/zone/median_wait"))
    checks.append(_check("invalid_rejected", data.get("invalid_rejected") is True, "must reject pie(ticket_id)"))
    return _result("lab_chart_encode", "DATA_VIZ_BI", checks, boundary)


def lab_dashboard_layout(submission: Any = None) -> LabResult:
    boundary = "Three-tile first screen with freshness."
    data, checks = _require_student(
        "lab_dashboard_layout", "DATA_VIZ_BI", submission,
        ["tiles", "max_tiles"], boundary,
    )
    if data is None:
        return _result("lab_dashboard_layout", "DATA_VIZ_BI", checks, boundary)
    tiles = set(data["tiles"])
    need = {"median_by_zone", "open_count", "freshness"}
    checks.append(_check("tiles", need.issubset(tiles), f"need {need}"))
    checks.append(_check("max", int(data["max_tiles"]) == 3 and len(data["tiles"]) <= 3, "max_tiles=3"))
    return _result("lab_dashboard_layout", "DATA_VIZ_BI", checks, boundary)


def lab_bi_refresh(submission: Any = None) -> LabResult:
    boundary = "Refresh SLA + license honesty. No binary redistribution."
    data, checks = _require_student(
        "lab_bi_refresh", "DATA_VIZ_BI", submission,
        ["refresh_minutes", "sla_minutes", "meets_sla", "license_ok"], boundary,
    )
    if data is None:
        return _result("lab_bi_refresh", "DATA_VIZ_BI", checks, boundary)
    meets = float(data["refresh_minutes"]) <= float(data["sla_minutes"])
    checks.append(_check("sla", bool(data["meets_sla"]) == meets, "meets_sla mismatch"))
    checks.append(_check("license", data.get("license_ok") is True, "license_ok must be true (no piracy)"))
    return _result("lab_bi_refresh", "DATA_VIZ_BI", checks, boundary)


def lab_pandas_group(submission: Any = None) -> LabResult:
    boundary = "Group medians on fixture + input digest."
    data, checks = _require_student(
        "lab_pandas_group", "DATA_VIZ_BI", submission,
        ["medians", "input_sha256"], boundary,
    )
    if data is None:
        return _result("lab_pandas_group", "DATA_VIZ_BI", checks, boundary)
    exp = {"A": 10, "B": 14, "C": 12}
    got = {k: float(v) for k, v in dict(data["medians"]).items()}
    checks.append(_check("medians", got == {k: float(v) for k, v in exp.items()}, f"expected {exp}"))
    checks.append(_check("hash", isinstance(data["input_sha256"], str) and len(data["input_sha256"]) >= 16, "input_sha256 required"))
    return _result("lab_pandas_group", "DATA_VIZ_BI", checks, boundary)


def lab_kpi_tree(submission: Any = None) -> LabResult:
    boundary = "Auditable KPI formula on fixture numbers."
    data, checks = _require_student(
        "lab_kpi_tree", "DATA_VIZ_BI", submission,
        ["open_count", "median_wait", "staff_on_duty", "desk_pressure"], boundary,
    )
    if data is None:
        return _result("lab_kpi_tree", "DATA_VIZ_BI", checks, boundary)
    exp = float(data["open_count"]) * float(data["median_wait"]) / float(data["staff_on_duty"])
    checks.append(_check("kpi", abs(float(data["desk_pressure"]) - exp) < 1e-6, f"expected {exp}"))
    return _result("lab_kpi_tree", "DATA_VIZ_BI", checks, boundary)


def lab_repro_hash(submission: Any = None) -> LabResult:
    boundary = "Portfolio quality gates + csv sha256."
    data, checks = _require_student(
        "lab_repro_hash", "DATA_VIZ_BI", submission,
        ["null_rate", "negatives_dropped", "freshness_minutes", "csv_sha256", "quality_ok"], boundary,
    )
    if data is None:
        return _result("lab_repro_hash", "DATA_VIZ_BI", checks, boundary)
    ok = (
        float(data["null_rate"]) <= 0.05
        and data.get("negatives_dropped") is True
        and float(data["freshness_minutes"]) <= 15
        and isinstance(data["csv_sha256"], str)
        and len(data["csv_sha256"]) >= 16
    )
    checks.append(_check("quality", bool(data["quality_ok"]) == ok, "quality_ok mismatch"))
    return _result("lab_repro_hash", "DATA_VIZ_BI", checks, boundary)


# ---- CLOUD_DEVOPS ----

def lab_linux_perms(submission: Any = None) -> LabResult:
    boundary = "Mode arithmetic on fixture deploy key. Not a live bastion mutate."
    data, checks = _require_student(
        "lab_linux_perms", "CLOUD_DEVOPS", submission,
        ["mode_octal", "mode_str", "world_writable"], boundary,
    )
    if data is None:
        return _result("lab_linux_perms", "CLOUD_DEVOPS", checks, boundary)
    checks.append(_check("mode", int(data["mode_octal"]) == 0o600 and data["mode_str"] == "0600", "expect 0600 / 384"))
    checks.append(_check("not_world", data.get("world_writable") is False, "world_writable must be false"))
    return _result("lab_linux_perms", "CLOUD_DEVOPS", checks, boundary)


def lab_git_state(submission: Any = None) -> LabResult:
    boundary = "Ahead/behind + conflict path. No force-push main."
    data, checks = _require_student(
        "lab_git_state", "CLOUD_DEVOPS", submission,
        ["ahead", "behind", "conflict_files", "force_push_main"], boundary,
    )
    if data is None:
        return _result("lab_git_state", "CLOUD_DEVOPS", checks, boundary)
    checks.append(_check("ahead_behind", int(data["ahead"]) == 2 and int(data["behind"]) == 0, "ahead=2 behind=0"))
    checks.append(_check("conflict", list(data["conflict_files"]) == ["services/api/health.py"], "conflict path"))
    checks.append(_check("no_force", data.get("force_push_main") is False, "force_push_main false"))
    return _result("lab_git_state", "CLOUD_DEVOPS", checks, boundary)


def lab_dockerfile_lint(submission: Any = None) -> LabResult:
    boundary = "Dockerfile lint on fixture flags."
    data, checks = _require_student(
        "lab_dockerfile_lint", "CLOUD_DEVOPS", submission,
        ["pinned_digest", "user_non_root", "uses_latest", "lint_ok"], boundary,
    )
    if data is None:
        return _result("lab_dockerfile_lint", "CLOUD_DEVOPS", checks, boundary)
    ok = data.get("pinned_digest") is True and data.get("user_non_root") is True and data.get("uses_latest") is False
    checks.append(_check("flags", ok, "pinned + nonroot + no latest"))
    checks.append(_check("lint_ok", bool(data["lint_ok"]) == ok, "lint_ok mismatch"))
    return _result("lab_dockerfile_lint", "CLOUD_DEVOPS", checks, boundary)


def lab_cicd_gate(submission: Any = None) -> LabResult:
    boundary = "PR pipeline order + no ungated deploy."
    data, checks = _require_student(
        "lab_cicd_gate", "CLOUD_DEVOPS", submission,
        ["on", "jobs", "deploy_on_pr"], boundary,
    )
    if data is None:
        return _result("lab_cicd_gate", "CLOUD_DEVOPS", checks, boundary)
    checks.append(_check("on", list(data["on"]) == ["pull_request"], "on pull_request"))
    checks.append(_check("jobs", list(data["jobs"]) == ["lint", "test", "upload-report"], "job order"))
    checks.append(_check("deploy", data.get("deploy_on_pr") is False, "deploy_on_pr false"))
    return _result("lab_cicd_gate", "CLOUD_DEVOPS", checks, boundary)


def lab_cloud_cost(submission: Any = None) -> LabResult:
    boundary = "Toy cost_units on fixture rates. Not a real cloud invoice."
    data, checks = _require_student(
        "lab_cloud_cost", "CLOUD_DEVOPS", submission,
        ["vcpu_hours", "storage_gb", "cost_units", "must_be_private"], boundary,
    )
    if data is None:
        return _result("lab_cloud_cost", "CLOUD_DEVOPS", checks, boundary)
    exp = float(data["vcpu_hours"]) * 1.0 + float(data["storage_gb"]) * 0.01
    checks.append(_check("cost", abs(float(data["cost_units"]) - exp) < 1e-6, f"expected {exp}"))
    checks.append(_check("private", data.get("must_be_private") is True, "must_be_private true"))
    return _result("lab_cloud_cost", "CLOUD_DEVOPS", checks, boundary)


def lab_iam_secrets(submission: Any = None) -> LabResult:
    boundary = "Least privilege + no plaintext secrets in git."
    data, checks = _require_student(
        "lab_iam_secrets", "CLOUD_DEVOPS", submission,
        ["allowed", "denied", "plaintext_secrets_found", "vault_path"], boundary,
    )
    if data is None:
        return _result("lab_iam_secrets", "CLOUD_DEVOPS", checks, boundary)
    allowed = set(data["allowed"])
    denied = set(data["denied"])
    checks.append(_check("allow", {"ecr:Upload", "ecs:UpdateService"}.issubset(allowed), "deploy actions"))
    checks.append(_check("deny", "iam:CreateUser" in denied, "CreateUser denied"))
    checks.append(_check("secrets", data.get("plaintext_secrets_found") is False, "no plaintext"))
    checks.append(_check("vault", isinstance(data.get("vault_path"), str) and len(data["vault_path"]) >= 4, "vault path"))
    return _result("lab_iam_secrets", "CLOUD_DEVOPS", checks, boundary)


def lab_slo_budget(submission: Any = None) -> LabResult:
    boundary = "Availability + error-budget arithmetic on fixture counts."
    data, checks = _require_student(
        "lab_slo_budget", "CLOUD_DEVOPS", submission,
        ["failed", "total", "availability", "failure_cap", "budget_ok"], boundary,
    )
    if data is None:
        return _result("lab_slo_budget", "CLOUD_DEVOPS", checks, boundary)
    avail = 1.0 - float(data["failed"]) / float(data["total"])
    ok = int(data["failed"]) <= int(data["failure_cap"])
    checks.append(_check("availability", abs(float(data["availability"]) - avail) < 1e-6, f"expected {avail}"))
    checks.append(_check("budget", bool(data["budget_ok"]) == ok, "budget_ok mismatch"))
    return _result("lab_slo_budget", "CLOUD_DEVOPS", checks, boundary)


def lab_deploy_rollback_cloud(submission: Any = None) -> LabResult:
    boundary = "Digest pin + health/migrate gates for ForgeCloud deploy."
    data, checks = _require_student(
        "lab_deploy_rollback_cloud", "CLOUD_DEVOPS", submission,
        ["current", "rollback_to", "migrate", "health"], boundary,
    )
    if data is None:
        return _result("lab_deploy_rollback_cloud", "CLOUD_DEVOPS", checks, boundary)
    checks.append(_check("differ", data["current"] != data["rollback_to"], "rollback_to must differ"))
    checks.append(_check("migrate", data.get("migrate") == "ok", "migrate ok"))
    checks.append(_check("health", data.get("health") == "healthy", "health healthy"))
    checks.append(_check("digest_form", str(data["current"]).startswith("sha256:"), "current digest form"))
    return _result("lab_deploy_rollback_cloud", "CLOUD_DEVOPS", checks, boundary)


def lab_k8s_probes(submission: Any = None) -> LabResult:
    boundary = "Probe fundamentals on fixture Deployment. No CKA claim."
    data, checks = _require_student(
        "lab_k8s_probes", "CLOUD_DEVOPS", submission,
        ["readiness", "liveness", "replicas", "requests_cpu", "probe_ok"], boundary,
    )
    if data is None:
        return _result("lab_k8s_probes", "CLOUD_DEVOPS", checks, boundary)
    ok = (
        data.get("readiness") == "/readyz"
        and data.get("liveness") == "/healthz"
        and int(data["replicas"]) == 2
        and data.get("requests_cpu") == "100m"
    )
    checks.append(_check("fields", ok, "probes/replicas/cpu"))
    checks.append(_check("probe_ok", bool(data["probe_ok"]) == ok, "probe_ok mismatch"))
    return _result("lab_k8s_probes", "CLOUD_DEVOPS", checks, boundary)


def lab_incident_runbook(submission: Any = None) -> LabResult:
    boundary = "Incident runbook without heroics. Fixture timeline only."
    data, checks = _require_student(
        "lab_incident_runbook", "CLOUD_DEVOPS", submission,
        ["heroics", "automation_runbook_id", "token_rotated", "timeline"], boundary,
    )
    if data is None:
        return _result("lab_incident_runbook", "CLOUD_DEVOPS", checks, boundary)
    checks.append(_check("heroics", data.get("heroics") is False, "heroics must be false"))
    checks.append(_check("runbook", data.get("automation_runbook_id") == "RB-FC-rollback", "runbook id"))
    checks.append(_check("rotate", data.get("token_rotated") is True, "token_rotated"))
    tl = data.get("timeline") or {}
    checks.append(_check("timeline", all(k in tl for k in ("detect", "contain", "recover")), "detect/contain/recover"))
    return _result("lab_incident_runbook", "CLOUD_DEVOPS", checks, boundary)


LABS_003 = {
    "lab_data_split": lab_data_split,
    "lab_supervised_metrics": lab_supervised_metrics,
    "lab_cluster_assign": lab_cluster_assign,
    "lab_eval_thresholds": lab_eval_thresholds,
    "lab_overfit_gap": lab_overfit_gap,
    "lab_feature_windows": lab_feature_windows,
    "lab_tiny_mlp_forward": lab_tiny_mlp_forward,
    "lab_score_model": lab_score_model,
    "lab_quantize_budget": lab_quantize_budget,
    "lab_rag_redact": lab_rag_redact,
    "lab_clean_nulls": lab_clean_nulls,
    "lab_sql_join_counts": lab_sql_join_counts,
    "lab_schema_nf": lab_schema_nf,
    "lab_stats_summary": lab_stats_summary,
    "lab_chart_encode": lab_chart_encode,
    "lab_dashboard_layout": lab_dashboard_layout,
    "lab_bi_refresh": lab_bi_refresh,
    "lab_pandas_group": lab_pandas_group,
    "lab_kpi_tree": lab_kpi_tree,
    "lab_repro_hash": lab_repro_hash,
    "lab_linux_perms": lab_linux_perms,
    "lab_git_state": lab_git_state,
    "lab_dockerfile_lint": lab_dockerfile_lint,
    "lab_cicd_gate": lab_cicd_gate,
    "lab_cloud_cost": lab_cloud_cost,
    "lab_iam_secrets": lab_iam_secrets,
    "lab_slo_budget": lab_slo_budget,
    "lab_deploy_rollback_cloud": lab_deploy_rollback_cloud,
    "lab_k8s_probes": lab_k8s_probes,
    "lab_incident_runbook": lab_incident_runbook,
}

COURSE_LABS_003 = {
    "AI_ML_EDGE": [
        "lab_data_split", "lab_supervised_metrics", "lab_cluster_assign", "lab_eval_thresholds", "lab_overfit_gap",
        "lab_feature_windows", "lab_tiny_mlp_forward", "lab_score_model", "lab_quantize_budget", "lab_rag_redact",
    ],
    "DATA_VIZ_BI": [
        "lab_clean_nulls", "lab_sql_join_counts", "lab_schema_nf", "lab_stats_summary", "lab_chart_encode",
        "lab_dashboard_layout", "lab_bi_refresh", "lab_pandas_group", "lab_kpi_tree", "lab_repro_hash",
    ],
    "CLOUD_DEVOPS": [
        "lab_linux_perms", "lab_git_state", "lab_dockerfile_lint", "lab_cicd_gate", "lab_cloud_cost",
        "lab_iam_secrets", "lab_slo_budget", "lab_deploy_rollback_cloud", "lab_k8s_probes", "lab_incident_runbook",
    ],
}

LAB_SPECS_003 = {
    lid: {
        "title": lid.replace("lab_", "").replace("_", " "),
        "readme": f"Runnable validator for {lid}. Empty/wrong/print-PASS fail.",
        "required_keys": [],
        "wrong_hint": "Wrong numeric or policy fields must fail.",
    }
    for lid in LABS_003
}

REFERENCE_003: dict[str, dict[str, Any]] = {
    "lab_data_split": {"n": 480, "holdout": 0.20, "train_n": 384, "val_n": 96, "shuffle": False},
    "lab_supervised_metrics": {"tp": 40, "fp": 10, "fn": 5, "precision": 0.8, "recall": 40 / 45, "f1": 2 * 0.8 * (40 / 45) / (0.8 + 40 / 45)},
    "lab_cluster_assign": {
        "point": [55, 2000, 2], "centroid_a": [40, 3000, 0], "centroid_b": [70, 1200, 5],
        "assignment": "B", "dist_a": 1017, "dist_b": 818,
    },
    "lab_eval_thresholds": {"tp": 6, "fp": 2, "fn": 2, "tn": 10, "tpr": 0.75, "fpr": 2 / 12, "fpr_cap_ok": True},
    "lab_overfit_gap": {"train_acc": 0.99, "val_acc": 0.61, "gap": 0.38, "mitigation_note": "fewer features + time-ordered CV"},
    "lab_feature_windows": {"series": [10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17], "window": 5, "index": 4, "mean": 11.6, "uses_future": False},
    "lab_tiny_mlp_forward": {"x": [0.5, 0.2], "y_hat": 0.0},  # filled below
    "lab_score_model": {"scores": [0.62, 0.40, 0.81], "threshold": 0.55, "labels": [1, 0, 1], "model_digest": "sha256:ef2803aa", "digest_ok": True},
    "lab_quantize_budget": {"params": 1000, "fp32_bytes": 4000, "int8_bytes": 1000, "ratio": 0.25, "latency_ms": 12, "sla_ms": 15, "budget_ok": True, "physical_status": "PHYSICAL_PENDING"},
    "lab_rag_redact": {"hits": ["R12", "R19"], "redactions": 2, "biometric_claim": False},
    "lab_clean_nulls": {"rows": 200, "nulls": 10, "null_rate": 0.05, "negatives_dropped": True},
    "lab_sql_join_counts": {"tickets": 100, "zones": 5, "matched": 95, "joined_rows": 95, "cartesian_trap_rows": 500},
    "lab_schema_nf": {"tables": [
        {"name": "tickets", "columns": ["ticket_id", "zone_id", "wait_min"]},
        {"name": "zone_dim", "columns": ["zone_id", "zone_address", "label"]},
    ]},
    "lab_stats_summary": {"values": [8, 8, 10, 12, 12, 12, 14, 18, 18, 120], "mean": 0, "median": 0, "iqr": 0},
    "lab_chart_encode": {"mark": "bar", "x": "zone", "y": "median_wait", "invalid_rejected": True},
    "lab_dashboard_layout": {"tiles": ["median_by_zone", "open_count", "freshness"], "max_tiles": 3},
    "lab_bi_refresh": {"refresh_minutes": 10, "sla_minutes": 15, "meets_sla": True, "license_ok": True},
    "lab_pandas_group": {"medians": {"A": 10, "B": 14, "C": 12}, "input_sha256": "sha256:" + "a" * 16},
    "lab_kpi_tree": {"open_count": 6, "median_wait": 12, "staff_on_duty": 3, "desk_pressure": 24},
    "lab_repro_hash": {"null_rate": 0.04, "negatives_dropped": True, "freshness_minutes": 8, "csv_sha256": "sha256:" + "b" * 16, "quality_ok": True},
    "lab_linux_perms": {"mode_octal": 0o600, "mode_str": "0600", "world_writable": False},
    "lab_git_state": {"ahead": 2, "behind": 0, "conflict_files": ["services/api/health.py"], "force_push_main": False},
    "lab_dockerfile_lint": {"pinned_digest": True, "user_non_root": True, "uses_latest": False, "lint_ok": True},
    "lab_cicd_gate": {"on": ["pull_request"], "jobs": ["lint", "test", "upload-report"], "deploy_on_pr": False},
    "lab_cloud_cost": {"vcpu_hours": 16, "storage_gb": 50, "cost_units": 16.5, "must_be_private": True},
    "lab_iam_secrets": {"allowed": ["ecr:Upload", "ecs:UpdateService"], "denied": ["iam:CreateUser"], "plaintext_secrets_found": False, "vault_path": "vault/fc/deploy"},
    "lab_slo_budget": {"failed": 40, "total": 10000, "availability": 0.996, "failure_cap": 50, "budget_ok": True},
    "lab_deploy_rollback_cloud": {"current": "sha256:fc4822aa", "rollback_to": "sha256:fc4810bb", "migrate": "ok", "health": "healthy"},
    "lab_k8s_probes": {"readiness": "/readyz", "liveness": "/healthz", "replicas": 2, "requests_cpu": "100m", "probe_ok": True},
    "lab_incident_runbook": {"heroics": False, "automation_runbook_id": "RB-FC-rollback", "token_rotated": True, "timeline": {"detect": "10:01", "contain": "10:08", "recover": "10:20"}},
}


def _fix_dynamic_refs() -> None:
    # MLP
    W1 = [[0.5, -0.2], [0.1, 0.4]]
    b1 = [0.0, 0.1]
    W2 = [0.7, -0.3]
    b2 = 0.2
    x = [0.5, 0.2]
    h = [max(0.0, W1[i][0] * x[0] + W1[i][1] * x[1] + b1[i]) for i in range(2)]
    z2 = W2[0] * h[0] + W2[1] * h[1] + b2
    REFERENCE_003["lab_tiny_mlp_forward"]["y_hat"] = 1.0 / (1.0 + math.exp(-z2))
    # stats
    vals = sorted(float(v) for v in REFERENCE_003["lab_stats_summary"]["values"])
    n = len(vals)
    mean = sum(vals) / n
    mid = n // 2
    median = vals[mid] if n % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    q1 = vals[n // 4]
    q3 = vals[(3 * n) // 4]
    REFERENCE_003["lab_stats_summary"].update({"mean": mean, "median": median, "iqr": q3 - q1})


_fix_dynamic_refs()

WRONG_003 = {
    "lab_data_split": {"n": 480, "holdout": 0.2, "train_n": 100, "val_n": 100, "shuffle": True},
    "lab_supervised_metrics": {"tp": 40, "fp": 10, "fn": 5, "precision": 0.1, "recall": 0.1, "f1": 0.1},
    "lab_cluster_assign": {"point": [55, 2000, 2], "centroid_a": [40, 3000, 0], "centroid_b": [70, 1200, 5], "assignment": "A", "dist_a": 1, "dist_b": 1},
    "lab_eval_thresholds": {"tp": 6, "fp": 2, "fn": 2, "tn": 10, "tpr": 1.0, "fpr": 1.0, "fpr_cap_ok": True},
    "lab_overfit_gap": {"train_acc": 0.99, "val_acc": 0.61, "gap": 0.01, "mitigation_note": ""},
    "lab_feature_windows": {"series": [10, 12, 11, 13, 12], "window": 5, "index": 4, "mean": 0, "uses_future": True},
    "lab_tiny_mlp_forward": {"x": [0.5, 0.2], "y_hat": 0.0},
    "lab_score_model": {"scores": [0.62, 0.40, 0.81], "threshold": 0.55, "labels": [0, 0, 0], "model_digest": "sha256:dead", "digest_ok": True},
    "lab_quantize_budget": {"params": 1000, "fp32_bytes": 1000, "int8_bytes": 4000, "ratio": 1, "latency_ms": 30, "sla_ms": 15, "budget_ok": True, "physical_status": "DONE"},
    "lab_rag_redact": {"hits": ["X"], "redactions": 0, "biometric_claim": True},
    "lab_clean_nulls": {"rows": 200, "nulls": 10, "null_rate": 0.5, "negatives_dropped": False},
    "lab_sql_join_counts": {"tickets": 100, "zones": 5, "matched": 95, "joined_rows": 500, "cartesian_trap_rows": 95},
    "lab_schema_nf": {"tables": [{"name": "tickets", "columns": ["ticket_id", "zone_address"]}]},
    "lab_stats_summary": {"values": [1, 2, 3], "mean": 0, "median": 0, "iqr": 0},
    "lab_chart_encode": {"mark": "pie", "x": "ticket_id", "y": "id", "invalid_rejected": False},
    "lab_dashboard_layout": {"tiles": ["stock_photo"], "max_tiles": 12},
    "lab_bi_refresh": {"refresh_minutes": 30, "sla_minutes": 15, "meets_sla": True, "license_ok": False},
    "lab_pandas_group": {"medians": {"A": 1}, "input_sha256": "x"},
    "lab_kpi_tree": {"open_count": 6, "median_wait": 12, "staff_on_duty": 3, "desk_pressure": 1},
    "lab_repro_hash": {"null_rate": 0.2, "negatives_dropped": False, "freshness_minutes": 40, "csv_sha256": "x", "quality_ok": True},
    "lab_linux_perms": {"mode_octal": 0o666, "mode_str": "0666", "world_writable": True},
    "lab_git_state": {"ahead": 0, "behind": 5, "conflict_files": [], "force_push_main": True},
    "lab_dockerfile_lint": {"pinned_digest": False, "user_non_root": False, "uses_latest": True, "lint_ok": True},
    "lab_cicd_gate": {"on": ["push"], "jobs": ["deploy"], "deploy_on_pr": True},
    "lab_cloud_cost": {"vcpu_hours": 16, "storage_gb": 50, "cost_units": 1, "must_be_private": False},
    "lab_iam_secrets": {"allowed": ["*"], "denied": [], "plaintext_secrets_found": True, "vault_path": ""},
    "lab_slo_budget": {"failed": 40, "total": 10000, "availability": 0.5, "failure_cap": 50, "budget_ok": False},
    "lab_deploy_rollback_cloud": {"current": "sha256:aaa", "rollback_to": "sha256:aaa", "migrate": "skipped", "health": "starting"},
    "lab_k8s_probes": {"readiness": "/admin", "liveness": "/root", "replicas": 20, "requests_cpu": "0", "probe_ok": True},
    "lab_incident_runbook": {"heroics": True, "automation_runbook_id": "", "token_rotated": False, "timeline": {}},
}
