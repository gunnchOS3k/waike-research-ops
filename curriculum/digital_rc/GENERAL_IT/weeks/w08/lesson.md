# Week 8: Services, printers, and the tracker that must stay dead

cups (`cupsd`) must be enabled and active or Saturday résumés pile up. sshd stays up for staff recovery. `toy-tracker` is a classroom malware analog — it must be disabled and inactive on the image. If a volunteer 'enabled it to see what it does,' the lab fails and you rewrite the image.

Restart budgets matter. cupsd restart_sec ≤ 15 so a crash during a 40-job queue comes back before the line forms. A 120 second RestartSec is how you get a crowd and a rumor that 'the printer hates us.'

Virtualization shows up as a nested recovery VM on the closet PC: a Debian guest with snapshots. Hypervisor type-1 vs type-2 is a sentence you can say, not a VMware sales pitch. The guest is for practicing useradd, not for production kiosks.

Software troubleshooting: a 'printer offline' balloon is often cups paused, not hardware. You will learn to read `lpstat -p` (or the Windows analog) before you buy toner.

## Learn the distinction

A service is a program managed to provide a function, often without an interactive window. Enabled at startup and currently running describe different states. A running process may still be unhealthy; health requires a task-level check. A print queue can be paused while the physical printer remains functional.

## Guided practice: interpret a status record

Use this fictional record: `print-service: enabled=true, state=active, queue=paused`; `toy-tracker: enabled=false, state=inactive`. Predict what a print submission might experience and what will happen to each service after restart under this fixture's rules. Expected interpretation: startup configuration alone does not unpause the queue, and an intentionally disabled tracker should not be started merely to make every row green.

In an authorized disposable environment, inspect status using its service manager without changing configuration. Record the manager, service identifier and timestamp. If no VM is available, label your record as analysis of the fixture, not a live inspection.

## Independent evidence

Write a runbook for a paused queue: confirm scope and permission, preserve relevant job information without exposing document contents, make one approved change, test a fictional page, and state a rollback or escalation point. A reviewer must be able to distinguish observation from simulation.

## Check your reasoning

Restarting a service can disrupt other users and erase diagnostic context. Ask what evidence the restart would provide before using it. Do not disable a security or management service on a real device for classroom practice.

## Worked example

cupsd enabled+active restart_sec=8 pass. toy-tracker active fail. Nested Debian guest snapshot before practicing useradd.
