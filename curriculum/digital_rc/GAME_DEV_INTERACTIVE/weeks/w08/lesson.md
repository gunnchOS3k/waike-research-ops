# Week 8: Playtest metrics — session length and churn without vanity DAU

Ticket GA-6808: 40 sessions, 8 churn out before minute 3. Compute early_churn_rate and
median_session_min from fixture list. Lab checks rate math and refuses vanity_dau_claim=true.

Consensus Ladder: observed = session table; inferred = early churn is a design smell;
still need = cohort significance. Failure: fake million-DAU slides.

Operators keep a numbered ticket trail for w8-lab_playtest_metrics and refuse noun-swapped decks from other academies. Detail mark w8-lab_playtest_metrics-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w8-lab_playtest_metrics-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w8-lab_playtest_metrics-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w8-lab_playtest_metrics-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w8-lab_playtest_metrics-4.

## Worked example

early_churn_rate=8/40=0.2; vanity_dau_claim false.
