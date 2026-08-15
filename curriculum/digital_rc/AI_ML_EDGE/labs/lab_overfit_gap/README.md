# lab_overfit_gap — overfit gap

Runnable validator for lab_overfit_gap. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the EdgeForge repo root, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_overfit_gap --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_overfit_gap --empty
```

Wrong numeric or policy fields must fail.
