# Week 1: Power supply budget — parts, headroom, and the smallest adequate unit

Work order ISH-4101: a donated tower is getting a graphics card so a youth club can edit video, and the old 450 W power supply is suspect. Start with a parts list and each part's rated draw from its spec sheet, not from a forum guess. The processor is rated 125 W, the card 200 W, the motherboard about 50, two memory sticks about 10 together, the SSD about 8, and the fans about 12, for 405 W. A supply running near its limit gets hot, loud, and less efficient, and real loads spike above their averages, so the bench adds a quarter on top: 405 × 1.25 is 506.25 W. The smallest catalogue unit that covers it is 550 W, so the 450 W supply goes in the parts bin. Bigger is not automatically better, since a 1,000 W unit idling at 60 W wastes money and often efficiency. Check that the new supply has the right connectors for the card, and never open a supply's case; the capacitors inside can hold a dangerous charge long after it is unplugged.

## Worked example

CPU 125 + GPU 200 + board 50 + RAM 10 + SSD 8 + fans 12 = 405 W × 1.25 = 506.25 W → 550 W unit
