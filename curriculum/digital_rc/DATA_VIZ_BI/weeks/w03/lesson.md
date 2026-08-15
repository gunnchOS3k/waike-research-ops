# Week 3: Relational modeling — stop repeating zone addresses

Ticket CM-3311 shows zone address repeated on every ticket row. That update anomaly means one rename edit misses 40 rows. You will propose a 3NF-ish split: tickets reference zone_id; zone_dim holds address. The lab checks that repeating groups are removed from the ticket table proposal.

Before: ticket rows carry zone_address text. After: zone_id FK only; address in zone_dim.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

Move zone_address into zone_dim; tickets keep zone_id FK only.
