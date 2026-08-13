# Independent re-verify — WAIKE-COURSE-READY-001 DRAFT #43

Prior FAIL VP `b78ba4b` is still in history. Live tip `494a4af` matches claimed. Cursor does not merge. `REAL_STUDENT_E6=false`. `REAL_TEACHER_E6=false`. Next 14 courses not started.

| Gate | Verdict |
|---|---|
| GENERAL_IT | **FAIL** |
| COMPUTER_NETWORKING | **FAIL** |
| CYBERSECURITY | **FAIL** |
| BATCH | **FAIL** |
| COURSE_DIGITAL_RC (independent) | **false — not earned** |
| Edmund-mergeable | **NO** |

CI `docs` + `digital_rc_batch` SUCCESS on `494a4af`. Docs job remains `test -f README.md`.

## What actually got fixed (do not ignore)

- Labs **20/20** with student JSON required. Empty `{}`, no submission, wrong fixtures, and print-`PASS` fail. kiosk-with-sudo / wrong CIDR / bot-can-close fail. SIEM note must contain `burst` and not `attacker`. TTL=1 is parsed from IP header byte then decremented. Socket guard + `targets==[course_ctf_fixture]`.
- Keys **A/B/C/D = 26/26/26/26** per course (104 items). Not collapsed.
- Packaging is domain-specific: 3 unique lab rubrics, 20/20 unique lab READMEs, 30/30 unique instructor week notes. Independent packaging Jaccard **0.0249**.
- Learner ingest still has no `answer_index` / `answer_keys`. Teacher ingest has keys.
- Mechanical weekly-dict clone in `extra_assessment_items()` is gone.

## What still fails (why RC is not earned)

Claimed “20+24 original, not weekly clones” is **exact-string** true and **substance** false.

Independent token Jaccard vs weekly stems:

| course | exact clones | j=1.0 restatements | j≥0.80 near-clones |
|---|---:|---:|---:|
| GENERAL_IT | 0 | 0 | 3 |
| COMPUTER_NETWORKING | 0 | **7** | 9 |
| CYBERSECURITY | 0 | **3** | 8 |

Examples on disk:

- Weekly `Access port vs trunk in one line` → mid `Access port vs trunk in one line?`
- Weekly `MAC flapping is evidence of` → final `MAC flapping is evidence of?`
- Weekly `Library PANs in the model context window` → mid `Library PANs in the model context window?`

Implementer provenance only rejects exact stem match and `Mid-course check:` / `Capstone check:` prefixes. That is why their detector still says PASS.

## Count table (independent)

File counts match the claimed table. Weekly 60 unique stems kept. Mid 20 / final 24 exist and are exact-string-distinct from weekly. They are not original enough to earn RC.

| course | syllabus | weeks | lessons | asg | labs | quizzes | quiz items | unique weekly | mid | mid exact-new | final | final exact-new | prac | proj | rubrics | keys | student | instr | slides | offline | port | A/B/C/D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GENERAL_IT | 1 | 10 | 10 | 10 | 7 | 10 | 60 | 60 | 20 | 20 | 24 | 24 | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 | 26/26/26/26 |
| NETWORKING | 1 | 10 | 10 | 10 | 6 | 10 | 60 | 60 | 20 | 20 | 24 | 24 | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 | 26/26/26/26 |
| CYBER | 1 | 10 | 10 | 10 | 7 | 10 | 60 | 60 | 20 | 20 | 24 | 24 | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 | 26/26/26/26 |

## Remaining OPEN (14 tracks)

`SOFTWARE_BUILDER`, `DATA_DASHBOARDS`, `AI_ML_EDGE`, `EMBEDDED_PROTOTYPING`, `WIRELESS_6G`, `PM_AGILE_LSS`, `GAME_DEV_INTERACTIVE`, `SEVEN_GC_APPRENTICESHIP`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `ROBOTICS_CONTROL`, `GUNNCHOS_PRODUCT_LAB`, `HARDWARE_ENGINEERING`, `DATA_VIZ_BI`.

## Must-fix before RC

Rewrite the restated mid/final items (new tickets/numbers/topologies, not a trailing `?`). Near-duplicate gate in provenance. Raise RC writer floors from ≥8/≥48/≥4 to the claimed 10/60/6–7 table.
