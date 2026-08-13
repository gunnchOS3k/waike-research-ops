# lab_logic_gate — logic gate

Runnable validator for lab_logic_gate. Empty/wrong/print-PASS fail.

## Student artifact
Wrong arithmetic fails. PHYSICAL_PENDING stays pending.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeSense digital bench, submit computed values — not a GUI screenshot.
```
python3 scripts/run_course_labs.py --lab lab_logic_gate --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_logic_gate --empty
```

Wrong numeric or policy fields must fail.
