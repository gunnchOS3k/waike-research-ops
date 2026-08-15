# lab_mcs_bler — mcs bler

Runnable validator for lab_mcs_bler. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS raises. No commercial 6G.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the Pier Radio Bench folder, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_mcs_bler --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_mcs_bler --empty
```

Wrong numeric or policy fields must fail.
