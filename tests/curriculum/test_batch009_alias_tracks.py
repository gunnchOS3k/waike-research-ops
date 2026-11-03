"""batch009: own packages for the four formerly alias-only catalog tracks."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.batch009 import labs_dco, labs_ish, labs_nif, labs_soc  # noqa: E402
from waike_course_ready.batch009.content import AUTHORED_COURSE_IDS, BATCH_COURSE_IDS  # noqa: E402
from waike_course_ready.content import COURSES  # noqa: E402
from waike_course_ready.provenance import repeated_lesson_sentences, strip_lesson_padding  # noqa: E402

DATA = json.loads((ROOT / "src" / "waike_course_ready" / "batch009" / "courses_data.json").read_text(encoding="utf-8"))
EXAMS = json.loads((ROOT / "src" / "waike_course_ready" / "batch009" / "exams_data.json").read_text(encoding="utf-8"))
LAB_MODULES = {m.COURSE: m for m in (labs_soc, labs_dco, labs_ish, labs_nif)}
TAGS = {labs_soc.COURSE: "SOC", labs_dco.COURSE: "DCO", labs_ish.COURSE: "ISH", labs_nif.COURSE: "NIF"}
FORMER_ALIAS_TARGET = {
    "CYBER_SOC": "CYBERSECURITY",
    "DIGITAL_CONFIDENCE": "GENERAL_IT",
    "IT_SUPPORT_HARDWARE": "HARDWARE_ENGINEERING",
    "NETWORKING_INFRA": "COMPUTER_NETWORKING",
}
_SENT = re.compile(r"(?<=[.!?])\s+")


def _sentences(text: str) -> set[str]:
    return {s.strip().lower() for s in _SENT.split(text) if len(s.strip()) > 30}


def _labs(cid: str):
    mod, tag = LAB_MODULES[cid], TAGS[cid]
    return getattr(mod, f"LABS_{tag}"), getattr(mod, f"REFERENCE_{tag}"), getattr(mod, f"WRONG_{tag}"), getattr(mod, f"LAB_ORDER_{tag}")


@pytest.mark.parametrize("cid", AUTHORED_COURSE_IDS)
def test_ten_distinct_weeks_without_repeated_sentences(cid):
    course = DATA[cid]
    weeks = course["weeks"]
    assert course["track_ids"] == [cid]
    assert [w["week"] for w in weeks] == list(range(1, 11))
    assert len({w["title"] for w in weeks}) == 10
    assert len({w["lesson"] for w in weeks}) == 10
    seen: set[str] = set()
    for w in weeks:
        assert not repeated_lesson_sentences(w["lesson"]), (cid, w["week"])
        assert len(strip_lesson_padding(w["lesson"])) >= 800, (cid, w["week"])
        sents = _sentences(w["lesson"])
        assert not (sents & seen), (cid, w["week"], sorted(sents & seen)[:2])
        seen |= sents
        assert len(w["quiz"]) == 6


@pytest.mark.parametrize("cid", AUTHORED_COURSE_IDS)
def test_not_a_copy_of_the_course_it_used_to_alias(cid):
    from waike_course_ready.content import COURSES as ALL

    ours = set().union(*(_sentences(w["lesson"]) for w in DATA[cid]["weeks"]))
    theirs = set().union(*(_sentences(w["lesson"]) for w in ALL[FORMER_ALIAS_TARGET[cid]]["weeks"]))
    assert not (ours & theirs)
    stems = {q["stem"] for w in ALL[FORMER_ALIAS_TARGET[cid]]["weeks"] for q in w["quiz"]}
    assert not stems & {q["stem"] for w in DATA[cid]["weeks"] for q in w["quiz"]}


@pytest.mark.parametrize("cid", AUTHORED_COURSE_IDS)
def test_exam_items_are_original(cid):
    weekly = {q["stem"] for w in DATA[cid]["weeks"] for q in w["quiz"]}
    mid, final = EXAMS[cid]["mid"], EXAMS[cid]["final"]
    assert len(mid) == 20 and len(final) == 24
    stems = [q["stem"] for q in mid + final]
    assert len(set(stems)) == 44
    assert not set(stems) & weekly


@pytest.mark.parametrize("cid", AUTHORED_COURSE_IDS)
def test_labs_map_one_to_one_and_reject_stub_and_wrong(cid):
    labs, ref, wrong, order = _labs(cid)
    assert [w["lab_id"] for w in DATA[cid]["weeks"]] == list(order) == list(labs)
    for lab_id, fn in labs.items():
        assert fn(ref[lab_id]).ok, lab_id
        assert not fn(wrong[lab_id]).ok, lab_id
        assert not fn({}).ok, lab_id
        assert not fn(None).ok, lab_id
        with pytest.raises(AssertionError):
            fn("PASS")


def test_soc_graders_recompute_from_submitted_parameters():
    ref = labs_soc.REFERENCE_SOC
    window = ref["lab_soc_window_rule"]
    assert not labs_soc.lab_soc_window_rule({**window, "threshold": 3}).ok
    assert labs_soc.lab_soc_window_rule({"threshold": 3, "window_s": 60, "alerts": labs_soc.window_alerts(3, 60)}).ok
    row = dict(ref["lab_soc_cvss_score"]["vectors"][0])
    changed = {**row, "vector": row["vector"].replace("C:H/I:H/A:H", "C:L/I:L/A:N")}
    assert not labs_soc.lab_soc_cvss_score({"vectors": [changed, ref["lab_soc_cvss_score"]["vectors"][1]]}).ok
    assert labs_soc.cvss31_base("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H") == 9.8
    assert labs_soc.cvss31_base("CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N") == 5.5


@pytest.mark.parametrize("cid", BATCH_COURSE_IDS)
def test_enabled_tracks_are_on_product_path_with_reachable_references(cid):
    assert COURSES[cid]["track_ids"] == [cid]
    assert cid not in (COURSES[FORMER_ALIAS_TARGET[cid]].get("track_ids") or [])
    alias = json.loads((ROOT / "artifacts" / "CATALOG_ALIAS_HONESTY.json").read_text(encoding="utf-8"))
    assert cid not in {row["catalog_track_id"] for row in alias["aliases"]}
    rc = json.loads((ROOT / "artifacts" / "COURSE_DIGITAL_RC.json").read_text(encoding="utf-8"))
    assert rc["courses"][cid]["COURSE_DIGITAL_RC"] is True, rc["courses"][cid]["rc_fail_reasons"]
    pkg = json.loads((ROOT / "curriculum" / "digital_rc" / cid / "course.json").read_text(encoding="utf-8"))
    alignment = json.loads((ROOT / pkg["alignment_ref"]).read_text(encoding="utf-8"))
    assert alignment["course_id"] == cid and alignment["track_ids"] == [cid]
    registry = {
        s["source_id"]: s
        for s in json.loads((ROOT / "sources" / "benchmark_registry.json").read_text(encoding="utf-8"))["sources"]
    }
    assert alignment["benchmarks"]
    for bench in alignment["benchmarks"]:
        src = registry[bench["source_id"]]
        assert src["url"].startswith("https://"), bench["source_id"]
        assert src["reuse_class"] == bench["reuse_class"], bench["source_id"]
        assert src["attribution"]
