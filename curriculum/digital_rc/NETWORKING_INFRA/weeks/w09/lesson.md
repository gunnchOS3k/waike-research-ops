# Week 9: 95th-percentile billing — the bursts you do not pay for

NIF-5909, the second NO_AI week, is a disputed transit invoice. Many internet transit contracts bill on the 95th percentile: the provider records average throughput every five minutes, sorts the month's samples, throws away the top five percent, and bills the highest remaining sample. The course fixture has twenty samples between 289 and 905 Mbit/s. With twenty samples, five percent is one, so the bill uses the sample at sorted index ceil(0.95 × 20) − 1, which is index 18 counting from zero. Sorted, that is 720 Mbit/s, while the 905 Mbit/s burst at the top is discarded. At $0.35 per Mbit/s the charge is $252. Billing the peak would charge $316.75, and billing the mean would undercount the busy hours. A real month has about 8,640 samples, so roughly 432 five-minute periods, about 36 hours, can burst without raising the bill. Know where your provider samples, whether inbound and outbound are compared, and check their arithmetic before paying.

## Worked example

20 five-minute samples sorted; index ceil(0.95 × 20) − 1 = 18 → 720 Mbit/s × $0.35 = $252; the single 905 Mbit/s burst is free
