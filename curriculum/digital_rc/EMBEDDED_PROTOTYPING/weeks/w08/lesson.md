# Week 8: Devicetree overlay — I2C1 and LED0 nodes

ForgeSense Subsystem Bench ticket EP-4808: Devicetree overlay — I2C1 and LED0 nodes. Overlay enables &i2c1 and led0; deleting &soc is unsafe. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4808: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Journal EP-4808: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs.

## Worked example

overlay_has_i2c1=true, overlay_has_led0=true, delete_soc=false
