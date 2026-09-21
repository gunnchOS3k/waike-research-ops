# Objectives — GAME_DEV_INTERACTIVE

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Game loop — fixed dt honesty on Forge Arcade
  - Complete the week contract: Game loop — fixed dt honesty on Forge Arcade.
  - Reproduce worked example: dt=1/60; clamp frame_time; spiral_of_death_guard true.
  - Ticket GA-6101: fixed timestep dt=1/60 with accumulator pattern.
### Week 2: AABB collision — overlap math before particle fireworks
  - Complete the week contract: AABB collision — overlap math before particle fireworks.
  - Reproduce worked example: hit = overlap_x and overlap_y; report both overlaps.
  - Ticket GA-6202: two AABBs.
### Week 3: Audio clock — beat grid without pirated sample packs
  - Complete the week contract: Audio clock — beat grid without pirated sample packs.
  - Reproduce worked example: BPM 120 → period 0.5; t=1.25 → beat 2 with phase 0.5.
  - Ticket GA-6303: BPM=120 → beat period 0.5 s.
### Week 4: Entity state — finite states with illegal transition reject
  - Complete the week contract: Entity state — finite states with illegal transition reject.
  - Reproduce worked example: Only legal edges pass; illegal Jump→Run fails transition_ok.
  - Ticket GA-6404: states Idle→Run→Jump→Idle.
### Week 5: Level data — JSON tiles with checksum, NO_AI
  - Complete the week contract: Level data — JSON tiles with checksum, NO_AI.
  - Reproduce worked example: tiles len = width*height; checksum_ok true.
  - Ticket GA-6505: level JSON with width, height, tiles length = width*height, and sha256 of
canonical bytes.
### Week 6: Input mapping — actions not raw scancodes in design docs
  - Complete the week contract: Input mapping — actions not raw scancodes in design docs.
  - Reproduce worked example: Jump action present; rebindable true; raw_only false.
  - Ticket GA-6606: map Jump to Space and South face button; rebindable=true; raw_only=false.
### Week 7: Optional four-game case study — no unmerged branch dependency
  - Complete the week contract: Optional four-game case study — no unmerged branch dependency.
  - Reproduce worked example: required_unmerged_branch=false; optional title from the four or none.
  - Ticket GA-6707: optional case study may cite anime-aggressors, beatlink-party, earth-species,
and foot-racing as named examples.
### Week 8: Playtest metrics — session length and churn without vanity DAU
  - Complete the week contract: Playtest metrics — session length and churn without vanity DAU.
  - Reproduce worked example: early_churn_rate=8/40=0.2; vanity_dau_claim false.
  - Ticket GA-6808: 40 sessions, 8 churn out before minute 3.
### Week 9: Accessibility — captions, remaps, color-safe UI, NO_AI
  - Complete the week contract: Accessibility — captions, remaps, color-safe UI, NO_AI.
  - Reproduce worked example: captions/remaps/colorblind_safe true; flash_hz≤3.
  - Ticket GA-6909: captions=true, remaps=true, colorblind_safe=true, flash_hz≤3.
### Week 10: Ship checklist capstone — build repro without unmerged deps
  - Complete the week contract: Ship checklist capstone — build repro without unmerged deps.
  - Reproduce worked example: a11y_ok true; labs_passed≥6; unmerged_branch_required false.
  - Ticket GA-6910: ship checklist with build_repro_hash, a11y_ok=true, labs_passed≥6,
unmerged_branch_required=false, and four_games_optional_note present.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
