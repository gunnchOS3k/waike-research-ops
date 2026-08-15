# Week 5: Visualization principles — encode waits, don't decorate

Ticket CM-3519 grades a chart spec: mark=bar, x=zone, y=median_wait. A rainbow pie of ticket_ids fails encoding principles. You will validate channel types (nominal x, quantitative y) and refuse 3D extrusion as 'insight.'

Valid: bar + nominal zone + quantitative median_wait. Invalid: pie of unique ticket_ids.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

bar/zone/median_wait valid; pie(ticket_id) invalid encoding.
