# Week 7 presentation — Names on the LAN — hosts, a tiny zone, and the printer that only exists locally

## Slide 1 — Cold open
Query printer.gary.waike.local → 10.20.30.40 from hosts. Query example.com → none. Link-local 169.254.13.9 on a kiosk → DHCP failure, not a new addressing plan.

## Slide 2 — Teaching beat
printer.gary.waike.local is not on the public Internet and should not be. The desk resolver checks a hosts file first, then a tiny zone. desk.gary.waike.local is 10.20.30.14. The library A records are 10.20.30.21 and .22; the lab returns the first. example.com must not resolve in this fixture — a classroom resolver that invents WAN answers is a liar.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
