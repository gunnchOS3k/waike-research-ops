# Week 5: Power budget with real MPNs

Rail 3V3 budget using real MPNs: nRF52840 Iq, AMS1117-3.3 quiescent, SSD1306 OLED. Sum currents; margin = regulator_mA - total must be positive. Fake MPNs fail.

Datasheets are PUBLIC_REFERENCE_ONLY. Values in fixture are course-sanctioned numbers for the lab, not a claim about every SKU revision.

Show the week 5 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Rail 3V3 budget uses real MPN fields: nRF52840 Iq, AMS1117-3.3 quiescent, SSD1306 OLED draw. Sum currents; flag over-budget if sum exceeds the fixture rail limit. Invented datasheet currents fail honesty checks. EMBEDDED_PROTOTYPING integration: the same budget sheet feeds the subsystem packet later. PHYSICAL_PENDING for thermal camera / shunt measurements.

Journal week 5 (Power budget with real MPNs): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Worked example

nRF52840 5.4 + AMS1117 5.0 + SSD1306 10.0 = 20.4 mA; regulator 50 → margin 29.6.
