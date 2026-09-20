# Week 5: Security, privacy & Privacy BOM

**Ticket:** GPL-5505  
**Lab:** `lab_gpl_privacy_bom`

## Objectives
- Inventory fields without PII in BOM
- Set retention_days
- Refuse biometric claims without evidence

## Body
Privacy BOM lists camera/mic/location-class fields with pii_in_bom=false and retention_days. Security/privacy is a product requirement, not a slide. Accessibility note: disclose what is recorded in text, not color alone.

## Worked example
fields=[camera,mic,location], pii_in_bom=false, retention_days=30

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No biometric product claim without evidence
- No PII in BOM

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_privacy_bom` and `GPL-5505`. Empty {} fails. A file whose body is only PASS raises.
