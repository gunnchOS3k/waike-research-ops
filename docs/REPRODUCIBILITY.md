# Reproducibility

## Quickstart

```bash
git clone https://github.com/gunnchOS3k/waike-research-ops.git
cd waike-research-ops
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python scripts/export_course_repo_map.py
```

## Tests

```bash
pytest -q
```

## Sample data policy

Synthetic/toy only. **No private competition data.** No student PII.

## Regenerate artifacts

Demo commands write to `results/` or `docs/generated/` where applicable.

## Citation

See `CITATION.cff` in repo root.
