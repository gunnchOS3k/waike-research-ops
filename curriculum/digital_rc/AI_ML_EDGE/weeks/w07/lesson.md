# Week 7: Tiny neural net — forward pass without mythology

Neural foundations on EdgeForge stay tiny: one hidden layer, two inputs (windowed rssi, hour_norm), two hidden units, one sigmoid output. Ticket EF-2710 gives weights as JSON. You will compute the forward pass by hand (or with plain Python) and match the lab's expected y_hat within 1e-3.

No downloading ImageNet. No claiming 'deep learning' for a 2×2×1 net. The point is that a weight is a number you can audit.

h = relu(W1·x+b1); y=σ(W2·h+b2). Fixture expects y_hat≈0.731 for the published x.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

Published fixture forward pass yields y_hat≈0.731 (±1e-3).
