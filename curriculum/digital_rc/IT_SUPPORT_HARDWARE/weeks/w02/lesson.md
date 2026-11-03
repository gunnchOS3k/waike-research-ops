# Week 2: Memory channels — the slots you choose set the bandwidth

ISH-4202 is a slow machine that has two good memory sticks in it. Desktop boards usually have two memory channels, labelled A and B, each a separate 64-bit path to the processor. Each transfer moves eight bytes per channel, so peak bandwidth in gigabytes per second is the transfer rate in megatransfers per second times eight times the number of channels, divided by a thousand. DDR4-3200 in one channel gives 25.6 GB/s; spread across both channels it gives 51.2. The previous volunteer pushed both sticks into A1 and A2, which sit on the same channel, so the machine runs single-channel and integrated graphics, which borrow system memory, crawl. Moving one stick to B2 doubles the path without buying anything. The board manual names the preferred slots, often A2 and B2 for two sticks, and the firmware setup screen confirms the mode after a reboot. Handle sticks by the edges, match the notch to the key in the slot, and press until both latches click; a half-seated stick is a classic cause of beeps and no display.

## Worked example

DDR4-3200 in A2 + B2 → 2 channels → 3200 × 8 × 2 / 1000 = 51.2 GB/s; in A1 + A2 → 1 channel → 25.6 GB/s
