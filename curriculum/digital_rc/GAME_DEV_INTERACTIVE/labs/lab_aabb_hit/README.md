# lab_aabb_hit — aabb hit

Runnable validator for lab_aabb_hit. Empty/wrong/print-PASS fail.

## Student artifact
Piracy and flash_hz>3 fail.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From Forge Arcade, submit loop/collision/a11y JSON.
```
python3 scripts/run_course_labs.py --lab lab_aabb_hit --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_aabb_hit --empty
```

Wrong numeric or policy fields must fail.
