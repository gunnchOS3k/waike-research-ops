# WAIKE Taxonomy (curriculum/taxonomy)

## Decision (ADR-style)

**Status:** Accepted for consumer contract  
**Date:** 2026-09-02  
**Context:** `eighteen_tracks.json` (`waike.taxonomy.eighteen_tracks.v1`) lists the owner 18 tracks but lacks stable UUIDs, historical aliases, package mappings, maturity, and a fail-closed resolver contract.

**Decision:** Introduce a new canonical registry rather than mutating the v1 snapshot in place.

| Artifact | Role |
|---|---|
| `eighteen_tracks.json` | **v1 compatibility snapshot** — keep as-is for existing readers |
| `academy_map_18_to_7.json` | Academy grouping (unchanged) |
| `canonical_track_registry.v1.json` | **Canonical contract** (`waike.taxonomy.canonical_track_registry.v1`) |
| `track_alias_map.v1.json` | Deterministic alias → track_id map (evidence-only) |
| `artifacts/taxonomy/CANONICAL_TRACK_REGISTRY.export.json` | Consumer export (hash + commit SHA + alias_map + package_mappings) |

**Consequences:**

- Consumers should prefer the canonical registry / export + `waike_curriculum.taxonomy.resolve_track_id`.
- UUIDs are deterministic `uuid5` over namespace `6ba7b810-9dad-11d1-80b4-00c04fd430c8` and name `waike.track.<TRACK_ID>`.
- Aliases are **evidence-only** (requirement IDs, exact snake folder/program stems, 1:1 historical package IDs). No fuzzy title matching.
- Multi-track packages (`GENERAL_IT`, and `HARDWARE_ENGINEERING` course.json multi-cover) live in `package_mappings`, **not** aliases.
- `GENERAL_IT` / `general_it` intentionally fail closed under `resolve_track_id`.

## Scripts

```bash
PYTHONPATH=src python3 scripts/validate_canonical_track_registry.py
PYTHONPATH=src python3 scripts/export_canonical_track_registry.py
PYTHONPATH=src python3 scripts/generate_taxonomy_reconciliation.py
PYTHONPATH=src pytest -q tests/test_canonical_track_registry.py
```
