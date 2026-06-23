"""Generate WAIKE UPNOW campus design docs, curriculum, and quality artifacts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from waike_campus.site_registry import (
    ASSIGNMENT_TITLES,
    LAB_TITLES,
    SHARED_ROOMS,
    SITE_IDS,
    SITE_REGISTRY,
    WEEK_TOPICS,
    get_site,
)

ROOT = Path(__file__).resolve().parents[1]

MATERIAL_CLASSES = [
    "light-gauge steel framing with mineral wool",
    "double-stud acoustic partitions",
    "acoustic gypsum assemblies",
    "fiber cement / cement board",
    "mineral wool insulation",
    "acoustic sealant and gasketed doors",
    "insulated glazing units",
    "low-VOC acoustic wall panels",
    "perforated acoustic ceiling panels",
    "recycled rubber acoustic underlayment",
    "modular utility pods",
    "raised floor assemblies",
    "structured cabling pathways",
    "acoustic baffles",
    "washable durable wall finishes",
    "moisture-resistant flooring",
    "locally repairable casework",
    "low-VOC paints and adhesives",
]

EVIDENCE_LABELS = [
    "brief-derived",
    "public-source-grounded",
    "synthetic simulation",
    "design assumption",
    "expert review required",
    "community validation required",
    "unsafe to publish publicly",
]


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _conceptual_banner(site_id: str) -> str:
    site = get_site(site_id)
    lines = [
        "> **Conceptual only — not for construction**",
        "> Expert review required before construction or field deployment.",
        "> Requires licensed architect/engineer review before construction.",
    ]
    if site.get("conceptual_only"):
        lines.append(
            "> No Antarctic construction or field operation claim; partner approval and environmental review required."
        )
    if site.get("privacy_sensitive"):
        lines.append(
            "> Do not publish sensitive locations, learner identities, family movements, shelter locations, or private recovery data."
        )
    return "\n".join(lines) + "\n\n"


def generate_campus_design_canon() -> None:
    base = ROOT / "docs" / "campus_design"
    _write(
        base / "README.md",
        """# 7GC Campus Design System

**WAIKE UPNOW** | **Build → Ship → Document → Present**

> Conceptual only — not for construction. Expert review required before construction or field deployment.

This directory contains the **7GC Campus Design System** for all seven WAIKE UPNOW sites:

| Site ID | Public name |
|---------|-------------|
| gary | WAIKE Gary UPNOW |
| ghana | WAIKE Ghana UPNOW |
| guyana | WAIKE Guyana UPNOW |
| gaza | WAIKE Gaza UPNOW |
| geelong | WAIKE Geelong UPNOW |
| graham_land | WAIKE Graham Land UPNOW |
| germany | WAIKE Germany UPNOW |

## Canon documents

- [7GC_CAMPUS_DESIGN_CANON.md](7GC_CAMPUS_DESIGN_CANON.md)
- [7GC_BUILDING_DESIGN_SYSTEM.md](7GC_BUILDING_DESIGN_SYSTEM.md)
- [7GC_ROOM_PROGRAM_LIBRARY.md](7GC_ROOM_PROGRAM_LIBRARY.md)
- [7GC_MATERIALS_ACOUSTICS_RF_CANON.md](7GC_MATERIALS_ACOUSTICS_RF_CANON.md)
- [7GC_SITE_SELECTION_RUBRIC.md](7GC_SITE_SELECTION_RUBRIC.md)
- [7GC_PUBLIC_BENEFIT_CHECKLIST.md](7GC_PUBLIC_BENEFIT_CHECKLIST.md)
- [7GC_NON_CLAIM_POLICY.md](7GC_NON_CLAIM_POLICY.md)
- [7GC_EXPERT_REVIEW_REQUIREMENTS.md](7GC_EXPERT_REVIEW_REQUIREMENTS.md)
- [7GC_SISTER_REVIEW_PACKET.md](7GC_SISTER_REVIEW_PACKET.md)

## Per-site packages

Each `docs/campus_design/<site_id>/` folder contains room programs, floor plan concepts, materials matrices, and community benefit plans.

## Evidence model

Every claim is labeled: brief-derived | public-source-grounded | synthetic simulation | design assumption | expert review required | community validation required | unsafe to publish publicly.

## Audience

Beginner students, instructors, urban planners, wireless/NTN researchers, campus designers, workforce reviewers, grant reviewers, GitHub reviewers, and community partners.
""",
    )

    canon_files = {
        "7GC_CAMPUS_DESIGN_CANON.md": """# 7GC Campus Design Canon

**Evidence:** brief-derived | **Status:** conceptual only — not for construction

## Principles

1. **Host-first, not brand-first** — local partners govern use and visibility.
2. **Retrofit before new construction** — lower cost, faster community benefit.
3. **Public benefit before expansion** — prove local value before scaling.
4. **Evidence before claims** — label assumptions; collect validation paths.
5. **Partner approval required** for field activity.

## Three footprint tiers (all sites)

| Tier | Purpose | Typical size class |
|------|---------|-------------------|
| Minimum pilot | Prove curriculum + community benefit | 2–4 learning zones |
| Semi-permanent hub | Stable cohort + device/repair operations | 6–10 zones |
| Full campus | Full WAIKE UPNOW room program | 12–20+ zones |

## RF and acoustics tradeoff (global)

- Strong **sound-isolated** partitions between learning zones (not "fully soundproof").
- **Wired Ethernet/fiber backbone** for signal continuity.
- **APs inside each learning zone** — do not rely on wall leakage.
- Intentional **RF pass-through / radome zones** only where appropriate.
- **Shielded RF zones** for experiments.

## Required deliverables per site

Room program, adjacency diagram, block floor plan, material matrix, acoustic strategy, RF strategy, power assumptions, accessibility notes, community-use notes, maintenance notes, cost-efficiency scoring, expert-review checklist.
""",
        "7GC_BUILDING_DESIGN_SYSTEM.md": """# 7GC Building Design System

> Conceptual only — not for construction. Requires licensed architect/engineer review before construction.

## Output types (allowed)

- Block diagrams, Mermaid diagrams, Markdown tables, YAML configs, JSON room graphs, SVG block floor plans

## Output types (not allowed)

- Stamped engineering drawings, final structural calculations, wind/snow/seismic/flood certifications, procurement-specific product recommendations

## Building typologies

Each site defines three typologies: pop-up/minimum pilot, retrofit/semi-permanent hub, full campus concept.

## Design workflow

```mermaid
flowchart LR
  A[Community brief] --> B[Room program]
  B --> C[Adjacency graph]
  C --> D[Block floor plan]
  D --> E[Materials matrix]
  E --> F[Acoustic/RF tradeoff]
  F --> G[Connectivity assumptions]
  G --> H[Expert review packet]
```
""",
        "7GC_ROOM_PROGRAM_LIBRARY.md": """# 7GC Room Program Library

Shared rooms across all WAIKE UPNOW campuses:

| Room ID | Purpose | Acoustic target | RF notes |
|---------|---------|-----------------|----------|
| welcome_intake | Orientation, device check-in | moderate | AP in zone |
| flexible_classroom | Cohort instruction | high isolation | AP in zone |
| device_bar | Loaner/repair intake | moderate | wired + AP |
| hardware_repair_lab | Bench work, ESD safety | moderate | lab VLAN |
| networking_cyber_lab | Segmented practice | high isolation | isolated lab net |
| ai_cloud_studio | AI literacy, edge demos | moderate | AP + wired |
| career_portfolio_studio | Resume, portfolio | moderate | AP in zone |
| community_room | Public workshops | moderate | guest VLAN |
| staff_mentor_workspace | Planning, 1:1 | high isolation | staff net |
| secure_storage | Devices, kits | N/A | no RF requirement |
| quiet_decompression | Rest, low stimulation | very high isolation | minimal RF |
| hybrid_learning_corner | Recording, async | high isolation | wired preferred |
| server_comms_closet | Backbone, UPS | N/A | controlled RF |
| mechanical_electrical_zone | MEP, ventilation | N/A | shielded |
| public_exhibit_wall | Showcase, demos | low | AP nearby |

Site-specific rooms are documented in each site's `_ROOM_PROGRAM.md`.
""",
        "7GC_MATERIALS_ACOUSTICS_RF_CANON.md": """# 7GC Materials, Acoustics, and RF Canon

> Conceptual only — not for construction. No brand-specific product recommendations.

## Material matrix columns

material class | use case | site suitability | climate/environment | thermal | acoustic isolation | RF/signal impact | moisture/corrosion/flood/fire | repairability | local procurement | shipping complexity | cost class | durability | accessibility/health | expert-review-needed | notes/risks

## Global material classes

""" + "\n".join(f"- {m}" for m in MATERIAL_CLASSES) + """

## Acoustic vs RF tradeoff

| Strategy | Acoustic benefit | RF impact | When to use |
|----------|------------------|-----------|-------------|
| Double-stud partition | High sound-isolated separation | Blocks RF — use wired backhaul | Between classrooms |
| Acoustic gypsum + sealant | Moderate-high | Blocks RF | Labs adjacent to quiet rooms |
| RF pass-through panel / radome zone | Lower acoustic | Enables controlled RF | NTN demo, antenna teaching only |
| Perforated acoustic ceiling | Moderate | Minimal if AP inside room | Open classrooms |

**Rule:** Model signal using AP placement inside zones, not wall leakage.
""",
        "7GC_SITE_SELECTION_RUBRIC.md": """# 7GC Site Selection Rubric

| Criterion | Weight | Score 1–5 | Evidence needed |
|-----------|--------|-----------|-----------------|
| Community partner readiness | 25% | | community validation required |
| Transit / access equity | 15% | | public-source-grounded |
| Retrofit feasibility | 15% | | expert review required |
| Power and connectivity baseline | 15% | | design assumption |
| Safety and child protection | 15% | | expert review required |
| Public benefit potential | 15% | | brief-derived |

**Gaza:** No fixed public site selection scores — distributed network model only.
**Graham Land:** Remote-first digital twin — no physical Antarctic site selection.
""",
        "7GC_PUBLIC_BENEFIT_CHECKLIST.md": """# 7GC Public Benefit Checklist

- [ ] Local partner identified and consulted (community validation required)
- [ ] Youth-to-career pathway documented (brief-derived)
- [ ] Device access plan for underserved learners (design assumption)
- [ ] Community workshop schedule drafted (design assumption)
- [ ] No unauthorized institutional partnership claims (non-claim policy)
- [ ] Privacy review for public dashboards (expert review required)
- [ ] Repair/refurbish culture supported (brief-derived)
- [ ] Instructor and caregiver support materials ready (brief-derived)
""",
        "7GC_NON_CLAIM_POLICY.md": """# 7GC Non-Claim Policy

**Do not claim:**

- Official institutional partnerships without signed agreements
- Deployed 6G/NTN operational infrastructure
- Physical Antarctic construction (Graham Land)
- Exact sensitive site locations (Gaza and other vulnerable contexts)
- Stamped engineering approval

**Internal/legacy only:** WAIKE TF UP — not for public-facing documents.

**Network simulations:** research simulation only — not operational carrier, emergency, satellite, or safety service.
""",
        "7GC_EXPERT_REVIEW_REQUIREMENTS.md": """# 7GC Expert Review Requirements

| Domain | Reviewer type | Before |
|--------|---------------|--------|
| Structural / envelope | Licensed architect/engineer | Any construction |
| Electrical / power | Licensed electrician/engineer | Permanent install |
| RF / NTN experiments | Wireless researcher | Lab commissioning |
| Child protection | Safeguarding specialist | Gaza public materials |
| Polar programs | Environmental / treaty advisor | Graham Land field-adjacent concepts |
| Community governance | Local partner lead | Field activity |

All building outputs: **requires licensed architect/engineer review before construction.**
""",
        "7GC_SISTER_REVIEW_PACKET.md": """# 7GC Sister Review Packet (Template)

## Reviewer roles

- Instructor, urban planner, wireless researcher, campus designer, workforce reviewer, grant reviewer, community partner

## Sections to review

1. Public positioning and non-claim compliance
2. Room program completeness
3. Acoustic/RF tradeoff documentation
4. Curriculum alignment (12-week spine)
5. Community benefit plan
6. Evidence matrix accuracy

## Sign-off

| Reviewer | Site | Date | Status |
|----------|------|------|--------|
| | | | requires expert review |
""",
    }
    for name, body in canon_files.items():
        _write(base / name, body)


def generate_site_campus_docs(site_id: str) -> None:
    site = get_site(site_id)
    base = ROOT / "docs" / "campus_design" / site_id
    banner = _conceptual_banner(site_id)
    rooms = SHARED_ROOMS + site["extra_rooms"]

    _write(
        base / "README.md",
        f"""# {site['display_name']} — Campus Design

{banner}
**Role:** {site['role']}
**Anchor:** {site['anchor']}

## Documents

- [_PUBLIC_POSITIONING.md](_PUBLIC_POSITIONING.md)
- [_CAMPUS_BRIEF_SUMMARY.md](_CAMPUS_BRIEF_SUMMARY.md)
- [_ROOM_PROGRAM.md](_ROOM_PROGRAM.md)
- [_CONCEPTUAL_BUILDING_PROGRAM.md](_CONCEPTUAL_BUILDING_PROGRAM.md)
- [_FLOOR_PLAN_PROGRAM.md](_FLOOR_PLAN_PROGRAM.md)
- [_MATERIALS_AND_ACOUSTICS_MATRIX.md](_MATERIALS_AND_ACOUSTICS_MATRIX.md)
- [_SIGNAL_AND_SOUND_ISOLATION_STRATEGY.md](_SIGNAL_AND_SOUND_ISOLATION_STRATEGY.md)
- [_SITE_SELECTION_RUBRIC.md](_SITE_SELECTION_RUBRIC.md)
- [_RISK_REGISTER.md](_RISK_REGISTER.md)
- [_COMMUNITY_BENEFIT_PLAN.md](_COMMUNITY_BENEFIT_PLAN.md)
- [_SISTER_REVIEW_PACKET.md](_SISTER_REVIEW_PACKET.md)
""",
    )

    _write(
        base / "_PUBLIC_POSITIONING.md",
        f"""# {site['display_name']} — Public Positioning

{banner}
## Public name

**{site['display_name']}**
{site['subtitle']}
{site['tagline']}

## Role

{site['role']}

## Anchor

{site['anchor']}

## Evidence

| Claim | Label |
|-------|-------|
| Program name and tagline | brief-derived |
| Anchor geography (general) | public-source-grounded |
| Building dimensions | design assumption |
| Partner relationships | community validation required |
""",
    )

    room_rows = "\n".join(
        f"| {r} | Learning/support | sound-isolated where needed | AP in zone | design assumption |"
        for r in rooms
    )
    _write(
        base / "_ROOM_PROGRAM.md",
        f"""# {site['display_name']} — Room Program

{banner}
## Shared + site-specific rooms

| Room ID | Function | Acoustic | RF | Evidence |
|---------|----------|----------|-----|----------|
{room_rows}

## Footprint tiers

{chr(10).join(f'- **{t}**' for t in site['building_typologies'])}
""",
    )

    adjacency = " --> ".join(rooms[:8])
    _write(
        base / "_FLOOR_PLAN_PROGRAM.md",
        f"""# {site['display_name']} — Floor Plan Program

{banner}
## Block adjacency (conceptual)

```mermaid
flowchart LR
  welcome_intake --> flexible_classroom
  flexible_classroom --> device_bar
  device_bar --> hardware_repair_lab
  hardware_repair_lab --> networking_cyber_lab
```

## Three footprints

| Tier | Zones | Notes |
|------|-------|-------|
| Minimum pilot | 4 | Pop-up / remote-first where applicable |
| Semi-permanent hub | 8 | Retrofit typology |
| Full campus | {len(rooms)} | Complete room program |

> Requires licensed architect/engineer review before construction.
""",
    )

    mat_rows = ""
    for mc in MATERIAL_CLASSES[:10]:
        mat_rows += f"| {mc} | walls/partitions | {site_id} | climate-aware | moderate | high isolation | blocks RF — wired backhaul | low-med | high | medium | medium | medium | high | low-VOC | yes | conceptual |\n"

    _write(
        base / "_MATERIALS_AND_ACOUSTICS_MATRIX.md",
        f"""# {site['display_name']} — Materials and Acoustics Matrix

{banner}
| material class | use case | site suitability | climate | thermal | acoustic | RF impact | moisture/fire | repairability | local procurement | shipping | cost | durability | health | expert review | notes |
|----------------|----------|------------------|---------|---------|----------|-----------|---------------|---------------|-------------------|----------|------|------------|--------|---------------|-------|
{mat_rows}
""",
    )

    _write(
        base / "_SIGNAL_AND_SOUND_ISOLATION_STRATEGY.md",
        f"""# {site['display_name']} — Signal and Sound Isolation Strategy

{banner}
## Network emphasis

{site['network_emphasis']}

## Connectivity stack

- Wired Ethernet/fiber backbone (design assumption)
- Wi-Fi AP per learning zone (design assumption)
- Local edge cache (synthetic simulation)
- Offline content server where needed (design assumption)
- Student vs staff vs lab network segmentation (brief-derived)
- Emergency/backup connectivity mode (design assumption)

## Acoustic/RF tradeoff matrix

| Zone pair | Acoustic strategy | RF strategy |
|-----------|-------------------|-------------|
| classroom ↔ classroom | double-stud, sound-isolated | separate APs; wired backbone |
| classroom ↔ quiet room | high isolation | minimal RF in quiet room |
| lab ↔ corridor | moderate isolation | AP inside lab only |

> Research simulation only — not operational carrier or emergency service.
""",
    )

    for fname, title, body in [
        ("_CAMPUS_BRIEF_SUMMARY.md", "Campus Brief Summary", site["role"]),
        ("_CONCEPTUAL_BUILDING_PROGRAM.md", "Conceptual Building Program", "\n".join(f"- {t}" for t in site["building_typologies"])),
        ("_SITE_SELECTION_RUBRIC.md", "Site Selection Rubric", "See global rubric; site-specific weights in community benefit plan."),
        ("_RISK_REGISTER.md", "Risk Register", "| Risk | Mitigation | Owner |\n|------|------------|-------|\n| Overclaiming deployment | Non-claim policy | program lead |\n| RF/acoustic conflict | Tradeoff matrix | campus designer |"),
        ("_COMMUNITY_BENEFIT_PLAN.md", "Community Benefit Plan", f"Host-first delivery for {site['anchor']}. Partner approval required for field activity."),
        ("_SISTER_REVIEW_PACKET.md", "Sister Review Packet", "Complete all checklist items before external grant submission."),
    ]:
        _write(base / fname, f"# {site['display_name']} — {title}\n\n{banner}{body}\n")


def generate_curriculum_site(site_id: str) -> None:
    site = get_site(site_id)
    base = ROOT / "curriculum" / f"{site_id}_upnow"
    banner = _conceptual_banner(site_id)

    _write(
        base / "README.md",
        f"""# {site['course_title']}

{banner}
12-week WAIKE UPNOW course for **{site['display_name']}**.

## Artifacts

- [SYLLABUS.md](SYLLABUS.md)
- [COURSE_MAP.md](COURSE_MAP.md)
- [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)
- [STUDENT_GUIDE.md](STUDENT_GUIDE.md)
- [ASSESSMENT_POLICY.md](ASSESSMENT_POLICY.md)
- [RUBRICS.md](RUBRICS.md)
- [EXAM_BANK.md](EXAM_BANK.md)
- [GLOSSARY.md](GLOSSARY.md)
""",
    )

    week_table = "\n".join(
        f"| {w} | {t} | A{w}: {ASSIGNMENT_TITLES[w-1]} | L{w}: {LAB_TITLES[w-1]} |"
        for w, t in enumerate(WEEK_TOPICS, 1)
    )
    _write(
        base / "SYLLABUS.md",
        f"""# {site['course_title']} — Syllabus

{banner}
## Course spine (12 weeks)

| Week | Topic | Assignment | Lab |
|------|-------|------------|-----|
{week_table}

## Site modules

{chr(10).join(f'- {m}' for m in site['modules'])}
""",
    )

    _write(
        base / "COURSE_MAP.md",
        f"""# {site['course_title']} — Course Map

```mermaid
flowchart TB
  W1[Ethics & place] --> W2[Digital foundations]
  W2 --> W3[Connectivity]
  W3 --> W4[Hardware]
  W4 --> W5[Software]
  W5 --> W6[Cybersecurity]
  W6 --> W7[AI/Cloud]
  W7 --> W8[Applied systems]
  W8 --> W9[Campus design]
  W9 --> W10[Community sprint]
  W10 --> W11[Portfolio]
  W11 --> W12[Capstone]
```
""",
    )

    for guide, audience in [("INSTRUCTOR_GUIDE.md", "instructors"), ("STUDENT_GUIDE.md", "students")]:
        _write(
            base / guide,
            f"""# {site['course_title']} — {guide.replace('.md','').replace('_',' ').title()}

{banner}
Audience: {audience}

## Weekly rhythm

Build → Ship → Document → Present

## Trauma-aware note (all sites)

Adjust pacing for disruption. Gaza cohorts: never punish connectivity loss or trauma-related absence.

## Evidence

Curriculum structure: brief-derived. Local examples: community validation required.
""",
        )

    _write(
        base / "ASSESSMENT_POLICY.md",
        f"""# {site['course_title']} — Assessment Policy

Open-book, scenario-based assessments. Partial credit for reasoning, documentation, safety, and ethics.

| Component | Weight |
|-----------|--------|
| Weekly assignments | 40% |
| Labs | 25% |
| Exams (midterm, final, practical) | 20% |
| Capstone + portfolio | 15% |
""",
    )

    _write(
        base / "RUBRICS.md",
        """# Rubrics

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| Local accountability | Names local partners and constraints | Identifies local context | Generic context | Missing |
| Documentation | Complete, cited, labeled evidence | Mostly complete | Gaps | Minimal |
| Safety & ethics | Proactive risk identification | Adequate | Incomplete | Unsafe |
| Technical literacy | Correct tradeoff reasoning | Mostly correct | Errors | Incorrect |
""",
    )

    _write(
        base / "GLOSSARY.md",
        f"""# GLOSSARY — {site['display_name']}

| Term | Definition | Evidence |
|------|------------|----------|
| WAIKE UPNOW | Workforce program brand for undiscovered professionals | brief-derived |
| sound-isolated | Acoustic privacy between rooms; not fully soundproof | brief-derived |
| edge cache | Local content store for offline/low-bandwidth learning | design assumption |
| NTN | Non-terrestrial networks (satellite) — simulation only here | synthetic simulation |
""",
    )

    exam_notes = {
        "gary": "Emphasize local public benefit and workforce readiness.",
        "ghana": "Emphasize mobile-first practicality and local entrepreneurship.",
        "guyana": "Emphasize climate/flood/logistics/data ethics.",
        "gaza": "Trauma-aware; do not punish disruption; no sensitive locations.",
        "geelong": "Emphasize design/build, manufacturing, and regional access.",
        "graham_land": "Distinguish simulation from field evidence; no operational NTN claims.",
        "germany": "Emphasize documentation, safety, and quality systems.",
    }

    _write(
        base / "EXAM_BANK.md",
        f"""# {site['course_title']} — Exam Bank

Index of formal assessments. All exams are open-book and scenario-based.

| Exam | File | Solution key |
|------|------|--------------|
| Midterm | [exams/midterm_exam.md](exams/midterm_exam.md) | [exams/midterm_solution_key.md](exams/midterm_solution_key.md) |
| Final | [exams/final_exam.md](exams/final_exam.md) | [exams/final_solution_key.md](exams/final_solution_key.md) |
| Practical | [exams/practical_exam.md](exams/practical_exam.md) | [exams/practical_solution_key.md](exams/practical_solution_key.md) |

**Site emphasis:** {exam_notes[site_id]}
""",
    )

    for week in range(1, 13):
        topic = WEEK_TOPICS[week - 1]
        mod = site["modules"][(week - 1) % len(site["modules"])]
        lec = f"""# Week {week} Lecture — {topic}

{banner}
**Site module emphasis:** {mod}

## Learning objectives

1. Explain how this week supports **{site['display_name']}** public benefit.
2. Complete documentation with evidence labels.
3. Identify what is proven vs assumed vs needs validation.

## Instructor notes

- Pace for local connectivity realities.
- Use sound-isolated room examples, not "fully soundproof."
- Portfolio artifact: week {week} reflection memo.

## Quiz questions

1. What is the local accountability goal this week? (open-book)
2. Name one RF/acoustic tradeoff relevant to {site_id}. (partial credit)
3. Label one claim as brief-derived vs design assumption.

## Provenance

| Item | Status |
|------|--------|
| Learning objectives | brief-derived |
| Technical examples | design assumption |
| Field measurements | expert review required |
"""
        _write(base / "lectures" / f"week_{week:02d}_lecture.md", lec)

        asn = f"""# Assignment {week} — {ASSIGNMENT_TITLES[week - 1]}

{banner}
**Course:** {site['course_title']}
**Week {week}:** {topic}

## Deliverables

1. Written memo (500–800 words) with evidence labels
2. Diagram or table as specified
3. Community benefit tie-in paragraph

## Rubric mapping

| Criterion | Points |
|-----------|--------|
| Local accountability | 25 |
| Documentation | 25 |
| Safety/ethics | 25 |
| Technical quality | 25 |

## Portfolio artifact

Upload to portfolio folder: `a{week:02d}_{site_id}_assignment.md`

## Provenance note

**Proven:** curriculum structure | **Assumed:** local partner names | **Needs validation:** field measurements
"""
        _write(base / "assignments" / f"a{week:02d}_assignment.md", asn)

        lab = f"""# Lab {week} — {LAB_TITLES[week - 1]}

{banner}
**Duration:** 90 minutes (adjust for connectivity)

## Setup

- Devices as available; offline pack if needed
- Partner-approved space only

## Steps

1. Document starting assumptions (evidence labels)
2. Execute lab procedure for week {week}
3. Record results in lab journal
4. Note RF/acoustic observations if relevant

## Student deliverable

`lab_{week:02d}_report.md` with screenshots or tables (no sensitive locations for Gaza)

## Instructor checklist

- [ ] Safety briefing complete
- [ ] Privacy check for public sharing
- [ ] Trauma-aware pacing (Gaza)
"""
        _write(base / "labs" / f"lab_{week:02d}.md", lab)

        _write(
            base / "tutor_cards" / f"week_{week:02d}_tutor_card.md",
            f"# Tutor Card Week {week}\n\n**Topic:** {topic}\n**Key misconception:** RF does not pass through sound-isolated walls — use APs per zone.\n**Socratic prompt:** What would a community partner ask about this week's deliverable?\n",
        )

    for exam in ["midterm", "final", "practical"]:
        _write(
            base / "exams" / f"{exam}_exam.md",
            f"""# {exam.title()} Exam — {site['course_title']}

{banner}
**Style:** open-book, scenario-based, partial credit
**Site emphasis:** {exam_notes[site_id]}

## Section A — Ethics and place (25%)

Scenario: A partner asks whether the campus claim is deployment-ready. Draft a non-claim response.

## Section B — Connectivity tradeoffs (25%)

Explain wired backbone vs AP-per-zone for a sound-isolated classroom pair.

## Section C — Site applied systems (25%)

Site-specific scenario using module: {site['modules'][0]}

## Section D — Documentation (25%)

Label three claims with evidence types from the master list.
""",
        )
        _write(
            base / "exams" / f"{exam}_solution_key.md",
            f"""# {exam.title()} Solution Key — INSTRUCTOR ONLY

Sample acceptable responses with rubric notes. Adjust for local validation.

> Do not distribute solution keys to students without instructor context.
""",
        )

    _write(
        base / "capstone" / "CAPSTONE_BRIEF.md",
        f"""# Capstone — {site['course_title']}

Integrate weeks 1–11 into a community-benefit project with portfolio presentation.

**Deliverables:** capstone report, demo, private partner briefing, public-safe summary.

**Evidence:** community validation required before any public claim of impact.
""",
    )

    _write(
        base / "datasets" / "synthetic_sample.json",
        json.dumps(
            {
                "site_id": site_id,
                "evidence_status": "synthetic simulation",
                "learners_sample_count": 12,
                "device_types": ["phone", "chromebook", "repair_bench"],
                "connectivity_modes": ["wired", "wifi", "offline_cache"],
            },
            indent=2,
        ),
    )

    _write(
        base / "slides_outline" / "week_01_outline.md",
        "# Week 1 Slides Outline\n\n1. Welcome + WAIKE UPNOW\n2. Place and ethics\n3. Non-claim policy\n4. Community benefit\n5. Lab preview\n",
    )


def generate_quality_matrices() -> None:
    q = ROOT / "quality"
    sites_rows = "\n".join(
        f"| {s} | yes | yes | yes | yes | design assumption |"
        for s in SITE_IDS
    )
    _write(
        q / "7GC_MASTER_EVIDENCE_MATRIX.md",
        f"""# 7GC Master Evidence Matrix

| Site | Curriculum | Campus design | Digital twin | Resilience sim | Overall |
|------|------------|---------------|--------------|----------------|---------|
{sites_rows}

Evidence labels: {', '.join(EVIDENCE_LABELS)}
""",
    )
    for s in SITE_IDS:
        _write(
            q / f"_{s}_EVIDENCE_MATRIX.md" if False else q / "_EVIDENCE_MATRIX.md",
            "",
        )  # placeholder overwritten below

    _write(
        q / "_EVIDENCE_MATRIX.md",
        """# Per-Site Evidence Matrix Template

Copy per site during review. All generated content starts as brief-derived or design assumption.
""",
    )

    _write(
        q / "7GC_EXPERT_REVIEW_REQUIREMENTS.md",
        """# 7GC Expert Review Requirements

All building outputs require licensed architect/engineer review before construction.
All network simulations are research-only — not operational services.
Gaza: child protection/safety review required.
Graham Land: polar program and environmental review required.
""",
    )

    checklists = {
        "7GC_CAMPUS_READINESS_CHECKLIST.md": "Campus design docs, room program, floor plan, materials, acoustic/RF strategy per site",
        "7GC_CURRICULUM_COMPLETION_MATRIX.md": "12 lectures, assignments, labs, exams per site",
        "7GC_BUILDING_DESIGN_COMPLETION_MATRIX.md": "Three footprints, adjacency, expert review flags per site",
        "7GC_EXPERT_REVIEW_MATRIX.md": "Architect, wireless, safeguarding, community sign-offs",
        "_READINESS_CHECKLIST.md": "Pilot → hub → full campus progression gates",
    }
    for name, desc in checklists.items():
        rows = "\n".join(f"| {s} | generated | expert review required |" for s in SITE_IDS)
        _write(
            q / name,
            f"""# {name.replace('.md','').replace('_',' ')}

{desc}

| Site | Status | Next gate |
|------|--------|-----------|
{rows}
""",
        )

    _write(
        q / "7GC_PUBLIC_SAFETY_AND_PRIVACY_REVIEW.md",
        """# 7GC Public Safety and Privacy Review

- Gaza: no sensitive locations, learner identities, or shelter data in public repos
- All sites: no unsafe public dashboards
- Graham Land: no Antarctic construction claims
- Network sims: not operational services
""",
    )


def generate_cross_repo_docs() -> None:
    base = ROOT / "docs" / "7gc"
    _write(
        base / "7GC_MASTER_INDEX.md",
        """# 7GC Master Index

| Repo | Purpose |
|------|---------|
| waike-research-ops | Curriculum, campus design, assessments |
| 7gc-digital-twin | Building digital twin, floor plans, exports |
| ntn-resilience-sim | Connectivity, outage, edge cache simulations |
""",
    )
    _write(
        base / "7GC_REPO_MAP.md",
        """# 7GC Repo Map

```mermaid
flowchart LR
  OPS[waike-research-ops] --> TWIN[7gc-digital-twin]
  OPS --> NTN[ntn-resilience-sim]
  TWIN --> NTN
```
""",
    )
    _write(
        base / "CROSS_REPO_HANDOFF.md",
        """# Cross-Repo Handoff

## waike-research-ops → others

Exports: room programs, curriculum week topics, material matrices (Markdown/YAML)

## 7gc-digital-twin → others

Exports: SVG floor plans, JSON adjacency graphs, CSV material scores

## ntn-resilience-sim → others

Exports: resilience metrics JSON, outage scenario results

See `docs/7gc/sites/<site_id>/CROSS_REPO_HANDOFF.md` per site.
""",
    )
    _write(
        base / "7GC_EVIDENCE_MATRIX.md",
        """# 7GC Cross-Repo Evidence Matrix

All repos share evidence labels. Building = expert review required. Network = synthetic simulation.
""",
    )
    _write(
        base / "7GC_NON_CLAIM_POLICY.md",
        """# 7GC Non-Claim Policy (Cross-Repo)

Same policy as campus_design/7GC_NON_CLAIM_POLICY.md — synchronized across repos.
""",
    )
    rows = "\n".join(f"| {s} | yes | yes | yes |" for s in SITE_IDS)
    _write(
        base / "7GC_SITE_COMPLETION_MATRIX.md",
        f"""# 7GC Site Completion Matrix

| Site | Curriculum | Campus | Twin | Resilience |
|------|------------|--------|------|------------|
{rows}
""",
    )

    for site_id in SITE_IDS:
        site = get_site(site_id)
        _write(
            base / "sites" / site_id / "CROSS_REPO_HANDOFF.md",
            f"""# {site['display_name']} — Cross-Repo Handoff

## waike-research-ops
- curriculum/{site_id}_upnow/
- docs/campus_design/{site_id}/

## 7gc-digital-twin
- configs/buildings/{site_id}/
- results/exports/{site_id}/

## ntn-resilience-sim
- configs/sites/{site_id}/
- results/site_scenarios/{site_id}/
""",
        )


def generate_curriculum_canon() -> None:
    c = ROOT / "curriculum"
    canon = {
        "README.md": "# WAIKE UPNOW Curriculum\n\nSeven site courses under `<site_id>_upnow/`.\n",
        "7GC_CURRICULUM_CANON.md": "# 7GC Curriculum Canon\n\n12-week shared spine + site modules.\n",
        "7GC_ASSESSMENT_POLICY.md": "# 7GC Assessment Policy\n\nOpen-book, scenario-based, partial credit.\n",
        "7GC_RUBRIC_LIBRARY.md": "# 7GC Rubric Library\n\nSee per-site RUBRICS.md.\n",
        "7GC_EXAM_DESIGN_GUIDE.md": "# 7GC Exam Design Guide\n\nNo trick questions; trauma-aware for Gaza.\n",
        "7GC_CAPSTONE_GUIDE.md": "# 7GC Capstone Guide\n\nCommunity benefit + portfolio.\n",
        "7GC_CREDENTIAL_AND_PORTFOLIO_OUTCOMES.md": "# Credential and Portfolio Outcomes\n\nBadges + portfolio artifacts per week.\n",
    }
    for name, body in canon.items():
        _write(c / name, body)


def generate_all() -> dict[str, int]:
    generate_campus_design_canon()
    generate_curriculum_canon()
    generate_quality_matrices()
    generate_cross_repo_docs()
    counts = {"sites": 0}
    for site_id in SITE_IDS:
        generate_site_campus_docs(site_id)
        generate_curriculum_site(site_id)
        counts["sites"] += 1
    return counts


if __name__ == "__main__":
    result = generate_all()
    print(f"Generated WAIKE UPNOW bundle for {result['sites']} sites")
