# Week 1: Consent on the walk-up desk — name audience and purpose

Harbor Desk Voice opens with a consent card, not a slogan. When a patron asks the desk AI tutor for help on ticket PD-2101, you must say who hears the log, why it is kept, which data classes are stored, how many days it lives, and how to opt out. 'Everyone' is not an audience. 'Improve the product' is not a purpose when the desk's real purpose is coaching a restore path.

Ticket PD-2101 is a walk-up library patron whose essay vanished after idle logout. The tutor may log ticket_id, device_role, and lesson_progress. It must not log SSN, library-card PAN, or passwords. Retention for coaching notes is 90 days unless the desk lead shortens it. Opt-out is spoken: ask the desk lead to disable AI coaching on that ticket.

Consensus Ladder this week: observed = tutor banner missing audience line; inferred = consent incomplete; still need = desk lead confirmation before enabling logging. Fabricating 'ninety percent of patrons consented' is forbidden.

You will write a consent disclosure JSON that names audience, purpose, data_classes (≥2, no ssn), retention_days > 0, opt_out_path, and ai_disclosure=true. Empty {} fails. A file that only says PASS raises. This is professional communication as an operational control, not a poster on the wall.

## Worked example

Audience 'Saturday volunteers + walk-up patrons'; purpose 'ticket coaching logs'; classes ticket_id/device_role; retention 90; opt-out via desk lead; ai_disclosure true.
