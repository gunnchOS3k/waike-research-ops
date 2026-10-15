# lab_debug_pipeline — debug pipeline

DL-3822 failed_stage∈{ingest,transform,calc,chart}; error_code; fix_action≥12; stage_rerun_ok true.

## Student artifact
Required keys: failed_stage, error_code, fix_action, stage_rerun_ok.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Name failed_stage and fix for DL-3822; rerun ok.
```
python3 scripts/run_course_labs.py --lab lab_debug_pipeline --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_debug_pipeline --empty
```

## Wrong submissions
Unknown stage, short fix, or stage_rerun_ok false fail.

## Execution and evidence boundary — current continuation

This historical JSON contract checks learner declarations and broad field constraints. It does not independently ingest source CSV bytes, execute the submitted SQL, inspect a rendered chart, certify privacy, or establish mastery. Use this course’s downloadable `learner_exercises/pier_ledger/README.md` for the actual local CSV/SQLite workflow, source hash, changed-input results and independent review criteria. Keep original lab IDs and existing Hub assignment records. A computed report supplements this contract; it does not silently change its schema or award a grade.
