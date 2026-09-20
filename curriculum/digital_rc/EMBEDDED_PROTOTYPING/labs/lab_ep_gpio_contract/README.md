# lab_ep_gpio_contract

GPIO contract before pinmux.

**Classification:** DIGITAL

## Student artifact
Keys: `pin, direction, default_level, pull`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_gpio_contract --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_gpio_contract --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
