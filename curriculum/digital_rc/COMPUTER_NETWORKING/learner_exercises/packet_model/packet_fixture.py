"""Original local Ethernet/IPv4 fixture and bounded services models. No sockets.

The TCP bytes are a teaching stub, not a validated transport implementation.
No Ethernet FCS, preamble, physical link or real DNS/DHCP exchange is present.
"""
import argparse
import hashlib
import ipaddress
import json
import struct

from network_model import forward


def checksum(data):
    if len(data) % 2:
        data += b'\0'
    total = sum(struct.unpack('!' + 'H' * (len(data) // 2), data))
    while total >> 16:
        total = (total & 65535) + (total >> 16)
    return (~total) & 65535


def crafted_frame(ttl=4, destination='198.51.100.9'):
    if type(ttl) is not int or not 0 <= ttl <= 255:
        raise ValueError('TTL must be an integer from 0 to 255')
    source = ipaddress.IPv4Address('192.0.2.14').packed
    destination = ipaddress.IPv4Address(destination).packed
    header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 40, 1, 0, ttl, 6, 0, source, destination)
    header = header[:10] + struct.pack('!H', checksum(header)) + header[12:]
    ethernet = bytes.fromhex('aaaaaaaaaa01aaaaaaaaaa020800')
    # TCP ports 50000 -> 443; offset 5; no transport checksum is computed.
    tcp_stub = struct.pack('!HHIIBBHHH', 50000, 443, 0, 0, 0x50, 0x02, 4096, 0, 0)
    return ethernet + header + tcp_stub


def parse_frame(frame):
    if not isinstance(frame, bytes) or not 34 <= len(frame) <= 65549:
        raise ValueError('expected 34..65549 bytes for the untagged IPv4 teaching frame')
    if frame[12:14] != b'\x08\x00':
        raise ValueError('this parser accepts untagged Ethernet IPv4 only')
    ip = frame[14:]
    version, ihl = ip[0] >> 4, (ip[0] & 15) * 4
    if version != 4 or ihl < 20 or len(ip) < ihl:
        raise ValueError('invalid IPv4 version/header length')
    total = int.from_bytes(ip[2:4], 'big')
    if total < ihl or total > len(ip):
        raise ValueError('IPv4 total length is inconsistent with supplied bytes')
    if checksum(ip[:ihl]) != 0:
        raise ValueError('IPv4 header checksum mismatch')
    flags_offset = int.from_bytes(ip[6:8], 'big')
    if flags_offset & 0x8000:
        raise ValueError('reserved IPv4 flag is invalid')
    if flags_offset & 0x3fff:
        raise ValueError('fragmented datagrams are outside this model')
    result = {
        'dst_mac': ':'.join(f'{b:02x}' for b in frame[:6]),
        'ethertype': '0x0800', 'ip_header_bytes': ihl, 'ip_total_bytes': total,
        'ttl': ip[8], 'proto': ip[9],
        'src_ip': str(ipaddress.IPv4Address(ip[12:16])),
        'dst_ip': str(ipaddress.IPv4Address(ip[16:20])),
        'source_sha256': hashlib.sha256(frame).hexdigest(),
    }
    if ip[9] == 6:
        payload = ip[ihl:total]
        if len(payload) < 20 or payload[12] >> 4 < 5 or (payload[12] >> 4) * 4 > len(payload):
            raise ValueError('truncated/invalid TCP header in fixture')
        result['src_port'], result['dst_port'] = struct.unpack('!HH', payload[:4])
    return result


class PositiveDnsCache:
    """Positive A-only TTL model, not a recursive resolver or DNS wire parser."""
    def __init__(self):
        self.entries = {}
        self.clock = 0

    def lookup(self, name, now, authority):
        if not isinstance(name, str) or not name.lower().endswith('.example'):
            raise ValueError('use a fictional .example name')
        if type(now) is not int or now < self.clock:
            raise ValueError('use nondecreasing integer model seconds')
        self.clock = now
        key = name.lower()
        entry = self.entries.get(key)
        if entry and now < entry[1]:
            return {'address': entry[0], 'how': 'cache', 'remaining_seconds': entry[1] - now}
        # Authority is a local dictionary with (address, TTL); no DNS query is sent.
        if key not in authority:
            self.entries.pop(key, None)
            return {'address': None, 'how': 'not_in_fixture', 'remaining_seconds': 0}
        address, ttl = authority[key]
        if type(ttl) is not int or ttl < 0:
            raise ValueError('TTL must be a nonnegative integer')
        address = str(ipaddress.IPv4Address(address))
        if ttl:
            self.entries[key] = (address, now + ttl)
        else:
            self.entries.pop(key, None)
        return {'address': address, 'how': 'fixture_authority', 'remaining_seconds': ttl}


def lease_status(start, duration, now):
    if any(type(v) is not int or v < 0 for v in (start, duration, now)) or duration == 0 or now < start:
        raise ValueError('use nonnegative model seconds, positive duration, now >= start')
    remaining = max(0, start + duration - now)
    return {'state': 'active' if remaining else 'expired', 'remaining_seconds': remaining}


def ipv6_prefix(cidr):
    network = ipaddress.IPv6Network(cidr, strict=False)
    return {'network': str(network), 'address_count': network.num_addresses, 'has_broadcast': False}


def report(ttl=4, destination='198.51.100.9'):
    raw = crafted_frame(ttl, destination)
    parsed = parse_frame(raw)
    decision = forward(parsed['dst_ip'], parsed['ttl'], [('0.0.0.0/0', 'uplink'), ('198.51.100.0/24', 'eth1')])
    return {'version': 'packet-fixture/1.0.0-review', 'frame_hex': raw.hex(), 'parsed': parsed, 'decision': decision,
            'physical_measurement': False, 'competency_demonstrated': False,
            'boundary': 'Synthetic bytes; IPv4 checksum checked; no TCP checksum, ICMP, MAC rewrite, packet transmission, real DNS/DHCP or latency measurement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ttl', type=int, default=4)
    parser.add_argument('--destination', default='198.51.100.9')
    args = parser.parse_args()
    try:
        print(json.dumps(report(args.ttl, args.destination), indent=2))
    except ValueError as error:
        parser.exit(2, f'Fixture rejected: {error}\n')
