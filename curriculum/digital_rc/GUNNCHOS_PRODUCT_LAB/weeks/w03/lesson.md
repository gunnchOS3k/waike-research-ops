# Week 3: User stories & checkout FSM handoff

**Ticket:** GPL-5303  
**Lab:** `lab_gpl_checkout_flow`

## Objectives
- Model states requested→approved→checked_out→returned
- Forbid orphan_state
- Keep handoff explicit between desk and volunteer

## Body
Checkout flow is the product spine for Device Lab. Map user stories to FSM states: a volunteer requests a device, desk lead approves, checkout happens, return closes the loop. orphan_state=true fails because the next shift cannot tell who holds the unit.

Industrial design interaction this week is a constraint note only (weight, port reach, label readability) — not a fabricated EVT photo. Keep states explicit so SOFTWARE_BUILDER ForgeDesk tickets and Product Lab charters do not silently diverge.
## Worked example
states=[requested,approved,checked_out,returned], orphan_state=false

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming production Device Lab metrics without fixture

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_checkout_flow` and `GPL-5303`. Empty {} fails. A file whose body is only PASS raises.
