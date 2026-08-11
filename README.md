# waike-research-ops

**WAIKE** — Wireless + Artificial Intelligence Kinesthetic Education research operations for equitable learning pathways (Gary UPNOW context and broader gunnchOS3k education).

> **Current release/state:** `INTEGRATED` digitally — education/ops content; partner/external program execution remains EXTERNAL_PENDING where noted.

Ecosystem portal: [gunnchos-research-portal](https://github.com/gunnchOS3k/gunnchos-research-portal) · Product charter: [gunnchOS3k_PRODUCT_CHARTER.md](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/blob/main/program/charter/gunnchOS3k_PRODUCT_CHARTER.md)

## What is this?

Curriculum maps, standards alignment drafts, templates, and ops tooling for WAIKE programs — not a carrier product.

## Why does it exist?

Education and workforce pathways need an explicit ops layer alongside devices, OS, and AI.

## Where does it fit?

Product Charter **layer 14**. Surfaced via Ecosystem Portal `WAIKE` docs; pairs with `gunnchAI3k` tutoring.

## What is real today?

- Knowledge OS outlines and skill-tree YAML
- Program/templates under `programs/`, `templates/`, `knowledge_maps/`
- Public docs without transcripts/grades/PII

## What is simulated / modelled?

- Partial standards mappings until objective completion
- Scenario/campus curriculum packages that are research/education artifacts

## What is physical / external pending?

- External partner execution / institutional adoption evidence
- Any claim of accredited degree program or carrier workforce certification — **not claimed**

## Try / inspect in 5 minutes

```bash
# Browse the Knowledge OS entrypoints
ls docs knowledge_maps programs
# Run unit tests if present
python3 -m pytest -q tests 2>/dev/null || true
```
Start: `docs/00_WAIKE_KNOWLEDGE_OS.md`, `knowledge_maps/waike_skill_tree.yaml`.

## Architecture

Docs + YAML knowledge maps + templates/tools; optional Python under `src/` / `tools/`.

## Repo map

| Path | Role |
|---|---|
| `docs/` | Knowledge OS + guides |
| `knowledge_maps/` | Skill trees |
| `programs/` | Program packs |
| `standards_alignment/` | Partial mappings |
| `tools/` | Local-only helpers (no PII in git) |

## Interfaces

Content consumed by portal/education surfaces; tutor bridge references `gunnchAI3k`.

## Tests

```bash
python3 -m pytest -q tests
```

## Evidence

`results/` when present; otherwise docs + YAML are the artifact. No learner PII in public git.

## Known gaps

Completed objective standards mapping; external partner evidence; privacy-safe private ingest remains local-only.

## Beginner path

WAIKE is the **education pathway** around the devices — skills and programs, not radioshipping claims.

## Intern path

Read Knowledge OS levels 0–7 and propose one skill-tree improvement with tests.

## Expert path

Align standards maps honestly; keep education_ops ≠ carrier.

## Contribution path

Curriculum clarity, templates, tests. Never commit transcripts/grades/PII.

## Current release / state

**INTEGRATED** (content) · **EXTERNAL_PENDING** (partner execution). Not a carrier certification program.

## Claim boundary

Education/ops only · no commercial 6G · no certification · Cursor DRAFT-only.

---

## Retained detail (post–Cycle 3A front door)

Prior short README: [docs/history/README_PRE_WP012.md](docs/history/README_PRE_WP012.md).

> No transcripts, grades, or PII in this public repo. Use `tools/private_transcript_ingestion/` locally only.
