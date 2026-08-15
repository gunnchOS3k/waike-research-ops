# Week 8: Deploy + inference — scoring JSON on the rack

Deployment on EdgeForge is a scored JSON bundle pinned by sha256, not a demo laptop left unlocked. Ticket EF-2803 asks you to run inference on three feature vectors with the published model card (threshold 0.55) and record predictions + model_digest.

If the digest mismatches the card, refuse to score — supply-chain basics. The lab checks predictions and that digest matches.

Model digest sha256:ef2803aa.... Threshold 0.55. Vector scores [0.62,0.40,0.81] → labels [1,0,1].

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

scores 0.62/0.40/0.81 at t=0.55 → labels 1/0/1 with matching digest.
