# lab_services — Spooler and tracker

cupsd must be enabled+active with restart_sec ≤ 15. toy-tracker must be dead. This is the Civic image, not a generic 'enable a service' worksheet.

## Student artifact
Keys: `units`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_services --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_services --empty
```

Leaving toy-tracker active fails the classroom image.
