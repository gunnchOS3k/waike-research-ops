# lab_ep_isr_vs_poll

ISR latency budget.

**Classification:** DIGITAL

## Student artifact
Keys: `mode, max_latency_us, missed_edges`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_isr_vs_poll --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_isr_vs_poll --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
