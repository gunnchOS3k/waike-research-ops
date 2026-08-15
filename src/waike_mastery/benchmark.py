"""Curriculum-grounded MCQ solver + isomorphic variants (anti-memorization)."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .grading import grade_mcq_submission
from .registry import build_assessable_registry, KEY_FIELD_NAMES

ROOT = Path(__file__).resolve().parents[2]


def _tokenize(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9_./+-]+", (s or "").lower()))


def _lesson_tokens(course_id: str, root: Path) -> set[str]:
    base = root / "curriculum" / "digital_rc" / course_id
    parts: list[str] = []
    for p in sorted((base / "weeks").glob("w*/lesson.md")):
        parts.append(p.read_text(encoding="utf-8"))
    cj = base / "course.json"
    if cj.is_file():
        parts.append(cj.read_text(encoding="utf-8"))
    return _tokenize("\n".join(parts))


def solve_mcq_item(item: dict[str, Any], lesson_tok: set[str]) -> int:
    """Pick a choice from student stem/choices + lesson text — never answer keys."""
    stem_tok = _tokenize(item.get("stem") or "")
    best_i = 0
    best_s = -1.0
    for i, ch in enumerate(item.get("choices") or []):
        ct = _tokenize(ch)
        score = float(len(ct & lesson_tok) * 2 + len(ct & stem_tok))
        for t in ct:
            if len(t) > 5 and t in lesson_tok:
                score += 2.0
        # Prefer concrete policy words that appear in lessons
        low = ch.lower()
        for cue in ("fail", "must", "both", "not", "never", "block", "disclose", "public_reference_only"):
            if cue in low and (cue in " ".join(lesson_tok) or cue in (item.get("stem") or "").lower()):
                score += 1.5
        if score > best_s:
            best_s = score
            best_i = i
    return best_i


def isomorphic_variant(item: dict[str, Any], seed: str = "v1") -> dict[str, Any]:
    """Permute choice order deterministically — same skill, different surface form."""
    choices = list(item.get("choices") or [])
    if len(choices) < 2:
        return dict(item)
    h = int(hashlib.sha256(f"{seed}:{item.get('item_id')}".encode()).hexdigest()[:8], 16)
    order = list(range(len(choices)))
    # rotate by hash
    rot = h % len(choices)
    order = order[rot:] + order[:rot]
    # optional swap if even
    if h % 2 == 0 and len(order) > 1:
        order[0], order[1] = order[1], order[0]
    new_choices = [choices[i] for i in order]
    # map original index → new index for later remapping if needed
    remap = {orig: new_i for new_i, orig in enumerate(order)}
    out = dict(item)
    out["choices"] = new_choices
    out["variant_seed"] = seed
    out["choice_remap_from_original"] = remap
    out["isomorphic"] = True
    return out


def run_mastery_benchmark(root: Path | None = None, max_items_per_course: int | None = None) -> dict[str, Any]:
    root = root or ROOT
    registry = build_assessable_registry(root)
    # Ensure registry has no keys
    assert not registry["key_fields_present_in_registry"]

    lesson_cache: dict[str, set[str]] = {}
    submissions: dict[str, dict[str, dict[str, int]]] = {}
    # course -> assessment_id -> {item_id_local: answer_index}
    item_meta: dict[str, dict[str, Any]] = {}

    mcq_items = [i for i in registry["items"] if i.get("kind") == "mcq" and i.get("choices")]
    per_course_seen: dict[str, int] = {}

    for item in mcq_items:
        cid = item["course_id"]
        if max_items_per_course is not None:
            if per_course_seen.get(cid, 0) >= max_items_per_course:
                continue
            per_course_seen[cid] = per_course_seen.get(cid, 0) + 1
        if cid not in lesson_cache:
            lesson_cache[cid] = _lesson_tokens(cid, root)
        # Canary: refuse if answer_index sneaks into item
        for k in KEY_FIELD_NAMES:
            if k in item:
                raise RuntimeError(f"solver saw key field {k} on {item.get('item_id')}")
        ans = solve_mcq_item(item, lesson_cache[cid])
        local_id = (item.get("item_id") or "").split(":")[-1]
        ak = item["assessment_kind"]
        aid = item["assessment_id"]
        submissions.setdefault(cid, {}).setdefault(f"{ak}::{aid}", {})[local_id] = ans
        item_meta[item["item_id"]] = {"course_id": cid, "assessment_kind": ak, "assessment_id": aid}

    # Isolated grading after all submissions collected
    grade_rows = []
    per_course_scores: dict[str, dict[str, Any]] = {}
    per_assessment: dict[str, float] = {}
    per_domain: dict[str, list[float]] = {}

    for cid, assessments in submissions.items():
        course_correct = 0
        course_total = 0
        for key, answers in assessments.items():
            kind, aid = key.split("::", 1)
            graded = grade_mcq_submission(cid, kind, aid, answers, root)
            grade_rows.append(graded)
            course_correct += graded["correct"]
            course_total += graded["total"]
            per_assessment[f"{cid}:{aid}"] = graded["score"]
            domain = f"{cid}.knowledge"
            per_domain.setdefault(domain, []).append(graded["score"])
        per_course_scores[cid] = {
            "correct": course_correct,
            "total": course_total,
            "score": (course_correct / course_total) if course_total else 0.0,
        }

    overall_correct = sum(r["correct"] for r in grade_rows)
    overall_total = sum(r["total"] for r in grade_rows)
    domain_scores = {d: (sum(v) / len(v) if v else 0.0) for d, v in per_domain.items()}

    return {
        "schema": "waike.mastery_benchmark.v1",
        "solver": "curriculum_overlap_v1",
        "used_instructor_keys_during_solve": False,
        "self_graded": False,
        "grading_agent": "isolated_after_submission",
        "items_attempted": overall_total,
        "items_correct": overall_correct,
        "overall_score": (overall_correct / overall_total) if overall_total else 0.0,
        "per_course": per_course_scores,
        "per_assessment": per_assessment,
        "per_domain": domain_scores,
        "grade_rows": grade_rows,
    }
