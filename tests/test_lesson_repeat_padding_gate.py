"""Verbatim repeated sentences are depth padding, not lesson depth."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402
from waike_course_ready.provenance import (  # noqa: E402
    dedupe_lesson_sentences,
    repeated_lesson_sentences,
)

_spec = importlib.util.spec_from_file_location("write_course_digital_rc", ROOT / "scripts" / "write_course_digital_rc.py")
writer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(writer)

DUP = "Journal EP-4101: restate the worked numbers and keep prose specific to this lab."


def test_repeated_sentence_detected_and_removed():
    text = f"Real content about the memory map. {DUP} {DUP}"
    assert repeated_lesson_sentences(text) == [DUP.lower()]
    assert dedupe_lesson_sentences(text).count("Journal EP-4101") == 1


def test_short_repeats_are_not_flagged():
    assert repeated_lesson_sentences("Empty {} fails. Empty {} fails.") == []


def test_writer_rejects_duplicate_padding(monkeypatch):
    body = ("Distinct week content sentence number one explains the bus timing in detail. " * 1)
    padded = body + " ".join([DUP] * 20)
    monkeypatch.setitem(writer.COURSES, "PAD_PROBE", {"weeks": [{"week": 1, "lesson": padded}]})
    ok, reasons = writer._lesson_depth_ok("PAD_PROBE")
    assert ok is False
    assert any("repeated-sentence depth padding" in r for r in reasons)
    assert any("< 800" in r for r in reasons)


def test_batch007_lessons_have_no_verbatim_repeats():
    for cid in ("EMBEDDED_PROTOTYPING", "GUNNCHOS_PRODUCT_LAB"):
        for week in COURSES[cid]["weeks"]:
            assert repeated_lesson_sentences(week["lesson"]) == [], f"{cid} week {week['week']}"


def test_course_digital_rc_artifact_matches_gate():
    rc = json.loads((ROOT / "artifacts" / "COURSE_DIGITAL_RC.json").read_text(encoding="utf-8"))
    assert rc["full_18_course_digital_rc"] is False
    for cid, row in rc["courses"].items():
        padded = any(repeated_lesson_sentences(w.get("lesson") or "") for w in COURSES[cid]["weeks"])
        if padded:
            assert row["COURSE_DIGITAL_RC"] is False, f"{cid} passes despite repeated-sentence padding"
