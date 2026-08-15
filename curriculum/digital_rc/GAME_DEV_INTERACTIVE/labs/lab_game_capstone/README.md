# lab_game_capstone — game capstone

Runnable validator for lab_game_capstone. Empty/wrong/print-PASS fail.

## Student artifact
Piracy and flash_hz>3 fail.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From Forge Arcade, submit loop/collision/a11y JSON.
```
python3 scripts/run_course_labs.py --lab lab_game_capstone --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_game_capstone --empty
```

Wrong numeric or policy fields must fail.
