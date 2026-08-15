# Week 9: Quantization + edge budget — int8 vs desk latency

Edge AI is a budget. Ticket EF-2915 compares fp32 weights (4 bytes × 1_000 params) vs int8 (1 byte × 1_000) and a latency SLA of ≤15 ms on the USB accelerator profile. Quantization is not free accuracy; you will record expected size ratio and whether the profiled latency_ms meets SLA.

PHYSICAL_PENDING: actual Coral flash remains pending until digital budgets PASS.

fp32_bytes=4000, int8_bytes=1000, ratio=0.25. latency_ms=12 ≤15 → budget_ok true.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

1000 params: fp32=4000B int8=1000B ratio=0.25; latency 12ms ≤15 → ok.
