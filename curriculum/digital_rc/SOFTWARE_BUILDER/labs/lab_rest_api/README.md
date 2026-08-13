# lab_rest_api — rest api

Runnable validator for lab_rest_api. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeDesk repo root, submit the JSON you computed.
```
python3 scripts/run_course_labs.py --lab lab_rest_api --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_rest_api --empty
```

Wrong numeric or policy fields must fail.
