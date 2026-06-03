import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from waike_curriculum.catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_assignments_per_course():
    for c in load_catalog()["courses"]:
        adir = ROOT / "assignments" / "by_course" / c["course_id"]
        assert len(list(adir.glob("*.yaml"))) >= 4
