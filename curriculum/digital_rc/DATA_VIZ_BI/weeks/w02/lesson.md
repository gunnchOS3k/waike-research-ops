# Week 2: SQL joins — tickets to zones without cartesian accidents

Ticket CM-3208 needs a join from tickets to zone_dim on zone_id. A missing ON clause explodes to a cartesian product and invents thousands of waits. You will count joined rows on the fixture and show that unmatched tickets are left out of the inner join used for the median KPI.

tickets=100, zones=5, matching=95 → inner join rows=95. Cartesian would be 500.

Joins need ON clauses the way tickets need zone_id. 100×5 without a match key is a 500-row cartesian accident that fabricates waits. Inner join on the fixture yields 95 matched rows for the median KPI — unmatched tickets stay out.

Write cartesian_trap_rows beside joined_rows so a reviewer sees you know the failure mode. SQL comments that only say 'joined stuff' fail the assignment even if the count is lucky.

Do not run DROP or mutate a live campus warehouse. Fixture counts only. The Studio desk is authorized for the course tables in this repository — nothing else.

## Worked example

inner join matching 95; cartesian 100×5=500 is the accident to refuse.
