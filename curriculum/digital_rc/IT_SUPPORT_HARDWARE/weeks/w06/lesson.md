# Week 6: Display bandwidth — will the cable carry the mode?

ISH-4606: a donated 4K monitor flickers or drops to 30 Hz on a refurbished PC. A screen mode is a stream of pixels, and the cable has a ceiling. Multiply width by height by refresh rate by bits per pixel: 3,840 by 2,160 at 60 Hz with 24-bit colour is about 11.94 gigabits per second. That ignores the blanking intervals between lines and frames, so the true need is somewhat higher, and the honest label is lower bound. Compare it with each link's usable data rate after encoding overhead: HDMI 1.4 carries about 8.16, HDMI 2.0 about 14.4, and DisplayPort 1.4 about 25.92. The 4K 60 Hz mode fits HDMI 2.0 and DisplayPort 1.4 but not HDMI 1.4, which is why the old port falls back to 30 Hz. Double the refresh to 120 Hz and the need becomes about 23.89 Gbit/s, which only DisplayPort 1.4 carries uncompressed here. Cables and ports are both links in the chain: a certified high-speed cable on an old port still runs at the old port's speed, so read both before promising a customer a mode.

## Worked example

3840×2160×60×24 = 11.94 Gbit/s → fits HDMI 2.0 (14.4) and DP 1.4 (25.92), not HDMI 1.4 (8.16); at 120 Hz 23.89 Gbit/s → only DP 1.4
