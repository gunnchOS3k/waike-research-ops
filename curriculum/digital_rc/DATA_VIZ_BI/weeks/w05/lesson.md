# Week 5: Visualization principles — encode waits, don't decorate

Ticket CM-3519 grades a chart spec: mark=bar, x=zone, y=median_wait. A rainbow pie of ticket_ids fails encoding principles. You will validate channel types (nominal x, quantitative y) and refuse 3D extrusion as 'insight.'

Valid: bar + nominal zone + quantitative median_wait. Invalid: pie of unique ticket_ids.

Encoding beats decoration. bar + nominal zone + quantitative median_wait is valid; a rainbow pie of ticket_ids is invalid for this KPI. 3D extrusion is chartjunk, not insight.

Set invalid_rejected=true only after you can name the rejected mark. The lab checks the triple (mark,x,y) and the rejection flag together.

Studio vocabulary stays concrete: channel types, marks, and the question the chart answers. If the chart cannot survive a grayscale print for the board packet, redesign it.

Week 5 close for DATA_VIZ_BI: ticket work ends when the lab JSON fields for `lab_chart_encode` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

bar/zone/median_wait valid; pie(ticket_id) invalid encoding.
