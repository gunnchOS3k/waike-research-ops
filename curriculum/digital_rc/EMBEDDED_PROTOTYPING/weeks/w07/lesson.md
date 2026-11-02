# Week 7: Zephyr west + QEMU — digital boot before iron

ForgeSense Subsystem Bench ticket EP-4707: Zephyr west + QEMU — digital boot before iron. west build -b qemu_cortex_m0; no board flash claim without EVT. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4707: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Build with west build -b qemu_cortex_m0 and run it with west build -t run; a QEMU boot proves the toolchain, kernel init and console path, but it says nothing about pin timing, radio behaviour or current draw.

## Worked example

board=qemu_cortex_m0, qemu_ok=true, physical_status=PHYSICAL_PENDING
