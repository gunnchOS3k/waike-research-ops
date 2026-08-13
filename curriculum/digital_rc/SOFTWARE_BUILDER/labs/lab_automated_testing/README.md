# lab_automated_testing — automated testing

Runnable validator for lab_automated_testing. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeDesk repo root, submit the JSON you computed.
```
python3 scripts/run_course_labs.py --lab lab_automated_testing --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_automated_testing --empty
```

Wrong numeric or policy fields must fail.
