import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from waike_curriculum.catalog import load_catalog, FLAGSHIP_CASE_STUDIES


def test_catalog_has_18_courses():
    courses = load_catalog().get("courses", [])
    assert len(courses) >= 18


def test_flagship_case_studies_per_site():
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        assert len(cases) >= 5, site
