# Week 4: Evaluation curves — thresholds are staffing decisions

Week 4 turns the busy classifier into a curve. Ticket EF-2411 gives score/label pairs for 20 validation rows. Sweeping threshold t from high to low changes TPR and FPR. The library board asks which t keeps FPR≤0.20 while maximizing TPR — that is an operating point, not a mystical AUC worship.

You will compute TPR=TP/(TP+FN) and FPR=FP/(FP+TN) at two named thresholds. The lab checks arithmetic. Claiming 'AUC=1 because we feel good' fails.

At t=0.60: TP=6 FP=2 FN=2 TN=10 → TPR=0.75 FPR=1/6≈0.167. Board constraint FPR≤0.20 holds.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

t=0.60 → TPR=0.75 FPR≈0.167 (≤0.20 constraint).
