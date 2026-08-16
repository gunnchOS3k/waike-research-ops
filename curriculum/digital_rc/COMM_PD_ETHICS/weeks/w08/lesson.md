# Week 8: AI disclosure modes — keys stay out

AI disclosure modes on Harbor Desk Voice are AI_ALLOWED, AI_RESTRICTED, AI_DISCLOSED, and NO_AI. Ticket PD-2822 requires disclosed=true, learner-key-access=false, learner_facing=true. Learner tutor and mastery benchmark modes must not load the instructor key store. Educator copilot may read keys only with HITL grading — never to whisper finals to learners.

For NO_AI mode, rationale must say human-only or no ai. Silent AI use during NO_AI weeks fails honesty even if the JSON looks fine.

Consensus Ladder: observed = mode banner; inferred = key access forbidden; still need = rationale sentence; action = submit disclosure JSON. This week wires the gunnchAI contract permission split into a lab students can run. Harbor Desk Voice insists on numbered ticket IDs in journals so a Saturday volunteer can continue without a hallway interrogation. Write the next action as a verb phrase a stranger can execute. Keep patron faces, passwords, and invented harm counts out of the packet. If two tools disagree, write what you saw, then what you guessed, then the missing fact before changing shared systems. Professional development here is measured by reproducible desk artifacts, not by slogans about culture.

## Worked example

mode valid; disclosed true; used_key material false; learner_facing true.
