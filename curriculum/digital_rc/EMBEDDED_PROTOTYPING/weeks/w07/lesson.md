# Week 7: Firmware build/flash path — Zephyr west + QEMU

**Ticket:** EP-4707  
**Lab:** `lab_ep_zephyr_qemu`

## Objectives
- Record west build on qemu_cortex_m0 (or fixture-equivalent)
- Set qemu_ok true only when digital boot evidence exists
- Keep physical_status=PHYSICAL_PENDING without EVT flash evidence

## Body
Digital-first firmware path: `west build -b qemu_cortex_m0` (fixture wording). QEMU boot is the honesty path before iron. Claiming a board flash without EVT evidence fails.

Debugging here means reading QEMU console/log digests, not inventing JTAG sessions. Connectivity to host tooling is local Device Lab compose / QEMU — not a carrier OTA story.

## Worked example
board=qemu_cortex_m0, qemu_ok=true, physical_status=PHYSICAL_PENDING

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No board flash claim without EVT
- No OTA/carrier claims
- No unmerged device-os PR as accepted pin

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_zephyr_qemu` and `EP-4707`. Empty {} fails. A file whose body is only PASS raises.
