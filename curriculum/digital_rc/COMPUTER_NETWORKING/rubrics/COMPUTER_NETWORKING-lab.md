# Packet Range lab

- **datapath_parse** (30%): Student reports TTL from bytes 14+8, not a hardcoded 4
- **ttl1_drop** (25%): A crafted TTL=1 header decrements to 0 and is not forwarded
- **lpm** (25%): /24 beats /16; /32 steals the host
- **acl_order** (20%): deny tcp/23 before permit 443 before deny *
