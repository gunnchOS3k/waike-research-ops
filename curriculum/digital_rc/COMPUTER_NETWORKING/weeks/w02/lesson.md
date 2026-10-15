# Week 2: CIDR as a land survey, not a guessing game

10.20.30.40/26 is not 'a class C with a funny number.' /26 means 26 bits of network, 6 bits of host, 64 addresses, network 10.20.30.0, broadcast 10.20.30.63, 62 ordinary host addresses under the multi-access subnet convention; /31 point-to-point and /32 host-route cases need separate treatment. The host .40 lives in that block the way a house lives on a surveyed lot.

A second block 10.20.30.80/28 is 16 addresses, .80–.95, 14 usable. If you put a printer at .96 you are in the next lot and the ACL you wrote for /28 will not save you.

Longest prefix match is how a router chooses among overlapping lots. /32 beats /24 beats /16 beats /0. This is the same idea you will wire into the datapath lab, and it is why 'add a more specific' is a real change, not a superstition.

IPv6 appears as a parallel survey (128 bits, no broadcast). We do not pretend a 10-week course makes you an IPv6 designer. You will be able to say why fe80:: is link-local and why it is not a public plan.

## Concept and scope

An IPv4 prefix identifies a block by its leading bits. A /26 contains 64 addresses; under the ordinary multi-access subnet convention, the first identifies the network and the last is broadcast. /31 point-to-point links and /32 host routes need separate interpretation.

## Guided practice

Predict the block containing 192.0.2.70/26. Its network is 192.0.2.64 and broadcast is 192.0.2.127, with 62 ordinary host addresses. Run the model test to compare. Expected result: all three values match. If one differs, check whether you rounded to a 64-address boundary before subtracting reserved addresses.

## Independent evidence

Solve a different /28 using a documentation address. Show the block size, boundary, broadcast and convention for usable addresses. Add /31 and /32 tests to the worked example; document where the canonical lab's contract differs.

## IPv6 addressing activity

The extended packet resource provides ipv6_prefix. Run its service_trace example for 2001:db8:20::7/64. Expected result: network 2001:db8:20::/64 with 2^64 addresses and no broadcast. This is a block size, not an assignable-device count. Compare /128 and explain why IPv4’s network/broadcast subtraction does not apply. Use documentation addresses only; no real adapter configuration is required.

## Worked example

10.20.30.40/26 → net 10.20.30.0 bcast 10.20.30.63 usable 62. 10.20.30.80/28 → net 10.20.30.80 bcast 10.20.30.95 usable 14.
