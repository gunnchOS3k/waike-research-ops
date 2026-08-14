# Hardware Engineering + Embedded Prototyping — ForgeSense Node

## Who this is for
Integrates HARDWARE_ENGINEERING and EMBEDDED_PROTOTYPING: SPICE nets, Thévenin, RC, logic, power budget with real MPNs, bus protocols, Zephyr west/QEMU, DT, PCB ERC/DRC/BOM, failure diagnosis. Sim/QEMU/Device Lab digital before physical; soldering/instruments PHYSICAL_PENDING. MIT 6.002/Zephyr/KiCad/datasheets are reference only.

## Tracks and academy
- Tracks: HARDWARE_ENGINEERING, EMBEDDED_PROTOTYPING
- Academy: ACADEMY_HARDWARE

## Duration
Ten Hardware+Embedded weeks with sim/QEMU before any iron. Budget quiet time for network math and DT overlays; PHYSICAL_PENDING blocks soldering until digital PASS.

## Weekly map
- Week 01: Device Lab bench — lumped nets before soldering
- Week 02: Thévenin of the sense divider
- Week 03: RC timing for the reset pin
- Week 04: NAND as the digital abstraction
- Week 05: Power budget with real MPNs
- Week 06: GPIO/I2C/SPI/UART — parse an I2C write
- Week 07: Zephyr west + QEMU before hardware
- Week 08: Devicetree overlay — I2C1 and LED0
- Week 09: PCB schematic/layout ERC/DRC + BOM
- Week 10: Failure diagnosis — digitally validate the subsystem

## Assessments
ForgeSense assessment mix: weekly circuit/embedded quizzes, mid (20 original) on dividers/Thevenin/RC/logic/power/bus, final (24 original) on Zephyr/DT/PCB/diagnosis, practical over ten digital labs, and a digitally validated subsystem project. Soldering remains PHYSICAL_PENDING. Fabricated yield claims fail.

## Claim boundary
Aligns to MIT OCW 6.002 rigor citations, Zephyr/KiCad/datasheet references. Integrates EMBEDDED_PROTOTYPING. Does not redistribute OCW problem sets or claim physical completion without evidence. Instructor keys stay out of the learner packet.

## Kinesthetic hook
Compute a divider, budget real MPNs, run Zephyr on QEMU, then digitally diagnose a sagging 3V3 rail.
