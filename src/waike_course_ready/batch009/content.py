"""Original WAIKE bodies for batch009 — the four formerly alias-only catalog tracks."""
from __future__ import annotations
import json
from pathlib import Path
AUTHORED_COURSE_IDS = ("CYBER_SOC", "DIGITAL_CONFIDENCE", "IT_SUPPORT_HARDWARE", "NETWORKING_INFRA")
# Tracks on the product path; a track joins only once its package passes the gate.
BATCH_COURSE_IDS = ("CYBER_SOC", "DIGITAL_CONFIDENCE")
_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
COURSES_009 = {cid: _DATA[cid] for cid in BATCH_COURSE_IDS}
