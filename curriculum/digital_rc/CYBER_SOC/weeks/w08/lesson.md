# Week 8: Triage queue — severity meets asset criticality

SOC-2808 hands you six open alerts at once and one pair of hands. Severity alone is a poor sort key, because a critical alert on a lobby kiosk can matter less than a high alert on the domain controller. The desk multiplies a severity weight, four for critical down to one for low, by the asset's criticality from one to three. A5, critical on a criticality-three server, scores twelve and goes first. A1, high on criticality three, scores nine. A3 and A6 both score six, so the earlier arrival, A3 at minute two, goes ahead of A6 at minute eight. A2, the critical alert on a criticality-one kiosk, scores four, and A4 scores three. Each alert also gets a due time: the minute it arrived plus the service-level target for its severity, fifteen minutes for critical, an hour for high, four hours for medium, a day for low. That puts A2's due time at minute 27 even though it sits fifth in the queue, which is a signal to ask for help rather than quietly breach the target. A queue is a plan you can explain to the shift lead, not a mood.

## Worked example

priority = severity weight × criticality: A5 12, A1 9, A3 6 (t=2), A6 6 (t=8), A2 4, A4 3; due = received + SLA (critical 15, high 60, medium 240, low 1440)
