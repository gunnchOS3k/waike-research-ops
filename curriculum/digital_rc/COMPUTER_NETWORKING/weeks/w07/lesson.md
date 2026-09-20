# Week 7: Routing — SPF on the four-router town

**Track:** NETWORKING_INFRA
**content_ref:** `../COMPUTER_NETWORKING/weeks/w07/lesson.md`

## Objectives
- Dijkstra on fixture costs
- Install prefix via correct nh
- Contrast scenic vs SPF

## Body (track overlay)
SPF beats scenic route. OSPFv2 cited as context only.

Shared lesson body is maintained under the legacy package at `../COMPUTER_NETWORKING/weeks/w07/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
dijkstra(A)['D']=4 via B. Scenic A-C-D=10 loses. Install 10.20.40.0/24 nh=Yard.

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No production IGP redesign claim
