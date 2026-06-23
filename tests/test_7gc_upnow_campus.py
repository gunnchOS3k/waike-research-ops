"""Tests for WAIKE UPNOW campus curriculum and design bundle."""
from pathlib import Path

import yaml

from waike_campus.site_registry import SITE_IDS, WEEK_TOPICS, get_site

ROOT = Path(__file__).resolve().parents[1]


def test_site_registry_complete():
    assert len(SITE_IDS) == 7
    for sid in SITE_IDS:
        site = get_site(sid)
        assert "display_name" in site
        assert "WAIKE" in site["display_name"]
        assert "UPNOW" in site["display_name"]


def test_campus_design_per_site():
    for sid in SITE_IDS:
        base = ROOT / "docs" / "campus_design" / sid
        assert (base / "README.md").exists()
        assert (base / "_ROOM_PROGRAM.md").exists()
        assert (base / "_FLOOR_PLAN_PROGRAM.md").exists()


def test_curriculum_twelve_weeks():
    for sid in SITE_IDS:
        base = ROOT / "curriculum" / f"{sid}_upnow"
        assert (base / "SYLLABUS.md").exists()
        for w in range(1, 13):
            assert (base / "lectures" / f"week_{w:02d}_lecture.md").exists()
            assert (base / "assignments" / f"a{w:02d}_assignment.md").exists()
            assert (base / "labs" / f"lab_{w:02d}.md").exists()
        for exam in ["midterm", "final", "practical"]:
            assert (base / "exams" / f"{exam}_exam.md").exists()
            assert (base / "exams" / f"{exam}_solution_key.md").exists()


def test_week_topics_count():
    assert len(WEEK_TOPICS) == 12


def test_non_claim_policy():
    text = (ROOT / "docs" / "campus_design" / "7GC_NON_CLAIM_POLICY.md").read_text()
    assert "WAIKE TF UP" in text or "internal" in text.lower() or "legacy" in text.lower()
    assert "Antarctic" in text or "antarctic" in text.lower()


def test_gaza_privacy_docs():
    text = (ROOT / "docs" / "campus_design" / "gaza" / "_PUBLIC_POSITIONING.md").read_text()
    assert "sensitive" in text.lower() or "privacy" in text.lower()


def test_graham_land_conceptual():
    text = (ROOT / "docs" / "campus_design" / "graham_land" / "README.md").read_text()
    assert "conceptual" in text.lower() or "Antarctic" in text


def test_cross_repo_handoffs():
    for sid in SITE_IDS:
        assert (ROOT / "docs" / "7gc" / "sites" / sid / "CROSS_REPO_HANDOFF.md").exists()


def test_quality_matrices():
    assert (ROOT / "quality" / "7GC_MASTER_EVIDENCE_MATRIX.md").exists()
    assert (ROOT / "quality" / "7GC_CURRICULUM_COMPLETION_MATRIX.md").exists()
