# Week 3: Ethernet / L2 switching & VLANs

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w03/lesson.md`

## Objectives
- Key MAC tables as (MAC, VLAN)
- Explain flood scope
- Name trunk vs access

## Body (track overlay)
L2 isolation separates campus from party line. VLAN 20/30 map to Pier/Yard.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w03/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
mac_table[(aa:aa:aa:aa:aa:10, 20)] = Gi1/0/8. Lookup with VLAN 30 misses. Isolation holds.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No vendor config paste as original work
