# Week 4 presentation — Forwarding plane — TTL, LPM, and a crafted IPv4 frame

## Slide 1 — Cold open
dst 10.20.40.9 matches /24 better than /16. nh 10.20.30.1 iface eth1. TTL 4→3. Host route /32 wins when present.

## Slide 2 — Teaching beat
This is the deep data-path week. You are handed a classroom-crafted Ethernet+IPv4+TCP frame. Destination MAC aa:aa:aa:aa:aa:01, ethertype 0x0800, IPv4 IHL 5, TTL 4, proto 6, src 10.20.30.14, dst 10.20.40.9. You parse bytes. You do not open Wireshark on a cafe network and call it a lab.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
