# Week 10: Modern ops runbook & campus edge capstone

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w10/lesson.md`

## Objectives
- Intent JSON with prefixes/ACL/NAT
- Three-check ops runbook
- Pier→Roof trace with VLAN/LPM/TTL/ACL

## Body (track overlay)
Capstone: intent + datapath proof + ops runbook. No fabricated outages.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w10/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
Intent JSON must include prefix 10.20.40.0/24 nh via Yard, ACL deny 23, datapath ok=true.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No CCNA grant
- No fabricated impact
