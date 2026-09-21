# Week 1: Packets are chopped on purpose

The WAIKE Packet Range is a table, a switch, and four Raspberry-class endpoints named Pier, Yard, Shed, and Roof. Nothing here is magic. A message that cannot fit in one frame is chopped. Ethernet carries 1500-ish bytes of payload because the local wire agreed to that, not because the Internet is polite.

Encapsulation is dressing: HTTP inside TCP inside IP inside Ethernet. Each header is a sticky note for a different worker. The sticky note you peel first on receive is the one you added last on send. Learners who skip that sentence try to debug TCP checksums when the Ethernet destination MAC is wrong.

Multiplexing is why port 443 and port 22 can share one IP. The 5-tuple (src IP, dst IP, protocol, src port, dst port) is the conversation ID. If you only look at IPs you will swear two students are 'the same traffic.'

CS144's public weekly shape (principles → transport → switching → congestion → routing) is a structure we acknowledge. We do not copy Stanford code. This week's lab starts an original Ethernet/IPv4 parse you will finish in the datapath lab.

## Worked example

A 2000-byte application buffer on a 1500 MTU path becomes at least two IP datagrams. Peel Ethernet first (ethertype 0x0800), then IP, then TCP.
