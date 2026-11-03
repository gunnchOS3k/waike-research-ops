# Week 7: O-RAN control loops — where an AI model may act

SGA-1707 places the week-five model inside a real architecture. O-RAN splits radio control into loops by how fast they must react. Decisions under about 10 ms, such as HARQ retransmission and per-slot scheduling, stay in the distributed unit and its real-time software. Decisions between roughly 10 ms and one second run as xApps on the near-real-time RAN Intelligent Controller, which is where a beam-pair or handover tuning model would live. Anything slower than a second, including training, long-horizon energy policy, and analytics, runs as an rApp on the non-real-time RIC inside service management and orchestration. The non-real-time RIC guides the near-real-time RIC through the A1 interface with declarative policies, while E2 connects the near-real-time RIC to the base-station nodes it controls. The lab gives you three tasks; classify each by its loop latency, cover all three loops, and name the A1 target. Placing model training in the real-time loop is a design error, not an optimisation, and the grader treats it that way. O-RAN Alliance specifications are cited here for topic labels only.

## Worked example

HARQ 1 ms → real_time (DU); handover tuning 100 ms → near_real_time (xApp); energy policy 60 s → non_real_time (rApp); A1 → near_rt_ric
