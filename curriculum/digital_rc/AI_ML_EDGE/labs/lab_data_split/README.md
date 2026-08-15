# lab_data_split — data split

Runnable validator for lab_data_split. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the EdgeForge repo root, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_data_split --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_data_split --empty
```

Wrong numeric or policy fields must fail.
