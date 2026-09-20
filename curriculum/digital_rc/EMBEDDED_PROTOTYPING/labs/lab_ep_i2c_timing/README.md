# lab_ep_i2c_timing

I2C timing + NACK plan.

**Classification:** DIGITAL

## Student artifact
Keys: `bus, addr, freq_khz, nack_recovery`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_i2c_timing --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_i2c_timing --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
