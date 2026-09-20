# lab_ep_subsystem_capstone

Subsystem packet; physical optional.

**Classification:** OPTIONAL_PHYSICAL

## Student artifact
Keys: `labs_passed, qemu_ok, dt_ok, physical_status`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_subsystem_capstone --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_subsystem_capstone --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
