# Week 10: Prototype validation capstone — QEMU + DT + bus evidence

**Ticket:** EP-4A10  
**Lab:** `lab_ep_subsystem_capstone`

## Objectives
- Assemble digests from ≥6 prior labs
- Require qemu_ok and dt_ok
- Keep physical_status=PHYSICAL_PENDING unless EVT exists

## Body
Capstone validates the ForgeSense subsystem packet: memory map, GPIO, buses, ADC, ISR budget, QEMU boot, DT overlay, sleep honesty. Connectivity and device security show up as claim refusals, not as fake field trials.

Prototype validation means the next engineer can reopen your digests without tribal knowledge.

## Worked example
labs_passed≥6, qemu_ok=true, dt_ok=true, physical_status=PHYSICAL_PENDING

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No fabricated EVT completion
- No commercial standardized 6G
- No vendor cert grant

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_subsystem_capstone` and `EP-4A10`. Empty {} fails. A file whose body is only PASS raises.
