# lab_conflict_interest — conflict of interest

PD-2204 conflict drill: mentoring plus scoring the same portfolio. Submit scenario (≥40 chars), conflict_present, disclose_to, recuse, and rationale (≥24). When conflict_present is true, recuse must be true after disclosure to the course lead.

## Student artifact
Required keys: scenario, conflict_present, disclose_to, recuse, rationale.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Author the PD-2204 disclose+recuse JSON before scoring starts.
```
python3 scripts/run_course_labs.py --lab lab_conflict_interest --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_conflict_interest --empty
```

## Wrong submissions
Short scenarios, empty disclose_to, or recuse=false while conflict_present=true fail.
