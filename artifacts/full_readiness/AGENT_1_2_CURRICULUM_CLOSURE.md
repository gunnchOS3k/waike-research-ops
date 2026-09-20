# Agent 1+2 — Curriculum / instructor / learner closure

**Worktree:** `waike-research-ops/.worktrees/18-track-full-readiness-closure`  
**Agent role:** Agent 1+2 (curriculum readiness for four tracks)  
**Registry:** `curriculum/taxonomy/canonical_track_registry.v1.json` **not modified** (control agent owns it).  
**No merge / push / PR** from this agent.

## Tracks closed

| Canonical track | Addressable package | Shared / legacy content |
|---|---|---|
| NETWORKING_INFRA | `curriculum/digital_rc/NETWORKING_INFRA/` | content_ref → `COMPUTER_NETWORKING/` |
| CYBER_SOC | `curriculum/digital_rc/CYBER_SOC/` | content_ref → `CYBERSECURITY/` |
| EMBEDDED_PROTOTYPING | `curriculum/digital_rc/EMBEDDED_PROTOTYPING/` | deepened in place |
| GUNNCHOS_PRODUCT_LAB | `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/` | deepened in place |

## What changed

### A. Independent entry packages (no blind full-tree duplication)

- Created **NETWORKING_INFRA** and **CYBER_SOC** as independently addressable entry packages.
- Each has own `course.json` (`course_id` = canonical track id, `track_id`, `version` `1.0.0`, `track_ids`, provenance, counts, `ai_use_policy` ref), `syllabus.md`, `ai_use_policy.json`, `student/`, `instructor/` (packet states **answer_keys not in learner ingest**), `portfolio/` (including **`outcomes.json`**), `assessments/`, quizzes, assignments, rubrics, projects, glossary, references, accessibility notes.
- Weeks use **content_ref** into legacy `weeks/wXX/lesson.md` plus track overlay (objectives, assessment mode, claim refusals).
- Labs use **lab_content_ref** / `labs/<id>/lab.json` pointing at legacy lab bodies; validators remain in `src/waike_course_ready/`.

### B. Legacy deepen + labs → 10

**COMPUTER_NETWORKING / NETWORKING_INFRA coverage:** models, Ethernet/L2, IP/subnetting, routing, switching, DNS/DHCP, transport, Wi-Fi fundamentals, troubleshooting, authorized fixture capture, security basics, modern ops — safe/local only.

New runnable labs (batch009):

- `lab_wifi_fundamentals` (DIGITAL)
- `lab_transport_ports` (DIGITAL)
- `lab_packet_capture_fixture` (SIMULATED; `authorized_fixture=true`)
- `lab_ops_runbook` (DIGITAL)

**CYBERSECURITY / CYBER_SOC coverage:** foundations, threat models, IAM, telemetry/SIEM, phishing **defense**, incident lifecycle, detection/triage, safe DFIR, vuln **concepts** (toy parser bounds checks), secure config, ethics/legal — **defensive sandboxed only**.

New runnable labs (batch009):

- `lab_phishing_defense` (DIGITAL; `no_credential_harvest=true`)
- `lab_threat_model` (DIGITAL; `offensive_scope=none`)
- `lab_secure_config_audit` (DIGITAL; `live_scan=false`)

Wired in `src/waike_course_ready/batch009/labs.py` and imported from `labs.py`. Smoke: reference submissions pass; empty `{}` fails.

### C. EMBEDDED_PROTOTYPING + GUNNCHOS_PRODUCT_LAB deepen

- Replaced repetitive ~1 kB template lessons with structured authored lessons: objectives, body, worked example, assessment mode, claim refusals, journal prompt.
- All 10 labs have `lab.json` **classification** (`DIGITAL` | `SIMULATED` | `OPTIONAL_PHYSICAL`).
- Added/updated: `portfolio/outcomes.json`, `glossary.md`, `references.md`, `accessibility_notes.md`, stronger student/instructor packets, syllabus, `course.json` `version`/`track_id`.
- EMBEDDED: MCU, GPIO, sensors/buses, ADC, ISR/realtime, QEMU build path, DT, power/sleep, device security, prototype validation, no-hardware fallbacks, **PHYSICAL_PENDING**.
- GUNNCHOS: requirements/charter, user stories/FSM, architecture/compat pins, Device OS compose, privacy/security, guest protocol, release eng, CI/a11y tokens, dep pins/telemetry honesty, product validation — real gunnchOS concepts; **no fabricated EVT**; **PHYSICAL_PENDING** where needed.

### D. Required artifact checklist (addressable packages)

For NETWORKING_INFRA, CYBER_SOC, EMBEDDED_PROTOTYPING, GUNNCHOS_PRODUCT_LAB:

- [x] syllabus.md  
- [x] 10 week lessons with objectives  
- [x] labs (10 canonical in `course.json`) + classification metadata  
- [x] assignments, quizzes, summative assessments  
- [x] capstone/project (`projects/group_project.md`)  
- [x] rubrics with criteria  
- [x] student/STUDENT_PACKET.md  
- [x] instructor/INSTRUCTOR_PACKET.md (answer_keys not in learner ingest)  
- [x] instructor/answer_keys.json  
- [x] portfolio/outcomes.json  
- [x] career_mapping.json  
- [x] glossary.md  
- [x] references.md (primary/official only)  
- [x] accessibility_notes.md  
- [x] ai_use_policy.json  

## Honesty limits (remaining)

1. **PHYSICAL_PENDING / OPTIONAL_PHYSICAL** — no fabricated EVT, solder, OTA, or carrier evidence is claimed.
2. **Certs aligned not granted** — CCNA / ISC2 CC / Security+ topic labels only.
3. **CYBER_SOC defensive only** — no exploit kits, malware instructions, credential harvesting, or unauthorized scanning; toy parser is bounds-check education on course fixtures.
4. **Shared content_ref** — entry packages intentionally do not duplicate entire legacy trees; ingest tooling must resolve `content_ref` / `lab_content_ref`.
5. **Registry sync** — control agent must point canonical package paths at `NETWORKING_INFRA/` and `CYBER_SOC/` when ready; this agent did not edit the registry.
6. **Parallel extras** — additional lab dirs (e.g. `lab_dhcp_lease_math`, `lab_ethics_boundary`) may exist from concurrent work; canonical `course.json` `labs` arrays list the ten readiness labs above.
7. **Answer keys** for brand-new lab items may still be instructor-process / reference-submission driven via `REFERENCE` in labs.py rather than exhaustive per-item quiz keys.
8. **No live community / field validation** claimed.

## Blockers

- **None blocking package readiness** inside this worktree for the four tracks.
- **Follow-up (control agent):** register `curriculum/digital_rc/NETWORKING_INFRA/course.json` and `CYBER_SOC/course.json` in the canonical track registry when appropriate.
- **Follow-up (ingest):** confirm learner pack builder resolves `content_ref` and excludes `instructor/answer_keys.json`.

## Key paths touched

- `curriculum/digital_rc/NETWORKING_INFRA/**` (new entry)
- `curriculum/digital_rc/CYBER_SOC/**` (new entry)
- `curriculum/digital_rc/COMPUTER_NETWORKING/**` (labs + policy + glossary/refs/outcomes)
- `curriculum/digital_rc/CYBERSECURITY/**` (labs + policy + glossary/refs/outcomes)
- `curriculum/digital_rc/EMBEDDED_PROTOTYPING/**` (lessons/labs/packets/outcomes)
- `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/**` (lessons/labs/packets/outcomes)
- `src/waike_course_ready/batch009/**` + `src/waike_course_ready/labs.py` (wire-up)
- `artifacts/full_readiness/AGENT_1_2_CURRICULUM_CLOSURE.md` (this file)
