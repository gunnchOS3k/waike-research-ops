# Independent verify — WAIKE-COURSE-READY-002 DRAFT #44

**BATCH: FAIL.** Cursor does not merge. Tip `42cb9c807e171631763409108f07528fbbccfff6` matches local HEAD on `operating-cycle-user-ready/waike-course-ready-002`. Base `eb3f416` (#43 merge) confirmed. `REAL_STUDENT_E6=false`. `REAL_TEACHER_E6=false`. WAIKE-003 not started. GitHub API/CI status could not be fetched from this verifier host (403); local gates below are decisive.

| Gate | Verdict |
|---|---|
| SOFTWARE_BUILDER | **FAIL** (batch gates) |
| HARDWARE_ENGINEERING (+EMBEDDED_PROTOTYPING integrated) | **FAIL** (batch gates) |
| PM_AGILE_LSS | **FAIL** (batch gates) |
| BATCH | **FAIL** |
| COURSE_DIGITAL_RC | **false — not earned** |
| Edmund-mergeable | **NO** |

Owner `COURSE_DIGITAL_RC.json` / `VP_*_OWNER*` are **rubber-stamps** relative to independent evidence.

## Hard FAIL reasons (any one blocks RC)

1. **CI / pytest broken on tip.** `tests/curriculum/test_digital_rc_batch.py` → **2 failed, 8 passed** (`PYTEST_EXIT:1`).
   - `test_three_courses_only_in_batch` still asserts `{GENERAL_IT, COMPUTER_NETWORKING, CYBERSECURITY}`; active `COURSES` is batch-002 only.
   - `test_labs_compute_and_negatives_fail` asserts `lab_count == 20`; `run_all()` returns **30**.
   - Workflow `.github/workflows/ci.yml` job `digital_rc_batch` runs this pytest → tip cannot be green.

2. **Weakens #43 bar (explicit non-goal).**
   - `content.py`: `COURSES = COURSES_002` — emit/ingest/catalog **drop** GENERAL_IT / COMPUTER_NETWORKING / CYBERSECURITY.
   - Committed `ingest/learner`, `ingest/teacher`, `ingest/waike_product_catalog.ui.v1.json` list **only** the three batch-002 ids.
   - `labs.py`: `COURSE_LABS.clear(); COURSE_LABS.update(COURSE_LABS_002)` — `run_all()` no longer executes the **20** #43 labs (still in `LABS` dict, orphaned from COURSE_LABS / CI).
   - On-disk `curriculum/digital_rc/{GENERAL_IT,COMPUTER_NETWORKING,CYBERSECURITY}` remains, but **product consumption no longer surfaces them**. Owner “preserved_digital_rc_tracks” claim is false for the live product path.

3. **Lesson depth padding / JSON-completeness gaming (same class as #43 FAIL→PASS).**
   - Batch-002 lessons pad with **8×** identical `Operator note: record evidence…` (and HW/PM also **3×** `Evidence discipline week N…`) to clear `len(lesson) >= 800`.
   - #43 courses: **0** such repeats.
   - After stripping the operator-note pad only: SOFTWARE min **318**, HARDWARE min **586**, PM min **544** — **fail** the ≥800 depth bar the suite still claims to enforce.
   - Assignments/presentations are thinner than #43 medians (assign med ~125–174 vs ~213–251; pres med ~430–484 vs ~727–862).

## What passed under independent challenge (not enough for RC)

| Check | Result |
|---|---|
| Labs golden | **30/30** |
| Empty `{}` / no-sub / wrong fixtures | **30/30 fail as required** |
| print-`PASS` | **30/30 raise** |
| Mid/final token-identity vs weekly | **j=1.0 → 0** |
| Mid/final Jaccard ≥0.80 vs weekly | **0** (alphanumeric tokenizer `[a-z0-9]+`) |
| Worst exam↔weekly Jaccard | **0.75** (`HARDWARE_ENGINEERING` `hwm15`) — under 0.80 |
| Injected clone gate | weekly stem as exam → identical **true**, j=**1.0**, restatement **true** |
| Cross-course / vs-#43 quiz stem identical | **0**; worst cross Jaccard **0.60** |
| Noun-swapped assignment pairs ≥0.80 | **0** |
| Key balance | A/B/C/D **26/26/26/26** per course (n=104); not all-B |
| Keys in learner UI/ingest | **absent**; teacher ingest has keys |
| Cert dumps / PMI ATP false claim | No ATP claim; dump-like stems are *anti*-cert questions |
| Hardware PHYSICAL_PENDING / QEMU-west honesty | Present; no NDA leak found |
| PM fabricated-outcomes / ATP | Labs require `fabricated_outcomes=false`; syllabus NOT ATP |
| Packaging 5-gram Jaccard (independent full-tree) | worst batch pair **~0.056** (owner packaging shell **0.092**) |
| AI-use policy modes | Present on all three |

Software lab validators check **student JSON artifacts** with domain rules (status maps, workflow shape, digest pins, availability math). They do **not** spawn git/subprocess CI. Same family as several #43 JSON validators; **not** print-PASS wrappers. Residual only — not the merge blocker.

## Exact counts (filesystem audit)

| field | SW | HW | PM |
|---|---:|---:|---:|
| syllabus | 1 | 1 | 1 |
| weeks / lessons | 10 | 10 | 10 |
| assignments | 10 | 10 | 10 |
| runnable labs | 10 | 10 | 10 |
| quizzes / items | 10 / 60 | 10 / 60 | 10 / 60 |
| mid / final | 20 / 24 | 20 / 24 | 20 / 24 |
| practical / project | 1 / 1 | 1 / 1 | 1 / 1 |
| rubrics.md | 8 | 8 | 8 |
| answer_keys (emit formula `1+10+2`) | 13 | 13 | 13 |
| presentations | 10 | 10 | 10 |
| student / offline / portfolio / career / ai_policy | 1 each | 1 each | 1 each |
| instructor week notes | 10 (+ packet) | 10 (+ packet) | 10 (+ packet) |

File counts match the claim table. **Counts ≠ COURSE_DIGITAL_RC.**

## OPEN tracks (after this DRAFT — still OPEN; do not start WAIKE-003)

`DATA_DASHBOARDS`, `AI_ML_EDGE`, `WIRELESS_6G`, `GAME_DEV_INTERACTIVE`, `SEVEN_GC_APPRENTICESHIP`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `ROBOTICS_CONTROL`, `GUNNCHOS_PRODUCT_LAB`, `DATA_VIZ_BI`, and **re-open product preservation** for `GENERAL_IT` / `COMPUTER_NETWORKING` / `CYBERSECURITY` until ingest+COURSE_LABS include them again. `EMBEDDED_PROTOTYPING` remains integrated-only (no separate digital_rc tree) — track still needs an honest close when HW RC is earned.

## Required before re-verify

- Restore #43 courses in active `COURSES` **and** product ingest/catalog **alongside** batch-002 (union, not replace).
- Restore `COURSE_LABS` to **union** of batch-001 + batch-002; `run_all` must execute **50** labs (or explicitly keep #43 suite green).
- Update pytest expectations for the multi-batch registry; `digital_rc_batch` must pass.
- Remove lesson pad spam; earn ≥800 with real instructional prose (match #43 honesty).
- Only then re-stamp owner RC; independent re-verify.

**Local SHA if push blocked:** `42cb9c807e171631763409108f07528fbbccfff6`
