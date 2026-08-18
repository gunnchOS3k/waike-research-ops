# Reproducibility — WAIKE Research Ops

Education/ops content plus Python validators. This repo does not produce RF results.

```bash
git clone https://github.com/gunnchOS3k/waike-research-ops.git
cd waike-research-ops
python3 -m pip install pytest
PYTHONPATH=src python3 -m pytest -q tests/test_pathway_schema.py tests/journeys tests/curriculum/test_digital_rc_batch.py
```

Expected: pytest PASS. Digital-RC count is **14 packages discovered from** `curriculum/digital_rc/*/course.json` — do not report 18 as COURSE_DIGITAL_RC.

Optional full lab bundle (heavier):

```bash
PYTHONPATH=src python3 scripts/emit_digital_rc.py
PYTHONPATH=src python3 scripts/run_course_labs.py
```

## Tool versions

| Tool | Guidance |
|---|---|
| Python | 3.12 in CI; 3.10+ locally |
| pytest | installed in CI via pip |

Record the commit SHA in any supervisor packet.

## Evidence discipline

**Real today:** course packages, schema tests, runnable lab validators, anonymous completion schema.

**Synthetic / demo-only:** campus scenario packs, mock evaluation dashboards.

**Not claimed:** accredited transcripts, partner classroom HUMAN_E6, citywide impact, Oulu affiliation, commercial 6G.

## Privacy

No grades, transcripts, or PII in git. Local-only path: `tools/private_transcript_ingestion/`.
