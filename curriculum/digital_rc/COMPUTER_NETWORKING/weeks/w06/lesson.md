# Week 6: When VLANs meet a loop — STP as a circuit breaker

Rapid PVST+ is a CCNA v1.1 phrase. In the Packet Range we treat STP as a circuit breaker: one forwarding tree per VLAN, blocked ports that would otherwise loop. Root bridge is the switch with the best priority+MAC, not the one closest to the coffee.

BPDU guard on access ports is how a volunteer plugging a 'helpful' mini-switch does not become the new root. You will explain that sentence in plain English. You will not paste Cisco config from a dump.

EtherChannel is two cables acting as one logical link so a single unplug does not partition Yard. It is not 'more Internet.' Misconfigured channel (one side on, one side off) is a loop factory.

Week 3's scar returns as a postmortem: which port should have been blocking, which VLAN flooded, and what evidence (CPU, MAC flapping) you would collect next time.

## Worked example

Two access cables into one closet without STP → storm. BPDU guard on access would err-disable the volunteer mini-switch instead of electing it root.
