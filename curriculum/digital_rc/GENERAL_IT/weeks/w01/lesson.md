# Week 1: The Civic Tech Desk — three jobs a computer actually has

At the Gary Civic Tech Desk the machine in front of a patron is not a personality. It remembers (files), it calculates (apps), and it talks (network). Beginners freeze when a window disappears because they cannot name which of those three jobs failed. Ticket 4417 from the library kiosk is a remember-job failure: the essay lived in a browser temp store and the idle timer (1200 seconds) wiped the session. Naming the job changes the next action. You do not 'fix the Internet' for a missing file.

Operator confidence is a spoken path. Say `Documents/waike/desk/4417` out loud before you copy anything. If that folder is missing, create it. Extra folders on the Desktop are clutter, not success. The lab marks required paths; it does not grade wallpaper.

Privacy is operational, not a poster. The desk forbids storing SSNs, library-card PANs, or passwords in ticket notes. If a patron dictates a password, you write 'credential reset requested' and walk them through a reset — you never type their secret into chat.

This week you will also meet the WAIKE Consensus Ladder in miniature: what you saw, what you inferred, what you still need. 'The kiosk is broken' is not an observation. 'Idle logout at 1200s discarded an unsaved textarea' is.

## Worked example

Idle policy 1200s = 20 minutes. Patron sat down at 14:02, last keystroke 14:07, return 14:28. Session is gone. Restore from the auto-save folder if present; do not disable the timer as your first move — the timer is a shared-kiosk control.
