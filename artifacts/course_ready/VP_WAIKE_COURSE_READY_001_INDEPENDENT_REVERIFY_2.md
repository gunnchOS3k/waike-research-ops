# Independent re-verify 2 — WAIKE-COURSE-READY-001 DRAFT #43

Prior FAIL VPs `b78ba4b` and `df96166` remain ancestors. Live tip `3b81933` matches claimed. Cursor does not merge. `REAL_STUDENT_E6=false`. `REAL_TEACHER_E6=false`. Next 14 tracks not started.

| Gate | Verdict |
|---|---|
| GENERAL_IT | **PASS** |
| COMPUTER_NETWORKING | **PASS** |
| CYBERSECURITY | **PASS** |
| BATCH | **PASS** |
| COURSE_DIGITAL_RC | **true — earned for this 3-course DRAFT only** |
| Edmund-mergeable | **YES** (Cursor still does not merge) |

CI `docs` + `digital_rc_batch` SUCCESS. Docs job remains README existence.

## Exam restatement (independent, all mid/final)

Own tokenizer: `[a-z0-9]+` lowercase. Punctuation/`?` ignored.

| course | j=1.0 | Jaccard≥0.80 | worst |
|---|---:|---:|---:|
| GENERAL_IT | **0** | **0** | 0.6364 (`GENERAL_IT-mid-12`) |
| COMPUTER_NETWORKING | **0** | **0** | 0.7143 (`COMPUTER_NETWORKING-fin-08`) |
| CYBERSECURITY | **0** | **0** | 0.6667 (`CYBERSECURITY-mid-20`) |
| **BATCH** | **0** | **0** | **0.7143** |

Implementer claimed worst 0.6923 (apostrophe-preserving tokens). Independent alphanumeric worst is 0.7143. Both under 0.80. Not a FAIL.

Sampled rewrites are new scenarios, not trailing `?`:

- Access-port clone → `Gi1/0/8` untagged VLAN 20 vs trunk `Gi1/0/24`
- MAC-flap clone → `aa:aa:aa:aa:aa:10` flipping `Gi1/0/8`/`Gi1/0/12` every 200 ms
- PAN clone → Harbor-bot ticket **H-22** with a pasted library-card number
- IHL clone → Pier capture **byte 14 = 0x45**, skip how many bytes to TCP

## Injected clone gate

`Access port vs trunk in one line?` against weekly `Access port vs trunk in one line` → token-identical **true**, Jaccard **1.0**, `exam_is_restatement` **true**. Weekly+`?` fails. Gate is real.

## Labs

**20/20** executed. Empty `{}`, no submission, wrong fixtures, print-`PASS`, kiosk-with-sudo, wrong CIDR, bot-can-close, SIEM “attacker” note all fail. pytest 10 passed.

## Keys / packaging

A/B/C/D **26/26/26/26** per course (n=104). Learner ingest has no `answer_index`/`answer_keys`. Teacher ingest has keys. Packaging Jaccard **0.0249**. Weekly **60** unique stems kept.

## Counts

File table unchanged and still matches the claimed 10/10/10/6–7/10/60/20/24/8/13 packet.

## OPEN 14 tracks

`SOFTWARE_BUILDER`, `DATA_DASHBOARDS`, `AI_ML_EDGE`, `EMBEDDED_PROTOTYPING`, `WIRELESS_6G`, `PM_AGILE_LSS`, `GAME_DEV_INTERACTIVE`, `SEVEN_GC_APPRENTICESHIP`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `ROBOTICS_CONTROL`, `GUNNCHOS_PRODUCT_LAB`, `HARDWARE_ENGINEERING`, `DATA_VIZ_BI`.

Residuals (not FAIL): RC writer unused slack floors ≥8/≥48/≥4; docs CI is README existence; remaining exam-weekly Jaccard 0.7143.
