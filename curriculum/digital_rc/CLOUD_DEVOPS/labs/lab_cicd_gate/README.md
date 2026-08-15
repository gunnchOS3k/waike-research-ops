# lab_cicd_gate — cicd gate

Runnable validator for lab_cicd_gate. Empty/wrong/print-PASS fail.

## Student artifact
World-writable keys and heroics fail.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeCloud folder, submit policy/math JSON.
```
python3 scripts/run_course_labs.py --lab lab_cicd_gate --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_cicd_gate --empty
```

Wrong numeric or policy fields must fail.
