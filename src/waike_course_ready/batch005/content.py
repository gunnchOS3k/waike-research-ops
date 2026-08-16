"""Original WAIKE bodies for STREAM-B-PKT-002 COMM_PD_ETHICS DIGITAL_RC."""
from __future__ import annotations

import json
from pathlib import Path

BATCH_COURSE_IDS = ("COMM_PD_ETHICS",)

_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
COMM_PD_ETHICS = _DATA["COMM_PD_ETHICS"]
COURSES_005 = {"COMM_PD_ETHICS": COMM_PD_ETHICS}
