# Sequence — IT_SUPPORT_HARDWARE

Complete module/week sequence from `IT_SUPPORT_HARDWARE` `course.json`.

| Week | Title | Lesson ID | Lab ID |
|------|-------|-----------|--------|
| 1 | The Civic Tech Desk — three jobs a computer actually has | `IT_SUPPORT_HARDWARE-w01` | `lab_ticket_queue` |
| 2 | Two operating systems, one pair of hands | `IT_SUPPORT_HARDWARE-w02` | `lab_os_users` |
| 3 | Users, groups, and the sudo you can actually type | `IT_SUPPORT_HARDWARE-w03` | `lab_os_users` |
| 4 | Storage, snapshots, and the Friday 16:00 panic | `IT_SUPPORT_HARDWARE-w04` | `lab_backup` |
| 5 | Tickets are promises, not chat threads | `IT_SUPPORT_HARDWARE-w05` | `lab_ticket_queue` |
| 6 | Hardware triage — power, then storage, then memory, then OS | `IT_SUPPORT_HARDWARE-w06` | `lab_storage` |
| 7 | Names on the LAN — hosts, a tiny zone, and the printer that only exists locally | `IT_SUPPORT_HARDWARE-w07` | `lab_dns_hosts` |
| 8 | Services, printers, and the tracker that must stay dead | `IT_SUPPORT_HARDWARE-w08` | `lab_services` |
| 9 | Automation without heroics — snapshot, change window, rollback | `IT_SUPPORT_HARDWARE-w09` | `lab_automation_runbook` |
| 10 | After-hours capstone — keep the desk alive without becoming a hero | `IT_SUPPORT_HARDWARE-w10` | `lab_automation_runbook` |

## Syllabus excerpt (source)

```
# IT Support and Hardware Foundations
## Addressability
This is the independent entry package for `IT_SUPPORT_HARDWARE`. Weekly **lesson bodies** are shared by `content_ref` from `GENERAL_IT` (see `shared_modules/general_it_content_ref.json`) to avoid blind duplication.
## Track focus
Support + hardware foundations: power-first triage, storage/memory checks, ESD-safe handling, and change windows.
## Objectives
- Execute power → storage → memory → OS triage on fixtures
- Document ESD-safe handling and bring-up checks
- Plan parts swaps only after naming the subsystem
- Apply shared change-window discipline with HITL
## Weekly map (shared modules + track emphasis)
- Week 01: Three jobs a computer actually has — *emphasis:* Ticket language that names subsystems — content_ref `GENERAL_IT/weeks/w01/lesson.md` — lab `lab_ticket_queue`
- Week 02: Two operating systems, one pair of hands — *emphasis:* Filesystem/media choices for recovery sticks — content_ref `GENERAL_IT/weeks/w02/lesson.md` — lab `lab_os_users`
- Week 03: Users, groups, and sudo you can type — *emphasis:* Privilege groups for desk.lead vs kiosk — content_ref `GENERAL_IT/weeks/w03/lesson.md` — lab `lab_os_users`
- Week 04: Storage, snapshots, and restore proof — *emphasis:* Capacity/quota before 'disk full' panic — content_ref `GENERAL_IT/weeks/w04/lesson.md` — lab `lab_backup`
- Week 05: Tickets are promises — *emphasis:* SE1 vs SE3 hardware impact — content_ref `GENERAL_IT/weeks/w05/lesson.md` — lab `lab_ticket_queue`
- Week 06: Hardware triage order — *emphasis:* Power-first hardware triage (primary emphasis) — content_ref `GENERAL_IT/weeks/w06/lesson.md` — lab `lab_storage`
- Week 07: Names on the LAN — *emphasis:* Link lights before blaming phones — content_ref `GENERAL_IT/weeks/w07/lesson.md` — lab `lab_dns_hosts`
- Week 08: Services and printers — *emphasis:* cups/sshd vs malware-analog service hygiene — content_ref `GENERAL_IT/weeks/w08/lesson.md` — lab `lab_services`
- Week 09: Change windows and rollback — *emphasis:* Snapshot/change window before image writes — content_ref `GENERAL_IT/weeks/w09/lesson.md` — lab `lab_automation_runbook`
- Week 10: After-hours desk survival — *emphasis:* Capstone: mixed desk + hardware incidents — content_ref `GENERAL_IT/weeks/w10/lesson.md` — lab `lab_automation_runbook`
## Assessments
Track mid/final emphasize hardware triage and ESD/HITL. Shared labs via GENERAL_IT. NO_AI on weeks 5 and 10.
## Claim boundary
Shares GENERAL_IT modules; does not grant CompTIA/Google credentials; no job guarantee.
```

## Duration note

Package default is **10 weeks**. Program files may also list workshop/bootcamp/apprenticeship formats — those are alternate delivery envelopes, not alternate content claims.
