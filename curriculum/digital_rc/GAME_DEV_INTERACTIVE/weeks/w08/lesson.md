# Week 8: Playtest metrics — session length and churn without vanity DAU

Ticket GA-6808: 40 sessions, 8 churn out before minute 3. Compute early_churn_rate and
median_session_min from fixture list. Lab checks rate math and refuses vanity_dau_claim=true.

Consensus Ladder: observed = session table; inferred = early churn is a design smell;
still need = cohort significance. Failure: fake million-DAU slides.

early_churn_rate = early_churn/sessions on the fixture (8/40=0.2). vanity_dau_claim
must be false. Fake million-DAU slides fail. Cohort significance remains a later need.

Median session minutes, when required by the lab fields, must come from the list math
rather than adjectives.

Compute GA-6808 early_churn_rate = early_churn/sessions on the fixture (8/40=0.2) and keep
vanity_dau_claim false. Fake million-DAU slides fail. Median session minutes, when required,
come from list math, not adjectives. Cohort significance remains later-need.

Recompute early_churn_rate with a second fixture slice (5 churn / 25 sessions = 0.2) and show
the rate is identical while vanity_dau_claim stays false. Refuse screenshots that replace the
ratio with adjectives about 'sticky players.'

## Worked example

early_churn_rate=8/40=0.2; vanity_dau_claim false.
