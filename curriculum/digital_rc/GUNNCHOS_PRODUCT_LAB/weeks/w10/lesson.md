# Week 10: Product validation capstone — charter + compat + CI

**Ticket:** GPL-5A10  
**Lab:** `lab_gpl_product_capstone`

## Objectives
- Assemble ≥6 lab digests
- compat_ok, no_device_os_pr, no_key_leak
- Docs packet for the next operator

## Body
Capstone is product validation: charter, compat matrix, checkout FSM, compose health, privacy BOM, guest protocol, release notes, CI tokens, dep pin. Tie to real gunnchOS concepts (Device Lab compose, guest protocol, accepted-main pins) without fabricating physical EVT evidence.

Mark PHYSICAL_PENDING where iron/OTA/carrier would otherwise be implied.

## Worked example
labs_passed≥6, compat_ok=true, no_device_os_pr=true, no_key_leak=true

## Assessment mode
AI_DISCLOSED

## Claim refusals
- Do not merge device-os #103 as course evidence
- No fabricated EVT
- No key leak in portfolio

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_product_capstone` and `GPL-5A10`. Empty {} fails. A file whose body is only PASS raises.
