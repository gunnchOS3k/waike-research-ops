# lab_join_integrity — join integrity

DL-3615 join_key=pier_bay; join_type inner|left; orphan_count=0; duplicate_meta_keys false; rows_joined≥3.

## Student artifact
Required keys: join_key, join_type, orphan_count, duplicate_meta_keys, rows_joined.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Join visits to meta on pier_bay for DL-3615; report orphans.
```
python3 scripts/run_course_labs.py --lab lab_join_integrity --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_join_integrity --empty
```

## Wrong submissions
orphans, duplicate meta, or wrong join_key fail.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
