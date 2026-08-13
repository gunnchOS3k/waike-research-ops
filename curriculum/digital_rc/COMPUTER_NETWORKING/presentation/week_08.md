# Week 8 presentation — DHCP, DNS, NAT — services that lie for us on purpose

## Slide 1 — Cold open
First resolve desk.gary.waike.example → 203.0.113.14 via auth_walk. Second → cache. NAT inside 10.20.30.14 outside 192.0.2.88.

## Slide 2 — Teaching beat
DHCP hands out leases so Pier does not keep a paper IP ledger. DNS walks stub → TLD → authoritative, then caches. The lab's second lookup must hit cache. NAT maps 10.20.30.14 to 192.0.2.88 so the library cache on the far side can answer without knowing our inside lot.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
