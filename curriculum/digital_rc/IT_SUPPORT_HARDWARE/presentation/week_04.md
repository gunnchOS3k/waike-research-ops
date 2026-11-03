# Refurb Bench 4: MBR or GPT — the two-terabyte ceiling and UEFI boot

On the board: MBR limit = 2^32 × 512 B = 2,199,023,255,552 B (2 TiB); 4 TB disk > limit → GPT, boot with UEFI; 4096-byte sectors raise the MBR limit to 16 TiB
