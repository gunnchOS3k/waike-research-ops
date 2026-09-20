# lab_gpl_dep_pin

Dependency pin honesty.

**Classification:** DIGITAL

## Student artifact
Keys: `preview_sha_in_accepted, pin_file`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_gpl_dep_pin --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_gpl_dep_pin --empty
```

## Honesty
No fabricated community impact. PHYSICAL_PENDING for EVT/OTA/carrier without evidence. Do not treat unmerged device-os PRs as accepted pins.
