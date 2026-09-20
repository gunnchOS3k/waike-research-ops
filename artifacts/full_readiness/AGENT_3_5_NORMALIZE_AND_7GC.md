# Agent 3+4+5 — Normalize + 7GC apprenticeship review

**Worktree:** `waike-research-ops/.worktrees/18-track-full-readiness-closure`  
**Updated:** 2026-09-20T15:41:59Z  
**Did not:** edit `curriculum/taxonomy/canonical_track_registry.v1.json`; merge/push/PR; overwrite Agents 1–2 deep lessons.

## Mission A — 7GC review packet
- Dossier: `curriculum/review_packets/SEVEN_GC_APPRENTICESHIP/` (**41 files**)
- Numbered coverage: objectives, module map, research methods, ethics, mentor expectations, reproducibility, data handling, AI-RAN/digital-twin scope, simulated vs physical boundaries, assessment plan, capstone artifact, publication/portfolio, reviewer checklist, open questions, claim boundary
- Gates: `artifacts/full_readiness/tracks/SEVEN_GC_APPRENTICESHIP_GATES.json`
  - `SEVEN_GC_APPRENTICESHIP_ACADEMIC_REVIEW_PACKET_READY=true`
  - `SEVEN_GC_APPRENTICESHIP_HUMAN_ACADEMIC_REVIEW_PASS=false`
  - mentor/hardware/field/human/physical/publication gates **false**

## Mission B — Track normalization
Addressable packages under `curriculum/digital_rc/` (**21 dirs**): AI_ML_EDGE, CLOUD_DEVOPS, COMM_PD_ETHICS, COMPUTER_NETWORKING, CYBERSECURITY, CYBER_SOC, DATA_DASHBOARDS, DATA_VIZ_BI, DIGITAL_CONFIDENCE, EMBEDDED_PROTOTYPING, GAME_DEV_INTERACTIVE, GENERAL_IT, GUNNCHOS_PRODUCT_LAB, HARDWARE_ENGINEERING, IT_SUPPORT_HARDWARE, NETWORKING_INFRA, PM_AGILE_LSS, ROBOTICS_CONTROL, SEVEN_GC_APPRENTICESHIP, SOFTWARE_BUILDER, WIRELESS_6G

### Required surface (all packages)
Each has: `ai_use_policy.json`, `portfolio/outcomes.json`, `glossary.md`, `references.md`, `accessibility_notes.md`, student + instructor packets (keys/HITL).

- Required-file misses: **0** (none)
- Instructor packets missing HITL literal: **0** (none)

### Entry packages (no blind duplication)
- `DIGITAL_CONFIDENCE/` — **16 files** — `shared_modules/general_it_content_ref.json` → GENERAL_IT weeks/labs; track syllabus, AI policy, mid/final, quizzes, portfolio, project
- `IT_SUPPORT_HARDWARE/` — **16 files** — same shared_modules pattern with hardware-triage emphasis

### Strengthened (non–Agents-1/2)
- Group projects expanded for AI_ML_EDGE, CLOUD_DEVOPS, COMM_PD_ETHICS, DATA_*, GAME_*, GENERAL_IT, HARDWARE_ENGINEERING, PM_AGILE_LSS, ROBOTICS_CONTROL, SEVEN_GC_APPRENTICESHIP, SOFTWARE_BUILDER, WIRELESS_6G, DIGITAL_CONFIDENCE, IT_SUPPORT_HARDWARE
- Stub glossaries/outcomes upgraded where thin
- Gap tracks (NETWORKING_INFRA/COMPUTER_NETWORKING, CYBER_SOC/CYBERSECURITY, EMBEDDED_PROTOTYPING, GUNNCHOS_PRODUCT_LAB): **normalization helpers only** — deep lessons/projects not overwritten

### Upgrades this pass
- glossary:SOFTWARE_BUILDER
- glossary:AI_ML_EDGE
- glossary:CLOUD_DEVOPS
- glossary:COMM_PD_ETHICS
- glossary:DATA_DASHBOARDS
- glossary:DATA_VIZ_BI
- glossary:GAME_DEV_INTERACTIVE
- glossary:GENERAL_IT
- glossary:HARDWARE_ENGINEERING
- glossary:PM_AGILE_LSS
- glossary:ROBOTICS_CONTROL
- glossary:SEVEN_GC_APPRENTICESHIP
- glossary:WIRELESS_6G
- outcomes:SOFTWARE_BUILDER
- outcomes:AI_ML_EDGE
- outcomes:CLOUD_DEVOPS
- outcomes:COMM_PD_ETHICS
- outcomes:DATA_DASHBOARDS
- outcomes:DATA_VIZ_BI
- outcomes:GAME_DEV_INTERACTIVE
- outcomes:GENERAL_IT
- outcomes:HARDWARE_ENGINEERING
- outcomes:PM_AGILE_LSS
- outcomes:ROBOTICS_CONTROL
- outcomes:SEVEN_GC_APPRENTICESHIP
- outcomes:WIRELESS_6G
- project:DIGITAL_CONFIDENCE
- project:IT_SUPPORT_HARDWARE
- review:README_index

## Mission C
This file: `artifacts/full_readiness/AGENT_3_5_NORMALIZE_AND_7GC.md`

## File counts (summary)
| Artifact | Files |
|----------|------:|
| Review packet | 41 |
| DIGITAL_CONFIDENCE | 16 |
| IT_SUPPORT_HARDWARE | 16 |
| digital_rc packages | 21 |
| Gates JSON present | True |

## Blockers
1. SEVEN_GC_APPRENTICESHIP_HUMAN_ACADEMIC_REVIEW_PASS remains false until human academic reviewer signs checklist
2. EXTERNAL_HUMAN_GATE / PHYSICAL / FIELD / mentor / hardware / field-pilot / publication gates remain false
3. Agents 1-2 still own deep curriculum for NETWORKING_INFRA/COMPUTER_NETWORKING, CYBER_SOC/CYBERSECURITY, EMBEDDED_PROTOTYPING, GUNNCHOS_PRODUCT_LAB (projects left thin by design)
4. Sibling research repos may be UNAVAILABLE in learner environments — fixture-only path must stay accepted
5. canonical_track_registry.v1.json not modified (per mission); registry still lists DIGITAL_CONFIDENCE/IT_SUPPORT as covered_via_shared_package — entry packages now exist on disk
