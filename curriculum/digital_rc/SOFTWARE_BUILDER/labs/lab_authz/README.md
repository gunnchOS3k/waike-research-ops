# lab_authz — authz

Runnable validator for lab_authz. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeDesk repo root, submit the JSON you computed.
```
python3 scripts/run_course_labs.py --lab lab_authz --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_authz --empty
```

Wrong numeric or policy fields must fail.
