# Week 9: Automation without heroics — snapshot, change window, rollback

CHG-88 moves the idle policy. Planned time 19:15 local. Window 18:00–21:00. Snapshot homes first, apply policy, verify kiosk login. Rollback is restore_snapshot_home. If you apply first and snapshot later, you have a souvenir, not a rollback.

Cron is a clock, not a personality. The desk runs `0 21 * * 3` for Windows patch download (Wednesday 21:00) and refuses to schedule image writes during public hours 10:00–17:00. Automation that fires at 11:00 on a Saturday is an incident.

Scripts in this course print what they would do, then do it only with `--apply`. Dry-run is how volunteers learn. The lab compares executed steps to planned steps; drift fails.

AI tools may draft a runbook. They may not be granted sudo. If a chatbot invents a command you cannot explain, it does not go on the kiosk. That is operational procedure and, later, a cybersecurity identity rule — here it is just not being a daredevil.

## Learn the distinction

Automation repeats instructions; it does not decide whether their assumptions remain valid. A change window limits when work is authorized. A dry run describes intended actions without applying them, but its reliability depends on the script's implementation. Rollback is a tested recovery method with a known starting state, not merely a command name.

## Guided practice: simulate a change

Write a plain-text runbook for the fictional CHG-88 window, 18:00–21:00 local. Record the timezone, proposed start at 19:15, original policy value and desired value. Order the steps: capture recoverable state; apply one change; verify a new kiosk session; roll back if verification fails; record the outcome.

Rehearse on paper with a failure at verification. Expected result: the procedure restores the recorded original value and tests the recovered state. A snapshot captured after the change cannot establish that original state. If rollback has not been tested, record that gap and do not apply to a real kiosk.

## Independent evidence

Create a second case with a start at 21:10. Explain why the same technically correct procedure must wait for a newly authorized window. Include a stop rule for missing backups, unavailable reviewer or unexpected output. Submit the runbook and both simulated traces.

## Check your reasoning

Scheduling syntax depends on the scheduler and its timezone configuration. The five-field cron fixture `0 21 * * 3` requests Wednesday at 21:00 under the configured timezone. It is not a Windows Task Scheduler instruction. Review commands from AI assistance before running them.

## Worked example

Window 18:00–21:00, planned 19:15 → in window. Steps [snapshot_home, apply_idle_policy, verify_kiosk_login]. Rollback named.
