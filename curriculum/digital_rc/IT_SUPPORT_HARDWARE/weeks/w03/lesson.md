# Week 3: RAID — usable space, tolerated failures, and why it is not a backup

ISH-4303 is a NO_AI week; build the table by hand. A community centre wants its donated four-bay storage box set up for shared files, with four 4 TB disks. RAID combines disks into one volume with different trade-offs. RAID 0 stripes data across all four for 16 TB and speed, but any single failure loses everything. RAID 1 mirrors the same data on every disk: only 4 TB usable, yet three disks can die. RAID 5 spreads one disk's worth of parity, leaving 12 TB and surviving one failure. RAID 6 uses two disks' worth of parity for 8 TB and survives any two. RAID 10 mirrors pairs and stripes across them, also 8 TB; it is guaranteed to survive one failure and survives a second only if it hits the other pair, so the honest table says one. With large disks, rebuilding after a failure takes many hours and stresses the survivors, which is why RAID 6 suits this box better than RAID 5. Most important: RAID protects against a disk dying, not against deletion, ransomware, or fire, because those damage every copy at once. The centre still needs the 3-2-1 backup plan.

## Worked example

four 4 TB disks: RAID 0 16 TB/0, RAID 1 4 TB/3, RAID 5 12 TB/1, RAID 6 8 TB/2, RAID 10 8 TB/1 guaranteed
