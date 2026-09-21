# Canonical Package Entry Contract (18 tracks / 17 dirs)

Generated: `2026-09-20T15:36:37Z`  
Source commit: `c13179eaec0b23cf5a18b7dec9043e193bcb9460`

## Abstraction

WAIKE readiness is **track-addressable**: every canonical `track_id` has an entry at

`curriculum/canonical_packages/<TRACK_ID>/PACKAGE_MANIFEST.v1.json`

Content packaging remains **directory-efficient**. There are **18 track IDs** and **17** primary `curriculum/digital_rc/` package trees. The shared package is:

| Track IDs | Shared digital_rc dir | Rationale |
|-----------|----------------------|-----------|
| `DIGITAL_CONFIDENCE`, `IT_SUPPORT_HARDWARE` | `GENERAL_IT` | One civic desk package serves both foundation tracks |
| `NETWORKING_INFRA` | `COMPUTER_NETWORKING` | Legacy dir name; track_id is canonical |
| `CYBER_SOC` | `CYBERSECURITY` | Legacy dir name; track_id is canonical |

All other tracks map 1:1 to a same-named `digital_rc` directory.

## No blind duplication

- Do **not** copy full course trees under alias track directories.
- Alias tracks may have a **minimal** `curriculum/digital_rc/<TRACK_ID>/PACKAGE_MANIFEST.v1.json` that points at the shared legacy package.
- Canonical entry manifests always set `digital_rc_path` to the real content tree and record `shared_content_refs`.
- `content_hash` is sha256 of the referenced `course.json` so both sibling tracks share one hash when they share one package.

## Versioning fields

| Field | Meaning |
|-------|---------|
| `package_version` | Semver of the track entry / packaging surface |
| `compatibility_version` | Consumer schema pin (`waike.course_package.v1`) |
| `source_commit` | Git commit that produced the entry |
| `content_hash` | sha256 of referenced `course.json` |
| `deprecation` | `null` unless a track entry is retired |

## Validator

`scripts/full_readiness/validate_canonical_package_entries.py` asserts all 18 manifests exist, parse, match schema required fields, and that `digital_rc_path` / `course.json` are addressable.
