"""Runnable labs for batch008 — SEVEN_GC_APPRENTICESHIP."""
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

B_SGC = (
    "SEVEN_GC_APPRENTICESHIP Gary 7GC Research Desk. Digital curriculum only. "
    "EXTERNAL_HUMAN/PHYSICAL/FIELD gates remain open. Not student/teacher E6. "
    "Commercial standardized 6G does not exist today."
)

def lab_sgc_evidence_class(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_evidence_class", "SEVEN_GC_APPRENTICESHIP", submission,
        ["classes", "pii_in_notes", "mentor_signed", "commercial_6g_exists"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_evidence_class", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("classes_len", isinstance(data.get("classes"), list) and len(data["classes"]) >= 5, "classes"))
    checks.append(_check("pii", data.get("pii_in_notes") is False, "pii"))
    checks.append(_check("mentor", data.get("mentor_signed") is False, "mentor"))
    checks.append(_check("c6g", data.get("commercial_6g_exists") is False, "c6g"))
    return _result("lab_sgc_evidence_class", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_repo_recon(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_repo_recon", "SEVEN_GC_APPRENTICESHIP", submission,
        ["repo_id", "purpose", "has_tests", "evidence_path", "limitations", "mutated_prod"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_repo_recon", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("repo", bool(str(data.get("repo_id") or "").strip()), "repo"))
    checks.append(_check("tests", data.get("has_tests") is True, "tests"))
    checks.append(_check("evidence", bool(str(data.get("evidence_path") or "").strip()), "evidence"))
    checks.append(_check("prod", data.get("mutated_prod") is False, "prod"))
    return _result("lab_sgc_repo_recon", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_baseline_repro(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_baseline_repro", "SEVEN_GC_APPRENTICESHIP", submission,
        ["fixture", "evidence_class", "output_sha256", "seed", "command"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_baseline_repro", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))
    sha = str(data.get("output_sha256") or "")
    checks.append(_check("sha", len(sha) == 64 and all(c in "0123456789abcdef" for c in sha.lower()), "sha"))
    checks.append(_check("seed", data.get("seed") is not None, "seed"))
    checks.append(_check("fixture", "sgc_baseline" in str(data.get("fixture") or ""), "fixture"))
    return _result("lab_sgc_baseline_repro", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_experiment_design(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_experiment_design", "SEVEN_GC_APPRENTICESHIP", submission,
        ["question", "hypothesis", "iv", "dv", "control", "confound", "claim_match", "evidence_plan"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_experiment_design", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("iv", bool(str(data.get("iv") or "").strip()), "iv"))
    checks.append(_check("dv", bool(str(data.get("dv") or "").strip()), "dv"))
    checks.append(_check("match", data.get("claim_match") is True, "match"))
    plan = str(data.get("evidence_plan") or "").lower()
    checks.append(_check("plan", "simulat" in plan or "digital" in plan, "plan"))
    return _result("lab_sgc_experiment_design", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_controlled_sim(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_controlled_sim", "SEVEN_GC_APPRENTICESHIP", submission,
        ["baseline_mcs", "trial_mcs", "snr_db", "evidence_class", "raw_preserved", "human_gate"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_controlled_sim", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))
    checks.append(_check("raw", data.get("raw_preserved") is True, "raw"))
    checks.append(_check("gate", data.get("human_gate") is True, "gate"))
    checks.append(_check("iv_changed", data.get("baseline_mcs") != data.get("trial_mcs"), "iv"))
    return _result("lab_sgc_controlled_sim", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_analysis(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_analysis", "SEVEN_GC_APPRENTICESHIP", submission,
        ["vendor_claim", "fixture_supports", "commercial_6g_exists", "docs_cited", "delta_noted"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_analysis", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("c6g", data.get("commercial_6g_exists") is False, "c6g"))
    checks.append(_check("support", data.get("fixture_supports") is False, "support"))
    checks.append(_check("docs", data.get("docs_cited") is True, "docs"))
    checks.append(_check("delta", data.get("delta_noted") is True, "delta"))
    return _result("lab_sgc_analysis", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_claim_audit(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_claim_audit", "SEVEN_GC_APPRENTICESHIP", submission,
        ["supports", "does_not_support", "human_gate", "physical_gate", "field_gate"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_claim_audit", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    supports = data.get("supports") or []
    dns = data.get("does_not_support") or []
    checks.append(_check("supports", isinstance(supports, list) and len(supports) >= 1, "supports"))
    blob = " ".join(str(x).lower() for x in dns)
    checks.append(_check("dns", "mentor" in blob or "field" in blob, "dns"))
    checks.append(_check("human", data.get("human_gate") == "EXTERNAL_HUMAN_GATE", "human"))
    checks.append(_check("physical", data.get("physical_gate") == "EXTERNAL_PHYSICAL_GATE", "physical"))
    return _result("lab_sgc_claim_audit", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_capstone_package(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_capstone_package", "SEVEN_GC_APPRENTICESHIP", submission,
        ["labs_passed", "mentor_signed", "evidence_class", "includes_limitations", "includes_readme", "product_use_unmerged_consumed"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_capstone_package", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("labs", int(data.get("labs_passed") or 0) >= 6, "labs"))
    checks.append(_check("mentor", data.get("mentor_signed") is False, "mentor"))
    checks.append(_check("limits", data.get("includes_limitations") is True, "limits"))
    checks.append(_check("unmerged", data.get("product_use_unmerged_consumed") is False, "unmerged"))
    return _result("lab_sgc_capstone_package", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_repro_handoff(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_repro_handoff", "SEVEN_GC_APPRENTICESHIP", submission,
        ["independent_repro", "map_rows", "unavailable_ok", "mutated_prod", "digest_match"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_repro_handoff", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    checks.append(_check("repro", data.get("independent_repro") is True, "repro"))
    checks.append(_check("rows", int(data.get("map_rows") or 0) >= 3, "rows"))
    checks.append(_check("prod", data.get("mutated_prod") is False, "prod"))
    checks.append(_check("digest", data.get("digest_match") is True, "digest"))
    return _result("lab_sgc_repro_handoff", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


def lab_sgc_robustness(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_sgc_robustness", "SEVEN_GC_APPRENTICESHIP", submission,
        ["snr_db_variants", "field_gain_invented", "evidence_class", "documented_sensitivity"], B_SGC,
    )
    if data is None:
        return _result("lab_sgc_robustness", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)
    variants = data.get("snr_db_variants") or []
    checks.append(_check("variants", isinstance(variants, list) and len(variants) >= 3, "variants"))
    checks.append(_check("field", data.get("field_gain_invented") is False, "field"))
    checks.append(_check("class", data.get("evidence_class") == "SIMULATED", "class"))
    checks.append(_check("doc", data.get("documented_sensitivity") is True, "doc"))
    return _result("lab_sgc_robustness", "SEVEN_GC_APPRENTICESHIP", checks, B_SGC)


LABS_008 = {
    "lab_sgc_evidence_class": lab_sgc_evidence_class,
    "lab_sgc_repo_recon": lab_sgc_repo_recon,
    "lab_sgc_baseline_repro": lab_sgc_baseline_repro,
    "lab_sgc_experiment_design": lab_sgc_experiment_design,
    "lab_sgc_controlled_sim": lab_sgc_controlled_sim,
    "lab_sgc_analysis": lab_sgc_analysis,
    "lab_sgc_claim_audit": lab_sgc_claim_audit,
    "lab_sgc_capstone_package": lab_sgc_capstone_package,
    "lab_sgc_repro_handoff": lab_sgc_repro_handoff,
    "lab_sgc_robustness": lab_sgc_robustness
}

COURSE_LABS_008 = {
    "SEVEN_GC_APPRENTICESHIP": ["lab_sgc_evidence_class", "lab_sgc_repo_recon", "lab_sgc_baseline_repro", "lab_sgc_experiment_design", "lab_sgc_controlled_sim", "lab_sgc_analysis", "lab_sgc_claim_audit", "lab_sgc_capstone_package", "lab_sgc_repro_handoff", "lab_sgc_robustness"],
}

LAB_SPECS_008 = {
    "lab_sgc_evidence_class": {
        "title": "evidence classification",
        "readme": "Classify evidence snippets; pii_in_notes must be false.",
        "required_keys": [
            "classes",
            "pii_in_notes",
            "mentor_signed",
            "commercial_6g_exists"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    },
    "lab_sgc_repo_recon": {
        "title": "repository reconnaissance",
        "readme": "Map purpose/setup/tests/evidence; UNAVAILABLE siblings allowed.",
        "required_keys": [
            "repo_id",
            "purpose",
            "has_tests",
            "evidence_path",
            "limitations",
            "mutated_prod"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "REPO_CONNECTED",
        "evidence_class": "DIGITAL_REPRODUCTION"
    },
    "lab_sgc_baseline_repro": {
        "title": "baseline reproduction",
        "readme": "Reproduce SIMULATED KPI baseline; capture sha256.",
        "required_keys": [
            "fixture",
            "evidence_class",
            "output_sha256",
            "seed",
            "command"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    },
    "lab_sgc_experiment_design": {
        "title": "experiment design",
        "readme": "Design before run; IV/DV/controls/claim_match.",
        "required_keys": [
            "question",
            "hypothesis",
            "iv",
            "dv",
            "control",
            "confound",
            "claim_match",
            "evidence_plan"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "DIGITAL_REPRODUCTION"
    },
    "lab_sgc_controlled_sim": {
        "title": "controlled simulated experiment",
        "readme": "One IV change; preserve raw; SIMULATED class.",
        "required_keys": [
            "baseline_mcs",
            "trial_mcs",
            "snr_db",
            "evidence_class",
            "raw_preserved",
            "human_gate"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    },
    "lab_sgc_analysis": {
        "title": "analysis vs vendor claims",
        "readme": "Compare vendor slogan to fixture; commercial_6g_exists false.",
        "required_keys": [
            "vendor_claim",
            "fixture_supports",
            "commercial_6g_exists",
            "docs_cited",
            "delta_noted"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    },
    "lab_sgc_claim_audit": {
        "title": "claim audit",
        "readme": "List supports vs does_not_support; external human gate.",
        "required_keys": [
            "supports",
            "does_not_support",
            "human_gate",
            "physical_gate",
            "field_gate"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "DIGITAL_REPRODUCTION"
    },
    "lab_sgc_capstone_package": {
        "title": "capstone package",
        "readme": "Digital capstone; mentor_signed false; limitations required.",
        "required_keys": [
            "labs_passed",
            "mentor_signed",
            "evidence_class",
            "includes_limitations",
            "includes_readme",
            "product_use_unmerged_consumed"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    },
    "lab_sgc_repro_handoff": {
        "title": "reproducibility handoff",
        "readme": "Independent repro + cross-repo map honesty.",
        "required_keys": [
            "independent_repro",
            "map_rows",
            "unavailable_ok",
            "mutated_prod",
            "digest_match"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "REPO_CONNECTED",
        "evidence_class": "DIGITAL_REPRODUCTION"
    },
    "lab_sgc_robustness": {
        "title": "robustness / sensitivity",
        "readme": "SNR sweep on SIMULATED table; no invented field gains.",
        "required_keys": [
            "snr_db_variants",
            "field_gain_invented",
            "evidence_class",
            "documented_sensitivity"
        ],
        "wrong_hint": "Wrong/empty/print-PASS / fabricated field-mentor claims fail.",
        "course_id": "SEVEN_GC_APPRENTICESHIP",
        "execution_mode": "LOCAL_SOFTWARE",
        "evidence_class": "SIMULATED"
    }
}

REFERENCE_008 = {
    "lab_sgc_evidence_class": {
        "classes": [
            "SIMULATED",
            "DIGITAL_REPRODUCTION",
            "MEASURED_HARDWARE",
            "MEASURED_FIELD",
            "HUMAN_REVIEW"
        ],
        "pii_in_notes": False,
        "mentor_signed": False,
        "commercial_6g_exists": False
    },
    "lab_sgc_repo_recon": {
        "repo_id": "waike-research-ops",
        "purpose": "reproducible_research_map",
        "has_tests": True,
        "evidence_path": "results/",
        "limitations": "sibling_repos_may_be_unavailable",
        "mutated_prod": False
    },
    "lab_sgc_baseline_repro": {
        "fixture": "fixtures/sgc_baseline/kpi_window.json",
        "evidence_class": "SIMULATED",
        "output_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "seed": 7,
        "command": "python3 -c \"import json,hashlib,pathlib; p=pathlib.Path('fixtures/sgc_baseline/kpi_window.json'); print(hashlib.sha256(p.read_bytes()).hexdigest())\""
    },
    "lab_sgc_experiment_design": {
        "question": "How does MCS index change BLER at fixed SNR on the SIMULATED table?",
        "hypothesis": "Higher MCS increases BLER at SNR=8 dB on the fixture.",
        "iv": "mcs_index",
        "dv": "bler",
        "control": "snr_db",
        "confound": "seed_leak",
        "claim_match": True,
        "evidence_plan": "SIMULATED table only; no field claim"
    },
    "lab_sgc_controlled_sim": {
        "baseline_mcs": 2,
        "trial_mcs": 3,
        "snr_db": 8,
        "evidence_class": "SIMULATED",
        "raw_preserved": True,
        "human_gate": True
    },
    "lab_sgc_analysis": {
        "vendor_claim": "6G ready",
        "fixture_supports": False,
        "commercial_6g_exists": False,
        "docs_cited": True,
        "delta_noted": True
    },
    "lab_sgc_claim_audit": {
        "supports": [
            "local_sim_delta"
        ],
        "does_not_support": [
            "field_bler",
            "mentor_signoff"
        ],
        "human_gate": "EXTERNAL_HUMAN_GATE",
        "physical_gate": "EXTERNAL_PHYSICAL_GATE",
        "field_gate": "EXTERNAL_FIELD_GATE"
    },
    "lab_sgc_capstone_package": {
        "labs_passed": 6,
        "mentor_signed": False,
        "evidence_class": "SIMULATED",
        "includes_limitations": True,
        "includes_readme": True,
        "product_use_unmerged_consumed": False
    },
    "lab_sgc_repro_handoff": {
        "independent_repro": True,
        "map_rows": 3,
        "unavailable_ok": True,
        "mutated_prod": False,
        "digest_match": True
    },
    "lab_sgc_robustness": {
        "snr_db_variants": [
            6,
            8,
            10
        ],
        "field_gain_invented": False,
        "evidence_class": "SIMULATED",
        "documented_sensitivity": True
    }
}

WRONG_008 = {
    "lab_sgc_evidence_class": {
        "pii_in_notes": True,
        "mentor_signed": True,
        "commercial_6g_exists": True
    },
    "lab_sgc_repo_recon": {
        "mutated_prod": True,
        "has_tests": False,
        "repo_id": ""
    },
    "lab_sgc_baseline_repro": {
        "evidence_class": "MEASURED_FIELD",
        "output_sha256": "short",
        "seed": None
    },
    "lab_sgc_experiment_design": {
        "claim_match": False,
        "iv": "",
        "dv": ""
    },
    "lab_sgc_controlled_sim": {
        "evidence_class": "MEASURED_FIELD",
        "raw_preserved": False,
        "human_gate": False
    },
    "lab_sgc_analysis": {
        "commercial_6g_exists": True,
        "fixture_supports": True,
        "docs_cited": False
    },
    "lab_sgc_claim_audit": {
        "supports": [
            "field_bler"
        ],
        "does_not_support": [],
        "human_gate": "COMPLETE",
        "physical_gate": "COMPLETE",
        "field_gate": "COMPLETE"
    },
    "lab_sgc_capstone_package": {
        "labs_passed": 1,
        "mentor_signed": True,
        "includes_limitations": False,
        "product_use_unmerged_consumed": True
    },
    "lab_sgc_repro_handoff": {
        "independent_repro": False,
        "map_rows": 0,
        "mutated_prod": True,
        "digest_match": False
    },
    "lab_sgc_robustness": {
        "field_gain_invented": True,
        "snr_db_variants": [],
        "evidence_class": "MEASURED_FIELD"
    }
}
