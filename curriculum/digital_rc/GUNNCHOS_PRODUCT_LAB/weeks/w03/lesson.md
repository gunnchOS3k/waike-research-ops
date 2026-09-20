# Week 3: User stories & checkout FSM handoff

**Ticket:** GPL-5303  
**Lab:** `lab_gpl_checkout_flow`

## Objectives
- Model states requested→approved→checked_out→returned
- Forbid orphan_state
- Keep handoff explicit between desk and volunteer

## Body
Checkout flow is the product spine for Device Lab. States must be complete; orphan states fail. This is requirements-to-FSM translation, not opening unmerged device-os PRs.

## Worked example
states=[requested,approved,checked_out,returned], orphan_state=false

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming production Device Lab metrics without fixture

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_checkout_flow` and `GPL-5303`. Empty {} fails. A file whose body is only PASS raises.
