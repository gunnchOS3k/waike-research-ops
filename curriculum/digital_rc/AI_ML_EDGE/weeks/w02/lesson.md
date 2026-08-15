# Week 2: Supervised labels — desk occupancy as a class, not a vibe

Supervised learning on EdgeForge means a label you can argue about. Ticket EF-2204 asks for a binary busy/quiet label on zone A using people_count≥3 as busy. That threshold is a policy choice from the library board, not a neural insight. You will fit a logistic-style score on rssi_dbm and hour_of_day from the fixture — then count TP/FP/FN against the held-out 96 rows.

Beginners chase accuracy. EdgeForge chases false quiet alarms: predicting quiet when the room is busy means understaffing the desk. The lab computes precision/recall/F1 from your confusion counts; a print of 'PASS' is not a metric.

Feature leakage to refuse: do not include people_count as an input when it defines the label. That is cheating dressed as ML.

Confusion fixture: TP=40, FP=10, FN=5, TN=41. Precision=40/50=0.80. Recall=40/45≈0.889. F1=2*0.80*0.889/(0.80+0.889)≈0.842. Report three decimals.

Write the decision costs before you tune. A false quiet alarm skips a staff slot; a false busy alarm overstaffs and still wastes money, but the board ranked understaffing worse. That ranking is why precision on the busy class is not the only number on the ticket.

Build the confusion table by hand on the night fold before you trust a library summary. TP/FP/FN must match the fixture counts exactly to three decimals on F1. If an assistant drafts the defense paragraph, tag AI_DISCLOSED — the arithmetic remains yours.

Leakage check is a gate, not a tip: any feature that is a deterministic function of the busy rule fails the week even if the ROC looks pretty. EdgeForge would rather ship a weaker honest score than a perfect cheater.

## Worked example

TP=40 FP=10 FN=5 → precision=0.800 recall=0.889 F1≈0.842.
