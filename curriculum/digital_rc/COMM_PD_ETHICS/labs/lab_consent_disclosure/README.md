# lab_consent_disclosure — consent disclosure

Harbor Desk Voice consent card for ticket PD-2101. Students submit audience, purpose, data_classes (≥2, no ssn), retention_days > 0, opt_out_path, and ai_disclosure=true. Vague audience='everyone' fails. This is operational consent, not a wall poster.

## Student artifact
Required keys: audience, purpose, data_classes, retention_days, opt_out_path, ai_disclosure.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Write the PD-2101 consent JSON from the walk-up desk script.
```
python3 scripts/run_course_labs.py --lab lab_consent_disclosure --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_consent_disclosure --empty
```

## Wrong submissions
SSN classes, retention_days=0, blank opt-out, or ai_disclosure false must fail.
