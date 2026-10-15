# lab_normalize_transform — normalize transform

DL-3307 normalize_map≥2 aliases; rows_out≤rows_in; null_rate 0..1; negatives_dropped true.

## Student artifact
Required keys: normalize_map, rows_in, rows_out, null_rate, negatives_dropped.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Map bay aliases and drop null/negative headcounts for DL-3307.
```
python3 scripts/run_course_labs.py --lab lab_normalize_transform --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_normalize_transform --empty
```

## Wrong submissions
Empty map, rows_out>rows_in, or negatives_dropped false fail.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
