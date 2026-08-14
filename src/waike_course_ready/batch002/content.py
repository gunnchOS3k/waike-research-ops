"""Original WAIKE bodies for COURSE-READY-002 batch."""
from __future__ import annotations
from typing import Any

BATCH_COURSE_IDS = ("SOFTWARE_BUILDER", "HARDWARE_ENGINEERING", "PM_AGILE_LSS")

def _q(qid: str, stem: str, choices: list[str], answer: int, explain: str, kind: str = "mcq") -> dict[str, Any]:
    assert 0 <= answer < len(choices)
    return {"id": qid, "kind": kind, "stem": stem, "choices": choices, "answer_index": answer, "explanation": explain}

import json
from pathlib import Path
_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
SOFTWARE_BUILDER = _DATA["SOFTWARE_BUILDER"]
HARDWARE_ENGINEERING = _DATA["HARDWARE_ENGINEERING"]
PM_AGILE_LSS = _DATA["PM_AGILE_LSS"]
COURSES_002 = {
    "SOFTWARE_BUILDER": SOFTWARE_BUILDER,
    "HARDWARE_ENGINEERING": HARDWARE_ENGINEERING,
    "PM_AGILE_LSS": PM_AGILE_LSS,
}
