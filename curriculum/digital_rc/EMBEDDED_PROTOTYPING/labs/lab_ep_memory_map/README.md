# lab_ep_memory_map

MCU memory map fixture.

**Classification:** DIGITAL

## Student artifact
Keys: `flash_base, sram_base, vector_table_offset, physical_status`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_memory_map --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_memory_map --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
