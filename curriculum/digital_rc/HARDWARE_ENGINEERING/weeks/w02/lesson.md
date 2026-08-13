# Week 2: Thévenin of the sense divider

Seen from the ADC pin, the divider becomes Vth and Rth. Vth=Vin*R2/(R1+R2), Rth=R1||R2. For 12V/1k/3k: Vth=9V, Rth=750Ω. Loading the node with ADC input resistance changes reading — quantify before you blame the firmware.

This week integrates HARDWARE_ENGINEERING analysis with EMBEDDED_PROTOTYPING measurement planning: you will later sample this node from Zephyr QEMU fixtures.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

Evidence discipline week 2: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 2: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 2: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. 

## Worked example

Vth=9 Rth=750 for Vin=12 R1=1k R2=3k.
