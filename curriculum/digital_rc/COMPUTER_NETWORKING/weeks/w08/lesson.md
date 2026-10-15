# Week 8: DHCP, DNS, NAT — configured services and explicit state

DHCP provides network configuration through a lease process. DNS associates names with resource records. NAT translates selected network address or port information. These are defined mechanisms with lifetimes and policies, not evidence that protocols are deceptive. An address configuration, name answer, successful connection and correct application response support different claims.

A typical stub resolver asks a recursive resolver. If it has no usable cached answer, that resolver can follow referrals from root to top-level and authoritative servers. This course’s local dictionary model does not implement that exchange. DNS answers are not always one name mapped to one address: record types, aliases, multiple records and policy matter. A TTL limits how long a particular cached positive result can be reused; it does not certify the result or guarantee availability.

DHCP lease expiry and DNS cache expiry are independent state. DHCP renewal occurs before normal lease expiry in a complete client; our arithmetic function omits renewal and network messages. NAT is not a firewall permission grant. A working address translation alone establishes neither authorization nor application health.

## Guided practice

Use service_trace.py from the extended packet resource README. The first fictional lookup at model second 0 gets 203.0.113.14 with TTL 300. Change the local authoritative fixture to .15. Expected result: a second lookup at 299 uses cached .14; at 300 the entry expires and the new .15 is retrieved. A zero-TTL answer is not reused. No real DNS queries or private hostnames leave your device.

A separate fictional lease begins at second 100 with duration 3600. At 3699 it is active with one second remaining; at 3700 it is expired. Compare this with the cache timeline rather than assuming both clocks expire together. Run the 19 public packet/model tests and inspect the exact-boundary cases.

## Independent evidence

Choose or receive changed cache and lease parameters. Predict a hit, exact expiry, zero TTL and lease expiry before running. Create a diagnosis table with address configuration, name result, connection result and application response; include a case where DNS succeeds but the connection fails. Identify the next safe observation without changing a real network. Preserve modeled versus observed outcomes and explain why the local dictionary’s not_in_fixture result is not a measured NXDOMAIN reply. Submit predictions, source/code version, outputs and limitations through the existing authorized assignment; instructor review remains pending.

## Worked example

At second 0, cache desk.example=.14 for 300 seconds. A changed fixture authority at .15 does not alter the cached .14 at second299; expiry at300 fetches .15. A lease starting100 with duration3600 expires at3700. These separate local models send no messages.
