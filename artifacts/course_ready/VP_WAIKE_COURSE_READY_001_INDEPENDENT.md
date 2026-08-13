# Independent VP — WAIKE-COURSE-READY-001 (DRAFT PR #43)

Verifier is not the implementer. Cursor does not merge. `REAL_STUDENT_E6=false`. `REAL_TEACHER_E6=false`. No device-os mega-PR. Next 15 courses not started.

| Gate | Verdict |
|---|---|
| GENERAL_IT | **FAIL** |
| COMPUTER_NETWORKING | **FAIL** |
| CYBERSECURITY | **FAIL** |
| BATCH | **FAIL** |
| COURSE_DIGITAL_RC (independent) | **false — not earned** |
| Edmund-mergeable | **NO** |

Live tip `ce364e27e817a3b2f6c3cb579c346a9cb9d10a1e` matches claimed. CI `docs` + `digital_rc_batch` SUCCESS. `docs` is `test -f README.md`.

## Count table (independent recount)

Same columns as implementer, plus distinctness columns the claim omitted.

| course | syllabus | weeks | full_lessons | assignments | runnable_labs | quizzes | quiz_items | unique stems | mid | mid original | final | final original | practicals | projects | rubrics | answer_keys | student | instructor | presentation | offline | portfolio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GENERAL_IT | 1 | 10 | 10 | 10 | 7 | 10 | 60 | 60 | 20 | **0** | 24 | **0** | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 |
| COMPUTER_NETWORKING | 1 | 10 | 10 | 10 | 6 | 10 | 60 | 60 | 20 | **0** | 24 | **0** | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 |
| CYBERSECURITY | 1 | 10 | 10 | 10 | 7 | 10 | 60 | 60 | 20 | **0** | 24 | **0** | 1 | 1 | 8 | 13 | 1 | 11 | 10 | 1 | 1 |

File counts match the implementer table. Weekly 60 stems are distinct original WAIKE items. Mid and final are `extra_assessment_items()` clones of those weekly stems (relabeled ids only).

## Challenges

1. **Live tip / CI — PASS.** Tip match. CI green. Docs job is a README existence check.
2. **Full contents — FAIL.** Lessons are original (Civic Tech Desk / Packet Range / Harbor SOC), not swapped-noun copies of each other. Rubrics are byte-identical across courses. Lab READMEs and instructor notes are emit.py shells. Syllabus Duration / Assessments / Claim boundary are shared boilerplate. Cyber `answer_index` is **60/60 = B**. Networking **59/60 = B**.
3. **Provenance / dumps — MIXED.** No CompTIA/ISC2/Cisco item harvest in sampled stems. 16 registry sources with `reuse_class`. Implementer Jaccard-on-lessons (`0.0003`) does not inspect packaging, keys, or recycled exams. Independent template audit **FAIL**.
4. **Labs — PASS_WITH_FINDINGS.** Executed **20/20**. Negatives kiosk-with-sudo, wrong CIDR, bot-can-close **fail as required**. Validators compute; they do not only print PASS. Findings: `_fail_if_print_pass` never called; `no_attacker_word` and `no_network` are always-True; datapath `ttl1_would_drop` is `(1-1)==0`; default fixtures already pass without learner work.
5. **Keys — PASS.** Learner ingest/catalog has no `answer_index` / `answer_keys` / `explanation`. Teacher ingest has keys.
6. **Count distinctness — MIXED.** 60 weekly items are 60 distinct stems. Claimed 20 mid + 24 final are not original.
7. **Datapath / cyber sandbox — PASS_WITH_FINDINGS.** `lab_datapath` parses crafted Ethernet+IPv4 and does LPM (not a wrapper). TTL-1 check is a tautology. Cyber labs are repo fixtures only.
8. **Device-os — PASS.** No device-os curriculum duplication in this PR.
9. **COURSE_DIGITAL_RC — FAIL.** `write_course_digital_rc.py` rubber-stamps at weeks≥8, quiz_items≥48, labs≥4, mid≥8, final≥8, rubrics≥4, and trusts the implementer's own provenance detector. Not earned.

## Mapping

- IT → `DIGITAL_CONFIDENCE` + `IT_SUPPORT_HARDWARE`
- Networking → `NETWORKING_INFRA`
- Cyber → `CYBER_SOC`

## Remaining OPEN (14 tracks)

`SOFTWARE_BUILDER`, `DATA_DASHBOARDS`, `AI_ML_EDGE`, `EMBEDDED_PROTOTYPING`, `WIRELESS_6G`, `PM_AGILE_LSS`, `GAME_DEV_INTERACTIVE`, `SEVEN_GC_APPRENTICESHIP`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `ROBOTICS_CONTROL`, `GUNNCHOS_PRODUCT_LAB`, `HARDWARE_ENGINEERING`, `DATA_VIZ_BI`.

## Must-fix before RC

Author course-specific rubrics; write original mid/final items; balance answer keys; require learner-submitted lab fixtures; replace tautology checks; raise the RC writer to the claimed table and add template/distinctness gates.
