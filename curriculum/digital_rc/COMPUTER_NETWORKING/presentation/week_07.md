# Week 7 presentation — Four-router town — SPF beats the scenic route

## Slide 1 — Cold open
dijkstra(A)['D']=4 via B. Scenic A-C-D=10 loses. Install 10.20.40.0/24 nh=Yard.

## Slide 2 — Teaching beat
Routers A (Pier), B (Yard), C (Shed), D (Roof). Costs: A-B 2, B-D 2, A-C 5, C-D 5, B-C 9. Shortest A→D is A-B-D cost 4, not A-C-D cost 10. SPF is just Dijkstra on a weighted graph. OSPFv2 (RFC 2328) is the protocol that floods the graph; this lab computes the graph you already know.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
