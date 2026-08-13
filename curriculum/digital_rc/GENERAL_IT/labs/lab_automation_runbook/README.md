# lab_automation_runbook — CHG-88 dry-run

Snapshot first. Planned minute inside 18:00–21:00. executed must equal steps.

## Student artifact
Keys: `change_id, planned_min, steps, rollback, executed`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_automation_runbook --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_automation_runbook --empty
```

Apply-then-snapshot, or a 10:00 plan, fails.
