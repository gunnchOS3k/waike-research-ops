# Week 8: DHCP, DNS, NAT — services that lie for us on purpose

DHCP hands out leases so Pier does not keep a paper IP ledger. DNS walks stub → TLD → authoritative, then caches. The lab's second lookup must hit cache. NAT maps 10.20.30.14 to 192.0.2.88 so the library cache on the far side can answer without knowing our inside lot.

Lying is the feature: NAT lies about addresses, DNS lies about 'this name is that number for now,' DHCP lies about 'you may use this for 3600 seconds.' Troubleshooting is asking which liar expired.

NTP, syslog, SNMP appear as a CCNA IP Services chorus. In WAIKE you will timestamp lab JSON and write one syslog line. You will not stand up a full NMS.

A cache that never expires is how a moved printer becomes a ghost. TTL 300 on an A record is a policy. Set it, write it, do not blame 'the Internet.' When Roof moves to a new address at 16:00 and Pier still prints to the old one at 16:10, the liar is the cache, not the cable.

## Worked example

First resolve desk.gary.waike.example → 203.0.113.14 via auth_walk. Second → cache. NAT inside 10.20.30.14 outside 192.0.2.88.
