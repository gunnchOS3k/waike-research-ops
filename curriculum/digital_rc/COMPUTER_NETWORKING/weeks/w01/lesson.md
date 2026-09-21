# Week 1: Network models & encapsulation on the Packet Range

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w01/lesson.md`

## Objectives
- Name OSI/TCP-IP layers on Pier→Roof path
- Peel Ethernet→IP→TCP in order
- Refuse GUI screenshot as proof

## Body (track overlay)
NETWORKING_INFRA reframes Packet Range week 1 for campus edge ops. Encapsulation and MTU chopping remain core. Fixtures only — no cafe capture.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w01/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
A 2000-byte application buffer on a 1500 MTU path becomes at least two IP datagrams. Peel Ethernet first (ethertype 0x0800), then IP, then TCP.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No CCNA grant
- No unauthorized packet capture
