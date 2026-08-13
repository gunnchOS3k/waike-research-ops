# Week 5 presentation — Reliability on an unreliable wire — sequences, ACKs, AIMD on paper

## Slide 1 — Cold open
seq=1000 len=200 → ACK 1200 on full receipt. cwnd 10, loss → 5, then 6,7,8... on additive increase per RTT without further loss.

## Slide 2 — Teaching beat
TCP (current spec RFC 9293) pretends the wire is reliable by numbering bytes and refusing to live on hope. Sequence 1000, payload 200 bytes, ACK 1200 means 'I have everything before 1200.' If ACK 1000 returns, none of that payload is safe yet.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
