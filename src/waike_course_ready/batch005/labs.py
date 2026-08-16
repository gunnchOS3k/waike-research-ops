"""Runnable labs for STREAM-B-PKT-002 — COMM_PD_ETHICS full DIGITAL_RC package.

Ten Harbor Desk Voice labs. Empty/wrong/print-PASS fail. COURSE_DIGITAL_RC earned only after full bar.
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
B = (
    "COMM_PD_ETHICS Harbor Desk Voice fixture. Not a student/teacher E6. "
    "Instructor keys stay out of learner modes. COURSE_DIGITAL_RC only when full package bar holds."
)


def lab_consent_disclosure(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_consent_disclosure", COURSE, submission,
        ["audience", "purpose", "data_classes", "retention_days", "opt_out_path", "ai_disclosure"], B,
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
        "lab_conflict_interest", COURSE, submission,
        ["scenario", "conflict_present", "disclose_to", "recuse", "rationale"], B,
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
        "lab_professional_comm", COURSE, submission,
        ["channel", "subject", "body", "demeaning_labels", "promises_outcome"], B,
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
        "lab_ethics_ladder", COURSE, submission,
        ["observation", "inference", "need", "action", "fabricated_impact"], B,
    )
    if data is None:
        return _result("lab_ethics_ladder", COURSE, checks, B)
    checks.append(_check("observation", len(str(data.get("observation") or "")) >= 20, "observation ≥20"))
    checks.append(_check("inference", len(str(data.get("inference") or "")) >= 20, "inference ≥20"))
    checks.append(_check("need", len(str(data.get("need") or "")) >= 12, "need ≥12"))
    checks.append(_check("action", len(str(data.get("action") or "")) >= 12, "action ≥12"))
    checks.append(_check("no_fabricated_impact", data.get("fabricated_impact") is False, "fabricated_impact must be false"))
    return _result("lab_ethics_ladder", COURSE, checks, B)


def lab_attribution_cite(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_attribution_cite", COURSE, submission,
        ["claim", "source_title", "reuse_class", "quote_chars", "paraphrase"], B,
    )
    if data is None:
        return _result("lab_attribution_cite", COURSE, checks, B)
    reuse = str(data.get("reuse_class") or "")
    checks.append(_check("claim", len(str(data.get("claim") or "")) >= 24, "claim ≥24"))
    checks.append(_check("source", len(str(data.get("source_title") or "")) >= 8, "source_title ≥8"))
    checks.append(_check("reuse_class", reuse in ("PUBLIC_REFERENCE_ONLY", "FAIR_USE_PARAPHRASE", "ORIGINAL"), "allowed reuse_class"))
    checks.append(_check("quote_budget", int(data.get("quote_chars") or 9999) <= 120, "quote_chars ≤120"))
    checks.append(_check("paraphrase", len(str(data.get("paraphrase") or "")) >= 40, "paraphrase ≥40"))
    checks.append(_check("no_dump", "verbatim dump" not in str(data.get("paraphrase") or "").lower(), "no verbatim dump"))
    return _result("lab_attribution_cite", COURSE, checks, B)


def lab_feedback_rubric(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_feedback_rubric", COURSE, submission,
        ["criterion", "evidence", "score", "next_action", "identity_attack"], B,
    )
    if data is None:
        return _result("lab_feedback_rubric", COURSE, checks, B)
    score = int(data.get("score") or -1)
    checks.append(_check("criterion", len(str(data.get("criterion") or "")) >= 12, "criterion ≥12"))
    checks.append(_check("evidence", len(str(data.get("evidence") or "")) >= 24, "evidence ≥24"))
    checks.append(_check("score_range", 0 <= score <= 4, "score 0..4"))
    checks.append(_check("next_action", len(str(data.get("next_action") or "")) >= 16, "next_action ≥16"))
    checks.append(_check("no_identity_attack", data.get("identity_attack") is False, "identity_attack must be false"))
    return _result("lab_feedback_rubric", COURSE, checks, B)


def lab_meeting_minutes(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_meeting_minutes", COURSE, submission,
        ["attendees_count", "decisions", "owners", "due_dates", "pii_redacted"], B,
    )
    if data is None:
        return _result("lab_meeting_minutes", COURSE, checks, B)
    decisions = data.get("decisions") or []
    owners = data.get("owners") or []
    dues = data.get("due_dates") or []
    checks.append(_check("attendees", int(data.get("attendees_count") or 0) >= 2, "≥2 attendees"))
    checks.append(_check("decisions", isinstance(decisions, list) and len(decisions) >= 2, "≥2 decisions"))
    checks.append(_check("owners", isinstance(owners, list) and len(owners) >= 2, "≥2 owners"))
    checks.append(_check("dues", isinstance(dues, list) and len(dues) >= 2, "≥2 due_dates"))
    checks.append(_check("aligned_lengths", len(decisions) == len(owners) == len(dues), "parallel arrays"))
    checks.append(_check("pii_redacted", data.get("pii_redacted") is True, "pii_redacted true"))
    return _result("lab_meeting_minutes", COURSE, checks, B)


def lab_ai_disclosure_modes(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_ai_disclosure_modes", COURSE, submission,
        ["mode", "disclosed", "used_instructor_keys", "learner_facing", "rationale"], B,
    )
    if data is None:
        return _result("lab_ai_disclosure_modes", COURSE, checks, B)
    mode = str(data.get("mode") or "")
    checks.append(_check("mode", mode in ("AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"), "valid mode"))
    checks.append(_check("disclosed", data.get("disclosed") is True, "disclosed true"))
    checks.append(_check("no_keys", data.get("used_instructor_keys") is False, "learner modes never use instructor keys"))
    checks.append(_check("learner_facing", data.get("learner_facing") is True, "learner_facing true"))
    checks.append(_check("rationale", len(str(data.get("rationale") or "")) >= 24, "rationale ≥24"))
    if mode == "NO_AI":
        checks.append(_check("no_ai_honest", "no ai" in str(data.get("rationale") or "").lower() or "human-only" in str(data.get("rationale") or "").lower(), "NO_AI rationale"))
    return _result("lab_ai_disclosure_modes", COURSE, checks, B)


def lab_accessibility_comm(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_accessibility_comm", COURSE, submission,
        ["captions", "plain_language", "alt_text", "color_only_signals", "large_print_available"], B,
    )
    if data is None:
        return _result("lab_accessibility_comm", COURSE, checks, B)
    checks.append(_check("captions", data.get("captions") is True, "captions true"))
    checks.append(_check("plain_language", data.get("plain_language") is True, "plain_language true"))
    checks.append(_check("alt_text", len(str(data.get("alt_text") or "")) >= 12, "alt_text ≥12"))
    checks.append(_check("no_color_only", data.get("color_only_signals") is False, "color_only_signals false"))
    checks.append(_check("large_print", data.get("large_print_available") is True, "large_print_available true"))
    return _result("lab_accessibility_comm", COURSE, checks, B)


def lab_pd_capstone(submission: Any = None) -> LabResult:
    data, checks = _require_student(
        "lab_pd_capstone", COURSE, submission,
        ["labs_passed", "consent_ok", "conflict_ok", "a11y_ok", "no_key_leak", "fabricated_impact"], B,
    )
    if data is None:
        return _result("lab_pd_capstone", COURSE, checks, B)
    checks.append(_check("labs_passed", int(data.get("labs_passed") or 0) >= 6, "labs_passed ≥6"))
    checks.append(_check("consent_ok", data.get("consent_ok") is True, "consent_ok"))
    checks.append(_check("conflict_ok", data.get("conflict_ok") is True, "conflict_ok"))
    checks.append(_check("a11y_ok", data.get("a11y_ok") is True, "a11y_ok"))
    checks.append(_check("no_key_leak", data.get("no_key_leak") is True, "no_key_leak"))
    checks.append(_check("no_fabricated", data.get("fabricated_impact") is False, "fabricated_impact false"))
    return _result("lab_pd_capstone", COURSE, checks, B)


LABS_005 = {
    "lab_consent_disclosure": lab_consent_disclosure,
    "lab_conflict_interest": lab_conflict_interest,
    "lab_professional_comm": lab_professional_comm,
    "lab_ethics_ladder": lab_ethics_ladder,
    "lab_attribution_cite": lab_attribution_cite,
    "lab_feedback_rubric": lab_feedback_rubric,
    "lab_meeting_minutes": lab_meeting_minutes,
    "lab_ai_disclosure_modes": lab_ai_disclosure_modes,
    "lab_accessibility_comm": lab_accessibility_comm,
    "lab_pd_capstone": lab_pd_capstone,
}

COURSE_LABS_005 = {
    COURSE: list(LABS_005.keys()),
}

LAB_SPECS_005 = {
    "lab_consent_disclosure": {
        "title": "consent disclosure",
        "readme": "Harbor Desk Voice consent card for ticket PD-2101. Students submit audience, purpose, data_classes (\u22652, no ssn), retention_days > 0, opt_out_path, and ai_disclosure=true. Vague audience='everyone' fails. This is operational consent, not a wall poster.",
        "required_keys": [],
        "wrong_hint": "SSN classes, retention_days=0, blank opt-out, or ai_disclosure false must fail.",
        "course_id": COURSE,
    },
    "lab_conflict_interest": {
        "title": "conflict of interest",
        "readme": "PD-2204 conflict drill: mentoring plus scoring the same portfolio. Submit scenario (\u226540 chars), conflict_present, disclose_to, recuse, and rationale (\u226524). When conflict_present is true, recuse must be true after disclosure to the course lead.",
        "required_keys": [],
        "wrong_hint": "Short scenarios, empty disclose_to, or recuse=false while conflict_present=true fail.",
        "course_id": COURSE,
    },
    "lab_professional_comm": {
        "title": "professional communication",
        "readme": "PD-2307 professional ticket. Channel must be email|ticket|slack_work. Subject \u22658, body \u226580 with observation and next action. demeaning_labels and promises_outcome must be false. Banned body tokens include stupid/lazy/hopeless/idiot.",
        "required_keys": [],
        "wrong_hint": "SMS channel, demeaning labels, outcome promises, or banned body words fail.",
        "course_id": COURSE,
    },
    "lab_ethics_ladder": {
        "title": "ethics ladder",
        "readme": "PD-2409 observation\u2192inference\u2192need\u2192action ladder (NO_AI authorship week). Each rung has a minimum length. fabricated_impact must be false \u2014 invented citywide harm stats fail.",
        "required_keys": [],
        "wrong_hint": "Short rungs or fabricated_impact=true fail the ladder honesty gate.",
        "course_id": COURSE,
    },
    "lab_attribution_cite": {
        "title": "attribution cite",
        "readme": "PD-2511 citation discipline. reuse_class \u2208 {PUBLIC_REFERENCE_ONLY, FAIR_USE_PARAPHRASE, ORIGINAL}. quote_chars \u2264120. paraphrase \u226540 in WAIKE words. Verbatim dumps fail. Certs stay aligned-not-granted.",
        "required_keys": [],
        "wrong_hint": "FULL_COPY, quote_chars>120, or 'verbatim dump' paraphrase fail.",
        "course_id": COURSE,
    },
    "lab_feedback_rubric": {
        "title": "feedback rubric",
        "readme": "PD-2615 peer feedback: criterion, evidence (\u226524 on journal behavior), score 0..4, next_action \u226516. identity_attack must be false. Educator HITL still required before any grade publish.",
        "required_keys": [],
        "wrong_hint": "Score outside 0..4, identity_attack true, or thin evidence/next_action fail.",
        "course_id": COURSE,
    },
    "lab_meeting_minutes": {
        "title": "meeting minutes",
        "readme": "PD-2718 minutes: attendees_count \u22652; parallel decisions/owners/due_dates arrays (\u22652 each); pii_redacted true. Unequal array lengths fail. Patron PANs must not appear.",
        "required_keys": [],
        "wrong_hint": "Solo attendees, misaligned arrays, or pii_redacted false fail.",
        "course_id": COURSE,
    },
    "lab_ai_disclosure_modes": {
        "title": "AI disclosure modes",
        "readme": "PD-2822 AI mode honesty. mode \u2208 {AI_ALLOWED, AI_RESTRICTED, AI_DISCLOSED, NO_AI}. disclosed=true, used_instructor_keys=false, learner_facing=true. Learner tutors never open the instructor key store. NO_AI rationale must say human-only/no ai.",
        "required_keys": [],
        "wrong_hint": "Key access true, disclosed false, or invalid mode fail.",
        "course_id": COURSE,
    },
    "lab_accessibility_comm": {
        "title": "accessibility communication",
        "readme": "PD-2925 accessible professional communication (NO_AI walkthrough). captions, plain_language, large_print_available true; color_only_signals false; alt_text \u226512. Fabricated disability quotes forbidden.",
        "required_keys": [],
        "wrong_hint": "Missing captions, color-only signals, or tiny alt_text fail.",
        "course_id": COURSE,
    },
    "lab_pd_capstone": {
        "title": "PD capstone",
        "readme": "PD-2A30 ship checklist: labs_passed \u22656; consent_ok, conflict_ok, a11y_ok, no_key_leak true; fabricated_impact false. Portfolio claim boundary stays digital-fixture only; REAL_*_E6 false.",
        "required_keys": [],
        "wrong_hint": "labs_passed<6, any honesty flag false, or fabricated_impact true fail.",
        "course_id": COURSE,
    },
}

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
    "lab_attribution_cite": {
        "claim": "Public ISC2 ethics theme names align to Harbor Desk conflict drills.",
        "source_title": "ISC2 Code of Ethics themes (PUBLIC_REFERENCE_ONLY)",
        "reuse_class": "PUBLIC_REFERENCE_ONLY",
        "quote_chars": 40,
        "paraphrase": "Harbor Desk maps protect-society themes to recusal and disclosure labs without harvesting exam stems.",
    },
    "lab_feedback_rubric": {
        "criterion": "Observation vs inference separation",
        "evidence": "Journal listed idle logout time before guessing 'broken PC'.",
        "score": 3,
        "next_action": "Add one still-need question before action.",
        "identity_attack": False,
    },
    "lab_meeting_minutes": {
        "attendees_count": 4,
        "decisions": ["Pause USB wipe", "Post Friday notice"],
        "owners": ["desk.lead", "volunteer.sat"],
        "due_dates": ["2026-08-18", "2026-08-17"],
        "pii_redacted": True,
    },
    "lab_ai_disclosure_modes": {
        "mode": "AI_DISCLOSED",
        "disclosed": True,
        "used_instructor_keys": False,
        "learner_facing": True,
        "rationale": "Tutor may hint on ladder steps but must not load answer_keys.json.",
    },
    "lab_accessibility_comm": {
        "captions": True,
        "plain_language": True,
        "alt_text": "Desk layout diagram with labeled kiosks 1-4",
        "color_only_signals": False,
        "large_print_available": True,
    },
    "lab_pd_capstone": {
        "labs_passed": 9,
        "consent_ok": True,
        "conflict_ok": True,
        "a11y_ok": True,
        "no_key_leak": True,
        "fabricated_impact": False,
    },
}

WRONG_005 = {
    "lab_consent_disclosure": {
        "audience": "everyone", "purpose": "collect everything", "data_classes": ["ssn", "password"],
        "retention_days": 0, "opt_out_path": "", "ai_disclosure": False,
    },
    "lab_conflict_interest": {
        "scenario": "short", "conflict_present": True, "disclose_to": "", "recuse": False, "rationale": "fine",
    },
    "lab_professional_comm": {
        "channel": "sms", "subject": "hi", "body": "you are stupid and lazy",
        "demeaning_labels": True, "promises_outcome": True,
    },
    "lab_ethics_ladder": {
        "observation": "bad", "inference": "bad", "need": "x", "action": "y", "fabricated_impact": True,
    },
    "lab_attribution_cite": {
        "claim": "x", "source_title": "x", "reuse_class": "FULL_COPY", "quote_chars": 9000,
        "paraphrase": "verbatim dump of the chapter",
    },
    "lab_feedback_rubric": {
        "criterion": "x", "evidence": "x", "score": 9, "next_action": "x", "identity_attack": True,
    },
    "lab_meeting_minutes": {
        "attendees_count": 1, "decisions": ["a"], "owners": [], "due_dates": ["x"], "pii_redacted": False,
    },
    "lab_ai_disclosure_modes": {
        "mode": "NO_AI", "disclosed": False, "used_instructor_keys": True,
        "learner_facing": False, "rationale": "keys ok",
    },
    "lab_accessibility_comm": {
        "captions": False, "plain_language": False, "alt_text": "x",
        "color_only_signals": True, "large_print_available": False,
    },
    "lab_pd_capstone": {
        "labs_passed": 1, "consent_ok": False, "conflict_ok": False,
        "a11y_ok": False, "no_key_leak": False, "fabricated_impact": True,
    },
}
