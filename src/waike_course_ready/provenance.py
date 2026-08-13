"""Provenance + template detectors for the digital RC batch.

Lesson Jaccard alone is not enough. Packaging shells (rubrics, lab READMEs,
instructor notes, syllabus assessment language) and answer-key collapse are
first-class FAIL conditions.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.labs import COURSE_LABS
from waike_course_ready.packaging import (
    SYLLABUS_ASSESSMENT,
    SYLLABUS_CLAIM,
    SYLLABUS_DURATION,
    instructor_packet,
    instructor_week_notes,
    lab_readme,
    portfolio,
    rubrics,
)

ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN_SUBSTRINGS = [
    "prepare waike learners for industry-ready competence",
    "week 1: intuition + vocabulary + safety/privacy",
    "like learning to cook: read the recipe",
    "this is not a renamed template",
]

DUMP_MARKERS = [
    "actual exam question",
    "leaked question",
    "brain dump",
    "here is the exam dump",
    "full exam dump download",
    "paywall bypass",
    "certmaster complete dump",
]

GENERIC_TEMPLATE_MARKERS = [
    "plain-english: build real understanding and portfolio-ready skill — not exam cramming",
    "theory → case study → lab → group project → portfolio artifact",
]

CLONE_PREFIXES = ("Mid-course check:", "Capstone check:")
LETTERS = "ABCD"


def _ngrams(text: str, n: int = 5) -> set[tuple[str, ...]]:
    toks = re.findall(r"[a-z0-9']+", text.lower())
    return {tuple(toks[i : i + n]) for i in range(0, max(0, len(toks) - n + 1))}


def jaccard(a: str, b: str) -> float:
    na, nb = _ngrams(a), _ngrams(b)
    if not na or not nb:
        return 0.0
    return len(na & nb) / len(na | nb)


def lesson_text(course_id: str) -> str:
    return "\n\n".join(w["lesson"] for w in COURSES[course_id]["weeks"])


def packaging_text(course_id: str) -> str:
    c = COURSES[course_id]
    parts = [
        SYLLABUS_DURATION[course_id],
        SYLLABUS_ASSESSMENT[course_id],
        SYLLABUS_CLAIM[course_id],
        instructor_packet(course_id),
        portfolio(course_id),
        json.dumps(rubrics(course_id), sort_keys=True),
    ]
    for w in c["weeks"]:
        parts.append(instructor_week_notes(course_id, w))
    for lab_id in COURSE_LABS[course_id]:
        parts.append(lab_readme(course_id, lab_id))
    return "\n\n".join(parts)


def _key_rows(course_id: str) -> list[int]:
    rows: list[int] = []
    for w in COURSES[course_id]["weeks"]:
        for item in w["quiz"]:
            rows.append(int(item["answer_index"]))
    extras = extra_assessment_items(course_id)
    for item in extras["mid"] + extras["final"]:
        rows.append(int(item["answer_index"]))
    return rows


def _weekly_stems(course_id: str) -> set[str]:
    return {item["stem"] for w in COURSES[course_id]["weeks"] for item in w["quiz"]}


def audit() -> dict[str, Any]:
    findings: list[str] = []
    texts = {cid: lesson_text(cid) for cid in COURSES}
    packs = {cid: packaging_text(cid) for cid in COURSES}
    ids = list(COURSES)
    pairs = []
    pack_pairs = []
    worst = 0.0
    worst_pair = None
    worst_pack = 0.0
    worst_pack_pair = None
    for i, a in enumerate(ids):
        for b in ids[i + 1 :]:
            j = jaccard(texts[a], texts[b])
            pj = jaccard(packs[a], packs[b])
            pairs.append({"a": a, "b": b, "jaccard_5gram": round(j, 4)})
            pack_pairs.append({"a": a, "b": b, "packaging_jaccard_5gram": round(pj, 4)})
            if j > worst:
                worst = j
                worst_pair = [a, b]
            if pj > worst_pack:
                worst_pack = pj
                worst_pack_pair = [a, b]
    if worst >= 0.35:
        findings.append(f"BATCH_TEMPLATED_COURSES: lesson jaccard {worst:.3f} on {worst_pair}")
    if worst_pack >= 0.35:
        findings.append(f"BATCH_TEMPLATED_COURSES: packaging jaccard {worst_pack:.3f} on {worst_pack_pair}")

    for cid, text in texts.items():
        low = text.lower()
        for marker in FORBIDDEN_SUBSTRINGS + DUMP_MARKERS + GENERIC_TEMPLATE_MARKERS:
            if marker in low:
                findings.append(f"{cid} contains forbidden marker: {marker}")
        if len(text) < 8000:
            findings.append(f"{cid} lesson body too short ({len(text)} chars) — stub risk")
        weeks = [w["lesson"][:80] for w in COURSES[cid]["weeks"]]
        if len(set(weeks)) < 8:
            findings.append(f"{cid} week openings not distinct")

        weekly = list(_weekly_stems(cid))
        if len(weekly) < 48:
            findings.append(f"{cid} weekly stems {len(weekly)} < 48")
        if len(set(weekly)) != len(weekly):
            findings.append(f"{cid} duplicate weekly stems")

        extras = extra_assessment_items(cid)
        weekly_set = set(weekly)
        mid_orig = 0
        fin_orig = 0
        for item in extras["mid"]:
            stem = item["stem"]
            if stem.startswith(CLONE_PREFIXES) or stem in weekly_set:
                findings.append(f"{cid} mid clone: {item['id']}")
            else:
                mid_orig += 1
        for item in extras["final"]:
            stem = item["stem"]
            if stem.startswith(CLONE_PREFIXES) or stem in weekly_set:
                findings.append(f"{cid} final clone: {item['id']}")
            else:
                fin_orig += 1
        if mid_orig < 20:
            findings.append(f"{cid} mid original items {mid_orig} < 20")
        if fin_orig < 24:
            findings.append(f"{cid} final original items {fin_orig} < 24")

        keys = _key_rows(cid)
        dist = Counter(keys)
        n = len(keys) or 1
        unused = [LETTERS[i] for i in range(4) if dist.get(i, 0) == 0]
        if unused:
            findings.append(f"{cid} unused answer letters {unused}")
        max_share = max(dist.values()) / n
        if max_share > 0.40:
            findings.append(f"{cid} answer_index collapse max_share={max_share:.2f} dist={dict(dist)}")

    registry = json.loads((ROOT / "sources" / "benchmark_registry.json").read_text(encoding="utf-8"))
    if len(registry.get("sources", [])) < 8:
        findings.append("benchmark registry too small")
    for src in registry["sources"]:
        if src.get("reuse_class") not in {
            "OPEN_LICENSE_ADAPT_ALLOWED",
            "PUBLIC_REFERENCE_ONLY",
            "RESTRICTED",
            "UNKNOWN",
        }:
            findings.append(f"bad reuse_class on {src.get('source_id')}")
        if not src.get("attribution"):
            findings.append(f"missing attribution {src.get('source_id')}")

    stub = 1 if any("stub risk" in f for f in findings) else 0
    templated = 1 if any("BATCH_TEMPLATED" in f for f in findings) else 0
    key_balance_ok = not any("answer_index collapse" in f or "unused answer letters" in f for f in findings)
    exam_items_original = not any(" clone:" in f or "original items" in f for f in findings)

    status = "PASS" if not findings else "FAIL"
    key_report = {}
    exam_report = {}
    for cid in COURSES:
        dist = Counter(_key_rows(cid))
        key_report[cid] = {LETTERS[i]: dist.get(i, 0) for i in range(4)}
        key_report[cid]["n"] = sum(dist.values())
        extras = extra_assessment_items(cid)
        weekly_set = _weekly_stems(cid)
        exam_report[cid] = {
            "weekly_stems": len(weekly_set),
            "mid_original": sum(1 for i in extras["mid"] if i["stem"] not in weekly_set and not i["stem"].startswith(CLONE_PREFIXES)),
            "final_original": sum(1 for i in extras["final"] if i["stem"] not in weekly_set and not i["stem"].startswith(CLONE_PREFIXES)),
        }

    return {
        "schema": "waike.curriculum_provenance_audit.v1",
        "status": status,
        "BATCH_TEMPLATED_COURSES": templated,
        "BATCH_STUB_COURSES": stub,
        "worst_jaccard": round(worst, 4),
        "worst_pair": worst_pair,
        "worst_packaging_jaccard": round(worst_pack, 4),
        "worst_packaging_pair": worst_pack_pair,
        "pairs": sorted(pairs, key=lambda x: -x["jaccard_5gram"])[:8],
        "packaging_pairs": sorted(pack_pairs, key=lambda x: -x["packaging_jaccard_5gram"])[:8],
        "key_distribution": key_report,
        "key_balance_ok": key_balance_ok,
        "exam_items_original": exam_items_original,
        "exam_original_counts": exam_report,
        "registry_size": len(registry.get("sources", [])),
        "findings": findings,
        "claim_boundary": "Original WAIKE items. Restricted sources used as domain labels only.",
    }
