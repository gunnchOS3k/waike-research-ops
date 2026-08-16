# lab_pii_redact_etl — PII redact ETL

DL-3718 redactions≥1; pii_remaining false; biometric_claim false; fields_redacted nonempty.

## Student artifact
Required keys: redactions, pii_remaining, biometric_claim, fields_redacted.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Redact email/phone before warehouse load on DL-3718.
```
python3 scripts/run_course_labs.py --lab lab_pii_redact_etl --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_pii_redact_etl --empty
```

## Wrong submissions
pii_remaining true or biometric_claim true fail.
