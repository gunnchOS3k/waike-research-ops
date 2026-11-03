# Week 3: Bandwidth-delay product — why one connection cannot fill the pipe

NIF-5303: a research group pays for a one-gigabit link to a partner 80 milliseconds away and complains that a single file transfer crawls at a few megabits. TCP may only have one window of unacknowledged bytes in flight, then must wait for acknowledgements to return. The bandwidth-delay product says how many bytes the pipe holds: one gigabit per second times 0.08 seconds is 80 million bits, or 10,000,000 bytes. The original TCP header allows a window of at most 65,535 bytes, so the sender stalls after 64 KiB each round trip; throughput is window times eight divided by the round-trip time, about 6.55 Mbit/s here, less than one percent of the link. RFC 7323 window scaling shifts the advertised window left by a negotiated count; a shift of 8 multiplies 65,535 by 256 to about 16.8 MB, enough to cover the 10 MB product. The fix is end-host tuning and checking that no middlebox strips the option, not buying a bigger link.

## Worked example

1 Gbit/s × 0.080 s / 8 = 10,000,000 B BDP; 65,535-byte window × 8 / 0.080 s = 6.55 Mbit/s; window scale shift 8 (65,535 × 256 ≥ 10 MB)
