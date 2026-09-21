# Week 2: CIDR as a land survey, not a guessing game

10.20.30.40/26 is not 'a class C with a funny number.' /26 means 26 bits of network, 6 bits of host, 64 addresses, network 10.20.30.0, broadcast 10.20.30.63, 62 usable if you still believe in network and broadcast addresses. The host .40 lives in that block the way a house lives on a surveyed lot.

A second block 10.20.30.80/28 is 16 addresses, .80–.95, 14 usable. If you put a printer at .96 you are in the next lot and the ACL you wrote for /28 will not save you.

Longest prefix match is how a router chooses among overlapping lots. /32 beats /24 beats /16 beats /0. This is the same idea you will wire into the datapath lab, and it is why 'add a more specific' is a real change, not a superstition.

IPv6 appears as a parallel survey (128 bits, no broadcast). We do not pretend a 10-week course makes you an IPv6 designer. You will be able to say why fe80:: is link-local and why it is not a public plan.

## Worked example

10.20.30.40/26 → net 10.20.30.0 bcast 10.20.30.63 usable 62. 10.20.30.80/28 → net 10.20.30.80 bcast 10.20.30.95 usable 14.
