# Week 6: GPIO/I2C/SPI/UART — parse an I2C write

Buses: GPIO edges, I2C addr+reg+data, SPI mode clocks, UART framing. Lab parses I2C write frame hex 3c00af → addr 0x3C reg 0x00 data 0xAF (OLED).

You will name which bus the OLED uses and why bit-bang GPIO is the wrong first debug when NACK appears.

Show the week 6 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Buses: GPIO edges, I2C addr+reg+data, SPI mode clocks, UART framing. Lab parses an I2C write byte sequence and checks address, register, and payload fields. Wrong address ACKs are not success. Keep protocol vocabulary precise so this lab is not a noun-swap of networking packet labs from batch-001.

Journal week 6 (GPIO/I2C/SPI/UART — parse an I2C write): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

Week 6 digital validators must pass before any PHYSICAL_PENDING soldering or instrument claim; show the arithmetic or parse fields the lab recomputes.

## Worked example

frame_hex 3c00af → addr=0x3C reg=0x00 data=0xAF bus=I2C.
