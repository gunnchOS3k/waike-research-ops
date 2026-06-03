from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_master_rubric_scale():
    text = (ROOT / "rubrics" / "master_rubric.yaml").read_text()
    assert "4:" in text or "4 :" in text or "scale" in text
