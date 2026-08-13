from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES
from waike_course_ready.ingest import build_learner, build_product_catalog, build_teacher
from waike_course_ready.labs import run_all
from waike_course_ready.provenance import audit


def test_three_courses_only_in_batch():
    assert set(COURSES) == {"GENERAL_IT", "COMPUTER_NETWORKING", "CYBERSECURITY"}


def test_each_course_has_depth():
    for cid, c in COURSES.items():
        assert len(c["weeks"]) >= 8, cid
        assert all(len(w["lesson"]) >= 800 for w in c["weeks"]), cid
        items = sum(len(w["quiz"]) for w in c["weeks"])
        assert items >= 48, (cid, items)
        assert len({w["lesson"][:120] for w in c["weeks"]}) == len(c["weeks"]), cid


def test_labs_compute_and_negatives_fail():
    bundle = run_all()
    assert bundle["ok"] is True
    assert bundle["lab_count"] >= 12
    assert all(n["ok"] for n in bundle["negatives_must_fail_and_did"])


def test_learner_has_no_keys_teacher_does():
    learner = json.dumps(build_learner())
    teacher = json.dumps(build_teacher())
    assert "answer_index" not in learner
    assert "answer_keys" not in learner
    assert "answer_keys" in teacher
    assert "answer_index" in teacher


def test_product_catalog_ui_fields():
    cat = build_product_catalog()
    assert cat["schema"] == "waike.course_catalog.ui.v1"
    for course in cat["courses"]:
        for field in (
            "course_id",
            "title",
            "kinesthetic_hook",
            "lesson_excerpt",
            "worked_example",
            "assignment",
            "lab_hint",
        ):
            assert course[field]


def test_provenance_pass():
    result = audit()
    assert result["BATCH_TEMPLATED_COURSES"] == 0
    assert result["BATCH_STUB_COURSES"] == 0
    assert result["status"] == "PASS", result["findings"]
