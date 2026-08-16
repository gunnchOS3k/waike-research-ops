"""Runnable labs for STREAM-B-PKT-001 — begin lifting COMM_PD_ETHICS toward DIGITAL_RC.

Executable labs only. COURSE_DIGITAL_RC stays false until full package bar earned.
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


COURSE = "COMM_PD_ETHICS"
B = "COMM_PD_ETHICS fixture only. Not a student/teacher E6. Not COURSE_DIGITAL_RC until full package bar."


def lab_consent_disclosure(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_consent_disclosure",
        COURSE,
        submission,
        ["audience", "purpose", "data_classes", "retention_days", "opt_out_path", "ai_disclosure"],
        B,
    )
    if data is None:
        return _result("lab_consent_disclosure", COURSE, checks, B)
    classes = data.get("data_classes") or []
    checks.append(_check("audience_named", bool(str(data.get("audience") or "").strip()), "audience required"))
    checks.append(_check("purpose_named", bool(str(data.get("purpose") or "").strip()), "purpose required"))
    checks.append(_check("data_classes_list", isinstance(classes, list) and len(classes) >= 2, "≥2 data classes"))
    checks.append(_check("no_ssn_class", "ssn" not in [str(c).lower() for c in classes], "ssn forbidden in desk notes"))
    checks.append(_check("retention_positive", int(data.get("retention_days") or 0) > 0, "retention_days > 0"))
    checks.append(_check("opt_out", bool(str(data.get("opt_out_path") or "").strip()), "opt_out_path required"))
    checks.append(_check("ai_disclosed", data.get("ai_disclosure") is True, "ai_disclosure must be true"))
    return _result("lab_consent_disclosure", COURSE, checks, B)


def lab_conflict_interest(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_conflict_interest",
        COURSE,
        submission,
        ["scenario", "conflict_present", "disclose_to", "recuse", "rationale"],
        B,
    )
    if data is None:
        return _result("lab_conflict_interest", COURSE, checks, B)
    conflict = bool(data.get("conflict_present"))
    checks.append(_check("scenario", len(str(data.get("scenario") or "")) >= 40, "scenario ≥40 chars"))
    checks.append(_check("disclose_named", bool(str(data.get("disclose_to") or "").strip()), "disclose_to required"))
    if conflict:
        checks.append(_check("recuse_when_conflict", data.get("recuse") is True, "must recuse when conflict_present"))
    else:
        checks.append(_check("honest_no_conflict", data.get("recuse") in (False, True), "recuse boolean"))
    checks.append(_check("rationale", len(str(data.get("rationale") or "")) >= 24, "rationale ≥24 chars"))
    return _result("lab_conflict_interest", COURSE, checks, B)


def lab_professional_comm(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_professional_comm",
        COURSE,
        submission,
        ["channel", "subject", "body", "demeaning_labels", "promises_outcome"],
        B,
    )
    if data is None:
        return _result("lab_professional_comm", COURSE, checks, B)
    body = str(data.get("body") or "")
    checks.append(_check("channel", data.get("channel") in ("email", "ticket", "slack_work"), "allowed channel"))
    checks.append(_check("subject", len(str(data.get("subject") or "")) >= 8, "subject ≥8"))
    checks.append(_check("body_depth", len(body) >= 80, "body ≥80"))
    checks.append(_check("no_demeaning", data.get("demeaning_labels") is False, "demeaning_labels must be false"))
    checks.append(_check("no_outcome_promise", data.get("promises_outcome") is False, "no guaranteed outcome"))
    banned = ("stupid", "lazy", "hopeless", "idiot")
    checks.append(_check("body_clean", not any(b in body.lower() for b in banned), "no demeaning words in body"))
    return _result("lab_professional_comm", COURSE, checks, B)


def lab_ethics_ladder(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ethics_ladder",
        COURSE,
        submission,
        ["observation", "inference", "need", "action", "fabricated_impact"],
        B,
    )
    if data is None:
        return _result("lab_ethics_ladder", COURSE, checks, B)
    checks.append(_check("observation", len(str(data.get("observation") or "")) >= 20, "observation ≥20"))
    checks.append(_check("inference", len(str(data.get("inference") or "")) >= 20, "inference ≥20"))
    checks.append(_check("need", len(str(data.get("need") or "")) >= 12, "need ≥12"))
    checks.append(_check("action", len(str(data.get("action") or "")) >= 12, "action ≥12"))
    checks.append(_check("no_fabricated_impact", data.get("fabricated_impact") is False, "fabricated_impact must be false"))
    return _result("lab_ethics_ladder", COURSE, checks, B)


LABS_005 = {
    "lab_consent_disclosure": lab_consent_disclosure,
    "lab_conflict_interest": lab_conflict_interest,
    "lab_professional_comm": lab_professional_comm,
    "lab_ethics_ladder": lab_ethics_ladder,
}

COURSE_LABS_005 = {
    COURSE: [
        "lab_consent_disclosure",
        "lab_conflict_interest",
        "lab_professional_comm",
        "lab_ethics_ladder",
    ],
}

LAB_SPECS_005 = {k: {"course_id": COURSE} for k in LABS_005}

REFERENCE_005 = {
    "lab_consent_disclosure": {
        "audience": "library walk-up patrons and Saturday volunteers",
        "purpose": "explain desk AI tutor logging for ticket coaching",
        "data_classes": ["ticket_id", "device_role", "lesson_progress"],
        "retention_days": 90,
        "opt_out_path": "ask desk lead to disable AI coaching on ticket",
        "ai_disclosure": True,
    },
    "lab_conflict_interest": {
        "scenario": "Volunteer is scoring a classmate's portfolio while also mentoring that classmate on the same assignment.",
        "conflict_present": True,
        "disclose_to": "course lead",
        "recuse": True,
        "rationale": "Scoring power plus private mentoring creates unfair advantage; recuse from grading.",
    },
    "lab_professional_comm": {
        "channel": "ticket",
        "subject": "kiosk idle logout — essay restore path",
        "body": (
            "Observed idle logout at 1200s discarded an unsaved textarea on kiosk 3. "
            "Next action: check auto-save folder, then coach patron on Save As. No reboot."
        ),
        "demeaning_labels": False,
        "promises_outcome": False,
    },
    "lab_ethics_ladder": {
        "observation": "Three patrons reported missing USB files after the Friday close.",
        "inference": "Likely shared-machine cleanup script, not intentional deletion by staff.",
        "need": "Confirm cleanup schedule and whether USB mounts are wiped.",
        "action": "Pull cleanup logs; pause wipe until confirmed; post notice.",
        "fabricated_impact": False,
    },
}

WRONG_005 = {
    "lab_consent_disclosure": {
        "audience": "everyone",
        "purpose": "collect everything",
        "data_classes": ["ssn", "password"],
        "retention_days": 0,
        "opt_out_path": "",
        "ai_disclosure": False,
    },
    "lab_conflict_interest": {
        "scenario": "short",
        "conflict_present": True,
        "disclose_to": "",
        "recuse": False,
        "rationale": "fine",
    },
    "lab_professional_comm": {
        "channel": "sms",
        "subject": "hi",
        "body": "you are stupid and lazy",
        "demeaning_labels": True,
        "promises_outcome": True,
    },
    "lab_ethics_ladder": {
        "observation": "bad",
        "inference": "bad",
        "need": "x",
        "action": "y",
        "fabricated_impact": True,
    },
}
