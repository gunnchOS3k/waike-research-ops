# Week 6 presentation — When VLANs meet a loop — STP as a circuit breaker

## Slide 1 — Cold open
Two access cables into one closet without STP → storm. BPDU guard on access would err-disable the volunteer mini-switch instead of electing it root.

## Slide 2 — Teaching beat
Rapid PVST+ is a CCNA v1.1 phrase. In the Packet Range we treat STP as a circuit breaker: one forwarding tree per VLAN, blocked ports that would otherwise loop. Root bridge is the switch with the best priority+MAC, not the one closest to the coffee.

## Slide 3 — Live work
Slice the crafted frame: bytes 0–5 dest MAC, 12–13 ethertype, IP[8] TTL. Then decrement a TTL=1 copy.

## Speaker notes
Refuse CS144 solutions and CCNA item banks. The datapath lab is original WAIKE Python.
