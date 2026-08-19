"""Original WAIKE bodies for batch007 residual closure."""
from __future__ import annotations
import json
from pathlib import Path
BATCH_COURSE_IDS = ("EMBEDDED_PROTOTYPING", "GUNNCHOS_PRODUCT_LAB")
_DATA = json.loads((Path(__file__).with_name("courses_data.json")).read_text(encoding="utf-8"))
EMBEDDED_PROTOTYPING = _DATA["EMBEDDED_PROTOTYPING"]
GUNNCHOS_PRODUCT_LAB = _DATA["GUNNCHOS_PRODUCT_LAB"]
COURSES_007 = {"EMBEDDED_PROTOTYPING": EMBEDDED_PROTOTYPING, "GUNNCHOS_PRODUCT_LAB": GUNNCHOS_PRODUCT_LAB}
