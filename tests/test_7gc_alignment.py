import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES

ROOT = Path(__file__).resolve().parents[1]


def test_case_study_dirs_exist():
    for site, cases in FLAGSHIP_CASE_STUDIES.items():
        for case in cases:
            assert (ROOT / "case_studies" / "7gc" / site / case["case_id"] / "case_brief.md").exists()
