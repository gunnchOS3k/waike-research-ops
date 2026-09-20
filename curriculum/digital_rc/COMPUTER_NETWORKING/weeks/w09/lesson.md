# Week 9: Security basics & authorized fixture capture

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w09/lesson.md`

## Objectives
- Order ACLs
- Parse authorized fixtures only
- Deny telnet

## Body (track overlay)
Operator security basics. Cafe Wireshark is not a lab.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w09/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
decide(23)=deny, decide(443)=permit, decide(9)=deny. NAT still maps the inside host.

## Assessment mode
NO_AI

## Claim refusals
- No unauthorized interception
