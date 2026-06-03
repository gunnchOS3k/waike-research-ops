from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from waike_curriculum.catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_group_project_files():
    for c in load_catalog()["courses"]:
        assert (ROOT / "group_projects" / "by_course" / f"{c['course_id']}.yaml").exists()
