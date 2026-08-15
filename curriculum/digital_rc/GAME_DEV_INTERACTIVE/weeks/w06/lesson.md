# Week 6: Input mapping — actions not raw scancodes in design docs

Ticket GA-6606: map Jump to Space and South face button; rebindable=true; raw_only=false.
Lab checks actions include Jump and rebindable.

Consensus Ladder: observed = input table; inferred = actions survive device swaps;
still need = accessibility remaps beyond defaults (week 9). Failure: hard-coded scancode-only docs.

Actions, not scancodes: Jump must appear, rebindable=true, raw_only=false. Device swaps
should not break design docs. Week 9 accessibility remaps extend this work; they do not
delete it.

Bind GA-6606 actions (not scancodes): Jump must appear with rebindable=true and
raw_only=false. Argue why device swaps must not break design docs. Week 9 remaps extend
this contract; they do not erase it. Provide a sample remap table keyboard→gamepad that
keeps the Jump action id stable across devices. Also bind Interact and Pause with the
same action-id rule, and show a failing submission that stores only HID scancodes without
action names so the class can quote the reject reason in journals.

## Worked example

Jump action present; rebindable true; raw_only false.
