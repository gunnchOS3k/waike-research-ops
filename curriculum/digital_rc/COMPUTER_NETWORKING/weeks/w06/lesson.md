# Week 6: When VLANs meet a loop — STP as a circuit breaker

Rapid PVST+ is a CCNA v1.1 phrase. In the Packet Range we treat STP as a circuit breaker: one forwarding tree per VLAN, blocked ports that would otherwise loop. Root bridge is the switch with the best priority+MAC, not the one closest to the coffee.

BPDU guard on access ports is how a volunteer plugging a 'helpful' mini-switch does not become the new root. You will explain that sentence in plain English. You will not paste Cisco config from a dump.

EtherChannel is two cables acting as one logical link so a single unplug does not partition Yard. It is not 'more Internet.' Misconfigured channel (one side on, one side off) is a loop factory.

Week 3's scar returns as a postmortem: which port should have been blocking, which VLAN flooded, and what evidence (CPU, MAC flapping) you would collect next time.

## Concept and scope

A Layer-2 forwarding loop can circulate frames and amplify broadcasts. A spanning-tree protocol chooses a loop-free active topology while retaining alternative physical links according to its rules. A blocked forwarding port is not necessarily a broken cable.

## Guided practice

Draw three fictional switches linked in a triangle. Mark one logical edge non-forwarding for your simplified model. Trace a broadcast over the active edges and count the copies per edge. Expected result: the active graph has no cycle. Remove one active link and draw a proposed replacement tree, labeling the reconfiguration as simulated.

## Independent evidence

Explain what measurements would be needed to evaluate a real protocol's convergence and disruption. Never connect an unauthorized loop to a real network. A diagram proves only a property of the graph you drew.

## Worked example

Two access cables into one closet without STP → storm. BPDU guard on access would err-disable the volunteer mini-switch instead of electing it root.
