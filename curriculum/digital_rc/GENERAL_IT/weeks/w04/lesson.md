# Week 4: Storage, snapshots, and the Friday 16:00 panic

The civic volume is 256 GiB. Used 180 GiB. Reserved 12 GiB for snapshots. The desk policy demands 15% free because Windows updates and browser profiles balloon without asking. Free = 256-180-12 = 64 GiB, which is 25% — you pass today. If used climbs to 220 GiB, you fail the policy before the disk is 'full,' and that is the point of a quota.

Backup is a restore you have practiced. A `.tgz` that nobody has extracted is a rumor. The lab hashes the tree, archives, restores, and hashes again. If you exclude `ticket_4417.txt` because it 'looks temporary,' the patron essay is gone.

3-2-1 is the language: three copies, two media, one off-box. For this desk, that means the volume, a USB disk in the locked drawer, and a weekly encrypted copy to the staff closet PC. Cloud is optional and never the only copy — the closet floods less often than the WAN dies on Sunday.

PII still does not belong in the archive. The lab fails if you add `ssn.txt`. Backup is not a place to hide documents you would not leave on the desk.

## Worked example

size=256GiB used=180 reserved=12 → free=64 GiB → 64/256=0.25 ≥ 0.15. SHA256 of source tree must equal SHA256 of restored tree.
