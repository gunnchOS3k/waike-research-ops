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
