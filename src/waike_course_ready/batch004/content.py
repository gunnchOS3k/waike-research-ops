"""Original WAIKE bodies for COURSE-READY-004 batch."""
from __future__ import annotations

import json
from pathlib import Path

BATCH_COURSE_IDS = ("WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE")

_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
WIRELESS_6G = _DATA["WIRELESS_6G"]
ROBOTICS_CONTROL = _DATA["ROBOTICS_CONTROL"]
GAME_DEV_INTERACTIVE = _DATA["GAME_DEV_INTERACTIVE"]
COURSES_004 = {
    "WIRELESS_6G": WIRELESS_6G,
    "ROBOTICS_CONTROL": ROBOTICS_CONTROL,
    "GAME_DEV_INTERACTIVE": GAME_DEV_INTERACTIVE,
}
