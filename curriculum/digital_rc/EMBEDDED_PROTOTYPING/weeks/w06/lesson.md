# Week 6: ISR vs polling — realtime latency budget

**Ticket:** EP-4606  
**Lab:** `lab_ep_isr_vs_poll`

## Objectives
- Choose ISR when edge latency must stay under 250 µs
- Bound missed_edges
- Keep ISR work short — defer heavy work

## Body
Realtime is a budget. If an edge must be observed within 250 µs, a polling loop that sometimes runs longer fails — choose mode=isr, keep the handler short, and defer heavy work. missed_edges must be 0 on the acceptance window.

Connectivity note: ISR latency budgets matter for button/wake paths that later feed Device OS guest boot_status. No hard-realtime certification is granted.
## Worked example
mode=isr, max_latency_us=250, missed_edges=0

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming hard realtime certification
- No unbounded work inside ISR

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_isr_vs_poll` and `EP-4606`. Empty {} fails. A file whose body is only PASS raises.
