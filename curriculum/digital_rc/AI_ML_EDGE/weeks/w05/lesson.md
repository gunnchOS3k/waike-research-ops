# Week 5: Overfitting — when train glory means val shame

Ticket EF-2502 shows a student model with train_acc=0.99 and val_acc=0.61. That gap is the week's villain. Overfitting on EdgeForge often comes from memorizing janitor midnight patterns that never appear in daytime validation — or from tuning on the test fold until it smiles.

Generalization means the val fold stays sealed until the final score. The lab checks gap=train_acc-val_acc and whether you marked leakage_flags correctly (e.g., people_count in features). A gap≥0.25 with no mitigation note fails the honesty check.

gap=0.99-0.61=0.38. Mitigation options: fewer features, time-ordered CV, early stop. Not: 'download a bigger model.'

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

train_acc=0.99 val_acc=0.61 → gap=0.38 (≥0.25 triggers mitigation note).
