# Week 3: I2C sensors — address, frequency, NACK recovery

**Ticket:** EP-4303  
**Lab:** `lab_ep_i2c_timing`

## Objectives
- Place SSD1306-class address 0x3C at 100 kHz
- Require an explicit NACK recovery plan
- Treat bus errors as recoverable states, not vibes

## Body
Serial buses are contracts. I2C at 100 kHz with address 0x3C is the ForgeSense display-class fixture. If the device NACKs, your plan must say what happens next (retry count, bus clear, fail closed) — not 'try again somehow.'

Sensors and actuators share the same honesty rule: the JSON names bus, addr, freq_khz, nack_recovery. Screenshots of a logic analyzer GUI are not acceptance.

No-hardware fallback: use the fixture timing table. PHYSICAL_PENDING for probe hooks on real wires.

## Worked example
bus=i2c1, addr=0x3C, freq_khz=100, nack_recovery=true

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No inventing µA draw numbers without measurement
- No claiming production sensor qualification

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_i2c_timing` and `EP-4303`. Empty {} fails. A file whose body is only PASS raises.
