# lab_ep_dt_overlay

Devicetree overlay contract.

**Classification:** DIGITAL

## Student artifact
Keys: `overlay_has_i2c1, overlay_has_led0, delete_soc`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_dt_overlay --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_dt_overlay --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
