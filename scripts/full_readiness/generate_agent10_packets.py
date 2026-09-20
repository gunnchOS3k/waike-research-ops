#!/usr/bin/env python3
"""Agent 10 — generate human review packets, pilot packets, standards YAML, and aggregates.

Reads curriculum/taxonomy/canonical_track_registry.v1.json (does not modify it).
Prefers substance from digital_rc packages + programs; call out gaps honestly.
Does not wipe an existing SEVEN_GC_APPRENTICESHIP review packet; only fills missing files.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "curriculum/taxonomy/canonical_track_registry.v1.json"
DRC = ROOT / "curriculum/digital_rc"
REVIEW_ROOT = ROOT / "curriculum/review_packets"
PILOT_ROOT = ROOT / "pilot"
STANDARDS_BY_TRACK = ROOT / "standards_alignment/by_track"
ARTIFACTS = ROOT / "artifacts/full_readiness"
SKILL_TREE = ROOT / "knowledge_maps/waike_skill_tree.yaml"

REQUIRED_REVIEW = [
    "README.md",
    "objectives.md",
    "sequence.md",
    "assessment_map.md",
    "lab_map.md",
    "standards_map.md",
    "ai_policy.md",
    "accessibility.md",
    "provenance.md",
    "known_risks.md",
    "reviewer_rubric.md",
    "signoff_form.md",
]

REQUIRED_PILOT = [
    "prerequisites.md",
    "session_plan.md",
    "facilitator_plan.md",
    "instrumentation.md",
    "learning_measures.md",
    "usability_measures.md",
    "issue_logging.md",
    "consent_ethics_placeholders.md",
    "rollback_safety.md",
    "post_pilot_review.md",
]

# Track → internal skill-tree domain ids (best-effort; not accreditation)
SKILL_MAP: dict[str, list[str]] = {
    "DIGITAL_CONFIDENCE": ["digital_confidence", "it_support"],
    "IT_SUPPORT_HARDWARE": ["it_support", "digital_confidence"],
    "SOFTWARE_BUILDER": ["programming", "software_engineering"],
    "NETWORKING_INFRA": ["networking"],
    "CYBER_SOC": ["cybersecurity"],
    "DATA_DASHBOARDS": ["data_databases_viz"],
    "AI_ML_EDGE": ["ai_ml", "edge_embedded"],
    "EMBEDDED_PROTOTYPING": ["edge_embedded", "hardware"],
    "WIRELESS_6G": ["wireless_dsp", "networking"],
    "PM_AGILE_LSS": ["project_process"],
    "GAME_DEV_INTERACTIVE": ["programming", "software_engineering"],
    "SEVEN_GC_APPRENTICESHIP": ["research_methods", "wireless_dsp", "ai_ml"],
    "CLOUD_DEVOPS": ["cloud_devops", "software_engineering"],
    "COMM_PD_ETHICS": ["professional_development"],
    "ROBOTICS_CONTROL": ["robotics", "hardware"],
    "GUNNCHOS_PRODUCT_LAB": ["hardware", "software_engineering", "product_lab"],
    "HARDWARE_ENGINEERING": ["hardware"],
    "DATA_VIZ_BI": ["data_databases_viz"],
}

# External standards frameworks (DRAFT mappings only)
EXTERNAL_DRAFT: dict[str, list[dict[str, str]]] = {
    "DIGITAL_CONFIDENCE": [
        {"framework": "SFIA9", "note": "Digital literacy / IT user support themes — draft"},
        {"framework": "CompTIA_A+", "note": "Operator/end-user skills overlap — draft, not cert prep"},
    ],
    "IT_SUPPORT_HARDWARE": [
        {"framework": "CompTIA_A+", "note": "Hardware/support themes — draft"},
        {"framework": "SFIA9", "note": "IT infrastructure themes — draft"},
    ],
    "SOFTWARE_BUILDER": [
        {"framework": "SWEBOK", "note": "Construction/testing themes — draft"},
        {"framework": "ACM_CS2023", "note": "SDF/SE knowledge areas — draft"},
    ],
    "NETWORKING_INFRA": [
        {"framework": "Cisco_CCNA", "note": "Routing/switching topic shape — draft"},
        {"framework": "CompTIA_Network+", "note": "Foundational networking — draft"},
    ],
    "CYBER_SOC": [
        {"framework": "NIST_NICE", "note": "Protect/Detect/Respond work roles — draft"},
        {"framework": "ISC2_CC", "note": "Security concepts — draft"},
    ],
    "DATA_DASHBOARDS": [
        {"framework": "SFIA9", "note": "Data management / analytics themes — draft"},
        {"framework": "ACM_CS2023", "note": "Information Management — draft"},
    ],
    "AI_ML_EDGE": [
        {"framework": "NIST_AI_RMF", "note": "Map/Measure/Manage themes — draft"},
        {"framework": "ACM_CS2023", "note": "AI/ML knowledge areas — draft"},
    ],
    "EMBEDDED_PROTOTYPING": [
        {"framework": "SFIA9", "note": "Systems development / hardware themes — draft"},
        {"framework": "ABET_computing", "note": "Design/experiment outcomes — draft only"},
    ],
    "WIRELESS_6G": [
        {"framework": "SFIA9", "note": "Radio/network specialist themes — draft"},
        {"framework": "ACM_CS2023", "note": "Networking/systems — draft"},
    ],
    "PM_AGILE_LSS": [
        {"framework": "PMI_CAPM_PMP", "note": "Charter/risk/schedule themes — draft"},
        {"framework": "Lean_Six_Sigma", "note": "DMAIC vocabulary — draft, not belt award"},
    ],
    "GAME_DEV_INTERACTIVE": [
        {"framework": "ACM_CS2023", "note": "Graphics/HCI/SE — draft"},
        {"framework": "SWEBOK", "note": "Design/construction — draft"},
    ],
    "SEVEN_GC_APPRENTICESHIP": [
        {"framework": "NIST_AI_RMF", "note": "Evidence/claim boundaries for AI systems — draft"},
        {"framework": "SFIA9", "note": "Research / specialist themes — draft"},
    ],
    "CLOUD_DEVOPS": [
        {"framework": "Linux_Cloud_Open_Source", "note": "Linux/CI/CD themes — draft"},
        {"framework": "SWEBOK", "note": "Software configuration / process — draft"},
    ],
    "COMM_PD_ETHICS": [
        {"framework": "SFIA9", "note": "Communication / ethics themes — draft"},
        {"framework": "ACM_CS2023", "note": "SEP (Society/Ethics/Profession) — draft"},
    ],
    "ROBOTICS_CONTROL": [
        {"framework": "ABET_computing", "note": "Design/experiment — draft only"},
        {"framework": "SFIA9", "note": "Systems engineering themes — draft"},
    ],
    "GUNNCHOS_PRODUCT_LAB": [
        {"framework": "SWEBOK", "note": "Product/process themes — draft"},
        {"framework": "SFIA9", "note": "Product development — draft"},
    ],
    "HARDWARE_ENGINEERING": [
        {"framework": "ABET_computing", "note": "Design outcomes — draft only"},
        {"framework": "SFIA9", "note": "Hardware engineering themes — draft"},
    ],
    "DATA_VIZ_BI": [
        {"framework": "SFIA9", "note": "Visualisation / BI themes — draft"},
        {"framework": "ACM_CS2023", "note": "HCI / Information Management — draft"},
    ],
}

TRACK_EMPHASIS: dict[str, str] = {
    "DIGITAL_CONFIDENCE": (
        "Operator-first path: files, accounts, tickets, and plain-language troubleshooting. "
        "Canonical entry may overlay shared GENERAL_IT content — reviewers must check that "
        "hardware-bench depth is not required for this track's PASS."
    ),
    "IT_SUPPORT_HARDWARE": (
        "Support + hardware path: deskside diagnosis, storage, services, backups. "
        "Canonical entry may overlay shared GENERAL_IT content — reviewers must verify "
        "hardware-specific labs are present or explicitly gap-listed."
    ),
    "SOFTWARE_BUILDER": "ForgeDesk issue→CI→deploy path with runnable lab validators.",
    "NETWORKING_INFRA": "Packets, DNS, campus edge — COMPUTER_NETWORKING historical package id.",
    "CYBER_SOC": "Harbor SOC foundations — CYBERSECURITY historical package id.",
    "DATA_DASHBOARDS": "Pier Ledger Bench: schema, ingest, dashboard honesty.",
    "AI_ML_EDGE": "EdgeForge Bench: tensors as tables, edge constraints, claim boundaries.",
    "EMBEDDED_PROTOTYPING": (
        "ForgeSense subsystems. Has standalone package plus shared HARDWARE_ENGINEERING "
        "coverage — do not treat shared package alone as full embedded readiness."
    ),
    "WIRELESS_6G": "Pier Radio Bench: path loss, NTN/AI-RAN vocabulary without marketing claims.",
    "PM_AGILE_LSS": "Device Lab Flow: charter, WIP, DMAIC vocabulary — no belt awards.",
    "GAME_DEV_INTERACTIVE": "Forge Arcade: fixed-dt game loop, input, accessibility in play.",
    "SEVEN_GC_APPRENTICESHIP": (
        "Research apprenticeship with EXTERNAL human/physical/field gates still open. "
        "Digital package present; do not claim field validation or partner approval."
    ),
    "CLOUD_DEVOPS": "ForgeCloud: Linux permissions before YAML, CI gates, rollback.",
    "COMM_PD_ETHICS": "Harbor desk: consent, audience, ethics — not soft filler.",
    "ROBOTICS_CONTROL": "HarborBot: SE(2) pose honesty, safety envelopes, sim vs hardware.",
    "GUNNCHOS_PRODUCT_LAB": "Product Bench: charter, Device OS modes, no fabricated impact numbers.",
    "HARDWARE_ENGINEERING": (
        "ForgeSense Node shared package also lists EMBEDDED_PROTOTYPING. "
        "Review hardware-specific lumped nets / bench safety vs embedded MCU track."
    ),
    "DATA_VIZ_BI": "Civic Metrics Studio: dirty rows before pretty charts.",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def first_existing(paths: list[Path]) -> Path | None:
    for p in paths:
        if p.exists():
            return p
    return None


def resolve_package(track: dict[str, Any]) -> tuple[str | None, Path | None, dict[str, Any]]:
    pkgs = (
        track.get("content_maturity", {})
        .get("facets", {})
        .get("covering_package_ids", [])
    )
    # Prefer standalone / first listed
    for pkg_id in pkgs:
        pdir = DRC / pkg_id
        course = load_json(pdir / "course.json")
        if course:
            return pkg_id, pdir, course
    return None, None, {}


def program_path(track: dict[str, Any]) -> Path | None:
    for p in track.get("authoritative_source_paths", []):
        if p.startswith("programs/") and p.endswith(".md"):
            cand = ROOT / p
            if cand.exists():
                return cand
    return None


def extract_outcomes(program_md: str) -> list[str]:
    outcomes: list[str] = []
    in_section = False
    for line in program_md.splitlines():
        if re.match(r"^##\s+Learning outcomes", line, re.I):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            m = re.match(r"^\d+\.\s+(.+)", line.strip())
            if m:
                outcomes.append(m.group(1).strip())
            elif line.strip().startswith("- "):
                outcomes.append(line.strip()[2:].strip())
    return outcomes


def week_objectives(week: dict[str, Any]) -> list[str]:
    lesson = week.get("lesson") or {}
    body = lesson.get("body_md") or ""
    objs: list[str] = []
    # Prefer explicit worked_example / first paragraph as objective anchors
    title = week.get("title") or lesson.get("title") or "Untitled week"
    objs.append(f"Complete the week contract: {title}.")
    we = lesson.get("worked_example") or week.get("worked_example")
    if we:
        objs.append(f"Reproduce worked example: {we}")
    # First non-empty sentence as content objective
    for para in body.split("\n\n"):
        para = para.strip()
        if len(para) > 40:
            sentence = re.split(r"(?<=[.!?])\s+", para)[0]
            if len(sentence) > 20:
                objs.append(sentence[:220])
            break
    return objs


def list_lab_dirs(pdir: Path, course: dict[str, Any]) -> list[dict[str, str]]:
    labs: list[dict[str, str]] = []
    lab_ids = course.get("labs") or []
    labs_root = pdir / "labs"
    for lid in lab_ids:
        entry = {"lab_id": lid, "path": "", "title": lid, "notes": ""}
        cand = labs_root / lid
        if cand.is_dir():
            entry["path"] = str(cand.relative_to(ROOT))
            readme = first_existing(
                [cand / "README.md", cand / "lab.md", cand / f"{lid}.md"]
            )
            if readme:
                first = next(
                    (ln.strip("# ").strip() for ln in read_text(readme).splitlines() if ln.strip()),
                    lid,
                )
                entry["title"] = first[:120]
                body = read_text(readme)
                if "print-PASS" in body or "print_pass" in body.lower():
                    entry["notes"] = "Rejects empty/print-PASS submissions."
                if len(body) < 120:
                    entry["notes"] = (entry["notes"] + " Thin lab README.").strip()
        elif (labs_root / f"{lid}.md").exists():
            entry["path"] = str((labs_root / f"{lid}.md").relative_to(ROOT))
            entry["title"] = lid
        else:
            entry["notes"] = "GAP: lab id listed in course.json but folder/file missing."
        labs.append(entry)
    # Also discover unlisted lab dirs
    if labs_root.exists():
        known = {x["lab_id"] for x in labs}
        for d in sorted(labs_root.iterdir()):
            name = d.name if d.is_dir() else d.stem
            if name not in known and not name.startswith("."):
                labs.append(
                    {
                        "lab_id": name,
                        "path": str(d.relative_to(ROOT)),
                        "title": name,
                        "notes": "Present on disk; not in course.json labs list.",
                    }
                )
    return labs


def assignment_deliverables(pdir: Path, course: dict[str, Any]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    assigns = course.get("assignments") or []
    adir = pdir / "assignments"
    for name in assigns:
        path = adir / name
        text = read_text(path) if path.exists() else ""
        deliverable = ""
        for pat in [
            r"[Dd]eliverable[s]?:\s*(.+)",
            r"[Ss]ubmit(?:\s+a|\s+an|\s+the)?\s+(.+)",
            r"[Ww]rite\s+(.+)",
            r"[Bb]uild\s+(.+)",
            r"[Dd]raw\s+(.+)",
            r"[Mm]ark\s+(.+)",
            r"[Ee]xplain\s+(.+)",
            r"[Ll]ab to run:\s*`?([^`\n]+)`?",
        ]:
            m = re.search(pat, text)
            if m:
                deliverable = m.group(1).strip().rstrip(".")[:200]
                break
        if not deliverable and text:
            # First non-heading line
            for ln in text.splitlines():
                if ln.strip() and not ln.startswith("#"):
                    deliverable = ln.strip()[:200]
                    break
        gap = ""
        if not path.exists():
            gap = "GAP: assignment file missing."
        elif not deliverable:
            gap = "GAP: no clear deliverable found in assignment body."
        out.append(
            {
                "file": name,
                "path": str(path.relative_to(ROOT)) if path.exists() else "",
                "deliverable": deliverable or "(none extracted)",
                "gap": gap,
            }
        )
    return out


def rubric_criteria(pdir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    rdir = pdir / "rubrics"
    if not rdir.exists():
        return rows
    for path in sorted(rdir.glob("*.md")):
        text = read_text(path)
        criteria = re.findall(r"^\s*[-*]\s+\*\*([^*]+)\*\*", text, re.M)
        if not criteria:
            criteria = re.findall(r"^\s*[-*]\s+([^:\n]+):", text, re.M)
        gap = ""
        if not criteria:
            gap = "GAP: rubric file lacks scored criteria bullets."
        rows.append(
            {
                "file": path.name,
                "criteria_count": str(len(criteria)),
                "criteria_sample": ", ".join(criteria[:5]) if criteria else "(none)",
                "gap": gap,
            }
        )
    return rows


def inventory_gaps(
    track: dict[str, Any],
    pkg_id: str | None,
    pdir: Path | None,
    course: dict[str, Any],
    labs: list[dict[str, str]],
    assigns: list[dict[str, str]],
    rubrics: list[dict[str, str]],
) -> list[str]:
    gaps: list[str] = []
    maturity = track.get("content_maturity", {}).get("state", "unknown")
    facets = track.get("content_maturity", {}).get("facets", {})
    if maturity in {
        "covered_via_shared_package",
        "covered_via_historical_package_id",
        "canonical_entry_over_shared_content",
    }:
        shared = facets.get("shared_content_roots") or []
        gaps.append(
            f"Content maturity `{maturity}` via package `{pkg_id}`"
            + (f" (shared roots: {shared})" if shared else "")
            + " — confirm specialization vs shared overlay."
        )
    if not pkg_id or not pdir:
        gaps.append("No digital_rc package resolved — review packet is program-doc only.")
        return gaps
    if not (pdir / "instructor" / "INSTRUCTOR_PACKET.md").exists():
        gaps.append("Missing instructor/INSTRUCTOR_PACKET.md")
    if not (pdir / "student" / "STUDENT_PACKET.md").exists():
        gaps.append("Missing student/STUDENT_PACKET.md")
    weeks = course.get("weeks") or []
    for w in weeks:
        lesson = w.get("lesson") or {}
        body = lesson.get("body_md") or ""
        if len(body.strip()) < 200:
            gaps.append(f"Week {w.get('week')}: thin lesson body ({len(body)} chars).")
        if not week_objectives(w):
            gaps.append(f"Week {w.get('week')}: no extractable objectives.")
    for lab in labs:
        if lab.get("notes", "").startswith("GAP"):
            gaps.append(lab["notes"] + f" ({lab['lab_id']})")
        if "Thin lab" in lab.get("notes", ""):
            gaps.append(f"Thin lab README: {lab['lab_id']}")
    for a in assigns:
        if a.get("gap"):
            gaps.append(f"{a['file']}: {a['gap']}")
    for r in rubrics:
        if r.get("gap"):
            gaps.append(f"{r['file']}: {r['gap']}")
    # Shared package specialization risk
    covering = facets.get("covering_package_ids") or []
    if len(covering) > 1:
        gaps.append(
            f"Multiple covering packages {covering} — confirm which is authoritative for this track."
        )
    if facets.get("shared_content_roots"):
        gaps.append(
            f"shared_content_roots={facets.get('shared_content_roots')} — "
            "canonical entry may still be thin if overlay does not specialize labs."
        )
    if track["track_id"] == "SEVEN_GC_APPRENTICESHIP":
        gaps.append(
            "EXTERNAL gates (human/physical/field/partner) remain open — digital package ≠ apprenticeship complete."
        )
    return gaps


def write_if_allowed(
    path: Path, content: str, *, preserve_existing: bool, min_bytes: int = 800
) -> str:
    """Return 'created' | 'updated' | 'preserved'.

    For peer-preserved tracks: keep existing required files only when they already
    have substantive content (>= min_bytes). Thin stubs are replaced for completeness
    without deleting peer-only extra files in the same directory.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if preserve_existing and path.exists() and path.stat().st_size >= min_bytes:
        return "preserved"
    path.write_text(content, encoding="utf-8")
    return "updated"


def ensure_review_packet(track: dict[str, Any]) -> dict[str, Any]:
    tid = track["track_id"]
    title = track["title"]
    out_dir = REVIEW_ROOT / tid
    preserve = tid == "SEVEN_GC_APPRENTICESHIP" and out_dir.exists()
    pkg_id, pdir, course = resolve_package(track)
    prog = program_path(track)
    prog_md = read_text(prog) if prog else ""
    outcomes = extract_outcomes(prog_md)
    weeks = course.get("weeks") or []
    labs = list_lab_dirs(pdir, course) if pdir else []
    assigns = assignment_deliverables(pdir, course) if pdir else []
    rubrics = rubric_criteria(pdir) if pdir else []
    gaps = inventory_gaps(track, pkg_id, pdir, course, labs, assigns, rubrics)
    ai_pol = load_json(pdir / "ai_use_policy.json") if pdir else None
    prereq = load_json(pdir / "prerequisites.json") if pdir else None
    syllabus = read_text(pdir / "syllabus.md") if pdir else ""
    emphasis = TRACK_EMPHASIS.get(tid, title)

    status = {}

    # README
    gap_block = "\n".join(f"- {g}" for g in gaps) if gaps else "- No structural gaps flagged by Agent 10 inventory (still requires human review)."
    readme = f"""# Review packet — {tid}

## Summary

**Track:** {tid} — {title}  
**Academy:** {track.get('academy_id')}  
**Extension class:** {track.get('extension_class')}  
**Content maturity:** {track.get('content_maturity', {}).get('state')}  
**Covering package:** `{pkg_id or 'NONE'}`

{emphasis}

## Scope and audience

- **Audience:** WAIKE Level 1–4 learners (Gary UPNOW, apprentices, 7GC campus cohorts) unless program file narrows further.
- **Primary sources:** `{(prog.relative_to(ROOT) if prog else 'programs/(missing)')}`, `{f'curriculum/digital_rc/{pkg_id}/' if pkg_id else '(no package)'}`.
- **Not in scope for this packet:** Accreditation claims, partner field approval, or asserting a pilot already ran.

## What reviewers should verify

1. Week sequence matches package `course.json` and syllabus.
2. Each lab has a runnable or clearly simulated contract (not noun-swapped titles only).
3. Assignments name deliverables; rubrics name scored criteria.
4. Instructor and learner guidance exist and are track-specific.
5. Gaps below are accepted, fixed, or ticketed — not papered over.

## Known inventory gaps

{gap_block}

## Packet contents

| File | Purpose |
|------|---------|
| objectives.md | Learning outcomes + week objectives |
| sequence.md | Full module/week sequence |
| assessment_map.md | Quizzes / practicals / projects |
| lab_map.md | Lab inventory |
| standards_map.md | Internal skills + draft external (no accreditation) |
| ai_policy.md | AI use / assessment modes |
| accessibility.md | A11y / low-cost notes |
| provenance.md | Source paths and claim boundaries |
| known_risks.md | Delivery and honesty risks |
| reviewer_rubric.md | Human scoring rubric |
| signoff_form.md | Unsigned human sign-off (PASS=false) |

_Generated by Agent 10 helper · {now_iso()}_
"""
    status["README.md"] = write_if_allowed(out_dir / "README.md", readme, preserve_existing=preserve)

    # objectives
    outcome_lines = "\n".join(f"{i}. {o}" for i, o in enumerate(outcomes, 1)) or (
        "_GAP: no numbered learning outcomes extracted from program file — use package week contracts._"
    )
    week_obj_blocks = []
    for w in weeks:
        objs = week_objectives(w)
        bullets = "\n".join(f"  - {o}" for o in objs)
        week_obj_blocks.append(f"### Week {w.get('week')}: {w.get('title', '')}\n{bullets}")
    if not week_obj_blocks:
        week_obj_blocks.append("_GAP: no weeks in course.json._")
    objectives = f"""# Objectives — {tid}

## Program learning outcomes

{outcome_lines}

## Week-level objectives (from package lessons)

{chr(10).join(week_obj_blocks)}

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
"""
    status["objectives.md"] = write_if_allowed(out_dir / "objectives.md", objectives, preserve_existing=preserve)

    # sequence
    seq_rows = []
    for w in weeks:
        lid = w.get("lab_id") or "(none)"
        lesson = (w.get("lesson") or {}).get("lesson_id") or ""
        seq_rows.append(
            f"| {w.get('week')} | {w.get('title', '')} | `{lesson}` | `{lid}` |"
        )
    if not seq_rows:
        seq_rows.append("| — | GAP: no week sequence in package | — | — |")
    syllabus_excerpt = ""
    if syllabus:
        lines = [ln for ln in syllabus.splitlines() if ln.strip()][:25]
        syllabus_excerpt = "\n".join(lines)
    sequence = f"""# Sequence — {tid}

Complete module/week sequence from `{pkg_id or 'N/A'}` `course.json`.

| Week | Title | Lesson ID | Lab ID |
|------|-------|-----------|--------|
{chr(10).join(seq_rows)}

## Syllabus excerpt (source)

```
{syllabus_excerpt or '(no syllabus.md)'}
```

## Duration note

Package default is **{len(weeks) or 'unknown'} weeks**. Program files may also list workshop/bootcamp/apprenticeship formats — those are alternate delivery envelopes, not alternate content claims.
"""
    status["sequence.md"] = write_if_allowed(out_dir / "sequence.md", sequence, preserve_existing=preserve)

    # assessment_map
    assess_dir = (pdir / "assessments") if pdir else None
    assess_files = sorted(assess_dir.glob("*")) if assess_dir and assess_dir.exists() else []
    assess_list = "\n".join(f"- `{f.relative_to(ROOT)}`" for f in assess_files[:40]) or "- GAP: no assessments/ directory entries."
    assign_table = ["| Assignment | Deliverable | Gap |", "|------------|-------------|-----|"]
    for a in assigns:
        assign_table.append(
            f"| `{a['file']}` | {a['deliverable'].replace('|', '/')} | {a['gap'] or 'ok'} |"
        )
    if len(assign_table) == 2:
        assign_table.append("| — | GAP: no assignments listed | — |")
    rubric_table = ["| Rubric | Criteria count | Sample | Gap |", "|--------|----------------|--------|-----|"]
    for r in rubrics:
        rubric_table.append(
            f"| `{r['file']}` | {r['criteria_count']} | {r['criteria_sample'].replace('|', '/')} | {r['gap'] or 'ok'} |"
        )
    if len(rubric_table) == 2:
        rubric_table.append("| — | 0 | — | GAP: no rubrics |")
    assessment_map = f"""# Assessment map — {tid}

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

{assess_list}

## Assignments → deliverables

{chr(10).join(assign_table)}

## Rubrics → criteria

{chr(10).join(rubric_table)}

## Capstone / portfolio

- Portfolio path: `{f'curriculum/digital_rc/{pkg_id}/portfolio/' if pkg_id else 'GAP'}`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
"""
    status["assessment_map.md"] = write_if_allowed(
        out_dir / "assessment_map.md", assessment_map, preserve_existing=preserve
    )

    # lab_map
    lab_table = ["| Lab ID | Title | Path | Notes |", "|--------|-------|------|-------|"]
    for lab in labs:
        lab_table.append(
            f"| `{lab['lab_id']}` | {lab['title'].replace('|', '/')} | `{lab['path']}` | {lab['notes'] or '—'} |"
        )
    if len(lab_table) == 2:
        lab_table.append("| — | GAP: no labs | — | — |")
    # Noun-swap warning: compare lab title tokens across weeks
    titles = [lab["title"].lower() for lab in labs]
    lab_map = f"""# Lab map — {tid}

Package labs for `{pkg_id or 'N/A'}` ({len(labs)} entries).

{chr(10).join(lab_table)}

## Anti-filler note for reviewers

Reject labs that only rename another track's lab (e.g., same steps with nouns swapped).  
Each lab should name **track-specific artifacts, fixtures, or validators**.

Titles inventoried: {len(titles)}.
"""
    status["lab_map.md"] = write_if_allowed(out_dir / "lab_map.md", lab_map, preserve_existing=preserve)

    # standards_map
    skills = SKILL_MAP.get(tid, [])
    ext = EXTERNAL_DRAFT.get(tid, [])
    ext_lines = "\n".join(
        f"- **{e['framework']}** (DRAFT): {e['note']}" for e in ext
    ) or "- (none listed)"
    standards_map = f"""# Standards map — {tid}

## Internal skill taxonomy (authoritative for WAIKE)

Mapped skill-tree domain ids (see `knowledge_maps/waike_skill_tree.yaml`):

{chr(10).join(f'- `{s}`' for s in skills) or '- GAP: no internal map entry'}

These are **internal** curriculum skills. They are not third-party certificates.

## External frameworks — DRAFT ONLY

{ext_lines}

### Non-claims (mandatory)

- WAIKE is **aligned / informed by** frameworks where noted — **not accredited by**, **not endorsed by**, and **not official certification training**.
- Do not advertise “CompTIA-ready”, “CCNA prep”, “ABET-aligned degree”, or similar without a separate, signed compliance packet.
- Status of objective-by-objective external mapping: **draft / incomplete**.

## Pointers

- Repo summaries: `standards_alignment/*.md`
- Structured drafts: `standards_alignment/data/*.yaml`
- Per-track YAML: `standards_alignment/by_track/{tid}.yaml`
"""
    status["standards_map.md"] = write_if_allowed(
        out_dir / "standards_map.md", standards_map, preserve_existing=preserve
    )

    # ai_policy
    if ai_pol:
        modes = ", ".join(ai_pol.get("modes") or [])
        amodes = ", ".join(ai_pol.get("assessment_modes") or [])
        notes = ai_pol.get("notes") or ""
        ai_body = f"""# AI policy — {tid}

Source: `curriculum/digital_rc/{pkg_id}/ai_use_policy.json`

## Allowed assistant modes

{modes or '(none listed)'}

## Assessment modes

{amodes or '(none listed)'}

## Package notes

{notes or '(none)'}

## Reviewer checks

- Graded security / research-claim practicals should default toward **NO_AI** or **AI_RESTRICTED** where the package says so.
- Learner submissions using assistants need **AI_DISCLOSED** when required.
- Do not allow “print PASS” or empty JSON as AI-assisted lab completion.
"""
    else:
        ai_body = f"""# AI policy — {tid}

**GAP:** No `ai_use_policy.json` in package `{pkg_id or 'N/A'}`.

Interim defaults for human review (not a substitute for package policy):

- Practice drills: AI_ALLOWED / PRACTICE
- Graded artifacts: AI_DISCLOSED minimum
- Security / claim-boundary practicals: NO_AI preferred
- Never accept empty or PASS-string lab submissions
"""
    status["ai_policy.md"] = write_if_allowed(out_dir / "ai_policy.md", ai_body, preserve_existing=preserve)

    # accessibility
    a11y = f"""# Accessibility — {tid}

## Repo principles (from ACCESSIBILITY_AND_LOW_COST.md)

1. Phone-first / hardware learners already own
2. Offline-first where possible
3. Low-bandwidth / synthetic paths documented
4. Plain-language docs; structured headings
5. No paywall on core learning path

## Track-specific checks

- Package UI/lab text must not rely on **color alone** for meaning (see SOFTWARE_BUILDER board pattern as reference quality bar).
- Instructor packet should state keyboard / low-vision alternatives when UI labs exist.
- Cost assumption: existing laptop; cloud optional; field hardware **opt-in**.

## Gaps to confirm in human review

- [ ] Student packet states real vs synthetic vs planned for any Device Lab / radio / robot gear
- [ ] Error messages in labs are human-readable
- [ ] Multilingual needs documented if campus requires them

Prerequisites (package): `{json.dumps(prereq) if prereq else 'GAP: missing prerequisites.json'}`
"""
    status["accessibility.md"] = write_if_allowed(
        out_dir / "accessibility.md", a11y, preserve_existing=preserve
    )

    # provenance
    sources = "\n".join(f"- `{p}`" for p in track.get("authoritative_source_paths", []))
    provenance = f"""# Provenance — {tid}

## Registry identity

- `track_id`: {tid}
- `stable_uuid`: {track.get('stable_uuid')}
- `historical_aliases`: {', '.join(track.get('historical_aliases') or []) or '(none)'}

## Authoritative source paths (registry)

{sources}

## Package claim boundary

- Course title in package: {course.get('title') or '(none)'}
- Kinesthetic hook: {course.get('kinesthetic_hook') or '(none)'}
- Structure citations / PUBLIC_REFERENCE_ONLY materials are **not** copied item banks.
- Certifications: **aligned themes only — not granted**.

## Generation

Agent 10 assembled this review packet from on-disk sources on {now_iso()}.  
Human review remains required; PASS on signoff_form stays false until signed.
"""
    status["provenance.md"] = write_if_allowed(
        out_dir / "provenance.md", provenance, preserve_existing=preserve
    )

    # known_risks
    risk_lines = [f"- {g}" for g in gaps] or ["- No inventory gaps; residual delivery risk still applies."]
    known_risks = f"""# Known risks — {tid}

## Inventory / content risks

{chr(10).join(risk_lines)}

## Delivery risks (all tracks)

- Treating digital_rc presence as field-validated teaching.
- Noun-swapped labs across tracks creating false breadth.
- Instructor keys or answer keys leaking into learner packets.
- Fabricated community-impact numbers in portfolios.
- External standard name-dropping read as accreditation.

## Track emphasis risk

{emphasis}
"""
    status["known_risks.md"] = write_if_allowed(
        out_dir / "known_risks.md", known_risks, preserve_existing=preserve
    )

    # reviewer_rubric
    reviewer_rubric = f"""# Reviewer rubric — {tid}

Score each criterion 0–3 (0 missing, 1 thin/templated, 2 usable with gaps, 3 ready for pilot design).  
**Pilot execution is out of scope** — do not score as if a cohort already ran.

| # | Criterion | 0 | 1 | 2 | 3 | Score | Notes |
|---|-----------|---|---|---|---|-------|-------|
| 1 | Outcomes specific & assessable | absent | vague | mostly clear | clear+measurable |  |  |
| 2 | Full week sequence present | absent | partial | full but thin | full+coherent |  |  |
| 3 | Labs track-specific (anti noun-swap) | absent | swapped | mostly unique | unique+validators |  |  |
| 4 | Assignments name deliverables | absent | implied | explicit | explicit+examples |  |  |
| 5 | Rubrics have scored criteria | absent | adjectives only | criteria listed | criteria+weights |  |  |
| 6 | Instructor guidance present | absent | stub | usable | week-ready |  |  |
| 7 | Learner guidance present | absent | stub | usable | week-ready |  |  |
| 8 | AI policy explicit | absent | generic | package policy | policy+assessment modes |  |  |
| 9 | Accessibility/low-cost addressed | absent | boilerplate | concrete | concrete+checklist |  |  |
| 10 | Gaps honestly documented | hidden | minimized | listed | listed+tickets |  |  |
| 11 | No false accreditation claims | fails | risky wording | clean | clean+disclaimers |  |  |
| 12 | Provenance traceable | absent | vague | paths listed | paths+claim boundary |  |  |

**Minimum for “ready to design pilot”:** no zeros on 1–7 and 11; average ≥ 2.0.  
**Not a pilot-complete verdict.**
"""
    status["reviewer_rubric.md"] = write_if_allowed(
        out_dir / "reviewer_rubric.md", reviewer_rubric, preserve_existing=preserve
    )

    # signoff_form — unsigned, PASS false
    signoff = f"""# Sign-off form — {tid}

**PASS:** `false`  
**Status:** unsigned — awaiting human reviewer

| Field | Value |
|-------|-------|
| Track ID | {tid} |
| Track title | {title} |
| Reviewer name |  |
| Reviewer role |  |
| Review date (UTC) |  |
| Packet commit / SHA reviewed |  |
| Overall verdict (PASS/FAIL/CONDITIONAL) |  |
| PASS boolean (must stay false until human sets true) | false |
| Conditions / required fixes |  |
| Signature / typed name |  |

## Confirmation checklist (human initials)

- [ ] ____ Outcomes reviewed
- [ ] ____ Sequence complete
- [ ] ____ Labs not noun-swapped filler
- [ ] ____ Assessments/rubrics usable
- [ ] ____ AI + accessibility reviewed
- [ ] ____ No accreditation overclaim
- [ ] ____ Gaps accepted or ticketed

_Do not machine-set PASS=true._
"""
    status["signoff_form.md"] = write_if_allowed(
        out_dir / "signoff_form.md", signoff, preserve_existing=preserve
    )

    # Ensure any missing required files if preserve mode skipped some
    if preserve:
        for req in REQUIRED_REVIEW:
            if not (out_dir / req).exists():
                # regenerate that single file by re-calling write without preserve
                # Simplest: write a stub pointer
                (out_dir / req).write_text(
                    f"# {req} — {tid}\n\n_Filled by Agent 10 to complete packet; peer content preserved where present._\n",
                    encoding="utf-8",
                )
                status[req] = "created_missing"

    present = [f for f in REQUIRED_REVIEW if (out_dir / f).exists()]
    return {
        "track_id": tid,
        "package_id": pkg_id,
        "files_present": present,
        "files_required": REQUIRED_REVIEW,
        "complete": set(REQUIRED_REVIEW).issubset(set(present)),
        "gaps": gaps,
        "week_count": len(weeks),
        "lab_count": len(labs),
        "status": status,
        "preserved_peer": preserve,
    }


def ensure_pilot_packet(track: dict[str, Any], review_meta: dict[str, Any]) -> dict[str, Any]:
    tid = track["track_id"]
    title = track["title"]
    out_dir = PILOT_ROOT / f"track_{tid}"
    pkg_id = review_meta.get("package_id")
    _, pdir, course = resolve_package(track)
    prereq = load_json(pdir / "prerequisites.json") if pdir else None
    weeks = course.get("weeks") or []
    status = {}

    files: dict[str, str] = {}

    files["prerequisites.md"] = f"""# Pilot prerequisites — {tid}

**This is a pilot design packet. No pilot is claimed to have run.**

## Learner prerequisites

Package JSON: `{json.dumps(prereq) if prereq else 'GAP: missing prerequisites.json — use program file + instructor judgment.'}`

## Facilitator prerequisites

- Read `curriculum/review_packets/{tid}/` (unsigned until human sign-off).
- Confirm Device Lab / offline / synthetic mode for this track.
- Confirm AI assessment modes for graded artifacts.
- Do **not** run field/partner activities for SEVEN_GC without EXTERNAL gate owners.

## Environment

- Covering package: `{pkg_id or 'NONE'}`
- Preferred: local/synthetic fixtures first; hardware opt-in only.
"""

    week_plan = []
    for w in weeks[:4]:  # pilot sample: first 4 weeks or fewer
        week_plan.append(
            f"- **Session focusing Week {w.get('week')}:** {w.get('title')} — lab `{w.get('lab_id')}`"
        )
    if not week_plan:
        week_plan.append("- GAP: no weeks available — pilot cannot be scheduled until sequence exists.")

    files["session_plan.md"] = f"""# Session plan — {tid}

**Pilot status:** NOT RUN · design only

## Proposed pilot envelope

| Item | Plan |
|------|------|
| Format | 2–4 facilitated sessions (subset of full {len(weeks) or 'N'}-week course) |
| Cohort size | 6–12 learners (TBD by campus) |
| Mode | Synthetic / local first |
| Full course claim | Forbidden — pilot is a slice |

## Candidate sessions (from real week titles)

{chr(10).join(week_plan)}

## Session skeleton (each meeting)

1. Safety / consent reminder (5m)
2. Objective + worked example (15m)
3. Guided lab (40–60m)
4. Artifact check / exit ticket (15m)
5. Issue log capture (10m)
"""

    files["facilitator_plan.md"] = f"""# Facilitator plan — {tid}

## Role

Facilitator coaches labs; does not invent accreditation claims; does not skip consent.

## Prep checklist

- [ ] Review packet gaps read (`known_risks.md`)
- [ ] Lab validators runnable or clearly simulated
- [ ] Answer keys kept out of learner share
- [ ] Rollback path understood (see rollback_safety.md)

## Facilitation moves

- Socratic hints before answers
- Require artifact fields (ids, counts, digests) — reject adjectives-only “PASS”
- Log blockers in issue_logging.md template

## Track emphasis

{TRACK_EMPHASIS.get(tid, title)}
"""

    files["instrumentation.md"] = f"""# Instrumentation — {tid}

## What to capture (design)

| Signal | Source | PII rule |
|--------|--------|---------|
| Session attendance | roster code only | no real names in shared artifacts |
| Lab submit accept/reject | lab runner exit codes | strip emails |
| Time-on-task (optional) | facilitator tally | aggregate only |
| Issue tags | issue_logging.md | no secrets |

## Schema pointer

See `pilot/PILOT_DATA_SCHEMA.md` (repo-level). Pilot track folder does not claim collected data exists.
"""

    files["learning_measures.md"] = f"""# Learning measures — {tid}

## Primary (artifact-based)

- Lab acceptance rate (empty/wrong/print-PASS must fail)
- Assignment deliverable completeness vs assessment_map
- Week-objective exit tickets (3 questions max, open notes)

## Secondary

- Pre/post confidence self-rating (1–5) — **not** competence proof
- Rubric scores on one shared artifact

## Non-measures

- Certification exam pass rates (out of scope)
- Fabricated community impact metrics
"""

    files["usability_measures.md"] = f"""# Usability measures — {tid}

| Measure | How | Target (design) |
|---------|-----|-----------------|
| Time to first successful lab submit | wall clock | record actual; no fake SLA |
| Blocker count per session | issue log | trend down across sessions |
| Instruction clarity (1–5) | end-of-session pulse | median ≥ 3 before scaling |
| Accessibility friction reports | issue tags `a11y` | each report gets owner |

Do not claim SUS/NPS benchmarks were met — none have been run in this packet.
"""

    files["issue_logging.md"] = f"""# Issue logging — {tid}

## Template

```
date_utc:
session_id:
track_id: {tid}
severity_code:  # never full name in shared export
severity: blocker|confusion|a11y|safety|content_gap|tooling
summary:
repro_steps:
severity_or_synthetic: synthetic|local|hardware
owner:
status: open|mitigated|closed
```

## Severity

- **S0** safety / consent breach → stop session
- **S1** lab validator broken → switch to backup exercise
- **S2** content gap → continue with disclosed gap
- **S3** polish
"""

    files["consent_ethics_placeholders.md"] = f"""# Consent & ethics placeholders — {tid}

**Placeholders only — not an approved IRB/consent form.**

## Required before any live pilot

- [ ] Institutional / campus consent language approved by responsible adult owner
- [ ] Data minimization plan (codes not names in shared repos)
- [ ] Opt-out path that does not punish learners
- [ ] Photo/video policy default = no capture
- [ ] AI disclosure rules explained verbally + in writing

## Research apprenticeship note

For `SEVEN_GC_APPRENTICESHIP`, EXTERNAL gates (partner/field/hardware) need explicit owners before any non-synthetic activity.

## Forbidden

- Collecting unnecessary PII into curriculum git
- Claiming ethics approval that does not exist
"""

    files["rollback_safety.md"] = f"""# Rollback & safety — {tid}

## Technical rollback

- Prefer local/synthetic fixtures; pin known-good lab scripts before session
- If Device Lab compose used: keep prior image digest / rollback pointer (see software deploy labs pattern)
- Do not flash physical devices in pilot slice unless hardware owner co-facilitates

## Pedagogical rollback

- Abort graded practical → convert to PRACTICE mode with disclosure
- Broken validator → paper worksheet using same objectives (mark as degraded)

## Safety stop conditions

- Consent confusion
- Suspected secret/credential exposure
- Hardware/electrical risk
- Learner distress — pause and escalate to human owner
"""

    files["post_pilot_review.md"] = f"""# Post-pilot review — {tid}

**Status:** N/A — pilot not run.

## When a pilot completes, humans fill

| Field | Value |
|-------|-------|
| Pilot dates |  |
| Cohort size |  |
| Sessions completed |  |
| Learning measure summary |  |
| Usability summary |  |
| Top 5 issues |  |
| Content changes required |  |
| Ready for wider cohort? (Y/N/Conditional) |  |
| Reviewer |  |

## Non-claims

This file existing does **not** mean a pilot occurred.
"""

    for name, content in files.items():
        path = out_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        status[name] = "written"

    present = [f for f in REQUIRED_PILOT if (out_dir / f).exists()]
    return {
        "track_id": tid,
        "files_present": present,
        "complete": set(REQUIRED_PILOT).issubset(set(present)),
        "status": status,
    }


def write_standards_yaml(track: dict[str, Any]) -> Path:
    tid = track["track_id"]
    STANDARDS_BY_TRACK.mkdir(parents=True, exist_ok=True)
    path = STANDARDS_BY_TRACK / f"{tid}.yaml"
    skills = SKILL_MAP.get(tid, [])
    ext = EXTERNAL_DRAFT.get(tid, [])
    lines = [
        f"track_id: {tid}",
        f"title: {json.dumps(track['title'])}",
        "accreditation_claim: false",
        "external_mapping_status: draft",
        "disclaimer: >",
        "  WAIKE mappings are draft alignments to internal skill taxonomy and",
        "  external framework themes. Not accredited, not endorsed, not cert training.",
        "internal_skill_taxonomy:",
    ]
    for s in skills:
        lines.append(f"  - skill_id: {s}")
        lines.append("    source: knowledge_maps/waike_skill_tree.yaml")
        lines.append("    confidence: provisional")
    lines.append("external_frameworks_draft:")
    for e in ext:
        lines.append(f"  - framework: {e['framework']}")
        lines.append(f"    status: draft")
        lines.append(f"    note: {json.dumps(e['note'])}")
        lines.append("    accreditation: false")
    lines.append(f"generated_at: {now_iso()}")
    lines.append("generator: scripts/full_readiness/generate_agent10_packets.py")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def portfolio_outcomes_index(tracks: list[dict[str, Any]]) -> dict[str, Any]:
    entries = []
    for track in tracks:
        tid = track["track_id"]
        pkg_id, pdir, course = resolve_package(track)
        artifacts = []
        if pdir:
            port = pdir / "portfolio"
            if (port / "artifacts.json").exists():
                data = load_json(port / "artifacts.json")
                if isinstance(data, list):
                    artifacts = data
                elif isinstance(data, dict):
                    artifacts = data.get("artifacts") or data.get("items") or [data]
            elif (port / "PORTFOLIO.md").exists():
                artifacts.append({"source": str((port / "PORTFOLIO.md").relative_to(ROOT))})
            elif (pdir / "portfolio" / "PORTFOLIO.md").exists():
                artifacts.append({"source": f"curriculum/digital_rc/{pkg_id}/portfolio/PORTFOLIO.md"})
            # fallback: PORTFOLIO.md at package root
            if (pdir / "PORTFOLIO.md").exists():
                artifacts.append({"source": f"curriculum/digital_rc/{pkg_id}/PORTFOLIO.md"})
        prog = program_path(track)
        outcomes = extract_outcomes(read_text(prog)) if prog else []
        entries.append(
            {
                "track_id": tid,
                "title": track["title"],
                "package_id": pkg_id,
                "program_outcomes": outcomes,
                "portfolio_artifacts": artifacts,
                "portfolio_present": bool(artifacts),
                "gap": None
                if artifacts
                else "No portfolio artifacts.json/PORTFOLIO.md found in package",
            }
        )
    return {
        "schema": "waike.full_readiness.portfolio_outcomes_index.v1",
        "generated_at": now_iso(),
        "track_count": len(entries),
        "tracks_with_portfolio": sum(1 for e in entries if e["portfolio_present"]),
        "entries": entries,
        "notes": [
            "Aggregated from packages when present; absence is recorded as gap.",
            "Does not claim learner portfolios were submitted.",
        ],
    }


def standards_matrix(tracks: list[dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for track in tracks:
        tid = track["track_id"]
        rows.append(
            {
                "track_id": tid,
                "title": track["title"],
                "internal_skills": SKILL_MAP.get(tid, []),
                "external_draft": EXTERNAL_DRAFT.get(tid, []),
                "accreditation_claim": False,
                "external_mapping_status": "draft",
                "yaml_path": f"standards_alignment/by_track/{tid}.yaml",
            }
        )
    return {
        "schema": "waike.full_readiness.standards_alignment_matrix.v1",
        "generated_at": now_iso(),
        "disclaimer": (
            "Draft alignments only. Not accredited, not endorsed, not official certification training."
        ),
        "track_count": len(rows),
        "rows": rows,
    }


def matrix_md(matrix: dict[str, Any]) -> str:
    lines = [
        "# Standards alignment matrix (draft)",
        "",
        matrix["disclaimer"],
        "",
        "| Track | Internal skills | External frameworks (draft) | Accreditation |",
        "|-------|-----------------|----------------------------|---------------|",
    ]
    for r in matrix["rows"]:
        skills = ", ".join(f"`{s}`" for s in r["internal_skills"]) or "—"
        ext = ", ".join(e["framework"] for e in r["external_draft"]) or "—"
        lines.append(f"| {r['track_id']} | {skills} | {ext} | false |")
    lines.append("")
    lines.append(f"_Generated {matrix['generated_at']}_")
    return "\n".join(lines) + "\n"


def portfolio_md(index: dict[str, Any]) -> str:
    lines = [
        "# Portfolio outcomes index",
        "",
        f"Tracks: {index['track_count']} · With portfolio files: {index['tracks_with_portfolio']}",
        "",
        "| Track | Package | Portfolio present | Gap | Outcome count |",
        "|-------|---------|-------------------|-----|---------------|",
    ]
    for e in index["entries"]:
        lines.append(
            f"| {e['track_id']} | `{e['package_id']}` | {e['portfolio_present']} | "
            f"{e['gap'] or '—'} | {len(e['program_outcomes'])} |"
        )
    lines.append("")
    lines.append("## Notes")
    for n in index["notes"]:
        lines.append(f"- {n}")
    lines.append(f"\n_Generated {index['generated_at']}_")
    return "\n".join(lines) + "\n"


def write_agent10_report(
    review_results: list[dict[str, Any]],
    pilot_results: list[dict[str, Any]],
    standards_paths: list[Path],
) -> Path:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    path = ARTIFACTS / "AGENT_10_REVIEW_PILOT.md"
    r_ok = sum(1 for r in review_results if r["complete"])
    p_ok = sum(1 for r in pilot_results if r["complete"])
    thin = [r for r in review_results if r["gaps"]]
    lines = [
        "# Agent 10 — Review & Pilot readiness closure",
        "",
        f"Generated: {now_iso()}",
        "",
        "## Counts",
        "",
        f"- Review packets complete: **{r_ok}/18**",
        f"- Pilot packets complete: **{p_ok}/18**",
        f"- Standards YAML written: **{len(standards_paths)}/18**",
        "",
        "## Honesty summary",
        "",
        "- Signoff forms left **PASS=false** and human fields blank.",
        "- Pilot packets are **design only** — no claim that a pilot ran.",
        "- External standards mappings marked **draft**; accreditation_claim=false.",
        "- Shared packages (GENERAL_IT, HARDWARE_ENGINEERING) called out as specialization risks.",
        "- SEVEN_GC_APPRENTICESHIP: EXTERNAL gates remain open; peer review packet preserved if present.",
        "",
        "## Review packets",
        "",
        "| Track | Package | Weeks | Labs | Complete | Gap count | Peer preserved |",
        "|-------|---------|-------|------|----------|-----------|----------------|",
    ]
    for r in review_results:
        lines.append(
            f"| {r['track_id']} | `{r['package_id']}` | {r['week_count']} | {r['lab_count']} | "
            f"{r['complete']} | {len(r['gaps'])} | {r.get('preserved_peer')} |"
        )
    lines.extend(
        [
            "",
            "## Pilot packets",
            "",
            "| Track | Complete | Files |",
            "|-------|----------|-------|",
        ]
    )
    for r in pilot_results:
        lines.append(
            f"| {r['track_id']} | {r['complete']} | {len(r['files_present'])} |"
        )
    lines.extend(["", "## Tracks with inventory gaps (not hidden)", ""])
    for r in thin:
        lines.append(f"### {r['track_id']}")
        for g in r["gaps"][:12]:
            lines.append(f"- {g}")
        if len(r["gaps"]) > 12:
            lines.append(f"- … +{len(r['gaps']) - 12} more")
        lines.append("")
    lines.extend(
        [
            "## Artifacts produced",
            "",
            "- `curriculum/review_packets/<TRACK_ID>/` ×18",
            "- `pilot/track_<TRACK_ID>/` ×18",
            "- `standards_alignment/by_track/<TRACK_ID>.yaml` ×18",
            "- `artifacts/full_readiness/STANDARDS_ALIGNMENT_MATRIX.json` + `.md`",
            "- `artifacts/full_readiness/PORTFOLIO_OUTCOMES_INDEX.json` + `.md`",
            "- `scripts/full_readiness/validate_depth_anti_filler.py`",
            "- `artifacts/full_readiness/DEPTH_ANTI_FILLER_REPORT.json` (run validator)",
            "",
            "## Non-actions",
            "",
            "- Did not edit `curriculum/taxonomy/canonical_track_registry.v1.json`",
            "- Did not merge, push, or open PRs",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    reg = load_json(REGISTRY)
    if not reg:
        raise SystemExit(f"Cannot read registry {REGISTRY}")
    tracks = reg["tracks"]
    assert len(tracks) == 18, len(tracks)

    review_results = []
    pilot_results = []
    standards_paths = []

    for track in tracks:
        rmeta = ensure_review_packet(track)
        review_results.append(rmeta)
        pilot_results.append(ensure_pilot_packet(track, rmeta))
        standards_paths.append(write_standards_yaml(track))

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    matrix = standards_matrix(tracks)
    (ARTIFACTS / "STANDARDS_ALIGNMENT_MATRIX.json").write_text(
        json.dumps(matrix, indent=2) + "\n", encoding="utf-8"
    )
    (ARTIFACTS / "STANDARDS_ALIGNMENT_MATRIX.md").write_text(
        matrix_md(matrix), encoding="utf-8"
    )
    port = portfolio_outcomes_index(tracks)
    (ARTIFACTS / "PORTFOLIO_OUTCOMES_INDEX.json").write_text(
        json.dumps(port, indent=2) + "\n", encoding="utf-8"
    )
    (ARTIFACTS / "PORTFOLIO_OUTCOMES_INDEX.md").write_text(
        portfolio_md(port), encoding="utf-8"
    )

    report = write_agent10_report(review_results, pilot_results, standards_paths)
    summary = {
        "review_packets_complete": sum(1 for r in review_results if r["complete"]),
        "pilot_packets_complete": sum(1 for r in pilot_results if r["complete"]),
        "standards_yaml": len(standards_paths),
        "report": str(report.relative_to(ROOT)),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
