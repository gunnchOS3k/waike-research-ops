# Week 4: Forwarding plane — TTL, LPM, and a crafted IPv4 frame

This is the deep data-path week. You are handed a classroom-crafted Ethernet+IPv4+TCP frame. Destination MAC aa:aa:aa:aa:aa:01, ethertype 0x0800, IPv4 IHL 5, TTL 4, proto 6, src 10.20.30.14, dst 10.20.40.9. You parse bytes. You do not open Wireshark on a cafe network and call it a lab.

The forwarding table has 10.20.40.0/24 via 10.20.30.1 on eth1, a /16 on eth0, and a default out wan0. LPM must choose eth1. Adding 10.20.40.9/32 must steal the route to host9. TTL decrements; TTL 1 would drop instead of forward. That drop is a feature: loops die.

RFC 791 is the field dictionary (version, IHL, TTL, protocol, addresses). We cite it; we do not paste pages of it. Checksums are mentioned; this lab does not require you to recompute the IP checksum unless you take the stretch goal.

If you treat the frame as a string of hex without slicing 0:6, 6:12, 12:14, you will invent an ethertype from the IP version nibble and then write a sad forum post.

## Concept and scope

Forwarding selects a next hop or output using the destination and forwarding table. Longest-prefix match chooses the most specific matching prefix. An IPv4 router also decrements TTL; expiry is a separate condition from finding a route.

## Guided practice

Run the model with a default route to uplink and 192.0.2.64/26 to desk. For destination 192.0.2.70 and TTL 8, predict desk and TTL 7. Expected result: the longest-prefix test passes. Repeat with TTL 1: the model drops instead. It reports a reason but does not construct an ICMP packet or update an IP checksum.

## Independent evidence

Add a /32 route for the destination and verify precedence. Then remove all matching routes and verify the no-route result. Explain why these calculations alone do not validate the canonical byte-parsing datapath lab.

## Worked example

dst 10.20.40.9 matches /24 better than /16. nh 10.20.30.1 iface eth1. TTL 4→3. Host route /32 wins when present.
