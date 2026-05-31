#!/usr/bin/env python3
"""Lightweight WAIKE artifact validation."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "knowledge_maps/waike_skill_tree.yaml",
    "programs/research_apprenticeship_digital_twin.md",
    "scripts/export_course_repo_map.py",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        print("FAIL missing:", missing)
        return 1
    print("PASS waike core artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
