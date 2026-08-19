from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_ops.pathways import (  # noqa: E402
    PII_KEYS,
    anonymous_completion,
    build_all_pathways,
    discover_course_dirs,
)

SCHEMA = json.loads((ROOT / "schema" / "waike_pathway.v1.json").read_text(encoding="utf-8"))
REQUIRED = SCHEMA["required"]


def _digital_rc_course_ids(root: Path) -> list[str]:
    base = root / "curriculum" / "digital_rc"
    return sorted(
        p.name for p in base.iterdir() if p.is_dir() and (p / "course.json").is_file()
    )


def test_digital_rc_count_comes_from_files_not_a_slogan():
    dirs = discover_course_dirs(ROOT)
    ids = {p.name for p in dirs}
    on_disk = _digital_rc_course_ids(ROOT)
    assert len(dirs) == len(on_disk)
    assert ids == set(on_disk)
    assert "SOFTWARE_BUILDER" in ids
    assert "DATA_DASHBOARDS" in ids
    assert "EMBEDDED_PROTOTYPING" in ids
    assert "GUNNCHOS_PRODUCT_LAB" in ids
    # Catalog 18 is a different universe — do not collapse counts.
    catalog = (ROOT / "curriculum" / "catalog.yaml").read_text(encoding="utf-8")
    assert catalog.count("course_id:") >= 18


def test_each_digital_rc_pathway_has_required_fields_and_refs():
    dirs = discover_course_dirs(ROOT)
    pathways = build_all_pathways(ROOT)
    assert len(pathways) == len(dirs)
    seen = set()
    for pathway in pathways:
        for key in REQUIRED:
            assert key in pathway, (pathway.get("course_id"), key)
        cid = pathway["course_id"]
        assert cid not in seen
        seen.add(cid)
        course_dir = ROOT / "curriculum" / "digital_rc" / cid
        assert (course_dir / pathway["start"]["student_packet_ref"]).is_file()
        assert (course_dir / pathway["instructor_guidance"]["instructor_packet_ref"]).is_file()
        assert (course_dir / "prerequisites.json").is_file()
        assert len(pathway["objectives"]) >= 8
        assert len(pathway["lessons"]) >= 8
        assert len(pathway["labs"]) >= 4
        assert len(pathway["rubrics"]) >= 1
        assert pathway["completion_tracking"]["pii_forbidden"] is True
        for lesson in pathway["lessons"]:
            assert (course_dir / lesson["body_ref"]).is_file(), (cid, lesson["body_ref"])
        for lab_id in pathway["labs"]:
            assert (course_dir / "labs" / lab_id / "README.md").is_file(), (cid, lab_id)


def test_completion_records_reject_pii_keys():
    rec = anonymous_completion("SOFTWARE_BUILDER", 1, "a01", lab_id="lab_git_conflict", lab_ok=True)
    assert rec["schema"] == "waike.completion_tracking.v1"
    assert PII_KEYS.isdisjoint(rec)
    try:
        anonymous_completion("SOFTWARE_BUILDER", 1, "a01", opaque_learner_ref="ada@example.com")
        raised = False
    except ValueError:
        raised = True
    assert raised
