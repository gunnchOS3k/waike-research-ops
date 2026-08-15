# Week 4: Entity state — finite states with illegal transition reject

Ticket GA-6404: states Idle→Run→Jump→Idle. Reject Jump→Run without Idle/land if table forbids.
Lab checks transition_ok and state_after.

Consensus Ladder: observed = transition table; inferred = illegal edges must hard-fail;
still need = animation blend trees. Failure: boolean soup without a table.

Author the transition table and reject illegal Jump→Run if the fixture forbids it.
transition_ok and state_after must match legality. Boolean soups without a table fail.

Animation blend trees are not claimed done after FSM week.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 4: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

Only legal edges pass; illegal Jump→Run fails transition_ok.
