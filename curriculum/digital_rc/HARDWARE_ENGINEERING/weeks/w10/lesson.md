# Week 10: Failure diagnosis — digitally validate the subsystem

Final practical: symptoms rail_sag_3v3 + i2c_nack. Root cause among weak_regulator, missing_pullups, shared_rail_overload. next_probe must include measure. physical_status PHYSICAL_PENDING.

Capstone: digitally validate embedded subsystem (power + bus + DT + QEMU) with artifacts — not fabricated field yield claims.

Show the week 10 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Symptoms rail_sag_3v3 + i2c_nack. Choose root cause among weak_regulator, missing_pullup, wrong_address, and open_gnd using the digital evidence pack — not gut feel. Capstone: assemble the subsystem packet (net math, Thévenin, RC, power, bus parse, west/QEMU, overlay, ERC/DRC) with PHYSICAL_PENDING where hardware is still pending. AI modes disclosed when used; NO_AI on the diagnosis practical.

Journal week 10 (Failure diagnosis — digitally validate the subsystem): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Worked example

symptoms include rail_sag_3v3 and i2c_nack; root_cause shared_rail_overload; next_probe measure 3V3 under load; PHYSICAL_PENDING.
