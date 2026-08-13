# Week 9: Automation without heroics — snapshot, change window, rollback

CHG-88 moves the idle policy. Planned time 19:15 local. Window 18:00–21:00. Snapshot homes first, apply policy, verify kiosk login. Rollback is restore_snapshot_home. If you apply first and snapshot later, you have a souvenir, not a rollback.

Cron is a clock, not a personality. The desk runs `0 21 * * 3` for Windows patch download (Wednesday 21:00) and refuses to schedule image writes during public hours 10:00–17:00. Automation that fires at 11:00 on a Saturday is an incident.

Scripts in this course print what they would do, then do it only with `--apply`. Dry-run is how volunteers learn. The lab compares executed steps to planned steps; drift fails.

AI tools may draft a runbook. They may not be granted sudo. If a chatbot invents a command you cannot explain, it does not go on the kiosk. That is operational procedure and, later, a cybersecurity identity rule — here it is just not being a daredevil.

## Worked example

Window 18:00–21:00, planned 19:15 → in window. Steps [snapshot_home, apply_idle_policy, verify_kiosk_login]. Rollback named.
