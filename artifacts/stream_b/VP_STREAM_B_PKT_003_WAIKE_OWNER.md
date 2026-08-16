# STREAM-B-PKT-003 — WAIKE owner tip (DATA_DASHBOARDS DIGITAL_RC)

## Tip
- Base: `5a3cf859` (#50 COMM_PD merge)
- Branch: `stream/b-pkt-003-data-dashboards-digital-rc`

## Verify
```bash
python3 scripts/run_course_labs.py
python3 scripts/emit_digital_rc.py
python3 scripts/validate_curriculum_provenance.py
python3 scripts/detect_templated_courses.py
python3 scripts/prove_product_consumption.py
python3 scripts/write_course_digital_rc.py
python3 -m pytest tests/curriculum/test_batch006_data_dashboards.py tests/curriculum/test_digital_rc_batch.py -q
python3 -c "import json; d=json.load(open('artifacts/COURSE_DIGITAL_RC.json')); assert d['courses']['DATA_DASHBOARDS']['COURSE_DIGITAL_RC'] is True; assert d['DATA_DASHBOARDS_COURSE_DIGITAL_RC'] is True; assert d['COURSE_DIGITAL_RC_BATCH'] is True; assert d['REAL_STUDENT_E6'] is False; assert d['REAL_TEACHER_E6'] is False"
test -f artifacts/stream_b/WAIKE_FULL_TAXONOMY_GAP_LEDGER.json
```

## Claims
- `DATA_DASHBOARDS_COURSE_DIGITAL_RC=true` (full package bar; distinct from DATA_VIZ_BI)
- Taxonomy ledger: DATA_DASHBOARDS earned; next remaining EMBEDDED_PROTOTYPING (B-PKT-004 not started)
- REAL_STUDENT_E6 / REAL_TEACHER_E6 / HUMAN_E6 = false
- Cursor NEVER merges

## Key leak check
Learner ingest must not contain `answer_keys` / `answer_index` markers as key fields.

## Package notes
- Batch006 Pier Ledger Bench: 10 machine-verifiable labs (ingest/SQL/transform/KPI/chart/join/PII/debug/freshness/capstone)
- `test_digital_rc_batch` expects `len(COURSES)==14` with `BATCH_006={DATA_DASHBOARDS}`
- lab_count ≥130 / batch_006_lab_count==10
