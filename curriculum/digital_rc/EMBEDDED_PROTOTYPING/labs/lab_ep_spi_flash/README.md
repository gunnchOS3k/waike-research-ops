# lab_ep_spi_flash

SPI read frame honesty.

**Classification:** DIGITAL

## Student artifact
Keys: `opcode, addr, read_len, crc_ok`.
Empty {} fails. PASS-only body fails.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_ep_spi_flash --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ep_spi_flash --empty
```

## No-hardware fallback
Submit fixture JSON. Mark PHYSICAL_PENDING for solder/OTA/EVT claims without evidence.
