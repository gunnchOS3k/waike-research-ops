# Objectives — EMBEDDED_PROTOTYPING

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: MCU memory map — flash vs SRAM before first boot
  - Complete the week contract: MCU memory map — flash vs SRAM before first boot.
  - Reproduce worked example: flash_base=0x00000000, sram_base=0x20000000, vector_table_offset=0x100
  - ForgeSense Subsystem Bench ticket EP-4101: MCU memory map — flash vs SRAM before first boot.
### Week 2: GPIO contract — direction, pull, and safe defaults
  - Complete the week contract: GPIO contract — direction, pull, and safe defaults.
  - Reproduce worked example: pin=LED0, direction=out, default_level=0, pull=none
  - ForgeSense Subsystem Bench ticket EP-4202: GPIO contract — direction, pull, and safe defaults.
### Week 3: I2C timing — address, frequency, and NACK recovery
  - Complete the week contract: I2C timing — address, frequency, and NACK recovery.
  - Reproduce worked example: bus=i2c1, addr=0x3C, freq_khz=100, nack_recovery=true
  - ForgeSense Subsystem Bench ticket EP-4303: I2C timing — address, frequency, and NACK recovery.
### Week 4: SPI flash read — opcode and length honesty
  - Complete the week contract: SPI flash read — opcode and length honesty.
  - Reproduce worked example: opcode=0x03, addr=0x00001000, read_len=16, crc_ok=true
  - ForgeSense Subsystem Bench ticket EP-4404: SPI flash read — opcode and length honesty.
### Week 5: ADC scaling — counts to millivolts
  - Complete the week contract: ADC scaling — counts to millivolts.
  - Reproduce worked example: raw=2048, vref_mv=3300, resolution_bits=12, mv=1650
  - ForgeSense Subsystem Bench ticket EP-4505: ADC scaling — counts to millivolts.
### Week 6: ISR vs polling — latency budget
  - Complete the week contract: ISR vs polling — latency budget.
  - Reproduce worked example: mode=isr, max_latency_us=250, missed_edges=0
  - ForgeSense Subsystem Bench ticket EP-4606: ISR vs polling — latency budget.
### Week 7: Zephyr west + QEMU — digital boot before iron
  - Complete the week contract: Zephyr west + QEMU — digital boot before iron.
  - Reproduce worked example: board=qemu_cortex_m0, qemu_ok=true, physical_status=PHYSICAL_PENDING
  - ForgeSense Subsystem Bench ticket EP-4707: Zephyr west + QEMU — digital boot before iron.
### Week 8: Devicetree overlay — I2C1 and LED0 nodes
  - Complete the week contract: Devicetree overlay — I2C1 and LED0 nodes.
  - Reproduce worked example: overlay_has_i2c1=true, overlay_has_led0=true, delete_soc=false
  - ForgeSense Subsystem Bench ticket EP-4808: Devicetree overlay — I2C1 and LED0 nodes.
### Week 9: Sleep modes — wake source honesty
  - Complete the week contract: Sleep modes — wake source honesty.
  - Reproduce worked example: sleep_mode=SYSTEM_OFF, wake_gpio=BTN0, wake_latency_ms=5
  - ForgeSense Subsystem Bench ticket EP-4909: Sleep modes — wake source honesty.
### Week 10: Subsystem capstone — QEMU + DT + bus evidence
  - Complete the week contract: Subsystem capstone — QEMU + DT + bus evidence.
  - Reproduce worked example: labs_passed≥6, qemu_ok=true, dt_ok=true, physical_status=PHYSICAL_PENDING
  - ForgeSense Subsystem Bench ticket EP-4A10: Subsystem capstone — QEMU + DT + bus evidence.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
