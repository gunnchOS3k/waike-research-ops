from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.ingest import build_learner, build_product_catalog, build_teacher
from waike_course_ready.labs import _fail_if_print_pass, run_all, run_lab
from waike_course_ready.packaging import SYLLABUS_ASSESSMENT, rubrics
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
    assert bundle["ok"] is True, {k: bundle.get(k) for k in (
        "empty_submission_fails", "wrong_submission_fails", "print_pass_raises",
        "ttl1_from_parsed_header", "no_submission_fails", "negatives_must_fail_and_did",
    )}
    assert bundle["lab_count"] == 20
    assert all(n["ok"] for n in bundle["negatives_must_fail_and_did"])
    assert bundle["empty_submission_fails"] is True
    assert bundle["wrong_submission_fails"] is True
    assert bundle["print_pass_raises"] is True
    assert bundle["ttl1_from_parsed_header"] is True
    assert bundle["no_submission_fails"] is True


def test_empty_and_print_pass_fail():
    empty = run_lab("lab_os_users", submission={})
    assert empty["ok"] is False
    raised = False
    try:
        _fail_if_print_pass("PASS")
    except AssertionError:
        raised = True
    assert raised
    raised2 = False
    try:
        run_lab("lab_siem_triage", submission="PASS")
    except AssertionError:
        raised2 = True
    assert raised2


def test_mid_final_not_weekly_clones():
    for cid in COURSES:
        weekly = {i["stem"] for w in COURSES[cid]["weeks"] for i in w["quiz"]}
        extras = extra_assessment_items(cid)
        assert len(extras["mid"]) == 20
        assert len(extras["final"]) == 24
        for item in extras["mid"]:
            assert item["stem"] not in weekly, (cid, item["id"])
            assert not item["stem"].startswith("Mid-course check:")
        for item in extras["final"]:
            assert item["stem"] not in weekly, (cid, item["id"])
            assert not item["stem"].startswith("Capstone check:")


def test_answer_keys_not_collapsed():
    for cid in COURSES:
        idxs = [i["answer_index"] for w in COURSES[cid]["weeks"] for i in w["quiz"]]
        extras = extra_assessment_items(cid)
        idxs += [i["answer_index"] for i in extras["mid"] + extras["final"]]
        present = set(idxs)
        assert present == {0, 1, 2, 3}, (cid, present)
        n = len(idxs)
        for letter in range(4):
            share = idxs.count(letter) / n
            assert share <= 0.40, (cid, letter, share)


def test_packaging_not_cloned():
    texts = [json.dumps(rubrics(cid), sort_keys=True) + SYLLABUS_ASSESSMENT[cid] for cid in COURSES]
    assert len(set(texts)) == 3


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
