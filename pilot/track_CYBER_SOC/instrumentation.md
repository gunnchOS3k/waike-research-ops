# Instrumentation — CYBER_SOC

## What to capture (design)

| Signal | Source | PII rule |
|--------|--------|---------|
| Session attendance | roster code only | no real names in shared artifacts |
| Lab submit accept/reject | lab runner exit codes | strip emails |
| Time-on-task (optional) | facilitator tally | aggregate only |
| Issue tags | issue_logging.md | no secrets |

## Schema pointer

See `pilot/PILOT_DATA_SCHEMA.md` (repo-level). Pilot track folder does not claim collected data exists.
