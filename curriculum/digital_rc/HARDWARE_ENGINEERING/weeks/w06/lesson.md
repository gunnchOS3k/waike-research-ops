# Week 6: GPIO/I2C/SPI/UART — parse an I2C write

Buses: GPIO edges, I2C addr+reg+data, SPI mode clocks, UART framing. Lab parses I2C write frame hex 3c00af → addr 0x3C reg 0x00 data 0xAF (OLED).

You will name which bus the OLED uses and why bit-bang GPIO is the wrong first debug when NACK appears.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

Evidence discipline week 6: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 6: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 6: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. 

## Worked example

frame_hex 3c00af → addr=0x3C reg=0x00 data=0xAF bus=I2C.
