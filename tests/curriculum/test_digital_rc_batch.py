from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES, COURSES_001, extra_assessment_items
from waike_course_ready.batch002.content import COURSES_002
from waike_course_ready.exams import TOKEN_JACCARD_FAIL, nearest_weekly, token_identical
from waike_course_ready.ingest import build_learner, build_product_catalog, build_teacher
from waike_course_ready.labs import _fail_if_print_pass, run_all, run_lab
from waike_course_ready.packaging import SYLLABUS_ASSESSMENT, rubrics
from waike_course_ready.provenance import audit, strip_lesson_padding

BATCH_001 = {"GENERAL_IT", "COMPUTER_NETWORKING", "CYBERSECURITY"}
BATCH_002 = {"SOFTWARE_BUILDER", "HARDWARE_ENGINEERING", "PM_AGILE_LSS"}


def test_batch001_and_batch002_coexist_in_product_paths():
    """#43 coverage must remain; #44 adds three courses. Do not replace COURSES."""
    assert BATCH_001.issubset(set(COURSES))
    assert BATCH_002.issubset(set(COURSES))
    assert set(COURSES) == BATCH_001 | BATCH_002
    assert len(COURSES) == 6
    assert set(COURSES_001) == BATCH_001
    assert set(COURSES_002) == BATCH_002


def test_each_course_has_depth():
    for cid, c in COURSES.items():
        assert len(c["weeks"]) >= 8, cid
        for w in c["weeks"]:
            stripped = strip_lesson_padding(w["lesson"])
            assert len(stripped) >= 800, (cid, w["week"], len(stripped))
            assert "Operator note: record evidence" not in stripped
            assert "Evidence discipline week" not in stripped
        items = sum(len(w["quiz"]) for w in c["weeks"])
        assert items >= 48, (cid, items)
        assert len({w["lesson"][:120] for w in c["weeks"]}) == len(c["weeks"]), cid


def test_labs_compute_and_negatives_fail():
    bundle = run_all()
    assert bundle["ok"] is True, {k: bundle.get(k) for k in (
        "empty_submission_fails", "wrong_submission_fails", "print_pass_raises",
        "ttl1_from_parsed_header", "no_submission_fails", "negatives_must_fail_and_did",
        "computed_honesty_gate",
    )}
    # #43 (20) ∪ #44 (30) when both batches are registered
    assert bundle["lab_count"] == 50, bundle["lab_count"]
    assert bundle.get("batch_001_lab_count") == 20
    assert bundle.get("batch_002_lab_count") == 30
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
    raised3 = False
    try:
        run_lab("lab_observability", submission="PASS")
    except AssertionError:
        raised3 = True
    assert raised3


def test_mid_final_not_weekly_clones():
    for cid in COURSES:
        weekly = {i["stem"] for w in COURSES[cid]["weeks"] for i in w["quiz"]}
        weekly_list = list(weekly)
        extras = extra_assessment_items(cid)
        assert len(extras["mid"]) == 20
        assert len(extras["final"]) == 24
        for item in extras["mid"] + extras["final"]:
            assert item["stem"] not in weekly, (cid, item["id"])
            assert not item["stem"].startswith("Mid-course check:")
            assert not item["stem"].startswith("Capstone check:")
            j, near = nearest_weekly(item["stem"], weekly_list)
            assert not token_identical(item["stem"], near), (cid, item["id"], item["stem"], near)
            assert j < TOKEN_JACCARD_FAIL, (cid, item["id"], j, item["stem"], near)


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
    assert len(set(texts)) == len(COURSES)


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
    ids = {c["course_id"] for c in cat["courses"]}
    assert BATCH_001.issubset(ids)
    assert BATCH_002.issubset(ids)
    assert len(ids) == 6
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
    assert result["exam_token_identical"] == 0, result.get("exam_restatement_hits")
    assert result["exam_token_jaccard_ge_0_80"] == 0, result.get("exam_restatement_hits")
    assert result["status"] == "PASS", result["findings"]
    # Depth gate: padding spam must be rejected at provenance layer
    assert result.get("lesson_padding_rejected", 0) == 0
    assert all(v >= 800 for v in (result.get("stripped_lesson_mins") or {}).values())
