#!/usr/bin/env python3
"""Generate batch009 course data for the four formerly alias-only catalog tracks.

CYBER_SOC, DIGITAL_CONFIDENCE, IT_SUPPORT_HARDWARE, and NETWORKING_INFRA each get
their own course. Lessons, quizzes, and exams are authored in
scripts/batch009_authoring/, one week at a time; numbers in lessons match the
graders in batch009/labs_*.py, which recompute them from submitted inputs.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "src" / "waike_course_ready" / "batch009"
sys.path.insert(0, str(Path(__file__).resolve().parent))

from batch009_authoring import cyber_soc, digital_confidence, it_support_hardware, networking_infra  # noqa: E402

MODULES = (cyber_soc, digital_confidence, it_support_hardware, networking_infra)
EXAM_OFFSETS = {"CYBER_SOC": 2, "DIGITAL_CONFIDENCE": 5, "IT_SUPPORT_HARDWARE": 3, "NETWORKING_INFRA": 6}


def _q(qid: str, stem: str, choices: list[str], explain: str) -> dict:
    if len(choices) != 4 or len(set(choices)) != 4:
        raise SystemExit(f"{qid}: need four distinct choices")
    return {"id": qid, "kind": "mcq", "stem": stem, "choices": choices, "answer_index": 0, "explanation": explain}


def _weeks(mod) -> list[dict]:
    if len(mod.WEEKS) != 10:
        raise SystemExit(f"{mod.COURSE_ID}: {len(mod.WEEKS)} weeks")
    out = []
    for n, spec in enumerate(mod.WEEKS, start=1):
        if len(spec["quiz"]) != 6:
            raise SystemExit(f"{mod.COURSE_ID} week {n}: {len(spec['quiz'])} quiz items")
        out.append({
            "week": n,
            "title": spec["title"],
            "lesson": spec["lesson"],
            "worked_example": spec["worked_example"],
            "assignment": spec["assignment"],
            "lab_id": spec["lab_id"],
            "quiz": [_q(f"{mod.PREFIX}-w{n}-{i}", s, c, w) for i, (s, c, w) in enumerate(spec["quiz"], start=1)],
        })
    return out


def course(mod) -> dict:
    return {
        "course_id": mod.COURSE_ID,
        "title": mod.TITLE,
        "track_ids": [mod.COURSE_ID],
        "academy_id": mod.ACADEMY,
        "kinesthetic_hook": mod.KINESTHETIC,
        "syllabus_hook": mod.SYLLABUS_HOOK,
        "career": mod.CAREER,
        "ai_use_policy": {
            "modes": ["EXPLAIN", "HINT", "QUESTION_ME", "DEBUG_WITH_ME", "REVIEW_MY_WORK", "COMPARE_APPROACHES", "PRACTICE"],
            "assessment_modes": ["AI_ALLOWED", "AI_RESTRICTED", "AI_DISCLOSED", "NO_AI"],
            "default_weekly": "AI_DISCLOSED",
            "no_ai_weeks": list(mod.NO_AI_WEEKS),
        },
        "weeks": _weeks(mod),
    }


def exams(mod) -> dict:
    mid = [_q(f"{mod.PREFIX}-mid-{i:02d}", s, c, w) for i, (s, c, w) in enumerate(mod.MID, start=1)]
    final = [_q(f"{mod.PREFIX}-fin-{i:02d}", s, c, w) for i, (s, c, w) in enumerate(mod.FINAL, start=1)]
    if len(mid) != 20 or len(final) != 24:
        raise SystemExit(f"{mod.COURSE_ID} exam sizes mid={len(mid)} final={len(final)}")
    return {"offset": EXAM_OFFSETS[mod.COURSE_ID], "mid": mid, "final": final}


def _write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    BATCH.mkdir(parents=True, exist_ok=True)
    _write_json(BATCH / "courses_data.json", {m.COURSE_ID: course(m) for m in MODULES})
    _write_json(BATCH / "exams_data.json", {m.COURSE_ID: exams(m) for m in MODULES})
    print("Wrote batch009 course + exam data under", BATCH)


if __name__ == "__main__":
    main()
