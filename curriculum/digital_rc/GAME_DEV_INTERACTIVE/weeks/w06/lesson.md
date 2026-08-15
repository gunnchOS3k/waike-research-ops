# Week 6: Input mapping — actions not raw scancodes in design docs

Ticket GA-6606: map Jump to Space and South face button; rebindable=true; raw_only=false.
Lab checks actions include Jump and rebindable.

Consensus Ladder: observed = input table; inferred = actions survive device swaps;
still need = accessibility remaps beyond defaults (week 9). Failure: hard-coded scancode-only docs.

Actions, not scancodes: Jump must appear, rebindable=true, raw_only=false. Device swaps
should not break design docs. Week 9 accessibility remaps extend this work; they do not
delete it.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 6: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

Jump action present; rebindable true; raw_only false.
