# Week 3: I2C timing — address, frequency, and NACK recovery

ForgeSense Subsystem Bench ticket EP-4303: I2C timing — address, frequency, and NACK recovery. SSD1306-class address 0x3C at 100 kHz with explicit NACK plan. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4303: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. A 7-bit address of 0x3C appears on the wire as 0x78 for a write and 0x79 for a read; an address NACK means the device is absent or the address is wrong, and a slave holding SDA low is released by clocking SCL up to nine times and then issuing a STOP.

## Worked example

bus=i2c1, addr=0x3C, freq_khz=100, nack_recovery=true
