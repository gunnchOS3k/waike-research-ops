# Agent 3+4+5 — Normalize + 7GC apprenticeship review

**Worktree:** `waike-research-ops/.worktrees/18-track-full-readiness-closure`  
**Updated:** 2026-09-20T15:43:58Z  

**Did not:** edit `curriculum/taxonomy/canonical_track_registry.v1.json`; merge/push/open PRs; overwrite Agents 1–2 deep lessons on NETWORKING_INFRA / CYBER_SOC / EMBEDDED_PROTOTYPING / GUNNCHOS_PRODUCT_LAB (and legacy COMPUTER_NETWORKING / CYBERSECURITY).

## Mission A — 7GC review packet
- Path: `curriculum/review_packets/SEVEN_GC_APPRENTICESHIP/` — **41 files**
- Numbered dossier `00`–`14` covers: objectives, module map, research methods, ethics, mentor expectations, reproducibility, data handling, AI-RAN/digital-twin scope, simulated vs physical boundaries, assessment plan, capstone/research artifact, publication/portfolio, reviewer checklist, open questions, claim boundary
- Gates: `artifacts/full_readiness/tracks/SEVEN_GC_APPRENTICESHIP_GATES.json`
  - `SEVEN_GC_APPRENTICESHIP_ACADEMIC_REVIEW_PACKET_READY=true`
  - `SEVEN_GC_APPRENTICESHIP_HUMAN_ACADEMIC_REVIEW_PASS=false`
  - External/mentor/hardware/field/publication human gates **false**

## Mission B — Normalize all digital_rc packages
**21 packages:** AI_ML_EDGE, CLOUD_DEVOPS, COMM_PD_ETHICS, COMPUTER_NETWORKING, CYBERSECURITY, CYBER_SOC, DATA_DASHBOARDS, DATA_VIZ_BI, DIGITAL_CONFIDENCE, EMBEDDED_PROTOTYPING, GAME_DEV_INTERACTIVE, GENERAL_IT, GUNNCHOS_PRODUCT_LAB, HARDWARE_ENGINEERING, IT_SUPPORT_HARDWARE, NETWORKING_INFRA, PM_AGILE_LSS, ROBOTICS_CONTROL, SEVEN_GC_APPRENTICESHIP, SOFTWARE_BUILDER, WIRELESS_6G

### Required surface (create-if-missing; no rich-content deletes)
Each package has: `ai_use_policy.json`, `portfolio/outcomes.json` (no job guarantees), `glossary.md`, `references.md` (real refs), `accessibility_notes.md`, student + instructor packets with **keys/HITL**.

- Required-file misses: **0** (none)
- Instructor HITL coverage: **all packages**

### Entry packages (independent addressability without blind duplication)
| Package | Files | Pattern |
|---------|------:|---------|
| `DIGITAL_CONFIDENCE` | 31 | `shared_modules/general_it_content_ref.json` + optional weeks/labs symlinks; **track-specific** syllabus, AI policy, quizzes, mid/final, project, portfolio |
| `IT_SUPPORT_HARDWARE` | 31 | same pattern; hardware-triage emphasis |

### Strengthened (non–gap tracks)
Group projects / glossaries / outcomes / references upgraded for SOFTWARE_BUILDER, COMM_PD_ETHICS, WIRELESS_6G, AI_ML_EDGE, CLOUD_DEVOPS, DATA_*, GAME_*, GENERAL_IT, HARDWARE_ENGINEERING, PM_AGILE_LSS, ROBOTICS_CONTROL, SEVEN_GC_APPRENTICESHIP, plus the two entry packages.

### Gap tracks (Agents 1–2)
Normalization helpers only (ai policy, glossary, refs, a11y, outcomes, HITL). Deep lessons/projects left for Agents 1–2 (`NETWORKING_INFRA`/`COMPUTER_NETWORKING`, `CYBER_SOC`/`CYBERSECURITY`, `EMBEDDED_PROTOTYPING`, `GUNNCHOS_PRODUCT_LAB`).

## Mission C
This summary file.

## File counts
| Item | Count |
|------|------:|
| Review packet files | 41 |
| DIGITAL_CONFIDENCE files | 31 |
| IT_SUPPORT_HARDWARE files | 31 |
| digital_rc package dirs | 21 |
| Required-file misses | 0 |

## Blockers
1. `SEVEN_GC_APPRENTICESHIP_HUMAN_ACADEMIC_REVIEW_PASS=false` until a human academic reviewer signs `12_reviewer_checklist.md`.
2. EXTERNAL human / physical / field / mentor / hardware / pilot / publication gates remain false by design.
3. Agents 1–2 still own deep curriculum for the four gap tracks (thin group projects intentionally untouched).
4. Sibling research repos may be UNAVAILABLE — fixture-only completion must remain valid.
5. `canonical_track_registry.v1.json` unchanged per mission; on-disk entry packages now exist for DIGITAL_CONFIDENCE / IT_SUPPORT_HARDWARE while registry maturity may still say `covered_via_shared_package`.
6. Concurrent writers briefly collided on entry-package assessments (symlinks); remediated to track-specific assessments — re-check if another agent re-symlinks.
