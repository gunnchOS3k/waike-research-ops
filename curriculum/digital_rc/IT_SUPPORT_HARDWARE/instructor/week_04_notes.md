# IT_SUPPORT_HARDWARE — Bench-lead notes, week 4

**Board work:** MBR limit = 2^32 × 512 B = 2,199,023,255,552 B (2 TiB); 4 TB disk > limit → GPT, boot with UEFI; 4096-byte sectors raise the MBR limit to 16 TiB

**Hands on the case:** have each technician run lab_ish_partition_scheme against the machine on their bench.

**Watch for:** Converting MBR to GPT before the data is copied off.
