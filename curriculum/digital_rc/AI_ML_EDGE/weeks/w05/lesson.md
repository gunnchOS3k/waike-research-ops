# Week 5: Overfitting — when train glory means val shame

Ticket EF-2502 shows a student model with train_acc=0.99 and val_acc=0.61. That gap is the week's villain. Overfitting on EdgeForge often comes from memorizing janitor midnight patterns that never appear in daytime validation — or from tuning on the test fold until it smiles.

Generalization means the val fold stays sealed until the final score. The lab checks gap=train_acc-val_acc and whether you marked leakage_flags correctly (e.g., people_count in features). A gap≥0.25 with no mitigation note fails the honesty check.

gap=0.99-0.61=0.38. Mitigation options: fewer features, time-ordered CV, early stop. Not: 'download a bigger model.'

Gap is a first-class ticket field: train_acc minus val_acc. When gap ≥ 0.25 the mitigation note is mandatory — fewer features, stricter time-ordered CV, or early stop. 'Download a bigger checkpoint' is not a mitigation; it is a shopping list.

Seal the validation fold. Every peek that changes a hyperparameter after seeing val scores is a quiet restatement of the test set. EdgeForge treats that as the same class of failure as editing the golden JSON until it passes.

Mark leakage_flags when people_count sneaks into features. The honesty check fails if the gap is large and the note is empty, even when train_acc looks like a demo reel.

## Worked example

train_acc=0.99 val_acc=0.61 → gap=0.38 (≥0.25 triggers mitigation note).
