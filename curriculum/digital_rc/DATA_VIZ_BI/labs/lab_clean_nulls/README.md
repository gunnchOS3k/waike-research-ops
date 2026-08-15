# lab_clean_nulls — clean nulls

Runnable validator for lab_clean_nulls. Empty/wrong/print-PASS fail.

## Student artifact
Wrong rates/joins fail. No piracy.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the Civic Metrics Studio folder, submit fixture JSON.
```
python3 scripts/run_course_labs.py --lab lab_clean_nulls --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_clean_nulls --empty
```

Wrong numeric or policy fields must fail.
