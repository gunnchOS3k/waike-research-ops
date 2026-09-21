# Week 9: Power & sleep — wake source honesty

**Ticket:** EP-4909  
**Lab:** `lab_ep_sleep_mode`

## Objectives
- Name sleep_mode and wake_gpio
- Bound wake_latency_ms without inventing µA
- NO_AI for wake documentation fields

## Body
Power is a first-class embedded topic. SYSTEM_OFF with wake on BTN0 and wake_latency_ms=5 is the fixture story. Do not invent microamp draw numbers without a meter log — mark PHYSICAL_PENDING for measured current.

Device security angle: wake sources are attack surface. Document them; do not leave undocumented debug wakes in 'temporary' overlays.

## Worked example
sleep_mode=SYSTEM_OFF, wake_gpio=BTN0, wake_latency_ms=5

## Assessment mode
NO_AI

## Claim refusals
- No invented µA figures
- No undocumented debug wake in submitted overlay

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_sleep_mode` and `EP-4909`. Empty {} fails. A file whose body is only PASS raises.
