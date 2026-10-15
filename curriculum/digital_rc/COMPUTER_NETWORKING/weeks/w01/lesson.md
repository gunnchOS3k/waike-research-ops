# Week 1: Packets are chopped on purpose

The WAIKE Packet Range is a synthetic teaching fixture with four endpoints named Pier, Yard, Shed, and Roof, not evidence of a deployed campus. In this fixture, the path MTU is 1500 bytes: one IP packet can occupy at most 1500 bytes, including its IP header. The Ethernet header is outside that limit. Other links can have different MTUs. TCP divides its byte stream into segments; that is different from IP fragmentation.

For an HTTPS example using TCP, the nesting is HTTP data inside TLS records inside TCP segments inside IP packets inside Ethernet frames. HTTP/3 uses QUIC over UDP, so this example is not the only web stack. Each header is a sticky note for a different worker. The sticky note you peel first on receive is the one you added last on send. Learners who skip that sentence try to debug TCP checksums when the Ethernet destination MAC is wrong.

Multiplexing is why port 443 and port 22 can share one IP. The 5-tuple (src IP, dst IP, protocol, src port, dst port) distinguishes transport flows at a given observation point. NAT can rewrite the tuple. If you only look at IPs you will swear two students are 'the same traffic.'

CS144's public weekly shape (principles → transport → switching → congestion → routing) is a structure we acknowledge. We do not copy Stanford code. This week's lab starts an original Ethernet/IPv4 parse you will finish in the datapath lab.

Technical source: RFC 9293 sections 3.7 and 3.7.1, https://www.rfc-editor.org/rfc/rfc9293.html#section-3.7. Before running code, predict the payload capacity, calculate it, then explain the assumptions. A large application write alone does not tell you an exact packet count.

## Concept and scope

A path MTU limits IP packet size on the path being modeled. TCP segmentation and IP fragmentation are different mechanisms. Header options, encapsulation and retransmission affect actual traffic; an application write does not specify an exact packet count.

## Guided practice

Run the downloadable packet model. Calculate 2000 stream bytes with MTU 1500, IPv4 header 20 and TCP header 20: 1460 bytes remain per data segment, so the minimum is two. Expected result: the arithmetic test passes. Repeat with MTU 1280, IPv6 header 40 and TCP header 20, and explain which assumptions changed. This function performs arithmetic; it does not send or capture packets.

## Independent evidence

Write an encapsulation diagram including TLS for a TCP-based HTTPS example. Label byte counts separately from protocol names. Explain why HTTP/3 would need a different transport diagram.

## Worked example

Assume IPv4 without options (20-byte header), TCP without options (20-byte header), a 1500-byte path MTU, and no IP fragmentation. TCP payload capacity is 1500 - 20 - 20 = 1460 bytes. Sending 2000 TCP stream bytes requires at least ceil(2000/1460) = 2 data segments, for example 1460 + 540. Actual segment count can be higher. TLS adds its own bytes before TCP. On receive, peel Ethernet (ethertype 0x0800), then IPv4, then TCP. Independent practice: repeat for MTU 1280 with a 40-byte IPv6 header and 20-byte TCP header; state why your result does not count acknowledgments or retransmissions.
