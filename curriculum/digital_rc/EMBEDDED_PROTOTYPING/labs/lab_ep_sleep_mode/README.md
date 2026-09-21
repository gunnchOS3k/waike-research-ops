# lab_ep_sleep_mode

Sleep/wake honesty.

**Classification:** DIGITAL

## Student artifact
Keys: `sleep_mode, wake_gpio, wake_latency_ms`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_sleep_mode --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_sleep_mode --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
