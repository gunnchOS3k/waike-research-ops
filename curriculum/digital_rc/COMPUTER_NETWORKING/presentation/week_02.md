# Week 2 presentation — CIDR as a land survey, not a guessing game

## Slide 1 — Cold open
10.20.30.40/26 → net 10.20.30.0 bcast 10.20.30.63 usable 62. 10.20.30.80/28 → net 10.20.30.80 bcast 10.20.30.95 usable 14.

## Slide 2 — Teaching beat
10.20.30.40/26 is not 'a class C with a funny number.' /26 means 26 bits of network, 6 bits of host, 64 addresses, network 10.20.30.0, broadcast 10.20.30.63, 62 usable if you still believe in network and broadcast addresses. The host .40 lives in that block the way a house lives on a surveyed lot.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
