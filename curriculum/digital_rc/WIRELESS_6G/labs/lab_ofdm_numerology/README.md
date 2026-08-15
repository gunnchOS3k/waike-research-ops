# lab_ofdm_numerology — ofdm numerology

Runnable validator for lab_ofdm_numerology. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS raises. No commercial 6G.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the Pier Radio Bench folder, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_ofdm_numerology --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ofdm_numerology --empty
```

Wrong numeric or policy fields must fail.
