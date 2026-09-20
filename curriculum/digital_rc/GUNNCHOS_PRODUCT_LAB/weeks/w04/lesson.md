# Week 4: Device OS compose health — migrate before healthy

**Ticket:** GPL-5404  
**Lab:** `lab_gpl_compose_health`

## Objectives
- Require migrate_ok before health=healthy
- Keep rollback_to ≠ current_digest
- NO_AI for digest/rollback fields

## Body
HW/SW interface at the compose layer: image digest pins, migrate, health, rollback pointer. Skipping migrate fails. This is Device OS local honesty — not a physical flash claim.

## Worked example
migrate_ok=true, health=healthy, rollback_to≠current_digest

## Assessment mode
NO_AI

## Claim refusals
- No physical flash claim for compose target
- No rollback_to == current

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_compose_health` and `GPL-5404`. Empty {} fails. A file whose body is only PASS raises.
