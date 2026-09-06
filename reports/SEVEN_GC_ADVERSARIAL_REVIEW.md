# SEVEN_GC_ADVERSARIAL_REVIEW

**Date:** 2026-09-06  
**Track:** SEVEN_GC_APPRENTICESHIP  
**Reviewer stance:** try to break honesty / clone / leakage claims

| ID | Attack | Result | Fix |
|---|---|---|---|
| SGC-A1 | Invented RF/field findings in labs | **Clean** — labs require SIMULATED labels; MEASURED_FIELD upgrades fail | N/A |
| SGC-A2 | Unlabeled simulation | **Clean** — fixture README + evidence_class checks | N/A |
| SGC-A3 | Fake mentor evidence | **Clean** — mentor_signed must be false; EXTERNAL_HUMAN_GATE | N/A |
| SGC-A4 | Dead lab commands | **Clean** — `run_course_labs.py` 160 labs ok; empty/wrong fail | N/A |
| SGC-A5 | Unrelated cloned WIRELESS content | **Clean** — original SGC tickets/stems; template detector PASS | N/A |
| SGC-A6 | Answer-key leakage | **Clean** — learner ingest has no answer_index | N/A |
| SGC-A7 | Unsupported certification claims | **Clean** — PUBLIC_REFERENCE_ONLY; certs aligned not granted | N/A |
| SGC-A8 | Broken provenance | **Clean** — PROVENANCE.md + alignment + discovery reports | N/A |
| SGC-A9 | Track-ID mismatch / collapse | **Clean** — stable UUID retained; not aliased into WIRELESS_6G | N/A |
| SGC-A10 | Taxonomy overclaim / field PASS | **Clean** — maturity digital_rc_present; EXTERNAL gates documented | N/A |
| SGC-A11 | Placeholder-only required content | **Clean** — student/instructor ready PASS; depth PASS | N/A |

## Open blockers (non-digital)
- EXTERNAL_HUMAN/PHYSICAL/FIELD gates remain open by design
- Platform PR #5 must not be repinned until this WAIKE PR is owner-merged

## Digital merge blockers
None remaining after local CI-equivalent gates.
