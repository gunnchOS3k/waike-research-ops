# Week 7: Names on the LAN — hosts, a tiny zone, and the printer that only exists locally

printer.gary.waike.local is not on the public Internet and should not be. The desk resolver checks a hosts file first, then a tiny zone. desk.gary.waike.local is 10.20.30.14. The library A records are 10.20.30.21 and .22; the lab returns the first. example.com must not resolve in this fixture — a classroom resolver that invents WAN answers is a liar.

DHCP is how kiosks get 10.20.30.0/24 addresses. When a kiosk shows 169.254.x.x, it did not 'go rogue'; it failed to hear a lease. Check the switch port, the DHCP pool, and whether someone enabled a second DHCP server on a home router under the table.

Ports you must be able to name at the desk: 53 (DNS), 67/68 (DHCP), 80/443 (web), 631 (IPP/cups). You do not need a CCNA to say 'the printer name does not resolve.' You do need to stop reinstalling drivers until ping of the IP works and the name matches.

Split horizon is why staff see an internal A record and patrons on guest Wi-Fi do not. If a volunteer tests from a phone on guest, they will swear DNS is down. They are on the wrong horizon.

## Learn the distinction

A hostname is a name. A resolver maps a requested name and record type to a response according to its configuration. A hosts file can provide local mappings. DNS responses can differ by network view, cache or policy. Successful name resolution does not prove that a remote service is reachable or that its certificate is valid.

## Guided practice: use a fictional resolver

Create a text table: `desk.test → 192.0.2.10`, `printer.test → 192.0.2.20`, and `library.test → 192.0.2.30`. These are documentation examples; do not configure a real network with them. Define the exercise resolver to return no record for all other names. Query the table by hand for the three names and `example.com`. Expected result: the three listed answers match the table; the last query has no record in this deliberately closed fixture. That is not a claim about public DNS.

Change only the printer entry to `192.0.2.21`. Predict which previous answer becomes stale. Record how a cached value could make two observations disagree. Do not edit your real hosts file or query private infrastructure for this exercise.

## Independent evidence

Write a troubleshooting decision tree that separates name lookup failure, connection failure after lookup and application failure after connection. For each branch, identify one observation needed before taking action. Submit the input table, query results and decision tree.

## Check your reasoning

A public resolver is not a universal fix for a private name. Sending private names to an unauthorized resolver may disclose information and may still produce no usable answer.

## Worked example

Query printer.gary.waike.local → 10.20.30.40 from hosts. Query example.com → none. Link-local 169.254.13.9 on a kiosk → DHCP failure, not a new addressing plan.
