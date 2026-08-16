# lab_sql_select — SQL select

DL-3204 SELECT with WHERE; threshold=40; filter_count≥1; sql_text includes WHERE. SELECT * alone fails.

## Student artifact
Required keys: sql_text, filter_count, has_where, threshold.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Write the DL-3204 WHERE query and report filter_count.
```
python3 scripts/run_course_labs.py --lab lab_sql_select --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_sql_select --empty
```

## Wrong submissions
Missing WHERE, wrong threshold, or empty filter_count fail.
