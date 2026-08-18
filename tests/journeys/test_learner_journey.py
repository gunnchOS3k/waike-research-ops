from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.ingest import build_learner  # noqa: E402
from waike_course_ready.labs import reference_submission, run_lab  # noqa: E402
from waike_ops.pathways import anonymous_completion, build_pathway  # noqa: E402

COURSE_DIR = ROOT / "curriculum" / "digital_rc" / "SOFTWARE_BUILDER"


def test_software_builder_learner_journey():
    """Anonymous learner: start packet → week 1 lesson → lab (empty fails, reference passes)."""
    pathway = build_pathway(COURSE_DIR)
    assert pathway["course_id"] == "SOFTWARE_BUILDER"
    start = COURSE_DIR / pathway["start"]["student_packet_ref"]
    lesson = COURSE_DIR / pathway["lessons"][0]["body_ref"]
    assert "Empty submissions fail" in start.read_text(encoding="utf-8")
    assert lesson.is_file()
    assert pathway["labs"][0] == "lab_git_conflict"

    empty = run_lab("lab_git_conflict", submission={})
    assert empty["ok"] is False

    ok = run_lab("lab_git_conflict", submission=reference_submission("lab_git_conflict"))
    assert ok["ok"] is True

    learner = json.dumps(build_learner())
    assert "answer_keys" not in learner
    assert "answer_index" not in learner

    record = anonymous_completion(
        "SOFTWARE_BUILDER",
        1,
        "lab_git_conflict",
        lab_id="lab_git_conflict",
        lab_ok=True,
        opaque_learner_ref="fixture-learner",
    )
    dumped = json.dumps(record)
    assert "@" not in dumped
    assert "grade" not in record
    assert "transcript" not in record
