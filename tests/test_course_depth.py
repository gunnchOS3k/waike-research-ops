import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from waike_curriculum.depth_content import FLAGSHIP_COURSES

ROOT = Path(__file__).resolve().parents[1]


def test_flagship_assignment_depth():
    text = (ROOT / "assignment_bodies/by_course/digital_confidence/assignment_01.md").read_text()
    assert "## Step-by-step instructions" in text
    assert len(text) > 800


def test_flagship_count():
    assert len(FLAGSHIP_COURSES) == 6
