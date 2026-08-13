# Week 7 presentation — Names on the LAN — hosts, a tiny zone, and the printer that only exists locally

## Slide 1 — Cold open
Query printer.gary.waike.local → 10.20.30.40 from hosts. Query example.com → none. Link-local 169.254.13.9 on a kiosk → DHCP failure, not a new addressing plan.

## Slide 2 — Teaching beat
printer.gary.waike.local is not on the public Internet and should not be. The desk resolver checks a hosts file first, then a tiny zone. desk.gary.waike.local is 10.20.30.14. The library A records are 10.20.30.21 and .22; the lab returns the first. example.com must not resolve in this fixture — a classroom resolver that invents WAN answers is a liar.

## Slide 3 — Live work
Put 1200 seconds, 15% free, and CHG window 18:00–21:00 on the board. Sit in silence until someone does the arithmetic.

## Speaker notes
If they ask for A+ dumps, close the slide and open the alignment JSON. Keys never leave the instructor packet.
