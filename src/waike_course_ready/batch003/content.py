"""Original WAIKE bodies for COURSE-READY-003 batch."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BATCH_COURSE_IDS = ("AI_ML_EDGE", "DATA_VIZ_BI", "CLOUD_DEVOPS")

_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
AI_ML_EDGE = _DATA["AI_ML_EDGE"]
DATA_VIZ_BI = _DATA["DATA_VIZ_BI"]
CLOUD_DEVOPS = _DATA["CLOUD_DEVOPS"]
COURSES_003 = {
    "AI_ML_EDGE": AI_ML_EDGE,
    "DATA_VIZ_BI": DATA_VIZ_BI,
    "CLOUD_DEVOPS": CLOUD_DEVOPS,
}
