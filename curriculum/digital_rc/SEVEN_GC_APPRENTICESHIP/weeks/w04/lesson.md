# Week 4: LEO Doppler — orbital speed and the upper bound

SGA-1404 is a NO_AI week: work the numbers by hand and show each line. A satellite in a circular orbit moves at v = sqrt(μ / r), where μ for Earth is 398,600.4418 km³/s² and r is Earth's mean radius of 6,371 km plus the altitude. At 600 km that gives r = 6,971 km and v ≈ 7.5617 km/s, roughly 27,000 km/h. The carrier seen by a ground user shifts by the component of that velocity along the line of sight, so the shift can never exceed (v / c) · f_c. At a 2 GHz S-band carrier the bound is about 50.45 kHz, which is more than three times the 15 kHz subcarrier spacing of a common NR numerology, so uncompensated Doppler would smear subcarriers into each other. The true maximum seen from the ground is somewhat lower because Earth's curvature and the user's own rotation change the geometry, and it falls to zero as the satellite passes overhead. That is why the lab names this an upper bound and sets bound_is_upper = true. A bound is a design margin, not a measurement, and the claim ledger from week one should file it as SYNTHETIC_SIM or CITED_SPEC.

## Worked example

v = sqrt(398600.4418 / (6371 + 600)) = 7.5617 km/s; f_d ≤ (v/c)·f_c = 50.45 kHz at 2 GHz
