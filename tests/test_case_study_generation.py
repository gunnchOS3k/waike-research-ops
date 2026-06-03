from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES

ROOT = Path(__file__).resolve().parents[1]


def test_35_flagship_cases():
    total = sum(len(v) for v in FLAGSHIP_CASE_STUDIES.values())
    assert total == 35
