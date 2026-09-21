# Week 2: GPIO contract — direction, pull, and safe defaults

**Ticket:** EP-4202  
**Lab:** `lab_ep_gpio_contract`

## Objectives
- Author pin direction/pull/default before pinmux calls
- Default outputs to a safe inactive level
- Separate digital I/O contract from SPICE weeks in HARDWARE_ENGINEERING

## Body
Before any Zephyr pinmux call, write a GPIO contract JSON: pin name, direction, default_level, pull. LED0 as output with default_level 0 (inactive) and pull none is the ForgeSense safe start.

Floating inputs without pulls are noise generators. Driving a pin as output while another driver contends is how boards brown out. The contract is the conversation with hardware — the code must match it.

No-hardware fallback: validate the contract JSON against the lab keys. Do not claim an LED blinked on iron unless OPTIONAL_PHYSICAL evidence exists.

## Worked example
pin=LED0, direction=out, default_level=0, pull=none

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming physical LED blink without evidence
- No deleting safety defaults 'temporarily'

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_gpio_contract` and `EP-4202`. Empty {} fails. A file whose body is only PASS raises.
