# Week 2: Windowed detection — a threshold means nothing without a clock

SOC-2202 asks you to turn last night's eyeballing into a rule the SIEM can run. 'Four failed logins' is not a rule until you say within how long. The fixture lists eleven failures with second offsets. With a threshold of four inside a sixty-second sliding window, 203.0.113.45 fires at second 70: the failures at 20, 50, 65 and 70 all sit within sixty seconds of each other, while the first one at second 0 has already aged out. 198.51.100.7 never fires, because its attempts at 200, 230, 250 and 265 span sixty-five seconds, one heartbeat too slow. Widen the window to ninety seconds and that address alerts at 265 as well. Neither choice is free. A wider window catches slow guessing and also pulls in people who mistype their passwords on a cold morning. Write the threshold and window into the rule's description so the next analyst can reason about a miss, and replay the rule against stored events before you switch it on. The lab grader replays your parameters, so it rejects an alert list that would only be true for a different window.

## Worked example

threshold 4 in 60 s → 203.0.113.45 fires at t=70 (events 20, 50, 65, 70); 198.51.100.7 does not; widen to 90 s → it fires at 265
