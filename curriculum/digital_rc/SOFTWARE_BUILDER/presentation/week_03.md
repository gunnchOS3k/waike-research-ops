# Week 3: Migrations that do not strand the Device Lab

## Slide 1 — Hook
Migrations that do not strand the Device Lab

## Slide 2 — Worked example
Forward adds returned_at TIMESTAMP NULL; schema_version=3; down drops returned_at only.

## Slide 3 — Lab contract
`lab_db_migration` rejects empty/wrong/print-PASS.

## Speaker notes
Stay in SOFTWARE_BUILDER vocabulary. Do not noun-swap another academy's deck.
Assignment: Write forward and down SQL for 0003; explain why DELETE FROM checkouts is forbidden....
