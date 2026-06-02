import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from waike_ops.campus_tracks import list_sites, load_track


def test_tracks():
    assert len(list_sites()) == 7
    t = load_track("gary")
    assert "beginner_pathway" in t
