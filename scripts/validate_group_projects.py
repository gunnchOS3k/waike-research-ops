#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog

try:
    import yaml
except ImportError:
    yaml = None


def main() -> int:
    missing = []
    for c in load_catalog().get("courses", []):
        cid = c["course_id"]
        p = ROOT / "group_projects" / "by_course" / f"{cid}.yaml"
        if not p.exists():
            missing.append(cid)
            continue
        if yaml:
            data = yaml.safe_load(p.read_text()) or {}
            if not data.get("team_roles") or not data.get("peer_review"):
                missing.append(f"{cid}: roles/peer_review")
    if missing:
        print("FAIL group projects", missing)
        return 1
    print("PASS validate-group-projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
