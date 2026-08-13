# Week 10: Failure diagnosis — digitally validate the subsystem

Final practical: symptoms rail_sag_3v3 + i2c_nack. Root cause among weak_regulator, missing_pullups, shared_rail_overload. next_probe must include measure. physical_status PHYSICAL_PENDING.

Capstone: digitally validate embedded subsystem (power + bus + DT + QEMU) with artifacts — not fabricated field yield claims.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

Evidence discipline week 10: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 10: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 10: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. 

## Worked example

symptoms include rail_sag_3v3 and i2c_nack; root_cause shared_rail_overload; next_probe measure 3V3 under load; PHYSICAL_PENDING.
