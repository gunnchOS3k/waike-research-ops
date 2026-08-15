# Week 8: Deploy + inference — scoring JSON on the rack

Deployment on EdgeForge is a scored JSON bundle pinned by sha256, not a demo laptop left unlocked. Ticket EF-2803 asks you to run inference on three feature vectors with the published model card (threshold 0.55) and record predictions + model_digest.

If the digest mismatches the card, refuse to score — supply-chain basics. The lab checks predictions and that digest matches.

Model digest sha256:ef2803aa.... Threshold 0.55. Vector scores [0.62,0.40,0.81] → labels [1,0,1].

Inference is applying a pinned card, not improvising on an unlocked laptop. Threshold 0.55 on scores [0.62,0.40,0.81] yields labels [1,0,1] only when model_digest matches sha256:ef2803aa.

Digest mismatch means refuse to score — supply chain is a verb. Do not 'hotfix' by pasting new weights into the card without rotating the digest in the change record.

Record predictions and the digest in the lab JSON. A screenshot of a dashboard gauge is not a substitute for those fields. EdgeForge will not accept a demo that cannot name its bytes.

## Worked example

scores 0.62/0.40/0.81 at t=0.55 → labels 1/0/1 with matching digest.
