# Week 5: Tickets are promises, not chat threads

A ticket is a promise to restore someone's work. Severity is about impact, not volume of adjectives. SE1 is 'the whole desk is down during public hours.' SE3 is 'one kiosk idle-logout ate an essay.' Reboot-and-hope is never a next action in this course because it destroys evidence and trains patrons to kick hardware.

Ticket 4418: fan scream then black screen. Subsystem is hardware thermal, not 'Windows update.' Next action is capture temps and plan a reseat/clean, not order a new PC from a flyer. Ticket 4419: cannot reach printer.gary.waike.local — name resolution first, then spooler. You will be tempted to reinstall the printer driver. Resist until the name resolves.

SLA for SE3 at this desk is end of next public day. Write that in the ticket so a Sunday volunteer does not inherit a mystery. Documentation is an operational procedure on A+ V15 Core 2, but here it is also how Gary's Saturday shift survives.

Customer communication is specific: 'I saved a copy of your essay to the restore folder and the kiosk will still log out at 20 minutes because this is a shared station.' That sentence is kinder than 'we fixed it.'

## Learn the distinction

A support ticket is a record of a request, its scope, observations, actions and current disposition. Severity describes impact; priority orders work using impact and urgency. Neither should be assigned solely from how emphatically someone describes a problem. An action record must distinguish a proposed step from a step actually performed.

## Guided practice: hand off a ticket

Write a fictional ticket for a printer that is unavailable to one laptop. Include time, device alias, affected task, exact observed message, what still works, and the user's permission for any test. Suggest a bounded test: check whether another authorized application can print to that printer. Predict what each outcome would imply, without declaring a root cause in advance. Record a fictional result explicitly as simulated.

Now remove your own name from the procedure and give the record to a peer, or return to it after a break. Expected result: the next operator can identify the next safe action and the condition for stopping. If the record requires your memory, add the missing starting state or observation.

## Independent evidence

Triage three cases: one device cannot print; all devices in one room lack connectivity; a user reports a suspicious password request. Explain the ordering and the escalation boundary. Do not invent measurements. If no peer is available, label the handoff as a self-review rather than peer validation.

## Check your reasoning

A ticket can be resolved by a documented workaround without proving the root cause. Closure should include the user-visible verification and any remaining risk. Never record passwords or unnecessary personal information.

## Worked example

4417 next=adjust_idle_or_save_prompt; 4418 next=capture_temps_then_reseating_plan; 4419 next=check_hosts_then_spooler. None of them are reboot_and_hope.
