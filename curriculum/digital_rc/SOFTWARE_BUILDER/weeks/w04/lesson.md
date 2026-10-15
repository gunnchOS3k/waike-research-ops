# Week 4: Frontend contract — accessible checkout board

The ForgeDesk board is a single HTML page with a table of checkouts. Accessibility is not a slide. Every overdue signal needs text marker OVERDUE, not color alone. The filter must be a button named Filter overdue. API failures render in a role=alert region.

The lab parses a DOM-like JSON tree. Broken API JSON must not fail silently. This is original WAIKE UI work, not a CS50 project port.

AI mode COMPARE_APPROACHES allowed when weighing table vs card layouts; disclose the comparison in the assignment footer.

Every overdue row shows a text marker OVERDUE, not color alone. The filter control is a button named exactly Filter overdue. API failures render inside a role=alert region; broken JSON must not blank the board. The lab parses a DOM-like JSON tree and checks those contracts. COMPARE_APPROACHES is allowed when weighing table versus card layouts if you disclose the comparison in the assignment footer. This is original ForgeDesk UI work, not a port of any CS50 frontend project.

## Concept and boundary

An interface has a visual presentation and an interaction contract. Labels connect controls to their purpose. Keyboard focus identifies the active control. Color alone should not carry the only explanation of an error or status. A button click is not proof that the server accepted a mutation.

## Guided implementation

Sketch an accessible checkout form with an item label, submit button, pending state, success state and error state. Write text for a 403 denial and a 409 state conflict. Expected result: the user can distinguish missing permission from an already checked-out item without relying on color. If you implement it, test the entire path using only the keyboard and preserve focus after validation failure.

## Independent evidence and recovery

Create a test plan covering a duplicate submission, a network failure and a long item name. For each, state the expected visible feedback and whether the original input is retained. Record actual observations separately from planned outcomes.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

Tree includes button Filter overdue, table, OVERDUE text for ring-7, and role=alert.
