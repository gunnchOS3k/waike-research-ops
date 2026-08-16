# lab_pd_capstone — PD capstone

PD-2A30 ship checklist: labs_passed ≥6; consent_ok, conflict_ok, a11y_ok, no_key_leak true; fabricated_impact false. Portfolio claim boundary stays digital-fixture only; REAL_*_E6 false.

## Student artifact
Required keys: labs_passed, consent_ok, conflict_ok, a11y_ok, no_key_leak, fabricated_impact.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Assemble the PD-2A30 ship checklist from prior lab evidence.
```
python3 scripts/run_course_labs.py --lab lab_pd_capstone --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_pd_capstone --empty
```

## Wrong submissions
labs_passed<6, any honesty flag false, or fabricated_impact true fail.
