# Week 4: SIEM triage — bursts are a look, not a conviction

AUTH_FAIL lines for ada four times from 10.20.30.5 cross the threshold of 3. cal fails once. bea succeeds. Your note says 'burst on ada,' not 'ada is the attacker.' Bursts are a look. Conviction needs more.

Alert fatigue is how SOCs die. A bot may cluster bursts. A human still owns the close. That is the 2026 ops guidance in our own words.

Logs must not contain passwords. If a fixture line has `password=`, the lab author failed — and you will file a bug, not reuse it.

Security+ operations domain is the alignment label: alerting and monitoring as verbs. Harbor's shift handoff is a six-line paste: burst users, threshold, window, what you looked at, what you did not conclude, and who owns the next look. A handoff that says 'ada weird' is how Sunday starts from zero. Thresholds are policy, not vibes.

## Worked example

counts ada=4, cal=1, threshold=3 → bursts=['ada']. Note: burst, not attacker.
