# Week 4: Device OS compose health — migrate before healthy

**Ticket:** GPL-5404  
**Lab:** `lab_gpl_compose_health`

## Objectives
- Require migrate_ok before health=healthy
- Keep rollback_to ≠ current_digest
- NO_AI for digest/rollback fields

## Body
HW/SW interface at the compose layer: pin the image digest, run migrate, then allow health=healthy. rollback_to must point at the previous digest, never the current one. Skipping migrate is how Device Lab weekends strand volunteers on a half-applied schema.

NO_AI for digest and rollback fields. PHYSICAL_PENDING if anyone claims a physical flash for this digital compose target.
## Worked example
migrate_ok=true, health=healthy, rollback_to≠current_digest

## Assessment mode
NO_AI

## Claim refusals
- No physical flash claim for compose target
- No rollback_to == current

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_compose_health` and `GPL-5404`. Empty {} fails. A file whose body is only PASS raises.
