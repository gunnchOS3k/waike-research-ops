"""Original WAIKE bodies for batch008 SEVEN_GC_APPRENTICESHIP."""
from __future__ import annotations
import json
from pathlib import Path
BATCH_COURSE_IDS = ("SEVEN_GC_APPRENTICESHIP",)
_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
SEVEN_GC_APPRENTICESHIP = _DATA["SEVEN_GC_APPRENTICESHIP"]
COURSES_008 = {"SEVEN_GC_APPRENTICESHIP": SEVEN_GC_APPRENTICESHIP}
