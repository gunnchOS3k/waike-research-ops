# Week 7: Optical link budget — loss, margin, and the 3 dB rule

NIF-5707 is a NO_AI week: do the decibel arithmetic on paper first. A field team must confirm that optics with a 0 dBm transmitter and a receiver sensitivity of −23 dBm will work over a new 40 km span. Decibels add, which is why engineers like them. The planning coefficients are 0.35 dB per kilometre of fiber, 0.5 dB for each mated connector, and 0.1 dB for each fusion splice. Forty kilometres costs 14 dB, four connectors cost 2, and six splices cost 0.6, for 16.6 dB in total. The light arrives at −16.6 dBm, and the receiver can still read it down to −23, so the margin is 6.4 dB. The backbone rule asks for at least 3 dB of margin to cover ageing, dirty connectors, temperature, and the repair splices a backhoe will eventually require, so this span passes. Counting only fiber loss would claim 9 dB of margin and hide two decibels of connectors. Clean and inspect every connector before measuring, and compare the light meter's reading with the budget.

## Worked example

40 km × 0.35 + 4 × 0.5 + 6 × 0.1 = 16.6 dB loss; margin = 0 − 16.6 − (−23) = 6.4 dB ≥ 3 → passes
