# Week 2: Reproducible runs — config digest, seed, and rerun

SGA-1202 turns the week-one question into something another apprentice can rerun on a different campus. A run manifest has four parts. The config text is the exact file the simulator read, byte for byte, and its SHA-256 digest proves which file that was; changing a single newline changes the digest, so the grader recomputes it rather than trusting a pasted hash. The seed must be an integer you chose and wrote down, not the word random, because an unpinned generator makes every comparison later in the course meaningless. The command line is recorded verbatim, including flags, so nobody has to guess which entry point produced a figure. Finally, run the same seed and config twice and report both metrics. If they differ, something nondeterministic is leaking in: thread scheduling, an unseeded library, or a timestamp in the config. Track that down before moving on. Gary, Geelong, and Nubuke cohorts swap manifests in week ten, and a figure whose manifest does not reproduce is removed from the shared packet rather than footnoted.

## Worked example

config_text='scenario=leo600_sband\nseed=20261102\nbeams=8\nepochs=5\n' → sha256 recorded; rerun_metric_a == rerun_metric_b == 0.625
