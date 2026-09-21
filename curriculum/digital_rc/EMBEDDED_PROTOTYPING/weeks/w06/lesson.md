# Week 6: ISR vs polling — latency budget

ForgeSense Subsystem Bench ticket EP-4606: ISR vs polling — latency budget. Choose ISR when edge latency must stay under 250 µs. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4606: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Journal EP-4606: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs.

## Worked example

mode=isr, max_latency_us=250, missed_edges=0
