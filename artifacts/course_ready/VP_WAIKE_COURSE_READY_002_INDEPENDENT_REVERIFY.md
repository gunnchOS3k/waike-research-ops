# Independent re-verify — WAIKE-COURSE-READY-002 DRAFT #44

Prior FAIL VP `58d50aa` (tip `42cb9c8`) remains an ancestor. Live tip `7b130f06457105f93f9a4bc066b3aa032c33a713` matches claimed. Cursor does not merge. `REAL_STUDENT_E6=false`. `REAL_TEACHER_E6=false`. WAIKE-003 not started.

| Gate | Verdict |
|---|---|
| SOFTWARE_BUILDER | **PASS** |
| HARDWARE_ENGINEERING (+EMBEDDED_PROTOTYPING integrated) | **PASS** |
| PM_AGILE_LSS | **PASS** |
| #43 coexistence (GENERAL_IT / COMPUTER_NETWORKING / CYBERSECURITY) | **PASS** |
| BATCH | **PASS** |
| COURSE_DIGITAL_RC | **true — earned for this 6-course DRAFT product set** |
| Edmund-mergeable | **YES** (Cursor still does not merge) |

## Prior FAIL items — independent re-challenge

| Claimed fix | Independent result |
|---|---|
| pytest 10/10 | **10 passed** (`PYTEST_EXIT:0`) |
| Catalog/COURSES 6 courses | Live+committed catalog/learner/teacher all list all **6** ids; `COURSES = {**COURSES_001, **COURSES_002}` |
| `run_all` lab_count 50 | **50**; `COURSE_LABS.update` (no clear); batch-001 **20/20** gold+empty-fail via `reference_submission`; batch-002 **30/30** gold/empty/wrong/print-PASS |
| Stripped lesson mins SW860/HW875/PM864 | **860 / 875 / 864**; operator-note count **0**; evidence-discipline spam **0**; unique heads **10/10** |
| #43 still on product paths | Confirmed in catalog + ingest |
| FAIL VP ancestor | `58d50aa` ⊂ HEAD |

## Exam restatement (independent, batch-002 mid/final)

Tokenizer `[a-z0-9]+`.

| course | j=1.0 | Jaccard≥0.80 | worst |
|---|---:|---:|---:|
| SOFTWARE_BUILDER | **0** | **0** | 0.40 (`swf23`) |
| HARDWARE_ENGINEERING | **0** | **0** | 0.75 (`hwm15`) |
| PM_AGILE_LSS | **0** | **0** | 0.7143 (`pmm12`) |
| **BATCH-002** | **0** | **0** | **0.75** |

Injected clone gate: weekly stem as exam → token-identical **true**, j=**1.0**. Gate is real.

## Keys / packaging / policy

- A/B/C/D **26/26/26/26** per batch-002 course (n=104). Learner ingest has no `answer_index`/`answer_keys`. Teacher has both.
- Provenance audit **PASS**; packaging worst Jaccard **0.092**; `BATCH_TEMPLATED_COURSES=0`.
- PMI ATP false-claim scan: **0** hits. PHYSICAL_PENDING labeled. AI-use policy modes present.
- Counts: 10/10/10/10/60/20/24/8/13 packet still exact for batch-002.

## Labs

**50/50** via `run_all` (ok, empty/wrong/print-PASS/no-sub negatives hold; computed-honesty gate true). Batch-002 alone **30/30** with full negatives. Batch-001 sample+full **20/20** still runnable.

## OPEN tracks (do not start WAIKE-003)

`DATA_DASHBOARDS`, `AI_ML_EDGE`, `WIRELESS_6G`, `GAME_DEV_INTERACTIVE`, `SEVEN_GC_APPRENTICESHIP`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `ROBOTICS_CONTROL`, `GUNNCHOS_PRODUCT_LAB`, `DATA_VIZ_BI`. `EMBEDDED_PROTOTYPING` remains integrated into HARDWARE_ENGINEERING (no separate tree).

Residuals (not FAIL): worst exam-weekly Jaccard 0.75; docs CI still README existence; software validators remain JSON-artifact domain checks (same family as #43).

**Tip verified:** `7b130f06457105f93f9a4bc066b3aa032c33a713`
