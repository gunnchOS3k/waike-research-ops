# Reference Track Quality Profile

**Audited:** 2026-09-20 against `origin/main` @ `c13179eaec0b23cf5a18b7dec9043e193bcb9460`  
**Floor (not ceiling):** SOFTWARE_BUILDER (software), HARDWARE_ENGINEERING / WIRELESS_6G (hardware/wireless), COMM_PD_ETHICS (professional/communication).

## Why these three (+ wireless)

| Track | Domain | Strength signals |
|---|---|---|
| SOFTWARE_BUILDER | Technical / software | Kinesthetic ForgeDesk narrative; week-specific lab IDs; explicit AI assessment modes; negative-path grading; original fixtures (not CS50 dumps) |
| WIRELESS_6G | Hardware / RF / systems | Claim refusals (no commercial-6G brochure); PUBLIC_REFERENCE_ONLY for 3GPP/IEEE; Friis/numerology worked examples |
| COMM_PD_ETHICS | Professional / communication | Harbor Desk Voice continuity; consent/recusal/AI disclosure; ethics without credential-grant claims |
| HARDWARE_ENGINEERING | Hardware engineering | SPICE/QEMU/Device Lab digital-before-physical; PHYSICAL_PENDING honesty |

## Patterns to copy (floor)

### Lesson depth
- Named ticket/lab_id in the lesson body
- Worked example with concrete tokens/numbers
- Explicit assessment AI mode (AI_ALLOWED / RESTRICTED / DISCLOSED / NO_AI)
- At least one claim the learner must refuse
- Domain-specific vocabulary (avoid noun-swapped clones across tracks)

### Lab format
- Executable validator or JSON fixture acceptance
- Empty `{}` fails; screenshot-only fails
- Classification: DIGITAL / SIMULATED / OPTIONAL_PHYSICAL / PHYSICAL / EXTERNAL
- Safety + fallback when physical

### Assignment structure
- Deliverable named (JSON/report/artifact id)
- Linked to week objective
- Integrity / disclosure footer when AI used

### Rubric structure
- Named criteria with levels/scores
- Separate lab / assignment / practical / project rubrics
- No single generic “did the thing” row as the only criterion

### Instructor packet
- Points to `instructor/answer_keys.json`
- States keys are **not** in learner ingest
- HITL / no publish-without-human
- Prep, pacing, misconceptions, UDL notes

### Student packet
- Syllabus pointer, materials, completion criteria, portfolio expectations, troubleshooting

### References
- Primary/official docs as PUBLIC_REFERENCE_ONLY labels
- No textbook reproduction; no fake DOIs; no invented standards versions

### Package schema
- `waike.course_package.v1` with `course_id`, `track_ids`, weeks[], labs, assessments, offline_pack_ref, provenance, counts
- Semver `package_version` required for digitally release-ready tracks

## Anti-patterns (reject)

- Noun-swapped labs across tracks
- Lessons that only restate the title + “journal the ticket”
- Rubrics without criteria
- Null `latest_compatible_package_version` while claiming digital RC
- Collapsing DIGITAL_CONFIDENCE / IT_SUPPORT_HARDWARE behind GENERAL_IT without independent entry points
- Claiming PHYSICAL labs validated without device evidence

## Application rule

Do not weaken SOFTWARE_BUILDER / WIRELESS_6G / COMM_PD_ETHICS to match thinner tracks. Raise thinner tracks toward this floor.
