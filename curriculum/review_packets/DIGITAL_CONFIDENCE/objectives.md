# Objectives — DIGITAL_CONFIDENCE

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: The Civic Tech Desk — three jobs a computer actually has
  - Complete the week contract: The Civic Tech Desk — three jobs a computer actually has.
  - Reproduce worked example: Idle policy 1200s = 20 minutes. Patron sat down at 14:02, last keystroke 14:07, return 14:28. Session is gone. Restore from the auto-save folder if present; do not disable the timer as your first move — the timer is a shared-kiosk control.
  - At the Gary Civic Tech Desk the machine in front of a patron is not a personality.
### Week 2: Two operating systems, one pair of hands
  - Complete the week contract: Two operating systems, one pair of hands.
  - Reproduce worked example: A 4.7 GiB `.mkv` copied to a FAT32 camera card ends as a 0-byte or missing file. Reformat is the wrong first step. Copy to the NTFS staff volume, then to the patron exFAT share.
  - The Civic Tech Desk dual-boots a Windows 11 image for walk-up patrons and a Debian bookworm image for staff recovery.
### Week 3: Users, groups, and the sudo you can actually type
  - Complete the week contract: Users, groups, and the sudo you can actually type.
  - Reproduce worked example: kiosk uid 1010, groups=[kiosk], sudo=false. desk.lead uid 1020, groups=[helpdesk, staff]. If kiosk also sits in sudo, the lab fails even if the password is long.
  - The kiosk account exists so a stranger can browse.
### Week 4: Storage, snapshots, and the Friday 16:00 panic
  - Complete the week contract: Storage, snapshots, and the Friday 16:00 panic.
  - Reproduce worked example: size=256GiB used=180 reserved=12 → free=64 GiB → 64/256=0.25 ≥ 0.15. SHA256 of source tree must equal SHA256 of restored tree.
  - The civic volume is 256 GiB.
### Week 5: Tickets are promises, not chat threads
  - Complete the week contract: Tickets are promises, not chat threads.
  - Reproduce worked example: 4417 next=adjust_idle_or_save_prompt; 4418 next=capture_temps_then_reseating_plan; 4419 next=check_hosts_then_spooler. None of them are reboot_and_hope.
  - A ticket is a promise to restore someone's work.
### Week 6: Hardware triage — power, then storage, then memory, then OS
  - Complete the week contract: Hardware triage — power, then storage, then memory, then OS.
  - Reproduce worked example: No video, fans spin, one short beep, Ethernet lights off because you pulled the PC out. Restore the display cable and the patch cable before you unbox the spare SODIMM.
  - The Civic Tech Desk keeps a parts tub: one spare 16 GB SODIMM, one SATA SSD, one 90 W brick, one display cable.
### Week 7: Names on the LAN — hosts, a tiny zone, and the printer that only exists locally
  - Complete the week contract: Names on the LAN — hosts, a tiny zone, and the printer that only exists locally.
  - Reproduce worked example: Query printer.gary.waike.local → 10.20.30.40 from hosts. Query example.com → none. Link-local 169.254.13.9 on a kiosk → DHCP failure, not a new addressing plan.
  - printer.gary.waike.local is not on the public Internet and should not be.
### Week 8: Services, printers, and the tracker that must stay dead
  - Complete the week contract: Services, printers, and the tracker that must stay dead.
  - Reproduce worked example: cupsd enabled+active restart_sec=8 pass. toy-tracker active fail. Nested Debian guest snapshot before practicing useradd.
  - cups (`cupsd`) must be enabled and active or Saturday résumés pile up.
### Week 9: Automation without heroics — snapshot, change window, rollback
  - Complete the week contract: Automation without heroics — snapshot, change window, rollback.
  - Reproduce worked example: Window 18:00–21:00, planned 19:15 → in window. Steps [snapshot_home, apply_idle_policy, verify_kiosk_login]. Rollback named.
  - CHG-88 moves the idle policy.
### Week 10: After-hours capstone — keep the desk alive without becoming a hero
  - Complete the week contract: After-hours capstone — keep the desk alive without becoming a hero.
  - Reproduce worked example: Capstone scoring: tickets with subsystems, passing lab hashes, CHG in window, recorder notes usable by a stranger, no PII.
  - Saturday 16:40: kiosk idle-logout, printer name missing from a volunteer laptop on guest Wi-Fi, disk at 88% used, and a well-meaning AI browser extension asking for admin.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
