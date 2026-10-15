# Week 7: Four-router town — SPF beats the scenic route

Routers A (Pier), B (Yard), C (Shed), D (Roof). Costs: A-B 2, B-D 2, A-C 5, C-D 5, B-C 9. Shortest A→D is A-B-D cost 4, not A-C-D cost 10. SPF is just Dijkstra on a weighted graph. OSPFv2 (RFC 2328) is the protocol that floods the graph; this lab computes the graph you already know.

A routing table is not a suggestion. If Roof's LAN is 10.20.40.0/24, Pier installs that prefix via Yard. Administrative distance is a CCNA word for 'who do I trust when two protocols argue.' Static vs OSPF is enough for this course.

First-hop redundancy is postponed to a paragraph: two gateways, one VIP, so a brick dying does not isolate the kiosk VLAN. We do not implement VRRP here.

You will trace one packet from Pier to Roof using last week's datapath plus this week's route. That is IP connectivity as a story, not a memorized command list.

## Concept and scope

A routing algorithm computes paths from a model of topology and costs. Dijkstra's algorithm assumes nonnegative edge weights. A shortest modeled path need not be the fastest measured path if configured costs do not represent measured latency.

## Guided practice

Use edges A–B cost 2, B–D cost 2, A–C cost 5 and C–D cost 5. Compare A–B–D cost 4 with A–C–D cost 10. Expected result: the first is cheaper under these configured costs. Remove B–D and recompute rather than continuing to report the old answer.

## Independent evidence

Add another route with an equal total cost. Document how your chosen model resolves ties. Explain why this calculation does not demonstrate OSPF packet exchange, a vendor implementation or real failover time.

## Worked example

dijkstra(A)['D']=4 via B. Scenic A-C-D=10 loses. Install 10.20.40.0/24 nh=Yard.
