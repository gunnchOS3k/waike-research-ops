# Week 2: SQL joins — tickets to zones without cartesian accidents

Ticket CM-3208 needs a join from tickets to zone_dim on zone_id. A missing ON clause explodes to a cartesian product and invents thousands of waits. You will count joined rows on the fixture and show that unmatched tickets are left out of the inner join used for the median KPI.

tickets=100, zones=5, matching=95 → inner join rows=95. Cartesian would be 500.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

inner join matching 95; cartesian 100×5=500 is the accident to refuse.
