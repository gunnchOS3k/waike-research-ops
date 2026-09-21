# Objectives — HARDWARE_ENGINEERING

## Program learning outcomes

_GAP: no numbered learning outcomes extracted from program file — use package week contracts._

## Week-level objectives (from package lessons)

### Week 1: Device Lab bench — lumped nets before soldering
  - Complete the week contract: Device Lab bench — lumped nets before soldering.
  - Reproduce worked example: R1=1000 R2=3000 Vin=12 → I=0.003 A Vout=9 V.
  - WAIKE Device Lab Hardware Studio opens with SPICE-class network analysis before any iron heats.
### Week 2: Thévenin of the sense divider
  - Complete the week contract: Thévenin of the sense divider.
  - Reproduce worked example: Vth=9 Rth=750 for Vin=12 R1=1k R2=3k.
  - Seen from the ADC pin, the divider becomes Vth and Rth.
### Week 3: RC timing for the reset pin
  - Complete the week contract: RC timing for the reset pin.
  - Reproduce worked example: R=1000 C=1e-6 V0=5 t=0.001 → tau=0.001 Vt=5*(1-e^{-1}).
### Week 4: NAND as the digital abstraction
  - Complete the week contract: NAND as the digital abstraction.
  - Reproduce worked example: NAND rows (0,0)->1 (0,1)->1 (1,0)->1 (1,1)->0.
  - 2-input NAND truth: only 1,1 yields 0.
### Week 5: Power budget with real MPNs
  - Complete the week contract: Power budget with real MPNs.
  - Reproduce worked example: nRF52840 5.4 + AMS1117 5.0 + SSD1306 10.0 = 20.4 mA; regulator 50 → margin 29.6.
  - Rail 3V3 budget using real MPNs: nRF52840 Iq, AMS1117-3.3 quiescent, SSD1306 OLED.
### Week 6: GPIO/I2C/SPI/UART — parse an I2C write
  - Complete the week contract: GPIO/I2C/SPI/UART — parse an I2C write.
  - Reproduce worked example: frame_hex 3c00af → addr=0x3C reg=0x00 data=0xAF bus=I2C.
  - Buses: GPIO edges, I2C addr+reg+data, SPI mode clocks, UART framing.
### Week 7: Zephyr west + QEMU before hardware
  - Complete the week contract: Zephyr west + QEMU before hardware.
  - Reproduce worked example: board=qemu_cortex_m0 west_cmd includes west build -b qemu_cortex_m0; PHYSICAL_PENDING; qemu_ok true.
  - west build -b qemu_cortex_m0 for the ForgeSense app.
### Week 8: Devicetree overlay — I2C1 and LED0
  - Complete the week contract: Devicetree overlay — I2C1 and LED0.
  - Reproduce worked example: i2c1_status=okay; led0_gpios set; overlay contains &i2c1 and led0.
  - Overlay enables &i2c1 status okay and led0 gpios.
### Week 9: PCB schematic/layout ERC/DRC + BOM
  - Complete the week contract: PCB schematic/layout ERC/DRC + BOM.
  - Reproduce worked example: erc_errors=0 drc_errors=0 unconnected_power=false bom with nRF52840, AMS1117-3.3, SSD1306.
  - KiCad docs are reference.
### Week 10: Failure diagnosis — digitally validate the subsystem
  - Complete the week contract: Failure diagnosis — digitally validate the subsystem.
  - Reproduce worked example: symptoms include rail_sag_3v3 and i2c_nack; root_cause shared_rail_overload; next_probe measure 3V3 under load; PHYSICAL_PENDING.
  - Final practical: symptoms rail_sag_3v3 + i2c_nack.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
