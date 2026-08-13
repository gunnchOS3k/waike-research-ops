# Week 3: RC timing for the reset pin

Reset RC: tau=R*C. Charging V(t)=V0(1-e^{-t/tau}). With R=1k C=1uF tau=1ms. At t=tau, Vt≈0.632 V0. Firmware that samples reset too early sees a lie. Lab checks tau and Vt math.

PHYSICAL_PENDING: scope capture of the real RC. Digital validation is mandatory first.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

Evidence discipline week 3: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 3: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. Evidence discipline week 3: keep ticket numbers, hashes, and fixture counts in the journal; do not replace them with adjectives. 

## Worked example

R=1000 C=1e-6 V0=5 t=0.001 → tau=0.001 Vt=5*(1-e^{-1}).
