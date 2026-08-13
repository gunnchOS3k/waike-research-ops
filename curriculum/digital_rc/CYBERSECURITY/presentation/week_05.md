# Week 5 presentation — Hardening the image — guest off, keys on, bot sudo off

## Slide 1 — Cold open
All six baseline flags must match. Mutating ai_agent_sudo true fails the lab.

## Slide 2 — Teaching beat
The Harbor workstation image: guest_login false, ssh_password_auth false, unattended_upgrades true, open_ports {22,443}, world_writable_home false, ai_agent_sudo false. That last flag is the 2026 identity lesson bolted onto a baseline that would otherwise look like 2014 CIS.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
