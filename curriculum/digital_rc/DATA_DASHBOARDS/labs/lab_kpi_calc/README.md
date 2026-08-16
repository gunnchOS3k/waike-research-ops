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
