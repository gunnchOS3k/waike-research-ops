# lab_freshness_sla — freshness SLA

DL-3925 NO_AI: sla_minutes=60; sla_ok matches lag≤sla; claim_live_when_stale false.

## Student artifact
Required keys: lag_minutes, sla_minutes, sla_ok, claim_live_when_stale.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Compute lag vs 60-minute SLA for DL-3925 under NO_AI.
```
python3 scripts/run_course_labs.py --lab lab_freshness_sla --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_freshness_sla --empty
```

## Wrong submissions
Dishonest sla_ok or stale live claim fail.
