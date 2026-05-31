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


def main() -> int:
    out_dir = ROOT / "docs" / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "course_repo_map.json"
    payload = {"programs": MAP, "note": "synthetic map for supervisor demo"}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
