# STREAM-B-PKT-002 — WAIKE owner tip (COMM_PD_ETHICS DIGITAL_RC)

## Tip
- Base: `cf30a41` (#49)
- Branch: `stream/b-pkt-002-comm-pd-digital-rc`

## Verify
```bash
python3 scripts/run_course_labs.py
python3 scripts/emit_digital_rc.py
python3 scripts/validate_curriculum_provenance.py
python3 scripts/detect_templated_courses.py
python3 scripts/prove_product_consumption.py
python3 scripts/write_course_digital_rc.py
python3 -m pytest tests/curriculum/test_batch005_comm_pd_ethics.py -q
python3 -c "import json; d=json.load(open('artifacts/COURSE_DIGITAL_RC.json')); assert d['courses']['COMM_PD_ETHICS']['COURSE_DIGITAL_RC'] is True; assert d['COURSE_DIGITAL_RC_BATCH'] is True"
test -f artifacts/stream_b/WAIKE_FULL_TAXONOMY_GAP_LEDGER.json
```

## Claims
- `COMM_PD_ETHICS_COURSE_DIGITAL_RC=true` (full package bar)
- Taxonomy ledger ranks `DATA_DASHBOARDS` next for B-PKT-003 (not started)
- REAL_STUDENT_E6 / REAL_TEACHER_E6 / HUMAN_E6 = false
- Cursor NEVER merges

## Key leak check
Learner ingest must not contain `answer_keys` / `instructor_keys` / `answer_index` markers as key fields (policy prose scrubbed to avoid false positives).
