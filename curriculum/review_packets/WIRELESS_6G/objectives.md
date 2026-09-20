# Objectives — WIRELESS_6G

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Pier Radio Bench — free-space path loss without marketing
  - Complete the week contract: Pier Radio Bench — free-space path loss without marketing.
  - Reproduce worked example: d=120 m, f=3500 MHz → FSPL ≈ 20*log10(120)+20*log10(3500)-27.55 ≈ 84.9 dB.
  - The Pier Radio Bench sits under the Gary pier canopy: a USRP-class SDR, a scratched
ThinkPad, and a laminated card that says COMMERCIAL_STANDARDIZED_6G=false.
### Week 2: OFDM numerology intuition — symbols without a fake 6G waveform
  - Complete the week contract: OFDM numerology intuition — symbols without a fake 6G waveform.
  - Reproduce worked example: PRB BW = 12×30e3 = 360000 Hz; T_sym ≈ 1/30000 ≈ 33.33 μs (no CP).
  - Ticket WR-4202 ships a toy OFDM numerology card: Δf=30 kHz, N_sc=12 subcarriers per PRB,
symbol duration ≈ 1/Δf ignoring CP.
### Week 3: 5G-Advanced features map — Release labels without exam dumps
  - Complete the week contract: 5G-Advanced features map — Release labels without exam dumps.
  - Reproduce worked example: ≥3 features with release tags; commercial_6g_exists=false.
  - Ticket WR-4303 is a feature map: RedCap, XR awareness, NTN early hooks, AI/ML study items —
all PUBLIC_REFERENCE_ONLY.
### Week 4: Link adaptation toy — MCS vs BLER on a fixture
  - Complete the week contract: Link adaptation toy — MCS vs BLER on a fixture.
  - Reproduce worked example: SNR=8 dB, cap 0.1 → chosen_mcs=2 (BLER 0.09).
  - Ticket WR-4404 gives BLER for MCS 0..4 at SNR=8 dB: [0.40,0.22,0.09,0.18,0.35].
### Week 5: NTN LEO delay honesty — light-time, not sci-fi maps
  - Complete the week contract: NTN LEO delay honesty — light-time, not sci-fi maps.
  - Reproduce worked example: d=700 km → one_way≈2.333 ms, RTT≈4.667 ms; geo_comparable=false.
  - Ticket WR-4505: LEO altitude 550 km, slant ≈700 km.
### Week 6: Channel tap toy — RMS delay spread on pier railing fixture
  - Complete the week contract: Channel tap toy — RMS delay spread on pier railing fixture.
  - Reproduce worked example: Three-tap PDP → compute tau_rms_ns; tap_count=3.
  - Ticket WR-4606: delays_ns=[0,120,350], powers_db=[0,-3,-10].
### Week 7: AI-RAN control loop — gated policy, not magic autonomy
  - Complete the week contract: AI-RAN control loop — gated policy, not magic autonomy.
  - Reproduce worked example: human_gate=true; auto_apply_without_gate=false; action names MCS or PRB.
  - Ticket WR-4707: observe KPI window → propose MCS/PRB action → human gate → apply.
### Week 8: Spectrum honesty — masks and no unauthorized TX
  - Complete the week contract: Spectrum honesty — masks and no unauthorized TX.
  - Reproduce worked example: center 3.5 GHz, OBW 18 MHz, mask_ok true, unauthorized_tx false.
  - Ticket WR-4808: lab license narrative at 3.5 GHz, OBW 18 MHz.
### Week 9: O-RAN interface map — vocabulary without fake RIC production
  - Complete the week contract: O-RAN interface map — vocabulary without fake RIC production.
  - Reproduce worked example: interfaces include A1,E2,O1; deployed_full_ric=false.
  - Ticket WR-4909 maps A1/E2/O1/O2 to pier roles.
### Week 10: Capstone radio notebook — no Product-Use unmerged dependency
  - Complete the week contract: Capstone radio notebook — no Product-Use unmerged dependency.
  - Reproduce worked example: product_use_unmerged_consumed=false; commercial_6g false statement; labs_passed≥6.
  - Ticket WR-4910 assembles FSPL, numerology, MCS, NTN delay, AI-RAN gate, and spectrum digests
into one notebook hash.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
