# lab_professional_comm — professional communication

PD-2307 professional ticket. Channel must be email|ticket|slack_work. Subject ≥8, body ≥80 with observation and next action. demeaning_labels and promises_outcome must be false. Banned body tokens include stupid/lazy/hopeless/idiot.

## Student artifact
Required keys: channel, subject, body, demeaning_labels, promises_outcome.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Draft the PD-2307 ticket body from the idle-logout observation.
```
python3 scripts/run_course_labs.py --lab lab_professional_comm --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_professional_comm --empty
```

## Wrong submissions
SMS channel, demeaning labels, outcome promises, or banned body words fail.
