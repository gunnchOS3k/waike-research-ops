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
