#!/usr/bin/env python3
"""Export course → research repo map for WAIKE apprenticeships."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAP = {
    "research_apprenticeship_digital_twin": "7gc-digital-twin",
    "research_apprenticeship_6g_ai_ran": "spectrumx-ai-ran-gary",
    "research_apprenticeship_beam_selection": "readygary-6g-beam-selection",
    "research_apprenticeship_edge_measurement": "edge-io-measurement-node",
    "research_apprenticeship_ntn_resilience": "ntn-resilience-sim",
    "research_apprenticeship_reproducible_research": "waike-research-ops",
}

LEVELS = {
    "beginner": ["Read SUPERVISOR_README", "Run target repo make e2e", "Open one research_task issue"],
    "intermediate": ["Fix test or doc", "Update traceability row"],
    "advanced": ["Add metric or scenario", "Draft paper figure"],
}


def main() -> int:
    payload = {"programs": MAP, "levels": LEVELS, "note": "synthetic map — no PII"}
    e2e = ROOT / "results" / "e2e"
    e2e.mkdir(parents=True, exist_ok=True)
    (e2e / "course_repo_map.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    md = ["# Course → Repo Map", ""]
    for prog, repo in MAP.items():
        md.append(f"- **{prog}** → `{repo}`")
    (e2e / "course_repo_map.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    idx = ["# Research Apprenticeship Index", ""]
    for level, tasks in LEVELS.items():
        idx.append(f"## {level.title()}")
        idx.extend(f"- {t}" for t in tasks)
        idx.append("")
    for p in sorted((ROOT / "programs").glob("research_apprenticeship_*.md")):
        idx.append(f"- Program: `{p.name}`")
    (e2e / "research_apprenticeship_index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    print(f"Wrote {e2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
