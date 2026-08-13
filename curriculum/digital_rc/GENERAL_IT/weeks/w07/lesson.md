# Week 7: Names on the LAN — hosts, a tiny zone, and the printer that only exists locally

printer.gary.waike.local is not on the public Internet and should not be. The desk resolver checks a hosts file first, then a tiny zone. desk.gary.waike.local is 10.20.30.14. The library A records are 10.20.30.21 and .22; the lab returns the first. example.com must not resolve in this fixture — a classroom resolver that invents WAN answers is a liar.

DHCP is how kiosks get 10.20.30.0/24 addresses. When a kiosk shows 169.254.x.x, it did not 'go rogue'; it failed to hear a lease. Check the switch port, the DHCP pool, and whether someone enabled a second DHCP server on a home router under the table.

Ports you must be able to name at the desk: 53 (DNS), 67/68 (DHCP), 80/443 (web), 631 (IPP/cups). You do not need a CCNA to say 'the printer name does not resolve.' You do need to stop reinstalling drivers until ping of the IP works and the name matches.

Split horizon is why staff see an internal A record and patrons on guest Wi-Fi do not. If a volunteer tests from a phone on guest, they will swear DNS is down. They are on the wrong horizon.

## Worked example

Query printer.gary.waike.local → 10.20.30.40 from hosts. Query example.com → none. Link-local 169.254.13.9 on a kiosk → DHCP failure, not a new addressing plan.
