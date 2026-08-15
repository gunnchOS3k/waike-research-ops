# lab_diff_drive — diff drive

Runnable validator for lab_diff_drive. Empty/wrong/print-PASS fail.

## Student artifact
Soft E-stop and B=0 fail.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From HarborBot Bay, submit kinematics/safety JSON.
```
python3 scripts/run_course_labs.py --lab lab_diff_drive --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_diff_drive --empty
```

Wrong numeric or policy fields must fail.
