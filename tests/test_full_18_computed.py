"""full_18 is computed from the writer gate over all 18 catalog tracks, never hardcoded."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402

_spec = importlib.util.spec_from_file_location("write_course_digital_rc", ROOT / "scripts" / "write_course_digital_rc.py")
writer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(writer)

CATALOG = sorted(
    t.get("track_id") or t.get("id")
    for t in json.loads((ROOT / "curriculum" / "taxonomy" / "eighteen_tracks.json").read_text(encoding="utf-8"))["tracks"]
)


def _load(name: str) -> dict:
    return json.loads((ROOT / "artifacts" / name).read_text(encoding="utf-8"))


def _synthetic(ids: list[str]) -> tuple[dict, dict]:
    courses = {t: {"track_ids": [t]} for t in ids}
    per_course = {t: {"COURSE_DIGITAL_RC": True} for t in ids}
    return courses, per_course


def test_writer_has_no_literal_full_18_value():
    src = (ROOT / "scripts" / "write_course_digital_rc.py").read_text(encoding="utf-8")
    assert not re.search(r'"full_18_course_digital_rc"\s*:\s*(True|False)', src)
    assert '"full_18_course_digital_rc": full_18' in src
    assert "full_18, full_18_detail = compute_full_18(" in src


def test_compute_full_18_follows_its_inputs():
    courses, per_course = _synthetic(CATALOG)
    assert writer.compute_full_18(per_course, CATALOG, [], courses)[0] is True

    failing = {**per_course, CATALOG[0]: {"COURSE_DIGITAL_RC": False}}
    full, detail = writer.compute_full_18(failing, CATALOG, [], courses)
    assert full is False and detail["catalog_ids_not_passing"] == [CATALOG[0]]

    alias = [{"catalog_track_id": CATALOG[1], "maps_to_course_digital_rc_key": CATALOG[2]}]
    assert writer.compute_full_18(per_course, CATALOG, alias, courses)[0] is False

    alias_only = {k: v for k, v in courses.items() if k != CATALOG[1]}
    full, detail = writer.compute_full_18(per_course, CATALOG, alias, alias_only)
    assert full is False and detail["alias_only_catalog_ids"] == [CATALOG[1]]

    borrowing = {**courses, "EXTRA": {"track_ids": [CATALOG[3]]}}
    full, detail = writer.compute_full_18(per_course, CATALOG, [], borrowing)
    assert full is False and detail["catalog_ids_borrowed_by_other_courses"] == [CATALOG[3]]

    assert writer.compute_full_18(per_course, CATALOG[:17], [], courses)[0] is False


def test_artifact_full_18_matches_recomputation_from_gate_rows():
    rc = _load("COURSE_DIGITAL_RC.json")
    aliases = _load("CATALOG_ALIAS_HONESTY.json")["aliases"]
    full, detail = writer.compute_full_18(rc["courses"], CATALOG, aliases)
    assert rc["full_18_course_digital_rc"] is full
    assert rc["full_18_detail"] == detail


def test_full_18_true_only_with_own_packages_and_no_aliases():
    rc = _load("COURSE_DIGITAL_RC.json")
    aliases = _load("CATALOG_ALIAS_HONESTY.json")["aliases"]
    own_passing = [
        t for t in CATALOG
        if t in COURSES and COURSES[t].get("track_ids") == [t] and rc["courses"].get(t, {}).get("COURSE_DIGITAL_RC") is True
    ]
    borrowed = [t for cid, c in COURSES.items() for t in c.get("track_ids") or [] if t != cid and t in CATALOG]
    expected = len(CATALOG) == 18 and len(own_passing) == 18 and not aliases and not borrowed
    assert rc["full_18_course_digital_rc"] is expected
    if rc["full_18_course_digital_rc"]:
        for t in CATALOG:
            assert (ROOT / "curriculum" / "digital_rc" / t / "course.json").is_file(), t
    for flag in ("HUMAN_E6", "REAL_STUDENT_E6", "REAL_TEACHER_E6"):
        assert rc[flag] is False
