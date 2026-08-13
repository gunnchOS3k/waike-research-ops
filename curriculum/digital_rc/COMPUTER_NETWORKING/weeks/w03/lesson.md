# Week 3: The MAC closet — learning, flooding, and VLAN 20

Pier hangs off Gi1/0/8 on VLAN 20. Yard hangs off Gi1/0/9 on VLAN 30. A frame destined to aa:aa:aa:aa:aa:10 in VLAN 20 egresses Gi1/0/8. The same MAC in VLAN 30 is a different key. If your mental model is 'MAC table is just MAC,' you have built a VLAN leak.

Unknown unicasts flood inside the VLAN, not across it. That sentence is the difference between a campus and a party line. Trunks carry VLAN tags; access ports do not surprise patrons with tagged frames.

CCNA v1.1 Network Access is the alignment label: VLANs, trunks, STP later. We configure none of that on a real Cisco in this packet. We compute forwarding on a fixture so the idea is testable offline.

A loop without STP is how the Packet Range went dark in a previous cohort: two cables into the same closet, broadcast joy, CPU 100% on the cheap switch. Week 6 returns to that scar.

## Worked example

mac_table[(aa:aa:aa:aa:aa:10, 20)] = Gi1/0/8. Lookup with VLAN 30 misses. Isolation holds.
