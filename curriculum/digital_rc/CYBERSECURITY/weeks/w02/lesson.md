# Week 2: IAM lifecycle — humans and bots

**Track:** CYBER_SOC
**content_ref:** `../CYBERSECURITY/weeks/w02/lesson.md`

## Objectives
- Bind Naiya/Omar/harbor-bot
- Non-human identities first-class
- Deprovision tickets

## Body (track overlay)
Bots read; humans close.

Shared lesson body is maintained under the legacy package at `../CYBERSECURITY/weeks/w02/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
allow(naiya, case.close)=false; allow(omar, case.close)=true; allow(harbor-bot, case.close)=false.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No production IAM without ticket
