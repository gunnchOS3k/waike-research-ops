# Week 3: I2C timing — address, frequency, and NACK recovery

ForgeSense Subsystem Bench ticket EP-4303: I2C timing — address, frequency, and NACK recovery. SSD1306-class address 0x3C at 100 kHz with explicit NACK plan. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4303: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Journal EP-4303: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs.

## Worked example

bus=i2c1, addr=0x3C, freq_khz=100, nack_recovery=true
