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

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
