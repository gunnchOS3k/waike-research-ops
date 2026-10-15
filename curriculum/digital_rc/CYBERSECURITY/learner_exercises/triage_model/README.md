# Fictional SOC triage model

Requirements: Python 3.11+. Save `triage.py` and `test_triage.py` in an empty folder and run `python3 -m unittest -v test_triage.py` (or `py -3 -m unittest -v test_triage.py` with the Windows Python launcher). Expected result: seven tests pass. No packages, network access or administrative rights are needed.

Inspect each test before execution. The model accepts fictional dictionaries; it does not authenticate analysts, read system logs, detect real intrusions or perform containment. Its authorization function illustrates a policy decision only. No account permissions are changed.

The failed-login rule flags at least three failures for investigation. It does not establish malicious intent. Two failures produce no flag in this rule, but that does not establish safety. Change the threshold and explain how alert count changes without claiming measured sensitivity or specificity. Those metrics require labeled evidence and a defined dataset.

Create your own four fictional events in two explicit timezones. Predict the order after conversion to UTC, then test it. A timestamp without timezone is rejected rather than silently assumed local. Chronological order does not prove causation, and clock synchronization uncertainty still matters.

Independent work: test failures split across two actors, an invalid threshold, and events with identical timestamps. Document the behavior you observed and one limitation. Then create a containment proposal describing scope, permission, preservation and rollback; do not execute it on a real device. Instructor review of that reasoning remains required.

Use no real passwords, identifiers or security telemetry. AI assistance contributed to code, tests and instruction. Human technical and educational acceptance remains pending.
