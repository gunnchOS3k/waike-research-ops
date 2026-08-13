# Week 9 presentation — ACLs that actually order, and the telnet we refuse

## Slide 1 — Cold open
decide(23)=deny, decide(443)=permit, decide(9)=deny. NAT still maps the inside host.

## Slide 2 — Teaching beat
An ACL is a story told top to bottom. Deny tcp/23, permit tcp/443, deny *. Telnet is a classroom fossil we refuse at the edge. HTTPS to the library cache is allowed. Port 9 discard is denied by the star rule — implicit deny made visible.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
