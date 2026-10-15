# Week 3: The MAC closet — learning, flooding, and VLAN 20

Pier hangs off Gi1/0/8 on VLAN 20. Yard hangs off Gi1/0/9 on VLAN 30. A frame destined to aa:aa:aa:aa:aa:10 in VLAN 20 egresses Gi1/0/8. The same MAC in VLAN 30 is a different key. If your mental model is 'MAC table is just MAC,' you have built a VLAN leak.

Unknown unicasts flood inside the VLAN, not across it. That sentence is the difference between a campus and a party line. Trunks carry VLAN tags; access ports do not surprise patrons with tagged frames.

CCNA v1.1 Network Access is the alignment label: VLANs, trunks, STP later. We configure none of that on a real Cisco in this packet. We compute forwarding on a fixture so the idea is testable offline.

Consider a hypothetical layer-2 loop with redundant links and no loop-prevention mechanism. Repeated frames can consume resources. This is an instructional scenario, not evidence of a prior cohort outage or a measured switch CPU load. Week 6 examines the modeled topology.

## Concept and scope

A learning Ethernet switch associates source MAC addresses with ports within a forwarding domain. Unknown destination behavior and broadcast forwarding are bounded by the VLAN. A MAC address observed in one VLAN does not automatically authorize forwarding in another.

## Guided practice

Draw a fictional table with MAC A on port 1 in VLAN 20 and MAC B on port 2 in VLAN 30. Predict forwarding for a frame to A arriving in VLAN 20, then the same destination arriving in VLAN 30. Expected interpretation: the second lookup must use VLAN 30, not reuse VLAN 20's entry. Explain the unknown-destination policy of your model rather than assuming all switches use an identical configuration.

## Independent evidence

Add a third port in VLAN 20 and trace source learning followed by a destination lookup. Record the input table and output decision. Do not change a campus switch to test this exercise.

## Worked example

mac_table[(aa:aa:aa:aa:aa:10, 20)] = Gi1/0/8. Lookup with VLAN 30 misses. Isolation holds.
