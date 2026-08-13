# Week 4: Frontend contract — accessible checkout board

The ForgeDesk board is a single HTML page with a table of checkouts. Accessibility is not a slide. Every overdue signal needs text marker OVERDUE, not color alone. The filter must be a button named Filter overdue. API failures render in a role=alert region.

The lab parses a DOM-like JSON tree. Broken API JSON must not fail silently. This is original WAIKE UI work, not a CS50 project port.

AI mode COMPARE_APPROACHES allowed when weighing table vs card layouts; disclose the comparison in the assignment footer.

Every overdue row shows a text marker OVERDUE, not color alone. The filter control is a button named exactly Filter overdue. API failures render inside a role=alert region; broken JSON must not blank the board. The lab parses a DOM-like JSON tree and checks those contracts. COMPARE_APPROACHES is allowed when weighing table versus card layouts if you disclose the comparison in the assignment footer. This is original ForgeDesk UI work, not a port of any CS50 frontend project.

## Worked example

Tree includes button Filter overdue, table, OVERDUE text for ring-7, and role=alert.
