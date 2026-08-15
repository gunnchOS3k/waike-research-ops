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


def measure_instructor_keys_in_contexts(contexts: list[str], root: Path) -> dict[str, Any]:
    """Measure whether solver contexts contain instructor answer-key material (not hardcoded)."""
    hits: list[dict[str, str]] = []
    for course_dir in sorted((root / "curriculum" / "digital_rc").iterdir()):
        if not course_dir.is_dir():
            continue
        keys_path = course_dir / "instructor" / "answer_keys.json"
        if not keys_path.is_file():
            continue
        keys_blob = keys_path.read_text(encoding="utf-8")
        # Distinctive fingerprints from real keys
        fingerprints = ['"schema": "waike.answer_keys.v1"', '"answer_index"']
        # Also sample a few concrete answer_index lines
        for line in keys_blob.splitlines():
            if "answer_index" in line and len(line.strip()) > 10:
                fingerprints.append(line.strip()[:80])
                if len(fingerprints) > 8:
                    break
        for i, ctx in enumerate(contexts):
            for fp in fingerprints:
                if fp and fp in ctx:
                    hits.append({"course_id": course_dir.name, "fingerprint": fp, "context_index": str(i)})
                    break
    return {
        "used_instructor_keys_during_solve": len(hits) > 0,
        "hit_count": len(hits),
        "hits_sample": hits[:5],
    }


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
    rot = h % len(choices)
    order = order[rot:] + order[:rot]
    if h % 2 == 0 and len(order) > 1:
        order[0], order[1] = order[1], order[0]
    new_choices = [choices[i] for i in order]
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
    assert not registry["key_fields_present_in_registry"]

    lesson_cache: dict[str, set[str]] = {}
    submissions: dict[str, dict[str, dict[str, int]]] = {}
    solver_contexts: list[str] = []
    transfer_pairs: list[dict[str, Any]] = []

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
        for k in KEY_FIELD_NAMES:
            if k in item:
                raise RuntimeError(f"solver saw key field {k} on {item.get('item_id')}")

        ctx = json.dumps({"item": item, "lesson_tokens_sorted": sorted(lesson_cache[cid])[:50]})
        solver_contexts.append(ctx)

        ans = solve_mcq_item(item, lesson_cache[cid])
        local_id = (item.get("item_id") or "").split(":")[-1]
        ak = item["assessment_kind"]
        aid = item["assessment_id"]
        submissions.setdefault(cid, {}).setdefault(f"{ak}::{aid}", {})[local_id] = ans

        # Transfer probe: isomorphic variant — remap chosen index back for grading later
        if len(transfer_pairs) < 60:
            variant = isomorphic_variant(item, seed="transfer-v1")
            var_ans = solve_mcq_item(variant, lesson_cache[cid])
            # Map variant choice index back to original index
            remap = variant.get("choice_remap_from_original") or {}
            inv = {new: orig for orig, new in remap.items()}
            orig_from_variant = inv.get(var_ans, var_ans)
            transfer_pairs.append(
                {
                    "item_id": item["item_id"],
                    "course_id": cid,
                    "assessment_kind": ak,
                    "assessment_id": aid,
                    "local_id": local_id,
                    "primary_answer": ans,
                    "transfer_answer_original_space": orig_from_variant,
                }
            )

    key_measure = measure_instructor_keys_in_contexts(solver_contexts, root)

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

    # Grade transfer answers via isolated grader
    transfer_correct = 0
    transfer_total = 0
    # Batch by assessment
    transfer_subs: dict[str, dict[str, dict[str, int]]] = {}
    for pair in transfer_pairs:
        cid = pair["course_id"]
        key = f"{pair['assessment_kind']}::{pair['assessment_id']}"
        transfer_subs.setdefault(cid, {}).setdefault(key, {})[pair["local_id"]] = pair[
            "transfer_answer_original_space"
        ]
    for cid, assessments in transfer_subs.items():
        for key, answers in assessments.items():
            kind, aid = key.split("::", 1)
            graded = grade_mcq_submission(cid, kind, aid, answers, root)
            # Only count items we actually transferred
            ids = set(answers.keys())
            for row in graded["items"]:
                if row["id"] in ids:
                    transfer_total += 1
                    if row["ok"]:
                        transfer_correct += 1
    transfer_score = (transfer_correct / transfer_total) if transfer_total else None

    return {
        "schema": "waike.mastery_benchmark.v1",
        "solver": "curriculum_overlap_v1",
        "used_instructor_keys_during_solve": bool(key_measure["used_instructor_keys_during_solve"]),
        "key_use_measurement": key_measure,
        "self_graded": False,
        "grading_agent": "isolated_after_submission",
        "items_attempted": overall_total,
        "items_correct": overall_correct,
        "overall_score": (overall_correct / overall_total) if overall_total else 0.0,
        "per_course": per_course_scores,
        "per_assessment": per_assessment,
        "per_domain": domain_scores,
        "transfer": {
            "items": transfer_total,
            "correct": transfer_correct,
            "score": transfer_score,
            "method": "isomorphic_choice_permutation",
        },
        "grade_rows": grade_rows,
    }
