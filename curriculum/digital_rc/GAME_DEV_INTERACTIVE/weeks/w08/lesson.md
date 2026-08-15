# Week 8: Playtest metrics — session length and churn without vanity DAU

Ticket GA-6808: 40 sessions, 8 churn out before minute 3. Compute early_churn_rate and
median_session_min from fixture list. Lab checks rate math and refuses vanity_dau_claim=true.

Consensus Ladder: observed = session table; inferred = early churn is a design smell;
still need = cohort significance. Failure: fake million-DAU slides.

early_churn_rate = early_churn/sessions on the fixture (8/40=0.2). vanity_dau_claim
must be false. Fake million-DAU slides fail. Cohort significance remains a later need.

Median session minutes, when required by the lab fields, must come from the list math
rather than adjectives.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 8: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

early_churn_rate=8/40=0.2; vanity_dau_claim false.
