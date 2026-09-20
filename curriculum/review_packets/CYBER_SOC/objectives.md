# Objectives — CYBER_SOC

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Harbor SOC — principles, governance, and the model that is also an asset
  - Complete the week contract: Harbor SOC — principles, governance, and the model that is also an asset.
  - Reproduce worked example: A triage bot with sudo would violate least privilege for a non-human identity and would turn a prompt injection into root. Harbor policy: bots read, humans close.
  - Harbor SOC is a classroom security operations center for WAIKE.
### Week 2: Identity lifecycle — Naiya, Omar, and harbor-bot
  - Complete the week contract: Identity lifecycle — Naiya, Omar, and harbor-bot.
  - Reproduce worked example: allow(naiya, case.close)=false; allow(omar, case.close)=true; allow(harbor-bot, case.close)=false.
  - Naiya is an analyst: read and comment.
### Week 3: Cloud-shaped edges and the kiosk that must not walk into the SOC
  - Complete the week contract: Cloud-shaped edges and the kiosk that must not walk into the SOC.
  - Reproduce worked example: matrix[(kiosk,soc)]=deny; [(soc,kiosk)]=allow_syslog_only; [(guest,staff)]=deny.
  - Networking and cloud security on the upcoming CC outline is not a vendor catalog.
### Week 4: SIEM triage — bursts are a look, not a conviction
  - Complete the week contract: SIEM triage — bursts are a look, not a conviction.
  - Reproduce worked example: counts ada=4, cal=1, threshold=3 → bursts=['ada']. Note: burst, not attacker.
  - AUTH_FAIL lines for ada four times from 10.20.30.5 cross the threshold of 3.
### Week 5: Hardening the image — guest off, keys on, bot sudo off
  - Complete the week contract: Hardening the image — guest off, keys on, bot sudo off.
  - Reproduce worked example: All six baseline flags must match. Mutating ai_agent_sudo true fails the lab.
  - The Harbor workstation image: guest_login false, ssh_password_auth false, unattended_upgrades true, open_ports {22,443}, world_writable_home false, ai_agent_sudo false.
### Week 6: Segmentation that survives a stolen laptop
  - Complete the week contract: Segmentation that survives a stolen laptop.
  - Reproduce worked example: Revoke omar's sessions before rewriting the zone matrix. Matrix widen is not containment.
  - A stolen staff laptop should not become a SOC pass.
### Week 7: Incident clock — detect, contain, eradicate, recover, lessons
  - Complete the week contract: Incident clock — detect, contain, eradicate, recover, lessons.
  - Reproduce worked example: steps == [detect, contain, eradicate, recover, lessons]. contain index < eradicate index.
### Week 8: Authorized toy parser — detect the length lie, do not grow an exploit kit
  - Complete the week contract: Authorized toy parser — detect the length lie, do not grow an exploit kit.
  - Reproduce worked example: unsafe(\x14short) returns a short slice (the lie). safe(\x14short) raises ValueError. safe(\x04abcd)==b'abcd'.
  - Berkeley CS161 uses authorized vulnerable targets in a course VM.
### Week 9: USB story — a timeline is an argument
  - Complete the week contract: USB story — a timeline is an argument.
  - Reproduce worked example: kinds after sort: login, usb_insert, file_copy, usb_unmount. Copy sits between insert and unmount.
  - Events: login t=90, usb_insert t=100, file_copy t=140, usb_unmount t=155.
### Week 10: Harbor capstone — evidence locker design then operate
  - Complete the week contract: Harbor capstone — evidence locker design then operate.
  - Reproduce worked example: Policy checker rejects records with password= and rejects harbor-bot as closer. Seven labs ok, three negatives fail as required.
  - CS161's depth pattern is design-document checkpoint then implementation.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
