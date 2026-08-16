# lab_consent_disclosure — consent disclosure

Runnable validator for lab_consent_disclosure. Empty/wrong/print-PASS fail. Harbor Desk Voice.

## Student artifact
Empty {} fails. PASS raises. Harbor Desk Voice ethics/PD fields must be honest.

## How to run
From the Harbor Desk Voice folder, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_consent_disclosure --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_consent_disclosure --empty
```

Wrong ethics/PD policy fields must fail.
