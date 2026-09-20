# Week 8: DNS / DHCP / NAT service honesty

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w08/lesson.md`

## Objectives
- Walk stub→TLD→auth then cache
- Map NAT inside/outside
- One syslog line

## Body (track overlay)
Services that lie on purpose: leases, names, addresses.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w08/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
First resolve desk.gary.waike.example → 203.0.113.14 via auth_walk. Second → cache. NAT inside 10.20.30.14 outside 192.0.2.88.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No full NMS standup required
