# Week 1: MCU memory map — flash vs SRAM before first boot

ForgeSense Subsystem Bench ticket EP-4101: MCU memory map — flash vs SRAM before first boot. Map the nRF52840-class memory regions for ForgeSense subsystem firmware. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from HARDWARE_ENGINEERING SPICE weeks — this course owns firmware/bus/QEMU path. Journal EP-4101: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Journal EP-4101: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs.

## Worked example

flash_base=0x00000000, sram_base=0x20000000, vector_table_offset=0x100
