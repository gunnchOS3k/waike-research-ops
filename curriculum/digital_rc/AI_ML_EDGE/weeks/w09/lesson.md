# Week 9: Quantization + edge budget — int8 vs desk latency

Edge AI is a budget. Ticket EF-2915 compares fp32 weights (4 bytes × 1_000 params) vs int8 (1 byte × 1_000) and a latency SLA of ≤15 ms on the USB accelerator profile. Quantization is not free accuracy; you will record expected size ratio and whether the profiled latency_ms meets SLA.

PHYSICAL_PENDING: actual Coral flash remains pending until digital budgets PASS.

fp32_bytes=4000, int8_bytes=1000, ratio=0.25. latency_ms=12 ≤15 → budget_ok true.

Quantization is a budget conversation: 1000 params → 4000 fp32 bytes vs 1000 int8 bytes (ratio 0.25) and latency_ms against a 15 ms SLA. Measure, do not assume accuracy survives.

PHYSICAL_PENDING stays on the Coral flash until digital budgets PASS. Claiming DONE without the latency and size fields is a portfolio lie.

If latency_ms=18 against SLA 15, budget_ok is false even when the size ratio looks heroic. Write the inequality in the journal. Edge AI that misses the desk SLA is a research toy, not a civic deploy.

## Worked example

1000 params: fp32=4000B int8=1000B ratio=0.25; latency 12ms ≤15 → ok.
