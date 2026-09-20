# Week 1: MCU memory map — flash vs SRAM before first boot

**Ticket:** EP-4101  
**Lab:** `lab_ep_memory_map`

## Objectives
- Distinguish flash vs SRAM roles on an nRF52840-class map
- Place vector table offset honestly
- Mark soldering/OTA as PHYSICAL_PENDING until EVT evidence exists

## Body
ForgeSense Subsystem Bench starts with a memory map, not a soldering iron. Flash holds firmware images; SRAM holds runtime state. Confusing the two is how learners invent 'I flashed SRAM' stories.

For this course's nRF52840-class fixture, treat flash_base as 0x00000000 and sram_base as 0x20000000 unless the lab fixture says otherwise. vector_table_offset is a relocatable detail you must report, not invent from a blog screenshot.

No-hardware fallback: submit the JSON map from the fixture sheet. QEMU later (week 7) boots without iron. PHYSICAL_PENDING covers soldering, carrier OTA, and any claim that a specific EVT board was flashed in class without evidence.

Zephyr and Nordic docs are PUBLIC_REFERENCE_ONLY. Your artifact is original WAIKE fixture wording with computed fields.

## Worked example
flash_base=0x00000000, sram_base=0x20000000, vector_table_offset=0x100, physical_status=PHYSICAL_PENDING

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming a physical flash without EVT evidence
- No vendor cert grant
- No fabricated field trial

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_memory_map` and `EP-4101`. Empty {} fails. A file whose body is only PASS raises.
