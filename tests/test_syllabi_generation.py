import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from waike_curriculum.generators import seed_course
from waike_curriculum.catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_seed_one_syllabus(tmp_path, monkeypatch):
    import waike_curriculum.generators as gen
    import waike_curriculum.catalog as cat
    monkeypatch.setattr(gen, "ROOT", ROOT)
    monkeypatch.setattr(cat, "ROOT", ROOT)
    course = load_catalog()["courses"][0]
    seed_course(course)
    assert (ROOT / "syllabi" / course["course_id"] / "syllabus.md").exists()
