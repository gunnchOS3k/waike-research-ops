# Week 3: Users, groups, and the sudo you can actually type

The kiosk account exists so a stranger can browse. It must not be in `sudo`. The desk lead account `desk.lead` is in `helpdesk` and may use sudo for printer cups and user unlocks, not for installing random `.exe` from a USB stick. Least privilege is a group membership you can print, not a vibe.

UIDs collide in the worst way: two names, one number, one home. The lab rejects duplicate UIDs and duplicate homes. If you clone an account by copying `/etc/passwd` lines and forget to change the UID, you have invented a ghost who owns the lead's files.

Windows analog: local users vs Microsoft accounts vs the kiosk local account that is not an administrator. Fast User Switching is how a volunteer leaves a session without killing the spooler. Logging off the last admin session while cups is printing 40 résumés is how Saturday starts with a fight.

Zero Trust shows up here as a support behavior, not a product: do not grant admin because someone is late. Grant the group that the ticket type requires, time-box it, and write the change.

## Learn the distinction

An account identifies an actor. Authentication checks a claimed identity; authorization determines which actions that actor may perform. Groups can simplify authorization, but a group name has meaning only in the system that interprets it. Administrative access increases the consequences of mistakes. A shared public session should not inherit a staff administrator's privileges.

## Guided practice: build an access table

Do this as a paper or text exercise unless you have an authorized disposable virtual machine. Define fictional accounts `patron`, `operator`, and `maintainer`; resources `public-docs`, `private-tickets`, and `system-settings`; actions read, write, and administer. Give each account only the actions needed for its role. For each allowed action, write a task that justifies it. For each denied action, write an expected denial.

Expected result: patron access supports public work without reading private tickets or administering the system. A maintainer can perform maintenance through an approved elevation mechanism rather than sharing a password. Test one allowed and one denied action in an authorized VM if available, then restore its snapshot. Do not modify real shared accounts.

## Independent evidence

Add a temporary volunteer role. Specify its expiry, the access removed at expiry, and how an administrator would verify removal. Submit the access table and test record. A correct table alone is a design artifact; a test record must say which environment actually enforced it.

## Check your reasoning

Being able to log in does not mean being authorized to read every file. Removing a visible shortcut does not revoke access. When a permission test unexpectedly succeeds, stop and investigate the effective permissions before using real information.

## Worked example

kiosk uid 1010, groups=[kiosk], sudo=false. desk.lead uid 1020, groups=[helpdesk, staff]. If kiosk also sits in sudo, the lab fails even if the password is long.
