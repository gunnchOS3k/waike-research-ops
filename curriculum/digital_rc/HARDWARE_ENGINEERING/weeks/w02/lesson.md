# Week 2: Thévenin of the sense divider

Seen from the ADC pin, the divider becomes Vth and Rth. Vth=Vin*R2/(R1+R2), Rth=R1||R2. For 12V/1k/3k: Vth=9V, Rth=750Ω. Loading the node with ADC input resistance changes reading — quantify before you blame the firmware.

This week integrates HARDWARE_ENGINEERING analysis with EMBEDDED_PROTOTYPING measurement planning: you will later sample this node from Zephyr QEMU fixtures.

Show the week 2 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

From the ADC pin: Vth=Vin*R2/(R1+R2)=9V and Rth=R1∥R2=750Ω for the 12V/1k/3k fixture. Loading the node with finite ADC input resistance changes the reading — quantify before blaming firmware. This week bridges HARDWARE_ENGINEERING analysis to EMBEDDED_PROTOTYPING measurement planning: later you sample this node from Zephyr QEMU fixtures. Invented Thévenin numbers fail the recomputed checks.

## Worked example

Vth=9 Rth=750 for Vin=12 R1=1k R2=3k.
