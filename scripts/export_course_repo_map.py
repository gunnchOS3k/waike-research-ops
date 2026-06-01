#!/usr/bin/env python3
"""Export course → research repo map and apprenticeship task lists."""
from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
MAP_YAML = ROOT / "knowledge_maps" / "course_repo_map.yaml"


def load_map() -> dict:
    if yaml and MAP_YAML.exists():
        return yaml.safe_load(MAP_YAML.read_text(encoding="utf-8"))
    return {"core_repos": [], "levels": {}}


def main() -> int:
    data = load_map()
    e2e = ROOT / "results" / "e2e"
    e2e.mkdir(parents=True, exist_ok=True)
    (e2e / "course_repo_map.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    md = ["# Course → Repo Map", ""]
    for repo in data.get("core_repos", []):
        md.append(f"- **{repo['id']}** — demo: `{repo.get('demo')}` — program: `{repo.get('apprenticeship')}`")
    (e2e / "course_repo_map.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    idx = ["# Research Apprenticeship Index", ""]
    for level, tasks in (data.get("levels") or {}).items():
        idx.append(f"## {level.title()}")
        idx.extend(f"- {t}" for t in tasks)
        idx.append("")
    (e2e / "research_apprenticeship_index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    for level in ("beginner", "intermediate", "advanced"):
        tasks = (data.get("levels") or {}).get(level, [])
        (e2e / f"{level}_tasks.md").write_text(f"# {level.title()} tasks\n\n" + "\n".join(f"- {t}" for t in tasks) + "\n")
    print(json.dumps({"repos": len(data.get("core_repos", []))}, indent=2))
    print(f"Wrote {e2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
