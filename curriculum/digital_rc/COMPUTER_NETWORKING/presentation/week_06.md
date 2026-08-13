# Week 6 presentation — When VLANs meet a loop — STP as a circuit breaker

## Slide 1 — Cold open
Two access cables into one closet without STP → storm. BPDU guard on access would err-disable the volunteer mini-switch instead of electing it root.

## Slide 2 — Teaching beat
Rapid PVST+ is a CCNA v1.1 phrase. In the Packet Range we treat STP as a circuit breaker: one forwarding tree per VLAN, blocked ports that would otherwise loop. Root bridge is the switch with the best priority+MAC, not the one closest to the coffee.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
