# Week 4: MBR or GPT — the two-terabyte ceiling and UEFI boot

ISH-4404 is a new 4 TB data disk that shows only about 2 TB of usable space after the last technician set it up. A disk's partition table records where each partition starts and ends. The older Master Boot Record format stores those positions as 32-bit sector numbers, so it can address at most 2^32 sectors. With the common 512-byte sectors that is 2,199,023,255,552 bytes, two tebibytes, and anything beyond is simply unreachable. The GUID Partition Table uses 64-bit addresses, supports far larger disks, keeps a backup copy of the table at the end of the disk, and allows many more partitions. A 4,000,000,000,000-byte disk is larger than the MBR ceiling, so it must be GPT. Disks with 4,096-byte native sectors stretch MBR to 16 TiB, but they are not what the bench usually sees. To boot an operating system from a GPT disk, the PC's firmware needs to run in UEFI mode rather than legacy BIOS mode, a setting in the firmware setup screen. Converting the scheme erases the table, so copy the data off and confirm the backup before you touch it.

## Worked example

MBR limit = 2^32 × 512 B = 2,199,023,255,552 B (2 TiB); 4 TB disk > limit → GPT, boot with UEFI; 4096-byte sectors raise the MBR limit to 16 TiB
