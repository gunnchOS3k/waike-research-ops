# Week 5: ADC scaling — counts to millivolts

ForgeSense Subsystem Bench ticket EP-4505: ADC scaling — counts to millivolts. Convert 12-bit ADC count to millivolts with stated vref. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4505: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Millivolts equal raw multiplied by vref divided by 2^bits, so 2048 x 3300 / 4096 = 1650; dividing by 4095 instead gives about 1650.4, so record which convention you used, and remember that SAADC gain and reference settings change the effective full scale.

## Worked example

raw=2048, vref_mv=3300, resolution_bits=12, mv=1650
