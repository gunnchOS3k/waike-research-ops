# Week 1: The Civic Tech Desk — three jobs a computer actually has

At the Gary Civic Tech Desk the machine in front of a patron is not a personality. It remembers (files), it calculates (apps), and it talks (network). Beginners freeze when a window disappears because they cannot name which of those three jobs failed. Ticket 4417 from the library kiosk is a remember-job failure: the essay lived in a browser temp store and the idle timer (1200 seconds) wiped the session. Naming the job changes the next action. You do not 'fix the Internet' for a missing file.

Operator confidence is a spoken path. Say `Documents/waike/desk/4417` out loud before you copy anything. If that folder is missing, create it. Extra folders on the Desktop are clutter, not success. The lab marks required paths; it does not grade wallpaper.

Privacy is operational, not a poster. The desk forbids storing SSNs, library-card PANs, or passwords in ticket notes. If a patron dictates a password, you write 'credential reset requested' and walk them through a reset — you never type their secret into chat.

This week you will also meet the WAIKE Consensus Ladder in miniature: what you saw, what you inferred, what you still need. 'The kiosk is broken' is not an observation. 'Idle logout at 1200s discarded an unsaved textarea' is.

## Learn the distinction

An application holds working state in memory. A saved file is data written to storage at a named location. A network service may keep another copy, but that depends on the application's behavior. A disappearing browser window does not prove that the network failed or that all copies were erased. The kiosk story is a configured teaching fixture, not a claim that every browser deletes drafts after 20 minutes.

## Guided practice: make a recoverable file

1. In a folder you own, create `waike-practice/4417`. Use only fictional text.
2. Open a text editor, enter `Practice draft, version 1`, and save it as `essay.txt` in that folder.
3. Close the editor, reopen the file from its folder, and compare the text. Expected result: the saved text survives closing the application.
4. Make a second copy named `essay-recovery.txt`. Change the original to version 2. Reopen both and explain why they now differ.
5. Record the path, the two observed contents, and the recovery action. If you cannot find the file, search your chosen folder before creating another copy. Do not change a shared kiosk policy.

## Independent evidence

Create a third fictional ticket for a missing print job. Separate an observation, an inference, and one safe next test. Submit the folder listing and a redacted journal, not a screenshot containing an account name. A reviewer should be able to locate and reopen your recovery copy without asking you where it is.

## Check your reasoning

Does closing an editor guarantee that unsaved changes were written? No: save behavior depends on the application. Does a second filename on the same disk protect against losing the disk? No. It is a recovery exercise, not a complete backup strategy.

## Worked example

Idle policy 1200s = 20 minutes. Patron sat down at 14:02, last keystroke 14:07, return 14:28. Session is gone. Restore from the auto-save folder if present; do not disable the timer as your first move — the timer is a shared-kiosk control.
