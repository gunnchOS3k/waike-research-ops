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
