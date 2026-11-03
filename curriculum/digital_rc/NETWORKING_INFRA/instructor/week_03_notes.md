# NETWORKING_INFRA — NOC mentor notes, week 3

**Board work:** 1 Gbit/s × 0.080 s / 8 = 10,000,000 B BDP; 65,535-byte window × 8 / 0.080 s = 6.55 Mbit/s; window scale shift 8 (65,535 × 256 ≥ 10 MB)

**Whiteboard:** ask one trainee to derive lab_nif_bdp_window from its inputs before checking.

**Watch for:** Leaving RTT in milliseconds or the rate in bits when computing BDP bytes.
