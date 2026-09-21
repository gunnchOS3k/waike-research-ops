# Objectives — GUNNCHOS_PRODUCT_LAB

## Program learning outcomes

1. Write testable user stories and non-functional requirements for a Device OS surface.
2. Map system architecture across apps, services, and capability adapters without inventing unmerged hardware.
3. Exercise digital Device Lab / simulator paths before any PHYSICAL_PENDING step.
4. Apply accessibility, privacy, and security review checklists to a release candidate.
5. Produce a portfolio packet with provenance, claim boundary, and reproducibility notes.

## Week-level objectives (from package lessons)

### Week 1: Product charter — scope without fabricated impact
  - Complete the week contract: Product charter — scope without fabricated impact.
  - Reproduce worked example: problem=checkout latency, goal_metric=median_wait_minutes, fabricated_outcomes=false
  - gunnchOS Product Lab Bench ticket GPL-5101: Product charter — scope without fabricated impact.
### Week 2: Compatibility matrix — device-os × gunnchAI pins
  - Complete the week contract: Compatibility matrix — device-os × gunnchAI pins.
  - Reproduce worked example: device_os_sha=d5c2d17, gunnchai_sha=d357846, contract_ok=true
  - gunnchOS Product Lab Bench ticket GPL-5202: Compatibility matrix — device-os × gunnchAI pins.
### Week 3: Checkout flow — ticket states and handoff
  - Complete the week contract: Checkout flow — ticket states and handoff.
  - Reproduce worked example: states=[requested,approved,checked_out,returned], orphan_state=false
  - gunnchOS Product Lab Bench ticket GPL-5303: Checkout flow — ticket states and handoff.
### Week 4: Compose health — migrate before healthy
  - Complete the week contract: Compose health — migrate before healthy.
  - Reproduce worked example: migrate_ok=true, health=healthy, rollback_to!=current_digest
  - gunnchOS Product Lab Bench ticket GPL-5404: Compose health — migrate before healthy.
### Week 5: Privacy BOM — field inventory without PII
  - Complete the week contract: Privacy BOM — field inventory without PII.
  - Reproduce worked example: fields=[camera,mic,location], pii_in_bom=false, retention_days=30
  - gunnchOS Product Lab Bench ticket GPL-5505: Privacy BOM — field inventory without PII.
### Week 6: Guest protocol — ping/boot_status contract
  - Complete the week contract: Guest protocol — ping/boot_status contract.
  - Reproduce worked example: ping_ok=true, boot_status=ready, protocol_version=wp011r
  - gunnchOS Product Lab Bench ticket GPL-5606: Guest protocol — ping/boot_status contract.
### Week 7: Release notes — semver and breaking flag
  - Complete the week contract: Release notes — semver and breaking flag.
  - Reproduce worked example: semver=1.4.0, breaking=false, changelog_entries=3
  - gunnchOS Product Lab Bench ticket GPL-5707: Release notes — semver and breaking flag.
### Week 8: CI gate tokens — honest pass/fail
  - Complete the week contract: CI gate tokens — honest pass/fail.
  - Reproduce worked example: tokens_passed=4, tokens_total=4, fabricated_green=false
  - gunnchOS Product Lab Bench ticket GPL-5808: CI gate tokens — honest pass/fail.
### Week 9: Cross-repo dependency pin — no preview in accepted
  - Complete the week contract: Cross-repo dependency pin — no preview in accepted.
  - Reproduce worked example: preview_sha_in_accepted=false, pin_file=CURRENT_ACCEPTED_MAIN.json
  - gunnchOS Product Lab Bench ticket GPL-5909: Cross-repo dependency pin — no preview in accepted.
### Week 10: Product lab capstone — charter+compat+CI evidence
  - Complete the week contract: Product lab capstone — charter+compat+CI evidence.
  - Reproduce worked example: labs_passed≥6, compat_ok=true, no_device_os_pr=true, no_key_leak=true
  - gunnchOS Product Lab Bench ticket GPL-5A10: Product lab capstone — charter+compat+CI evidence.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
