# lab_ops_runbook — Network ops runbook — Yard to Roof path

Document symptom, ordered checks, escalate_if. fabricated_outage must be false.

## Student artifact
Keys: `symptom, checks, escalate_if, fabricated_outage`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_ops_runbook --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ops_runbook --empty
```

fabricated_outage=true fails honesty gate.
