# Week 5: Power budget with real MPNs

Rail 3V3 budget using real MPNs: nRF52840 Iq, AMS1117-3.3 quiescent, SSD1306 OLED. Sum currents; margin = regulator_mA - total must be positive. Fake MPNs fail.

Datasheets are PUBLIC_REFERENCE_ONLY. Values in fixture are course-sanctioned numbers for the lab, not a claim about every SKU revision.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

Evidence discipline week 5: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 5: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 5: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. 

## Worked example

nRF52840 5.4 + AMS1117 5.0 + SSD1306 10.0 = 20.4 mA; regulator 50 → margin 29.6.
