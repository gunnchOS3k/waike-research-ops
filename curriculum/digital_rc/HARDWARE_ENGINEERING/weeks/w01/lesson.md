# Week 1: Device Lab bench — lumped nets before soldering

WAIKE Device Lab Hardware Studio opens with SPICE-class network analysis before any iron heats. PHYSICAL_PENDING covers soldering and instruments. Digitally you solve a series divider: R1=1k, R2=3k, Vin=12V → I=3mA, Vout=9V. The lab checks your arithmetic, not a screenshot of a GUI.

MIT OCW 6.002 is PUBLIC_REFERENCE_ONLY rigor citation: lumped abstraction, KCL/KVL habits. We do not redistribute OCW problem sets. KiCad appears later; this week is pure network math on original ForgeSense sensor node nets.

Show the week 1 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Series divider fixture: R1=1kΩ, R2=3kΩ, Vin=12V → I=Vin/(R1+R2)=3mA, Vout=Vin*R2/(R1+R2)=9V. The lab checks your arithmetic fields, not a SPICE GUI screenshot. MIT OCW 6.002 is PUBLIC_REFERENCE_ONLY for lumped abstraction and KCL/KVL habits; we do not redistribute OCW problem sets. KiCad comes later — this week is pure network math on ForgeSense sensor nets. PHYSICAL_PENDING covers soldering and instruments until digital validators pass.

## Worked example

R1=1000 R2=3000 Vin=12 → I=0.003 A Vout=9 V.
