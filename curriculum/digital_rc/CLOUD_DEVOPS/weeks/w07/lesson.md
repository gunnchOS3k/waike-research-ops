# Week 7: Observability — error budgets before blame

Ticket FC-4719 sets SLO availability 99.5% over 10_000 requests. With 40 failures, availability=0.996 and budget_ok depends on the remaining error budget vs a 50-failure cap. You will compute availability and budget_ok. Blame-first chat without numbers fails.

failed=40 total=10000 → availability=0.996; failure_cap=50 → budget_ok=true.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

40/10000 → 0.996 availability; under 50-failure cap → budget_ok.
