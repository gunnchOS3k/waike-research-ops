#!/usr/bin/env python3
from pathlib import Path
out = Path("results/tooling_learning")
out.mkdir(parents=True, exist_ok=True)
for name in ["nvidia_6g_learning_path", "oran_learning_path", "sionna_deepmimo_learning_path", "eucnc_watchlist", "industry_tooling_apprenticeship_map"]:
    (out / f"{name}.md").write_text(f"# {name}\n\nBeginner: read NON_AFFILIATION_NOTICE. First lab: run repo smoke test.\n", encoding="utf-8")
print("Wrote results/tooling_learning/")
