# Week 8 presentation — DHCP, DNS, NAT — services that lie for us on purpose

## Slide 1 — Cold open
First resolve desk.gary.waike.example → 203.0.113.14 via auth_walk. Second → cache. NAT inside 10.20.30.14 outside 192.0.2.88.

## Slide 2 — Teaching beat
DHCP hands out leases so Pier does not keep a paper IP ledger. DNS walks stub → TLD → authoritative, then caches. The lab's second lookup must hit cache. NAT maps 10.20.30.14 to 192.0.2.88 so the library cache on the far side can answer without knowing our inside lot.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
