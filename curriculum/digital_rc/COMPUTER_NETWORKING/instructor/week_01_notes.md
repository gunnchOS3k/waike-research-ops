# Packet Range — instructor week 1

**Hex/graph on the board:** Assume IPv4 without options (20-byte header), TCP without options (20-byte header), a 1500-byte path MTU, and no IP fragmentation. TCP payload capacity is 1500 - 20 - 20 = 1460 bytes. Sending 2000 TCP stream bytes requires at least ceil(2000/1460) = 2 data segments, for example 1460 + 540. Actual segment count can be higher. TLS adds its own bytes before TCP. On receive, peel Ethernet (ethertype 0x0800), then IPv4, then TCP. Independent practice: repeat for MTU 1280 with a 40-byte IPv6 header and 20-byte TCP header; state why your result does not count acknowledgments or retransmissions.

**Lab `lab_cidr_math`:** student must submit parse/table JSON. Empty fails.

**Pitfall:** If they debug TCP checksums with a wrong dest MAC, rewind to sticky notes.

No CS144 code, no CCNA dumps. Alignment JSON only.
