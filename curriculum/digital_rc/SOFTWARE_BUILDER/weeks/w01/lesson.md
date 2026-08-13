# Week 1: ForgeDesk ticket 8801 — git conflict on the deploy branch

The WAIKE Software ForgeDesk is a two-person civic issue tracker for Device Lab checkouts. Ticket 8801 opens when a volunteer edits routes.py on feature/kiosk-hours while the desk lead edited the same function on main. A conflict is not a personality crisis. It is two hashes that claim the same lines. You will read both sides, keep the authz guard that main added, and keep the hours table that the feature branch added.

Branch names in this course are contracts. main is always deployable to the local Device Lab compose stack. Feature branches must merge with an explicit conflict report JSON that names the surviving function signature. The lab rejects a resolution that drops require_role or that keeps both copies as _v1 and _v2 without a test.

CS50 Web Git week is a structure citation only. Harvard lab text stays at Harvard. WAIKE conflict fixture is original: two parents, one file, one required survivor set. Publicly viewable is not free to copy. AI mode for practice drills: PRACTICE; for the graded conflict report: AI_DISCLOSED if you used HINT.

## Worked example

Parents A and B both touch def open_hours. A adds require_role('desk'). B adds HOURS={...}. Survivor must include both tokens.
