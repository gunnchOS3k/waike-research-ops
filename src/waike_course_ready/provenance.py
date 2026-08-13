"""Provenance + shallow-template detectors for the digital RC batch."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES

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


def audit() -> dict[str, Any]:
    findings: list[str] = []
    texts = {cid: lesson_text(cid) for cid in COURSES}
    pairs = []
    ids = list(COURSES)
    worst = 0.0
    worst_pair = None
    for i, a in enumerate(ids):
        for b in ids[i + 1 :]:
            j = jaccard(texts[a], texts[b])
            pairs.append({"a": a, "b": b, "jaccard_5gram": round(j, 4)})
            if j > worst:
                worst = j
                worst_pair = [a, b]
    if worst >= 0.35:
        findings.append(f"BATCH_TEMPLATED_COURSES: jaccard {worst:.3f} on {worst_pair}")

    for cid, text in texts.items():
        low = text.lower()
        for marker in FORBIDDEN_SUBSTRINGS + DUMP_MARKERS + GENERIC_TEMPLATE_MARKERS:
            if marker in low:
                findings.append(f"{cid} contains forbidden marker: {marker}")
        if len(text) < 8000:
            findings.append(f"{cid} lesson body too short ({len(text)} chars) — stub risk")
        # swapped-noun detector: identical sentence frames across weeks
        weeks = [w["lesson"][:80] for w in COURSES[cid]["weeks"]]
        if len(set(weeks)) < 8:
            findings.append(f"{cid} week openings not distinct")

    # Attribution present
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

    stub = 0
    templated = 1 if any("BATCH_TEMPLATED" in f for f in findings) else 0
    if any("stub risk" in f for f in findings):
        stub = 1

    status = "PASS" if not findings else "FAIL"
    return {
        "schema": "waike.curriculum_provenance_audit.v1",
        "status": status,
        "BATCH_TEMPLATED_COURSES": templated,
        "BATCH_STUB_COURSES": stub,
        "worst_jaccard": round(worst, 4),
        "worst_pair": worst_pair,
        "pairs": sorted(pairs, key=lambda x: -x["jaccard_5gram"])[:8],
        "registry_size": len(registry.get("sources", [])),
        "findings": findings,
        "claim_boundary": "Original WAIKE items. Restricted sources used as domain labels only.",
    }
