# Week 3 presentation — Users, groups, and the sudo you can actually type

## Slide 1 — Cold open
kiosk uid 1010, groups=[kiosk], sudo=false. desk.lead uid 1020, groups=[helpdesk, staff]. If kiosk also sits in sudo, the lab fails even if the password is long.

## Slide 2 — Teaching beat
The kiosk account exists so a stranger can browse. It must not be in `sudo`. The desk lead account `desk.lead` is in `helpdesk` and may use sudo for printer cups and user unlocks, not for installing random `.exe` from a USB stick. Least privilege is a group membership you can print, not a vibe.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
