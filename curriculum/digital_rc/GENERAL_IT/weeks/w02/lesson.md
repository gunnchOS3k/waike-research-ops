# Week 2: Two operating systems, one pair of hands

The Civic Tech Desk dual-boots a Windows 11 image for walk-up patrons and a Debian bookworm image for staff recovery. You will not memorize every click. You will learn the same three verbs on both: list, copy, and permission. On Windows those verbs are Explorer, `robocopy` or copy, and icacls. On Debian they are `ls`, `cp`, and `chmod`/`chown`.

File systems are not fashion. The staff recovery stick is ext4. The patron share that must be read by Windows is exFAT. NTFS is fine for the internal Windows volume. FAT32 still appears on old camera cards and lies about files over 4 GiB. When a 4.7 GiB video 'disappears' on a camera card, the card is not haunted — FAT32 refused the write.

Task Manager and `top` answer the same question: who is burning CPU and who is waiting on disk. A kiosk that feels 'frozen' with disk 100% and CPU 4% is a storage job, not a virus story. You will capture that evidence before you reboot, because reboot erases the graph.

Updates are operational procedures. The desk patches Windows after 21:00 local on Wednesdays and Debian with unattended-upgrades, but never both images in the same hour. A dual-boot machine that patches both at once can leave GRUB confused and a Saturday volunteer with no kiosk.

## Learn the distinction

An operating system manages processes, memory, devices and access to files. A graphical file manager and a command-line shell provide different ways to request operations; neither is the operating system itself. Paths identify locations. Relative paths start from a current directory; absolute paths identify a location from a filesystem root. Case sensitivity and path syntax vary with the filesystem and configuration.

## Guided practice: compare two interfaces

Use your own practice folder, not system directories. First list its files in a graphical file manager. Then use a terminal only if it is available: Windows PowerShell `Get-ChildItem` or a POSIX shell `ls`. Record the current directory using `Get-Location` or `pwd`. Do not assume that two terminal windows start in the same directory. Copy `essay.txt` to a new name using the file manager. List again in the terminal. Expected result: both interfaces show the new saved file after refresh. Reopen the copy to verify its content.

If a command is missing, identify the shell before looking for an equivalent. Never download a replacement executable merely to make a classroom command work. If permission is denied in the practice directory, inspect its location and ownership; do not grant everyone write access.

## Independent evidence

Write a five-step procedure that another learner can follow on your operating system, including the starting directory and expected listing. Identify which steps would need adaptation on another system. Submit commands as text, with account names redacted.

## Check your reasoning

A file manager reporting a full disk is evidence about storage, not proof that RAM is exhausted. A low free-memory reading alone is not proof of a fault because operating systems use memory for caching. Diagnose with several observations and the affected task.

## Worked example

A 4.7 GiB `.mkv` copied to a FAT32 camera card ends as a 0-byte or missing file. Reformat is the wrong first step. Copy to the NTFS staff volume, then to the patron exFAT share.
