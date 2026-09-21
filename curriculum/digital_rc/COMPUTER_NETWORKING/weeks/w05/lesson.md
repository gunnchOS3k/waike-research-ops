# Week 5: Transport — TCP reliability & ports

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w05/lesson.md`

## Objectives
- Map https/dns/ssh
- ACK from seq+len
- Refuse telnet

## Body (track overlay)
Transport overlay pairs AIMD with lab_transport_ports.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w05/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
seq=1000 len=200 → ACK 1200 on full receipt. cwnd 10, loss → 5, then 6,7,8... on additive increase per RTT without further loss.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No copying CS144 TCP stacks
