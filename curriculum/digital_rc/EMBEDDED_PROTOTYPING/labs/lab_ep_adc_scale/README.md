# lab_ep_adc_scale

ADC counts to mV.

**Classification:** DIGITAL

## Student artifact
Keys: `raw, vref_mv, resolution_bits, mv`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_adc_scale --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_adc_scale --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
