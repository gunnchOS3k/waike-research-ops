# Week 7: Tiny neural net — forward pass without mythology

Neural foundations on EdgeForge stay tiny: one hidden layer, two inputs (windowed rssi, hour_norm), two hidden units, one sigmoid output. Ticket EF-2710 gives weights as JSON. You will compute the forward pass by hand (or with plain Python) and match the lab's expected y_hat within 1e-3.

No downloading ImageNet. No claiming 'deep learning' for a 2×2×1 net. The point is that a weight is a number you can audit.

h = relu(W1·x+b1); y=σ(W2·h+b2). Fixture expects y_hat≈0.731 for the published x.

A weight is a number you can audit. The published 2×2×1 net uses ReLU hidden units and a sigmoid output; you will forward-propagate x=[0.5,0.2] to y_hat within 1e-3 of the fixture.

Refuse ImageNet downloads and 'deep learning' branding for a toy net. The pedagogical point is that deployment later pins these exact numbers by digest — mythology does not pin.

NO_AI week for the arithmetic: show h activations and the final σ(z). If you use a tool for explanations only, keep it off the submitted y_hat path. Mismatch beyond 1e-3 fails even when the story sounds confident.

## Worked example

Published fixture forward pass yields y_hat≈0.731 (±1e-3).
