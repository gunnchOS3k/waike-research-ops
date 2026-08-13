# Week 3: RC timing for the reset pin

Reset RC: tau=R*C. Charging V(t)=V0(1-e^{-t/tau}). With R=1k C=1uF tau=1ms. At t=tau, Vt≈0.632 V0. Firmware that samples reset too early sees a lie. Lab checks tau and Vt math.

PHYSICAL_PENDING: scope capture of the real RC. Digital validation is mandatory first.

Show the week 3 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Reset RC: τ=R·C. With R=1kΩ and C=1µF, τ=1ms. Charging V(t)=V0(1−e^{−t/τ}); at t=τ, Vt≈0.632·V0. Firmware that samples reset too early sees a lie. Lab checks τ and Vt math to stated precision. PHYSICAL_PENDING: scope capture of the real RC stays pending; digital validation is mandatory first. Cite timing concepts; do not invent scope screenshots.

Journal week 3 (RC timing for the reset pin): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

Week 3 digital validators must pass before any PHYSICAL_PENDING soldering or instrument claim; show the arithmetic or parse fields the lab recomputes.

## Worked example

R=1000 C=1e-6 V0=5 t=0.001 → tau=0.001 Vt=5*(1-e^{-1}).
