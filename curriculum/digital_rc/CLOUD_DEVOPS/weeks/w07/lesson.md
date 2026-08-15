# Week 7: Observability — error budgets before blame

Ticket FC-4719 sets SLO availability 99.5% over 10_000 requests. With 40 failures, availability=0.996 and budget_ok depends on the remaining error budget vs a 50-failure cap. You will compute availability and budget_ok. Blame-first chat without numbers fails.

failed=40 total=10000 → availability=0.996; failure_cap=50 → budget_ok=true.

SLO math: failed=40, total=10000 → availability=0.996; failure_cap=50 → budget_ok=true. Blame-first chat without numbers fails the ForgeCloud note.

If failed rises to 55 against cap 50, budget_ok flips false — write the inequality. Error budgets are how you decide whether to ship features or freeze for reliability work.

Observability is counts plus availability, not a wall of unlabeled graphs. The lab checks the arithmetic; your paragraph must cite it.

Week 7 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_slo_budget` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

40/10000 → 0.996 availability; under 50-failure cap → budget_ok.
