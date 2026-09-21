# Week 6: Guest protocol — Device OS ping/boot_status

**Ticket:** GPL-5606  
**Lab:** `lab_gpl_guest_protocol`

## Objectives
- Require ping_ok and boot_status=ready
- Name protocol_version
- Reject obsolete click-collector protocols

## Body
Guest agent protocol is the Device OS boundary learners can actually test: ping_ok, boot_status=ready, protocol_version pinned. Obsolete click-collector protocols are rejected — telemetry must ride on honest fields.

This week ties product architecture to the guest contract without opening unmerged device-os PRs as Product-Use evidence.
## Worked example
ping_ok=true, boot_status=ready, protocol_version=wp011r

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No obsolete click-collector
- No claiming unmerged guest features

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_guest_protocol` and `GPL-5606`. Empty {} fails. A file whose body is only PASS raises.
