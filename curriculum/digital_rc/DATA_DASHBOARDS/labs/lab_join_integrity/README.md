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
