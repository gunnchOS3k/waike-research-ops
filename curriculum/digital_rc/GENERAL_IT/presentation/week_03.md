# Week 3 presentation — Users, groups, and the sudo you can actually type

## Slide 1 — Cold open
kiosk uid 1010, groups=[kiosk], sudo=false. desk.lead uid 1020, groups=[helpdesk, staff]. If kiosk also sits in sudo, the lab fails even if the password is long.

## Slide 2 — Teaching beat
The kiosk account exists so a stranger can browse. It must not be in `sudo`. The desk lead account `desk.lead` is in `helpdesk` and may use sudo for printer cups and user unlocks, not for installing random `.exe` from a USB stick. Least privilege is a group membership you can print, not a vibe.

## Slide 3 — Live work
Put 1200 seconds, 15% free, and CHG window 18:00–21:00 on the board. Sit in silence until someone does the arithmetic.

## Speaker notes
If they ask for A+ dumps, close the slide and open the alignment JSON. Keys never leave the instructor packet.
