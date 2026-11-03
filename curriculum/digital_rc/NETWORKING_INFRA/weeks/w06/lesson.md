# Week 6: CDN offload — the miss ratio is what the origin pays for

NIF-5606: a public broadcaster expects 12,000 requests per second for a live results page, each object about 150 kilobytes, and its origin servers sit behind a two-gigabit link. A content delivery network answers from edge caches when it can, and only the misses travel back to the origin. The origin's load scales with the miss ratio, one minus the hit ratio. At a 92 percent hit ratio, 8 percent of 12,000 is 960 requests per second, and 960 times 150,000 bytes times 8 bits is 1.152 gigabits per second, uncomfortably close to the two-gigabit link. Raising the hit ratio to 96 percent halves the misses to 480 requests per second and 0.576 Gbit/s. Four points of hit ratio halved the origin's work, which is why cache keys, longer TTLs for static images, and stripping needless query strings matter. The edge still delivers all 14.4 Gbit/s to viewers, so the CDN contract must cover that. Multiplying by the hit ratio instead of the miss ratio gives a number that looks impressive and is wrong.

## Worked example

12,000 rps × 150 KB: hit 0.92 → 960 rps, 1.152 Gbit/s at origin; hit 0.96 → 480 rps, 0.576 Gbit/s; edge serves 14.4 Gbit/s total
