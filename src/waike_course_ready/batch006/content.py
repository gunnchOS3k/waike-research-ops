"""Original WAIKE bodies for STREAM-B-PKT-003 DATA_DASHBOARDS DIGITAL_RC."""
from __future__ import annotations

import json
from pathlib import Path

BATCH_COURSE_IDS = ("DATA_DASHBOARDS",)

_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
DATA_DASHBOARDS = _DATA["DATA_DASHBOARDS"]
COURSES_006 = {"DATA_DASHBOARDS": DATA_DASHBOARDS}
