#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "results" / "validation" / "rubric_tables.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("# Rubric tables\n\nSee rubrics/master_rubric.yaml (scale 0–4).\n", encoding="utf-8")
print("Generated rubric tables")
