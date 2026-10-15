# lab_kpi_calc — KPI calc

DL-3409 NO_AI: avg_headcount>0; p95≥avg; n≥3; fabricated_lift false.

## Student artifact
Required keys: avg_headcount, p95_headcount, n, fabricated_lift.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Hand-calc avg and p95 for DL-3409 under NO_AI.
```
python3 scripts/run_course_labs.py --lab lab_kpi_calc --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_kpi_calc --empty
```

## Wrong submissions
fabricated_lift true or non-positive avg fail.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
