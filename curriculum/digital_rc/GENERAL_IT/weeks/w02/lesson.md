# Week 2: Two operating systems, one pair of hands

The Civic Tech Desk dual-boots a Windows 11 image for walk-up patrons and a Debian bookworm image for staff recovery. You will not memorize every click. You will learn the same three verbs on both: list, copy, and permission. On Windows those verbs are Explorer, `robocopy` or copy, and icacls. On Debian they are `ls`, `cp`, and `chmod`/`chown`.

File systems are not fashion. The staff recovery stick is ext4. The patron share that must be read by Windows is exFAT. NTFS is fine for the internal Windows volume. FAT32 still appears on old camera cards and lies about files over 4 GiB. When a 4.7 GiB video 'disappears' on a camera card, the card is not haunted — FAT32 refused the write.

Task Manager and `top` answer the same question: who is burning CPU and who is waiting on disk. A kiosk that feels 'frozen' with disk 100% and CPU 4% is a storage job, not a virus story. You will capture that evidence before you reboot, because reboot erases the graph.

Updates are operational procedures. The desk patches Windows after 21:00 local on Wednesdays and Debian with unattended-upgrades, but never both images in the same hour. A dual-boot machine that patches both at once can leave GRUB confused and a Saturday volunteer with no kiosk.

## Worked example

A 4.7 GiB `.mkv` copied to a FAT32 camera card ends as a 0-byte or missing file. Reformat is the wrong first step. Copy to the NTFS staff volume, then to the patron exFAT share.
