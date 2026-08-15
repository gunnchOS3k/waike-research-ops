# lab_four_games_case — four games case

Runnable validator for lab_four_games_case. Empty/wrong/print-PASS fail.

## Student artifact
Piracy and flash_hz>3 fail.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From Forge Arcade, submit loop/collision/a11y JSON.
```
python3 scripts/run_course_labs.py --lab lab_four_games_case --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_four_games_case --empty
```

Wrong numeric or policy fields must fail.
