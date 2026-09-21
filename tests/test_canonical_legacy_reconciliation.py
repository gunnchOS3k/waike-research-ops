"""Machine-readable canonical ↔ legacy package reconciliation tests."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_course_ready.content import COURSES  # noqa: E402

RECON = ROOT / "artifacts/full_readiness/CANONICAL_LEGACY_PACKAGE_RECONCILIATION.json"
EMIT = ROOT / "scripts/full_readiness/emit_canonical_legacy_reconciliation.py"

EXPECTED_SHARED = {
    "DIGITAL_CONFIDENCE": "GENERAL_IT",
    "IT_SUPPORT_HARDWARE": "GENERAL_IT",
    "NETWORKING_INFRA": "COMPUTER_NETWORKING",
    "CYBER_SOC": "CYBERSECURITY",
}


def test_emit_reconciliation_ok():
    subprocess.check_call([sys.executable, str(EMIT)], cwd=ROOT)
    assert RECON.exists()
    data = json.loads(RECON.read_text(encoding="utf-8"))
    assert data["ok"] is True
    assert data["canonical_track_count"] == 18
    assert data["legacy_product_course_count"] == 17
    assert data["all_canonical_tracks_addressable"] is True
    assert set(data["legacy_product_courses"]) == set(COURSES)
    by_tid = {row["track_id"]: row for row in data["mapping"]}
    assert set(by_tid) == {
        t["track_id"]
        for t in json.loads((ROOT / "curriculum/taxonomy/eighteen_tracks.json").read_text())["tracks"]
    }
    for tid, legacy in EXPECTED_SHARED.items():
        assert by_tid[tid]["legacy_digital_rc_id"] == legacy
        assert by_tid[tid]["shared_package"] is True
        assert by_tid[tid]["ok"] is True
    for row in data["mapping"]:
        assert row["ok"] is True
        assert row["legacy_in_COURSES_product_path"] is True
        assert (ROOT / row["digital_rc_path"] / "course.json").exists()


def test_reconciliation_required_by_digital_rc_writer_contract():
    """Writer must not silent-pass without reconciliation artifact."""
    text = (ROOT / "scripts/write_course_digital_rc.py").read_text(encoding="utf-8")
    assert "CANONICAL_LEGACY_PACKAGE_RECONCILIATION.json" in text
    assert "expected 27 after batch009" in text
    assert "batch_007_lab_count" in text
    assert "187" in text
