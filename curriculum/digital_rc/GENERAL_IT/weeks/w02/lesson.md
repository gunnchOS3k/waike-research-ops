# Week 2: Two operating systems, one pair of hands

The Civic Tech Desk dual-boots a Windows 11 image for walk-up patrons and a Debian bookworm image for staff recovery. You will not memorize every click. You will learn the same three verbs on both: list, copy, and permission. On Windows those verbs are Explorer, `robocopy` or copy, and icacls. On Debian they are `ls`, `cp`, and `chmod`/`chown`.

File systems are not fashion. The staff recovery stick is ext4. The patron share that must be read by Windows is exFAT. NTFS is fine for the internal Windows volume. FAT32 has a maximum individual file size of 4 GiB minus 1 byte. A 4.7 GiB file exceeds that limit. Inspect the actual filesystem and copy error rather than assuming that every camera card uses FAT32.

Task Manager and a process monitor such as `top` can provide CPU and memory observations. Storage activity may require additional views or tools. A high disk-active-time reading with low CPU use suggests a storage-related bottleneck, but it does not establish a root cause or rule out malware. Capture relevant observations before restarting, because some live context will be lost.

Updates are operational procedures. In this fictional desk, maintenance windows are scheduled and recovery is prepared first. A dual-boot machine normally runs one installed operating system at a time; this lesson does not establish a special simultaneous-update mechanism or a general claim that updates confuse GRUB. Check the actual boot, encryption and update configuration before planning maintenance.

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

A 4.7 GiB file exceeds FAT32's individual-file limit. The copy should report failure; exact partial-file behavior depends on the tool. Preserve the original, verify the destination filesystem, and choose authorized compatible storage. Reformatting would erase existing destination data and is not the first diagnostic step.
