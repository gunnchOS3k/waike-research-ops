# Week 8: Services, printers, and the tracker that must stay dead

cups (`cupsd`) must be enabled and active or Saturday résumés pile up. sshd stays up for staff recovery. `toy-tracker` is a classroom malware analog — it must be disabled and inactive on the image. If a volunteer 'enabled it to see what it does,' the lab fails and you rewrite the image.

Restart budgets matter. cupsd restart_sec ≤ 15 so a crash during a 40-job queue comes back before the line forms. A 120 second RestartSec is how you get a crowd and a rumor that 'the printer hates us.'

Virtualization shows up as a nested recovery VM on the closet PC: a Debian guest with snapshots. Hypervisor type-1 vs type-2 is a sentence you can say, not a VMware sales pitch. The guest is for practicing useradd, not for production kiosks.

Software troubleshooting: a 'printer offline' balloon is often cups paused, not hardware. You will learn to read `lpstat -p` (or the Windows analog) before you buy toner.

## Worked example

cupsd enabled+active restart_sec=8 pass. toy-tracker active fail. Nested Debian guest snapshot before practicing useradd.
