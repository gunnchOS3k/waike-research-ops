# Week 8 presentation — Authorized toy parser — detect the length lie, do not grow an exploit kit

## Slide 1 — Cold open
unsafe(\x14short) returns a short slice (the lie). safe(\x14short) raises ValueError. safe(\x04abcd)==b'abcd'.

## Slide 2 — Teaching beat
Berkeley CS161 uses authorized vulnerable targets in a course VM. We take the depth pattern, not the projects. Harbor's course CTF is a length-prefixed toy parser: first byte claims payload length. The unsafe parser trusts it. A message `\x14short` claims 20 bytes and only has 5. The safe parser raises.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
