"""Curriculum self-audit → CURRICULUM_DEFECT_CANDIDATE when warranted."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .discover import discover_courses

ROOT = Path(__file__).resolve().parents[2]

TRAILER_SPAM = re.compile(r"(Ticket arithmetic checkpoint|Acceptance for week \d+ still names)", re.I)


def audit_curriculum(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    courses = discover_courses(root)
    candidates: list[dict[str, Any]] = []

    for meta in courses:
        course_dir = root / meta["path"]
        for week_dir in sorted((course_dir / "weeks").glob("w*")):
            lesson = week_dir / "lesson.md"
            if not lesson.is_file():
                candidates.append(
                    {
                        "code": "CURRICULUM_DEFECT_CANDIDATE",
                        "severity": "high",
                        "course_id": meta["course_id"],
                        "path": str(lesson.relative_to(root)),
                        "reason": "missing_lesson_md",
                    }
                )
                continue
            text = lesson.read_text(encoding="utf-8")
            if len(text.strip()) < 400:
                candidates.append(
                    {
                        "code": "CURRICULUM_DEFECT_CANDIDATE",
                        "severity": "medium",
                        "course_id": meta["course_id"],
                        "path": str(lesson.relative_to(root)),
                        "reason": "lesson_too_short",
                        "chars": len(text.strip()),
                    }
                )
            hits = TRAILER_SPAM.findall(text)
            if len(hits) >= 3:
                candidates.append(
                    {
                        "code": "CURRICULUM_DEFECT_CANDIDATE",
                        "severity": "high",
                        "course_id": meta["course_id"],
                        "path": str(lesson.relative_to(root)),
                        "reason": "adversarial_trailer_spam",
                        "hit_count": len(hits),
                    }
                )
        # quiz without choices
        for qrel in meta["quiz_files"]:
            quiz = json.loads((course_dir / qrel).read_text(encoding="utf-8"))
            for item in quiz.get("items") or []:
                if item.get("kind") == "mcq" and len(item.get("choices") or []) < 2:
                    candidates.append(
                        {
                            "code": "CURRICULUM_DEFECT_CANDIDATE",
                            "severity": "high",
                            "course_id": meta["course_id"],
                            "path": qrel,
                            "item_id": item.get("id"),
                            "reason": "mcq_missing_choices",
                        }
                    )

    return {
        "schema": "waike.curriculum_self_audit.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "courses_audited": len(courses),
        "defect_candidate_count": len(candidates),
        "candidates": candidates,
        "note": "Candidates are not confirmed defects until human curriculum review.",
    }
