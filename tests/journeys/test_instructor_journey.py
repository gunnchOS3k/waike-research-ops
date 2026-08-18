from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.ingest import build_learner, build_teacher  # noqa: E402
from waike_ops.pathways import build_pathway  # noqa: E402

COURSE_DIR = ROOT / "curriculum" / "digital_rc" / "SOFTWARE_BUILDER"
ONBOARDING = ROOT / "instructor_training" / "instructor_onboarding_path.md"


def test_software_builder_instructor_journey():
    """Instructor: onboarding → packet → keys present → HITL / no publish-without-human."""
    text = ONBOARDING.read_text(encoding="utf-8")
    assert "HITL" in text or "human" in text.lower()
    assert "SOFTWARE_BUILDER" in text
    assert "answer_keys" in text
    assert "PII" in text or "transcript" in text.lower()

    pathway = build_pathway(COURSE_DIR)
    packet = COURSE_DIR / pathway["instructor_guidance"]["instructor_packet_ref"]
    keys = COURSE_DIR / "instructor" / "answer_keys.json"
    assert packet.is_file()
    assert keys.is_file()
    packet_text = packet.read_text(encoding="utf-8")
    assert "answer_keys.json" in packet_text
    assert "not in learner" in packet_text.lower() or "not in learner ingest" in packet_text.lower()

    key_data = json.loads(keys.read_text(encoding="utf-8"))
    assert key_data

    learner = json.dumps(build_learner())
    teacher = json.dumps(build_teacher())
    assert "answer_keys" not in learner
    assert "answer_keys" in teacher
    assert "may_publish_grades_without_human" not in teacher.lower()
