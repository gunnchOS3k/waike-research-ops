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
