# Week 2: IPv6 text and prefixes — one canonical way to write an address

NIF-5202 began as an outage: two engineers searched the change log for the same router address and missed each other because they had typed it differently. IPv6 addresses are 128 bits, written as eight groups of four hex digits, and RFC 5952 sets one canonical text form so tools and people agree. Write hex in lowercase, drop leading zeros in each group, and replace the longest run of two or more all-zero groups with a double colon, choosing the first run if two are equally long. A single zero group stays as 0. So 2001:0DB8:0000:0000:0001:0000:0000:0001 has two runs of two zero groups; the first one collapses and the result is 2001:db8::1:0:0:1. The 2001:db8::/32 block is reserved for documentation, which is why this course uses it. Prefix math is about counting bits: a site receives a /48, and LAN segments are /64, so 64 minus 48 leaves 16 bits for subnet numbers, which is 65,536 subnets. Never squeeze a LAN smaller than /64; address autoconfiguration expects it.

## Worked example

2001:0DB8:0000:0000:0001:0000:0000:0001 → 2001:db8::1:0:0:1; /48 site → /64 subnets: 2^16 = 65,536
