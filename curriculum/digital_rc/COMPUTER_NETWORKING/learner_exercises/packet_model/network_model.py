"""Deterministic, local teaching calculations. Sends no packets."""
import ipaddress
import math

def segment_count(stream_bytes, mtu=1500, ip_header=20, tcp_header=20):
    for value in (stream_bytes, mtu, ip_header, tcp_header):
        if type(value) is not int or value < 0:
            raise ValueError('Use nonnegative integer byte counts')
    payload=mtu-ip_header-tcp_header
    if payload<=0: raise ValueError('Headers must leave room for data')
    return math.ceil(stream_bytes/payload)

def ipv4_summary(cidr):
    network=ipaddress.IPv4Network(cidr, strict=False)
    # /31 follows point-to-point convention; /32 represents one host route.
    usable=network.num_addresses if network.prefixlen>=31 else network.num_addresses-2
    return {'network':str(network.network_address),'broadcast':str(network.broadcast_address),'usable':usable}

def forward(destination, ttl, routes):
    if type(ttl) is not int or not 0 <= ttl <= 255: raise ValueError('Invalid TTL')
    if ttl <= 1: return {'action':'drop','reason':'ttl_expired'}
    address=ipaddress.IPv4Address(destination)
    matches=[(ipaddress.IPv4Network(cidr),port) for cidr,port in routes if address in ipaddress.IPv4Network(cidr)]
    if not matches:return {'action':'drop','reason':'no_route'}
    network,port=max(matches,key=lambda row:row[0].prefixlen)
    return {'action':'forward','port':port,'ttl':ttl-1,'prefix':str(network)}
