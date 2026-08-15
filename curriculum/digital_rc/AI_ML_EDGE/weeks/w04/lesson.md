# Week 4: Evaluation curves — thresholds are staffing decisions

Week 4 turns the busy classifier into a curve. Ticket EF-2411 gives score/label pairs for 20 validation rows. Sweeping threshold t from high to low changes TPR and FPR. The library board asks which t keeps FPR≤0.20 while maximizing TPR — that is an operating point, not a mystical AUC worship.

You will compute TPR=TP/(TP+FN) and FPR=FP/(FP+TN) at two named thresholds. The lab checks arithmetic. Claiming 'AUC=1 because we feel good' fails.

At t=0.60: TP=6 FP=2 FN=2 TN=10 → TPR=0.75 FPR=1/6≈0.167. Board constraint FPR≤0.20 holds.

An operating point is a staffing contract. Sweep thresholds on the twenty validation pairs and stop when FPR crosses 0.20. Do not hand the board an AUC and walk away — AUC does not schedule a Saturday volunteer.

Compute TPR and FPR from the confusion at the chosen t; show both fractions. If two thresholds meet the FPR cap, prefer the higher TPR and document the tie-break in one line.

NO_AI week rule: generative fill of the fractions fails. Calculator OK. The board paragraph must name the threshold, the FPR, and the staffing implication without adjectives like 'robust AI.'

## Worked example

t=0.60 → TPR=0.75 FPR≈0.167 (≤0.20 constraint).
