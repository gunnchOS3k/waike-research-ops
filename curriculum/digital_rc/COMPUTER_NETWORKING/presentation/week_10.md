# Week 10 presentation — Campus edge capstone — intent files and a datapath proof

## Slide 1 — Cold open
Intent JSON must include prefix 10.20.40.0/24 nh via Yard, ACL deny 23, datapath ok=true.

## Slide 2 — Teaching beat
You will ship a JSON intent file: VLANs, prefixes, ACL order, NAT, and the four-router costs. A tiny validator will reject missing next-hops. That is the automation domain without pretending we built a controller fabric.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
