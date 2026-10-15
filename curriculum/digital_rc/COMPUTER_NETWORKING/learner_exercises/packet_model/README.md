# Packet model: calculate, predict, compare

Requirements: Python 3.11+, including the standard `ipaddress` library. Save both `.py` files in the same empty practice folder. Run `python3 -m unittest -v test_network_model.py` there (or `py -3 -m unittest -v test_network_model.py` with the Windows Python launcher). Expected result: seven tests pass. An import error means you should check the filenames and starting directory before changing code.

This model sends no packets, opens no sockets and changes no network settings. It models data-segment arithmetic without options/retransmissions, IPv4 prefix arithmetic, longest-prefix selection and TTL decrement. It does not parse bytes, implement TCP, exchange routing protocols, transmit ICMP or validate a physical network.

Predict the output before running. Add a more-specific /32 route and a test showing that it takes priority over /26. Change TTL to 1 and explain why a matching route does not permit forwarding. Add your own /31 and /32 arithmetic tests and state their point-to-point/host-route conventions. The existing canonical CIDR lab has its own acceptance contract; do not assume this example's /32 convention automatically satisfies it.

Independent work: add a test for equal-length duplicate route entries and document the model's tie behavior. Does that establish a real router's policy? Explain why not. Deliberately replace longest-prefix selection with shortest-prefix selection, observe the failed test, then restore and rerun. Preserve the failing output as evidence of a test that detects a defect.

No real learner or network measurements are present. AI assistance contributed to code, tests and instruction. Human technical and educational acceptance remains pending.


## Parse actual crafted bytes, then make a forwarding decision

The original seven tests above cover arithmetic only. Download `packet_fixture.py` and `test_packet_fixture.py` into the same folder to add byte-parsing and bounded service-state exercises. Run all the public example tests:

```
python3 -m unittest -v test_network_model.py test_packet_fixture.py
python3 packet_fixture.py
python3 packet_fixture.py --ttl 1
python3 packet_fixture.py --destination 203.0.113.4
```

Expected result: 19 tests pass. The default JSON includes 54 crafted bytes as `frame_hex`, a SHA-256 hash, parsed Ethernet/IPv4 fields, TCP port fields and a modeled forwarding decision. Its destination is 198.51.100.9, so /24 beats /0 and the output is eth1 with TTL 3. The TTL=1 invocation parses a genuinely different header and drops for expiry. The changed destination uses the default uplink route. No packet is transmitted.

Offsets are relative to a layer. Ethernet's destination occupies bytes 0–5, source 6–11, and ethertype 12–13. IPv4 starts at frame offset 14; its TTL is IP offset 8, so frame offset 22. The IHL nibble gives IP header length in four-byte units, not individual bytes. The parser validates declared total length and IPv4 header checksum before extracting the modeled fields. It rejects unsupported fragmentation and invalid/truncated TCP headers. It accepts untagged Ethernet IPv4 only; it is not a general capture analyzer.

This is a header fixture. The 54-byte representation omits Ethernet minimum-frame padding, preamble and FCS. TCP is a stub whose transport checksum is not computed or validated. The forwarding decision does not emit a rewritten frame, recompute a forwarded checksum, apply an ACL, send ICMP, resolve a next-hop MAC or prove physical connectivity. A valid IPv4 header checksum detects some header corruption; it is not an authenticity or security check.

Predict the byte indices and output before running. In a copy, change the parser to read TTL from IP offset 9. Expected result: the field test fails because that byte is the protocol field (6), not TTL (4). Preserve the failed output, restore offset 8 and rerun. Corrupt a header byte without updating its checksum and observe rejection. A checksum mismatch is a meaningful failure, not a reason to disable validation.

## DNS cache and DHCP lease timing without touching your network

Create a new local `service_trace.py` containing:

```
from packet_fixture import PositiveDnsCache, lease_status, ipv6_prefix

cache = PositiveDnsCache()
authority = {'desk.example': ('203.0.113.14', 300)}
print(cache.lookup('desk.example', 0, authority))
authority['desk.example'] = ('203.0.113.15', 300)
print(cache.lookup('desk.example', 299, authority))
print(cache.lookup('desk.example', 300, authority))
print(lease_status(100, 3600, 3699))
print(lease_status(100, 3600, 3700))
print(ipv6_prefix('2001:db8:20::7/64'))
```

Run `python3 service_trace.py`. Expected results: first lookup uses the local fixture authority at .14; the cached value remains .14 at second 299 with one second left; at second 300 the new .15 value is retrieved. The model uses nondecreasing integer seconds, positive A-record caching and a local dictionary. It implements no resolver, DNS packet exchange, negative caching, DNSSEC, aliases or multiple-record behavior. A name absent from the fixture returns `not_in_fixture`; that is not a measured NXDOMAIN response.

The lease is active with one second left at 3699 and expired at 3700. These are different clocks and state variables from DNS TTL. This lease function implements expiry arithmetic only; no DISCOVER/OFFER/REQUEST/ACK traffic, renewal timers, address conflict detection or device configuration is performed. A still-active lease does not prove DNS or the application works. Do not change a real adapter to try this exercise.

The IPv6 output identifies `2001:db8:20::/64`, containing 2^64 addresses, and explicitly has no broadcast. This is the size of an address block, not a statement that every address is assignable or that 2^64 devices exist. Do not subtract IPv4's network/broadcast pair from IPv6. The documentation prefix is for examples; link-local addressing and real allocation policy need separate treatment.

## Independent packet and services evidence

A reviewer issues a different destination, TTL, pair of overlapping prefixes, DNS expiry time and lease start/duration. Before running, submit your predicted byte offsets, parsed fields, selected prefix and expiry boundaries. Build a distinct local script that computes the trace, then compare. Include TTL=1, no route, a /32 route winning over /24, an exact cache-expiry boundary, zero DNS TTL and an expired lease. Show a defect your tests catch and keep the repair output. Record assistance and distinguish copied reference behavior from your own reasoning.

Use the existing WAIKE assignment for the corresponding week to submit original bytes/hex, byte hash, route table, predictions, actual outputs, test history and a limitation statement when authorized. Review criteria: correct byte-to-field mapping; explicit prefix and TTL rules; correct independent DNS/lease state; meaningful boundary tests; and accurate claim limits. A reviewer may request changed inputs or a live explanation. Every criterion remains pending until genuinely reviewed. These programs create no grades or records and cannot independently prove mastery.

Return to Networking Week 4 for datapath, Week 8 for services and Week 10 for the integrated evidence portfolio. Reference field definitions: [RFC 791](https://www.rfc-editor.org/rfc/rfc791.html); DNS TTL behavior [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html); DHCP [RFC 2131](https://www.rfc-editor.org/rfc/rfc2131.html); IPv6 addressing [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291.html). Models intentionally cover only the behavior described here. No standards conformance, physical measurements or real learner acceptance is asserted.
