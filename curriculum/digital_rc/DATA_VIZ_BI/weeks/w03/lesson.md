# Week 3: Relational modeling — stop repeating zone addresses

Ticket CM-3311 shows zone address repeated on every ticket row. That update anomaly means one rename edit misses 40 rows. You will propose a 3NF-ish split: tickets reference zone_id; zone_dim holds address. The lab checks that repeating groups are removed from the ticket table proposal.

Before: ticket rows carry zone_address text. After: zone_id FK only; address in zone_dim.

Repeating zone_address on every ticket is an update anomaly waiting for a rename. Move address into zone_dim; leave tickets with zone_id FK only. That is the 3NF-ish contract lab_schema_nf enforces.

Tell the anomaly story in one sentence: 'one rename missed forty ticket rows.' If your tables[] still list zone_address under tickets, the lab fails regardless of prose quality.

Normalization here is civic maintenance: fewer copy-paste address edits, fewer contradictory labels on the same zone letter across weeks of dashboards.

## Worked example

Move zone_address into zone_dim; tickets keep zone_id FK only.
