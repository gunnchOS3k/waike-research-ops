# Week 6: Channel tap toy — RMS delay spread on pier railing fixture

Ticket WR-4606: delays_ns=[0,120,350], powers_db=[0,-3,-10]. Compute discrete PDP RMS delay
spread with linear powers. Lab checks tau_rms_ns within tolerance and tap_count=3.

Multipath is a number, not a vibe. Claiming 'AI beamforming solved multipath' without taps
fails. PHYSICAL sounding stays PHYSICAL_PENDING.

Consensus Ladder: observed = tap table; inferred = late energy grows τ_rms; still need =
measured sounding. Empty {} fails. Wrong τ_rms fails. PASS raises.

Convert powers_db to linear, form the first and second moments of delay, then take the
square root for τ_rms. Change the last tap power by −1 dB as a sensitivity check and
note how τ_rms moves. PHYSICAL sounding stays PHYSICAL_PENDING until a real capture
exists; AI beamforming slogans without taps score zero.

Submit delays_ns, powers_db, tau_rms_ns, and tap_count=3. Wrong moments fail even when
the journal prose is polished.

## Worked example

Three-tap PDP → compute tau_rms_ns; tap_count=3.
