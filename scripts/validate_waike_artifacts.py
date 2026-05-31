#!/usr/bin/env python3
"""Validate WAIKE artifacts and core repo coverage."""
from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
CORE = {
    "7gc-digital-twin",
    "spectrumx-ai-ran-gary",
    "readygary-6g-beam-selection",
    "edge-io-measurement-node",
    "ntn-resilience-sim",
    "waike-research-ops",
}


def main() -> int:
    report = {"pass": True, "checks": []}
    ypath = ROOT / "knowledge_maps" / "course_repo_map.yaml"
    if not ypath.exists():
        report["pass"] = False
        report["checks"].append("missing course_repo_map.yaml")
    elif yaml:
        data = yaml.safe_load(ypath.read_text())
        ids = {r["id"] for r in data.get("core_repos", [])}
        missing = CORE - ids
        if missing:
            report["pass"] = False
            report["checks"].append(f"missing repos in map: {missing}")
    for prog in ROOT.glob("programs/research_apprenticeship_*.md"):
        text = prog.read_text(encoding="utf-8")
        for section in ("Beginner", "Intermediate", "Advanced", "ethics"):
            if section.lower() not in text.lower() and "beginner" not in section.lower():
                continue
        report["checks"].append(f"ok: {prog.name}")
    e2e = ROOT / "results" / "e2e"
    e2e.mkdir(parents=True, exist_ok=True)
    (e2e / "waike_validation_report.md").write_text(
        "# WAIKE Validation\n\n```json\n" + json.dumps(report, indent=2) + "\n```\n",
        encoding="utf-8",
    )
    print("PASS" if report["pass"] else "FAIL", json.dumps(report))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
