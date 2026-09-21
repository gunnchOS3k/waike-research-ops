# Week 3: Threat models for Harbor zones

**Track:** CYBER_SOC
**content_ref:** `../CYBERSECURITY/weeks/w03/lesson.md`

## Objectives
- Asset + ≥3 threats + ≥2 controls
- offensive_scope=none
- kiosk→SOC deny

## Body (track overlay)
Defensive threat modeling only. No exploit steps.

Shared lesson body is maintained under the legacy package at `../CYBERSECURITY/weeks/w03/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
matrix[(kiosk,soc)]=deny; [(soc,kiosk)]=allow_syslog_only; [(guest,staff)]=deny.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- offensive_scope=none
- No unauthorized scanning
