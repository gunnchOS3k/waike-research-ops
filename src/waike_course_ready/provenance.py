"""Provenance + template detectors for the digital RC batch (COURSE-READY-002 active).

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
from waike_course_ready.exams import scan_exam_restatements
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

# Depth padding the independent verifier strips before measuring ≥800.
# Include batch-003 Evidence/operator-note rubber-stamps and batch-004 Detail-mark /
# rotating trailer + Ticket-arithmetic-checkpoint spam invented to dodge those markers.
_PAD_RE = re.compile(
    r"(Operator note: record evidence before changing shared systems\.\s*)+|"
    r"(Evidence discipline week \d+: keep ticket numbers, hashes, and fixture counts "
    r"in the journal; do not replace them with adjectives\.\s*)+|"
    r"(Evidence for this week lives in the submitted lab JSON and the numbered fixture "
    r"cases\s*[—\-–-]\s*not in a screenshot of a green checkmark\.\s*)+|"
    r"(Evidence for this week lives in the submitted lab JSON[^\n]*\n*)+|"
    # Batch-004 Detail-mark / rotating trailer class
    r"(Detail mark [^\n.]*\.\s*)+|"
    r"(Operators keep a numbered ticket trail for [^\n]* and refuse noun-swapped decks "
    r"from other academies\.\s*(?:Detail mark [^\n.]*\.\s*)*)+|"
    r"(Whiteboard the worked numbers before opening any GUI; the validator grades fields, "
    r"not vibes\.\s*(?:Detail mark [^\n.]*\.\s*)*)+|"
    r"(If a volunteer asks for a certificate selfie, point them at career_mapping\.json: "
    r"aligned, not granted\.\s*(?:Detail mark [^\n.]*\.\s*)*)+|"
    r"(Keep journals free of patron faces, passwords, and fabricated impact statistics\.\s*"
    r"(?:Detail mark [^\n.]*\.\s*)*)+|"
    r"(When tools disagree, name the observation first, then the inference, then what is "
    r"still needed\.\s*(?:Detail mark [^\n.]*\.\s*)*)+|"
    r"(Runnable labs must fail empty submissions and reject a file whose entire body is "
    r"PASS\.\s*(?:Detail mark [^\n.]*\.\s*)*)+|"
    # Batch-004 Ticket-arithmetic / synonym checkpoint trailer class
    r"(Ticket arithmetic checkpoint for [^\n]*(?:\n(?!\n)[^\n]*)*)+",
    re.I,
)
_PAD_MARKERS = (
    "operator note: record evidence before changing shared systems",
    "evidence discipline week",
    "evidence for this week lives in the submitted lab json",
    "not in a screenshot of a green checkmark",
    # Batch-004 padding class — must be absent from authored bodies and stripped if present
    "detail mark",
    "operators keep a numbered ticket trail for",
    "whiteboard the worked numbers before opening any gui",
    "if a volunteer asks for a certificate selfie",
    "keep journals free of patron faces, passwords, and fabricated impact statistics",
    "when tools disagree, name the observation first, then the inference",
    "runnable labs must fail empty submissions and reject a file whose entire body is pass",
    "ticket arithmetic checkpoint",
    "restate the worked example in your own symbols",
)

# Phrases that often head synonym depth-padding trailers (defense for the next rename).
_TRAILER_HEAD_MARKERS = (
    "ticket arithmetic checkpoint",
    "detail mark",
    "operator note: record evidence",
    "evidence discipline week",
    "evidence for this week lives",
    "operators keep a numbered ticket trail",
)


def strip_lesson_padding(text: str) -> str:
    """Remove operator-note / evidence / Detail-mark / Ticket-arithmetic trailer spam."""
    cleaned = _PAD_RE.sub("", text or "")
    # Drop whole paragraphs that still carry known pad heads (synonym-resistant cleanup).
    kept_paras: list[str] = []
    for para in re.split(r"\n\s*\n", cleaned):
        low = para.lower()
        if any(m in low for m in _TRAILER_HEAD_MARKERS):
            continue
        if "detail mark" in low:
            continue
        kept_paras.append(para)
    cleaned = "\n\n".join(kept_paras)
    # Line-level Detail-mark residue
    kept: list[str] = []
    for line in cleaned.splitlines():
        if "detail mark" in line.lower():
            continue
        kept.append(line)
    cleaned = "\n".join(kept)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def _normalize_trailer_blob(text: str) -> str:
    """Normalize course/week/ticket tokens so synonym pads compare as one body."""
    t = (text or "").lower()
    t = re.sub(r"\b(wireless_6g|robotics_control|game_dev_interactive)\b", "course", t)
    t = re.sub(r"\bweek\s+\d+\b", "week n", t)
    t = re.sub(r"\bw\d{1,2}\b", "wn", t)
    t = re.sub(r"\b(?:wr|rb|ga|ef|it|nw|cy)-\d+\b", "ticket", t)
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def week_trailer_paragraph(lesson: str, min_chars: int = 180, max_chars: int = 650) -> str:
    """Last substantial paragraph (or lesson tail) used for cross-week trailer spam checks."""
    parts = [p.strip() for p in re.split(r"\n\s*\n", (lesson or "").strip()) if p.strip()]
    if not parts:
        return ""
    last = parts[-1]
    if len(last) >= min_chars:
        return last[:max_chars]
    return (lesson or "").strip()[-max_chars:]


def detect_repeated_near_identical_trailers(
    weeks: list[dict[str, Any]],
    *,
    min_hits: int = 3,
    min_chars: int = 180,
    jaccard_thresh: float = 0.85,
) -> dict[str, Any]:
    """Fail when the same near-identical trailer body repeats across weeks (any synonym class)."""
    trailers: list[tuple[int, str, str]] = []
    for w in weeks:
        raw = week_trailer_paragraph(w.get("lesson") or "", min_chars=min_chars)
        if len(raw) < min_chars:
            continue
        trailers.append((int(w.get("week") or 0), raw, _normalize_trailer_blob(raw)))

    exact_counts = Counter(n for _, _, n in trailers)
    for norm, count in exact_counts.items():
        if count >= min_hits:
            weeks_hit = [wk for wk, _, n in trailers if n == norm]
            return {
                "spam": True,
                "kind": "normalized_exact",
                "hits": count,
                "weeks": weeks_hit,
                "sample": norm[:160],
            }

    # Pairwise near-duplicates (catches light synonym edits of the same pad).
    involved: set[int] = set()
    pair_hits = 0
    for i in range(len(trailers)):
        for j in range(i + 1, len(trailers)):
            a_raw, b_raw = trailers[i][1], trailers[j][1]
            if jaccard(a_raw, b_raw) >= jaccard_thresh:
                pair_hits += 1
                involved.add(trailers[i][0])
                involved.add(trailers[j][0])
    if len(involved) >= min_hits and pair_hits >= min_hits:
        return {
            "spam": True,
            "kind": "pairwise_jaccard",
            "hits": pair_hits,
            "weeks": sorted(involved),
            "jaccard_thresh": jaccard_thresh,
        }
    return {"spam": False, "hits": 0, "weeks": []}


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

    stripped_lesson_mins: dict[str, int] = {}
    lesson_padding_rejected = 0
    repeated_trailer_findings: dict[str, Any] = {}
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

        # Raise RC depth gate: reject operator-note / evidence / Detail-mark / Ticket-arithmetic spam.
        week_stripped_lens: list[int] = []
        for w in COURSES[cid]["weeks"]:
            raw = w["lesson"]
            raw_low = raw.lower()
            if any(m in raw_low for m in _PAD_MARKERS):
                lesson_padding_rejected += 1
                findings.append(
                    f"{cid} week {w['week']} uses operator-note/evidence-discipline/"
                    f"lab-JSON-evidence/Detail-mark/Ticket-arithmetic trailer depth padding"
                )
            stripped = strip_lesson_padding(raw)
            week_stripped_lens.append(len(stripped))
            floor = (
                871
                if cid in ("WIRELESS_6G", "ROBOTICS_CONTROL", "GAME_DEV_INTERACTIVE")
                else 800
            )
            if len(stripped) < floor:
                findings.append(
                    f"{cid} week {w['week']} stripped lesson depth {len(stripped)} < {floor}"
                )
        stripped_lesson_mins[cid] = min(week_stripped_lens) if week_stripped_lens else 0

        # General cross-week near-identical trailer detector (catches the next synonym pad).
        trailer_spam = detect_repeated_near_identical_trailers(COURSES[cid]["weeks"])
        if trailer_spam.get("spam"):
            lesson_padding_rejected += int(trailer_spam.get("hits") or 1)
            findings.append(
                f"{cid} repeated near-identical lesson trailers "
                f"kind={trailer_spam.get('kind')} hits={trailer_spam.get('hits')} "
                f"weeks={trailer_spam.get('weeks')}"
            )
            repeated_trailer_findings[cid] = trailer_spam

        weekly = list(_weekly_stems(cid))
        if len(weekly) < 60:
            findings.append(f"{cid} weekly stems {len(weekly)} < 60")
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

        rest = scan_exam_restatements(cid, weekly)
        if rest["token_identical"]:
            findings.append(
                f"{cid} token-identical exam restatements={rest['token_identical']} "
                f"(ignore punctuation/?/case) e.g. {rest['hits'][0]['id'] if rest['hits'] else '?'}"
            )
        if rest["token_jaccard_ge_0_80"]:
            findings.append(
                f"{cid} exam token Jaccard≥0.80 vs weekly={rest['token_jaccard_ge_0_80']} "
                f"worst={rest['worst_token_jaccard']}"
            )

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
    exam_items_original = not any(
        " clone:" in f
        or "original items" in f
        or "token-identical" in f
        or "Jaccard≥0.80" in f
        for f in findings
    )

    status = "PASS" if not findings else "FAIL"
    key_report = {}
    exam_report = {}
    restatement_hits: list[dict[str, Any]] = []
    token_identical_total = 0
    token_j80_total = 0
    worst_exam_weekly = 0.0
    for cid in COURSES:
        dist = Counter(_key_rows(cid))
        key_report[cid] = {LETTERS[i]: dist.get(i, 0) for i in range(4)}
        key_report[cid]["n"] = sum(dist.values())
        extras = extra_assessment_items(cid)
        weekly_list = list(_weekly_stems(cid))
        weekly_set = set(weekly_list)
        rest = scan_exam_restatements(cid, weekly_list)
        token_identical_total += rest["token_identical"]
        token_j80_total += rest["token_jaccard_ge_0_80"]
        worst_exam_weekly = max(worst_exam_weekly, rest["worst_token_jaccard"])
        restatement_hits.extend({"course_id": cid, **h} for h in rest["hits"])
        exam_report[cid] = {
            "weekly_stems": len(weekly_set),
            "mid_original": sum(1 for i in extras["mid"] if i["stem"] not in weekly_set and not i["stem"].startswith(CLONE_PREFIXES)),
            "final_original": sum(1 for i in extras["final"] if i["stem"] not in weekly_set and not i["stem"].startswith(CLONE_PREFIXES)),
            "token_identical": rest["token_identical"],
            "token_jaccard_ge_0_80": rest["token_jaccard_ge_0_80"],
            "worst_token_jaccard": rest["worst_token_jaccard"],
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
        "exam_token_identical": token_identical_total,
        "exam_token_jaccard_ge_0_80": token_j80_total,
        "worst_exam_weekly_token_jaccard": round(worst_exam_weekly, 4),
        "exam_restatement_hits": restatement_hits[:20],
        "stripped_lesson_mins": stripped_lesson_mins,
        "lesson_padding_rejected": lesson_padding_rejected,
        "repeated_trailer_findings": repeated_trailer_findings,
        "registry_size": len(registry.get("sources", [])),
        "findings": findings,
        "claim_boundary": "Original WAIKE items. Restricted sources used as domain labels only.",
    }
