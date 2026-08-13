# Week 3: Migrations that do not strand the Device Lab

Checkout rows live in SQLite for local Device Lab and Postgres in staging. Week 3 is migration discipline. Migration 0003_add_returned_at must add a nullable timestamp, bump schema_version to 3, and leave a down migration that drops the column without deleting checkout history.

A migration that hard-codes production passwords fails. A migration that DELETE FROM checkouts to make room fails. CS50 Web SQL/models week is a domain label only. Fixture SQL is original WAIKE wording for ForgeDesk.

Assessment mode AI_RESTRICTED for the SQL artifact: you may use EXPLAIN orally with an instructor, but the submitted forward/down SQL must be authored without generative paste.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

## Worked example

Forward adds returned_at TIMESTAMP NULL; schema_version=3; down drops returned_at only.
