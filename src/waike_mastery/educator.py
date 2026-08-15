"""Educator copilot surfaces — HITL grading, planning, analytics (no auto-publish grades)."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def educator_copilot_session(
    *,
    course_id: str,
    intent: str = "planning",
) -> dict[str, Any]:
    """
    Modes of educator support. Grades suggestions require human-in-the-loop confirmation.
    """
    intents = {
        "planning": {
            "title": "Week plan",
            "actions": [
                "Map kinesthetic hook → lab → quiz for next session",
                "Flag prerequisite edges from skill graph",
                "Prepare isomorphic practice set",
            ],
        },
        "first_time_teacher": {
            "title": "First-time teacher checklist",
            "actions": [
                "Read instructor packet + answer keys offline",
                "Run one lab empty-submission fail demo",
                "Rehearse accessibility board contract",
            ],
        },
        "live_support": {
            "title": "Live classroom support",
            "actions": [
                "Socratic prompts only for learner-visible channel",
                "Do not paste answer keys into learner chat",
                "Escalate safety / integrity issues",
            ],
        },
        "grading_assist": {
            "title": "Grading assist (HITL)",
            "actions": [
                "Propose rubric scores",
                "Require human confirm before publish",
                "Never auto-submit LMS grades",
            ],
            "hitl_required": True,
            "auto_publish_grades": False,
        },
        "feedback": {
            "title": "Feedback drafting",
            "actions": [
                "Skill-focused comments only",
                "No demeaning labels",
                "Point to remediation packet ids",
            ],
        },
        "analytics": {
            "title": "Section analytics",
            "actions": [
                "Aggregate mastery by domain",
                "Surface CURRICULUM_DEFECT_CANDIDATE rates",
                "Keep learner refs opaque",
            ],
        },
    }
    pack = intents.get(intent) or intents["planning"]
    return {
        "schema": "waike.educator_copilot.v1",
        "mode": "EDUCATOR_COPILOT",
        "course_id": course_id,
        "intent": intent if intent in intents else "planning",
        "pack": pack,
        "permissions": {
            "may_read_instructor_keys": True,
            "may_publish_grades_without_human": False,
            "hitl_grading_required": True,
        },
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
