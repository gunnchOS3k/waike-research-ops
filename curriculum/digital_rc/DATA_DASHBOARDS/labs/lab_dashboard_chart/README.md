# lab_dashboard_chart — dashboard chart

DL-3511 chart_type bar|line|scatter; x/y fields; title≥8; alt_text≥12; color_only false.

## Student artifact
Required keys: chart_type, x_field, y_field, title, alt_text, color_only.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Author the DL-3511 chart contract with alt_text.
```
python3 scripts/run_course_labs.py --lab lab_dashboard_chart --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dashboard_chart --empty
```

## Wrong submissions
color_only true, tiny alt_text, or missing axes fail.
