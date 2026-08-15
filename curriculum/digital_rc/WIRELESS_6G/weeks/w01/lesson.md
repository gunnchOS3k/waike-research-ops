# Week 1: Pier Radio Bench — free-space path loss without marketing

The Pier Radio Bench sits under the Gary pier canopy: a USRP-class SDR, a scratched
ThinkPad, and a laminated card that says COMMERCIAL_STANDARDIZED_6G=false. Week 1 is
ticket WR-4101. Beginners want a 6G slide deck. Operators compute free-space path loss
for a 3.5 GHz pier hop at 120 m using FSPL_dB = 20*log10(d_m) + 20*log10(f_MHz) - 27.55.

Plug numbers on paper before any GUI: d=120, f=3500. That is the only number the lab
accepts. Pasting a vendor '6G ready' banner into the journal fails the claim boundary.

Consensus Ladder for WR-4101: observed = 120 m tape and 3.5 GHz center; inferred = FSPL
dominates this short clear hop; still need = pier-railing multipath (week 6).

Failure mode: claiming 'we have 6G coverage' because a slide said so. Operators speak
`fixtures/wr4101/fspl.json` with d_m, f_mhz, fspl_db. Invented 6G standard IDs fail.

Resource rule: light math fixtures only while Product-Use QEMU is busy — no multi-GB
Sionna/DeepMIMO tarballs on this ticket. Accessibility: journals stay text-first; any
optional plot needs an alt_text field in the portfolio later.

Work the Friis card on paper with a second hop length (95 m at 3500 MHz) so the class
sees how 20*log10(d) moves when the tape changes. Record both answers in the journal
with units. The Pier Radio Bench treats invented '6G coverage radius' strings as claim
boundary failures even when the arithmetic for FSPL is correct.

Operators also name the antenna assumption: isotropic teaching model, not a measured
panel pattern. If someone imports a vendor EIRP table without citing the fixture path
`fixtures/wr4101/fspl.json`, stop the demo and return to the laminated card.

## Worked example

d=120 m, f=3500 MHz → FSPL ≈ 20*log10(120)+20*log10(3500)-27.55 ≈ 84.9 dB.
