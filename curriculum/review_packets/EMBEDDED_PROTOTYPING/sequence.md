# Sequence — EMBEDDED_PROTOTYPING

Complete module/week sequence from `EMBEDDED_PROTOTYPING` `course.json`.

| Week | Title | Lesson ID | Lab ID |
|------|-------|-----------|--------|
| 1 | MCU memory map — flash vs SRAM before first boot | `EMBEDDED_PROTOTYPING-w01` | `lab_ep_memory_map` |
| 2 | GPIO contract — direction, pull, and safe defaults | `EMBEDDED_PROTOTYPING-w02` | `lab_ep_gpio_contract` |
| 3 | I2C timing — address, frequency, and NACK recovery | `EMBEDDED_PROTOTYPING-w03` | `lab_ep_i2c_timing` |
| 4 | SPI flash read — opcode and length honesty | `EMBEDDED_PROTOTYPING-w04` | `lab_ep_spi_flash` |
| 5 | ADC scaling — counts to millivolts | `EMBEDDED_PROTOTYPING-w05` | `lab_ep_adc_scale` |
| 6 | ISR vs polling — latency budget | `EMBEDDED_PROTOTYPING-w06` | `lab_ep_isr_vs_poll` |
| 7 | Zephyr west + QEMU — digital boot before iron | `EMBEDDED_PROTOTYPING-w07` | `lab_ep_zephyr_qemu` |
| 8 | Devicetree overlay — I2C1 and LED0 nodes | `EMBEDDED_PROTOTYPING-w08` | `lab_ep_dt_overlay` |
| 9 | Sleep modes — wake source honesty | `EMBEDDED_PROTOTYPING-w09` | `lab_ep_sleep_mode` |
| 10 | Subsystem capstone — QEMU + DT + bus evidence | `EMBEDDED_PROTOTYPING-w10` | `lab_ep_subsystem_capstone` |

## Syllabus excerpt (source)

```
# Embedded Systems and Device Prototyping — ForgeSense Subsystem Bench
## Who this is for
Standalone EMBEDDED_PROTOTYPING COURSE_DIGITAL_RC: MCU map, GPIO, I2C/SPI, ADC scaling, ISR latency, Zephyr west/QEMU, devicetree overlay, sleep modes, subsystem capstone. Complements HARDWARE_ENGINEERING SPICE path — does not replace it. Not student/teacher E6.
## Tracks and academy
- Tracks: EMBEDDED_PROTOTYPING
- Academy: ACADEMY_HARDWARE
## Duration
Ten ForgeSense Subsystem weeks (~6–8 hours/week). QEMU/digital-first; NO_AI weeks 4 and 9. PHYSICAL_PENDING for solder/OTA.
## Weekly map
- Week 01: MCU memory map — flash vs SRAM before first boot
- Week 02: GPIO contract — direction, pull, and safe defaults
- Week 03: I2C timing — address, frequency, and NACK recovery
- Week 04: SPI flash read — opcode and length honesty
- Week 05: ADC scaling — counts to millivolts
- Week 06: ISR vs polling — latency budget
- Week 07: Zephyr west + QEMU — digital boot before iron
- Week 08: Devicetree overlay — I2C1 and LED0 nodes
- Week 09: Sleep modes — wake source honesty
- Week 10: Subsystem capstone — QEMU + DT + bus evidence
## Assessments
ForgeSense Subsystem Bench: weekly EP quizzes on MCU/GPIO/I2C/SPI/ADC/ISR/QEMU/DT/sleep, mid (20 original) on digital-first honesty, final (24 original) on capstone + PHYSICAL_PENDING, practical over ten runnable labs, subsystem portfolio. Complements HARDWARE_ENGINEERING.
## Claim boundary
Zephyr/J-STD topic labels PUBLIC_REFERENCE_ONLY. Does not grant certs. Standalone track — complements HARDWARE_ENGINEERING integration. Instructor keys out of learner packet.
## Kinesthetic hook
Ten ForgeSense Subsystem Bench weeks: memory map → GPIO → I2C → SPI → ADC → ISR → Zephyr QEMU → DT overlay → sleep → capstone. Digital-first; PHYSICAL_PENDING for solder/OTA.
```

## Duration note

Package default is **10 weeks**. Program files may also list workshop/bootcamp/apprenticeship formats — those are alternate delivery envelopes, not alternate content claims.
