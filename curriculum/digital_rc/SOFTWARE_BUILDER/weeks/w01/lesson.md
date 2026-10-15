# Week 1: ForgeDesk ticket 8801 — git conflict on the deploy branch

The WAIKE Software ForgeDesk is a two-person civic issue tracker for Device Lab checkouts. Ticket 8801 opens when a volunteer edits routes.py on feature/kiosk-hours while the desk lead edited the same function on main. A conflict is not a personality crisis. It is two hashes that claim the same lines. You will read both sides, keep the authz guard that main added, and keep the hours table that the feature branch added.

Branch names in this course are contracts. main is always deployable to the local Device Lab compose stack. Feature branches must merge with an explicit conflict report JSON that names the surviving function signature. The lab rejects a resolution that drops require_role or that keeps both copies as _v1 and _v2 without a test.

CS50 Web Git week is a structure citation only. Harvard lab text stays at Harvard. WAIKE conflict fixture is original: two parents, one file, one required survivor set. Publicly viewable is not free to copy. AI mode for practice drills: PRACTICE; for the graded conflict report: AI_DISCLOSED if you used HINT.

## Concept and boundary

Version control records changes, not correctness. A commit identifies a project state; a branch names a movable line of development. A merge conflict means Git could not choose an edit automatically. Deleting conflict markers without understanding both changes can silently discard behavior.

## Guided implementation

Create a new local practice repository containing a two-line runbook. Commit it. Make two branches that edit the same line differently, commit on each, then merge one into the other. Expected result: Git identifies the conflicting path. Read both edits, write a combined version that preserves the intended requirements, stage it, and commit. Confirm with `git status` and inspect the final file. If you cannot explain the conflict, stop; preserve both branches instead of resetting away their work.

## Independent evidence and recovery

Document both original requirements, the final decision and a test that would detect a lost requirement. Repeat with edits to separate lines and explain why a conflict may not occur. Use only a disposable local repository; do not practice force-pushing on a shared branch.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

Parents A and B both touch def open_hours. A adds require_role('desk'). B adds HOURS={...}. Survivor must include both tokens.
