# Week 6: ISR vs polling — realtime latency budget

**Ticket:** EP-4606  
**Lab:** `lab_ep_isr_vs_poll`

## Objectives
- Choose ISR when edge latency must stay under 250 µs
- Bound missed_edges
- Keep ISR work short — defer heavy work

## Body
Realtime is a budget, not a brand. If an edge must be seen within 250 µs, polling loops that sometimes run longer fail the budget — use ISR mode and keep the handler short. missed_edges must be 0 on the fixture acceptance window.

No-hardware fallback: reason from the latency table in the lab README.

## Worked example
mode=isr, max_latency_us=250, missed_edges=0

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming hard realtime certification
- No unbounded work inside ISR

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_isr_vs_poll` and `EP-4606`. Empty {} fails. A file whose body is only PASS raises.
