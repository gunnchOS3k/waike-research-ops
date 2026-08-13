# Week 1 presentation — Packets are chopped on purpose

## Slide 1 — Cold open
A 2000-byte application buffer on a 1500 MTU path becomes at least two IP datagrams. Peel Ethernet first (ethertype 0x0800), then IP, then TCP.

## Slide 2 — Teaching beat
The WAIKE Packet Range is a table, a switch, and four Raspberry-class endpoints named Pier, Yard, Shed, and Roof. Nothing here is magic. A message that cannot fit in one frame is chopped. Ethernet carries 1500-ish bytes of payload because the local wire agreed to that, not because the Internet is polite.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
