# Week 3 presentation — The MAC closet — learning, flooding, and VLAN 20

## Slide 1 — Cold open
mac_table[(aa:aa:aa:aa:aa:10, 20)] = Gi1/0/8. Lookup with VLAN 30 misses. Isolation holds.

## Slide 2 — Teaching beat
Pier hangs off Gi1/0/8 on VLAN 20. Yard hangs off Gi1/0/9 on VLAN 30. A frame destined to aa:aa:aa:aa:aa:10 in VLAN 20 egresses Gi1/0/8. The same MAC in VLAN 30 is a different key. If your mental model is 'MAC table is just MAC,' you have built a VLAN leak.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
