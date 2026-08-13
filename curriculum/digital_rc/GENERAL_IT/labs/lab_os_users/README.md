# lab_os_users — Civic kiosk accounts

Build a three-account desk store. `kiosk` must not be in sudo/root. `desk.lead` must sit in helpdesk. Unique UID and home. Submitting nothing, or cloning UID 1020 onto sat.am, fails.

## Student artifact
Keys: `users`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_os_users --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_os_users --empty
```

A kiosk with sudo=true is an automatic fail (same as the package negative).
