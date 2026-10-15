# Week 4: SIEM triage — bursts are a look, not a conviction

AUTH_FAIL lines for ada four times from 10.20.30.5 cross the threshold of 3. cal fails once. bea succeeds. Your note says 'burst on ada,' not 'ada is the attacker.' Bursts are a look. Conviction needs more.

Alert fatigue is how SOCs die. A bot may cluster bursts. A human still owns the close. That is the 2026 ops guidance in our own words.

Logs must not contain passwords. If a fixture line has `password=`, the lab author failed — and you will file a bug, not reuse it.

Security+ operations domain is the alignment label: alerting and monitoring as verbs. Harbor's shift handoff is a six-line paste: burst users, threshold, window, what you looked at, what you did not conclude, and who owns the next look. A handoff that says 'ada weird' is how Sunday starts from zero. Thresholds are policy, not vibes.

## Concept and scope

An alert rule identifies conditions for investigation. A threshold crossing is evidence that the rule matched, not a verdict about intent. Sensitivity and false-positive rates require defined labels and representative evaluation data; a fictional event count cannot establish them.

## Guided practice

Run the local triage function with three failed events for actor-a. Expected result: an investigate disposition with count 3. Repeat with two events, then split three events across two aliases. Explain the difference between no flag from this rule and evidence of safety. No real login attempts occur.

## Independent evidence

Change the threshold and record the changed number of flags. Propose additional context needed before escalation, including legitimate user error and service faults. Do not tune a threshold and report improved detection without labeled evaluation evidence.

## Worked example

counts ada=4, cal=1, threshold=3 → bursts=['ada']. Note: burst, not attacker.
