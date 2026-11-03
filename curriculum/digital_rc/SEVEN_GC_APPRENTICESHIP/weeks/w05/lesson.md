# Week 5: Beam selection — top-1 and top-k accuracy

SGA-1505 moves from link physics to the learning problem behind the AI-RAN papers. A millimetre-wave or NTN cell sweeps a codebook of narrow beams, and exhaustive sweeping costs time and overhead. A beam-selection model looks at side information, such as position or a coarse channel estimate, and ranks the beams it thinks are best, so the radio only measures the top few. The honest metric is top-k accuracy: the fraction of samples whose true best beam appears in the model's first k guesses. On the eight-sample fixture in the lab readme, four samples rank the true beam first, giving top-1 = 0.5, and seven of eight contain it within three guesses, giving top-3 = 0.875. Read those numbers together: top-3 tells you a three-beam refinement sweep would usually succeed, while top-1 says the model alone is right only half the time. Top-k also hides how much signal is lost when the second-best beam is chosen, which week nine records as a construct-validity threat. The fixture is synthetic, so dataset_class must say so.

## Worked example

8 samples; top-1 hits at samples 1,3,5,7 → 0.5; top-3 misses only sample 6 → 0.875
