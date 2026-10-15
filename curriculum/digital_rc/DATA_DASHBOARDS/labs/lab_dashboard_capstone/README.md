# lab_dashboard_capstone — dashboard capstone

DL-3A30 labs_passed≥6; schema/kpi/chart/pii/freshness/no_key_leak true; fabricated_lift false. REAL_*_E6 false.

## Student artifact
Required keys: labs_passed, schema_ok, kpi_ok, chart_ok, pii_ok, freshness_ok, no_key_leak, fabricated_lift.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Assemble DL-3A30 ship checklist from prior lab evidence.
```
python3 scripts/run_course_labs.py --lab lab_dashboard_capstone --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dashboard_capstone --empty
```

## Wrong submissions
labs_passed<6 or any honesty flag wrong fails.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
