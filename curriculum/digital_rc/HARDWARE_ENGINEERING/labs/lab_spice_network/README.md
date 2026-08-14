# lab_spice_network — spice network

Runnable validator for lab_spice_network. Empty/wrong/print-PASS fail.

## Student artifact
Wrong arithmetic fails. PHYSICAL_PENDING stays pending.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the ForgeSense digital bench, submit computed values — not a GUI screenshot.
```
python3 scripts/run_course_labs.py --lab lab_spice_network --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_spice_network --empty
```

Wrong numeric or policy fields must fail.
