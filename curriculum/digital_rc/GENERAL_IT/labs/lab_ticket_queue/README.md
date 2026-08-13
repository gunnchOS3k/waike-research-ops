# lab_ticket_queue — Tickets 4417/4418/4419

reboot_and_hope is never a next-action. 4417 idle math is 1200 seconds.

## Student artifact
Keys: `tickets`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_ticket_queue --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ticket_queue --empty
```

Three reboots score three zeros.
