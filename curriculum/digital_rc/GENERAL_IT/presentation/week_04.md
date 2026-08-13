# Week 4 presentation — Storage, snapshots, and the Friday 16:00 panic

## Slide 1 — Cold open
size=256GiB used=180 reserved=12 → free=64 GiB → 64/256=0.25 ≥ 0.15. SHA256 of source tree must equal SHA256 of restored tree.

## Slide 2 — Teaching beat
The civic volume is 256 GiB. Used 180 GiB. Reserved 12 GiB for snapshots. The desk policy demands 15% free because Windows updates and browser profiles balloon without asking. Free = 256-180-12 = 64 GiB, which is 25% — you pass today. If used climbs to 220 GiB, you fail the policy before the disk is 'full,' and that is the point of a quota.

## Slide 3 — Live work
Put 1200 seconds, 15% free, and CHG window 18:00–21:00 on the board. Sit in silence until someone does the arithmetic.

## Speaker notes
If they ask for A+ dumps, close the slide and open the alignment JSON. Keys never leave the instructor packet.
