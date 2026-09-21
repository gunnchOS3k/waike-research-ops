# Week 4: Forwarding plane — TTL, LPM, crafted frames

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w04/lesson.md`

## Objectives
- Parse authorized frame
- Choose LPM next hop
- Decrement TTL

## Body (track overlay)
Deep datapath. Classroom-crafted frames only.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w04/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
dst 10.20.40.9 matches /24 better than /16. nh 10.20.30.1 iface eth1. TTL 4→3. Host route /32 wins when present.

## Assessment mode
AI_RESTRICTED

## Claim refusals
- No live capture on networks you do not own
