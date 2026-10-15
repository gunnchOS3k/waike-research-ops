# Week 1 presentation — Packets are chopped on purpose

## Slide 1 — Cold open
Assume IPv4 without options (20-byte header), TCP without options (20-byte header), a 1500-byte path MTU, and no IP fragmentation. TCP payload capacity is 1500 - 20 - 20 = 1460 bytes. Sending 2000 TCP stream bytes requires at least ceil(2000/1460) = 2 data segments, for example 1460 + 540. Actual segment count can be higher. TLS adds its own bytes before TCP. On receive, peel Ethernet (ethertype 0x0800), then IPv4, then TCP. Independent practice: repeat for MTU 1280 with a 40-byte IPv6 header and 20-byte TCP header; state why your result does not count acknowledgments or retransmissions.

## Slide 2 — Teaching beat
The WAIKE Packet Range is a synthetic teaching fixture with four endpoints named Pier, Yard, Shed, and Roof, not evidence of a deployed campus. In this fixture, the path MTU is 1500 bytes: one IP packet can occupy at most 1500 bytes, including its IP header. The Ethernet header is outside that limit. Other links can have different MTUs. TCP divides its byte stream into segments; that is different from IP fragmentation.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
