# lab_ep_zephyr_qemu

QEMU boot before iron.

**Classification:** SIMULATED

## Student artifact
Keys: `board, qemu_ok, physical_status`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_zephyr_qemu --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_zephyr_qemu --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
