# Week 4: SPI flash read — opcode and length honesty

**Ticket:** EP-4404  
**Lab:** `lab_ep_spi_flash`

## Objectives
- Hand-author SPI read opcode/addr/length
- Require crc_ok true on fixture
- NO_AI authorship for frame fields

## Body
SPI flash read (opcode 0x03 class) needs address and length honesty. Claiming you read 256 bytes when the fixture issued 16 is a length lie — the same class of bug CYBER_SOC teaches in a toy parser, applied here to firmware storage.

NO_AI week for the frame fields: you may use EXPLAIN orally, but submitted opcode/addr/read_len/crc_ok are authored without generative paste.

## Worked example
opcode=0x03, addr=0x00001000, read_len=16, crc_ok=true

## Assessment mode
NO_AI

## Claim refusals
- No generative paste of SPI frame fields
- No claiming external flash part qualification

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_spi_flash` and `EP-4404`. Empty {} fails. A file whose body is only PASS raises.
