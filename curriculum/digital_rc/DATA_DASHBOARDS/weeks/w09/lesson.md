# Week 9: Freshness SLA — stale tiles fail (NO_AI)

Freshness is a defined time difference, not a decorative live badge. This model compares an explicit as-of timestamp with the newest retained valid observation. The “within policy” threshold is 30 minutes by default and includes the boundary. It is a teaching rule, not a measured service-level agreement or a guarantee of application availability.

Timestamps need explicit timezones. Two strings that display different clock hours can represent the same instant. Convert them to UTC before subtraction. A missing timezone is rejected so a local assumption does not silently change an answer. A future observation is also rejected in this model for clock and source review.

## Guided practice — calculate before running

The newest valid observation is v4 at 18:15 UTC. The missing v5 and negative v6 are not valid observations for this defined metric. At 18:40 UTC, age is 25 minutes: within the 30-minute policy. Run `ledger.py visits.csv report-stale.json --now 2026-10-01T19:00:00Z`. Expected result: age is 45 minutes and within_policy is false. This unfavorable result is correct and must remain visible.

Compare 18:40Z with 20:40+02:00 using a copied invocation. Both represent the same as-of instant, so age remains 25. Explain why a newer invalid row does not automatically make a valid-data chart fresh. Distinguish observation time from actual ingestion time; the fixture has no independently measured arrival clock.

## Independent evidence and recovery

For new case timestamps, calculate one within-policy, one exact-boundary and one stale result by hand. Preserve the canonical NO_AI assessment rules for unaided evidence. Include a missing-timezone rejection and document clock assumptions. A stale result calls for honest labeling and investigation, not changing the clock to manufacture freshness.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

As-of18:40Z minus newest-valid18:15Z gives25minutes, within30. As-of19:00Z gives45minutes, correctly stale. Neither result is a measurement of operational service availability.
