# Week 4: Entity state — finite states with illegal transition reject

Ticket GA-6404: states Idle→Run→Jump→Idle. Reject Jump→Run without Idle/land if table forbids.
Lab checks transition_ok and state_after.

Consensus Ladder: observed = transition table; inferred = illegal edges must hard-fail;
still need = animation blend trees. Failure: boolean soup without a table.

Operators keep a numbered ticket trail for w4-lab_entity_fsm and refuse noun-swapped decks from other academies. Detail mark w4-lab_entity_fsm-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w4-lab_entity_fsm-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w4-lab_entity_fsm-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w4-lab_entity_fsm-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w4-lab_entity_fsm-4.

## Worked example

Only legal edges pass; illegal Jump→Run fails transition_ok.
