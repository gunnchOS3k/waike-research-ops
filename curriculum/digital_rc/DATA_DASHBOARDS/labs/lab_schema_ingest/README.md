# lab_schema_ingest — schema ingest

DL-3101 Pier Ledger ingest: table pier_visits; columns include visit_id/pier_bay/ts_utc/headcount; row_count≥3; source_sha256; invented_columns false/[]. Distinct from DATA_VIZ_BI — schema before tiles.

## Student artifact
Required keys: table, columns, row_count, source_sha256, invented_columns.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Declare pier_visits schema and ingest DL-3101 CSV with hash.
```
python3 scripts/run_course_labs.py --lab lab_schema_ingest --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_schema_ingest --empty
```

## Wrong submissions
Wrong table, invented columns, tiny row_count, or missing sha fail.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
