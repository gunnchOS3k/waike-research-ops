"""Mid/final banks for STREAM-B DATA_DASHBOARDS."""
from __future__ import annotations

import json
from pathlib import Path

_EX = json.loads((Path(__file__).with_name("exams_data.json")).read_text(encoding="utf-8"))


def extra_assessment_items_006(course_id: str):
    from waike_course_ready.exams import rebalance_mcq

    spec = _EX[course_id]
    mid = rebalance_mcq(spec["mid"], spec["offset"])
    final = rebalance_mcq(spec["final"], spec["offset"] + 1)
    if len(mid) != 20 or len(final) != 24:
        raise ValueError(f"{course_id} exam sizes mid={len(mid)} final={len(final)}")
    return {"mid": mid, "final": final}
