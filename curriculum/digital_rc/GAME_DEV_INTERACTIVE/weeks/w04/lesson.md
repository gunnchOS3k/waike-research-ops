# Week 4: Entity state — finite states with illegal transition reject

Ticket GA-6404: states Idle→Run→Jump→Idle. Reject Jump→Run without Idle/land if table forbids.
Lab checks transition_ok and state_after.

Consensus Ladder: observed = transition table; inferred = illegal edges must hard-fail;
still need = animation blend trees. Failure: boolean soup without a table.

Author the transition table and reject illegal Jump→Run if the fixture forbids it.
transition_ok and state_after must match legality. Boolean soups without a table fail.

Animation blend trees are not claimed done after FSM week.

Author GA-6404 transition table rows and reject illegal Jump→Run when the fixture forbids
it. Publish transition_ok and state_after that match legality. Boolean soups without a
table fail. Animation blend trees are not claimed complete after FSM week. Add Idle→Jump
as a legal row and document the guard condition in one sentence next to the table.

Add a legal Run→Idle transition beside the illegal Jump→Run row so learners contrast guards
rather than memorizing a single boolean.

## Worked example

Only legal edges pass; illegal Jump→Run fails transition_ok.
