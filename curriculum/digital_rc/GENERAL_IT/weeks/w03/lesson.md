# Week 3: Users, groups, and the sudo you can actually type

The kiosk account exists so a stranger can browse. It must not be in `sudo`. The desk lead account `desk.lead` is in `helpdesk` and may use sudo for printer cups and user unlocks, not for installing random `.exe` from a USB stick. Least privilege is a group membership you can print, not a vibe.

UIDs collide in the worst way: two names, one number, one home. The lab rejects duplicate UIDs and duplicate homes. If you clone an account by copying `/etc/passwd` lines and forget to change the UID, you have invented a ghost who owns the lead's files.

Windows analog: local users vs Microsoft accounts vs the kiosk local account that is not an administrator. Fast User Switching is how a volunteer leaves a session without killing the spooler. Logging off the last admin session while cups is printing 40 résumés is how Saturday starts with a fight.

Zero Trust shows up here as a support behavior, not a product: do not grant admin because someone is late. Grant the group that the ticket type requires, time-box it, and write the change.

## Worked example

kiosk uid 1010, groups=[kiosk], sudo=false. desk.lead uid 1020, groups=[helpdesk, staff]. If kiosk also sits in sudo, the lab fails even if the password is long.
