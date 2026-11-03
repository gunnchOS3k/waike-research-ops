# Week 9: Threats to validity and research ethics

SGA-1909 is the second NO_AI week, because the point is your own judgement about your own work. Sort what could make the results wrong into four kinds. Internal validity asks whether the comparison itself is fair: five seeds, a tuned model against an untuned baseline, or a data leak between training and test positions. External validity asks whether the result travels: one synthetic LEO scenario says little about a dense Gary street canyon or a Geelong port. Construct validity asks whether the metric measures what you care about: top-k accuracy ignores how many decibels are lost when the second-best beam is used. Conclusion validity asks whether the statistics support the sentence: five paired runs give a wide interval, and testing many metrics invites a lucky one. Then restate the guardrails every 7GC research program shares. Use synthetic data only. Never use private competition IQ captures, even if a teammate offers them. Make no claim that a university, operator, or agency endorses the work. A reviewer who sees honest threats listed early trusts the remaining claims more, not less.

## Worked example

internal: 5 seeds; external: one synthetic scenario; construct: top-k ignores SNR loss; conclusion: n=5, wide CI
